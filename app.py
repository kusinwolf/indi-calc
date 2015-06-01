
from copy import deepcopy
import logging
import json

from flask import Flask
from flask import request

from base import MarketItem
from costs import get_next_requirement

# This is bad but a hack for now
from materials import *

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)


def get_item(name):
    """
    Finds the item object based on the string name

    :param name: Name of market item being converted to an object
    :type name: str
    :returns: Item object
        ex: "Ionic Solutions" => IonicSolutions
    :rtype: MarketItem
    :raises Exception: If the item is not found
    """
    for item in globals().values():
        if isinstance(item, MarketItem) and item.name == name:
            return item

    raise Exception("Invaid item '{}'".format(name))


def convert_payload_to_items(requirements):
    """
    Converts the incoming user payload into the required payload

    :param requirements: Incoming body of {"Item": amount}
    :type requirements: dict
    :returns: All "Item" strings convert to Item objects
        ex: {"Ionic Solutions": 3000} => {IonicSolutions: 3000}
    :rtype: dict
    """
    new_requirements = {}

    for key, value in requirements.items():
        new_requirements[deepcopy(get_item(key))] = value

    return new_requirements


def convert_to_jsonable_object(item):
    """
    Converts any object to a json string
    Examples: {IonicSoluions: 3000} => {"Ionic Solutions": 3000}
        {SomeItem: {HereItem: 3000}} => {"SomeItem": {"HereItem": 3000}}

    :param item: What ever needs conversion
    :type item: *
    :returns: jsonable object
    :rtype: *
    """
    if isinstance(item, dict):
        output = {
            convert_to_jsonable_object(key): convert_to_jsonable_object(value)
            for key, value in item.items()
        }

    elif isinstance(item, list):
        output = [
            convert_to_jsonable_object(x) for x in item
        ]

    elif isinstance(item, tuple):
        output = (
            convert_to_jsonable_object(x) for x in item
        )

    elif isinstance(item, MarketItem):
        output = str(item)

    else:
        output = item

    return output


def filter_requirements(input_filter, requirements):
    """
        Only returns the key, value pairs requested

        :param input_filter: List, tuple, or dictionary of Items to filter by
        :type input_filter: List/tuple/dict
        :param requirements: Dictionary of all calcuated requirements
            :see get_next_requirement:
        :type requirements: dict
        :returns: Filtered requirements
        :rtype: dict
    """
    if not input_filter:
        return deepcopy(requirements)

    return {
        key: value
        for key, value in requirements.items()
        if key in input_filter
    }


def handle_exception(function):
    """
    Decorator for handling logging and HTTP response code conversion

    :param function: Any function having handling performed for, always a
        routed function
    :type function: func
    :returns: wrapped function
    :rtype: func
    """
    def inner(*args, **kwargs):
        """
        Runs the entered function, logs any errors then processes response code

        :param args: Poistional arguments
        :type args: list/tuple
        :param kwargs: Keyword arguments
        :type kwargs: dict
        :returns: function's results
        :rtype: *
        """
        try:
            return function(*args, **kwargs)
        except Exception as error:
            LOGGER.error("Exception: {}".format(error))
            return json.dumps({"status": 500, "body": "Internal exception :("})

    return inner


# http://flask.pocoo.org/docs/0.10/quickstart/#routing

@app.route("/")
def hello():
    page = """
    Good evening!<br/>
    <br/>
    Glad you could make it, would you like to know how much an
    item costs to make? Glad you asked! You have API access to getting
    calculations for any manufacturable item in game!<br/>
    (*Ahem* working on filling out the tables with everything available)<br/>
    <br/>
    <br/>
    Available endpoints<br/>
    GET to:<br/>
    http://104.130.216.45:5000/cost/Item%20Name<br/>
    http://104.130.216.45:5000/cost/Item%20Name/AmountDesired<br/>
    http://104.130.216.45:5000/cost/Item%20Name/AmountDesired/HowFarDownTheRequirementsTreeTogo<br/>
    <br/>
    POST to http://104.130.216.45:5000/cost<br/>
    Payload:<br/>
    - Required: {"item": "Item Name"}<br/>
    - Available: {
        "item": "Item Name",
        "depth": int,
        "amount": int,
        "filter_by": {"Item Name": amount_on_hand},
        "blueprints": {
            "Item Name": {"material_efficiency": int, "time_efficiency": int},
            ..
        }
    }<br/>
    Headers: {"Content-Type": "application/json", "accept": "application/json"}
    <br/>
    Returns: {
        "item": "Item Name",
        "produces": number_of_items_produced,
        "requirements": {"Item": amount_required, ..},
        "time_required": time_to_produce_in_seconds
    }<br/>
    <br/>
    Defaults:<br/>
    - Depth: -1<br/>
    - Amount: 1<br/>
    - Item: None<br/>
    <br/>
    Here is what we have to offer right now:<br/>
    <br/>
    <a href="http://104.130.216.45:5000/cost/Caldari%20Fuel%20Block">
        1 run of Caldari Fuel Blocks</a><br/>
    <a href="http://104.130.216.45:5000/cost/Caldari%20Fuel%20Block/40">
        40 runs of Caldari Fuel Blocks</a><br/>
    <a href="http://104.130.216.45:5000/cost/Caldari%20Fuel%20Block/40/0">
        40 runs of Caldari Fuel Blocks with only the top node requirements</a>
    <br/>
    <br/>
    Other Available Items:<br/>
    """

    market_items = sorted(
        [item for item in globals().values() if isinstance(item, MarketItem)],
        key=lambda x: x.name
    )

    page = page + "<br/>".join([
        """<a href="{}{}">{}</a>""".format(
            "http://104.130.216.45:5000/cost/",
            item.name.replace(" ", "%20"),
            item.name
        )
        for item in market_items
    ])

    return page


# @handle_exception
@app.route("/cost", methods=["POST"])
def cost_handler():
    """
    Finds the shopping list costs for a given item

    :param item: Which item to get a shopping list for
    :type item: str
    :param amount: How many to produce
    :type amount: int
    :param filter_by: Filter requirements down to provided materials, subtract
        the provided amount from the requirements
        ex: {"Item": amount_on_hand}
    :type filter_by: dict
    :param blueprints: Current blueprints on hand with their ME & TE values
        ex: {"Item": {
                "material_efficiency": me_level, "time_efficiency": te_level
            }}
    :type blueprints: dict
    :param depth: How far down the requirements tree to go
        -1 Go till end of all requirements -- Default
        0 Stop at the head node
        n Go till n == 0
    :type depth: int
    :returns: Shopping list of all materials required to make said item
    :rtype: dict
    """
    data = request.get_json() or {}

    item = deepcopy(get_item(
        data.get("item", "Caldari Fuel Block")
    ))

    blueprints = convert_payload_to_items(data.get("blueprints", {}))

    requirements = get_next_requirement(
        item,
        number_of_runs=data.get("amount", 1),
        depth=data.get("depth", -1),
        blueprints=blueprints
    )

    filtered_requirements = filter_requirements(
        convert_payload_to_items(data.get("filter_by", {})), requirements
    )

    output = {
        "item": str(item),
        "produces": item.produces * data.get("amount", 1),
        "requirements": filtered_requirements,
        "time_required": item.processing_time * (
            1.0 - (data.get("time_efficiency", 0) / 100.0)
        ) * data.get("amount", 1)
    }

    return json.dumps(convert_to_jsonable_object(output))


# @handle_exception
@app.route("/cost/<name>", methods=["GET"])
@app.route("/cost/<name>/<int:amount>", methods=["GET"])
@app.route("/cost/<name>/<int:amount>/<depth>", methods=["GET"])
def cost_get_handler(name=None, amount=1, depth=-1):
    """
    Finds the shopping list costs for a given item

    :param name: Which item to get a shopping list for
    :type name: str
    :param amount: How many to produce
    :type amount: int
    :param depth: How deep to go for the shopping list
    :type depth: int
    :returns: Shopping list of all materials required to make said item
    :rtype: dict
    """
    depth = int(depth)

    return json.dumps(convert_to_jsonable_object(get_next_requirement(
        get_item(name) * amount,
        depth=depth
    )))

if __name__ == "__main__":
    app.debug = True
    app.run(host="104.130.216.45")

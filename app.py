import logging
import json

from flask import Flask
from flask import request

from base import MarketItem
from costs import convert_to_jsonable_object
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
        new_requirements[get_item(key)] = value

    return new_requirements


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
        "body": {"Item Name": int}
        "show_only_provided": boolean
    }<br/>
    Headers: {"Content-Type": "application/json", "accept": "application/json"}
    <br/>
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
    :param show_only_provided: Given the provided list, only return data for
        that fills that list.
        ex: {"Ionic Solutions": 0} => {"Ionic Solutions": 6000}
    :type show_only_provided: boolean
    :param body: Provided materials, or materials you only want to see returned
        ex: {"Item": amount}
        :see show_only_provided:
    :type body: dict
    :param depth: How far down the requirements tree to go
        -1 Go till end of all requirements -- Default
        0 Stop at the head node
        n Go till n == 0
    :type depth: int
    :returns: Shopping list of all materials required to make said item
    :rtype: dict
    """
    data = request.get_json() or {}

    item = get_item(
        data.get("item", "Caldari Fuel Block")
    )

    requirements = get_next_requirement(
        item,
        material_efficiency=data.get("material_efficiency", 0),
        time_efficiency=data.get("time_efficiency", 0),
        number_of_runs=data.get("amount", 1),
        limit_to_input_keys_only=data.get("show_only_provided", False),
        requirements=convert_payload_to_items(data.get("body", {})),
        depth=data.get("depth", -1)
    )

    output = {
        "item": str(item),
        "produces": item.produces,
        "requirements": requirements
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

    return json_dumps(get_next_requirement(
        get_item(name) * amount,
        depth=depth
    ))

if __name__ == "__main__":
    app.debug = True
    app.run(host="104.130.216.45")

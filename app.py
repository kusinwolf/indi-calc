import logging
import json

from flask import Flask
from flask import request

from base import MarketItem
from costs import json_dumps
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
@handle_exception
@app.route("/cost", methods=["POST"])
def cost_handler():
    """
    Finds the shopping list costs for a given item

    :param item: Which item to get a shopping list for
    :type item: str
    :param amount: How many to produce
    :type amount: int
    :param show_only_requested: Given the provided list, only return data for
        that fills that list.
        ex: {"Ionic Solutions": 0} => {"Ionic Solutions": 6000}
    :type show_only_requested: boolean
    :param body: Provided materials, or materials you only want to see returned
        ex: {"Item": amount}
        :see show_only_requested:
    :type body: dict
    :param depth: How far down the requirements tree to go
        -1 Go till end of all requirements -- Default
        0 Stop at the head node
        n Go till n == 0
    :type depth: int
    """
    data = request.get_json()

    return json_dumps(get_next_requirement(
        get_item(data.get("item", "")) * data.get("amount", 1),
        limit_to_input_keys_only=data.get(
            "show_only_requested", False
        ),
        requirements=convert_payload_to_items(data.get("body", {})),
        depth=data.get("depth", -1)
    ))


if __name__ == "__main__":
    app.debug = True
    app.run()

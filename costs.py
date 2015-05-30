
from copy import deepcopy
import json
import math

from base import Manufacturable
from base import MarketItem


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


def extend(left, right):
    new_dict = deepcopy(left)

    for key, value in right.items():
        if key not in new_dict:
            new_dict[key] = value

    return new_dict


def get_next_requirement(
    item, material_efficiency=0, time_efficiency=0, number_of_runs=1,
    requirements={}, limit_to_input_keys_only=False, depth=0
):
    """
        Returns a shopping list requirement of all materials needed to produce
        the item in question (till depth is reached)

        :param item: Item that is a requirement
        :type item: MarketItem
        :param material_efficiency: Level of material efficiency researched
            [0 -> 10]
        :type material_efficiency: int
        :param time_efficiency: Level of time efficiency researched
            [0 -> 20, 2]
        :type time_efficiency: int
        :param number_of_runs: How many runs to do in order to complete the job
        :type number_of_runs: int
        :param requirements: What does it take to make this?
            {MarketItem: amount}
        :type requirements: dict
        :param limit_to_input_keys_only: Should only the keys found in
            requirements be allowed to be set?
            True: Only input keys are allowed to be set
            False: All keys are filled
        :type limit_to_input_keys_only: boolean
        :param depth: How far down to go the requirements list
            -1 goes till end
            0 stops item.requirements
            n goes till n == 0
        :type depth: int
    """

    # Prevents a memory leak from happening if someone does not provide a dict
    requirements = deepcopy(requirements)
    new_item = deepcopy(item)

    new_item.set_material_efficiency(material_efficiency=material_efficiency)
    new_item.set_time_efficiency(time_efficiency=time_efficiency)

    for sub_item, amount in new_item.requirements.items():
        amount *= number_of_runs
        if (
            isinstance(sub_item, Manufacturable) and
            sub_item.requirements != {} and
            depth != 0
        ):
            requirements = extend(requirements, get_next_requirement(
                sub_item,
                number_of_runs=math.ceil(
                    float(amount) / float(sub_item.produces)
                ),
                requirements=requirements,
                limit_to_input_keys_only=limit_to_input_keys_only,
                depth=depth-1
            ))

        if limit_to_input_keys_only:
            if sub_item in requirements:
                requirements[sub_item] += amount
        else:
            requirements.setdefault(sub_item, 0)
            requirements[sub_item] += amount

    return requirements

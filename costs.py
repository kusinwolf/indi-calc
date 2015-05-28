import math

from pprint import pprint

from base import Manufacturable
from materials import CaldariFuelBlocks

from materials import IonicSolutions
from materials import ConsumerElectronics

number_of_large_towers = 10

required_fuel = CaldariFuelBlocks * number_of_large_towers


def get_next_requirement(
    item, number_of_runs=1, requirements={}, limit_to_input_keys_only=False,
    depth=0
):
    """
        Returns a shopping list requirement of all materials needed to produce
        the item in question (till depth is reached)

        :param item: Item that is a requirement
        :type item: MarketItem
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

    for sub_item, amount in item.requirements.items():
        amount *= number_of_runs
        if (
            isinstance(sub_item, Manufacturable) and
            sub_item.requirements != {} and
            depth != 0
        ):
            get_next_requirement(
                sub_item,
                number_of_runs=math.ceil(amount / sub_item.produces),
                requirements=requirements,
                limit_to_input_keys_only=limit_to_input_keys_only,
                depth=depth-1
            )

        if limit_to_input_keys_only:
            if sub_item in requirements:
                requirements[sub_item] += amount
        else:
            requirements.setdefault(sub_item, 0)
            requirements[sub_item] += amount

    return requirements

all_materials_required = {
    IonicSolutions: 0,
    ConsumerElectronics: 0
}

get_next_requirement(
    CaldariFuelBlocks * 40,
    requirements=all_materials_required,
    limit_to_input_keys_only=True,
    depth=-1
)
pprint(all_materials_required)

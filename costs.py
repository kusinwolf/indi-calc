
from copy import deepcopy
import math

from base import Manufacturable


def get_next_requirement(
    item, number_of_runs=1, requirements={}, depth=0, blueprints={}
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
        :param depth: How far down to go the requirements list
            -1 goes till end
            0 stops item.requirements
            n goes till n == 0
        :type depth: int
        :param blueprints: Material/Time efficiency values for given blueprints
        :type blueprints: dict
    """

    # Prevents a memory leak from happening if someone does not provide a dict
    requirements = deepcopy(requirements)

    if item in blueprints:
        item.set_material_efficiency(
            material_efficiency=blueprints[item].get("material_efficiency", 0)
        )
        item.set_time_efficiency(
            time_efficiency=blueprints[item].get("time_efficiency", 0)
        )

    for sub_item, amount in item.requirements.items():
        amount *= number_of_runs
        if (
            isinstance(sub_item, Manufacturable) and
            sub_item.requirements != {} and
            depth != 0
        ):
            requirements = get_next_requirement(
                sub_item,
                number_of_runs=math.ceil(
                    float(amount) / float(sub_item.produces)
                ),
                requirements=requirements,
                depth=depth-1,
                blueprints=blueprints
            )

        requirements.setdefault(sub_item, 0)
        requirements[sub_item] += amount

    return requirements

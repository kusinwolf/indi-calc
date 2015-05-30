""" I feel as though I'm over doing this o_o """
from copy import deepcopy
import math


class MarketItem(object):
    def __init__(self, jita_price=0.0, zero_zero_price=0.0, name=None):
        """
        :param jita_price: Price at said location
        :type jita_price: float
        :param zero_zero_price: Price at said location
        :type zero_zero_price: float
        """
        self.jita_price = jita_price
        self.zero_zero_price = zero_zero_price
        self.name = name

    def __repr__(self):
        """
        :returns: Basic structure of stringing this object
        :rtype: str
        """
        return "<{}: '{}'>".format(
            self.__class__.__name__, self.name
        )

    def __hash__(self):
        """
        :returns: Hashed self.name
        :rtype: hash
        """
        return self.name.lower().__hash__()

    def __eq__(self, other):
        """
        :returns: Compares self and other via name
        :rtype: boolean
        """
        return self.name == other.name

    def __str__(self):
        """
        :returns: String representation of the object
        :rtype: str
        """
        return self.name


class Manufacturable(MarketItem):
    def __init__(
        self, requirements={}, produces=0, processing_time=0,
        material_efficiency=0, time_efficiency=0, *args, **kwargs
    ):
        """
        Blueprint original, copy, or planetary factory

        :param requirements: What items are required to produce at 0 ME
            {Item: Amount}
        :type requirements: dict
        :param produces: How many items are produced from one run
        :type produces: int
        :param processing_time: Time in seconds for how long it takes at 0 TE
        :type processing_time: int
        :param material_efficiency: Level of material efficiency researched
            [0 -> 10]
        :type material_efficiency: int
        :param time_efficiency: Level of time efficiency researched
            [0 -> 20, 2]
        :type time_efficiency: int
        """
        self.material_efficiency = material_efficiency
        self.time_efficiency = time_efficiency
        self.requirements = deepcopy(requirements)
        self.processing_time = processing_time
        self.produces = produces

        self.set_material_efficiency(material_efficiency=material_efficiency)
        self.set_time_efficiency(time_efficiency=time_efficiency)

        super(Manufacturable, self).__init__(*args, **kwargs)

    def set_material_efficiency(self, material_efficiency):
        """
        :param material_efficiency: What is the ME level of this blueprint
            [0 -> 10]
        :type material_efficiency: int
        """
        self.material_efficiency = material_efficiency

        for item, amount in self.requirements.items():
            self.requirements[item] = math.ceil(
                amount * (1.0 - (material_efficiency / 100.0))
            )

    def set_time_efficiency(self, time_efficiency):
        """
        :param time_efficiency: What is the TE level of this blueprint
            [0 -> 20, 2]
        :type time_efficiency: int
        """
        self.time_efficiency = time_efficiency
        self.processing_time = self.processing_time * (
            1.0 - (time_efficiency / 100.0)
        )

    def __mul__(self, multiplier):
        """
        :param multiplier: What to mulitple this item by
        :type multiplier: int
        :returns: New Manufacturable object multipled by multiplier
        :rtype: Manufacturable
        """
        new_object = deepcopy(self)

        new_object.processing_time = new_object.processing_time * multiplier

        for key, value in new_object.requirements.items():
            new_object.requirements[key] = (value * multiplier)

        return new_object


class PlanetaryInteractionMaterial(Manufacturable):
    def __init__(
        self, base_import_export_fee=0.0, tax_rate=1.02, *args, **kwargs
    ):
        """
        Basically a blueprint original or copy

        :param base_import_export_fee: How much is the base cost to
            import/export the materials
        :type base_import_export_fee: float
        :param tax_rate: What is the tax rate set by the owner
        :type tax_rate: float
        """
        self.base_import_export_fee = base_import_export_fee
        self.tax_rate = tax_rate
        super(PlanetaryInteractionMaterial, self).__init__(*args, **kwargs)

    def get_export_fee(self):
        """
        :returns: Calculated export tax of goods
        :rtype: float
        """
        return self.base_import_export_fee * self.tax_rate * 1.5

    def get_import_fee(self):
        """
        :returns: Calculated import tax of goods
        :rtype: float
        """
        return self.base_import_export_fee * self.tax_rate * 0.5


class RawMaterial(PlanetaryInteractionMaterial):
    def __init__(self, *args, **kwargs):
        """
        :param args: Position arguments used for super class
        :type args: list/tuple
        :param kwargs: Keyword arguments used for super class
        :type kwargs: dict
        """
        super(RawMaterial, self).__init__(
            base_import_export_fee=4.0,
            processing_time=0,
            produces=1,
            *args,
            **kwargs
        )


class ProcessedMaterials(PlanetaryInteractionMaterial):
    def __init__(self, *args, **kwargs):
        """
        :param args: Position arguments used for super class
        :type args: list/tuple
        :param kwargs: Keyword arguments used for super class
        :type kwargs: dict
        """
        super(ProcessedMaterials, self).__init__(
            base_import_export_fee=400.0,
            processing_time=30 * 60,
            produces=20,
            *args,
            **kwargs
        )


class RefinedCommodities(PlanetaryInteractionMaterial):
    def __init__(self, *args, **kwargs):
        """
        :param args: Position arguments used for super class
        :type args: list/tuple
        :param kwargs: Keyword arguments used for super class
        :type kwargs: dict
        """
        super(RefinedCommodities, self).__init__(
            base_import_export_fee=7200.0,
            processing_time=60 * 60,
            produces=5,
            *args,
            **kwargs
        )


class SpecializedCommodities(PlanetaryInteractionMaterial):
    def __init__(self, *args, **kwargs):
        """
        :param args: Position arguments used for super class
        :type args: list/tuple
        :param kwargs: Keyword arguments used for super class
        :type kwargs: dict
        """
        super(SpecializedCommodities, self).__init__(
            base_import_export_fee=60000.0,
            processing_time=60 * 60,
            produces=3,
            *args,
            **kwargs
        )


class AdvancedCommodities(PlanetaryInteractionMaterial):
    def __init__(self, *args, **kwargs):
        """
        :param args: Position arguments used for super class
        :type args: list/tuple
        :param kwargs: Keyword arguments used for super class
        :type kwargs: dict
        """
        super(AdvancedCommodities, self).__init__(
            base_import_export_fee=1200000.0,
            processing_time=60 * 60,
            produces=1,
            *args,
            **kwargs
        )

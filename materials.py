
from base import AdvancedCommodities
from base import Manufacturable
from base import MarketItem
from base import ProcessedMaterials
from base import RawMaterial
from base import RefinedCommodities
from base import SpecializedCommodities


# (T0) Raw Materials
AqueousLiquids = RawMaterial(name="Aqueous Liquids")
BaseMetals = RawMaterial(name="Base Metals")
ComplexOrganisms = RawMaterial(name="Complex Organisms")
HeavyMetals = RawMaterial(name="Heavy Metals")
MicroOrganisms = RawMaterial(name="Micro Organisms")
NobleMetals = RawMaterial(name="Noble Metals")
PlankticColonies = RawMaterial(name="Planktic Colonies")
SuspendedPlasma = RawMaterial(name="Suspended Plasma")
Autotrophs = RawMaterial(name="Autotrophs")
CarbonCompounds = RawMaterial(name="Carbon Compounds")
FelsicMagma = RawMaterial(name="Felsic Magma")
IonicSolutions = RawMaterial(name="Ionic Solutions")
NobleGas = RawMaterial(name="Noble Gas")
NonCSCrystals = RawMaterial(name="Non-CS Crystals")
ReactiveGas = RawMaterial(name="Reactive Gas")

# (T1)  Processed Materials
Bacteria = ProcessedMaterials(
    requirements={MicroOrganisms: 3000}, name="Bacteria"
)
Biofuels = ProcessedMaterials(
    requirements={CarbonCompounds: 3000}, name="Biofuels"
)
Biomass = ProcessedMaterials(
    requirements={PlankticColonies: 3000}, name="Biomass"
)
ChiralStructures = ProcessedMaterials(
    requirements={NonCSCrystals: 3000}, name="Chiral Structures"
)
Electrolytes = ProcessedMaterials(
    requirements={IonicSolutions: 3000}, name="Electrolytes"
)
IndustrialFibers = ProcessedMaterials(
    requirements={Autotrophs: 3000}, name="Industrial Fibers"
)
OxidizingCompound = ProcessedMaterials(
    requirements={ReactiveGas: 3000}, name="Oxidizing Compound"
)
Oxygen = ProcessedMaterials(
    requirements={NobleGas: 3000}, name="Oxygen"
)
Plasmoids = ProcessedMaterials(
    requirements={SuspendedPlasma: 3000}, name="Plasmoids"
)
PreciousMetals = ProcessedMaterials(
    requirements={NobleMetals: 3000}, name="Precious Metals"
)
Proteins = ProcessedMaterials(
    requirements={ComplexOrganisms: 3000}, name="Proteins"
)
ReactiveMetals = ProcessedMaterials(
    requirements={BaseMetals: 3000}, name="Reactive Metals"
)
Silicon = ProcessedMaterials(
    requirements={FelsicMagma: 3000}, name="Silicon"
)
ToxicMetals = ProcessedMaterials(
    requirements={HeavyMetals: 3000}, name="Toxic Metals"
)
Water = ProcessedMaterials(
    requirements={AqueousLiquids: 3000}, name="Water"
)

# (T2)  Refined Commodities
Biocells = RefinedCommodities(
    requirements={Biofuels: 20, PreciousMetals: 20}, name="Biocells"
)
ConstructionBlocks = RefinedCommodities(
    requirements={ReactiveMetals: 20, ToxicMetals: 20},
    name="Construction Blocks"
)
ConsumerElectronics = RefinedCommodities(
    requirements={ToxicMetals: 20, ChiralStructures: 20},
    name="Consumer Electronics"
)
Coolant = RefinedCommodities(
    requirements={Electrolytes: 20, Water: 20}, name="Coolant"
)
EnrichedUranium = RefinedCommodities(
    requirements={PreciousMetals: 20, ToxicMetals: 20},
    name="Enriched Uranium"
)
Fertilizer = RefinedCommodities(
    requirements={Bacteria: 20, Proteins: 20}, name="Fertilizer"
)
GeneticallyEnhancedLivestock = RefinedCommodities(
    requirements={Proteins: 20, Biomass: 20},
    name="Genetically Enhanced Livestock"
)
Livestock = RefinedCommodities(
    requirements={Proteins: 20, Biofuels: 20}, name="Livestock"
)
MechanicalParts = RefinedCommodities(
    requirements={ReactiveMetals: 20, PreciousMetals: 20},
    name="Mechanical Parts"
)
MicrofiberShielding = RefinedCommodities(
    requirements={IndustrialFibers: 20, Silicon: 20},
    name="Microfiber Shielding"
)
MiniatureElectronics = RefinedCommodities(
    requirements={ChiralStructures: 20, Silicon: 20},
    name="Miniature Electronics"
)
Nanites = RefinedCommodities(
    requirements={Bacteria: 20, ReactiveMetals: 20}, name="Nanites"
)
Oxides = RefinedCommodities(
    requirements={OxidizingCompound: 20, Oxygen: 20}, name="Oxides"
)
Polyaramids = RefinedCommodities(
    requirements={OxidizingCompound: 20, IndustrialFibers: 20},
    name="Polyaramids"
)
Polytextiles = RefinedCommodities(
    requirements={Biofuels: 20, IndustrialFibers: 20},
    name="Polytextiles"
)
RocketFuel = RefinedCommodities(
    requirements={Plasmoids: 20, Electrolytes: 20},
    name="Rocket Fuel"
)
SilicateGlass = RefinedCommodities(
    requirements={OxidizingCompound: 20, Silicon: 20},
    name="Silicate Glass"
)
Superconductors = RefinedCommodities(
    requirements={Plasmoids: 20, Water: 20},
    name="Superconductors"
)
SupertensilePlastics = RefinedCommodities(
    requirements={Oxygen: 20, Biomass: 20},
    name="Supertensile Plastics"
)
SyntheticOil = RefinedCommodities(
    requirements={Electrolytes: 20, Oxygen: 20},
    name="Synthetic Oil"
)
TestCultures = RefinedCommodities(
    requirements={Bacteria: 20, Water: 20},
    name="Test Cultures"
)
Transmitter = RefinedCommodities(
    requirements={Plasmoids: 20, ChiralStructures: 20},
    name="Transmitter"
)
ViralAgent = RefinedCommodities(
    requirements={Bacteria: 20, Biomass: 20},
    name="Viral Agent"
)
WaterCooledCPU = RefinedCommodities(
    requirements={ReactiveMetals: 20, Water: 20},
    name="Water Cooled CPU"
)

# (T3)  Specialized Commodities
BiotechResearchReports = SpecializedCommodities(
    requirements={Nanites: 10, Livestock: 10, ConstructionBlocks: 10},
    name="Biotech Research Reports"
)
CameraDrones = SpecializedCommodities(
    requirements={SilicateGlass: 10, RocketFuel: 10},
    name="Camera Drones"
)
Condensates = SpecializedCommodities(
    requirements={Oxides: 10, Coolant: 10},
    name="Condensates"
)
CryoprotectantSolution = SpecializedCommodities(
    requirements={TestCultures: 10, SyntheticOil: 10, Fertilizer: 10},
    name="Cryoprotectant Solution"
)
DataChips = SpecializedCommodities(
    requirements={SupertensilePlastics: 10, MicrofiberShielding: 10},
    name="Data Chips"
)
GelMatrixBiopaste = SpecializedCommodities(
    requirements={Oxides: 10, Biocells: 10, Superconductors: 10},
    name="Gel Matrix Biopaste"
)
GuidanceSystems = SpecializedCommodities(
    requirements={WaterCooledCPU: 10, Transmitter: 10},
    name="Guidance Systems"
)
HazmatDetectionSystems = SpecializedCommodities(
    requirements={Polytextiles: 10, ViralAgent: 10, Transmitter: 10},
    name="Hazmat Detection Systems"
)
HermeticMembranes = SpecializedCommodities(
    requirements={Polyaramids: 10, GeneticallyEnhancedLivestock: 10},
    name="Hermetic Membranes"
)
HighTechTransmitters = SpecializedCommodities(
    requirements={Polyaramids: 10, Transmitter: 10},
    name="High Tech Transmitters"
)
IndustrialExplosives = SpecializedCommodities(
    requirements={Fertilizer: 10, Polytextiles: 10},
    name="Industrial Explosives"
)
Neocoms = SpecializedCommodities(
    requirements={Biocells: 10, SilicateGlass: 10}, name="Neocoms"
)
NuclearReactors = SpecializedCommodities(
    requirements={EnrichedUranium: 10, MicrofiberShielding: 10},
    name="Nuclear Reactors"
)
PlanetryVehicles = SpecializedCommodities(
    requirements={
        SupertensilePlastics: 10, MechanicalParts: 10, MiniatureElectronics: 10
    },
    name="Planetry Vehicles"
)
Robotics = SpecializedCommodities(
    requirements={MechanicalParts: 10, ConsumerElectronics: 10},
    name="Robotics"
)
SmartfabUnits = SpecializedCommodities(
    requirements={ConstructionBlocks: 10, MiniatureElectronics: 10},
    name="Smartfab Units"
)
Supercomputers = SpecializedCommodities(
    requirements={WaterCooledCPU: 10, Coolant: 10, ConsumerElectronics: 10},
    name="Supercomputers"
)
SyntheticSynapses = SpecializedCommodities(
    requirements={SupertensilePlastics: 10, TestCultures: 10},
    name="Synthetic Synapses"
)
TranscranialMicorcontrollers = SpecializedCommodities(
    requirements={Biocells: 10, Nanites: 10},
    name="Transcranial Micorcontrollers"
)
UkomiSuperconductors = SpecializedCommodities(
    requirements={SyntheticOil: 10, Superconductors: 10},
    name="Ukomi Superconductors"
)
Vaccines = SpecializedCommodities(
    requirements={Livestock: 10, ViralAgent: 10},
    name="Vaccines"
)

# (T4) Advanced Commodities
BroadcastNode = AdvancedCommodities(
    requirements={Neocoms: 6, DataChips: 6, HighTechTransmitters: 6},
    name="Broadcast Node"
)
IntegrityResponseDrones = AdvancedCommodities(
    requirements={
        GelMatrixBiopaste: 6, HazmatDetectionSystems: 6, PlanetryVehicles: 6
    },
    name="Integrity Response Drones"
)
NanoFactory = AdvancedCommodities(
    requirements={
        IndustrialExplosives: 6, ReactiveMetals: 40, UkomiSuperconductors: 6
    },
    name="Nano Factory"
)
OrganicMortarApplicators = AdvancedCommodities(
    requirements={Condensates: 6, Bacteria: 40, Robotics: 6},
    name="Organic Mortar Applicators"
)
RecursiveComputingModule = AdvancedCommodities(
    requirements={
        SyntheticSynapses: 6,
        GuidanceSystems: 6,
        TranscranialMicorcontrollers: 6
    },
    name="Recursive Computing Module"
)
SelfHarmonizingPowerCore = AdvancedCommodities(
    requirements={CameraDrones: 6, NuclearReactors: 6, HermeticMembranes: 6},
    name="Self Harmonizing Power Core"
)
SterileConduits = AdvancedCommodities(
    requirements={SmartfabUnits: 6, Water: 40, Vaccines: 6},
    name="Sterile Conduits"
)
WetwareMainframe = AdvancedCommodities(
    requirements={
        Supercomputers: 6, BiotechResearchReports: 6, CryoprotectantSolution: 6
    },
    name="Wetware Mainframe"
)

# Ice
HeavyWater = MarketItem(name="Heavy Water")
LiquidOzone = MarketItem(name="Liquid Ozone")
NitrogenIsotopes = MarketItem(name="Nitrogen Isotopes")


# Items
CaldariFuelBlocks = Manufacturable(
    requirements={
        EnrichedUranium: 4,
        Oxygen: 22,
        MechanicalParts: 4,
        Coolant: 9,
        Robotics: 1,
        HeavyWater: 167,
        LiquidOzone: 167,
        NitrogenIsotopes: 444
    },
    produces=40,
    processing_time=15 * 60,
    name="Caldari Fuel Block"
)

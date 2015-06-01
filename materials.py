
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
HeliumIsotopes = MarketItem(name="Helium Isotopes")
OxygenIsotopes = MarketItem(name="Oxygen Isotopes")
HydrogenIsotopes = MarketItem(name="Hydrogen Isotopes")

# Minerals
Tritanium = MarketItem(name="Tritanium")
Pyerite = MarketItem(name="Pyerite")
Mexallon = MarketItem(name="Mexallon")
Nocxium = MarketItem(name="Nocxium")
Isogen = MarketItem(name="Isogen")
Zydrine = MarketItem(name="Zydrine")
Megacyte = MarketItem(name="Megacyte")
Morphite = MarketItem(name="Morphite")

# Fuel Blocks
CaldariFuelBlock = Manufacturable(
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

AmarrFuelBlock = Manufacturable(
    requirements={
        EnrichedUranium: 4,
        Oxygen: 22,
        MechanicalParts: 4,
        Coolant: 9,
        Robotics: 1,
        HeavyWater: 167,
        LiquidOzone: 167,
        HeliumIsotopes: 444
    },
    produces=40,
    processing_time=15 * 60,
    name="Amarr Fuel Block"
)

GallenteFuelBlock = Manufacturable(
    requirements={
        EnrichedUranium: 4,
        Oxygen: 22,
        MechanicalParts: 4,
        Coolant: 9,
        Robotics: 1,
        HeavyWater: 167,
        LiquidOzone: 167,
        OxygenIsotopes: 444
    },
    produces=40,
    processing_time=15 * 60,
    name="Gallente Fuel Block"
)

MinmatarFuelBlock = Manufacturable(
    requirements={
        EnrichedUranium: 4,
        Oxygen: 22,
        MechanicalParts: 4,
        Coolant: 9,
        Robotics: 1,
        HeavyWater: 167,
        LiquidOzone: 167,
        HydrogenIsotopes: 444
    },
    produces=40,
    processing_time=15 * 60,
    name="Minmatar Fuel Block"
)

# NPC Market Items
ElectronicParts = MarketItem(name="Electronic Parts")

# Items
SamllTractorBeamI = Manufacturable(
    requirements={
        Tritanium: 27778,
        Pyerite: 12222,
        Mexallon: 10000,
        Isogen: 2778,
        Nocxium: 389,
        Zydrine: 164,
        Megacyte: 88
    },
    produces=1,
    processing_time=15 * 60,
    name="Samll Tractor Beam I"
)

WarpScramblerI = Manufacturable(
    requirements={
        Tritanium: 502,
        Pyerite: 297,
        Mexallon: 334,
        Isogen: 197,
        Zydrine: 4
    },
    produces=1,
    processing_time=30 * 60,
    name="Warp Scrambler I"
)

# Capital Construction Components
CapitalConstructionParts = Manufacturable(
    requirements={
        Tritanium: 388208,
        Pyerite: 93777,
        Mexallon: 37729,
        Isogen: 5104,
        Nocxium: 1530,
        Zydrine: 538,
        Megacyte: 212
    },
    produces=1,
    processing_time=4 * 60 * 60 + 26 * 60 + 40,
    name="Capital Construction Parts"
)

# Structures
MobileCynosuralInhibitor = Manufacturable(
    requirements={
        BroadcastNode: 4,
        OrganicMortarApplicators: 9,
        SelfHarmonizingPowerCore: 2,
        SterileConduits: 4,
        WetwareMainframe: 2,
        GuidanceSystems: 22,
        Tritanium: 277778,
        Pyerite: 11111,
        Isogen: 5556,
        Zydrine: 11112,
        Megacyte: 1112
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Mobile Cynosural Inhibitor"
)

MobileDepot = Manufacturable(
    requirements={
        SmartfabUnits: 3,
        NuclearReactors: 1,
        GuidanceSystems: 3,
        HighTechTransmitters: 1,
        Tritanium: 5556,
        Pyerite: 222,
        Zydrine: 444
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Mobile Depot"
)

MobileMicroJumpUnit = Manufacturable(
    requirements={
        SmartfabUnits: 3,
        NuclearReactors: 2,
        GuidanceSystems: 4,
        HighTechTransmitters: 2,
        Tritanium: 11111,
        Pyerite: 556,
        Zydrine: 1112
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Mobile Micro Jump Unit"
)

MobileScanInhibitor = Manufacturable(
    requirements={
        SmartfabUnits: 11,
        BroadcastNode: 7,
        WetwareMainframe: 3,
        Tritanium: 22222,
        Pyerite: 1111,
        Isogen: 1111,
        Zydrine: 2222
    },
    produces=1,
    processing_time=5 * 60 * 60,
    name="Mobile Scan Inhibitor"
)

SmallMobileHybridSiphonUnit = Manufacturable(
    requirements={
        GuidanceSystems: 100,
        MiniatureElectronics: 100,
        DataChips: 12,
        Tritanium: 238813,
        Pyerite: 34527,
        Mexallon: 20957,
        Isogen: 6611,
        Nocxium: 1919,
        Zydrine: 1260,
        Megacyte: 382
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Small Mobile 'Hybrid' Siphon Unit"
)

SmallMobileRoteSiphonUnit = Manufacturable(
    requirements={
        GuidanceSystems: 100,
        MiniatureElectronics: 100,
        DataChips: 12,
        Tritanium: 251058,
        Pyerite: 35082,
        Mexallon: 21078,
        Isogen: 6611,
        Nocxium: 1986,
        Zydrine: 1294,
        Megacyte: 402
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Small Mobile 'Rote' Siphon Unit"
)

SmallMobileSiphonUnit = Manufacturable(
    requirements={
        GuidanceSystems: 100,
        MiniatureElectronics: 100,
        DataChips: 12,
        Tritanium: 238813,
        Pyerite: 34527,
        Mexallon: 20957,
        Isogen: 6611,
        Nocxium: 1919,
        Zydrine: 1260,
        Megacyte: 382
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Small Mobile Siphon Unit"
)

MobileTractorUnit = Manufacturable(
    requirements={
        SamllTractorBeamI: 1,
        OrganicMortarApplicators: 2,
        WetwareMainframe: 1,
        UkomiSuperconductors: 2,
        Zydrine: 948
    },
    produces=1,
    processing_time=1 * 60 * 60 + 40 * 60,
    name="Mobile Tractor Unit"
)

MobileSmallWarpDisruptorI = Manufacturable(
    requirements={
        Tritanium: 15992,
        Pyerite: 4923,
        Mexallon: 2237,
        Isogen: 260,
        Nocxium: 197,
        Zydrine: 166,
        Megacyte: 44,
        WarpScramblerI: 3,
        ElectronicParts: 11
    },
    produces=1,
    processing_time=25 * 60,
    name="Mobile Small Warp Disruptor I"
)

MobileMediumWarpDisruptorI = Manufacturable(
    requirements={
        Tritanium: 66979,
        Pyerite: 21476,
        Mexallon: 10952,
        Isogen: 2222,
        Nocxium: 787,
        Zydrine: 688,
        Megacyte: 178,
        WarpScramblerI: 6,
        ElectronicParts: 17
    },
    produces=1,
    processing_time=50 * 60,
    name="Mobile Medium Warp Disruptor I"
)

MobileLargeWarpDisruptorI = Manufacturable(
    requirements={
        Tritanium: 275448,
        Pyerite: 90358,
        Mexallon: 48816,
        Isogen: 11845,
        Nocxium: 3147,
        Zydrine: 2808,
        Megacyte: 712,
        WarpScramblerI: 9,
        ElectronicParts: 22
    },
    produces=1,
    processing_time=1 * 60 + 15 * 60,
    name="Mobile Large Warp Disruptor I"
)

OreProspectingArray1 = Manufacturable(
    requirements={
        BroadcastNode: 4,
        IntegrityResponseDrones: 3,
        NanoFactory: 6,
        OrganicMortarApplicators: 6,
        RecursiveComputingModule: 4,
        SelfHarmonizingPowerCore: 4,
        SterileConduits: 6,
        WetwareMainframe: 3,
        CapitalConstructionParts: 1
    },
    produces=1,
    processing_time=16 * 60 * 60 + 40 * 60,
    name="Ore Prospecting Array 1"
)

OreProspectingArray2 = Manufacturable(
    requirements={
        BroadcastNode: 6,
        IntegrityResponseDrones: 5,
        NanoFactory: 7,
        OrganicMortarApplicators: 7,
        RecursiveComputingModule: 6,
        SelfHarmonizingPowerCore: 6,
        SterileConduits: 7,
        WetwareMainframe: 5,
        CapitalConstructionParts: 2
    },
    produces=1,
    processing_time=16 * 60 * 60 + 40 * 60,
    name="Ore Prospecting Array 2"
)

OreProspectingArray3 = Manufacturable(
    requirements={
        BroadcastNode: 7,
        IntegrityResponseDrones: 5,
        NanoFactory: 11,
        OrganicMortarApplicators: 11,
        RecursiveComputingModule: 7,
        SelfHarmonizingPowerCore: 7,
        SterileConduits: 11,
        WetwareMainframe: 5,
        CapitalConstructionParts: 3
    },
    produces=1,
    processing_time=16 * 60 * 60 + 40 * 60,
    name="Ore Prospecting Array 3"
)

OreProspectingArray4 = Manufacturable(
    requirements={
        BroadcastNode: 10,
        IntegrityResponseDrones: 8,
        NanoFactory: 13,
        OrganicMortarApplicators: 13,
        RecursiveComputingModule: 13,
        SelfHarmonizingPowerCore: 10,
        SterileConduits: 13,
        WetwareMainframe: 8,
        CapitalConstructionParts: 4
    },
    produces=1,
    processing_time=16 * 60 * 60 + 40 * 60,
    name="Ore Prospecting Array 4"
)

OreProspectingArray5 = Manufacturable(
    requirements={
        BroadcastNode: 18,
        IntegrityResponseDrones: 13,
        NanoFactory: 27,
        OrganicMortarApplicators: 27,
        RecursiveComputingModule: 18,
        SelfHarmonizingPowerCore: 18,
        SterileConduits: 27,
        WetwareMainframe: 13,
        CapitalConstructionParts: 8
    },
    produces=1,
    processing_time=16 * 60 * 60 + 40 * 60,
    name="Ore Prospecting Array 5"
)

# Advanced Reaction Materials
CrystallineCarbonide = MarketItem(name="Crystalline Carbonide")
PhenolicComposites = MarketItem(name="Phenolic Composites")
Ferrogel = MarketItem(name="Ferrogel")
Nanotransistors = MarketItem(name="Nanotransistors")
HypersynapticFibers = MarketItem(name="Hypersynaptic Fibers")
PhotonicMetamaterials = MarketItem(name="Photonic Metamaterials")
SylramicFibers = MarketItem(name="Sylramic Fibers")
FermionicCondensates = MarketItem(name="Fermionic Condensates")
Fullerides = MarketItem(name="Fullerides")

# T2 Components
IonThruster = Manufacturable(
    requirements={
        CrystallineCarbonide: 13,
        PhenolicComposites: 3,
        Ferrogel: 1
    },
    produces=1,
    processing_time=2 * 60 + 30,
    name="Ion Thruster"
)

MagnetometricSensorCluster = Manufacturable(
    requirements={
        CrystallineCarbonide: 22,
        Nanotransistors: 1,
        HypersynapticFibers: 2
    },
    produces=1,
    processing_time=2 * 60 + 30,
    name="Magnetometric Sensor Cluster"
)

PhotonMicroprocessor = Manufacturable(
    requirements={
        CrystallineCarbonide: 17,
        PhenolicComposites: 6,
        Nanotransistors: 2,
        PhotonicMetamaterials: 2
    },
    produces=1,
    processing_time=1 * 60 + 15,
    name="Photon Microprocessor"
)

CrystallineCarbonideArmorPlate = Manufacturable(
    requirements={
        CrystallineCarbonide: 44,
        SylramicFibers: 11
    },
    produces=1,
    processing_time=25,
    name="Crystalline Carbonide Armor Plate"
)

FusionReactorUnit = Manufacturable(
    requirements={
        CrystallineCarbonide: 9,
        FermionicCondensates: 2
    },
    produces=1,
    processing_time=5 * 60,
    name="Fusion Reactor Unit"
)

OscillatorCapacitorUnit = Manufacturable(
    requirements={
        CrystallineCarbonide: 27,
        Fullerides: 11,
        Nanotransistors: 1,
        PhotonicMetamaterials: 2
    },
    produces=1,
    processing_time=2 * 60 + 30,
    name="Oscillator Capacitor Unit"
)

PulseShieldEmitter = Manufacturable(
    requirements={
        CrystallineCarbonide: 22,
        SylramicFibers: 9,
        Ferrogel: 1
    },
    produces=1,
    processing_time=2 * 60 + 30,
    name="Pulse Shield Emitter"
)

# RAMs
RAMStarshipTech = Manufacturable(
    requirements={
        Tritanium: 556,
        Pyerite: 444,
        Mexallon: 222,
        Isogen: 82,
        Nocxium: 36
    },
    produces=100,
    processing_time=41 * 60 + 40,
    name="R.A.M. Starship Tech"
)

# Ships
Atron = Manufacturable(
    requirements={
        Tritanium: 20556,
        Pyerite: 3889,
        Mexallon: 2222,
        Isogen: 278,
        Nocxium: 56,
        Zydrine: 12
    },
    produces=1,
    processing_time=1 * 60 * 60 + 40 * 60,
    name="Atron"
)

Ares = Manufacturable(
    requirements={
        IonThruster: 45,
        MagnetometricSensorCluster: 30,
        PhotonMicroprocessor: 120,
        CrystallineCarbonideArmorPlate: 450,
        FusionReactorUnit: 5,
        OscillatorCapacitorUnit: 75,
        PulseShieldEmitter: 23,
        Morphite: 8,
        ConstructionBlocks: 15,
        Atron: 1,
        RAMStarshipTech: 1
    },
    produces=1,
    processing_time=1 * 24 * 60 * 60 + 9 * 60 * 60 + 20 * 60,
    name="Ares"
)

Vexor = Manufacturable(
    requirements={
        Tritanium: 622222,
        Pyerite: 133333,
        Mexallon: 41111,
        Isogen: 10111,
        Nocxium: 2889,
        Zydrine: 1312,
        Megacyte: 356
    },
    produces=1,
    processing_time=3 * 60 * 60 + 20 * 60,
    name="Vexor"
)

Ishtar = Manufacturable(
    requirements={
        IonThruster: 75,
        MagnetometricSensorCluster: 398,
        PhotonMicroprocessor: 1350,
        CrystallineCarbonideArmorPlate: 5625,
        FusionReactorUnit: 38,
        OscillatorCapacitorUnit: 450,
        PulseShieldEmitter: 450,
        Morphite: 150,
        ConstructionBlocks: 150,
        Vexor: 1,
        RAMStarshipTech: 18
    },
    produces=1,
    processing_time=2 * 24 * 60 * 60 + 18 * 60 * 60 + 40 * 60,
    name="Ishtar"
)

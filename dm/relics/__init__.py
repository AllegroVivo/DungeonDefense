from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from dm.core.objects.relic import DMRelic
################################################################################

__all__ = ("ALL_RELICS",)

################################################################################
from .OneStar       import *
from .TwoStar       import *
from .ThreeStar     import *
################################################################################
# All Relics
ALL_RELICS: List[Type["DMRelic"]] = [
    # 1-Star
    AbyssLamp, AdvancedIncubator, Apple, BloodStaff, BloodyMeteorite, Bullion,
    CateyeStone, CurseOfTheSkull, DeadlySting, ForeseeingOrb, GhostAmulet,
    GravityBracelet, Hammer, InsigniaOfTerror, IronPlate, LastResort,
    LesserManaPotion, LifePotion, MagicGear, Morningstar, ObservingEye,
    RegenerationOrb, TokenOfFriendship, UndeadGrip, VampiricMonster,

    # 2-Star
    AbyssAnvil, AbyssThorn, ArmorOfPower, BatControl, BattleDrums,
    ConstructionMaterial, CrystalEye, DawnDew, DeathGrip, DeepSeaBracelet,
    DemonArmor, DemonicWater, DemonSword, DemonTooth, DragonKingsBelt,
    FakeMap, Flute, Furball, Grapes, HallucinogenicMushroom, HealingNecklace,
    HiddenBox, InfectedBlood, LesserManaStone, LittleCoin, ManaPotion,
    ManaRecoveryRune, ManEatingPlant, MeteorDebris, NecklaceOfFocus, Net,
    ObsidianFang, PhoenixBeak, PotionOfTranscendence, RingOfDefense,
    RingOfWeakness, RuneOfVulnerability, SealedCoffin, SecondHeart, SharpThorn,
    SnakeBracelet, SoulOrb, SpeedPotion, StaffOfAuthority, Starfish,
    StrawberryPudding, SwordOfCharm, ThunderBracelet, TimeBomb, Wrench,

    # 3-Star
    AbyssFlower, AncientCoin, ArmorOfMadness, BlackBox, BloodyCloth,
    BloodyHourglass, BlueCoralReef, BrokenPromise, Cake, CommandersGauntlet,
    ConchShell, CorpseFlower, CubeFromOtherworld, CursedCandle, DeliciousMilk,
    DemonGlove, DemonicLamp, DemonLordsSeal, DemonsScale, DevilsTooth, Doorbell,
    DungeonIndex, Dynamite, ElixirOfImmortality, EmmasTailAccessory,
    FlameOfEternity, FourLeafClover, FuryMace, GiantThorn, GreaterManaPotion,
    JewelOfTheDeepSea, LoopOfFate, MagicalSoil, MagicSpring, ManaCollector,
    ManaConverter, ManaGrail, ManaStone, Monocle, MonsterHorn, MysteriousQuill,
    PhoenixClaw, RingOfEnlightenment, Rose, RustyBlade, Scorpion, SmokedMeat,
    SolarKey, StaffOfReign, Strawberry, TheOriginOfTheFall, TraitorsDagger,
    VampireAxe, VampireRing, VampireRune, VoodooMask, WarriorsBlood,
    WoodenStaff,

    # 4-Star
]
################################################################################

from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from dm.core.objects.relic import DMRelic
################################################################################

__all__ = ("ALL_RELICS",)

################################################################################
from .OneStar       import *
from .TwoStar       import *
from .ThreeStar     import *
from .FourStar      import *
from .FiveStar      import *
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
    AmethystChoker, AncientPickaxe, AssassinsDagger, BackwardsClock,
    BeadsOfObedience, Biography, BlackCatStatue, BloodyHammer, BloomingBud,
    Blueprint, BottomlessWallet, BraceletOfFury, CoreOfEarth, CoreOfFire,
    CoreOfIce, CoreOfWind, DemonicFruit, DemonIndex, FaintMagicEnergy,
    FairyWings, Flowerpot, GobletOfSoul, GreaterManaStone, GuardianJellyfish,
    HiddenTrapChute, LegendaryPickaxe, MagicShovelB, MagicShovelT, MonsterNest,
    OldAltarKey, PearlShell, PhoenixFeather, PioneersEye, PrehistoricPickaxe,
    PremiumMembershipCert, Rafflesia, SacredScissors, SagesBrush,
    ShadowPriestsBook, ShieldOfTheDevil, SmallDemonStatue, SteelBoomerang,
    Thunderbolt, Thurible, TurbanOfCharm, VampireThorn,

    # 5-Star
    AcceleratingWatch, AncientEgg, BigPortal, BlackHolyGrail, BlackMask,
    BlooddrinkerSword, BrokenAncientEgg, BrokenHolyGrail, CompletedDNA,
    CorruptedAncientEgg, CorruptedDragon, CorruptedSoulOrb, CorruptionController,
    CrackedAmberStone, CrescentNecklace, CrudeCube, CursedAmberStone,
    CursedPocketWatch, CurseOfTheSwampMonster, DarkCube, DungeonGuideMap,
    ElderDragon, FakeDungeonGuideMap, FirstMarkOfAsceticism, FullMoonNecklace,
    ImprovedCube, ImprovedDNA, IncompleteDNA, InfinitelyRotatingBlade,
    LastMarkOfAsceticism, LittleSwampMonster, MarkOfShadow, PerfectAmberStone,
    PicturesOfVillageRuins, ProtectorsDNA, ReapersSoulFragment, RestoredHolyGrail,
    RulersDNA, SecondMarkOfAsceticism, ShiningCube, ShiningMarkOfShadow,
    SmallPortal, SoulPot, StatueOfControlledAnger, StatueOfLiberatedRage,
    StatueOfSealedRage, StickyNet, StigmaOfAsceticism, StigmaOfDragonSlayer,
    SwampMonsterWall, TeardrinkerSword, ThirdMarkOfAsceticism,
]
################################################################################

from enum   import Enum
################################################################################

__all__ = (
    "DMType",
    "DMRoomType",
    "UnlockPack",
    "DMSpawnType",
    "HeroState",
    "DMFateType",
    "StatComponentType",
    "DMStatusType",
    "BattleState",
    "AttackType",
    "DMPurchaseType",
    "DMAdjustmentType"
)

################################################################################
class DMType(Enum):

    Room = 0
    Monster = 1
    Hero = 2
    DarkLord = 3
    FateCard = 4
    Object = 5
    Relic = 6
    Status = 7
    Skill = 8

################################################################################
class DMRoomType(Enum):

    Empty = 0
    Battle = 1
    Trap = 2
    Facility = 3
    Entrance = 4
    Boss = 5
    FateEntry = 6
    Blank = 7
    Shrine = 8

################################################################################
class UnlockPack(Enum):

    Original = 1
    Awakening = 2
    Advanced = 3
    Corruption = 4
    Adventure = 5
    Myth = 6
    Conqueror = 7
    AncientDict = 8
    Abyss = 9

################################################################################
class DMSpawnType(Enum):

    Monster = 1
    Hero = 2
    Room = 3
    Status = 4
    Relic = 5
    Fate = 6

################################################################################
class HeroState(Enum):

    Exploring = 1
    Engaging = 2
    InBattle = 3
    Disengaging = 4

################################################################################
class DMFateType(Enum):

    Entrance = 0
    Battle = 1
    Elite = 2
    Invade = 3
    Boss = 4
    Dungeon = 5
    Event = 6
    Treasure = 7
    MonsterTrader = 8
    FacilityTrader = 9
    EquipmentTrader = 10
    Trial = 11
    Rest = 12
    Upgrade = 13
    Train = 14
    Reading = 15
    Torture = 16
    RoomSwap = 17


################################################################################
class StatComponentType(Enum):

    Life = 1
    Attack = 2
    Defense = 3
    Dex = 4
    CombatAbility = 5
    NumAttacks = 6
    Speed = 7

################################################################################
class DMStatusType(Enum):

    Buff = 1
    Debuff = 2
    AntiBuff = 3
    AntiDebuff = 4
    HeroOnly = 5

################################################################################
class BattleState(Enum):

    InCombat = 1
    OutOfCombat = 2

################################################################################
class AttackType(Enum):

    Attack = 1
    Skill = 2
    Trap = 3

################################################################################
class DMPurchaseType(Enum):

    Temp = 0

################################################################################
class DMAdjustmentType(Enum):

        Gold = 1
        Soul = 2

################################################################################

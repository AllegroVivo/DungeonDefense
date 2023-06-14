from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from dm.core    import DMFateCard
################################################################################

__all__ = ("ALL_FATES", "SPAWNABLE_FATES")

################################################################################
# Packages
# from .dungeon         import *

# Modules
from .battle            import BattleFate
from .boss              import BossFate
from .dungeon           import DungeonFate
from .elite             import EliteFate
from .entrance          import EntranceFate
from .equipmenttrader   import EquipmentTraderFate
from .event             import EventFate
from .facilitytrader    import FacilityTraderFate
from .invade            import InvadeFate
from .monstertrader     import MonsterTraderFate
from .treasure          import TreasureFate
from .trial             import TrialFate
################################################################################

ALL_FATES: List[Type["DMFateCard"]] = [
    # Main Fates
    BattleFate, BossFate, DungeonFate, EliteFate, EntranceFate,
    EquipmentTraderFate, EventFate, FacilityTraderFate, InvadeFate,
    MonsterTraderFate, TreasureFate, TrialFate,

    # Dungeon Card sub-Fates.
    # ReadingFate, RestFate, RoomSwapFate, TortureFate, TrainFate, UpgradeFate
]

SPAWNABLE_FATES: List[Type["DMFateCard"]] = [
    BattleFate, DungeonFate, EliteFate, EquipmentTraderFate, EventFate,
    FacilityTraderFate, InvadeFate, MonsterTraderFate, TreasureFate, TrialFate,
]

################################################################################

from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from ..core     import DMRoom
################################################################################

__all__ = ("ALL_ROOMS", )

################################################################################
# Parent Modules
from .battleroom    import DMBattleRoom

# Packages
from .OneStar       import *
from .TwoStar       import *
from .ThreeStar     import *

from .special       import *
################################################################################
# All Rooms
ALL_ROOMS: List[Type["DMRoom"]] = [
    # Special (0-Star)
    BossRoom, EmptyRoom, EntranceRoom,

    # 1-Star
    Arena, Arrow, Barrier, Battle, Ice, Pit, Rockslide,

    # 2-Star
    Ambush, Betrayal, BloodAltar, Darkness, Distortion, Excess, Frenzy, Guillotine,
    Hatchery, Hunger, Ignition, Incineration, IronMaiden, Meditation, PanicRoom,
    Rage, Return, Sloth, Solitude, Sprout, SwordAndShield, Venom,

    # 3-Star

]

################################################################################

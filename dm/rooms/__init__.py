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

from .special       import *
################################################################################
# All Monsters
ALL_ROOMS: List[Type["DMRoom"]] = [
    # Special (0-Star)
    BossRoom, EmptyRoom, EntranceRoom,

    # 1-Star
    Battle,

    # 2-Star

]

################################################################################

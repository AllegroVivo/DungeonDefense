from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from ..core.objects.status  import DMStatus
################################################################################

__all__ = ("ALL_STATUSES", )

################################################################################
from .antibuffs import *
from .buffs     import *
################################################################################
# All Monsters
ALL_STATUSES: List[Type["DMStatus"]] = [
    # Buffs
    Absorption, Acceleration, Armor, Bloodlust, Defense, Dodge, DodgeTrap,
    Ecstacy, Elasticity, Focus, Fury, Grudge, Hatred, Immortality,

    # Antibuffs
    ArmorFragment, DodgeResist,
]
################################################################################

from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from ..core.objects.status  import DMStatus
################################################################################

__all__ = ("ALL_STATUSES", )

################################################################################
from .antibuffs     import *
from .antidebuffs   import *
from .buffs         import *
from .debuffs       import *
from .heroes        import *
################################################################################
# All Monsters
ALL_STATUSES: List[Type["DMStatus"]] = [
    # Buffs
    Absorption, Acceleration, Armor, Bloodlust, Defense, Dodge, DodgeTrap,
    Ecstasy, Elasticity, Focus, Fury, Grudge, Hatred, Immortality, ImmortalRage,
    Immune, Merciless, Mirror, NaturesPower, Phantom, Pleasure, Quick,
    Rampage, Rebound, Regeneration, Revenge, Seed, Shield, Taunt, Thorn,
    Vampire,

    # Debuffs
    Betray, Blind, Burn, Chained, Charm,

    # Antibuffs
    ArmorFragment, DodgeResist, ImmuneResist,

    # Antidebuffs


    # Hero-only

]
################################################################################

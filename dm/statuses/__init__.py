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
    Betray, Blind, Burn, Chained, Charm, Coagulation, CorpseExplosion, Curse,
    Despair, Dull, ElectricalShort, Fatigue, Frostbite, Haze, LivingBomb,
    Obey, Overweight, Panic, Peace, Poison, Recharge, Rigidity, Shock, Slow,
    Spore, Stun, Vulnerable, Weak, Web,

    # Antibuffs
    ArmorFragment, Calmness, DodgeResist, ImmuneResist, Inattention,
    MirrorFragment, RegeneratedBody, RegeneratedSkin,

    # Antidebuffs
    BlindResist, ChainedResist, CharmResist, CurseResist, FearResist,
    HazeResist, RigidityResist, StunResist,

    # Hero-only

]
################################################################################

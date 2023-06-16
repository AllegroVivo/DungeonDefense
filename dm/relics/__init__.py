from typing     import TYPE_CHECKING, List, Type

if TYPE_CHECKING:
    from dm.core.objects.relic import DMRelic
################################################################################

__all__ = ("ALL_RELICS",)

################################################################################
from .OneStar       import *

################################################################################
# All Relics
ALL_RELICS: List[Type["DMRelic"]] = [
    # 1-Star
    AbyssLamp, AdvancedIncubator, Apple, BloodStaff, BloodyMeteorite, Bullion,
    CateyeStone, CurseOfTheSkull, DeadlySting, ForseeingOrb, GhostAmulet,
    GravityBracelet, Hammer, InsigniaOfTerror, IronPlate, LastResort,
    LesserManaPotion, LifePotion, MagicGear, Morningstar, ObservingEye,
    RegenerationOrb, TokenOfFriendship, UndeadGrip, VampiricMonster
]
################################################################################

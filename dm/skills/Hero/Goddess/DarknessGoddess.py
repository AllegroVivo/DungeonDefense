from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DarknessGoddess",)

################################################################################
class DarknessGoddess(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-407",
            name="Darkness Goddess",
            description=(
                "When entering the dungeon, all heroes become immune to Panic, "
                "Corpse Explosion and all monsters cannot gain Immortality "
                "anymore."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if isinstance(ctx.target, DMMonster):
            if ctx.status.name == "Immortality":
                ctx.will_fail = True
        else:
            if ctx.status.name in ("Panic", "Corpse Explosion"):
                ctx.will_fail = True

################################################################################

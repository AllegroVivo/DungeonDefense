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

__all__ = ("WaterGoddess",)

################################################################################
class WaterGoddess(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-401",
            name="Water Goddess",
            description=(
                "When entering the dungeon, all heroes become immune to Slow, "
                "Frostbite and all monsters cannot gain Dodge anymore."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If the status is being applied to a monster
        if isinstance(ctx.target, DMMonster):
            # If the status is Dodge
            if ctx.status.name == "Dodge":
                # Nullify it
                ctx.will_fail = True
        # Otherwise, if the status is being applied to a hero
        else:
            # If the status is Slow or Frostbite
            if ctx.status.name in ("Slow", "Frostbite"):
                # Nullify it
                ctx.will_fail = True

################################################################################

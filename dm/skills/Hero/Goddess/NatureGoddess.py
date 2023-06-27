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

__all__ = ("NatureGoddess",)

################################################################################
class NatureGoddess(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-405",
            name="Nature Goddess",
            description=(
                "When entering the dungeon, all heroes become immune to Poison, "
                "Chained and all monsters cannot gain Regeneration anymore."
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
            # If the status is Regeneration
            if ctx.status.name == "Regeneration":
                # Nullify it
                ctx.will_fail = True
        # Otherwise, if the status is being applied to a hero
        else:
            # If the status is Poison or Chained
            if ctx.status.name in ("Poison", "Chained"):
                # Nullify it
                ctx.will_fail = True

################################################################################

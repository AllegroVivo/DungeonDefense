from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DarkMadness",)

################################################################################
class DarkMadness(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-408",
            name="Dark Madness",
            description=(
                "When Curse or Panic is applied to a hero, applies an identical "
                "amount of Hatred and Quick."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If the status is being applied to a hero
        if isinstance(ctx.target, DMHero):
            # If the status is Curse or Panic
            if ctx.status.name in ("Curse", "Panic"):
                # Apply identical amounts of Hatred and Quick
                for status in ("Hatred", "Quick"):
                    ctx.target.add_status(status, ctx.status.stacks, self)

################################################################################

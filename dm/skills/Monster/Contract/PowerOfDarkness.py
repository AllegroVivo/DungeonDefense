from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.monster import DMMonster
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PowerOfDarkness",)

################################################################################
class PowerOfDarkness(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-300",
            name="Power of Darkness",
            description=(
                "Panic applied to all monsters are converted to Hatred, and "
                "Corpse Explosion applied to enemy is doubled."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        # I'm going to make the assumption that "converted" means that the
        # status is entirely replaced with the new one - but for the same
        # intended target monster.

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # Had to reverse the order from the other four skills because this one
        # checks for Corpse Explosion instead of the initial status effect that
        # was nullified. So we're checking the status name after the class type.
        if isinstance(ctx.target, DMMonster):
            if ctx.status.name == "Panic":
                ctx.will_fail = True
                ctx.target.add_status("Hatred", ctx.status.stacks, self)
        elif isinstance(ctx.target, DMHero):
            if ctx.status.name == "Corpse Explosion":
                ctx.status.increase_stacks_pct(1.00)  # 100% additional effectiveness.

################################################################################

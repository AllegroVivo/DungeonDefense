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

__all__ = ("PowerOfLight",)

################################################################################
class PowerOfLight(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-304",
            name="Power of Light",
            description=(
                "Shock applied to all monsters are converted to Fury, "
                "and Shock applied to enemy is doubled."
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

        if ctx.status.name == "Shock":
            if isinstance(ctx.target, DMMonster):
                ctx.will_fail = True
                ctx.target.add_status("Fury", ctx.status.stacks, self)
            elif isinstance(ctx.target, DMHero):
                ctx.status.increase_stacks_pct(1.00)  # 100% additional effectiveness.

################################################################################

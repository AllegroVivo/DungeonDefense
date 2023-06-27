from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FormOfWater",)

################################################################################
class FormOfWater(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-242",
            name="Form of Water",
            description=(
                "Apply 2 Slow to the attacker. Also, damage received from "
                "enemies in Slow state is reduced by 60 %."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.source.add_status("Slow", 2, self)
            slow = ctx.source.get_status("Slow")
            if slow is not None:
                ctx.mitigate_pct(0.60)

################################################################################

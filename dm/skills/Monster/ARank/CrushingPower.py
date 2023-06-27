from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CrushingPower",)

################################################################################
class CrushingPower(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-239",
            name="Crushing Power",
            description=(
                "Gain 5 (+0.5*ATK) Fury at the beginning of the battle. "
                "Doubles the effect of Fury."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=5, scalar=0.5)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start", self.battle_start)
        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        if self.owner == ctx.target:
            if ctx.status.name == "Fury":
                ctx.amplify_pct(1.00)

################################################################################
    def battle_start(self):

        self.owner.add_status("Fury", self.effect, self)

################################################################################

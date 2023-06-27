from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CharredLeather",)

################################################################################
class CharredLeather(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-203",
            name="Charred Leather",
            description=(
                "Convert Burn applied to you to Fury. Also, damage received "
                "from enemies under the effect of Burn is reduced by 50 %."
            ),
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            burn = ctx.source.get_status("Burn")
            if burn is not None:
                ctx.mitigate_pct(0.50)

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")
        self.listen("on_attack", self.on_attack)

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if self.owner == ctx.target:
            if ctx.status.name == "Burn":
                ctx.will_fail = True
                self.owner.add_status("Fury", ctx.status.stacks, self)

################################################################################

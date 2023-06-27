from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BarelyAlive",)

################################################################################
class BarelyAlive(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-200",
            name="Barely Alive",
            description=(
                "Gain 3 (+0.5*ATK) Armor for every damage received."
            ),
            rank=2,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=3, scalar=0.5),
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            self.owner.add_status("Armor", self.effect * ctx.damage, self)

################################################################################

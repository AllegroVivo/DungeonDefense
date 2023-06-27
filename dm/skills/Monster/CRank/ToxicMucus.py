from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ToxicMucus",)

################################################################################
class ToxicMucus(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-210",
            name="Toxic Mucus",
            description=(
                "Apply 4 (+0.3*ATK) Poison to enemies that have attacked you "
                "or received damaged from you."
            ),
            rank=2,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=4, scalar=0.3),
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.source.add_status("Poison", self.effect, self)
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Poison", self.effect, self)

################################################################################

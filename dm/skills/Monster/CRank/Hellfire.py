from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Hellfire",)

################################################################################
class Hellfire(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-206",
            name="Hellfire",
            description=(
                "When inflicting damage, apply 12 (+1.0*ATK) Burn to target."
            ),
            rank=2,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=12, scalar=1.0),
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            ctx.target.add_status("Burn", self.effect, self)

################################################################################

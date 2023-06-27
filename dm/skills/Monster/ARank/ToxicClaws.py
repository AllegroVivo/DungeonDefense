from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ToxicClaws",)

################################################################################
class ToxicClaws(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-252",
            name="Toxic Claws",
            description=(
                "Inflict 15 (+0.75*ATK) Poison every time damage is inflicted "
                "to target."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=15, scalar=0.75)
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

        if ctx.damage > 0:
            ctx.target.add_status("Poison", self.effect, self)

################################################################################

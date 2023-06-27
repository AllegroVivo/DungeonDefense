from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities         import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Ultraregeneration",)

################################################################################
class Ultraregeneration(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-234",
            name="Ultraregeneration",
            description=(
                "Gain 8 (+0.8*ATK) Regeneration when attacked."
            ),
            rank=3,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=8, scalar=0.8)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            self.owner.add_status("Regeneration", self.effect, self)

################################################################################

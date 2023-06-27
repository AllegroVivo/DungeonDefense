from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Template",)

################################################################################
class Template(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-217",
            name="Healing Wave",
            description=(
                "Apply 2 (+0.25*ATK) Regeneration to all allies in the "
                "room when attacked."
            ),
            rank=3,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=2, scalar=0.25)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            for unit in self.room.units_of_type(self.owner):
                unit.add_status("Regeneration", self.effect, self)

################################################################################

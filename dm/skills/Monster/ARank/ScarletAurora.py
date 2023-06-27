from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ScarletAurora",)

################################################################################
class ScarletAurora(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-248",
            name="Scarlet Aurora",
            description=(
                "Apply 6 (+0.3*ATK) Vampire to all allies in the room when "
                "attacking enemy."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=6, scalar=0.3)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            for unit in ctx.room.units_of_type(self.owner):
                unit.add_status("Vampire", self.effect, self)

################################################################################

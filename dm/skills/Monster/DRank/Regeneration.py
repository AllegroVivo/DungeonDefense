from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RegenerationSkill",)

################################################################################
class RegenerationSkill(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-198",
            name="Regeneration",
            description=(
                "Gain (+0.5*ATK) Regeneration when attacked."
            ),
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=0, scalar=0.5),
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            self.owner.add_status("Regeneration", self.effect, self)

################################################################################

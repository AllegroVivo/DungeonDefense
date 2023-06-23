from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ChallengersCry",)

################################################################################
class ChallengersCry(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-148",
            name="Challenger's Cry",
            description=(
                "Gain 5 Taunt and 5 Defense."
            ),
            rank=2,
            cooldown=2
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        self.owner.add_status("Taunt", 5, self)
        self.owner.add_status("Defense", 5, self)

################################################################################

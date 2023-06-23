from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Feint",)

################################################################################
class Feint(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-127",
            name="Feint",
            description=(
                "Receive 66 % less damage from AoE attacks."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:
        """When called, performs this skill's active effect, if any."""

        # Not sure how to identify AoE attacks yet, so...
        pass

################################################################################

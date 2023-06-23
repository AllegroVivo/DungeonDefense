from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Disarm",)

################################################################################
class Disarm(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-125",
            name="Disarm",
            description=(
                "Apply 5 Weak to an enemy."
            ),
            rank=2,
            cooldown=2
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.source.add_status("Weak", 5, self)

################################################################################

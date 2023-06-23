from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Corrosion",)

################################################################################
class Corrosion(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-121",
            name="Corrosion",
            description="Apply 2 Weak to the attacker.",
            rank=2,
            cooldown=0
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.add_status("Weak", 2, self)

################################################################################

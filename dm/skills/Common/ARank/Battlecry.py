from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Battlecry",)

################################################################################
class Battlecry(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-146",
            name="Battlecry",
            description=(
                "Apply 3 Weak to all enemies in the room."
            ),
            rank=2,
            cooldown=4
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in ctx.room.units_of_type(self.owner, inverse=True):
            unit.add_status("Weak", 3, self)

################################################################################

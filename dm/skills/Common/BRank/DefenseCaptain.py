from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DefenseCaptain",)

################################################################################
class DefenseCaptain(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-123",
            name="Defense Captain",
            description=(
                "Apply 3 Defense to all allies in the room for every 2 "
                "attacks received."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're defending
        if self.owner == ctx.target:
            # If we're on the 2nd attack
            if self.atk_count % 2 == 0:
                # Apply Defense to all allies in the room.
                for unit in ctx.room.units_of_type(self.owner):
                    unit.add_status("Defense", 3, self)

################################################################################

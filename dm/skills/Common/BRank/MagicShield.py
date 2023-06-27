from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicShield",)

################################################################################
class MagicShield(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-133",
            name="Magic Shield",
            description=(
                "Apply 3 Shield to ally."
            ),
            rank=3,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Get a random ally
        target = self.random.choice(ctx.room.units_of_type(self.owner))
        # Apply Shield to the target.
        target.add_status("Shield", 3, self)

################################################################################

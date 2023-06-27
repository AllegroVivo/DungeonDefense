from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AchillesHeel",)

################################################################################
class AchillesHeel(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-113",
            name="Achilles Heel",
            description="Apply 5 Vulnerable to an enemy.",
            rank=3,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Get a random enemy in the room.
        target = self.random.choice(ctx.room.units_of_type(self.owner, inverse=True))
        # Apply Vulnerable.
        target.add_status("Vulnerable", 5, self)

################################################################################

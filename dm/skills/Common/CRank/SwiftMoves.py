from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwiftMoves",)

################################################################################
class SwiftMoves(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-109",
            name="Swift Moves",
            description="Gain 1 Dodge when damage is received 4 times.",
            rank=1,
            cooldown=CooldownType.Passive
        )

        self._dmg_count: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're defending
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage is being dealt
        if not ctx.will_fail:
            # Increment damage count
            self._dmg_count += 1
            # If we've been damaged 4 times
            if self._dmg_count % 4 == 0:
                # Reset damage count
                self._dmg_count = 0
                # Apply Dodge
                self.owner.add_status("Dodge", 1, self)

################################################################################

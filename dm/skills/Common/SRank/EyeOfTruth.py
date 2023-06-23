from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("EyeOfTruth",)

################################################################################
class EyeOfTruth(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-179",
            name="Eye of Truth",
            description=(
                "No debuff will cause it to attack an ally."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Late callback is a single callable that will be executed at the end of
        # the attack before damage application.
        if self.owner == ctx.source:
            ctx.register_late_callback(self.late_callback)

################################################################################
    def late_callback(self, ctx: AttackContext) -> None:

        # Check at the last second to see if the owner is attacking an ally.
        if ctx.target.is_ally(self.owner):
            # And negate the attack if so.
            ctx.will_fail = True

################################################################################

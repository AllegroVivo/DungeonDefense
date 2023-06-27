from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BlueGuardian",)

################################################################################
class BlueGuardian(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-117",
            name="Blue Guardian",
            description="Become immune to Slow and Frostbite.",
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the target of the status
        if self.owner == ctx.target:
            # If the status is Slow or Frostbite
            if ctx.status.name in ("Slow", "Frostbite"):
                # Nullify it.
                ctx.will_fail = True

################################################################################

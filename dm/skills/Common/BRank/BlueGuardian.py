from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

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
            description="(Passive) Become immune to Slow and Frostbite.",
            rank=2,
            cooldown=0
        )

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        self.listen("status_acquired")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:
        """A general event response function."""

        if self.owner == ctx.target:
            if ctx.status.name in ("Slow", "Frostbite"):
                ctx.will_fail = True

################################################################################

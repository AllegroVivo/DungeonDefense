from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts.status_apply import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Blindsense",)

################################################################################
class Blindsense(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-101",
            name="Blindsense",
            description="Become immune to Blind and Panic.",
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the status target
        if self.owner == ctx.target:
            # If the status is Blind or Panic
            if ctx.status.name in ("Blind", "Panic"):
                # Cancel the application
                ctx.will_fail = True

################################################################################

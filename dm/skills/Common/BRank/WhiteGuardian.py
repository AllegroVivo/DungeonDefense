from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("WhiteGuardian",)

################################################################################
class WhiteGuardian(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-145",
            name="White Guardian",
            description=(
                "Become immune to Weak and Curse."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the status target
        if self.owner == ctx.target:
            # If the status is Weak or Curse
            if ctx.status.name in ("Weak", "Curse"):
                # Cancel the status application
                ctx.will_fail = True

################################################################################

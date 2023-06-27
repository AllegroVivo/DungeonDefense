from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GraceOfDark",)

################################################################################
class GraceOfDark(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-159",
            name="Grace of Dark",
            description=(
                "Gain 1 Immune instead of Curse."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If the status is being applied to us.
        if self.owner == ctx.target:
            # If the status is Curse.
            if ctx.status.name == "Curse":
                # Cancel the application.
                ctx.will_fail = True
                # Apply Immune instead.
                self.owner.add_status("Immune", 1, self)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Valor",)

################################################################################
class Valor(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-186",
            name="Valor",
            description=(
                "Cancel Panic applied to self, and gain 1 Immortality instead."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're being targeted with a status
        if self.owner == ctx.target:
            # And it's Panic
            if ctx.status.name == "Panic":
                # Convert it to Immortality
                ctx.target.add_status("Immortality", 1, self)
                # And negate the original application
                ctx.will_fail = True

################################################################################

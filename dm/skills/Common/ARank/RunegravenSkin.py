from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RunegravenSkin",)

################################################################################
class RunegravenSkin(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-165",
            name="Runegraven Skin",
            description=(
                "Become immune to Vulnerable."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the target of the status.
        if self.owner == ctx.target:
            # If the status is Vulnerable.
            if ctx.status.name == "Vulnerable":
                # Cancel the application.
                ctx.will_fail = True

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RedGuardian",)

################################################################################
class RedGuardian(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-137",
            name="Red Guardian",
            description=(
                "Become immune to Burn and Shock."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if self.owner == ctx.target:
            if ctx.status.name in ("Burn", "Shock"):
                ctx.will_fail = True

################################################################################

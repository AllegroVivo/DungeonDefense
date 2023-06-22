from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

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
            description="(Passive) Become immune to Blind and Panic.",
            rank=1,
            cooldown=0
        )

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        self.listen("status_acquire")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:
        """A general event response function."""

        if self.owner == ctx.target:
            if ctx.status.name in ("Blind", "Panic"):
                ctx.will_fail = True

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

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
            if ctx.status.name == "Curse":
                ctx.will_fail = True
                self.owner.add_status("Immune", 1, self)

################################################################################

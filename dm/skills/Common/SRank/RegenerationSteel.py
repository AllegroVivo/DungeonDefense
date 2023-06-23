from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RegenerationSteel",)

################################################################################
class RegenerationSteel(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-184",
            name="Regeneration Steel",
            description=(
                "Regeneration applied to self is converted into double "
                "the amount of Armor."
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
            if ctx.status.name == "Regeneration":
                ctx.will_fail = True
                ctx.target.add_status("Armor", ctx.status.stacks * 2, self)

################################################################################

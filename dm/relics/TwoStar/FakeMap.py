from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import StatusExecutionContext
################################################################################

__all__ = ("FakeMap",)

################################################################################
class FakeMap(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-144",
            name="Fake Map",
            description="Ignores enemy's Dodge Trap effect at a 25 % chance.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        if isinstance(ctx.target, DMHero):
            if ctx.status.name == "Dodge Trap":
                ignore = self.random.chance(25)
                if ignore:
                    ctx.will_fail = True

################################################################################

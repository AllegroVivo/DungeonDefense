from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts import StatusExecutionContext
    from dm.core.objects.hero import DMHero
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssThorn",)

################################################################################
class AbyssThorn(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-134",
            name="AbyssThorn",
            description="Doubles Thorn damage against enemies.",
            rank=2
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        # If the status being executed is Thorn
        if ctx.status.name == "Thorn":
            # And the owner is a hero
            if isinstance(ctx.status.owner, DMHero):
                # Then double the base effect (Thorn damage = thorn.stacks)
                ctx.status.increase_base_effect(1.0)

################################################################################

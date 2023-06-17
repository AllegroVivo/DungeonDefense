from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Immortality",)

################################################################################
class Immortality(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-114",
            name="Immortality",
            description=(
                "Survive critical damage with 1 LIFE. Stat decreases by 1 and "
                "you gain 1 Regenerated Body per effect activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.defender:
            ctx.register_after_execute(self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if not ctx.defender.is_alive:
            # Check resistance
            resist = self.owner.get_status("Regenerated Body")
            if resist is not None:
                if resist >= self:
                    return

            # Survive death with 1 LIFE
            self.owner.heal(1)

            # Reduce stacks
            self.reduce_stacks_by_one()

            # And resistance
            self.owner.add_status("Regenerated Body")

################################################################################

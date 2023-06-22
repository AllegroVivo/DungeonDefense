from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Thorn",)

################################################################################
class Thorn(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-130",
            name="Thorn",
            description=(
                "Inflicts damage as much as Thorn stat to the enemy who inflicted "
                "damage. The stat is reduced by half upon activation."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        ctx.register_after_execute(self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If we're defending.
        if self.owner == ctx.target:
            # And damage will occur
            if ctx.damage > 0:
                damage = self.stacks

                # Check for the corresponding relic.
                relic = self.game.get_relic("Abyss Thorn")
                if relic is not None:
                    damage *= 2

                # Apply final damage and reduce stacks
                ctx.source.damage(damage)
                self.reduce_stacks_by_half()

################################################################################

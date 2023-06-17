from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Poison",)

################################################################################
class Poison(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-121",
            name="Peace",
            description=(
                "Receive damage as much as this stat at the beginning of action, "
                "and then the stat is reduced by half."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically upon the status's acquisition by the unit."""

        self.game.subscribe_event("before_attack", self.notify)

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        # Appears to apply on any action - attacking or defending
        self.owner.damage(self.stacks)
        self.reduce_stacks_by_half()

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Vampire",)

################################################################################
class Vampire(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-131",
            name="Vampire",
            description=(
                "Recover LIFE as much as Vampire stat possessed when attacking "
                "enemy. Stacks are reduced by half upon activation."
            ),
            stacks=stacks,
            status_type=StatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every iteration of the battle loop."""

        if self.owner == ctx.source:
            # Pretty straightforward
            heal_amt = self.stacks
            # Check for the corresponding relic  (If present, doubles healing effect)
            relic = self.game.get_relic("X")
            if relic is not None:
                heal_amt *= 2

            # Heal the unit and reduce stacks by half.
            self.owner.heal(heal_amt)
            self.reduce_stacks_by_half()

            if heal_amt is None:
                return

            # Check for the other corresponding relic.
            relic = self.game.get_relic("BlooddrinkerSword")
            if relic is not None:
                self.game.dark_lord.add_status("Hatred", 1)

################################################################################

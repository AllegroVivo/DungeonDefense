from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ...core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts.attack import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Armor",)

################################################################################
class Armor(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-103",
            name="Armor",
            description=(
                "Reduces damage received from the enemy equal to stacks of Armor "
                "possessed. Stat decreases by the amount of damage reduced and "
                "unit gains Armor Fragment equal to that amount. "
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:

        if ctx.defender == self.owner:
            # Determine whether stack count or damage total is lower
            effect_value = min(self.stacks, ctx.damage)
            # Check for antibuff
            fragment = self.owner.get_status("Armor Fragment")
            if fragment is not None:
                # If the antibuff outweighs the stacks, it's a no go.
                if fragment.stacks > effect_value:
                    return

            # If it passed the antibuff check, we can execute the mitigation.
            ctx.mitigate_flat(effect_value)

            # Reduce stacks
            self.reduce_stacks_flat(effect_value)

            # Avoid adding an empty antibuff to the unit.
            if effect_value != 0:
                self.owner.add_status("Armor Fragment", stacks=effect_value)

################################################################################

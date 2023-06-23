from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.hero import DMHero
from dm.core.objects.monster import DMMonster
from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Betray",)

################################################################################
class Betray(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-101",
            name="Betray",
            description=(
                "The next attack against an ally deals double damage. Stat "
                "decreases by 1 each time an ally is damaged."
            ),
            stacks=stacks,
            status_type=StatusType.Debuff,
            base_effect=1.00
        )

        # This status is deprecated and doesn't appear in the game. Whoops!

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called in every battle loop iteration."""

        # Statuses can't be held by trap rooms, so that eliminates traps from this equation.
        if self.owner == ctx.source:
            # If we're not a hero fighting a hero, return.
            if isinstance(self, DMHero):
                if not isinstance(ctx.target, DMHero):
                    return
            # Or monster fighting monster
            elif not isinstance(ctx.target, DMMonster):
                return

            # If we passed the checks, double the damage
            ctx.amplify_pct(self.base_effect)

            # And reduce
            self.reduce_stacks_by_one()

################################################################################

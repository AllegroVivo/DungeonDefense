from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.contexts import DayAdvanceContext
################################################################################

__all__ = ("ElderDragon",)

################################################################################
class ElderDragon(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-292",
            name="Elder Dragon",
            description=(
                "Acquire 1000 Gold every time you win the Boss Battle, and "
                "the number of intruders is decreased by 15 %."
            ),
            rank=5
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        # 15 fewer intruders
        self.game.dungeon.modify_hero_spawn_rate(-0.15)

        self.listen("day_advance")

################################################################################
    def notify(self, ctx: DayAdvanceContext) -> None:

        # If the day is advancing, we know we won the fight.
        if ctx.next_day - 1 % 20 == 0:
            self.game.inventory.add_gold(1000)

################################################################################

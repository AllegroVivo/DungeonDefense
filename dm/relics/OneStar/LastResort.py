from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("LastResort",)

################################################################################
class LastResort(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-116",
            name="Last Resort",
            description=(
                "Decreases the damage received by the Dark Lord by 30 % when there "
                "are no monsters in the Dark Lord's Room except the Dark Lord."
            ),
            rank=1
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If the Dark Lord is defending
        if ctx.target == self.game.dark_lord:
            # And there are no other monsters in the boss room
            if len(self.game.dungeon.map.boss_tile.monsters) == 1:  # Remember, Dark Lord counts:
                # Reduce damage
                ctx.mitigate_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.30

################################################################################

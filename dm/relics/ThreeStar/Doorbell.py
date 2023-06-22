from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Doorbell",)

################################################################################
class Doorbell(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-217",
            name="Doorbell",
            description=(
                "Damage the Dark Lord receives per hero during battle in the "
                "Dark Lord's Room is decreased by 1 %. (Max 50 %)"
            ),
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're in the boss room
        if ctx.room == self.game.dungeon.map.boss_tile:
            # And the defender is the dark lord
            if ctx.target == self.game.dark_lord:
                # Mitigate the damage.
                ctx.mitigate_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = max(a * h, m)**

        In this function:

        - a is the additional effectiveness per hero.
        - h is the number of heroes.
        - m is the maximum effectiveness.
        """

        return max(0.01 * len(self.game.dungeon.map.boss_tile.heroes), 0.50)

################################################################################

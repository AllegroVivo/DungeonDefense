from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("AbyssAnvil",)

################################################################################
class AbyssAnvil(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-133",
            name="Abyss Anvil",
            description=(
                "Increases ATK of monsters equipped with equipment by 20 %."
            ),
            rank=2
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        # Check all monsters
        for monster in self.game.deployed_monsters:
            # And if they're wearing equipment
            if monster.equipment is not None:
                # Buff attack
                monster.increase_stat_pct("attack", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################

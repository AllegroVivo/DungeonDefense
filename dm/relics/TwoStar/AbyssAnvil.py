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

        for monster in self.game.deployed_monsters:
            if monster.equipment is not None:
                monster.increase_stat_pct("attack", 0.20)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("RulersDNA",)

################################################################################
class RulersDNA(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-309",
            name="Ruler's DNA",
            description=(
                "EXP required for monsters to level up is reduced by 30 %. "
                "All monsters' ATK is increased by 50 %."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

        # Probably going to implement this whole set in level-up logic.

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.game.deployed_monsters:
            monster.increase_stat_pct("atk", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################

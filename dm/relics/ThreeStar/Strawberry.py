from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Strawberry",)

################################################################################
class Strawberry(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-208",
            name="Strawberry",
            description="Increases all monsters' ATK by 10 %.",
            rank=3
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.game.deployed_monsters:
            monster.increase_stat_pct("attack", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.10

################################################################################

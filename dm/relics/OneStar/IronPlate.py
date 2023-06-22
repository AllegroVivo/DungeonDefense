from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("IronPlate",)

################################################################################
class IronPlate(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-115",
            name="Iron Plate",
            description=(
                "All monsters gain 20 % of max LIFE as Armor at the "
                "start of battle."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("battle_start")

################################################################################
    def notify(self, *args) -> None:

        for monster in self.game.deployed_monsters:
            monster.add_status("Armor", monster.max_life * self.effect_value(), self)

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.20

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("PicturesOfVillageRuins",)

################################################################################
class PicturesOfVillageRuins(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-340",
            name="Pictures of Village Ruins",
            description=(
                "The number of enemies entering the dungeon increases greatly."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

        # 50% additional entrance rate.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.dungeon.modify_hero_spawn_rate(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################

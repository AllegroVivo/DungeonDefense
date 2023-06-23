from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CurseOfTheSwampMonster",)

################################################################################
class CurseOfTheSwampMonster(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-325",
            name="Curse of the Swamp Monster",
            description="All characters' DEX is decreased by 10 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for unit in self.game.deployed_monsters + self.game.all_heroes:  # type: ignore
            unit.reduce_stat_pct("dex", self.effect_value())

################################################################################

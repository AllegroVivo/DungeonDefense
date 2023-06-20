from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SwampMonsterWall",)

################################################################################
class SwampMonsterWall(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-326",
            name="Swamp Monster Wall",
            description="All heroes' movement speed and DEX is reduced by 15 %.",
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for hero in self.game.all_heroes:
            hero.reduce_stat_pct("dex", self.effect_value())
            hero.reduce_stat_pct("speed", self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.15  # 15% reduced effectiveness

################################################################################

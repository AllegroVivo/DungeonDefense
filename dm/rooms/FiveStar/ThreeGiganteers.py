from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ThreeGiganteers",)

################################################################################
class ThreeGiganteers(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-170",
            name="Three Giganteers",
            description=(
                "Deployed monsters will gigantify and get {life}x LIFE "
                "and {atk}x ATK."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original,
            effects=[
                Effect(name="life", base=2, per_lv=1),
            ]
        )

################################################################################
    def atk_boost(self) -> float:

        # Effectiveness every 5 levels after 4
        return float(2 + (1 * ((self.level - 4) // 5)))

################################################################################
    def stat_adjust(self) -> None:

        for monster in self.monsters:
            monster.increase_stat_pct("LIFE", self.effects["life"])
            monster.increase_stat_pct("ATK", self.atk_boost())

################################################################################

from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Gigantify",)

################################################################################
class Gigantify(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-131",
            name="Gigantify",
            description=(
                "You can only deploy 1 monster in this room, but the monster "
                "will gigantify and get {life}x LIFE and {atk}x ATK."
            ),
            level=level,
            rank=3,
            monster_cap=1,
            effects=[
                Effect(name="buff", base=2, per_lv=1),
            ]
        )

################################################################################
    @property
    def atk_boost(self) -> float:

        # Effectiveness every 10 levels after 6
        return float(2 + (1 * ((self.level - 6) // 10)))

################################################################################
    def stat_adjust(self) -> None:

        for monster in self.monsters:  # (Only 1 monster can be deployed)
            monster.increase_stat_pct("life", self.effects["buff"])
            monster.increase_stat_pct("atk", self.atk_boost)

################################################################################

from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BiggerFight",)

################################################################################
class BiggerFight(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-174",
            name="Bigger Fight",
            description=(
                "Increases the number of deployable monsters by 2. The deployed "
                "monsters' ATK and LIFE is increased by {value} %. Gives 1 "
                "Rampage to deployed monsters whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            monster_cap=5,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="atk", base=50, per_lv=25),
                Effect(name="deg", base=50, per_lv=25)
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Rampage", 1, self)

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for monster in self.monsters:
            monster.increase_stat_pct("atk", self.effects["atk"] / 100)  # Convert to percentage
            monster.increase_stat_pct("life", self.effects["def"] / 100)

################################################################################

from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Pressure",)

################################################################################
class Pressure(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-149",
            name="Pressure",
            description=(
                "DEX of heroes in the room is decreased by {value} %. Gives "
                "{status} Slow to heroes that entered the room."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Original
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                unit.add_status("Slow", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[float, int]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        stat_adj = float(10 + (1 * self.level))
        status = 1 + (1 * self.level)

        return stat_adj, status

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("room_enter")

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        for hero in self.heroes:
            hero.reduce_stat_pct("DEX", self.effect_value()[0])

################################################################################

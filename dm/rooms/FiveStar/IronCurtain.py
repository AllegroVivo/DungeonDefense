from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("IronCurtain",)

################################################################################
class IronCurtain(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-177",
            name="Iron Curtain",
            description=(
                "Gives {value} Armor to all monsters in the dungeon when a "
                "hero enters."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                for monster in self.game.deployed_monsters:
                    monster.add_status("Armor", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 36 + (24 * self.level)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("room_enter")

################################################################################

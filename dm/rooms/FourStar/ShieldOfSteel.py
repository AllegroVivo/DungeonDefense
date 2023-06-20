from __future__ import annotations

import random

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ShieldOfSteel",)

################################################################################
class ShieldOfSteel(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-153",
            name="Shield of Steel",
            description=(
                "Gives {value} Armor to deployed monsters whenever a hero "
                "enters. Gives 3 Shield to all monsters in adjacent rooms at "
                "the beginning of battle."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                for monster in self.monsters:
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
        self.game.subscribe_event("battle_start", self.battle_start)

################################################################################
    def battle_start(self) -> None:

        rooms = self.game.dungeon.get_adjacent_rooms(self.position)
        for room in rooms:
            for monster in room.monsters:
                monster.add_status("Shield", 3)

################################################################################

from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.hero import DMHero

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Return",)

################################################################################
class Return(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-128",
            name="Return",
            description=(
                "The 3rd enemy is returned to the dungeon entrance. The number "
                "of entries required for operation increases with each "
                "activation. It works up to {value} times."
            ),
            level=level,
            rank=2
        )

        self._count: int = 0
        self._triggers: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.game.subscribe_event("battle_end", self.after_battle)

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        # If the unit is in this room.
        if unit.room == self:
            # If the unit is a hero.
            if isinstance(unit, DMHero):
                # Increment the count and check if the hero is the third hero
                # to enter this room.
                self._count += 1
                # If we've hit the third hero to enter.
                if self._count == 3:
                    # Return the hero to the dungeon entrance.
                    unit.room = self.game.dungeon.entrance
                    # Increment the number of times this room has been triggered.
                    self._triggers += 1
                    # And reset the entry count.
                    self._count = 0

        # If we've triggered this room enough times.
        if self._triggers >= self.effect_value():
            # Remove from the listener for this battle.
            self.game.unsubscribe_event("room_enter", self.notify)

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base number of uses.
        - a is the additional number of uses per level.
        - LV is the level of this room.
        """

        return 3 + (1 * self.level)

################################################################################
    def after_battle(self) -> None:

        # Always re-add the listener for future battles.
        self.listen("room_enter")

################################################################################

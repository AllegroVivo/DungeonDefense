from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SaplingOfYggdrasil",)

################################################################################
class SaplingOfYggdrasil(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-210",
            name="Sapling of Yggdrasil",
            description=(
                "UrMom"
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Adventure
        )

        self._uninvaded_battles: int = 0

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                self._uninvaded_battles = 0

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("room_enter")
        self.game.subscribe_event("battle_start", self.battle_start)
        self.game.subscribe_event("day_advance", self.check_advance)

################################################################################
    def battle_start(self) -> None:

        self._uninvaded_battles += 1

################################################################################
    def check_advance(self) -> None:

        if self._uninvaded_battles >= 100:
            # Unsubscribe from events.
            self.game.unsubscribe_event("room_enter", self.notify)
            self.game.unsubscribe_event("battle_start", self.battle_start)
            self.game.unsubscribe_event("day_advance", self.check_advance)

            self.remove()
            # Or something like this
            # self.game.add_room(SaplingOfYggdrasil(self.game, self.position, self.level + 1))

################################################################################

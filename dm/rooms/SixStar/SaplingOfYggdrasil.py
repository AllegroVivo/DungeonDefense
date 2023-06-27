from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.contexts import DayAdvanceContext
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
                "The last hope for the Yggdrasil, the World Tree."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Adventure
        )

        self._uninvaded_battles: int = 0

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        if isinstance(unit, DMHero):
            self._uninvaded_battles = 0

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start", self.battle_start)
        self.listen("day_advance", self.notify)

################################################################################
    def battle_start(self) -> None:

        self._uninvaded_battles += 1

################################################################################
    def notify(self, ctx: DayAdvanceContext) -> None:

        if self._uninvaded_battles >= 100:
            # Unsubscribe from events.
            self.game.unsubscribe_event("battle_start", self.battle_start)
            self.game.unsubscribe_event("day_advance", self.notify)

            # Spawn the replacement room
            new_room = self.game.spawn(_id="ROOM-233", position=self.position, level=self.level)

            # And perform the swap
            self.remove()
            self.game.dungeon.replace_room(self, new_room)  # type: ignore

################################################################################

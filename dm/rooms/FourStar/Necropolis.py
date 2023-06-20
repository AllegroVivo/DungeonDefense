from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Necropolis",)

################################################################################
class Necropolis(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-151",
            name="Necropolis",
            description=(
                "Gives {value} Immortality to all monsters in the room at the "
                "beginning of the battle. When a deployed monster dies, "
                "give {status} Immortality to all monsters."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if ctx.room == self:
            if ctx.defender in self.monsters:
                for monster in self.game.deployed_monsters:
                    monster.add_status("Immortality", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int, int]:
        """The value(s) of this room's effect(s).

        Breakdown:
        ----------
        **start_status = b + (a * LV)**

        **on_death_status = b + (a * LV@10(6))**

        In these functions:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        - LV@10(6) represents every 10 levels after the 6th level.
        """

        status = 4 + (2 * self.level)
        on_death = 3 + (1 * ((self.level - 6) // 10))

        return status, on_death

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("on_death")
        self.game.subscribe_event("battle_start", self.status_effect)

################################################################################
    def status_effect(self) -> None:

        for monster in self.monsters:
            monster.add_status("Immortality", self.effect_value()[0])

################################################################################

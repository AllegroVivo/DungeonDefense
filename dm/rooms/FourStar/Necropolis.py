from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

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
                "Gives {start} Immortality to all monsters in the room at the "
                "beginning of the battle. When a deployed monster dies, "
                "give {status} Immortality to all monsters."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="Immortality", base=4, per_lv=2),
            ]
        )

################################################################################
    def on_death(self, ctx: AttackContext) -> None:

        if ctx.room == self:
            if ctx.target in self.monsters:
                for monster in self.game.deployed_monsters:
                    monster.add_status("X", self.death_value, self)

################################################################################
    @property
    def death_value(self) -> int:

        # Additional effectiveness for every 10 levels above 6.
        return 3 + (1 * ((self.level - 6) // 10))

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("on_death", self.on_death)
        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        for monster in self.monsters:
            monster.add_status("X", self.effects["X"], self)

################################################################################

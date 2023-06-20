from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts.attack import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Sacrifice",)

################################################################################
class Sacrifice(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-143",
            name="Sacrifice",
            description=(
                "Dark Lord's LIFE is restored by {value} % if enemy dies "
                "in the room."
            ),
            level=level,
            rank=3,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if ctx.room == self:
            self.game.dark_lord.heal(self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = (b + (a * LV)) * DL**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        - DL is the Dark Lord's max life.
        """

        effect = 0.02 + (0.01 * self.level)
        return int(self.game.dark_lord.max_life * effect)

################################################################################

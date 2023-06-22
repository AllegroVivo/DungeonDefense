from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Dynamite",)

################################################################################
class Dynamite(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-193",
            name="Dynamite",
            description=(
                "When a hero in this room dies, inflict {value} % of the dead "
                "hero's Burn stat to all heroes in adjacent rooms."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if ctx.room == self:
            burn = ctx.target.get_status("Burn")
            if burn is not None:
                targets = []
                for room in self.adjacent_rooms:
                    targets.extend(room.heroes)

                for target in targets:
                    target.damage(burn.stacks * self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return (300 + (50 * self.level)) / 100  # Convert to percentage.

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("on_death")

################################################################################

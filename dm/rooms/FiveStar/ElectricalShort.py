from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElectricalShort",)

################################################################################
class ElectricalShort(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-183",
            name="Electrical Short",
            description=(
                "Consumes all of hero's Shock stat and inflicts damage by "
                "{value} % of stat consumed to all enemies in adjacent rooms."
            ),
            level=level,
            rank=5
        )

        # Assuming this triggers on entry?

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            shock = unit.get_status("Shock")
            if shock is not None:
                rooms = self.game.dungeon.get_adjacent_rooms(self.position)
                targets = []
                for room in rooms:
                    targets.extend(room.heroes)

                for target in targets:
                    target.damage(shock.stacks * self.effect_value())

                shock.reduce_stacks_flat(shock.stacks)

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

        return (200 + (50 * self.level)) / 100  # Convert to percentage.

################################################################################

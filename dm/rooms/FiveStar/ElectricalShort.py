from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

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
                "Consumes all of hero's Shock stat and inflicts damage equal to "
                "{value} % of stat consumed to all enemies in adjacent rooms."
            ),
            level=level,
            rank=5,
            effects=[
                Effect(name="scalar", base=200, per_lv=50)
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        shock = unit.get_status("Shock")
        if shock is not None:
            targets = []
            for room in self.adjacent_rooms:
                targets.extend(room.heroes)

            for target in targets:
                target.damage(shock.stacks * self.effects["scalar"] / 100)

            shock.deplete_all_stacks()

################################################################################

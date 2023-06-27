from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Slingshot",)

################################################################################
class Slingshot(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-164",
            name="Slingshot",
            description=(
                "Inflicts {value} damage and reduce Armor by {status} to hero "
                "that entered the room."
            ),
            level=level,
            rank=4,
            base_dmg=34,
            effects=[
                Effect(name="Armor", base=8, per_lv=6),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.dmg)
        armor = unit.get_status("Armor")
        if armor is not None:
            armor.reduce_stacks_flat(self.effects["Armor"])

################################################################################

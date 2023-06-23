from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FireStorm",)

################################################################################
class FireStorm(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-186",
            name="Fire Storm",
            description=(
                "Inflicts {damage} damage to all heroes in adjacent rooms, "
                "and applies {status} Burn whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening,
            base_dmg=43,
            effects=[
                Effect(name="Burn", base=192, per_lv=128)
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        for target in targets:
            target.damage(self.damage)
            target.add_status("Burn", self.effects["Burn"], self)

################################################################################

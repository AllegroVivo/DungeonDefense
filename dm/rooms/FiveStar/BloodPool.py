from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..battleroom   import DMBattleRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BloodPool",)

################################################################################
class BloodPool(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-172",
            name="Blood Pool",
            description=(
                "Give {value} Vampire and Fury to all monsters in adjacent "
                "rooms whenever a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="Vampire", base=20, per_lv=12),
                Effect(name="Fury", base=20, per_lv=12),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for room in self.adjacent_rooms:
            for monster in room.monsters:
                monster.add_status("Vampire", self.effects["Vampire"], self)
                monster.add_status("Fury", self.effects["Fury"], self)

################################################################################

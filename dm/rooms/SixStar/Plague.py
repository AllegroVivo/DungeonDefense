from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import UnlockPack, Effect
from ..battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Plague",)

################################################################################
class Plague(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-200",
            name="Plague",
            description=(
                "Gives {value} Poison and Corpse Explosion to all heroes in "
                "adjacent rooms whenever a hero enters the room."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Awakening,
            effects=[
                Effect(name="Poison", base=24, per_lv=16),
                Effect(name="Corpse Explosion", base=24, per_lv=16),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        for target in targets:
            target.add_status("Poison", self.effects["Poison"], self)
            target.add_status("Corpse Explosion", self.effects["Corpse Explosion"], self)

################################################################################

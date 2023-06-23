from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pygame import Vector2

from utilities import UnlockPack, Effect
from ..battleroom import DMBattleRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ShieldOfSteel",)

################################################################################
class ShieldOfSteel(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-153",
            name="Shield of Steel",
            description=(
                "Gives {value} Armor to deployed monsters whenever a hero "
                "enters. Gives 3 Shield to all monsters in adjacent rooms at "
                "the beginning of battle."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Armor", base=36, per_lv=24),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Armor", self.effects["Armor"], self)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        for room in self.adjacent_rooms:
            for monster in room.monsters:
                monster.add_status("Shield", 3, self)

################################################################################

from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ArrowBomb",)

################################################################################
class ArrowBomb(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-211",
            name="Arrow Bomb",
            description=(
                "Once recharged, inflict {value} damage to all enemies in "
                "adjacent area."
            ),
            level=level,
            rank=7,
            unlock=UnlockPack.Myth,
            base_dmg=33
        )
        self.setup_charging(1.6, 1.6)

################################################################################
    def on_charge(self) -> None:

        for room in self.adjacent_rooms:
            for hero in room.heroes:
                hero.damage(self.damage)

################################################################################

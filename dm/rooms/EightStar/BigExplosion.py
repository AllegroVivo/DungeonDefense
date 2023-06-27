from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BigExplosion",)

################################################################################
class BigExplosion(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-217",
            name="Big Explosion",
            description=(
                "Once recharged, inflict {value} damage to all enemies in "
                "the dungeon."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth,
            base_dmg=29
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.dmg)

################################################################################

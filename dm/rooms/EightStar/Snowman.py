from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from dm.rooms.traproom import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Snowman",)

################################################################################
class Snowman(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-220",
            name="Snowman",
            description=(
                "Once recharged, inflict {damage} damage to a random enemy "
                "in the adjacent area and the enemies near it, and give them "
                "{status} Slow."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Myth,
            base_dmg=81,
            effects=[
                Effect(name="Slow", base=3, per_lv=1)
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms + [self]:
            targets.extend(room.heroes)

        target = self.random.choice(targets)
        for hero in target.room.heroes:
            hero.damage(self.dmg)
            hero.add_status("Slow", self.effects["Slow"], self)

################################################################################

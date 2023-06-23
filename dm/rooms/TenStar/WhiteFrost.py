from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("WhiteFrost",)

################################################################################
class WhiteFrost(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-236",
            name="White Frost",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in "
                "the dungeon, and give them {status} Slow and 3 Frostbite."
            ),
            level=level,
            rank=10,
            unlock=UnlockPack.Myth,
            base_dmg=81,
            effects=[
                Effect(name="Slow", base=10, per_lv=1),
            ]
        )
        self.setup_charging(6.6, 6.6)

################################################################################
    def on_charge(self) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.damage)
            hero.add_status("Slow", self.effects["Slow"], self)
            hero.add_status("Frostbite", 3, self)

################################################################################

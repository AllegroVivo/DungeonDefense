from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("CurseWave",)

################################################################################
class CurseWave(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-218",
            name="Curse Wave",
            description=(
                "Once recharged, give 3 (+1 per Lv) Weak, Vulnerable, and Curse to all enemies in adjacent area."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        for hero in heroes:
            hero.add_status("Weak", self.effect_value())
            hero.add_status("Vulnerable", self.effect_value())
            hero.add_status("Curse", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 3 + (1 * self.level)

################################################################################

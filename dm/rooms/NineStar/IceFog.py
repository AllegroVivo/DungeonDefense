from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("IceFog",)

################################################################################
class IceFog(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-228",
            name="Ice Fog",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in "
                "adjacent area and give them {status} Slow."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            base_dmg=161,
            effects=[
                Effect(name="Slow", base=3, per_lv=1),
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        for hero in heroes:
            hero.damage(self.damage)
            hero.add_status("Slow", self.effects["Slow"], self)

################################################################################

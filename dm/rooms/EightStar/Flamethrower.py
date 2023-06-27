from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Flamethrower",)

################################################################################
class Flamethrower(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-219",
            name="Flamethrower",
            description=(
                "Once recharged, inflict {damage} damage to a random enemy "
                "in the adjacent area and the enemies near it, and give "
                "them {status} Burn."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth,
            base_dmg=81,
            effects=[
                Effect(name="Burn", base=72, per_lv=48)
            ]
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:
        """A general event response function."""

        targets = []
        for room in self.adjacent_rooms + [self]:
            targets.extend(room.heroes)

        target = self.random.choice(targets)
        target.damage(self.dmg)
        target.add_status("Burn", self.effects["Burn"], self)

################################################################################

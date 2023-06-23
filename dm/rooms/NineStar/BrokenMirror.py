from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BrokenMirror",)

################################################################################
class BrokenMirror(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-231",
            name="Broken Mirror",
            description=(
                "Once recharged, inflict {damage} damage to all enemies in "
                "adjacent room and give them {status} Haze. Inflict {buff} % "
                "extra damage by consuming 1 Mirror if the target is under "
                "effect of Mirror."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Myth,
            base_dmg=121,
            effects=[
                Effect(name="Haze", base=5, per_lv=1),
                Effect(name="buff", base=400, per_lv=4),
            ]
        )

################################################################################
    def on_charge(self) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        for hero in heroes:
            hero.damage(self.damage)
            hero.add_status("Haze", self.effects["Haze"], self)
            mirror = hero.get_status("Mirror")
            if mirror is not None:
                hero.damage(self.damage * (self.effects["buff"] / 100))
                mirror.reduce_stacks_flat(1)

################################################################################

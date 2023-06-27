from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("ExplosiveArrow",)

################################################################################
class ExplosiveArrow(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-197",
            name="Explosive Arrow",
            description=(
                "Once recharged, inflict {value} damage to a random enemy in "
                "adjacent area and the enemies near it."
            ),
            level=level,
            rank=6,
            base_dmg=37
        )
        self.setup_charging(1.2, 1.2)

################################################################################
    def on_charge(self) -> None:

        targets = []
        for room in self.adjacent_rooms:
            targets.extend(room.heroes)

        # Grab a random target from the list of targets.
        target = self.random.choice(targets)
        # Then damage all heroes in the target's room.
        for hero in target.room.heroes:
            hero.damage(self.dmg)

################################################################################

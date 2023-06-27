from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from ...core.objects.monster import DMMonster

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Guillotine",)

################################################################################
class Guillotine(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-123",
            name="Guillotine",
            description=(
                "Inflicts {value} damage to the hero that entered the room. "
                "The lower the LIFE of the hero, the more damage is inflicted."
            ),
            level=level,
            rank=2,
            base_dmg=24
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:

        if not isinstance(unit, DMMonster):
            scalar = unit.life / unit.max_life
            unit.damage(self.dmg * (scalar + 1))  # Make it 100% + whatever the scalar is.

################################################################################

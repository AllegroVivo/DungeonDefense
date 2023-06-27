from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ChainLightning",)

################################################################################
class ChainLightning(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-182",
            name="Chain Lightning",
            description=(
                "Give {value} Shock to 5 nearby enemies and the hero that "
                "entered the room when a hero enters the room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original,
            base_dmg=34,
            effects=[
                Effect(name="Shock", base=32, per_lv=24)
            ]
        )

        # Note: Also deals 1~34 (+0~33 per Lv) damage.
        # Will assume it's toward all targets.

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        heroes = []
        for room in self.adjacent_rooms:
            heroes.extend(room.heroes)

        # Select 5 targets.
        targets = self.random.sample(heroes, 5, exclude=unit)

        # Add the triggering hero into the list.
        targets.append(unit)

        for target in targets:
            target.damage(self.dmg)
            target.add_status("Shock", self.effects["Shock"], self)

################################################################################

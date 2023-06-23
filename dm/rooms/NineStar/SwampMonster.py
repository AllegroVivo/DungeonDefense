from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..traproom   import DMTrapRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwampMonster",)

################################################################################
class SwampMonster(DMTrapRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-232",
            name="Swamp Monster",
            description=(
                "Inflict {damage} damage to entering heroes, while reducing "
                "target's Armor by 50 % and giving {status} Slow."
            ),
            level=level,
            rank=9,
            unlock=UnlockPack.Adventure,
            base_dmg=91,
            effects=[
                Effect(name="Slow", base=5, per_lv=1),
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        unit.damage(self.damage)
        unit.add_status("Slow", self.effects["Slow"], self)

        armor = unit.get_status("Armor")
        if armor is not None:
            armor.reduce_stacks_pct(0.50)

################################################################################

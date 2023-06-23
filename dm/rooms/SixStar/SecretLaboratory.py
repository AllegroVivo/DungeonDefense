from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SecretLaboratory",)

################################################################################
class SecretLaboratory(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-207",
            name="Secret Laboratory",
            description=(
                "Once recharged, get {value} research points. When 300 research "
                "points are collected, one of your monsters will be enhanced."
            ),
            level=level,
            rank=6,
            unlock=UnlockPack.Myth,
            effects=[
                Effect(name="research", base=5, per_lv=1),
            ]
        )

        self._research: int = 0

        self.setup_charging(4.4, 2.2)

################################################################################
    def on_charge(self) -> None:
        """Called when this room is charged."""

        self._research += self.effects["research"]
        if self._research >= 300:
            self._research -= 300
            self.game.dungeon.upgrade_random_monster(include_inventory=True)

################################################################################

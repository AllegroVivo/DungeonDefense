from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MirrorRoom",)

################################################################################
class MirrorRoom(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-152",
            name="MirrorRoom",
            description=(
                "Gives {mirror} Mirror and {pleasure} Pleasure to deployed "
                "monsters whenever a hero enters."
            ),
            level=level,
            rank=4,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def notify(self, unit: DMUnit) -> None:
        """A general event response function."""

        if unit.room == self:
            if isinstance(unit, DMHero):
                for monster in self.monsters:
                    monster.add_status("Mirror", self.effect_value()[0])
                    monster.add_status("Pleasure", self.effect_value()[1])

################################################################################
    def effect_value(self) -> Tuple[int ,int]:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        mirror = 1 + (1 * self.level)
        pleasure = 20 + (20 * self.level)

        return mirror, pleasure

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("room_enter")

################################################################################

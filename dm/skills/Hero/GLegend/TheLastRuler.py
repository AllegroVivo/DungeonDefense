from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TheLastRuler",)

################################################################################
class TheLastRuler(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-388",
            name="The Last Ruler",
            description=(
                "Apply 1 Immune and Shield to all heroes upon entering the "
                "Battle Room."
            ),
            rank=8,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # Apply 1 Immune and Shield to all allies
            for unit in self.room.units_of_type(self.owner, inverse=True):
                for status in ("Immune", "Shield"):
                    unit.add_status(status, 1, self)

################################################################################

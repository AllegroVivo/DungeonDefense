from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, RoomType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HolyWarrior",)

################################################################################
class HolyWarrior(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-334",
            name="Holy Warrior",
            description=(
                "Gain 3 Hatred, 3 Shield when entering the Battle Room."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # Apply statuses.
            for status in ("Hatred", "Shield"):
                self.owner.add_status(status, 3, self)

################################################################################

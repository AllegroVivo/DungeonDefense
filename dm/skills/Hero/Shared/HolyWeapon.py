from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HolyWeapon",)

################################################################################
class HolyWeapon(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-342",
            name="Holy Weapon",
            description=(
                "Gain 30 Hatred and Quick upon entering the Dark Lord's Room."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("boss_room_entered")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we're the one who's entered the Dark Lord's room
        if self.owner == unit:
            # Apply statuses.
            for status in ("Hatred", "Quick"):
                self.owner.add_status(status, 30, self)

################################################################################

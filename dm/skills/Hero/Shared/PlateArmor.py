from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PlateArmor",)

################################################################################
class PlateArmor(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-331",
            name="Plate Armor",
            description=(
                "Gain Armor as much as 30 % of maximum LIFE at the beginning "
                "of the battle, but also gain 3 Slow."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            self.owner.add_status("Armor", self.owner.max_life * 0.30, self)
            self.owner.add_status("Slow", 3, self)

################################################################################

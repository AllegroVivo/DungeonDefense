from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LeatherArmor",)

################################################################################
class LeatherArmor(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-329",
            name="Leather Armor",
            description=(
                "Gain Armor as much as 10 % of maximum LIFE at the "
                "beginning of battle, and 1 Dodge."
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
            self.owner.add_status("Armor", self.owner.max_life * 0.10, self)
            self.owner.add_status("Dodge", 1, self)

################################################################################

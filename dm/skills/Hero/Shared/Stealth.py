from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Stealth",)

################################################################################
class Stealth(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-328",
            name="Stealth",
            description=(
                "Gain 1 Hide at the start of the battle."
            ),
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            self.owner.add_status("Hide", 1, self)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Minigun",)

################################################################################
class Minigun(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-368",
            name="Minigun",
            description=(
                "DEX increases by 800 %, but ATK is reduced by 80 %."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("DEX", 8.00)
        self.owner.reduce_stat_pct("ATK", 0.80)

################################################################################

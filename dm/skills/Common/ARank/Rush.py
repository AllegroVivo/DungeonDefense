from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Rush",)

################################################################################
class Rush(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-166",
            name="Rush",
            description=(
                "DEX increases by 100 %, but ATK is reduced by 50 %."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("DEX", 1.00)
        self.owner.reduce_stat_pct("ATK", 0.50)

################################################################################

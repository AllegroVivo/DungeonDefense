from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ComboAttack",)

################################################################################
class ComboAttack(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-120",
            name="Combo Attack",
            description=(
                "DEX is decreased by 50 %, but attack count is increased by 2."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.owner.reduce_stat_pct("DEX", 0.50)
        self.owner.increase_stat_flat("num_attacks", 2)

################################################################################

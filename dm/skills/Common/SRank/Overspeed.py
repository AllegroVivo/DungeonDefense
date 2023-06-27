from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import UnlockPack, CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Overspeed",)

################################################################################
class Overspeed(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-194",
            name="Overspeed",
            description=(
                "Default DEX increases by 40 %."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
            unlock=UnlockPack.Awakening
        )

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("DEX", 0.40)

################################################################################

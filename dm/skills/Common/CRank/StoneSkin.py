from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("StoneSkin",)

################################################################################
class StoneSkin(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-108",
            name="Stone Skin",
            description="DEF increases by 5 (+0.25*Lv).",
            rank=1,
            cooldown=CooldownType.Passive
        )

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_flat("DEF", int(5 + (0.25 * self.owner.level)))

################################################################################

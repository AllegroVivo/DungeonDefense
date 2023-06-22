from __future__ import annotations


from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
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
            description="(Passive) DEF increases by 5 (+0.25*Lv).",
            rank=1,
            cooldown=0
        )

################################################################################
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        return int(5 + (0.25 * self.owner.level))

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        self.owner.increase_stat_flat("DEF", self.effect_value())

################################################################################

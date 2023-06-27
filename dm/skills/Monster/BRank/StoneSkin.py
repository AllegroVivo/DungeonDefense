from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("StoneSkin",)

################################################################################
class StoneSkin(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-230",
            name="Stone Skin",
            description=(
                "DEF increases by 5 (+0.25*Lv)."
            ),
            rank=3,
            cooldown=CooldownType.Passive,
            # Can't use the SkillEffect here because we're multiplying by the
            # unit's level, not the unit's ATK.
        )

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("DEF", 0.25 * self.owner.level)

################################################################################

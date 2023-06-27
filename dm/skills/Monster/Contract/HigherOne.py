from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HigherOne",)

################################################################################
class HigherOne(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-298",
            name="Higher One",
            description=(
                "Combat ability is doubled, as well as being strongly "
                "resistant to most debuffs."
            ),
            rank=9,
            cooldown=CooldownType.Passive
        )

        # Not sure exactly how high a resistance is meant by "strongly resistant".
        # I'm going to assume 90% for now because that's what auto complete
        # put into the comment and it seems reasonable.

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        if self.owner == ctx.target:
            if self.random.chance(90):
                ctx.will_fail = True

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("Combat", 1.00)  # 100% additional effectiveness.

################################################################################

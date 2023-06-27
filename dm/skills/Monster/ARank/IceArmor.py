from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("IceArmor",)

################################################################################
class IceArmor(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-244",
            name="IceArmor",
            description=(
                "DEF increases by 5 (+0.25*Lv). Apply 1 Slow to attackers."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.source.add_status("Slow", 1, self)

################################################################################
    def stat_adjust(self) -> None:

        self.owner.increase_stat_pct("DEF", 5 + (0.25 * self.owner.level))

################################################################################

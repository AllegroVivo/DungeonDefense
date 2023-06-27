from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SpiderWeb",)

################################################################################
class SpiderWeb(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-268",
            name="Spider Web",
            description=(
                "Apply 15 Vulnerable and Slow to heroes entering the room. "
                "Also, damage inflicted to enemies in Slow state increases "
                "by 100 %."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("boss_room_entered")
        self.listen("on_attack", self.on_attack)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        unit.add_status("Vulnerable", 15, self)
        unit.add_status("Slow", 15, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            slow = ctx.target.get_status("Slow")
            if slow is not None:
                ctx.amplify_pct(1.00)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AbysmalCurse",)

################################################################################
class AbysmalCurse(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-267",
            name="Abysmal Curse",
            description=(
                "Apply 3 Dull to heroes entering the dungeon. Also, damage "
                "received from enemies in Slow or Dull state will decrease "
                "by 50 %."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn", self.hero_spawn)
        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            slow = ctx.target.get_status("Slow")
            dull = ctx.target.get_status("Dull")
            if slow is not None or dull is not None:
                ctx.amplify_pct(0.50)

################################################################################
    def hero_spawn(self, unit: DMUnit) -> None:

        unit.add_status("Dull", 3, self)

################################################################################

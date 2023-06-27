from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BlackCurtain",)

################################################################################
class BlackCurtain(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-275",
            name="Black Curtain",
            description=(
                "Apply 5 Haze to heroes entering the dungeon. Also, damage "
                "inflicted to enemies under the effect of Haze is increased "
                "by 100 %."
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

        if self.owner == ctx.source:
            haze = ctx.target.get_status("Haze")
            if haze is not None:
                ctx.amplify_pct(1.00)

################################################################################
    def hero_spawn(self, unit: DMUnit) -> None:

        unit.add_status("Haze", 5, self)

################################################################################

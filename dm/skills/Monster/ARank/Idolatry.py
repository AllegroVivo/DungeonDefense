from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, HealingContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Idolatry",)

################################################################################
class Idolatry(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-245",
            name="Idolatry",
            description=(
                "Damage received decreases by 33% and healing effect received "
                "increases by 100%."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")
        self.listen("on_heal", self.on_heal)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.mitigate_pct(0.33)

################################################################################
    def on_heal(self, ctx: HealingContext) -> None:

        if self.owner == ctx.target:
            ctx.amplify_pct(1.00)

################################################################################

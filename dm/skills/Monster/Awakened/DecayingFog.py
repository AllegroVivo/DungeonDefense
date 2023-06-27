from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DecayingFog",)

################################################################################
class DecayingFog(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-317",
            name="Decaying Fog",
            description=(
                "ATK of enemies in Weak state decrease by 50 %. Damage "
                "received by enemy with Vulnerable state increase by 3 % per "
                "Vulnerable given."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.target, DMHero):
            vulnerable = ctx.target.get_status("Vulnerable")
            if vulnerable is not None:
                ctx.amplify_pct(vulnerable.stacks * 0.03)

################################################################################
    def stat_adjust(self) -> None:

        for hero in self.game.all_heroes:
            weak = hero.get_status("Weak")
            if weak is not None:
                hero.reduce_stat_pct("ATK", 0.50)

################################################################################

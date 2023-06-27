from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FreezingCurse",)

################################################################################
class FreezingCurse(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-311",
            name="Freezing Curse",
            description=(
                "Applies 1 Stun to any hero that attacked an ally in the "
                "dungeon. Also, enemies in Stun state receive 200 % extra "
                "damage. This effect is dungeon wide."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMHero):
            if isinstance(ctx.target, DMMonster):
                ctx.source.add_status("Stun", 1, self)
        elif isinstance(ctx.target, DMHero):
            stun = ctx.target.get_status("Stun")
            if stun is not None:
                ctx.amplify_pct(2.00)  # 200 % extra damage

################################################################################

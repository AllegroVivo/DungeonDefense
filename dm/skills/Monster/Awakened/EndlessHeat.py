from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("EndlessHeat",)

################################################################################
class EndlessHeat(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-308",
            name="Endless Heat",
            description=(
                "Enemy in the dungeon receives 2(+2.0*ATK) Burn each time "
                "it takes an action."
            ),
            rank=10,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=2, scalar=2.0)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if isinstance(ctx.source, DMHero):
            ctx.source.add_status("Burn", self.effect, self)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DeepRoots",)

################################################################################
class DeepRoots(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-274",
            name="Deep Roots",
            description=(
                "Inflict 22 (+2.0*ATK) damage and apply 1 Chained to all "
                "enemies in combat. Also, apply 1 Chained to attacking enemies."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=22, scalar=2.0)
        )

        # I'm making the assumption that the application of 1 Chained to attacking
        # enemies implies that this portion of the skill is passive and applied
        # to all attacks, which means we need an on_attack hook.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.game.all_heroes:
            unit.damage(self.effect)
            unit.add_status("Chained", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.source.add_status("Chained", 1, self)

################################################################################

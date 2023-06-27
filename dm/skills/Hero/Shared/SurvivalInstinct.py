from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SurvivalInstinct",)

################################################################################
class SurvivalInstinct(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-344",
            name="Survival Instinct",
            description=(
                "Restore 30 (+3.0*ATK) LIFE and leave the battle immediately. "
                "Not effective in the Dark Lord's Room."
            ),
            rank=5,
            cooldown=CooldownType.SingleTarget,
            effect=SkillEffect(base=30, scalar=3.0)
        )

        # I'm making an assumption that "leaving the battle" means disengaging
        # from the current enemy and not entirely leaving the dungeon.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.room == self.game.dungeon.map.boss_tile:
            return

        if self.owner == ctx.source:
            self.owner.heal(self.effect)
            self.owner.disengage()

################################################################################

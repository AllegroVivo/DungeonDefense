from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FireStorm",)

################################################################################
class FireStorm(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-270",
            name="Fire Storm",
            description=(
                "Inflict 48 (+0.8*ATK) damage and apply 36 (+2.0*ATK) Burn to "
                "all enemies in the dungeon. Also, damage received from enemies "
                "under the effect of Burn is reduced by 30 %."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide,
            effect=SkillEffect(base=48, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            hero.damage(self.effect)
            hero.add_status("Burn", 36, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            burn = ctx.target.get_status("Burn")
            if burn is not None:
                ctx.mitigate_pct(0.30)

################################################################################

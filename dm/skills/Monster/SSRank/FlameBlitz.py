from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FlameBlitz",)

################################################################################
class FlameBlitz(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-277",
            name="Flame Blitz",
            description=(
                "Apply 20 (+1.0*ATK) Burn to heroes entering the dungeon. "
                "Also, gain 2 Acceleration from attacking enemies under the "
                "effect of Burn."
            ),
            rank=6,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=20, scalar=1.0)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")
        self.listen("on_attack", self.on_attack)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        unit.add_status("Burn", self.effect, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            burn = ctx.source.get_status("Burn")
            if burn is not None:
                self.owner.add_status("Acceleration", 2, self)

################################################################################

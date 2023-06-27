from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SuperconductiveSpirit",)

################################################################################
class SuperconductiveSpirit(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-264",
            name="Superconductive Spirit",
            description=(
                "Apply 6 (+0.6*Lv) Shock and 1 Recharge to all enemies in the "
                "dungeon when hit. Damage received is decreased by 60 %."
            ),
            rank=5,
            cooldown=CooldownType.Passive,
            passive=True,
            effect=SkillEffect(base=6, scalar=0.6)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.mitigate_pct(0.60)
            for unit in self.room.units_of_type(self.owner, inverse=True):
                unit.add_status("Shock", self.effect, self)
                unit.add_status("Recharge", 1, self)

################################################################################

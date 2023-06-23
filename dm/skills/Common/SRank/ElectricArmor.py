from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect, UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElectricArmor",)

################################################################################
class ElectricArmor(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-191",
            name="Electric Armor",
            description=(
                "Apply 10 (+1*ATK) Shock to all enemies in the room when "
                "you receive damage."
            ),
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=10, scalar=1),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            for unit in ctx.room.units_of_type(self.owner, inverse=True):
                unit.add_status("Shock", self.effect, self)

################################################################################

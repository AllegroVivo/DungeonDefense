from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, UnlockPack, CooldownType

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
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=10, scalar=1),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're defending, wait for damage to be dealt
        if self.owner == ctx.target:
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        # If damage is being applied
        if not ctx.will_fail:
            # Apply Shock to all enemies in the room
            for unit in ctx.room.units_of_type(self.owner, inverse=True):
                unit.add_status("Shock", self.effect, self)

################################################################################

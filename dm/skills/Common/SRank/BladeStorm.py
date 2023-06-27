from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BladeStorm",)

################################################################################
class BladeStorm(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-175",
            name="Blade Storm",
            description=(
                "Inflict 9 (+1.0*ATK) damage to all enemies in the room. "
                "Repeat 3 times."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=9, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Get all enemies in the current room
        targets = ctx.room.units_of_type(self.owner, inverse=True)
        # Damage each of them 3x
        for unit in targets:
            for _ in range(3):
                unit.damage(self.effect)

################################################################################

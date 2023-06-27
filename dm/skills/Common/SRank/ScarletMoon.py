from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ScarletMoon",)

################################################################################
class ScarletMoon(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-185",
            name="Scarlet Moon",
            description=(
                "Apply 8 (+0.8*ATK) Vampire, 2 Bloodlust to all allies in "
                "the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=8, scalar=0.8)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For each ally in the room
        for unit in ctx.room.units_of_type(self.owner):
            # Apply Vampire
            unit.add_status("Vampire", self.effect, self)
            # Apply Bloodlust
            unit.add_status("Bloodlust", 2, self)

################################################################################

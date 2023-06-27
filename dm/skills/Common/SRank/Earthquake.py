from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Earthquake",)

################################################################################
class Earthquake(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-178",
            name="Earthquake",
            description=(
                "Inflict 16 (+1.2*ATK) damage and apply 2 Stun to all "
                "enemies in the room."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
            effect=SkillEffect(base=16, scalar=1.2)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Get all enemies in the current room
        targets = ctx.room.units_of_type(self.owner, inverse=True)
        for unit in targets:
            # Damage each of them
            unit.damage(self.effect)
            # And apply Stun
            unit.add_status("Stun", 2, self)

################################################################################

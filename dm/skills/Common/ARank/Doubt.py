from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Doubt",)

################################################################################
class Doubt(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-150",
            name="Doubt",
            description=(
                "Inflict 16 (+1.5*ATK) damage and apply 3 Obey to all enemies "
                "in the room."
            ),
            rank=2,
            cooldown=4,
            effect=SkillEffect(base=16, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for target in ctx.room.units_of_type(self.owner, inverse=True):
            target.damage(self.effect)
            target.add_status("Obey", 3, self)

################################################################################

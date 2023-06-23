from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ArmorBreak",)

################################################################################
class ArmorBreak(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-114",
            name="Armor Break",
            description=(
                "Inflict 16 (+3.0*ATK) damage and apply 3 Fragile to an enemy."
            ),
            rank=2,
            cooldown=0,
            effect=SkillEffect(base=16, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Fragile", 3, self)

################################################################################

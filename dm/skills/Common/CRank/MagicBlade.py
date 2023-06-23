from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicBlade",)

################################################################################
class MagicBlade(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-105",
            name="Magic Blade",
            description=(
                "Inflict 8 (+3.0*ATK) damage and apply 1 Fragile to an enemy."
            ),
            rank=1,
            cooldown=2,
            effect=SkillEffect(base=8, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.target.damage(self.effect)
        ctx.target.add_status("Fragile", 1, self)

################################################################################

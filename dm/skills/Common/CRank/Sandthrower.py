from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sandthrower",)

################################################################################
class Sandthrower(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-106",
            name="Sandthrower",
            description=(
                "Inflict 8 (+3.0*ATK) damage and apply 1 Blind to an enemy."
            ),
            rank=1,
            cooldown=2,
            effect=SkillEffect(base=8, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.amplify_flat(self.effect)
        ctx.target.add_status("Blind", 1, self)

################################################################################

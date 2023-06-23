from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicExplosion",)

################################################################################
class MagicExplosion(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-161",
            name="Magic Explosion",
            description=(
                "Inflict 20 (+1.5*ATK) damage to all enemies in the room."
            ),
            rank=2,
            cooldown=4,
            effect=SkillEffect(base=20, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in ctx.room.units_of_type(self.owner, inverse=True):
            unit.damage(self.effect)

################################################################################

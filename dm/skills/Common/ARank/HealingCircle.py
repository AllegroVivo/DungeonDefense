from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HealingCircle",)

################################################################################
class HealingCircle(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-160",
            name="Healing Circle",
            description=(
                "Recover 30 (+1.5*ATK) LIFE of all allies in the room."
            ),
            rank=2,
            cooldown=4,
            effect=SkillEffect(base=30, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in ctx.room.units_of_type(self.owner):
            unit.heal(self.effect)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SpinStrike",)

################################################################################
class SpinStrike(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-141",
            name="Spin Strike",
            description=(
                "Inflict 24 (+1.5*ATK) damage to all enemies in the room."
            ),
            rank=2,
            cooldown=4,
            effect=SkillEffect(base=24, scalar=1.5)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in ctx.room.get_heroes_or_monsters(self.owner, inverse=True):
            unit.damage(self.effect)

################################################################################

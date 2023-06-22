from __future__ import annotations

import random

from typing     import TYPE_CHECKING
from ....core.objects.monster import DMMonster
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicArrow",)

################################################################################
class MagicArrow(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-104",
            name="Magic Arrow",
            description=(
                "Inflict 4 (+3.0*ATK) damage to a random enemy. Repeat 3 times."
            ),
            rank=1,
            cooldown=2
        )

################################################################################
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        return 4 + (3 * self.owner.attack)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        source = ctx.room.heroes if isinstance(ctx.source, DMMonster) else ctx.room.monsters
        for _ in range(4):  # 3 repeats to make 4 total
            target = random.choice(source)
            target.damage(self.effect_value())

################################################################################

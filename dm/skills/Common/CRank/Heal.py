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

__all__ = ("Heal",)

################################################################################
class Heal(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-103",
            name="Heal",
            description="Recover 15 (+3.0*ATK) LIFE of ally.",
            rank=1,
            cooldown=2
        )

################################################################################
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        return 15 + (3 * self.owner.attack)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        source = (
            ctx.room.heroes if isinstance(ctx.source, DMMonster)
            else ctx.room.monsters
        )
        target = random.choice(source)
        target.heal(self.effect_value())

################################################################################

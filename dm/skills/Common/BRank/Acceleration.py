from __future__ import annotations

import random
from typing     import TYPE_CHECKING
from dm.core.objects.monster import DMMonster
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AccelerationSkill",)

################################################################################
class AccelerationSkill(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-112",
            name="Acceleration",
            description="Apply 4 Acceleration to ally.",
            rank=2,
            cooldown=2
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        source = ctx.room.monsters if isinstance(ctx.source, DMMonster) else ctx.room.heroes
        target = random.choice(source)
        target.add_status("Acceleration", 4, self)

################################################################################

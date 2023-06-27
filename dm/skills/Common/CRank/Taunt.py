from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Taunt",)

################################################################################
class Taunt(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-110",
            name="Taunt",
            description="Gain 10 Taunt.",
            rank=1,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        self.owner.add_status("Taunt", 10, self)

################################################################################

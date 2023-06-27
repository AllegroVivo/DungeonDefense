from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CunningWhisper",)

################################################################################
class CunningWhisper(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-196",
            name="Cunning Whisper",
            description=(
                "Apply 3 Haze to an enemy."
            ),
            rank=1,
            cooldown=CooldownType.SingleTarget,
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.target.add_status("Haze", 3, self)

################################################################################

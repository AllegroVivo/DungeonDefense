from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RuneProtection",)

################################################################################
class RuneProtection(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-207",
            name="Rune Protection",
            description=(
                "Gain 3 Shield, 3 Immune."
            ),
            rank=2,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        self.owner.add_status("Shield", 3, self)
        self.owner.add_status("Immune", 3, self)

################################################################################

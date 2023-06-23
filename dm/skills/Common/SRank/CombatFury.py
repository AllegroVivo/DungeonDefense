from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect, UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CombatFury",)

################################################################################
class CombatFury(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-189",
            name="Combat Fury",
            description=(
                "Gain 20 (+1*ATK) Fury every time you attack an enemy."
            ),
            rank=2,
            cooldown=0,
            passive=True,
            effect=SkillEffect(base=20, scalar=1),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            self.owner.add_status("Fury", self.effect, self)

################################################################################

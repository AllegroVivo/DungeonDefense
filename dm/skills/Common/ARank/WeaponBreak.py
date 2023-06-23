from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("WeaponBreak",)

################################################################################
class WeaponBreak(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-172",
            name="Weapon Break",
            description=(
                "Inflict 16 (+3.0*ATK) damage and apply 3 Weak to the enemy."
            ),
            rank=2,
            cooldown=2,
            effect=SkillEffect(base=16, scalar=3.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.target.damage(self.effect)
            ctx.target.add_status("Weak", 3, self)

################################################################################

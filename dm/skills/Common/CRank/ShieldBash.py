from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill
from utilities import SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ShieldBash",)

################################################################################
class ShieldBash(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-107",
            name="Shield Bash",
            description=(
                "Apply 12 (+3.0*ATK) damage to target, and apply additional "
                "damage as much as 100 % of Armor applied to self."
            ),
            rank=1,
            cooldown=2,
            effect=SkillEffect(base=12, scalar=3)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        damage = self.effect
        armor = self.owner.get_status("Armor")
        if armor is not None:
            damage += armor.stacks
        ctx.amplify_flat(damage)

################################################################################

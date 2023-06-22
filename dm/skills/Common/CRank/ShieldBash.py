from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

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
            cooldown=2
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        ctx.amplify_flat(self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        damage = 12 + (3 * self.owner.attack)
        armor = self.owner.get_status("Armor")
        if armor is not None:
            damage += armor.stacks

        return damage

################################################################################

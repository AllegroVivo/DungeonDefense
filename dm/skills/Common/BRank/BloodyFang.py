from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BloodyFang",)

################################################################################
class BloodyFang(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-116",
            name="Bloody Fang",
            description=(
                "Inflict 12 (+3.0*ATK) damage to an enemy, and then inflict "
                "additional damage as much as Vampire."
            ),
            rank=2,
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
        vampire = self.owner.get_status("Vampire")
        if vampire is not None:
            damage += vampire.stacks

        return damage

################################################################################

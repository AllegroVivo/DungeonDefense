from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ArmorBreak",)

################################################################################
class ArmorBreak(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-114",
            name="Armor Break",
            description=(
                "Inflict 16 (+3.0*ATK) damage and apply 3 Fragile to an enemy."
            ),
            rank=2,
            cooldown=0
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        ctx.amplify_flat(self.effect_value())
        ctx.add_status("Fragile", 3)

################################################################################
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        return 16 + (3 * self.owner.attack)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Sandthrower",)

################################################################################
class Sandthrower(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-106",
            name="Sandthrower",
            description=(
                "Inflict 8 (+3.0*ATK) damage and apply 1 Blind to an enemy."
            ),
            rank=1,
            cooldown=2
        )

################################################################################
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        return 8 + (3 * self.owner.attack)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        ctx.amplify_flat(self.effect_value())
        ctx.add_status("Blind", 1)

################################################################################

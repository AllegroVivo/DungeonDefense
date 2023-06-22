from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ChosenOne",)

################################################################################
class ChosenOne(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-119",
            name="Chosen One",
            description=(
                "(Passive) When attacking enemy, inflict extra damage as much "
                "as 5 % per Curse stack while reducing Curse stack by 5."
            ),
            rank=2,
            cooldown=1
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        ctx.amplify_pct(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this skill."""

        curse = self.owner.get_status("Curse")
        if curse is None:
            return 0

        effect = (5 * curse.stacks)
        curse.reduce_stacks_flat(5)

        return effect / 100  # Convert to percentage

################################################################################

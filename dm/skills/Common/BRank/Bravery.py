from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Bravery",)

################################################################################
class Bravery(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-118",
            name="Bravery",
            description=(
                "(Passive) When attacking enemy, inflict extra damage as much "
                "as 5 % per Panic stack while reducing Panic stack by 5."
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

        panic = self.owner.get_status("Panic")
        if panic is None:
            return 0

        effect = (5 * panic.stacks)
        panic.reduce_stacks_flat(5)

        return effect / 100  # Convert to percentage

################################################################################

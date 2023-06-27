from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

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
                "When attacking enemy, inflict extra damage as much "
                "as 5 % per Panic stack while reducing Panic stack by 5."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # And if we're under the effect of Panic
            panic = self.owner.get_status("Panic")
            if panic is None:
                return

            # Deal extra damage based on the number of Panic stacks we have.
            ctx.amplify_pct((5 * panic.stacks) / 100)
            # Reduce the number of Panic stacks by 5.
            panic.reduce_stacks_flat(5)

################################################################################

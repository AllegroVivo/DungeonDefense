from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

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
                "When attacking enemy, inflict extra damage as much "
                "as 5 % per Curse stack while reducing Curse stack by 5."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # And if we're under the effect of Curse
            curse = self.owner.get_status("Curse")
            if curse is None:
                return

            # Deal extra damage based on the number of Curse stacks we have.
            ctx.amplify_pct((5 * curse.stacks) / 100)
            # Reduce the number of Curse stacks by 5.
            curse.reduce_stacks_flat(5)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GoddessAdvent",)

################################################################################
class GoddessAdvent(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-411",
            name="Goddess Advent",
            description=(
                "Does not receive any damage while other heroes are alive."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If the Goddess is the target of the attack
        if self.owner == ctx.target:
            # If there are more heroes alive than just the Goddess
            if len(self.game.all_heroes) > 1:
                # Nullify damage.
                ctx.will_fail = True

################################################################################

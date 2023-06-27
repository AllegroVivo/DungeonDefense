from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Salvation",)

################################################################################
class Salvation(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-365",
            name="Salvation",
            description=(
                "Recover all of target's LIFE, and apply Armor as much as "
                "100 % of the restored LIFE"
            ),
            rank=5,
            cooldown=CooldownType.SingleTarget
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Fully heal ourselves
            diff = self.owner.life - self.owner.max_life
            self.owner.heal(diff)
            # And add Armor equal to the restored LIFE value.
            self.owner.add_status("Armor", diff, self)

################################################################################

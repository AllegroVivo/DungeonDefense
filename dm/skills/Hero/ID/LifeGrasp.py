from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LifeGrasp",)

################################################################################
class LifeGrasp(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-395",
            name="Life Grasp",
            description=(
                "Always affected by Elasticity and Rebound. Gains 5 Defense "
                "with each damage taken."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the target
        if self.owner == ctx.target:
            # Add Elasticity and Rebound if not present.
            elasticity = self.owner.get_status("Elasticity")
            if elasticity is None:
                self.owner.add_status("Elasticity", 1, self)
            rebound = self.owner.get_status("Rebound")
            if rebound is None:
                self.owner.add_status("Rebound", 1, self)
        # If we're being attacked, wait for damage.
        else:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was received
        if ctx.damage > 0:
            # Apply Defense equal to that damage.
            self.owner.add_status("Defense", ctx.damage * 5, self)

################################################################################

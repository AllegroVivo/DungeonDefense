from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ElasticArmor",)

################################################################################
class ElasticArmor(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-152",
            name="Elastic Armor",
            description=(
                "Gain 10 Elasticity at the beginning of battle. Upon "
                "receiving 2nd damage, gain 1 Elasticity."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

        self._times_damaged: int = 0

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            self._times_damaged += 1
            if self._times_damaged % 2 == 0:
                self.owner.add_status("Elasticity", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Add Elasticity.
            self.owner.add_status("Elasticity", 10, self)

################################################################################

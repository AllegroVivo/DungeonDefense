from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Illusion",)

################################################################################
class Illusion(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-180",
            name="Illusion",
            description=(
                "Gain 5 Phantom at the beginning of battle. Upon receiving "
                "2nd damage, gain 1 Phantom."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage is being dealt
        if not ctx.will_fail:
            # If we've been hit 2 times
            if self.atk_count % 2 == 0:
                # Apply Phantom
                self.owner.add_status("Phantom", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Apply Phantom
            self.owner.add_status("Phantom", 5, self)

################################################################################

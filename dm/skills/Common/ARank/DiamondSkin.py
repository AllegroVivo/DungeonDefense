from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("DiamondSkin",)

################################################################################
class DiamondSkin(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-151",
            name="Diamond Skin",
            description=(
                "Gain 1 Absorption at the beginning of battle. Gain 1 "
                "Absorption when damage is received 2 times."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

        self._times_damaged: int = 0

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If the owner is the target of the attack
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if ctx.damage > 0:
            self._times_damaged += 1
            # If it's the 2nd time damage has been received
            if self._times_damaged % 2 == 0:
                # Add Absorption.
                self.owner.add_status("Absorption", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Add Absorption.
            self.owner.add_status("Absorption", 1, self)

################################################################################

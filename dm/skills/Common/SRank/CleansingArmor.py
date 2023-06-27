from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CleansingArmor",)

################################################################################
class CleansingArmor(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-176",
            name="Cleansing Armor",
            description=(
                "Gain 5 Immune at the beginning of battle. Upon receiving "
                "4th damage, gain 1 Immune."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

        self._hit_count: int = 0

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the target, register callback
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage is being dealt
        if not ctx.will_fail:
            # If we've been hit 4 times
            if self.atk_count % 4 == 0:
                # Apply Immune
                self.owner.add_status("Immune", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Apply Immune
            self.owner.add_status("Immune", 5, self)

################################################################################

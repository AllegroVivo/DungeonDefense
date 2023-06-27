from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SteelSkin",)

################################################################################
class SteelSkin(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-142",
            name="Steel Skin",
            description=(
                "Gain 1 Absorption at the beginning of battle. Gain 1 additional"
                "Absorption after damage is received 3 times."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

        self._hit_count: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're defending
        if self.owner == ctx.target:
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if ctx.damage > 0:
            # Increment our hit count
            self._hit_count += 1
            # If we're on the 3rd hit
            if self._hit_count % 3 == 0:
                # Gain Absorption
                self.owner.add_status("Absorption", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Gain Absorption
            self.owner.add_status("Absorption", 1, self)

################################################################################

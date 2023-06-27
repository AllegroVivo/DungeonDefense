from __future__ import annotations

from datetime import datetime

from typing     import TYPE_CHECKING, Optional
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AbsoluteEvasion",)

################################################################################
class AbsoluteEvasion   (HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-398",
            name="Absolute Evasion",
            description=(
                "Only receives damage from 1 attack per 0.5 second. Gains 4 "
                "Focus and Hatred with each damage taken."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        self._dmg_time: Optional[datetime] = None

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking, register a callback
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If 0.5 seconds has passed since last damage
        if abs(self._dmg_time - datetime.now()).total_seconds() > 0.5:
            # Reset the timer
            self._dmg_time = datetime.now()
            # Apply Focus and Hatred
            for status in ("Focus", "Hatred"):
                self.owner.add_status(status, 4, self)
        # Otherwise it will fail.
        else:
            ctx.will_fail = True

################################################################################

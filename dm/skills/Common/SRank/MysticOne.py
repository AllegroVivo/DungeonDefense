from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MysticOne",)

################################################################################
class MysticOne(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-183",
            name="Mystic One",
            description=(
                "Become immune to Stun, Haze, and Charm."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're being targeted with a status
        if self.owner == ctx.target:
            # And it's one of the statuses we're immune to
            if ctx.status.name in ("Stun", "Haze", "Charm"):
                # Negate it.
                ctx.will_fail = True

################################################################################

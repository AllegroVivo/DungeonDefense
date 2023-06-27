from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Faith",)

################################################################################
class Faith(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-349",
            name="Faith",
            description=(
                "Become immune to Charm, Panic, and Corruption."
            ),
            rank=4,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the target of a status
        if self.owner == ctx.target:
            # If the status is Charm, Panic, or Corruption
            if ctx.status.name in ("Charm", "Panic", "Corruption"):
                # Fail it.
                ctx.will_fail = True

################################################################################

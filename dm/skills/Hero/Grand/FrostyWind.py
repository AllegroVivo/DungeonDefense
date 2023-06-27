from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FrostyWind",)

################################################################################
class FrostyWind(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-360",
            name="Frosty Wind",
            description=(
                "Become immune to Slow. Apply 8 Slow to all monsters upon "
                "entering the battle room."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")
        self.listen("status_applied", self.status_applied)

################################################################################
    def status_applied(self, ctx: StatusApplicationContext) -> None:

        # If we're the target of Slow
        if self.owner == ctx.target:
            if ctx.status.name == "Slow":
                # Nullify it
                ctx.will_fail = True

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # Apply Slow to all enemies
            for unit in unit.room.units_of_type(self.owner, inverse=True):
                unit.add_status("Slow", 8, self)

################################################################################

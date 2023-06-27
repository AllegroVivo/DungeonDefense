from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ExpulsionCeremony",)

################################################################################
class ExpulsionCeremony(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-372",
            name="Expulsion Ceremony",
            description=(
                "Remove all buff from all enemies in the room and give them "
                "5 Curse. Also, become immune to Haze and Charm."
            ),
            rank=6,
            cooldown=CooldownType.RoomWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Remove all buffs from all enemies in the room
        for unit in self.room.units_of_type(self.owner, inverse=True):
            buffs = [
                status for status in unit.statuses
                if status._type in (StatusType.Buff, StatusType.AntiDebuff)
            ]
            for buff in buffs:
                buff.deplete_all_stacks()

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're being targeted by a status
        if self.owner == ctx.target:
            # If it's Haze or Charm
            if ctx.status.name in ("Haze", "Charm"):
                # Cancel the application
                ctx.will_fail = True

################################################################################

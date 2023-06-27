from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PurificationCeremony",)

################################################################################
class PurificationCeremony(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-380",
            name="Purification Ceremony",
            description=(
                "Remove all debuff from all allies in the room and give them "
                "5 Immune. Also, become immune to Haze and Charm."
            ),
            rank=7,
            cooldown=CooldownType.RoomWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # For every ally in the room, remove all debuffs and apply 5 Immune.
        for unit in self.room.units_of_type(self.owner):
            debuffs = [s for s in unit.statuses if s._type in (StatusType.Debuff, StatusType.AntiBuff)]
            for status in debuffs:
                status.deplete_all_stacks()
            unit.add_status("Immune", 5, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we are the target of Haze or Charm, it will fail.
        if self.owner == ctx.target:
            if ctx.status.name in ("Haze", "Charm"):
                ctx.will_fail = True

################################################################################

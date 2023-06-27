from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GoddessAdvent",)

################################################################################
class GoddessAdvent(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-386",
            name="Goddess Advent",
            description=(
                "Apply 15 Obey and Charm to all monsters upon entering the "
                "Battle Room. Apply 1 Mirror to all heroes upon death."
            ),
            rank=8,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter", self.room_enter)
        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If the own of this skill is killed
        if self.owner == ctx.target:
            # Apply 1 Mirror to all allies
            for unit in self.game.units_of_type(self.owner):
                unit.add_status("Mirror", 1, self)

################################################################################
    def room_enter(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # Apply 15 Obey and Charm to all opponents
            for unit in self.room.units_of_type(self.owner, inverse=True):
                for status in ("Obey", "Charm"):
                    unit.add_status(status, 15, self)

################################################################################

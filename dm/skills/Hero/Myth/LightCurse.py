from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LightCurse",)

################################################################################
class LightCurse(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-390",
            name="Light Curse",
            description=(
                "When entering the dungeon, Immune applied to all enemies is "
                "changed to Curse and applies 10 Panic. Curse or Panic applied "
                "to self is changed to Quick."
            ),
            rank=9,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")
        self.listen("status_applied", self.status_applied)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we're the one entering the dungeon
        if self.owner == unit:
            for unit in self.room.units_of_type(self.owner, inverse=True):
                # If the unit has Immune
                immune = unit.get_status("Immune")
                if immune is not None:
                    # Grab a count of the number of stacks so we can apply Curse
                    # after removing immune (otherwise it will just negate
                    # the application).
                    stack_ct = immune.stacks
                    immune.deplete_all_stacks()
                    unit.add_status("Curse", stack_ct, self)

################################################################################
    def status_applied(self, ctx: StatusApplicationContext) -> None:

        # If we're having a status applied to us
        if self.owner == ctx.target:
            # If it's Curse or Panic
            if ctx.status.name in ("Curse", "Panic"):
                # Change it to Quick
                self.owner.add_status("Quick", ctx.status.stacks, self)
                # Fail the original status application
                ctx.will_fail = True

################################################################################

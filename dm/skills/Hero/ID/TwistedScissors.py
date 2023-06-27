from __future__ import annotations

from typing     import TYPE_CHECKING, Optional
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("TwistedScissors",)

################################################################################
class TwistedScissors(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-399",
            name="Twisted Scissors",
            description=(
                "Halves all buffs gained by the target when attacking an enemy. "
                "Always affected by Phantom."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        self._target: Optional[DMUnit] = None

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_disengage", self.on_disengage)
        self.listen("status_applied")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # Check for Phantom and apply if necessary
        if self.owner == ctx.target:
            phantom = self.owner.get_status("Phantom")
            if phantom is None:
                self.owner.add_status("Phantom", 1, self)
        # Otherwise, if we're attacking
        else:
            # If we're attacking a new target, cache a reference.
            if self._target != ctx.target:
                self._target = ctx.target

################################################################################
    def on_disengage(self, unit: DMUnit) -> None:

        # If we're disengaging from our target, clear the reference.
        if self._target == unit:
            self._target = None

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If the status is being applied to our target
        if ctx.target == self._target:
            # If the status is a buff
            if ctx.status._type in (StatusType.Buff, StatusType.AntiDebuff):
                # Reduce the stacks by 50%
                ctx.reduce_stacks_pct(0.50)

################################################################################

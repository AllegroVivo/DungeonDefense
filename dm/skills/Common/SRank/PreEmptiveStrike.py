from __future__ import annotations

from typing     import TYPE_CHECKING, Optional
from dm.skills._common import CommonSkill
from utilities import SkillEffect, UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PreEmptiveStrike",)

################################################################################
class PreEmptiveStrike(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-193",
            name="Pre-emptive Strike",
            description=(
                "Deal 4 % additional damage on the first hit to each new "
                "enemy for every stack of Acceleration."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

        self._opponent: Optional[DMUnit] = None

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # If we're attacking a new target, reset the opponent.
        if self.owner == ctx.source and self._opponent != ctx.target:
            self._opponent = ctx.target

            # Then calculate the bonus damage based on the number of stacks
            # of Acceleration.
            acceleration = self.owner.get_status("Acceleration")
            if acceleration is not None:
                self._opponent.damage(acceleration.stacks * 4 / 100)  # 4% per stack.

################################################################################
    def on_acquire(self) -> None:

        # Need to add a listener here to reset the opponent when the owner
        # attacks a new target or after battle.
        # self.listen("after_attack", self.post_attack)  # Or something for disengagement.
        self.listen("battle_end")

################################################################################
    def notify(self) -> None:

        self._opponent = None

################################################################################

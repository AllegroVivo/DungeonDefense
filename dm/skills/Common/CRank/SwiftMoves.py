from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SwiftMoves",)

################################################################################
class SwiftMoves(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-109",
            name="Swift Moves",
            description="(Passive) Gain 1 Dodge when damage is received 4 times.",
            rank=1,
            cooldown=0
        )

        self._damage_counter: int = 0

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        self.listen("after_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if self.owner == ctx.target:
            if ctx.damage > 0:
                self._damage_counter += 1

                if self._damage_counter >= 4:
                    self._damage_counter = 0
                    self.owner.add_status("Dodge", 1, self)

################################################################################

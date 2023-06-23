from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Foresight",)

################################################################################
class Foresight(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-157",
            name="Foresight",
            description=(
                "Gain 1 Dodge when damage is received 2 times."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

        self._hit_counter: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            self._hit_counter += 1
            if self._hit_counter % 2 == 0:
                self.owner.add_status("Dodge", 1, self)

################################################################################

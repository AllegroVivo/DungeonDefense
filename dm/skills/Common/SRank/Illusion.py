from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Illusion",)

################################################################################
class Illusion(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-180",
            name="Illusion",
            description=(
                "Gain 5 Phantom at the beginning of battle. Upon receiving "
                "2nd damage, gain 1 Phantom."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

        self._hit_count: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            self._hit_count += 1
            if self._hit_count % 2 == 0:
                self.owner.add_status("Phantom", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        self.owner.add_status("Phantom", 5, self)

################################################################################

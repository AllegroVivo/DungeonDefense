from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("VowOfDeath",)

################################################################################
class VowOfDeath(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-187",
            name="Vow of Death",
            description=(
                "Gain 3 Immortality at the beginning of battle. Upon "
                "receiving 8th damage, gain 1 Immortality."
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
            if self._hit_count % 8 == 0:
                self.owner.add_status("Immortality", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        self.owner.add_status("Immortality", 3, self)

################################################################################

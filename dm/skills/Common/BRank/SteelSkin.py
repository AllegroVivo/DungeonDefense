from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SteelSkin",)

################################################################################
class SteelSkin(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-142",
            name="Steel Skin",
            description=(
                "Gain 1 Absorption at the beginning of battle. Gain 1 additional"
                "Absorption after damage is received 3 times."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

        self._hit_count: int = 0

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.register_after_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            self._hit_count += 1
            if self._hit_count % 3 == 0:
                self.owner.add_status("Absorption", 1, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        self.owner.add_status("Absorption", 1, self)

################################################################################

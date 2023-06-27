from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Trickery",)

################################################################################
class Trickery(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-232",
            name="Trickery",
            description=(
                "Inflict double damage to an enemy under the effect of Haze or Stun."
            ),
            rank=3,
            cooldown=CooldownType.Passive,
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        haze = ctx.target.get_status("Haze")
        stun = ctx.target.get_status("Stun")
        if haze is not None or stun is not None:
            ctx.amplify_pct(1.00)  # 100% additional damage

################################################################################

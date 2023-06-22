from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("VowBreaker",)

################################################################################
class VowBreaker(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-111",
            name="Vow Breaker",
            description=(
                "Inflict 24 (+3.0*ATK) damage and apply 5 Obey to target."
            ),
            rank=1,
            cooldown=2
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        if self.owner == ctx.source:
            ctx.amplify_flat(self.effect_value())
            ctx.add_status("Obey", 5)

################################################################################

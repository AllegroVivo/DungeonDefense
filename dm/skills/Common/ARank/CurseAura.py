from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CurseAura",)

################################################################################
class CurseAura(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-149",
            name="Curse Aura",
            description=(
                "Apply 1 Curse to enemies that have attacked you or received "
                "damage from you."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        if ctx.damage > 0:
            target = ctx.target if self.owner == ctx.source else ctx.source
            target.add_status("Curse", 1, self)

################################################################################

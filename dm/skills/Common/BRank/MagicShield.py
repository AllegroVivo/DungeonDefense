from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicShield",)

################################################################################
class MagicShield(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-133",
            name="Magic Shield",
            description=(
                "Apply 3 Shield to ally."
            ),
            rank=2,
            cooldown=2
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            target = self.random.choice(ctx.room.get_heroes_or_monsters(self.owner))
            target.add_status("Shield", 3, self)

################################################################################

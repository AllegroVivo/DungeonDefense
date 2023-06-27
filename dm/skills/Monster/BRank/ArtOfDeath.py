from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ArtOfDeath",)

################################################################################
class ArtOfDeath(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-211",
            name="Art of Death",
            description=(
                "Gain 2 Immortality every 3 attacks."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.register_post_execute(self.post_execute)

################################################################################
    def post_execute(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            if self.atk_count % 3 == 0:
                self.owner.add_status("Immortality", 2, self)

################################################################################

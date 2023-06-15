from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.hero import DMHero
from dm.core.objects.monster import DMMonster
from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Betray",)

################################################################################
class Betray(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="DBF-101",
            name="Betray",
            description=(
                "The next attack on ally deals double damage. Stat decreases by "
                "1 per each time ally is damaged."
            ),
            stacks=stacks,
            status_type=DMStatusType.Debuff
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """For use in an AttackContext-based situation. Is always called in
        every battle loop."""

        if self.owner == ctx.attacker:
            if isinstance(self, DMHero):
                if not isinstance(ctx.defender, DMHero):
                    return
            elif not isinstance(ctx.defender, DMMonster):
                return

            ctx.amplify_pct(1.00)  # Double damage
            self.reduce_stacks_by_one()

################################################################################

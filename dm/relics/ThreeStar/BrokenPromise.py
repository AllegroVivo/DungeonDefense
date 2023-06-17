from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("BrokenPromise",)

################################################################################
class BrokenPromise(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-187",
            name="Broken Promise",
            description=(
                "Every time an enemy under the effect of Charm attacks, they "
                "get 1 Obey."
            ),
            rank=3
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If a hero is attacking...
        if isinstance(ctx.attacker, DMHero):
            # Check if the attacker has charm.
            charm = ctx.attacker.get_status("Charm")
            if charm is not None:
                # If so, add 1 Obey.
                ctx.attacker.add_status("Obey", stacks=1)

################################################################################

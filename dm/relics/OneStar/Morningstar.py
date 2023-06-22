from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Morningstar",)

################################################################################
class Morningstar(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-120",
            name="Morningstar",
            description=(
                "Inflict extra damage as much as Thorn possessed when ally is "
                "attacking an enemy."
            ),
            rank=1
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        # If we're a monster attacking a hero
        if isinstance(ctx.source, DMMonster):
            if isinstance(ctx.target, DMHero):
                # And the monster has Thorn
                thorn = ctx.source.get_status("Thorn")
                if thorn is not None:
                    # Amplify the damage by the amount of Thorn stacks
                    ctx.amplify_flat(thorn.stacks)

################################################################################

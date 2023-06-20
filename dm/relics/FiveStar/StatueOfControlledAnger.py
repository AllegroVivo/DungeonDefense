from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.monster import DMMonster
from ...core.objects.relic import DMRelic
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("StatueOfControlledAnger",)

################################################################################
class StatueOfControlledAnger(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-339",
            name="Statue of Controlled Anger",
            description=(
                "All monsters get Fury as much as 50 % of their ATK upon attack."
            ),
            rank=5,
            unlock=UnlockPack.Adventure
        )

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.attacker, DMMonster):
            ctx.attacker.add_status("Fury", ctx.attacker.attack * self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect."""

        return 0.50

################################################################################

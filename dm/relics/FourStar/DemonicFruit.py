from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.hero import DMHero
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from ...core.contexts.attack import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DemonicFruit",)

################################################################################
class DemonicFruit(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-248",
            name="Demonic Fruit",
            description=(
                "Recovers the Dark Lord's LIFE by 1 % if enemy under the effect "
                "of Charm dies."
            ),
            rank=4
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:
        """A general event response function."""

        if isinstance(ctx.target, DMHero):
            charm = ctx.target.get_status("Charm")
            if charm is not None:
                self.game.dark_lord.heal(self.effect_value())

################################################################################
    def effect_value(self) -> float:
        """The value of this relic's effect.

        Breakdown:
        ----------
        **effect = e * l**

        In this function:

        - e is the amount of recovery.
        - l is the Dark Lord's max life.
        """

        return 0.01 * self.game.dark_lord.max_life

################################################################################

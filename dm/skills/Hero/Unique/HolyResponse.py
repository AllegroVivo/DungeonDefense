from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import HealingContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HolyResponse",)

################################################################################
class HolyResponse(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-347",
            name="Holy Response",
            description=(
                "Gain 2 Shield every time LIFE is recovered."
            ),
            rank=3,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_heal")

################################################################################
    def notify(self, ctx: HealingContext) -> None:

        # If we're the target of the heal
        if self.owner == ctx.target:
            # Gain 2 Shield.
            self.owner.add_status("Shield", 2, self)

################################################################################

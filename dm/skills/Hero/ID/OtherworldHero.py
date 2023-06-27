from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("OtherworldHero",)

################################################################################
class OtherworldHero(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-400",
            name="Otherworld Hero",
            description=(
                "Gains 10 Immune and Immortality at the start of battle."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # Gain Immune and Immortality when spawned.
        if self.owner == unit:
            for status in ("Immune", "Immortality"):
                self.owner.add_status(status, 10, self)

################################################################################

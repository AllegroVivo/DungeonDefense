from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("EmergencyHeal",)

################################################################################
class EmergencyHeal(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-102",
            name="Emergency Heal",
            description="Gain 16 (+5.0*ATK) Regeneration.",
            rank=1,
            cooldown=2
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:
        """Called when used on an offensive turn during a battle."""

        pass

################################################################################
    def on_defend(self, ctx: AttackContext) -> None:
        """Called when used on a defensive turn during a battle."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        self.owner.add_status("Regeneration", self.effect_value, self)

################################################################################
    @property
    def effect_value(self) -> int:
        """The value of the effect corresponding to this skill."""

        return 16 + (5 * self.owner.attack)

################################################################################

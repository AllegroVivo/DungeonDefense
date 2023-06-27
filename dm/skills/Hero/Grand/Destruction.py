from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Destruction",)

################################################################################
class Destruction(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-357",
            name="Destruction",
            description=(
                "When you attack the first enemy you encounter in this battle, "
                "apply additional damage as much as 60 % of target's current LIFE."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

        self._activated: bool = False

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_end")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If this is the first enemy of the battle
        if not self._activated:
            # If we're attacking
            if self.owner == ctx.source:
                # Apply additional damage
                ctx.amplify_pct(0.60 * ctx.target.life)
                self._activated = True

################################################################################
    def notify(self) -> None:

        # Reset activation status at the end of the battle
        self._activated = False

################################################################################

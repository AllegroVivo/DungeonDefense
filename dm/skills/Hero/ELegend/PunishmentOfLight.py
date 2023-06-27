from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PunishmentOfLight",)

################################################################################
class PunishmentOfLight(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-381",
            name="Punishment of Light",
            description=(
                "Attack count is increased by 1. Apply 3 Curse and Corruption "
                "whenever damage is done to an enemy. Also, immediately kill "
                "enemies with low LIFE at a low chance."
            ),
            rank=7,
            cooldown=CooldownType.Passive
        )

        # The description states that the instant death may occur at a low chance,
        # but not a *very* low chance, like some other status effects' descriptions
        # state. So, we'll say 10% for now.

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the attacker, register our callback.
        if self.owner == ctx.source:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # Apply 3 Curse and Corruption to the target if they were damaged.
        if ctx.damage > 0:
            for status in ("Curse", "Corruption"):
                ctx.target.add_status(status, 3, self)

################################################################################
    def stat_adjust(self) -> None:

        # Increase the owner's number of attacks by 1.
        self.owner.increase_stat_pct("num_attacks", 1)

################################################################################

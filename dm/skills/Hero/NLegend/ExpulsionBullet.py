from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ExpulsionBullet",)

################################################################################
class ExpulsionBullet(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-373",
            name="Expulsion Bullet",
            description=(
                "Apply 3 Curse and Corruption whenever damage is done to an "
                "enemy. Also, immediately kill enemies with low LIFE at a "
                "low chance."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

        # It's unspecified what "low life" entails, but I'm going with 10%.

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the attacker
        if self.owner == ctx.source:
            # Kill immediately at a 10% chance.
            if self.random.chance(10):
                ctx.target._damage(ctx.target.life)
                return

            # Otherwise, wait for damage
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if not ctx.will_fail:
            # Apply Curse and Corruption
            for status in ("Curse", "Corruption"):
                ctx.target.add_status(status, 3, self)

################################################################################

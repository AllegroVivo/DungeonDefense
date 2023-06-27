from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Fighting",)

################################################################################
class Fighting(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-371",
            name="Fighting",
            description=(
                "Apply 2 Rigidity at 35 % chance when inflicting damage to an "
                "enemy. For every 4th attack, gain 1 Focus, Acceleration, "
                "Dodge, and Mirror."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the attacker
        if self.owner == ctx.source:
            # Register a callback for post-execution
            ctx.register_post_execute(self.callback)

            # If this is the 4th attack
            if self.atk_count % 4 == 0:
                # Apply all the statuses
                for status in ("Focus", "Acceleration", "Dodge", "Mirror"):
                    self.owner.add_status(status, 1, self)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If we've dealt damage
        if not ctx.will_fail:
            # Apply Rigidity at a 35% chance
            if self.random.chance(35):
                ctx.target.add_status("Rigidity", 2, self)

################################################################################

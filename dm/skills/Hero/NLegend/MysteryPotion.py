from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MysteryPotion",)

################################################################################
class MysteryPotion(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-367",
            name="Mystery Potion",
            description=(
                "When attacking enemy, apply Poison as much as LIFE lost from "
                "the target. Also, Corpse Explosion and Poison applied to "
                "self are converted to Regeneration."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Wait for damage
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if not ctx.will_fail:
            # Apply Poison
            self.owner.add_status("Poison", ctx.damage, self)

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the one getting the status
        if self.owner == ctx.target:
            # If it's Corpse Explosion or Poison
            if ctx.status.name in ("Corpse Explosion", "Poison"):
                # Convert it to Regeneration
                self.owner.add_status("Regeneration", ctx.status.stacks, self)
                # And fail the original application
                ctx.will_fail = True

################################################################################

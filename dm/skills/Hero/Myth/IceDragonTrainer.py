from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("IceDragonTrainer",)

################################################################################
class IceDragonTrainer(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-394",
            name="Ice Dragon Trainer",
            description=(
                "Each time an enemy is damaged, changes all Acceleration of "
                "target to Slow and applies 10 Overweight. Also, Slow, "
                "Frostbite, Overweight applied to self is changed to Elasticity."
            ),
            rank=9,
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
            # Change target's Acceleration to Slow
            accel = ctx.target.get_status("Acceleration")
            if accel is not None:
                ctx.target.add_status("Slow", accel.stacks, self)
                accel.deplete_all_stacks()
            # And apply Overweight
            ctx.target.add_status("Overweight", 10, self)

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the target of a status
        if self.owner == ctx.target:
            # If the status is Slow, Frostbite, or Overweight
            if ctx.status.name in ("Slow", "Frostbite", "Overweight"):
                # Change it to Elasticity
                self.owner.add_status("Elasticity", ctx.status.stacks, self)
                # And nullify the original status
                ctx.will_fail = True

################################################################################

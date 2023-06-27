from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MindShatter",)

################################################################################
class MindShatter(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-313",
            name="Mind Shatter",
            description=(
                "Haze ignores Immune. Also, receives 5 % extra damage per Haze "
                "applied when enemy is damaged. This effect is dungeon wide."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")
        self.listen("status_applied", self.status_callback)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # Since the skill specifies that damage is more or less applied
        # at the time of the attack, we need to register a post execute
        # callback to capture the final damage value and apply the additional
        # damage relative to that.
        if isinstance(ctx.target, DMHero):
            haze = ctx.target.get_status("Haze")
            if haze is not None:
                ctx.register_post_execute(self.callback)

################################################################################
    @staticmethod
    def callback(ctx: AttackContext) -> None:

        # Get the status again to make sure it's not gone.
        haze = ctx.target.get_status("Haze")
        if haze is not None:
            # And apply crazy damage if it's still there.
            ctx.target.damage(haze.stacks * 0.05 * ctx.damage)

################################################################################
    def status_callback(self, ctx: StatusApplicationContext) -> None:

        # If we're a hero
        if isinstance(ctx.target, DMHero):
            # And are receiving Haze
            if ctx.status.name == "Haze":
                # Check if we have Immune
                immune = ctx.target.get_status("Immune")
                # If we do, register a late callback to reverse Immune.
                if immune is not None:
                    ctx.register_late_callback(self.reverse_immune)

################################################################################
    @staticmethod
    def reverse_immune(ctx: StatusApplicationContext) -> None:

        # Since we are here, we know that Haze is being applied to a hero with
        # Immune. We need to bypass Immune and un-fail Haze by just bypassing the
        # failure and applying it to the target directly using the private method.
        # We've registered this callback as a late callback so it will execute
        # after all calculations to the status effect and stacks are completed so
        # we ultimately have the finished item that would be applied anyway.
        if ctx.will_fail:
            ctx.target._add_status(ctx.status)

################################################################################

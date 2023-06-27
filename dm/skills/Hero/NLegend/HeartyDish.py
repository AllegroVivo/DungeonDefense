from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HeartyDish",)

################################################################################
class HeartyDish(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-366",
            name="Hearty Dish",
            description=(
                "All heroes in adjacent rooms recover LIFE as much as 30 % of "
                "their LIFE lost, and gain 2 Absorption. Gain 3 Absorption "
                "upon entering the dungeon."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Gain 3 Absorption.
            self.owner.add_status("Absorption", 3, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If a hero is being attacked
        if isinstance(ctx.target, DMHero):
            # If the hero is in an adjacent room
            if ctx.target.room in self.room.adjacent_rooms:
                # Register a callback that will heal the unit.
                ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if not ctx.will_fail:
            # Heal the target for 30% of the damage dealt.
            ctx.target.heal(ctx.damage * 0.30)
            # And add 2 Absorption.
            ctx.target.add_status("Absorption", 2, self)

################################################################################

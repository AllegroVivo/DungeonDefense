from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Bazooka",)

################################################################################
class Bazooka(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-376",
            name="Bazooka",
            description=(
                "Normal attacks target all enemies in adjacent rooms. Also, "
                "the attack is immune to Stun and will not miss."
            ),
            rank=7,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If we're the target
        if self.owner == ctx.target:
            # If the status is Stun
            if ctx.status.name == "Stun":
                # Nullify it.
                ctx.will_fail = True

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the one attacking, register our callbacks.
        if self.owner == ctx.source:
            ctx.register_late_callback(self.late_callback)
            ctx.register_post_execute(self.post_callback)

################################################################################
    @staticmethod
    def late_callback(ctx: AttackContext) -> None:

        # Make sure the hero doesn't miss by reversing everything that
        # could fail the context aside from damage become == 0.
        if ctx.will_fail:
            if ctx.damage > 0:
                ctx.will_fail = False

################################################################################
    def post_callback(self, ctx: AttackContext) -> None:

        # This callback targets all enemies in adjacent rooms.
        units = []
        for room in self.room.adjacent_rooms:
            units.extend(room.units_of_type(self.owner, inverse=True))

        for unit in units:
            unit.damage(ctx.damage)

################################################################################

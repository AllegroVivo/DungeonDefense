from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, RoomType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Pacify",)

################################################################################
class Pacify(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-353",
            name="Pacify",
            description=(
                "Apply 3 Immune to all heroes when entering the Battle Room. "
                "Also, gain 1 Immune for every damage received."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # Apply Immune to all allies
            for unit in unit.room.units_of_type(self.owner, inverse=True):
                unit.add_status("Immune", 3, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked
        if self.owner == ctx.target:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was received
        if ctx.damage > 0:
            # Apply Immune equal to damage received
            self.owner.add_status("Immune", ctx.damage, self)

################################################################################

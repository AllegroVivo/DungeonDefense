from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CursedBeing",)

################################################################################
class CursedBeing(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-364",
            name="Cursed Being",
            description=(
                "Apply 3 Curse to all enemies in the room when entering the "
                "Battle Room. Apply 1 Curse every time you inflict damage "
                "to an enemy."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If we've inflicted damage
        if not ctx.will_fail:
            # Apply Curse
            ctx.target.add_status("Curse", 1, self)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # Apply Curse to all enemies
            for unit in self.room.units_of_type(self.owner, inverse=True):
                unit.add_status("Curse", 3, self)

################################################################################

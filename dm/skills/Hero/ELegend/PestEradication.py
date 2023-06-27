from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PestEradication",)

################################################################################
class PestEradication(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-375",
            name="Pest Eradication",
            description=(
                "Apply Poison to all enemies in the room as much as 20 % of "
                "target's current LIFE upon entering a battle room. Also, "
                "apply Poison to the attacker as much as own ATK."
            ),
            rank=7,
            cooldown=CooldownType.Passive
        )

        # Unsure what's meant by "target" whether it's an enemy target or the
        # unit itself. I'm assuming it's the unit itself and that this was
        # phrased poorly.

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked
        if self.owner == ctx.target:
            # Apply Poison to the attacker equal to their ATK.
            ctx.source.add_status("Poison", ctx.source.attack, self)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # For all opponents in the room
            for unit in self.room.units_of_type(self.owner, inverse=True):
                # Apply Poison equal to 20 % of their current LIFE
                unit.add_status("Poison", int(unit.life * 0.20), self)

################################################################################

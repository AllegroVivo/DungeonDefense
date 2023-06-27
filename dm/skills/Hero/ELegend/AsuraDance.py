from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("AsuraDance",)

################################################################################
class AsuraDance(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-379",
            name="Asura Dance",
            description=(
                "Apply 2 Rigidity to all enemies in the room when entering the "
                "Battle Room. Monster's combat ability is increased by 25 %. "
                "Also, For every 2th attack, gain 1 Focus, Acceleration, "
                "Dodge, and Mirror."
            ),
            rank=7,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've entered a room
        if self.owner == unit:
            # For all opponents in the room
            for unit in self.room.units_of_type(self.owner, inverse=True):
                # Apply 2 Rigidity
                unit.add_status("Rigidity", 2, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the attacker
        if self.owner == ctx.source:
            # If this is the 2th attack
            if self.atk_count % 2 == 0:
                # Gain 1 Focus, Acceleration, Dodge, and Mirror
                for status in ("Focus", "Acceleration", "Dodge", "Mirror"):
                    ctx.source.add_status(status, 1, self)

################################################################################
    def stat_adjust(self) -> None:

        # For all monsters in the room
        for monster in self.room.monsters:
            # Increase their combat ability by 25 %
            monster.increase_stat_pct("combat", 0.25)

################################################################################

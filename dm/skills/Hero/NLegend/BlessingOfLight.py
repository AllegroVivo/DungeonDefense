from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BlessingOfLight",)

################################################################################
class BlessingOfLight(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-370",
            name="Blessing of Light",
            description=(
                "Apply 3 Focus, Acceleration, and Dodge to all heroes in the "
                "dungeon. Apply 10 Hatred to all heroes upon death."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide
        )

        # My assumption here is that the second condition, applying 10 Hatred
        # to all heroes upon death, refers to the death of this skill's owner.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Apply 3 Focus, Acceleration, and Dodge to all allies in the dungeon.
        for unit in self.game.units_of_type(self.owner):
            for status in ("Focus", "Acceleration", "Dodge"):
                unit.add_status(status, 3, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If we've died
        if self.owner == ctx.target:
            # Apply 10 Hatred to all heroes.
            for unit in self.game.units_of_type(self.owner):
                unit.add_status("Hatred", 10, self)

################################################################################

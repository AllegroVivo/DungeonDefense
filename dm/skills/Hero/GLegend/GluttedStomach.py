from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GluttedStomach",)

################################################################################
class GluttedStomach(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-382",
            name="Glutted Stomach",
            description=(
                "Gain 5 Absorption at the beginning of battle. On every 8th "
                "attack, remove Fury, Acceleration, and Rampage from all monsters "
                "in adjacent rooms and give them 3 Overweight."
            ),
            rank=8,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")
        self.listen("battle_start", self.callback)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            if self.atk_count % 8 == 0:
                for unit in self.game.units_of_type(self.owner, inverse=True):
                    if unit.room in self.room.adjacent_rooms:
                        unit.add_status("Overweight", 3, self)
                        for status in ("Fury", "Acceleration", "Rampage"):
                            status = unit.get_status(status)
                            if status is not None:
                                status.deplete_all_stacks()


################################################################################
    def callback(self) -> None:

        self.owner.add_status("Absorption", 5, self)

################################################################################

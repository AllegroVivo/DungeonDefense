from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FearMark",)

################################################################################
class FearMark(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-241",
            name="Fear Mark",
            description=(
                "Inflict 10 Panic to all enemies in the room. Deal 50 % more "
                "damage to enemies with Panic."
            ),
            rank=4,
            cooldown=CooldownType.RoomWide,
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for unit in self.room.units_of_type(self.owner, inverse=True):
            unit.add_status("Panic", 10, self)

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            panic = ctx.target.get_status("Panic")
            if panic is not None:
                ctx.amplify_pct(0.50)

################################################################################

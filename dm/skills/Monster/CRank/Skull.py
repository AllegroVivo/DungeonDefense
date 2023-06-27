from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SkullSkill",)

################################################################################
class SkullSkill(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-208",
            name="Skull",
            description=(
                "Become immune to Poison. Gain 3 Immortality at the start "
                "of the battle."
            ),
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start")
        self.listen("status_applied", self.status_applied)

################################################################################
    def notify(self) -> None:

        self.owner.add_status("Immortality", 3, self)

################################################################################
    def status_applied(self, ctx: StatusApplicationContext) -> None:

        if self.owner == ctx.target:
            if ctx.status.name == "Poison":
                ctx.will_fail = True

################################################################################

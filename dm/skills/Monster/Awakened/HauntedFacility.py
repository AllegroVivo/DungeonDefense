from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HauntedFacility",)

################################################################################
class HauntedFacility(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-319",
            name="Haunted Facility",
            description=(
                "All trap effects increase per ratio of souls filling the Altar."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        # TODO: Implement this skill once the Altar is implemented.

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        pass

################################################################################
    def on_acquire(self) -> None:

        pass

################################################################################
    def notify(self, *args) -> None:

        pass

################################################################################
    def stat_adjust(self) -> None:

        pass

################################################################################

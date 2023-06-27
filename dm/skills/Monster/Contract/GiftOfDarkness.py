from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GiftOfDarkness",)

################################################################################
class GiftOfDarkness(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-288",
            name="Gift of Darkness",
            description=(
                "Apply 8 Immortality and Immortal Rage to all monsters at "
                "the beginning of battle."
            ),
            rank=7,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("battle_start")

################################################################################
    def notify(self) -> None:

        for monster in self.game.all_monsters:
            for status in ("Immortality", "Immortal Rage"):
                monster.add_status(status, 8, self)

################################################################################

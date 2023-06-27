from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GiftOfNature",)

################################################################################
class GiftOfNature(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-289",
            name="Gift of Nature",
            description=(
                "Apply 10 Absorption and Rebound to all monsters at the "
                "beginning of battle."
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
            for status in ("Absorption", "Rebound"):
                monster.add_status(status, 10, self)

################################################################################

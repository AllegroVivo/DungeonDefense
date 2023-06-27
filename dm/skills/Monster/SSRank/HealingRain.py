from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("HealingRain",)

################################################################################
class HealingRain(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-278",
            name="Healing Rain",
            description=(
                "Fully restore LIFE of all monsters in the room and apply "
                "1 Absorption."
            ),
            rank=6,
            cooldown=CooldownType.RoomWide,
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for monster in self.room.monsters:
            monster.heal(monster.max_life - monster.life)  # Just restore the amount of life lost.
            monster.add_status("Absorption", 1, self)

################################################################################

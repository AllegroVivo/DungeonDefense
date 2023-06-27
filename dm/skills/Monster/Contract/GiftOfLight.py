from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("GiftOfLight",)

################################################################################
class GiftOfLight(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-292",
            name="Gift of Light",
            description=(
                "When a hero enters the room, apply 36 (+1.5*ATK) Shock and "
                "5 Recharge to all heroes in adjacent rooms."
            ),
            rank=7,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=36, scalar=1.5)
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        if unit.room == self.room:
            targets = []
            for room in self.room.adjacent_rooms:
                targets.extend(room.heroes)

            for target in targets:
                target.add_status("Shock", self.effect, self)
                target.add_status("Recharge", 5, self)

################################################################################

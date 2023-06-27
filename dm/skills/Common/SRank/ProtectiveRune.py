from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Common._common import CommonSkill
from utilities import SkillEffect, UnlockPack, CooldownType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ProtectiveRune",)

################################################################################
class ProtectiveRune(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-195",
            name="Protective Rune",
            description=(
                "Gain 15 (+1.5*ATK) Armor when a hero enters the room."
            ),
            rank=4,
            cooldown=CooldownType.Passive,
            effect=SkillEffect(base=15, scalar=1.5),
            unlock=UnlockPack.Awakening
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("room_enter")

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If a unit has entered the same room as us
        if unit.room == self.room:
            # Apply Armor
            self.owner.add_status("Armor", self.effect, self)

################################################################################

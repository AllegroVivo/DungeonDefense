from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PoignantChill",)

################################################################################
class PoignantChill(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-273",
            name="Poignant Chill",
            description=(
                "Apply 2 Stun to heroes entering the room. Also, apply 1 Stun "
                "to attacking enemies."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("boss_room_entered")
        self.listen("on_attack", self.on_attack)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        unit.add_status("Stun", 2, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            ctx.target.add_status("Stun", 1, self)

################################################################################

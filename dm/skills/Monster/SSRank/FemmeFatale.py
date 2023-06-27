from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FemmeFatale",)

################################################################################
class FemmeFatale(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-269",
            name="Femme Fatale",
            description=(
                "Apply 2 Charm to heroes that entered the dungeon. Also, "
                "inflict 100 % more damage to enemies under the effect of Charm."
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

        unit.add_status("Charm", 2, self)

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            charm = ctx.target.get_status("Charm")
            if charm is not None:
                ctx.amplify_pct(1.00)

################################################################################

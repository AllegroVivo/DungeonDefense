from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import StatusExecutionContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("BoilingRage",)

################################################################################
class BoilingRage(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-318",
            name="Boiling Rage",
            description=(
                "All monsters' Fury effect increase by 2 % per Hatred "
                "applied to self."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_execute")

################################################################################
    def notify(self, ctx: StatusExecutionContext) -> None:

        if isinstance(ctx.target, DMMonster):
            if ctx.status.name == "Fury":
                hatred = ctx.target.get_status("Hatred")
                if hatred is not None:
                    ctx.amplify_pct(hatred.stacks * 0.02)

################################################################################

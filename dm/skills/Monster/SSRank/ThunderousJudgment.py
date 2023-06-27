from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from dm.core.contexts import StatusExecutionContext
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ThunderousJudgment",)

################################################################################
class ThunderousJudgment(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-287",
            name="Thunderous Judgment",
            description=(
                "Apply 10 Electrical Short to all enemies in the dungeon, "
                "and Electrical Short is triggered immediately."
            ),
            rank=6,
            cooldown=CooldownType.DungeonWide
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        for hero in self.game.all_heroes:
            # Generate the status first.
            status = self.game.spawn("Electrical Short", init_obj=True, stacks=10, parent=hero)
            # (Internal method since we already have a DMStatus.)
            hero._add_status(status)  # type: ignore

            # Then just turn around and execute it. We'll need to manually
            # fire the `status_execute` event, though since it was pre-
            # generated to allow for immediate triggering.
            ctx = StatusExecutionContext(self.game, status)  # type: ignore
            self.game.dispatch_event("status_execute", ctx)
            ctx.execute()

################################################################################

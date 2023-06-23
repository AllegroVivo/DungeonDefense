from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Template",)

################################################################################
class Template(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-000",
            name="UrMom",
            description="UrMom",
            rank=2,
            cooldown=0
        )

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        pass

################################################################################
    def activate(self, ctx: AttackContext) -> None:
        """When called, performs this skill's active effect, if any."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """The default event response function if `self.notify()` is called
        with no callback argument."""

        pass

################################################################################

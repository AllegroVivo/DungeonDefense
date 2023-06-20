from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.core.objects.skill import DMSkill

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Template",)

################################################################################
class Template(DMSkill):

    __slots__ = (
        "_parent",
    )

################################################################################
    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="SKL-000",
            name="UrMom",
            description="UrMom",
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this skill."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################

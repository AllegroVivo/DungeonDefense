from __future__ import annotations

from typing     import TYPE_CHECKING

from .adjustable  import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.levelable import DMLevelable
################################################################################

__all__ = ("ExperienceContext",)

################################################################################
class ExperienceContext(AdjustableContext):

    def __init__(self, state: DMGame, obj: DMLevelable, base_exp: int):

        super().__init__(state, base_exp, obj)

################################################################################
    def execute(self) -> None:

        if self._scalar < 0:
            self._scalar = 0

        self._obj.grant_exp(self.calculate())  # type: ignore

################################################################################

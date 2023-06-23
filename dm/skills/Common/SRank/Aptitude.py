from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills._common import CommonSkill

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Aptitude",)

################################################################################
class Aptitude(CommonSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-174",
            name="Aptitude",
            description=(
                "Cooldown of Active skills is reduced to half."
            ),
            rank=2,
            cooldown=0,
            passive=True
        )

        # This might need tweaking. What happens on skill removal?

################################################################################
    def on_acquire(self) -> None:

        self.owner.override_skill_cooldown_scalar(0.50)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.objects.status import DMStatus
from utilities          import *

if TYPE_CHECKING:
    from dm.core.contexts import BossSkillContext
    from dm.core.objects.unit import DMUnit
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("Seed",)

################################################################################
class Seed(DMStatus):

    def __init__(
        self,
        game: DMGame,
        parent: Optional[DMUnit] = None,
        stacks: Optional[int] = 1
    ):

        super().__init__(
            game,
            parent,
            _id="BUF-127",
            name="Seed",
            description=(
                "A seed that holds the power of nature. Used by Floria's Abilities."
            ),
            stacks=stacks,
            status_type=DMStatusType.Buff
        )

        # Probably need to implement this in the Boss Skill logic.

################################################################################

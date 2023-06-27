from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("ImmortalOne",)

################################################################################
class ImmortalOne(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-299",
            name="Immortal One",
            description=(
                "You cannot be killed by any effect."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            # We could restore to 1 LIFE, but that would just cause the effect
            # to get triggered again sooner, which is silly, so just restore
            # to max LIFE. Seems like a good solution if the unit can't die.
            self.owner.heal(self.owner.max_life)

################################################################################

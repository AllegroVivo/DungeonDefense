from __future__ import annotations

from typing     import TYPE_CHECKING
from ...core.objects.relic import DMRelic

if TYPE_CHECKING:
    from dm.core.contexts   import BossSkillContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("VampiricMonster",)

################################################################################
class VampiricMonster(DMRelic):

    def __init__(self, state: DMGame):

        super().__init__(
            state,
            _id="REL-125",
            name="Vampiric Monster",
            description=(
                "When damage is inflicted using 'Boss Skill : Bite', the Dark "
                "Lord's LIFE is recovered as much as Vampire possessed by the "
                "Dark Lord."
            ),
            rank=1
        )

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when a relic is added to the player's inventory."""

        self.game.subscribe_event("boss_skill_bite", self.notify)

################################################################################
    def notify(self, ctx: BossSkillContext) -> None:
        """A general event response function."""

        ctx.register_after_execute(self.restore_life)  # type: ignore

################################################################################
    def restore_life(self, ctx: BossSkillContext) -> None:

        if ctx.damage > 0:
            vampire = self.game.dark_lord.get_status("Vampire")
            if vampire is not None:
                self.game.dark_lord.heal(vampire.stacks)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("SuperDimensionalManeuver",)

################################################################################
class SuperDimensionalManeuver(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-286",
            name="Super-Dimensional Maneuver",
            description=(
                "Gain 1 Dodge for every action. Also, the monster's attack "
                "won't be missed or absorbed."
            ),
            rank=6,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_attack")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.source:
            ctx.source.add_status("Dodge", 1, self)
            ctx.register_late_callback(self.late_callback)

################################################################################
    @staticmethod
    def late_callback(ctx: AttackContext) -> None:

        # Late callback is a single callable that, if registered, is called
        # after all other effects have been executed, but prior to damage
        # application.
        # We'll use the private attribute here since that's what gets set when
        # attack accuracy is overriden.
        if ctx._fail:
            # If there's actually damage to be applied...
            if ctx.damage > 0:
                # Un-fail that bitch.
                ctx._fail = False

################################################################################

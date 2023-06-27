from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from ....rooms.traproom import DMTrapRoom
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Pathfinder",)

################################################################################
class Pathfinder(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-350",
            name="Pathfinder",
            description=(
                "Apply 1 Dodge Trap to all heroes upon death by trap. Apply "
                "2 Dodge to all heroes upon death by another character."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

        # I'm making the assumption that this only refers to hero deaths.

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If a hero died
        if isinstance(ctx.target, DMHero):
            # If the source was a trap room
            if isinstance(ctx.source, DMTrapRoom):
                # Apply 1 Dodge Trap
                ctx.target.add_status("Dodge Trap", 1, self)
            # Otherwise
            else:
                # Apply 2 Dodge
                ctx.target.add_status("Dodge", 2, self)

################################################################################

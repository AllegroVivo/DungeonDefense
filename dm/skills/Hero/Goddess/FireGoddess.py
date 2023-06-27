from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FireGoddess",)

################################################################################
class FireGoddess(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-403",
            name="Fire Goddess",
            description=(
                "When entering the dungeon, all heroes become immune to Burn, "
                "Stun and all monsters cannot gain Fury anymore."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_applied")

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If the status is being applied to a monster
        if isinstance(ctx.target, DMMonster):
            # If the status is Fury
            if ctx.status.name == "Fury":
                # Nullify it
                ctx.will_fail = True
        # Otherwise, if the status is being applied to a hero
        else:
            # If the status is Burn or Stun
            if ctx.status.name in ("Burn", "Stun"):
                # Nullify it
                ctx.will_fail = True

################################################################################

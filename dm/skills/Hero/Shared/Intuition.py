from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.rooms.traproom import DMTrapRoom
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("Intuition",)

################################################################################
class Intuition(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-335",
            name="Intuition",
            description=(
                "Gain 5 Dodge Trap when entering the dungeon. Damage received "
                "from traps decrease by 30 %."
            ),
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If a trap room is the source of the attack
        if isinstance(ctx.source, DMTrapRoom):
            # And it's targeting us:
            if self.owner == ctx.target:
                # Mitigate damage
                ctx.mitigate_pct(0.30)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Gain Dodge Trap
            unit.add_status("Dodge Trap", 5, self)

################################################################################

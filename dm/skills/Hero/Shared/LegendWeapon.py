from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("LegendWeapon",)

################################################################################
class LegendWeapon(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-343",
            name="Legend Weapon",
            description=(
                "Gain 20 Hatred at the beginning of battle, and gain 1 Hatred "
                "every time you attack an enemy."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("hero_spawn")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the one who's attacking
        if self.owner == ctx.source:
            # If we're attacking a monster
            if isinstance(ctx.target, DMMonster):
                # Gain 1 Hatred.
                self.owner.add_status("Hatred", 1, self)

################################################################################
    def notify(self, unit: DMUnit) -> None:

        # If we've spawned
        if self.owner == unit:
            # Gain 20 Hatred.
            self.owner.add_status("Hatred", 20, self)

################################################################################

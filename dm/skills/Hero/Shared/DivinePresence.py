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

__all__ = ("DivinePresence",)

################################################################################
class DivinePresence(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-340",
            name="Divine Presence",
            description=(
                "Apply 10 Curse to enemies that have attacked you or received "
                "damaged from you. Recover all heroes' LIFE at time of death."
            ),
            rank=5,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If a monster is attacking
        if isinstance(ctx.source, DMMonster):
            # Apply Curse
            ctx.source.add_status("Curse", 10, self)
        # Otherwise, if we're attacking
        elif self.owner == ctx.source:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If we dealt damage
        if ctx.damage > 0:
            # Apply Curse
            ctx.target.add_status("Curse", 10, self)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If we've died
        if self.owner == ctx.target:
            # Recover all heroes' LIFE to full.
            for hero in self.game.all_heroes:
                hero.heal(hero.max_life)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.hero import DMHero
from dm.core.objects.monster import DMMonster
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FrenziedPoison",)

################################################################################
class FrenziedPoison(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-406",
            name="Frenzied Poison",
            description=(
                "All monsters gain Poison equal to 30 % of max LIFE each time "
                "they take an action. Also, when a hero attacks a monster in "
                "Poison state, gain Fury and Regeneration equal to Poison stat."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If a monster is performing an attack
        if isinstance(ctx.source, DMMonster):
            # Apply Poison to the monster
            ctx.source.add_status("Poison", ctx.source.max_life * 0.30, self)
        # Otherwise, if a hero is performing an attack against a monster
        elif isinstance(ctx.source, DMHero) and isinstance(ctx.target, DMMonster):
            # If the monster is afflicted with Poison
            poison = ctx.target.get_status("Poison")
            if poison is not None:
                # Apply Fury and Regeneration to the hero
                for status in ("Fury", "Regeneration"):
                    ctx.source.add_status(status, poison.stacks, self)

################################################################################

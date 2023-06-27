from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from dm.core.objects.hero import DMHero
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("MagicWeapon",)

################################################################################
class MagicWeapon(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-325",
            name="Magic Weapon",
            description=(
                "Armor penetration increases by 20 %."
            ),
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're the one who's attacking
        if isinstance(ctx.source, DMHero):
            # Increase armor penetration
            ctx.amplify_pct(0.20)  # Just add 20% to the damage total. Close enough.

################################################################################

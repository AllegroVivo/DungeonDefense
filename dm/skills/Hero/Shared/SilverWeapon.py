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

__all__ = ("SilverWeapon",)

################################################################################
class SilverWeapon(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-327",
            name="Silver Weapon",
            description=(
                "Deal 100 % additional damage to an enemy under Immortality "
                "effect, and decrease their Immortality stat by 1."
            ),
            rank=2,
            cooldown=CooldownType.Passive
        )

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If we're the one who's attacking
        if self.owner == ctx.source:
            # If we're attacking a monster
            if isinstance(ctx.target, DMMonster):
                # If the monster has Immortality
                immortality = ctx.target.get_status("Immortality")
                if immortality is not None:
                    # Increase damage
                    ctx.amplify_pct(1.00)
                    # Reduce Immortality stacks
                    immortality.reduce_stacks_flat(1)

################################################################################

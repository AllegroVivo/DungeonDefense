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

__all__ = ("LightBolt",)

################################################################################
class LightBolt(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-410",
            name="Light Bolt",
            # description=(  # Original description
            #     "When an enemy in Shock state attacked, deals damage 2 more "
            #     "times equal to Shock stat. In Blind state, the number of extra "
            #     "damages increase to 5."
            # ),
            description=(
                "When an enemy in Shock state is attacked, deal damage equal to "
                "300% of the enemy's Shock stat. If the enemy is under the effect "
                "of Blind, the amount of damage increases to 500%."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking a monster
        if isinstance(ctx.target, DMMonster):
            # If the target is afflicted with Shock
            shock = ctx.target.get_status("Shock")
            if shock is not None:
                # If the target is also afflicted with Blind, increase scalar.
                blind = ctx.target.get_status("Blind")
                scalar = 3 if blind is None else 5
                # Deal damage to the target
                ctx.amplify_flat(scalar * shock.stacks)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("IronFist",)

################################################################################
class IronFist(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-387",
            name="Iron Fist",
            description=(
                "Apply 1 Rigidity to the attacker. Also, gain 1 Dodge every "
                "time dealing or receiving damage from enemy."
            ),
            rank=8,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If this attack pertains to the owner of this skill, register a
        # callback to be executed after the attack is resolved.
        if self.owner in (ctx.source, ctx.target):
            ctx.register_post_execute(self.callback)
            # Additionally, if we're the target, apply 1 Rigidity to the
            # attacker.
            if self.owner == ctx.target:
                ctx.source.add_status("Rigidity", 1, self)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If the attack was successful
        if ctx.damage > 0:
            # Apply 1 Dodge to the owner of this skill
            self.owner.add_status("Dodge", 1, self)

################################################################################

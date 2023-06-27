from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("FormlessSword",)

################################################################################
class FormlessSword(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-396",
            name="Formless Sword",
            description=(
                "Inflicts damage that ignores absorption when an enemy attacks, "
                "and ignores DEF. Gains 8 Hatred with each damage inflicted "
                "on the enemy."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

        # I'm making the assumption that when the skill states "8 Hatred with
        # each damage inflicted on the enemy", it means 8 Hatred PER
        # POINT OF DAMAGE INFLICTED. That means it's gonna hurt <_<.

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked, counter with our own damage.
        # Doesn't say anything about the attack needed to connect.
        if self.owner == ctx.target:
            # Ignore the target's defense by adding additional damage equal
            # to that amount.
            ctx.target._damage(self.owner.attack + ctx.target.defense)
        # Otherwise, if we're attacking, gain Hatred once all damage calculations
        # have been completed.
        else:
            ctx.register_post_execute(self.callback)

################################################################################
    def callback(self, ctx: AttackContext) -> None:

        # If damage was dealt
        if ctx.damage > 0:
            # Gain Hatred equal to the damage dealt.
            self.owner.add_status("Hatred", 8 * ctx.damage, self)

################################################################################

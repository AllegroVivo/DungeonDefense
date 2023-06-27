from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext, StatusApplicationContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RainbowGemstones",)

################################################################################
class RainbowGemstones(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-383",
            name="Rainbow Gemstones",
            description=(
                "Turn all Burn, Shock, Poison, and Corpse Explosion stacks into "
                "Armor. When attacking enemy, inflict additional damage as much "
                "as 10 % of Armor stack."
            ),
            rank=8,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("status_acquire")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # Get the target's Armor status
            armor = ctx.target.get_status("Armor")
            if armor is not None:
                # Deal additional damage equal to 10 % of the target's Armor
                ctx.amplify_flat(int(armor.stacks * 0.10))

################################################################################
    def notify(self, ctx: StatusApplicationContext) -> None:

        # If the status is being applied to the owner of this skill
        if self.owner == ctx.target:
            # If the status is one of the following
            if ctx.status.name in ("Burn", "Shock", "Poison", "Corpse Explosion"):
                # Remove the status and add Armor equal to the amount of the
                # nullified status
                self.owner.add_status("Armor", ctx.status.stacks, self)
                ctx.will_fail = True

################################################################################

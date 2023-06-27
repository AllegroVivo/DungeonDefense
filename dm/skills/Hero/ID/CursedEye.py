from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, StatusType

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("CursedEye",)

################################################################################
class CursedEye(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-397",
            name="Cursed Eye",
            description=(
                "When attacking an enemy in a Curse state, removes 1 random "
                "buff and gains 25 Curse. When killed, gives own Curse to all "
                "enemies in the dungeon."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're attacking
        if self.owner == ctx.source:
            # If the target is cursed
            curse = ctx.target.get_status("Curse")
            if curse is not None:
                # Remove buffs first so that the curse can be applied without interference.
                buffs = [
                    s for s in ctx.target.statuses
                    if s._type in (StatusType.Buff, StatusType.AntiDebuff)
                ]
                if buffs:
                    self.random.choice(buffs).deplete_all_stacks()
                # Apply curse
                ctx.target.add_status("Curse", 25, self)

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        # If we've died
        if self.owner == ctx.target:
            # Get own Curse
            curse = self.owner.get_status("Curse")
            if curse is not None:
                # And apply equal amount to all enemies
                for unit in ctx.game.units_of_type(self.owner, inverse=True):
                    unit.add_status("Curse", curse.stacks, self)

################################################################################

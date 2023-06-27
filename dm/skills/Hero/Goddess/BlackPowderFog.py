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

__all__ = ("BlackPowderFog",)

################################################################################
class BlackPowderFog(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-404",
            name="Black Powder Fog",
            description=(
                "All monsters gain Burn equal to ATK each time they take an "
                "action. Also, when a monster in Burn state is attacked, all "
                "monsters in adjacent rooms receive damage equal to Burn stat."
            ),
            rank=10,
            cooldown=CooldownType.Passive
        )

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:

        # If we're being attacked by a monster
        if isinstance(ctx.source, DMMonster):
            # Apply Burn to the attacker
            ctx.source.add_status("Burn", ctx.source.attack, self)
        # Otherwise, if we're attacking a monster
        elif isinstance(ctx.target, DMMonster):
            # If the target is afflicted with Burn
            burn = ctx.target.get_status("Burn")
            if burn is not None:
                # Deal damage to all monsters in adjacent rooms
                targets = []
                for room in self.room.adjacent_rooms:
                    targets.extend(room.monsters)
                for target in targets:
                    target.damage(burn.stacks)

################################################################################

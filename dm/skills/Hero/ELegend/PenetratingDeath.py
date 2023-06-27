from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Hero._hero import HeroSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("PenetratingDeath",)

################################################################################
class PenetratingDeath(HeroSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-377",
            name="Penetrating Death",
            description=(
                "Inflict 80 (+1.0*ATK) damage to enemies in adjacent rooms and "
                "remove all of their Immortality effects. Also, gain Immortality "
                "as many enemies as you damaged."
            ),
            rank=7,
            cooldown=CooldownType.AdjacentWide,
            effect=SkillEffect(base=80, scalar=1.0)
        )

################################################################################
    def execute(self, ctx: AttackContext) -> None:

        # Targets all enemies in adjacent rooms.
        targets = []
        for room in self.room.adjacent_rooms:
            targets.extend(room.units_of_type(self.owner, inverse=True))

        # Inflict damage and remove Immortality.
        for target in targets:
            target.damage(self.effect)
            immortality = target.get_status("Immortality")
            if immortality is not None:
                immortality.deplete_all_stacks()

        # Then gain Immortality equal to the number of enemies damaged.
        self.owner.add_status("Immortality", len(targets), self)

################################################################################

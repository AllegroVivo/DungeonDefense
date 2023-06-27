from __future__ import annotations

from typing     import TYPE_CHECKING
from dm.skills.Monster._monster import MonsterSkill
from utilities import CooldownType, SkillEffect

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
################################################################################

__all__ = ("RevivingFlame",)

################################################################################
class RevivingFlame(MonsterSkill):

    def __init__(self, state: DMGame, parent: DMUnit = None):

        super().__init__(
            state, parent,
            _id="SKL-262",
            name="Reviving Flame",
            description=(
                "At the time of death, inflict 999 (+99*ATK) to all enemies in "
                "the room and revive with full LIFE. This effect is only "
                "activated once per battle."
            ),
            rank=5,
            cooldown=CooldownType.Passive,
            passive=True,
            effect=SkillEffect(base=999, scalar=99)
        )

        self._activated: bool = False

################################################################################
    def on_acquire(self) -> None:

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if self.owner == ctx.target:
            self._activated = True
            for unit in self.room.units_of_type(ctx.source):
                unit.damage(self.effect)
            self.owner.heal(self.owner.max_life)

################################################################################

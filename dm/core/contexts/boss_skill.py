from __future__ import annotations

from typing     import TYPE_CHECKING, Union

from .attack import AttackContext
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMFighter, DMGame, DMRoom, DMTrapRoom
################################################################################

__all__ = ("AttackContext", "BossSkillContext")

################################################################################
class BossSkillContext(AttackContext):

    __slots__ = (
        "_parent",
        "_mana_cost"
    )

################################################################################
    def __init__(
        self,
        game: DMGame,
        attacker: Union[DMFighter, DMTrapRoom],
        defender: DMFighter,
        room: DMRoom,
        # parent: DMBossSkill
    ):

        super().__init__(game, room, attacker, defender)

        # self._parent: DMBossSkill = parent
        # self.mana_cost = self._parent.mana_cost
        self._mana_cost = 1

################################################################################
    @property
    def mana_cost(self) -> int:

        return self._mana_cost

################################################################################
    def reduce_mana_cost(self, amount: int) -> None:

        if not isinstance(amount, int):
            raise ArgumentTypeError("BossSkillContext.reduce_mana_cost()", type(amount), type(int))

        self._mana_cost -= amount

################################################################################
    def execute(self) -> None:

        # Might not be able to call super method in here since the boss skill
        # may factor in at multiple places. But is a good placeholder for now.
        super().execute()

################################################################################

################################################################################

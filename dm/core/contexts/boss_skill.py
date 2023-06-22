from __future__ import annotations

from typing     import TYPE_CHECKING, List, Optional, Union

from .attack import AttackContext
from utilities  import *

if TYPE_CHECKING:
    from dm.core.objects.object import DMObject
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.objects.room import DMRoom
    from dm.core.objects.status import DMStatus
    from ...rooms.traproom import DMTrapRoom
    from dm.core.contexts import StatusApplicationContext
################################################################################

__all__ = ("BossSkillContext", )

################################################################################
class BossSkillContext(AttackContext):

    __slots__ = (
        "_parent",
        "_mana_cost",
        "_statuses",
    )

################################################################################
    def __init__(
        self,
        game: DMGame,
        attacker: Union[DMUnit, DMTrapRoom],
        defender: DMUnit,
        room: DMRoom,
        # parent: DMBossSkill
    ):

        super().__init__(game, attacker, defender, AttackType.Skill)

        # self._parent: DMBossSkill = parent
        # self.mana_cost = self._parent.mana_cost
        self._mana_cost = 1

################################################################################
    @property
    def mana_cost(self) -> int:

        return self._mana_cost

################################################################################
    @property
    def statuses(self) -> List[StatusApplicationContext]:

        return self._statuses

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
    def add_status(
        self,
        status: Union[DMStatus, str],
        stacks: int = 1,
        source: Optional[DMObject] = None
    ) -> None:

        if isinstance(status, str):
            status = self.game.spawn(status, stacks=stacks)

        self._statuses.append(StatusApplicationContext(self.game, source, status))

################################################################################
    def get_status(self, status: Union[DMStatus, str]) -> Optional[StatusApplicationContext]:

        if isinstance(status, str):
            status = self.game.spawn(status)

        for s in self._statuses:
            if s.status == status:
                return s

################################################################################

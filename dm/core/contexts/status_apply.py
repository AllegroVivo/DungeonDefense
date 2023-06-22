from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from dm.core.contexts.context import Context

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.unit   import DMUnit
    from dm.core.objects.status       import DMStatus
    from dm.core.objects.object import DMObject
    from dm.core.objects.room   import DMRoom
################################################################################

__all__ = ("StatusApplicationContext",)

################################################################################
class StatusApplicationContext(Context):

    __slots__ = (
        "_source",
        "_status",
        "_fail",
        "_stacks",

    )

################################################################################
    def __init__(self, state: DMGame, source: DMObject, status: DMStatus):

        super().__init__(state)

        self._source: DMObject = source
        self._status: DMStatus = status
        self._stacks: int = status.stacks

        self._fail: bool = False

        self.game.dispatch_event("status_applied", self)

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.target.room

################################################################################
    @property
    def source(self) -> DMObject:

        return self._source

################################################################################
    @property
    def target(self) -> DMUnit:

        return self._status.owner

################################################################################
    @property
    def status(self) -> DMStatus:

        return self._status

################################################################################
    @property
    def will_fail(self) -> bool:

        return self._status.stacks <= 0 or self._fail

################################################################################
    @will_fail.setter
    def will_fail(self, value: bool) -> None:

        self._fail = value

################################################################################
    def reduce_stacks_flat(self, amount: int) -> None:

        self._stacks -= amount

################################################################################
    def reduce_stacks_pct(self, amount: float) -> None:

        self._stacks = int(self._stacks * amount)

################################################################################
    def increase_stacks_flat(self, amount: int) -> None:

        self._stacks += amount

################################################################################
    def increase_stacks_pct(self, amount: float) -> None:

        self._stacks = int(self._stacks * (amount + 1))

################################################################################
    def execute(self) -> Optional[DMStatus]:

        # No point adding an empty status.
        if self.will_fail:
            return

        self._status._stacks = self._stacks

        return self._status

################################################################################

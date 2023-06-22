from __future__ import annotations

from typing     import TYPE_CHECKING, Union

from dm.core.contexts.adjustable import AdjustableContext

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.status       import DMStatus
    from dm.core.objects.room   import DMRoom
    from dm.core.objects.unit   import DMUnit
################################################################################

__all__ = ("StatusExecutionContext",)

################################################################################
class StatusExecutionContext(AdjustableContext):

    __slots__ = (
        "_status",
        "_fail",
        "_stacks",
        "_direct",
        "_additional",
    )

################################################################################
    def __init__(self, state: DMGame, status: DMStatus):

        super().__init__(state)

        self._status: DMStatus = status
        self._stacks: int = status.stacks
        self._fail: bool = False
        self._direct: bool = False

        self._additional: list[DMStatus] = []

################################################################################
    @property
    def room(self) -> DMRoom:

        return self.status.room

################################################################################
    @property
    def status(self) -> DMStatus:

        return self._status

################################################################################
    @property
    def stacks(self) -> int:

        return self._stacks

################################################################################
    @property
    def target(self) -> DMUnit:

        return self._status.owner

################################################################################
    @property
    def direct_damage(self) -> bool:

        return self._direct

################################################################################
    def set_direct_damage(self, value: bool) -> None:

        self._direct = value

################################################################################
    @property
    def will_fail(self) -> bool:

        return self._status.stacks <= 0 or self._fail

################################################################################
    @will_fail.setter
    def will_fail(self, value: bool) -> None:

        self._fail = value

################################################################################
    def execute(self) -> None:

        # Dispatch the event to all listeners.
        self.game.dispatch_event("status_execute", self)

        # Update the stack count after all listeners have acted on it.
        self._status._stacks = self._stacks

        # No point executing an empty status.
        if self.will_fail:
            return

        # Check for direct damage resulting from a relic or something else.
        if self._direct:
            # This will bypass the status' potential damage reduction.
            self._status.owner._damage(self.status.stacks)
            return

        # Execute the status's main effect.
        # self._status.execute

        # Apply any newly attached statuses.
        for s in self._additional:
            # Use the internal method because we already have an instance of DMStatus
            # and so we can bypass the event call.
            self.status.owner._add_status(s)

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
    def add_status(self, status: Union[DMStatus, str],  stacks: int = 1) -> None:

        if isinstance(status, str):
            status = self.game.spawn(status, stacks=stacks)

        self._additional.append(status)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING

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
        "_direct"
    )

################################################################################
    def __init__(self, state: DMGame, status: DMStatus):

        super().__init__(state)

        self._status: DMStatus = status
        self._stacks: int = status.stacks
        self._fail: bool = False
        self._direct: bool = False

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

        # Update the stack count after all listeners have acted on it.
        self._status._stacks = self._stacks

        # No point adding an empty status.
        if self.will_fail:
            return

        # Check for direct damage resulting from the Sharp Thorn relic.
        if self._direct:
            # This will bypass the status' potential damage reduction.
            self._status.owner._damage(self.status.stacks)
            return

        # I think this needs to be damage().
        # Use the internal method because we already have an instance of DMStatus
        self.status.owner._add_status(self._status)

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

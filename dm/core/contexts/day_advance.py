from __future__ import annotations

from typing     import TYPE_CHECKING, Any, Optional

from .context import Context

if TYPE_CHECKING:
    from dm.core.game.game    import DMGame
    from dm.core.objects.room import DMRoom
    from dm.core.game.day import DMDay
################################################################################

__all__ = ("DayAdvanceContext",)

################################################################################
class DayAdvanceContext(Context):

    __slots__ = (
        "_day",
        "_reset_mana",
    )

################################################################################
    def __init__(self, state: DMGame):

        super().__init__(state)

        self._day: DMDay = self.game.day
        self._reset_mana: bool = False

        # Dispatch the event to listeners can act on the CTX.
        self.game.dispatch_event("day_advance", self)

################################################################################
    @property
    def room(self) -> DMRoom:
        """Returns the room in which this context is taking place."""

        return self.game.dungeon.map.boss_tile

################################################################################
    @property
    def next_day(self) -> int:
        """Returns the day that will be advanced to."""

        return self._day.current + 1

################################################################################
    def toggle_mana_reset(self, value: bool) -> None:

        self._reset_mana = value

################################################################################
    def execute(self) -> DMDay:
        """Executes the context and returns the result of the execution."""

        if self._reset_mana:
            self.game.dark_lord.reset_mana()

        self._day.advance()
        return self._day

################################################################################

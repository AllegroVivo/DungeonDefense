from __future__ import annotations

from typing     import TYPE_CHECKING

from utilities      import *

if TYPE_CHECKING:
    from dm.core    import DMGame, RoomChangeContext
################################################################################

__all__ = ("DMChargeable",)

################################################################################
class DMChargeable:

    __slots__ = (
        "_current_charge",
        "_charge_rate",
        "_max_charge"
    )

################################################################################
    def __init__(self):

        self._current_charge: float = 0
        self._charge_rate: float = 1.0
        self._max_charge: float = 3.3

################################################################################
    def update(self, dt: float) -> None:

        self._current_charge += dt * self._charge_rate

        if self._current_charge >= self._max_charge:
            self.activate()
            self.reset_charge()

################################################################################
    def activate(self) -> None:

        raise NotImplementedError

################################################################################
    def set_charge_rate(self, rate: float) -> None:

        if not isinstance(rate, float):
            raise ArgumentTypeError(
                "Invalid type passed to DMChargeable.set_charge_rate().",
                type(rate),
                type(float)
            )

        self._charge_rate = rate

################################################################################
    def scale_charge_rate(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError(
                "Invalid type passed to DMChargeable.scale_charge_rate().",
                type(amount),
                type(float)
            )

        self._charge_rate += amount

################################################################################
    def set_charge_time(self, value: float) -> None:

        if not isinstance(value, float):
            raise ArgumentTypeError(
                "Invalid type passed to DMChargeable.set_charge_time().",
                type(value),
                type(float)
            )

        self._max_charge = value

################################################################################
    def reset_charge(self) -> None:

        self._current_charge = 0

################################################################################
    def register_listener(self, game: DMGame) -> None:

        game.subscribe_event("on_room_change", self.on_room_change)

################################################################################
    def on_room_change(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            self.activate()

################################################################################
    def on_room_change_other(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            half = self._max_charge * 0.50
            total = self._current_charge + half
            # If the total charge doesn't exceed the max charge, go ahead with it
            if total <= self._max_charge:
                self._current_charge += half
            # Otherwise we need to calculate the difference, activate the facility
            # in the middle there, then apply the remainder of the charge after
            # activation and reset.
            else:
                diff = total - self._max_charge
                self._current_charge += total - diff
                self.activate()
                self.reset_charge()
                self._current_charge += diff

################################################################################

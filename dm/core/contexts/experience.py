from __future__ import annotations

from typing     import TYPE_CHECKING

from .context  import Context
from utilities  import *

if TYPE_CHECKING:
    from dm.core    import DMGame, DMLevelable
################################################################################

__all__ = ("ExperienceContext",)

################################################################################
class ExperienceContext(Context):

    __slots__ = (
        "_obj",
        "_exp",
        "_scalar"
    )

################################################################################
    def __init__(self, state: DMGame, object: DMLevelable, base_exp: int):

        super().__init__(state)

        self._obj: DMLevelable = object
        self._exp: int = base_exp
        self._scalar: float = 1.0

################################################################################
    def scale(self, amount: float) -> None:

        if not isinstance(amount, float):
            raise ArgumentTypeError("ExperienceContext.scale_exp()", type(amount), type(float))

        self._scalar += amount

################################################################################
    def execute(self) -> None:

        if self._scalar < 0:
            self._scalar = 0

        self._obj.grant_exp(self._exp * self._scalar)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING, Optional, Type, TypeVar, Union
from .object    import DMObject
from utilities  import *

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
    from dm.core.objects.unit    import DMUnit
################################################################################

__all__ = ("DMSkill",)

S = TypeVar("S", bound="DMSkill")

################################################################################
class DMSkill(DMObject):

    __slots__ = (
        "_parent",
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        parent: DMUnit,
        *,
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None
    ):

        super().__init__(state, _id, name, description, rank, unlock)

        self._parent: DMUnit = parent

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Skill

################################################################################
    @property
    def owner(self) -> DMUnit:

        return self._parent

################################################################################
    def passive_effect(self) -> None:
        """Global effect always applied to this skill's owner."""

        pass

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def effect_value(self) -> float:
        """The value of the effect corresponding to this skill."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """A general event response function."""

        pass

################################################################################
    def _copy(self, **kwargs) -> DMSkill:
        """Returns a clean copy of the current skill.

        Returns:
        --------
        :class:`DMSkill`
            A fresh copy of the current DMObject.

        """

        new_obj: Type[S] = super()._copy()  # type: ignore

        new_obj._parent = kwargs.get("parent")

        return new_obj  # type: ignore

################################################################################

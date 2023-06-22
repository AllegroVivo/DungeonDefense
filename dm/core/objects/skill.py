from __future__ import annotations

from typing     import TYPE_CHECKING, Any, Literal, Optional, Type, TypeVar
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
        "__cooldown",
        "_active_cooldown"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        parent: Optional[DMUnit],
        cooldown: Literal[0, 1, 2, 4, 6, 8],
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None,
    ):

        super().__init__(state, _id, name, description, rank, unlock)

        self._parent: DMUnit = parent

        self.__cooldown: int = cooldown
        self._active_cooldown: int = cooldown

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Skill

################################################################################
    @property
    def skill_type(self) -> DMSkillType:

        raise NotImplementedError

################################################################################
    @property
    def owner(self) -> DMUnit:

        return self._parent

################################################################################
    def _offensive_callback(self, ctx: AttackContext) -> None:

        # If the master cooldown is 0, then this isn't a battle skill or
        # doesn't have battle-based logic.
        if self.__cooldown == 0:
            return

        self._active_cooldown -= 1
        if self._active_cooldown <= 0:
            self.handle(ctx)
            self._reset_cooldown()

################################################################################
    def _defensive_callback(self, ctx: AttackContext) -> None:

        # If the master cooldown is 0, then this isn't a battle skill or
        # doesn't have battle-based logic.
        if self.__cooldown == 0:
            return

        self._active_cooldown -= 1
        if self._active_cooldown <= 0:
            self.handle(ctx)
            self._reset_cooldown()

################################################################################
    def _reset_cooldown(self) -> None:

        self._active_cooldown = self.__cooldown

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        pass

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        pass

################################################################################
    def on_defend(self, ctx: AttackContext) -> None:
        """Called when used during a battle."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    @property
    def effect_value(self) -> Any:
        """The value of the effect corresponding to this skill."""

        return

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

        new_obj.__cooldown = kwargs.get("cooldown", self.__cooldown)
        new_obj._active_cooldown = new_obj.__cooldown

        return new_obj  # type: ignore

################################################################################

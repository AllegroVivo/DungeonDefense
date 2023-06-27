from __future__ import annotations

from typing     import (
    TYPE_CHECKING,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    TypeVar
)

from .unit import DMUnit
from .object    import DMObject
from utilities  import *

if TYPE_CHECKING:
    from dm.core.contexts   import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("DMSkill",)

S = TypeVar("S", bound="DMSkill")

################################################################################
class DMSkill(DMObject):

    __slots__ = (
        "_parent",
        "__cooldown",
        "_active_cooldown",
        "_passive",
        "_effect",
        "_parent_atk_count"
    )

################################################################################
    def __init__(
        self,
        state: DMGame,
        parent: Optional[DMUnit],
        cooldown: CooldownType,
        effect: Optional[SkillEffect],
        _id: str,
        name: str,
        description: Optional[str],
        rank: int = 0,
        unlock: Optional[UnlockPack] = None,
    ):

        super().__init__(state, _id, name, description, rank, unlock)

        self._parent: DMUnit = parent
        self._parent_atk_count: int = 1  # Start this at 1 since attacks aren't added until after execution.

        self.__cooldown: float = cooldown.value * self.owner._skill_cooldown_scalar
        self._active_cooldown: float = self.__cooldown

        self._passive: bool = self.__cooldown == 0
        self._effect: Optional[SkillEffect] = effect

        # Subscribe to relevant events
        self.listen("on_attack", self._callback)

################################################################################
    @property
    def type(self) -> DMType:

        return DMType.Skill

################################################################################
    @property
    def category(self) -> SkillCategory:

        raise NotImplementedError

################################################################################
    @property
    def passive(self) -> bool:

        return self._passive

################################################################################
    @property
    def owner(self) -> DMUnit:

        return self._parent

################################################################################
    @property
    def cooldown(self) -> float:

        return self.__cooldown * self.owner._skill_cooldown_scalar

################################################################################
    @property
    def atk_count(self) -> int:

        return self._parent_atk_count

################################################################################
    def _callback(self, ctx: AttackContext) -> None:

        # Call `on_attack` here because a number of passive effects will
        # need this listener.
        self.on_attack(ctx)

        # If the master cooldown is 0, then this isn't a battle skill or
        # doesn't have battle-based logic.
        if self.__cooldown == 0:
            return

        # If this attack doesn't involve this unit, just exit.
        if self.owner not in (ctx.source, ctx.target):
            return

        # This is useful in the subclasses.
        if self.owner == ctx.target:
            ctx.register_post_execute(self._increment_atk_count)

        # Reduce the cooldown and check if it's ready to be used.
        self._active_cooldown -= 1
        if self._active_cooldown <= 0:
            self.execute(ctx)
            self._reset_cooldown()

################################################################################
    def _increment_atk_count(self, ctx: AttackContext) -> None:

        if not ctx.will_fail:
            self._parent_atk_count += 1

################################################################################
    def _reset_cooldown(self) -> None:

        self._active_cooldown += self.cooldown

################################################################################
    def on_acquire(self) -> None:
        """Automatically called upon the skill's acquisition."""

        pass

################################################################################
    def execute(self, ctx: AttackContext) -> None:
        """When called, performs this skill's active effect, if any."""

        pass

################################################################################
    def on_attack(self, ctx: AttackContext) -> None:
        """Called automatically when an attack is initiated."""

        pass

################################################################################
    def stat_adjust(self) -> None:
        """Called automatically when a stat refresh is initiated."""

        pass

################################################################################
    def notify(self, *args) -> None:
        """The default event response function if `self.notify()` is called
        with no callback argument."""

        pass

################################################################################
    @property
    def effect(self) -> Optional[int]:
        """Returns this skill's outgoing active attack value, if any."""

        if self._effect is None:
            return

        return int(self._effect.base + (self._effect.scalar * self.owner.level))

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

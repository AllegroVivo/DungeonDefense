from __future__ import annotations

from typing     import TYPE_CHECKING, List

from .context  import Context

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.monster import DMMonster
################################################################################

__all__ = ("EggHatchContext",)

################################################################################
class EggHatchContext(Context):

    __slots__ = (
        "_options",
    )

################################################################################
    def __init__(self, state: DMGame, options: List[DMMonster]):

        super().__init__(state)

        self._options: List[DMMonster] = options

################################################################################
    def set_options(self, *options: DMMonster) -> None:

        self._options = [m for m in options]

################################################################################
    def execute(self) -> None:

        for m in self._options:
            self._state.inventory.add_monster(m)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING, List

from .context  import Context

if TYPE_CHECKING:
    from dm.core    import DMGame, DMMonster
################################################################################

__all__ = ("EggHatchContext",)

################################################################################
class EggHatchContext(Context):

    __slots__ = (
        "options",
    )

################################################################################
    def __init__(self, state: DMGame, options: List[DMMonster]):

        super().__init__(state)

        self.options: List[DMMonster] = options

################################################################################
    def set_options(self, *options: DMMonster) -> None:

        self.options = [m for m in options]

################################################################################
    def execute(self) -> None:

        for m in self.options:
            self._state.inventory.add_monster(m)

################################################################################

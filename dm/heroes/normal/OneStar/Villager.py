from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ....core.objects   import DMHero

if TYPE_CHECKING:
    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("Villager",)

################################################################################
class Villager(DMHero):

    def __init__(self, game: DMGame, spawn_room: Optional[DMRoom] = None):

        super().__init__(
            game,
            _id="HRO-102",
            name="Villager",
            rank=1,
            room=spawn_room
        )

################################################################################

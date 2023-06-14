from __future__ import annotations

from typing     import TYPE_CHECKING, Optional

from ....core.objects   import DMHero

if TYPE_CHECKING:
    from dm.core    import DMGame, DMRoom
################################################################################

__all__ = ("Farmer",)

################################################################################
class Farmer(DMHero):

    def __init__(self, game: DMGame, spawn_room: Optional[DMRoom] = None):

        super().__init__(
            game,
            _id="HRO-101",
            name="Farmer",
            rank=1,
            room=spawn_room
        )

################################################################################

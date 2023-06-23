from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional, Tuple

from ..battleroom   import DMBattleRoom
from ...core.objects.hero import DMHero
from utilities import UnlockPack, Effect

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.objects.unit import DMUnit
    from dm.core.contexts.attack import AttackContext
################################################################################

__all__ = ("Prism",)

################################################################################
class Prism(DMBattleRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-175",
            name="Prism",
            description=(
                "Gives {mirror} Mirror and {pleasure} Pleasure to deployed "
                "monsters whenever a hero enters. The Dark Lord gets 1 Mirror "
                "when a hero dies in this room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced,
            effects=[
                Effect(name="Mirror", base=1, per_lv=1),
                Effect(name="Pleasure", base=20, per_lv=20)
            ]
        )

################################################################################
    def on_enter(self, unit: DMUnit) -> None:

        for monster in self.monsters:
            monster.add_status("Mirror", self.effects["Mirror"], self)
            monster.add_status("Pleasure", self.effects["Pleasure"], self)

################################################################################
    def on_acquire(self) -> None:
        """Called automatically when this room is added to the map."""

        self.listen("on_death")

################################################################################
    def notify(self, ctx: AttackContext) -> None:

        if ctx.room == self:
            if isinstance(ctx.target, DMHero):
                self.game.dark_lord.add_status("Mirror", 1)

################################################################################

from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom           import DMBattleRoom
from ...core.objects.hero   import DMHero
from utilities              import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame, RoomChangeContext
################################################################################

__all__ = ("Prism",)

################################################################################
class Prism(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-131",
            name="Prism",
            description=(
                "Gives 1 (+1 per Lv) Mirror and 20 (+20 per Lv) Pleasure to "
                "deployed monsters whenever a hero enters. The Dark Lord gets "
                "1 Mirror when a hero dies in this room."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Advanced
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_room_change", self.on_room_change)
        self.game.subscribe_event("on_death", self.on_death)

################################################################################
    def on_room_change(self, **kwargs) -> None:

        ctx: RoomChangeContext = kwargs.get("ctx")
        if ctx.target_room == self:
            for monster in self.monsters:
                monster += self.game.spawn("Mirror", stacks=1 + (1 * self.level))
                monster += self.game.spawn("Pleasure", stacks=self.effect_value())

################################################################################
    def on_death(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")
        if ctx.room == self:
            if isinstance(ctx.defender, DMHero):
                self.game.dark_lord += self.game.spawn("Mirror")

################################################################################
    def effect_value(self) -> int:

        return 20 + (20 * self.level)

################################################################################

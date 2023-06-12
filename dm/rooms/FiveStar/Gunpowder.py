from __future__ import annotations

from typing     import TYPE_CHECKING

from ..battleroom   import DMBattleRoom
from utilities      import UnlockPack

if TYPE_CHECKING:
    from dm.core    import AttackContext, DMGame
################################################################################

__all__ = ("Gunpowder",)

################################################################################
class Gunpowder(DMBattleRoom):

    def __init__(self, game: DMGame, row: int, col: int, level: int = 1):

        super().__init__(
            game, row, col,
            _id="BTL-122",
            name="Gunpowder",
            description=(
                "If the attacked character in this room is under effect of Burn, "
                "it consumes all of Burn state and inflicts 200 (+50 per Lv) %x "
                "damage to the unit and all nearby enemies."
            ),
            level=level,
            rank=5,
            unlock=UnlockPack.Original
        )

################################################################################
    def on_acquire(self) -> None:

        self.game.subscribe_event("on_attack", self.notify)

################################################################################
    def notify(self, **kwargs) -> None:

        ctx: AttackContext = kwargs.get("ctx")
        if ctx.room == self:
            burn = ctx.defender.get_status("Burn")
            if burn is not None:
                for hero in ctx.room.heroes:
                    hero.damage(burn.stacks * self.effect_value())
                burn.reduce_stacks(burn.stacks)

################################################################################
    def effect_value(self) -> int:

        return 200 + (50 * self.level) // 100

################################################################################

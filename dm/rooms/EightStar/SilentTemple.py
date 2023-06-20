from __future__ import annotations

from pygame     import Vector2
from typing     import TYPE_CHECKING, Optional

from ...core.objects.monster import DMMonster
from ..facilityroom import DMFacilityRoom
from utilities import UnlockPack

if TYPE_CHECKING:
    from dm.core.contexts import AttackContext
    from dm.core.game.game import DMGame
################################################################################

__all__ = ("SilentTemple",)

################################################################################
class SilentTemple(DMFacilityRoom):

    def __init__(self, game: DMGame, position: Optional[Vector2] = None, level: int = 1):

        super().__init__(
            game, position,
            _id="ROOM-216",
            name="Silent Temple",
            description=(
                "Once recharged, give {value} Focus to all monsters in the "
                "dungeon. Monsters in adjacent area will inflict 5 % extra "
                "damage per their Focus stack."
            ),
            level=level,
            rank=8,
            unlock=UnlockPack.Myth
        )
        self.setup_charging(3.3, 3.3)

################################################################################
    def on_charge(self) -> None:
        """A general event response function."""

        for monster in self.game.deployed_monsters:
            monster.add_status("Focus", self.effect_value())

################################################################################
    def effect_value(self) -> int:
        """The value(s) of this room's effect.

        Breakdown:
        ----------
        **effect = b + (a * LV)**

        In this function:

        - b is the base effectiveness.
        - a is the additional effectiveness per level.
        - LV is the level of this room.
        """

        return 10 + (2 * self.level)

################################################################################
    def handle(self, ctx: AttackContext) -> None:
        """Automatically called as part of all battle loops."""

        if isinstance(ctx.attacker, DMMonster):
            if ctx.room in self.adjacent_rooms:
                focus = ctx.attacker.get_status("Focus")
                if focus is not None:
                    ctx.amplify_pct(focus.stacks * 0.05)

################################################################################

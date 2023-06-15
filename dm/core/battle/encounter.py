from __future__ import annotations

from typing     import TYPE_CHECKING, List
from uuid       import UUID, uuid4

from ..contexts.attack  import AttackContext

if TYPE_CHECKING:
    from ..game.game    import DMGame
    from ..objects.unit import DMUnit
    from ..objects.hero import DMHero
################################################################################

__all__ = ("DMEncounter",)

################################################################################
class DMEncounter:

    __slots__ = (
        "_id",
        "_state",
        "_attacker",
        "_defender",
        "_attacks",
        "_actions_elapsed",
    )

################################################################################
    def __init__(self, state: DMGame, attacker: DMUnit, defender: DMUnit):

        self._id: UUID = uuid4()
        self._state: DMGame = state

        self._attacker: DMUnit = attacker
        self._defender: DMUnit = defender

        self._attacks: List[AttackContext] = []
        self._actions_elapsed: int = 0

################################################################################
    def __eq__(self, other: DMEncounter) -> bool:

        return self._id == other._id

################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def in_progress(self) -> bool:

        return self._defender.life > 0 and self._actions_elapsed < 12.0

################################################################################
    @property
    def attacker(self) -> DMUnit:

        return self._attacker

################################################################################
    @property
    def defender(self) -> DMUnit:

        return self._defender

################################################################################
    def run_turn(self, dt: float) -> None:

        print("=== Monster Turn ===")
        # Monster attack
        if self.attacker.action_timer >= 1 / self.attacker.dex:
            # Create and log the CTX
            ctx = AttackContext(self.game, self.attacker, self.defender)
            self._attacks.append(ctx)

            # Probably need to notify some events before execution.
            ctx.execute()

            # Reset action_timer after attack
            self.attacker.reset_action_timer()

        # Check battle over?

        print("=== Hero Turn ===")
        # Hero attack
        if self.defender.action_timer >= 1 / self.defender.dex:
            ctx = AttackContext(self.game, self.defender, self.attacker)
            self._attacks.append(ctx)

            # Probably need to notify some events before execution.
            ctx.execute()

            # Reset action_timer after attack
            self.defender.reset_action_timer()

        # Check battle over?

        # Purge any fully depleted statuses
        self.attacker.purge_depleted_statuses()
        self.defender.purge_depleted_statuses()

        # Increment participants action timers:
        self.attacker.update_action_timer(dt)
        self.defender.update_action_timer(dt)

################################################################################
################################################################################

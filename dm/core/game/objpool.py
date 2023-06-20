from __future__ import annotations

import random

from typing     import TYPE_CHECKING, Dict, List, Optional, Tuple, Type, Union

# Bulk type imports for the pool
from ...fates       import ALL_FATES, SPAWNABLE_FATES
from ...heroes      import ALL_HEROES
from ...monsters    import ALL_MONSTERS
from ...relics      import ALL_RELICS
from ...rooms       import ALL_ROOMS
from ...statuses    import ALL_STATUSES

# Smaller individual imports
from ..objects.monster  import DMMonster
from ..objects.room     import DMRoom
from ..objects.status   import DMStatus
from utilities      import DMSpawnType

if TYPE_CHECKING:
    from dm.core.game.game import DMGame
    from dm.core.fates.fatecard import DMFateCard
    from dm.core.objects.object import DMObject
    from dm.core.objects.hero import DMHero
    from dm.core.objects.relic import DMRelic
################################################################################

__all__ = ("DMObjectPool",)

################################################################################
class DMObjectPool:

    __slots__ = (
        "_state",
        "__master",
        "__monster_types",
        "__hero_types",
        "__room_types",
        "__status_types",
        "__relic_types",
        "__fate_types",
        "__monsters",
        "__heroes",
        "__rooms",
        "__statuses",
        "__relics",
        "__fates",
    )

################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state

        self.__monster_types: List[Type[DMMonster]] = ALL_MONSTERS.copy()
        self.__hero_types: List[Type[DMHero]] = ALL_HEROES.copy()
        self.__room_types: List[Type[DMRoom]] = ALL_ROOMS.copy()
        self.__status_types: List[Type[DMStatus]] = ALL_STATUSES.copy()
        self.__relic_types: List[Type[DMRelic]] = ALL_RELICS.copy()
        self.__fate_types: List[Type[DMFateCard]] = SPAWNABLE_FATES.copy()

        self.__monsters: List[DMMonster] = [m(self._state) for m in self.__monster_types]  # type: ignore
        self.__heroes: List[DMHero] = [h(self._state) for h in self.__hero_types]  # type: ignore
        self.__rooms: List[DMRoom] = [r(self._state) for r in self.__room_types]  # type: ignore
        self.__statuses: List[DMStatus] = [s(self._state, None) for s in self.__status_types]  # type: ignore
        self.__relics: List[DMRelic] = [relic(self._state) for relic in self.__relic_types]  # type: ignore
        self.__fates: List[DMFateCard] = [f(self._state, 0, 0) for f in self.__fate_types]  # type: ignore

        self.__master: List[DMObject] = (
            self.__rooms.copy() +
            self.__monsters.copy() +   # type: ignore
            self.__heroes.copy() +
            self.__relics.copy() +
            self.__statuses.copy() +
            [f(self._state, 0, 0) for f in ALL_FATES].copy()  # type: ignore
        )

################################################################################
    def spawn(
        self,
        *,
        _n: Optional[str],
        obj_id: Optional[str],
        spawn_type: Optional[DMSpawnType],
        start_rank: int,
        end_rank: int,
        weighted: bool,
        init_obj: bool,
        **kwargs
    ) -> Union[DMObject, Type[DMObject]]:
        """Attempts to spawn a DMObject per the given arguments.

        All arguments are optional, but at least one of `_n`, `obj_id`, or
        `spawn_type` must be provided.

        By default this will return a newly instantiated copy of the object utilizing
        any provided `**kwargs` that would be compatible with the spawned type's
        internal `_copy()` method.

        Parameters:
        -----------
        _n: :class:`str`
            The object's in-game name. This is the one that might have spaces and
            definitely has capital letters.

        obj_id: :class:`str`
            The unique string identifier of the object. In the general format `ABC-123`.

        spawn_type: :class:`SpawnType`
            The type of object to spawn if a random spawn is being invoked.

        start_rank: :class:`int`
            If spawning a random entity, the lowest rank group to include in the
            options.

        end_rank: :class:`int`
            If spawning a random entity, the highest rank group to include in the
            options.

        weighted: :class:`bool`
            If spawning a random entity, whether or not to weight the selection based
            on ranking, where lower ranks will appear more frequently then higher ranks.

        init_obj: :class:`bool`
            Whether to return only the class type or an instantiated copy of the
            class with the given `**kwargs`.

        Returns:
        --------
        Union[:class:`DMObject`, Type[:class:`DMObject`]]
            Either the type of the returned spawn or a cleanly instantiated copy
            utilizing the provided `**kwargs` if `init_obj` was set to True.
        """

        # Try to search by name if passed.
        if _n is not None:
            try:
                obj = [o for o in self.__master if o.name == _n or o._id == obj_id][0]
            except IndexError:
                raise ValueError(f"Invalid status effect name |{_n}| provided to ObjectPool.spawn().")

            if isinstance(obj, DMStatus) or init_obj:
                return obj._copy(**kwargs)
            else:
                return type(obj)

        # If spawning a specific object, do that.
        if obj_id is not None:
            results = [obj for obj in self.__master if obj._id == obj_id]
            if not results:
                raise ValueError(f"Invalid object ID |{obj_id}| provided to ObjectPool.spawn().")
            else:
                result = results[0]
                if isinstance(result, DMStatus) or init_obj:
                    return result._copy(**kwargs)
                else:
                    return type(result)

        # Otherwise it's a random spawn.
        if spawn_type is None:
            raise ValueError("spawn_type cannot be None for ObjectPool.spawn() if no obj_id is provided.")

        match spawn_type:
            case DMSpawnType.Monster:
                source = self.__monsters
            case DMSpawnType.Hero:
                source = self.__heroes
            case DMSpawnType.Relic:
                source = self.__relics
            case DMSpawnType.Fate:
                source = self.__fates
            case _:
                source = self.__rooms

        # Initial values
        objs = {}
        for dm_object in source:
            try:
                objs[dm_object.rank].append(type(dm_object))
            except KeyError:
                objs[dm_object.rank] = [type(dm_object)]

        eligible_objs = {rank: objs[rank] for rank in range(start_rank, end_rank + 1)}

        eligible_weights = None
        if weighted:
            weights = self._generate_weights(spawn_type)
            eligible_weights = [weights[rank] for rank in range(start_rank, end_rank + 1)]

        chosen_idx = random.choices(
            list(eligible_objs.keys()), weights=eligible_weights, k=1
        )[0]

        result = random.choice(eligible_objs[chosen_idx])

        if not init_obj:
            return result

        return result(self._state)._copy(**kwargs)

################################################################################
    def _generate_weights(self, spawn_type: DMSpawnType) -> Dict[int, float]:
        # Define the start and end weights for each rank
        rank_weights = self._base_weights(spawn_type)

        # Calculate the weight for each rank based on the current day
        weights = {}
        for rank, (start_weight, end_weight) in rank_weights.items():
            weight = start_weight + ((end_weight - start_weight) * (self._state.day.current / 2000))  # 2000 is the "max" day
            weights[rank] = weight

        # Normalize the weights so they sum to 1
        total_weight = sum(weights.values())
        normalized_weights = {rank: weight / total_weight for rank, weight in weights.items()}

        return normalized_weights

################################################################################
    @staticmethod
    def generate_type(raw_type: str) -> Type[DMObject]:

        if raw_type == "room":
            return DMRoom  # type: ignore
        if raw_type == "monster":
            return DMMonster  # type: ignore

        raise ValueError("Invalid raw_type provided to ObjectPool.generate_type().")

################################################################################
    @staticmethod
    def _base_weights(_type: DMSpawnType) -> Dict[int, Tuple[int, int]]:
        """Returns a rank vs. weight-over-time mapping for the given spawn type."""

        if _type == DMSpawnType.Monster:
            return {
                1: (100, 50),
                2: (50, 40),
                3: (10, 30),
                4: (5, 15),
                5: (1, 5),
            }
        elif _type == DMSpawnType.Hero:
            pass
        elif _type == DMSpawnType.Relic:
            pass
        elif _type == DMSpawnType.Fate:
            return {
                1: (100, 100),
                2: (40, 40),
                3: (30, 30),
                4: (15, 15),
                5: (2, 5),
            }
        elif _type == DMSpawnType.Room:
            pass
        else:
            raise ValueError("Invalid spawn type provided to ObjectPool._base_weights().")

################################################################################

from typing     import TYPE_CHECKING, Dict, Type

if TYPE_CHECKING:
    from ..core     import DMState
################################################################################

__all__ = ("STATE_MAPPINGS", )

################################################################################
# Public States
# Packages
from .battle        import *
from .deployment    import *
from .fates         import *
from .menus         import *

# Modules
from ._debug                import _DebugState
# from .dng_rest          import RestFateState
# from .dng_upgrade       import UpgradeFateState
# from .dungeon_fate      import DungeonFateSelectState
# from .dungeon_menu      import DungeonMenuState
# from .dungeon_select    import DungeonSelectionState
# from .infocarddebug     import InfoCardDebugState
# from .popup             import PopupBoxState
# from ._vert_menu        import VerticalMenuState
################################################################################

STATE_MAPPINGS: Dict[str, Type["DMState"]] = {
    "main_menu" : MainMenuState,
    "debug_mode" : _DebugState,
    "new_game" : NewGameState,
    "auto_deploy" : AutoDeployState,
    "manual_deploy_a" : ManualDeployStateA,
    "manual_deploy_b" : ManualDeployStateB,
    "fate_board_view" : FateBoardViewState,
    "fate_select" : FateCardSelectState,
    "battle" : BattleState
}

################################################################################

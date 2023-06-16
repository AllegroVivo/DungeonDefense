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
    "battle" : BattleState,
}
################################################################################

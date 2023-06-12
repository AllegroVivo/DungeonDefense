import traceback

from typing     import List, Optional
################################################################################

__all__ = (
    "DMException",
    "ArgumentTypeError",
    "ArgumentMissingError",
)

################################################################################
class DMException(Exception):

    def __init__(
        self,
        ctx: str,
        message: Optional[str],
        additional_info: Optional[str]
    ):

        super().__init__(message or "Please check the custom breakdown provided.")

        self._ctx: str = ctx
        self._addl_info: Optional[str] = additional_info

################################################################################
    @property
    def additional_info(self) -> str:

        return (
            "\n==================================================\n"
            f"{self._addl_info}"
        ) if self._addl_info is not None else ""

################################################################################
    @property
    def tb(self) -> str:

        return traceback.format_exc()

################################################################################
class ArgumentTypeError(DMException):

    def __init__(
        self,
        ctx: str,
        invalid_arg_type: type,
        *req_arg_types: type,
        message: Optional[str] = None,
        additional_info: Optional[str] = None
    ):

        super().__init__(ctx, message, additional_info)

        self._error_type: type = invalid_arg_type
        self._target_types: List[type] = [t for t in req_arg_types]

################################################################################
    def __repr__(self) -> str:

        acceptable_types = "/".join([t.__name__ for t in self._target_types])

        return (
            "Traceback:\n"
            f"{self.tb}\n"
            "==================================================\n"
            "<ArgumentTypeException Raised!>\n"
            f"An object of type {self._error_type.__name__} was passed to function "
            f"{self._ctx}.\n"
            f"The accepted type(s) are as follows: {acceptable_types}."
            f"{self.additional_info}"
        )

################################################################################
class ArgumentMissingError(DMException):

    def __init__(
        self,
        ctx: str,
        missing_arg_name: str,
        *missing_arg_types: type,
        message: Optional[str] = None,
        additional_info: Optional[str] = None
    ):
        super().__init__(ctx, message, additional_info)

        self._arg_name: str = missing_arg_name
        self._missing_types: List[type] = [t for t in missing_arg_types]

################################################################################
    def __repr__(self):

        missing = "/".join([t.__name__ for t in self._missing_types])

        return (
            "Traceback:\n"
            f"{self.tb}\n"
            "==================================================\n"
            "<ArgumentTypeException Raised!>\n"
            f"'{self._arg_name}' was not passed to {self._ctx}.\n"
            f"Valid type(s) for the missing argument are as follows: {missing}."
            f"{self.additional_info}"
        )

################################################################################

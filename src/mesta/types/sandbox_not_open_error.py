
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_not_open_error_error import SandboxNotOpenErrorError


class SandboxNotOpenError(UniversalBaseModel):
    """
    The 403 body of the challenge, create and sign-up routes until the sandbox opens to the public. Mesta's firewall returns it before the API, so it carries no requestId.
    """

    error: SandboxNotOpenErrorError = pydantic.Field()
    """
    Error details
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

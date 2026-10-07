
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_provisioning_paused_error_error import SandboxProvisioningPausedErrorError


class SandboxProvisioningPausedError(UniversalBaseModel):
    """
    The 503 body of the challenge, create and sign-up routes. PROVISIONING_PAUSED adds pauseMessage at the root beside error and requestId; SANDBOX_SERVICE_UNAVAILABLE has no pauseMessage.
    """

    error: SandboxProvisioningPausedErrorError = pydantic.Field()
    """
    Error details
    """

    request_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique request identifier for debugging"),
    ]
    """
    Unique request identifier for debugging
    """

    pause_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pauseMessage"),
        pydantic.Field(
            alias="pauseMessage",
            description="Present with PROVISIONING_PAUSED: Mesta's message to developers while new sandboxes are paused (for example when they resume), or null when none is set. Show it as given.",
        ),
    ] = None
    """
    Present with PROVISIONING_PAUSED: Mesta's message to developers while new sandboxes are paused (for example when they resume), or null when none is set. Show it as given.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

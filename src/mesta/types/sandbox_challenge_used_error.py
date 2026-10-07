
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_challenge_used_error_error import SandboxChallengeUsedErrorError


class SandboxChallengeUsedError(UniversalBaseModel):
    error: SandboxChallengeUsedErrorError = pydantic.Field()
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

    sandbox_id: typing_extensions.Annotated[str, FieldMetadata(alias="sandboxId"), pydantic.Field(alias="sandboxId")]
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

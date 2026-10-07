
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_claim_email_owns_sandbox_error_error import SandboxClaimEmailOwnsSandboxErrorError


class SandboxClaimEmailOwnsSandboxError(UniversalBaseModel):
    error: SandboxClaimEmailOwnsSandboxErrorError = pydantic.Field()
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

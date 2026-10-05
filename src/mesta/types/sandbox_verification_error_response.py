
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_verification_error_response_error import SandboxVerificationErrorResponseError


class SandboxVerificationErrorResponse(UniversalBaseModel):
    """
    Wrong verification code. Request a new code when attemptsRemaining is zero; a resend voids the previous code and issues a new code with five attempts.
    """

    error: SandboxVerificationErrorResponseError
    request_id: typing_extensions.Annotated[int, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

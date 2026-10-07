
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_verification_error_response_error_code import SandboxVerificationErrorResponseErrorCode
from .sandbox_verification_error_response_error_details import SandboxVerificationErrorResponseErrorDetails


class SandboxVerificationErrorResponseError(UniversalBaseModel):
    code: typing_extensions.Annotated[
        SandboxVerificationErrorResponseErrorCode, FieldMetadata(alias="CODE"), pydantic.Field(alias="CODE")
    ]
    message: typing_extensions.Annotated[str, FieldMetadata(alias="MESSAGE"), pydantic.Field(alias="MESSAGE")]
    details: typing_extensions.Annotated[
        SandboxVerificationErrorResponseErrorDetails, FieldMetadata(alias="DETAILS"), pydantic.Field(alias="DETAILS")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

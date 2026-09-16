
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .verify_sender_requirements_missing_error_error import VerifySenderRequirementsMissingErrorError


class VerifySenderRequirementsMissingError(UniversalBaseModel):
    error: VerifySenderRequirementsMissingErrorError = pydantic.Field()
    """
    Standard Mesta error envelope. Property names are uppercase.
    """

    request_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Trace identifier for support and debugging."),
    ] = None
    """
    Trace identifier for support and debugging.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

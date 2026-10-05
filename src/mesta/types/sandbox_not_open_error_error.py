
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_not_open_error_error_code import SandboxNotOpenErrorErrorCode


class SandboxNotOpenErrorError(UniversalBaseModel):
    """
    Error details
    """

    code: typing_extensions.Annotated[
        SandboxNotOpenErrorErrorCode,
        FieldMetadata(alias="CODE"),
        pydantic.Field(alias="CODE", description="Machine-readable error code"),
    ]
    """
    Machine-readable error code
    """

    message: typing_extensions.Annotated[
        str, FieldMetadata(alias="MESSAGE"), pydantic.Field(alias="MESSAGE", description="Human-readable error message")
    ]
    """
    Human-readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

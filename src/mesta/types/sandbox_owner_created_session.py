
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxOwnerCreatedSession(UniversalBaseModel):
    access_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ]
    refresh_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="refreshToken"), pydantic.Field(alias="refreshToken")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

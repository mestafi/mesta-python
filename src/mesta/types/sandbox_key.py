
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_key_kind import SandboxKeyKind


class SandboxKey(UniversalBaseModel):
    id: str
    kind: SandboxKeyKind
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey"), pydantic.Field(alias="apiKey")]
    api_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="apiSecret"),
        pydantic.Field(alias="apiSecret", description="Shown once; store immediately."),
    ]
    """
    Shown once; store immediately.
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="The creation or claim deadline. Later verification clears expiry only for keys flagged expires_with_sandbox; a retiring predecessor keeps its 24-hour deadline and is never revived.",
        ),
    ]
    """
    The creation or claim deadline. Later verification clears expiry only for keys flagged expires_with_sandbox; a retiring predecessor keeps its 24-hour deadline and is never revived.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

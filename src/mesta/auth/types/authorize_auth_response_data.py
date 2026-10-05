
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .authorize_auth_response_data_kind import AuthorizeAuthResponseDataKind
from .authorize_auth_response_data_plane import AuthorizeAuthResponseDataPlane


class AuthorizeAuthResponseData(UniversalBaseModel):
    kind: typing.Optional[AuthorizeAuthResponseDataKind] = None
    plane: typing.Optional[AuthorizeAuthResponseDataPlane] = None
    sandbox_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sandboxId"),
        pydantic.Field(alias="sandboxId", description="Null outside a sandbox merchant."),
    ] = None
    """
    Null outside a sandbox merchant.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="Nullable expiry. Verification clears it only for keys flagged expires_with_sandbox; a retiring predecessor keeps its 24-hour deadline and is never revived.",
        ),
    ] = None
    """
    Nullable expiry. Verification clears it only for keys flagged expires_with_sandbox; a retiring predecessor keeps its 24-hour deadline and is never revived.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the authenticated principal
    """

    entity: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of principal (user or apiKey)
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The authenticated user or API key data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

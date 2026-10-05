
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_api_keys_response_data_kind import GetApiKeysResponseDataKind


class GetApiKeysResponseData(UniversalBaseModel):
    kind: typing.Optional[GetApiKeysResponseDataKind] = None
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

    last_used_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUsedAt"),
        pydantic.Field(alias="lastUsedAt", description="Null before first use; updated at most once a minute."),
    ] = None
    """
    Null before first use; updated at most once a minute.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the API key
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the API key was created"),
    ] = None
    """
    Timestamp when the API key was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the API key was last updated"),
    ] = None
    """
    Timestamp when the API key was last updated
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable name for the API key
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="ID of the merchant this API key belongs to"),
    ] = None
    """
    ID of the merchant this API key belongs to
    """

    permissions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of permissions granted to this API key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

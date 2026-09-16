
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class GetAcceptanceTermsOfServiceResponseData(UniversalBaseModel):
    sender_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderName"),
        pydantic.Field(alias="senderName", description="Name of the sender"),
    ] = None
    """
    Name of the sender
    """

    sender_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderEmail"),
        pydantic.Field(alias="senderEmail", description="Email of the sender"),
    ] = None
    """
    Email of the sender
    """

    merchant_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantName"),
        pydantic.Field(alias="merchantName", description="Name of the associated merchant"),
    ] = None
    """
    Name of the associated merchant
    """

    tos_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tosVersion"),
        pydantic.Field(alias="tosVersion", description="Version of the Terms of Service"),
    ] = None
    """
    Version of the Terms of Service
    """

    is_expired: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isExpired"),
        pydantic.Field(alias="isExpired", description="Whether the TOS acceptance link has expired"),
    ] = None
    """
    Whether the TOS acceptance link has expired
    """

    is_accepted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isAccepted"),
        pydantic.Field(alias="isAccepted", description="Whether the TOS has already been accepted"),
    ] = None
    """
    Whether the TOS has already been accepted
    """

    generated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="generatedAt"),
        pydantic.Field(alias="generatedAt", description="When the TOS link was generated"),
    ] = None
    """
    When the TOS link was generated
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="When the TOS link expires"),
    ] = None
    """
    When the TOS link expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

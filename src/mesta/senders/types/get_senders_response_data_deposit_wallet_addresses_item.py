
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetSendersResponseDataDepositWalletAddressesItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the wallet address
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the record
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Creation timestamp"),
    ] = None
    """
    Creation timestamp
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Last update timestamp"),
    ] = None
    """
    Last update timestamp
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The blockchain address
    """

    chain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The blockchain network
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Associated merchant ID"),
    ] = None
    """
    Associated merchant ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

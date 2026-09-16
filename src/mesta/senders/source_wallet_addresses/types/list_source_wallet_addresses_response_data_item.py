
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_source_wallet_addresses_response_data_item_chain import ListSourceWalletAddressesResponseDataItemChain
from .list_source_wallet_addresses_response_data_item_owner_type import (
    ListSourceWalletAddressesResponseDataItemOwnerType,
)
from .list_source_wallet_addresses_response_data_item_risk_level import (
    ListSourceWalletAddressesResponseDataItemRiskLevel,
)


class ListSourceWalletAddressesResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the source wallet address
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the record
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the source wallet address was created"),
    ] = None
    """
    Timestamp when the source wallet address was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the source wallet address was last updated"),
    ] = None
    """
    Timestamp when the source wallet address was last updated
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The blockchain address
    """

    chain: typing.Optional[ListSourceWalletAddressesResponseDataItemChain] = pydantic.Field(default=None)
    """
    The blockchain network
    """

    owner_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerId"),
        pydantic.Field(alias="ownerId", description="ID of the entity that owns this address"),
    ] = None
    """
    ID of the entity that owns this address
    """

    owner_type: typing_extensions.Annotated[
        typing.Optional[ListSourceWalletAddressesResponseDataItemOwnerType],
        FieldMetadata(alias="ownerType"),
        pydantic.Field(alias="ownerType", description="Type of the address owner"),
    ] = None
    """
    Type of the address owner
    """

    risk_level: typing_extensions.Annotated[
        typing.Optional[ListSourceWalletAddressesResponseDataItemRiskLevel],
        FieldMetadata(alias="riskLevel"),
        pydantic.Field(alias="riskLevel", description="Risk assessment level of the address"),
    ] = None
    """
    Risk assessment level of the address
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="ID of the merchant associated with this address"),
    ] = None
    """
    ID of the merchant associated with this address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

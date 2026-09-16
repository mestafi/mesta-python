
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .create_source_wallet_addresses_response_data_item_chain import CreateSourceWalletAddressesResponseDataItemChain
from .create_source_wallet_addresses_response_data_item_owner_type import (
    CreateSourceWalletAddressesResponseDataItemOwnerType,
)
from .create_source_wallet_addresses_response_data_item_risk_level import (
    CreateSourceWalletAddressesResponseDataItemRiskLevel,
)


class CreateSourceWalletAddressesResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    address: typing.Optional[str] = None
    chain: typing.Optional[CreateSourceWalletAddressesResponseDataItemChain] = None
    owner_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")
    ] = None
    owner_type: typing_extensions.Annotated[
        typing.Optional[CreateSourceWalletAddressesResponseDataItemOwnerType],
        FieldMetadata(alias="ownerType"),
        pydantic.Field(alias="ownerType"),
    ] = None
    risk_level: typing_extensions.Annotated[
        typing.Optional[CreateSourceWalletAddressesResponseDataItemRiskLevel],
        FieldMetadata(alias="riskLevel"),
        pydantic.Field(alias="riskLevel"),
    ] = None
    merchant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId")
    ] = None
    is_whitelisted_on_providers: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isWhitelistedOnProviders"),
        pydantic.Field(alias="isWhitelistedOnProviders"),
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_deposit_wallet_address_orders_response_data_chain import GetDepositWalletAddressOrdersResponseDataChain


class GetDepositWalletAddressOrdersResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the wallet address
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the wallet record
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the wallet was created"),
    ] = None
    """
    Timestamp when the wallet was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the wallet was last updated"),
    ] = None
    """
    Timestamp when the wallet was last updated
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The blockchain wallet address
    """

    chain: typing.Optional[GetDepositWalletAddressOrdersResponseDataChain] = pydantic.Field(default=None)
    """
    The blockchain network
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Identifier of the associated merchant"),
    ] = None
    """
    Identifier of the associated merchant
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fiat_deposit_list_item_currency import FiatDepositListItemCurrency


class FiatDepositListItem(UniversalBaseModel):
    """
    Fiat deposit object for list responses (excludes depositDetails)
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the deposit
    """

    amount: str = pydantic.Field()
    """
    Deposit amount (decimal with 2 decimal places)
    """

    currency: FiatDepositListItemCurrency = pydantic.Field()
    """
    Fiat currency code
    """

    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="Associated transaction ID"),
    ] = None
    """
    Associated transaction ID
    """

    merchant_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId", description="Merchant ID")
    ]
    """
    Merchant ID
    """

    sender_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="senderId"), pydantic.Field(alias="senderId", description="Sender ID")
    ] = None
    """
    Sender ID
    """

    deposit_bank_account_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="depositBankAccountId"),
        pydantic.Field(alias="depositBankAccountId", description="Deposit bank account ID"),
    ]
    """
    Deposit bank account ID
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

    merchant_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantName"),
        pydantic.Field(alias="merchantName", description="Name of the merchant"),
    ] = None
    """
    Name of the merchant
    """

    merchant_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantEmail"),
        pydantic.Field(alias="merchantEmail", description="Email of the merchant"),
    ] = None
    """
    Email of the merchant
    """

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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

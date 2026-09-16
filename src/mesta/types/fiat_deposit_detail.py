
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fiat_deposit_detail_currency import FiatDepositDetailCurrency
from .fiat_deposit_detail_deposit_details import FiatDepositDetailDepositDetails


class FiatDepositDetail(UniversalBaseModel):
    """
    Fiat deposit object for detail responses (includes depositDetails)
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the deposit
    """

    amount: str = pydantic.Field()
    """
    Deposit amount (decimal with 2 decimal places)
    """

    currency: FiatDepositDetailCurrency = pydantic.Field()
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

    deposit_details: typing_extensions.Annotated[
        typing.Optional[FiatDepositDetailDepositDetails],
        FieldMetadata(alias="depositDetails"),
        pydantic.Field(alias="depositDetails", description="Details of the deposit transaction from the bank"),
    ] = None
    """
    Details of the deposit transaction from the bank
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

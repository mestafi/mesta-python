
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_transfers_response_data_status import CreateTransfersResponseDataStatus
from .create_transfers_response_data_transfer_type import CreateTransfersResponseDataTransferType


class CreateTransfersResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the internal transfer (order id)
    """

    sender_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderId"),
        pydantic.Field(alias="senderId", description="Identifier of the source sender"),
    ] = None
    """
    Identifier of the source sender
    """

    beneficiary_sender_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="beneficiarySenderId"),
        pydantic.Field(alias="beneficiarySenderId", description="Identifier of the recipient sender"),
    ] = None
    """
    Identifier of the recipient sender
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Identifier of the merchant"),
    ] = None
    """
    Identifier of the merchant
    """

    transfer_type: typing_extensions.Annotated[
        typing.Optional[CreateTransfersResponseDataTransferType],
        FieldMetadata(alias="transferType"),
        pydantic.Field(alias="transferType", description="Always `internal` for internal transfers"),
    ] = None
    """
    Always `internal` for internal transfers
    """

    source_currency: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceCurrency"),
        pydantic.Field(alias="sourceCurrency", description="Source currency code"),
    ] = None
    """
    Source currency code
    """

    target_currency: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="targetCurrency"),
        pydantic.Field(alias="targetCurrency", description="Target currency code"),
    ] = None
    """
    Target currency code
    """

    accepted_gross_source_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="acceptedGrossSourceAmount"),
        pydantic.Field(
            alias="acceptedGrossSourceAmount",
            description="Amount debited from the source sender in source currency (including fees)",
        ),
    ] = None
    """
    Amount debited from the source sender in source currency (including fees)
    """

    target_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="targetAmount"),
        pydantic.Field(alias="targetAmount", description="Amount credited to the recipient sender in target currency"),
    ] = None
    """
    Amount credited to the recipient sender in target currency
    """

    accepted_quote_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="acceptedQuoteId"),
        pydantic.Field(alias="acceptedQuoteId", description="Identifier of the accepted internal quote"),
    ] = None
    """
    Identifier of the accepted internal quote
    """

    status: typing.Optional[CreateTransfersResponseDataStatus] = pydantic.Field(default=None)
    """
    Current status of the internal transfer. `created` on creation, `funds_received` once the source sender is debited, `success` once the recipient sender is credited.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the transfer was created"),
    ] = None
    """
    Timestamp when the transfer was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the transfer was last updated"),
    ] = None
    """
    Timestamp when the transfer was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

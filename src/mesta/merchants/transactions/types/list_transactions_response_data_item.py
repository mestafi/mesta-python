
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class ListTransactionsResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the transaction
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Merchant identifier"),
    ] = None
    """
    Merchant identifier
    """

    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction amount as a decimal string
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency code
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction type
    """

    sender_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderId"),
        pydantic.Field(alias="senderId", description="Sender identifier"),
    ] = None
    """
    Sender identifier
    """

    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="Transaction ID (exposed only to org)"),
    ] = None
    """
    Transaction ID (exposed only to org)
    """

    virtual_transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="virtualTransactionId"),
        pydantic.Field(alias="virtualTransactionId", description="Virtual transaction ID (exposed only to org)"),
    ] = None
    """
    Virtual transaction ID (exposed only to org)
    """

    order_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="orderId"),
        pydantic.Field(alias="orderId", description="Order identifier"),
    ] = None
    """
    Order identifier
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the transaction was created"),
    ] = None
    """
    Timestamp when the transaction was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the transaction was last updated"),
    ] = None
    """
    Timestamp when the transaction was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

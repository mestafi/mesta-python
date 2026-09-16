
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.beneficiary_relationship import BeneficiaryRelationship
from ...types.order_document import OrderDocument
from ...types.purpose import Purpose
from ...types.source_of_funds import SourceOfFunds
from .get_orders_response_data_status import GetOrdersResponseDataStatus


class GetOrdersResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the order
    """

    sender_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderId"),
        pydantic.Field(alias="senderId", description="Identifier of the sender"),
    ] = None
    """
    Identifier of the sender
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Identifier of the merchant"),
    ] = None
    """
    Identifier of the merchant
    """

    beneficiary_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="beneficiaryId"),
        pydantic.Field(alias="beneficiaryId", description="Identifier of the beneficiary"),
    ] = None
    """
    Identifier of the beneficiary
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
        pydantic.Field(alias="acceptedGrossSourceAmount", description="Accepted amount in source currency"),
    ] = None
    """
    Accepted amount in source currency
    """

    target_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="targetAmount"),
        pydantic.Field(alias="targetAmount", description="Amount in target currency"),
    ] = None
    """
    Amount in target currency
    """

    accepted_quote_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="acceptedQuoteId"),
        pydantic.Field(alias="acceptedQuoteId", description="Identifier of the accepted quote"),
    ] = None
    """
    Identifier of the accepted quote
    """

    status: typing.Optional[GetOrdersResponseDataStatus] = pydantic.Field(default=None)
    """
    Current status of the order
    """

    batch_order_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="batchOrderId"),
        pydantic.Field(alias="batchOrderId", description="Identifier of the batch order (if part of a batch)"),
    ] = None
    """
    Identifier of the batch order (if part of a batch)
    """

    cancellation_remarks: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cancellationRemarks"),
        pydantic.Field(alias="cancellationRemarks", description="Remarks for order cancellation"),
    ] = None
    """
    Remarks for order cancellation
    """

    merchant_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantName"),
        pydantic.Field(alias="merchantName", description="Name of the merchant"),
    ] = None
    """
    Name of the merchant
    """

    sender_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderName"),
        pydantic.Field(alias="senderName", description="Name of the sender"),
    ] = None
    """
    Name of the sender
    """

    beneficiary_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="beneficiaryName"),
        pydantic.Field(alias="beneficiaryName", description="Name of the beneficiary"),
    ] = None
    """
    Name of the beneficiary
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the order was created"),
    ] = None
    """
    Timestamp when the order was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the order was last updated"),
    ] = None
    """
    Timestamp when the order was last updated
    """

    awaiting_funds_expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="awaitingFundsExpiresAt"),
        pydantic.Field(alias="awaitingFundsExpiresAt", description="Timestamp when the awaiting funds status expires"),
    ] = None
    """
    Timestamp when the awaiting funds status expires
    """

    purpose: typing.Optional[Purpose] = None
    source_of_funds: typing_extensions.Annotated[
        typing.Optional[SourceOfFunds], FieldMetadata(alias="sourceOfFunds"), pydantic.Field(alias="sourceOfFunds")
    ] = None
    beneficiary_relationship: typing_extensions.Annotated[
        typing.Optional[BeneficiaryRelationship],
        FieldMetadata(alias="beneficiaryRelationship"),
        pydantic.Field(alias="beneficiaryRelationship"),
    ] = None
    documents: typing.Optional[typing.List[OrderDocument]] = pydantic.Field(default=None)
    """
    Array of supporting documents
    """

    uetr: typing.Optional[str] = pydantic.Field(default=None)
    """
    SWIFT Universal End-to-End Transaction Reference for tracking wire transfers
    """

    imad: typing.Optional[str] = pydantic.Field(default=None)
    """
    Fedwire Input Message Accountability Data for tracking domestic wire transfers
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Custom metadata attached to the order
    """

    rejection_remarks: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rejectionRemarks"),
        pydantic.Field(alias="rejectionRemarks", description="Reason for order rejection, if the order was declined"),
    ] = None
    """
    Reason for order rejection, if the order was declined
    """

    payment_method_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentMethodId"),
        pydantic.Field(alias="paymentMethodId", description="Identifier of the payment method used for this order"),
    ] = None
    """
    Identifier of the payment method used for this order
    """

    customer_reference_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="customerReferenceId"),
        pydantic.Field(alias="customerReferenceId", description="Merchant's internal reference ID for this order"),
    ] = None
    """
    Merchant's internal reference ID for this order
    """

    disbursement_blockchain_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="disbursementBlockchainHash"),
        pydantic.Field(
            alias="disbursementBlockchainHash", description="Blockchain transaction hash for crypto disbursements"
        ),
    ] = None
    """
    Blockchain transaction hash for crypto disbursements
    """

    payment_processing_partner: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentProcessingPartner"),
        pydantic.Field(
            alias="paymentProcessingPartner", description="Name of the payment processing partner used for disbursement"
        ),
    ] = None
    """
    Name of the payment processing partner used for disbursement
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

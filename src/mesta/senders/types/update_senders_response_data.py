
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.sender_associate import SenderAssociate
from ...types.sender_onboarding_info import SenderOnboardingInfo
from .update_senders_response_data_addresses_item import UpdateSendersResponseDataAddressesItem
from .update_senders_response_data_business_type import UpdateSendersResponseDataBusinessType
from .update_senders_response_data_documents_item import UpdateSendersResponseDataDocumentsItem
from .update_senders_response_data_gender import UpdateSendersResponseDataGender
from .update_senders_response_data_identity import UpdateSendersResponseDataIdentity
from .update_senders_response_data_kyb import UpdateSendersResponseDataKyb
from .update_senders_response_data_risk_score import UpdateSendersResponseDataRiskScore
from .update_senders_response_data_status import UpdateSendersResponseDataStatus
from .update_senders_response_data_tos import UpdateSendersResponseDataTos
from .update_senders_response_data_type import UpdateSendersResponseDataType


class UpdateSendersResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the sender
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the sender record
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the sender was created (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the sender was created (ISO 8601 format)
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the sender was last updated (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the sender was last updated (ISO 8601 format)
    """

    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(alias="deletedAt", description="Timestamp when the sender was deleted (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the sender was deleted (ISO 8601 format)
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="Identifier of the user who created the sender"),
    ] = None
    """
    Identifier of the user who created the sender
    """

    updated_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedBy"),
        pydantic.Field(alias="updatedBy", description="Identifier of the user who last updated the sender"),
    ] = None
    """
    Identifier of the user who last updated the sender
    """

    deleted_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deletedBy"),
        pydantic.Field(alias="deletedBy", description="Identifier of the user who deleted the sender"),
    ] = None
    """
    Identifier of the user who deleted the sender
    """

    full_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fullName"),
        pydantic.Field(alias="fullName", description="Full name of the business or individual"),
    ] = None
    """
    Full name of the business or individual
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name (for individual senders)"),
    ] = None
    """
    First name (for individual senders)
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name (for individual senders)"),
    ] = None
    """
    Last name (for individual senders)
    """

    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="birthDate"),
        pydantic.Field(
            alias="birthDate", description="Date of birth in ISO 8601 format (YYYY-MM-DD, for individual senders)"
        ),
    ] = None
    """
    Date of birth in ISO 8601 format (YYYY-MM-DD, for individual senders)
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the sender
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number in E.164 format
    """

    addresses: typing.Optional[typing.List[UpdateSendersResponseDataAddressesItem]] = pydantic.Field(default=None)
    """
    List of addresses associated with the sender
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Identifier of the associated merchant"),
    ] = None
    """
    Identifier of the associated merchant
    """

    kyb: typing.Optional[UpdateSendersResponseDataKyb] = pydantic.Field(default=None)
    """
    Know Your Business verification information
    """

    kyc: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Know Your Customer verification information
    """

    status: typing.Optional[UpdateSendersResponseDataStatus] = pydantic.Field(default=None)
    """
    Indicates whether the sender is currently active or inactive.
    """

    website_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="websiteUrl"),
        pydantic.Field(alias="websiteUrl", description="Business website URL"),
    ] = None
    """
    Business website URL
    """

    identification_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="identificationNumber"),
        pydantic.Field(alias="identificationNumber", description="Business identification number"),
    ] = None
    """
    Business identification number
    """

    onboarding_info: typing_extensions.Annotated[
        typing.Optional[SenderOnboardingInfo],
        FieldMetadata(alias="onboardingInfo"),
        pydantic.Field(alias="onboardingInfo"),
    ] = None
    documents: typing.Optional[typing.List[UpdateSendersResponseDataDocumentsItem]] = pydantic.Field(default=None)
    """
    List of KYB/KYC documents
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional metadata about the sender
    """

    risk_score: typing_extensions.Annotated[
        typing.Optional[UpdateSendersResponseDataRiskScore],
        FieldMetadata(alias="riskScore"),
        pydantic.Field(alias="riskScore", description="Risk assessment score"),
    ] = None
    """
    Risk assessment score
    """

    type: typing.Optional[UpdateSendersResponseDataType] = pydantic.Field(default=None)
    """
    Type of sender
    """

    identity: typing.Optional[UpdateSendersResponseDataIdentity] = pydantic.Field(default=None)
    """
    Identity verification information (for individual senders)
    """

    registration_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="registrationDate"),
        pydantic.Field(
            alias="registrationDate", description="Business registration date in ISO 8601 format (YYYY-MM-DD)"
        ),
    ] = None
    """
    Business registration date in ISO 8601 format (YYYY-MM-DD)
    """

    business_type: typing_extensions.Annotated[
        typing.Optional[UpdateSendersResponseDataBusinessType],
        FieldMetadata(alias="businessType"),
        pydantic.Field(alias="businessType", description="Type of business entity"),
    ] = None
    """
    Type of business entity
    """

    ubo: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Ultimate Beneficial Owner information
    """

    sender_associate: typing_extensions.Annotated[
        typing.Optional[typing.List[SenderAssociate]],
        FieldMetadata(alias="senderAssociate"),
        pydantic.Field(
            alias="senderAssociate", description="Directors and authorized representatives associated with the sender."
        ),
    ] = None
    """
    Directors and authorized representatives associated with the sender.
    """

    deposit_wallet_addresses: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="depositWalletAddresses"),
        pydantic.Field(alias="depositWalletAddresses", description="List of deposit wallet addresses"),
    ] = None
    """
    List of deposit wallet addresses
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name of an individual sender"),
    ] = None
    """
    Middle name of an individual sender
    """

    gender: typing.Optional[UpdateSendersResponseDataGender] = pydantic.Field(default=None)
    """
    Gender of an individual sender
    """

    occupation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Occupation of an individual sender
    """

    tos: typing.Optional[UpdateSendersResponseDataTos] = pydantic.Field(default=None)
    """
    Terms of Service status for the sender
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

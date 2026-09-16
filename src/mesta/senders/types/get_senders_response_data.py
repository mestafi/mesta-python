
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.sender_associate import SenderAssociate
from ...types.sender_onboarding_info import SenderOnboardingInfo
from .get_senders_response_data_addresses_item import GetSendersResponseDataAddressesItem
from .get_senders_response_data_business_type import GetSendersResponseDataBusinessType
from .get_senders_response_data_deposit_bank_accounts_item import GetSendersResponseDataDepositBankAccountsItem
from .get_senders_response_data_deposit_wallet_addresses_item import GetSendersResponseDataDepositWalletAddressesItem
from .get_senders_response_data_documents_item import GetSendersResponseDataDocumentsItem
from .get_senders_response_data_gender import GetSendersResponseDataGender
from .get_senders_response_data_identity import GetSendersResponseDataIdentity
from .get_senders_response_data_kyb import GetSendersResponseDataKyb
from .get_senders_response_data_kyc import GetSendersResponseDataKyc
from .get_senders_response_data_status import GetSendersResponseDataStatus
from .get_senders_response_data_tos import GetSendersResponseDataTos
from .get_senders_response_data_type import GetSendersResponseDataType
from .get_senders_response_data_ubo_item import GetSendersResponseDataUboItem


class GetSendersResponseData(UniversalBaseModel):
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

    addresses: typing.Optional[typing.List[GetSendersResponseDataAddressesItem]] = pydantic.Field(default=None)
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

    kyb: typing.Optional[GetSendersResponseDataKyb] = pydantic.Field(default=None)
    """
    Know Your Business verification information
    """

    kyc: typing.Optional[GetSendersResponseDataKyc] = pydantic.Field(default=None)
    """
    Know Your Customer verification information
    """

    status: typing.Optional[GetSendersResponseDataStatus] = pydantic.Field(default=None)
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
    documents: typing.Optional[typing.List[GetSendersResponseDataDocumentsItem]] = pydantic.Field(default=None)
    """
    List of KYB/KYC documents
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional metadata about the sender
    """

    type: typing.Optional[GetSendersResponseDataType] = pydantic.Field(default=None)
    """
    Type of sender
    """

    identity: typing.Optional[GetSendersResponseDataIdentity] = pydantic.Field(default=None)
    """
    Identity verification information (for individual senders)
    """

    registration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="registrationDate"),
        pydantic.Field(alias="registrationDate", description="Business registration date in ISO 8601 format"),
    ] = None
    """
    Business registration date in ISO 8601 format
    """

    business_type: typing_extensions.Annotated[
        typing.Optional[GetSendersResponseDataBusinessType],
        FieldMetadata(alias="businessType"),
        pydantic.Field(alias="businessType", description="Type of business entity"),
    ] = None
    """
    Type of business entity
    """

    ubo: typing.Optional[typing.List[GetSendersResponseDataUboItem]] = None
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
        typing.Optional[typing.List[GetSendersResponseDataDepositWalletAddressesItem]],
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

    gender: typing.Optional[GetSendersResponseDataGender] = pydantic.Field(default=None)
    """
    Gender of an individual sender
    """

    occupation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Occupation of an individual sender
    """

    tos: typing.Optional[GetSendersResponseDataTos] = pydantic.Field(default=None)
    """
    Terms of Service status for the sender
    """

    deposit_bank_accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[GetSendersResponseDataDepositBankAccountsItem]],
        FieldMetadata(alias="depositBankAccounts"),
        pydantic.Field(alias="depositBankAccounts", description="Fiat deposit bank accounts assigned to this sender"),
    ] = None
    """
    Fiat deposit bank accounts assigned to this sender
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

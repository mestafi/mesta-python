
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.payment_method import PaymentMethod
from .create_beneficiaries_response_data_address import CreateBeneficiariesResponseDataAddress
from .create_beneficiaries_response_data_business_type import CreateBeneficiariesResponseDataBusinessType
from .create_beneficiaries_response_data_identity import CreateBeneficiariesResponseDataIdentity
from .create_beneficiaries_response_data_status import CreateBeneficiariesResponseDataStatus
from .create_beneficiaries_response_data_type import CreateBeneficiariesResponseDataType
from .create_beneficiaries_response_data_verification import CreateBeneficiariesResponseDataVerification


class CreateBeneficiariesResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the beneficiary
    """

    type: typing.Optional[CreateBeneficiariesResponseDataType] = pydantic.Field(default=None)
    """
    Type of beneficiary
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name (for individual beneficiaries)"),
    ] = None
    """
    First name (for individual beneficiaries)
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name (for individual beneficiaries)"),
    ] = None
    """
    Middle name (for individual beneficiaries)
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name (for individual beneficiaries)"),
    ] = None
    """
    Last name (for individual beneficiaries)
    """

    full_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fullName"),
        pydantic.Field(alias="fullName", description="Full name of the business or individual"),
    ] = None
    """
    Full name of the business or individual
    """

    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="birthDate"),
        pydantic.Field(alias="birthDate", description="Date of birth (for individual beneficiaries)"),
    ] = None
    """
    Date of birth (for individual beneficiaries)
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number in E.164 format
    """

    address: typing.Optional[CreateBeneficiariesResponseDataAddress] = None
    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Associated merchant ID"),
    ] = None
    """
    Associated merchant ID
    """

    verification: typing.Optional[CreateBeneficiariesResponseDataVerification] = None
    status: typing.Optional[CreateBeneficiariesResponseDataStatus] = pydantic.Field(default=None)
    """
    Whether the beneficiary is active or inactive
    """

    identity: typing.Optional[CreateBeneficiariesResponseDataIdentity] = pydantic.Field(default=None)
    """
    Identity document information
    """

    business_type: typing_extensions.Annotated[
        typing.Optional[CreateBeneficiariesResponseDataBusinessType],
        FieldMetadata(alias="businessType"),
        pydantic.Field(alias="businessType", description="Type of business entity (for business beneficiaries)"),
    ] = None
    """
    Type of business entity (for business beneficiaries)
    """

    business_registration_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="businessRegistrationNumber"),
        pydantic.Field(
            alias="businessRegistrationNumber", description="Business registration number (for business beneficiaries)"
        ),
    ] = None
    """
    Business registration number (for business beneficiaries)
    """

    payment_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[PaymentMethod]],
        FieldMetadata(alias="paymentMethods"),
        pydantic.Field(alias="paymentMethods", description="Array of payment methods associated with the beneficiary"),
    ] = None
    """
    Array of payment methods associated with the beneficiary
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number for optimistic locking
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .business_beneficiary_address import BusinessBeneficiaryAddress
from .business_beneficiary_business_type import BusinessBeneficiaryBusinessType
from .business_beneficiary_identity import BusinessBeneficiaryIdentity
from .business_beneficiary_payment_info import BusinessBeneficiaryPaymentInfo
from .business_beneficiary_payment_type import BusinessBeneficiaryPaymentType
from .business_beneficiary_type import BusinessBeneficiaryType


class BusinessBeneficiary(UniversalBaseModel):
    type: BusinessBeneficiaryType = pydantic.Field()
    """
    The type for the beneficiary (business).
    """

    full_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fullName"),
        pydantic.Field(alias="fullName", description="Full name of the business beneficiary."),
    ]
    """
    Full name of the business beneficiary.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the beneficiary.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number of the beneficiary in international format (e.g., +11234567890).
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Merchant ID (optional, auto-assigned from API key)"),
    ] = None
    """
    Merchant ID (optional, auto-assigned from API key)
    """

    address: BusinessBeneficiaryAddress = pydantic.Field()
    """
    Postal address.
    """

    business_type: typing_extensions.Annotated[
        typing.Optional[BusinessBeneficiaryBusinessType],
        FieldMetadata(alias="businessType"),
        pydantic.Field(alias="businessType", description="Type of business entity."),
    ] = None
    """
    Type of business entity.
    """

    business_registration_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="businessRegistrationNumber"),
        pydantic.Field(alias="businessRegistrationNumber", description="Business registration number."),
    ] = None
    """
    Business registration number.
    """

    identity: typing.Optional[BusinessBeneficiaryIdentity] = None
    payment_type: typing_extensions.Annotated[
        BusinessBeneficiaryPaymentType,
        FieldMetadata(alias="paymentType"),
        pydantic.Field(alias="paymentType", description="Type of payment method for the beneficiary."),
    ]
    """
    Type of payment method for the beneficiary.
    """

    payment_info: typing_extensions.Annotated[
        BusinessBeneficiaryPaymentInfo,
        FieldMetadata(alias="paymentInfo"),
        pydantic.Field(
            alias="paymentInfo", description="Payment information for the beneficiary, varies based on payment type."
        ),
    ]
    """
    Payment information for the beneficiary, varies based on payment type.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional custom metadata.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

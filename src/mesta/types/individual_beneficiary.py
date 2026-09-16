
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .individual_beneficiary_address import IndividualBeneficiaryAddress
from .individual_beneficiary_identity import IndividualBeneficiaryIdentity
from .individual_beneficiary_payment_info import IndividualBeneficiaryPaymentInfo
from .individual_beneficiary_payment_type import IndividualBeneficiaryPaymentType
from .individual_beneficiary_type import IndividualBeneficiaryType


class IndividualBeneficiary(UniversalBaseModel):
    type: IndividualBeneficiaryType = pydantic.Field()
    """
    The type for the beneficiary (individual).
    """

    first_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the individual beneficiary."),
    ]
    """
    First name of the individual beneficiary.
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name of the individual beneficiary."),
    ] = None
    """
    Middle name of the individual beneficiary.
    """

    last_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the individual beneficiary."),
    ]
    """
    Last name of the individual beneficiary.
    """

    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="birthDate"),
        pydantic.Field(alias="birthDate", description="Birthdate of the Beneficiary in the format yyyy-mm-dd."),
    ] = None
    """
    Birthdate of the Beneficiary in the format yyyy-mm-dd.
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

    address: IndividualBeneficiaryAddress = pydantic.Field()
    """
    Postal address.
    """

    identity: typing.Optional[IndividualBeneficiaryIdentity] = None
    payment_type: typing_extensions.Annotated[
        IndividualBeneficiaryPaymentType,
        FieldMetadata(alias="paymentType"),
        pydantic.Field(alias="paymentType", description="Type of payment method for the beneficiary."),
    ]
    """
    Type of payment method for the beneficiary.
    """

    payment_info: typing_extensions.Annotated[
        IndividualBeneficiaryPaymentInfo,
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

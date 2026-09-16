
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .business_sender_business_type import BusinessSenderBusinessType
from .business_sender_type import BusinessSenderType


class BusinessSender(UniversalBaseModel):
    type: BusinessSenderType = pydantic.Field()
    """
    Type of the sender.
    """

    full_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="fullName"), pydantic.Field(alias="fullName", description="Legal business name.")
    ]
    """
    Legal business name.
    """

    email: str = pydantic.Field()
    """
    Email address of the sender.
    """

    phone: str = pydantic.Field()
    """
    A phone number in international format (e.g., +11234567890).
    """

    addresses: typing.List[Address] = pydantic.Field()
    """
    Array of addresses for the sender.
    """

    registration_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="registrationDate"),
        pydantic.Field(
            alias="registrationDate", description="Date when the business was registered (ISO 8601 format: YYYY-MM-DD)"
        ),
    ]
    """
    Date when the business was registered (ISO 8601 format: YYYY-MM-DD)
    """

    business_type: typing_extensions.Annotated[
        BusinessSenderBusinessType,
        FieldMetadata(alias="businessType"),
        pydantic.Field(alias="businessType", description="Type of business entity"),
    ]
    """
    Type of business entity
    """

    website_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="websiteUrl"),
        pydantic.Field(alias="websiteUrl", description="Website URL of the individual or business."),
    ] = None
    """
    Website URL of the individual or business.
    """

    identification_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="identificationNumber"),
        pydantic.Field(
            alias="identificationNumber",
            description="Business registration number issued by the sender's country of registration.",
        ),
    ] = None
    """
    Business registration number issued by the sender's country of registration.
    """

    tax_identification_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="taxIdentificationNumber"),
        pydantic.Field(
            alias="taxIdentificationNumber",
            description="Business tax identification number. This field is optional in the generic sender schema and becomes required when a selected capability requires it.",
        ),
    ] = None
    """
    Business tax identification number. This field is optional in the generic sender schema and becomes required when a selected capability requires it.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional custom metadata for the sender account.
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Merchant ID (optional, auto-assigned from API key)"),
    ] = None
    """
    Merchant ID (optional, auto-assigned from API key)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

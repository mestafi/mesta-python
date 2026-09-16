
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .individual_sender_gender import IndividualSenderGender
from .individual_sender_identity import IndividualSenderIdentity
from .individual_sender_occupation import IndividualSenderOccupation
from .individual_sender_type import IndividualSenderType


class IndividualSender(UniversalBaseModel):
    """
    Individual sender information. Note: Document requirements (documentFront, documentBack) vary by country. Please refer to the validation-rules endpoint with ownerType='individual' and the specific country to determine exact documentation requirements.
    """

    type: IndividualSenderType = pydantic.Field()
    """
    Type of the sender.
    """

    first_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the individual sender."),
    ]
    """
    First name of the individual sender.
    """

    last_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the individual sender."),
    ]
    """
    Last name of the individual sender.
    """

    birth_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="birthDate"),
        pydantic.Field(alias="birthDate", description="Birth date in ISO 8601 format (YYYY-MM-DD)."),
    ]
    """
    Birth date in ISO 8601 format (YYYY-MM-DD).
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

    identity: IndividualSenderIdentity
    website_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="websiteUrl"),
        pydantic.Field(alias="websiteUrl", description="Website URL of the individual or business."),
    ] = None
    """
    Website URL of the individual or business.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional custom metadata for the sender account.
    """

    gender: IndividualSenderGender = pydantic.Field()
    """
    Gender of the sender
    """

    occupation: IndividualSenderOccupation = pydantic.Field()
    """
    Occupation of the sender
    """

    middle_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="middleName"),
        pydantic.Field(alias="middleName", description="Middle name of the sender"),
    ] = None
    """
    Middle name of the sender
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

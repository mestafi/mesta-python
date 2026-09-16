
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_senders_response_data_ubo_item_address import GetSendersResponseDataUboItemAddress
from .get_senders_response_data_ubo_item_documents_item import GetSendersResponseDataUboItemDocumentsItem
from .get_senders_response_data_ubo_item_identity import GetSendersResponseDataUboItemIdentity
from .get_senders_response_data_ubo_item_kyc import GetSendersResponseDataUboItemKyc
from .get_senders_response_data_ubo_item_pep_questionnaire import GetSendersResponseDataUboItemPepQuestionnaire


class GetSendersResponseDataUboItem(UniversalBaseModel):
    """
    Ultimate Beneficial Owner information
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the UBO
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the UBO record
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the UBO was created (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the UBO was created (ISO 8601 format)
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the UBO was last updated (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the UBO was last updated (ISO 8601 format)
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the UBO"),
    ] = None
    """
    First name of the UBO
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the UBO"),
    ] = None
    """
    Last name of the UBO
    """

    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="birthDate"),
        pydantic.Field(alias="birthDate", description="Date of birth in ISO 8601 format (YYYY-MM-DD)"),
    ] = None
    """
    Date of birth in ISO 8601 format (YYYY-MM-DD)
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the UBO
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number in E.164 format
    """

    ownership_percent: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="ownershipPercent"),
        pydantic.Field(alias="ownershipPercent", description="Ownership percentage of the UBO in the company"),
    ] = None
    """
    Ownership percentage of the UBO in the company
    """

    address: typing.Optional[GetSendersResponseDataUboItemAddress] = pydantic.Field(default=None)
    """
    Address information of the UBO
    """

    identity: typing.Optional[GetSendersResponseDataUboItemIdentity] = pydantic.Field(default=None)
    """
    Identity verification information
    """

    sender_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="senderId"),
        pydantic.Field(alias="senderId", description="Identifier of the associated sender"),
    ] = None
    """
    Identifier of the associated sender
    """

    kyc: typing.Optional[GetSendersResponseDataUboItemKyc] = pydantic.Field(default=None)
    """
    Know Your Customer verification information
    """

    nationality: typing.Optional[str] = pydantic.Field(default=None)
    """
    UBO nationality as an ISO 3166-1 alpha-2 country code.
    """

    identification_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="identificationNumber"),
        pydantic.Field(alias="identificationNumber", description="Tax identification number for the UBO."),
    ] = None
    """
    Tax identification number for the UBO.
    """

    pep_declaration: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="pepDeclaration"),
        pydantic.Field(alias="pepDeclaration", description="Whether the UBO is politically exposed."),
    ] = None
    """
    Whether the UBO is politically exposed.
    """

    pep_questionnaire: typing_extensions.Annotated[
        typing.Optional[GetSendersResponseDataUboItemPepQuestionnaire],
        FieldMetadata(alias="pepQuestionnaire"),
        pydantic.Field(
            alias="pepQuestionnaire", description="PEP questionnaire details. Present when `pepDeclaration` is true."
        ),
    ] = None
    """
    PEP questionnaire details. Present when `pepDeclaration` is true.
    """

    documents: typing.Optional[typing.List[GetSendersResponseDataUboItemDocumentsItem]] = pydantic.Field(default=None)
    """
    Additional UBO documents stored for compliance review.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

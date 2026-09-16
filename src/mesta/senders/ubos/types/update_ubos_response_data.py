
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .update_ubos_response_data_address import UpdateUbosResponseDataAddress
from .update_ubos_response_data_documents_item import UpdateUbosResponseDataDocumentsItem
from .update_ubos_response_data_identity import UpdateUbosResponseDataIdentity
from .update_ubos_response_data_kyc import UpdateUbosResponseDataKyc
from .update_ubos_response_data_pep_questionnaire import UpdateUbosResponseDataPepQuestionnaire


class UpdateUbosResponseData(UniversalBaseModel):
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

    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(alias="deletedAt", description="Timestamp when the UBO was deleted (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the UBO was deleted (ISO 8601 format)
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="Identifier of the user who created the UBO"),
    ] = None
    """
    Identifier of the user who created the UBO
    """

    updated_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedBy"),
        pydantic.Field(alias="updatedBy", description="Identifier of the user who last updated the UBO"),
    ] = None
    """
    Identifier of the user who last updated the UBO
    """

    deleted_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deletedBy"),
        pydantic.Field(alias="deletedBy", description="Identifier of the user who deleted the UBO"),
    ] = None
    """
    Identifier of the user who deleted the UBO
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

    address: typing.Optional[UpdateUbosResponseDataAddress] = pydantic.Field(default=None)
    """
    Address information of the UBO
    """

    identity: typing.Optional[UpdateUbosResponseDataIdentity] = pydantic.Field(default=None)
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

    kyc: typing.Optional[UpdateUbosResponseDataKyc] = pydantic.Field(default=None)
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

    documents: typing.Optional[typing.List[UpdateUbosResponseDataDocumentsItem]] = pydantic.Field(default=None)
    """
    Additional UBO documents stored for compliance review.
    """

    pep_questionnaire: typing_extensions.Annotated[
        typing.Optional[UpdateUbosResponseDataPepQuestionnaire],
        FieldMetadata(alias="pepQuestionnaire"),
        pydantic.Field(
            alias="pepQuestionnaire",
            description="Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.",
        ),
    ] = None
    """
    Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

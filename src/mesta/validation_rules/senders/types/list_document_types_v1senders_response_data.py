
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_document_types_v1senders_response_data_owner import ListDocumentTypesV1SendersResponseDataOwner
from .list_document_types_v1senders_response_data_owner_type import ListDocumentTypesV1SendersResponseDataOwnerType
from .list_document_types_v1senders_response_data_rules import ListDocumentTypesV1SendersResponseDataRules


class ListDocumentTypesV1SendersResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the document rules
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the rules
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt",
            description="Timestamp when the rules were created (ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ)",
        ),
    ] = None
    """
    Timestamp when the rules were created (ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ)
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(
            alias="updatedAt",
            description="Timestamp when the rules were last updated (ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ)",
        ),
    ] = None
    """
    Timestamp when the rules were last updated (ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ)
    """

    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(
            alias="deletedAt",
            description="Timestamp when the rules were deleted, if applicable (ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ)",
        ),
    ] = None
    """
    Timestamp when the rules were deleted, if applicable (ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ)
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="Identifier of the user who created the rules"),
    ] = None
    """
    Identifier of the user who created the rules
    """

    updated_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedBy"),
        pydantic.Field(alias="updatedBy", description="Identifier of the user who last updated the rules"),
    ] = None
    """
    Identifier of the user who last updated the rules
    """

    deleted_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deletedBy"),
        pydantic.Field(alias="deletedBy", description="Identifier of the user who deleted the rules"),
    ] = None
    """
    Identifier of the user who deleted the rules
    """

    owner: typing.Optional[ListDocumentTypesV1SendersResponseDataOwner] = pydantic.Field(default=None)
    """
    Type of entity these rules apply to
    """

    owner_type: typing_extensions.Annotated[
        typing.Optional[ListDocumentTypesV1SendersResponseDataOwnerType],
        FieldMetadata(alias="ownerType"),
        pydantic.Field(alias="ownerType", description="Must be 'business' for document requirements"),
    ] = None
    """
    Must be 'business' for document requirements
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Two-letter country code (ISO 3166-1 alpha-2)
    """

    rules: typing.Optional[ListDocumentTypesV1SendersResponseDataRules] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_document_types_beneficiaries_response_data_owner import ListDocumentTypesBeneficiariesResponseDataOwner
from .list_document_types_beneficiaries_response_data_owner_type import (
    ListDocumentTypesBeneficiariesResponseDataOwnerType,
)
from .list_document_types_beneficiaries_response_data_rules import ListDocumentTypesBeneficiariesResponseDataRules


class ListDocumentTypesBeneficiariesResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the rule set
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the rules
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the rules were created"),
    ] = None
    """
    Timestamp when the rules were created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the rules were last updated"),
    ] = None
    """
    Timestamp when the rules were last updated
    """

    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(alias="deletedAt", description="Timestamp if rules are deleted, null otherwise"),
    ] = None
    """
    Timestamp if rules are deleted, null otherwise
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="ID of user who created the rules"),
    ] = None
    """
    ID of user who created the rules
    """

    updated_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedBy"),
        pydantic.Field(alias="updatedBy", description="ID of user who last updated the rules"),
    ] = None
    """
    ID of user who last updated the rules
    """

    deleted_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deletedBy"),
        pydantic.Field(alias="deletedBy", description="ID of user who deleted the rules"),
    ] = None
    """
    ID of user who deleted the rules
    """

    owner: typing.Optional[ListDocumentTypesBeneficiariesResponseDataOwner] = pydantic.Field(default=None)
    """
    Entity type these rules apply to
    """

    owner_type: typing_extensions.Annotated[
        typing.Optional[ListDocumentTypesBeneficiariesResponseDataOwnerType],
        FieldMetadata(alias="ownerType"),
        pydantic.Field(alias="ownerType", description="Type of owner these rules apply to"),
    ] = None
    """
    Type of owner these rules apply to
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country code these rules apply to
    """

    rules: typing.Optional[ListDocumentTypesBeneficiariesResponseDataRules] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_v2senders_response_data_rules_required_fields_item_nested_fields_item import (
    GetV2SendersResponseDataRulesRequiredFieldsItemNestedFieldsItem,
)


class GetV2SendersResponseDataRulesRequiredFieldsItem(UniversalBaseModel):
    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Field name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the field
    """

    nested_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[GetV2SendersResponseDataRulesRequiredFieldsItemNestedFieldsItem]],
        FieldMetadata(alias="nestedFields"),
        pydantic.Field(
            alias="nestedFields",
            description="Nested fields within this field. For identity fields, the documentType nested field includes supportedDocumentTypes.",
        ),
    ] = None
    """
    Nested fields within this field. For identity fields, the documentType nested field includes supportedDocumentTypes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

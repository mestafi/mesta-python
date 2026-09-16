
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_v2senders_response_data_rules_ubo_required_fields_item_nested_fields_item_supported_document_types_item_category import (
    GetV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItemCategory,
)


class GetV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItem(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    Document type identifier
    """

    category: GetV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItemCategory
    requires_front: typing_extensions.Annotated[
        bool, FieldMetadata(alias="requiresFront"), pydantic.Field(alias="requiresFront")
    ]
    requires_back: typing_extensions.Annotated[
        bool, FieldMetadata(alias="requiresBack"), pydantic.Field(alias="requiresBack")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

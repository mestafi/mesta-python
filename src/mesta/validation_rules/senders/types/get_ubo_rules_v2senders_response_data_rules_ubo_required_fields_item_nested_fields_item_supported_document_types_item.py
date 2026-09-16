
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_ubo_rules_v2senders_response_data_rules_ubo_required_fields_item_nested_fields_item_supported_document_types_item_category import (
    GetUboRulesV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItemCategory,
)


class GetUboRulesV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItem(
    UniversalBaseModel
):
    type: str = pydantic.Field()
    """
    Document type identifier
    """

    category: GetUboRulesV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItemCategory = pydantic.Field()
    """
    ID_DOCUMENT requires file uploads, ID_NUMBER requires only a document number
    """

    requires_front: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="requiresFront"),
        pydantic.Field(alias="requiresFront", description="Whether a front side document image is required"),
    ]
    """
    Whether a front side document image is required
    """

    requires_back: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="requiresBack"),
        pydantic.Field(alias="requiresBack", description="Whether a back side document image is required"),
    ]
    """
    Whether a back side document image is required
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

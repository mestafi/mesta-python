
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_ubo_rules_v2senders_response_data_rules_ubo_required_fields_item_nested_fields_item_supported_document_types_item import (
    GetUboRulesV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItem,
)


class GetUboRulesV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItem(UniversalBaseModel):
    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Nested field name (e.g., countryCode, documentType)
    """

    description: typing.Optional[str] = None
    supported_document_types: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                GetUboRulesV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItemSupportedDocumentTypesItem
            ]
        ],
        FieldMetadata(alias="supportedDocumentTypes"),
        pydantic.Field(
            alias="supportedDocumentTypes",
            description="Available identity document types for the requested country. Only present on the documentType nested field.",
        ),
    ] = None
    """
    Available identity document types for the requested country. Only present on the documentType nested field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

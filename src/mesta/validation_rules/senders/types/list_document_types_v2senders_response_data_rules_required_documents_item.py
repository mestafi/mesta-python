
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_document_types_v2senders_response_data_rules_required_documents_item_type import (
    ListDocumentTypesV2SendersResponseDataRulesRequiredDocumentsItemType,
)


class ListDocumentTypesV2SendersResponseDataRulesRequiredDocumentsItem(UniversalBaseModel):
    type: ListDocumentTypesV2SendersResponseDataRulesRequiredDocumentsItemType = pydantic.Field()
    """
    Type identifier for the required document
    """

    description: str = pydantic.Field()
    """
    Human-readable description of the required document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

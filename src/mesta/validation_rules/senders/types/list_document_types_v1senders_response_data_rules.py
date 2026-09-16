
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_document_types_v1senders_response_data_rules_required_documents_item import (
    ListDocumentTypesV1SendersResponseDataRulesRequiredDocumentsItem,
)


class ListDocumentTypesV1SendersResponseDataRules(UniversalBaseModel):
    required_documents: typing_extensions.Annotated[
        typing.Optional[typing.List[ListDocumentTypesV1SendersResponseDataRulesRequiredDocumentsItem]],
        FieldMetadata(alias="requiredDocuments"),
        pydantic.Field(alias="requiredDocuments", description="List of required documents for business verification"),
    ] = None
    """
    List of required documents for business verification
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

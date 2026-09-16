
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_document_types_beneficiaries_response_data_rules_required_documents_item import (
    ListDocumentTypesBeneficiariesResponseDataRulesRequiredDocumentsItem,
)


class ListDocumentTypesBeneficiariesResponseDataRules(UniversalBaseModel):
    required_documents: typing_extensions.Annotated[
        typing.Optional[typing.List[ListDocumentTypesBeneficiariesResponseDataRulesRequiredDocumentsItem]],
        FieldMetadata(alias="requiredDocuments"),
        pydantic.Field(
            alias="requiredDocuments", description="List of required documents (may be empty for some countries)"
        ),
    ] = None
    """
    List of required documents (may be empty for some countries)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

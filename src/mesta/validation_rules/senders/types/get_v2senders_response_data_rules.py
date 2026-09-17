
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_v2senders_response_data_rules_required_documents_item import (
    GetV2SendersResponseDataRulesRequiredDocumentsItem,
)
from .get_v2senders_response_data_rules_required_fields_item import GetV2SendersResponseDataRulesRequiredFieldsItem
from .get_v2senders_response_data_rules_ubo import GetV2SendersResponseDataRulesUbo


class GetV2SendersResponseDataRules(UniversalBaseModel):
    required_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[GetV2SendersResponseDataRulesRequiredFieldsItem]],
        FieldMetadata(alias="requiredFields"),
        pydantic.Field(
            alias="requiredFields",
            description="List of required fields for sender creation. Identity fields include supportedDocumentTypes.",
        ),
    ] = None
    """
    List of required fields for sender creation. Identity fields include supportedDocumentTypes.
    """

    required_documents: typing_extensions.Annotated[
        typing.Optional[typing.List[GetV2SendersResponseDataRulesRequiredDocumentsItem]],
        FieldMetadata(alias="requiredDocuments"),
        pydantic.Field(alias="requiredDocuments"),
    ] = None
    ubo: typing.Optional[GetV2SendersResponseDataRulesUbo] = pydantic.Field(default=None)
    """
    UBO validation rules (only present for business ownerType)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

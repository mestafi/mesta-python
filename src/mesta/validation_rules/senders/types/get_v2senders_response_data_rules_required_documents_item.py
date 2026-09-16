
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v2senders_response_data_rules_required_documents_item_type import (
    GetV2SendersResponseDataRulesRequiredDocumentsItemType,
)


class GetV2SendersResponseDataRulesRequiredDocumentsItem(UniversalBaseModel):
    type: typing.Optional[GetV2SendersResponseDataRulesRequiredDocumentsItemType] = pydantic.Field(default=None)
    """
    Type of required document
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the required document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

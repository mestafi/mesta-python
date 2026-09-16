
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_v2senders_response_data_rules_ubo_required_fields_item_nested_fields_item import (
    GetV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItem,
)


class GetV2SendersResponseDataRulesUboRequiredFieldsItem(UniversalBaseModel):
    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Field name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description
    """

    nested_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[GetV2SendersResponseDataRulesUboRequiredFieldsItemNestedFieldsItem]],
        FieldMetadata(alias="nestedFields"),
        pydantic.Field(alias="nestedFields"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

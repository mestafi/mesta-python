
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_states_validation_rules_response_data_states_item import ListStatesValidationRulesResponseDataStatesItem


class ListStatesValidationRulesResponseData(UniversalBaseModel):
    country: typing.Optional[str] = None
    states: typing.Optional[typing.List[ListStatesValidationRulesResponseDataStatesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

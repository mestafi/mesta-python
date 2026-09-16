
from __future__ import annotations

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .get_ubo_rules_v1senders_response_data_rules_ubo import GetUboRulesV1SendersResponseDataRulesUbo


class GetUboRulesV1SendersResponseDataRules(UniversalBaseModel):
    ubo: typing.Optional[GetUboRulesV1SendersResponseDataRulesUbo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetUboRulesV1SendersResponseDataRules)


import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_ubo_rules_v2senders_response_data import GetUboRulesV2SendersResponseData


class GetUboRulesV2SendersResponse(UniversalBaseModel):
    data: typing.Optional[GetUboRulesV2SendersResponseData] = None
    request_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

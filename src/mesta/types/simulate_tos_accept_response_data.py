
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .simulate_tos_accept_response_data_tos import SimulateTosAcceptResponseDataTos


class SimulateTosAcceptResponseData(UniversalBaseModel):
    sender_id: typing_extensions.Annotated[str, FieldMetadata(alias="senderId"), pydantic.Field(alias="senderId")]
    tos: SimulateTosAcceptResponseDataTos

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

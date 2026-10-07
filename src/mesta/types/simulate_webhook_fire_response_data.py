
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SimulateWebhookFireResponseData(UniversalBaseModel):
    event: str
    aggregate_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="aggregateId"), pydantic.Field(alias="aggregateId")
    ]
    published: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

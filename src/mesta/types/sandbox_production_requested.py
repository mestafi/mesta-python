
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_production_requested_status import SandboxProductionRequestedStatus


class SandboxProductionRequested(UniversalBaseModel):
    requested_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="requestedAt"), pydantic.Field(alias="requestedAt")
    ]
    status: SandboxProductionRequestedStatus = pydantic.Field()
    """
    The tracker's first state; the session read's `productionRequest` follows the request from here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

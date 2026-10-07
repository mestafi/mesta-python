
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_session_production_request_status import SandboxSessionProductionRequestStatus


class SandboxSessionProductionRequest(UniversalBaseModel):
    """
    The Go live request's tracker, null until the first request: `requested`, then `in_review` while Mesta reviews it, then `invited` with a production invite.
    """

    status: SandboxSessionProductionRequestStatus
    requested_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="requestedAt"), pydantic.Field(alias="requestedAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The last status change."),
    ]
    """
    The last status change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

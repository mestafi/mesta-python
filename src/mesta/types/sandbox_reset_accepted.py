
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_reset_accepted_status import SandboxResetAcceptedStatus


class SandboxResetAccepted(UniversalBaseModel):
    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    status: SandboxResetAcceptedStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

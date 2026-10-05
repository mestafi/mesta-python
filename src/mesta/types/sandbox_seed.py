
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_seed_current_step import SandboxSeedCurrentStep
from .sandbox_seed_error import SandboxSeedError
from .sandbox_seed_status import SandboxSeedStatus
from .sandbox_seed_step import SandboxSeedStep


class SandboxSeed(UniversalBaseModel):
    status: SandboxSeedStatus
    step: typing.Optional[SandboxSeedCurrentStep] = pydantic.Field(default=None)
    """
    The step running now.
    """

    steps: typing.List[SandboxSeedStep] = pydantic.Field()
    """
    One entry per step, in run order.
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None
    error: typing.Optional[SandboxSeedError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

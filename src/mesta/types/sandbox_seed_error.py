
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_seed_error_code import SandboxSeedErrorCode
from .sandbox_seed_error_step import SandboxSeedErrorStep


class SandboxSeedError(UniversalBaseModel):
    code: SandboxSeedErrorCode
    step: SandboxSeedErrorStep

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

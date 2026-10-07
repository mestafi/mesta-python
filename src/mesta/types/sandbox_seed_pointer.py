
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_seed_pointer_status import SandboxSeedPointerStatus


class SandboxSeedPointer(UniversalBaseModel):
    status: SandboxSeedPointerStatus
    url: str = pydantic.Field()
    """
    Poll `GET /v1/sandbox/sessions/{id}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

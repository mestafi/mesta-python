
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_seed_step_name import SandboxSeedStepName
from .sandbox_seed_step_status import SandboxSeedStepStatus


class SandboxSeedStep(UniversalBaseModel):
    name: SandboxSeedStepName
    status: SandboxSeedStepStatus = pydantic.Field()
    """
    skipped: the step does not apply in this sandbox, as the wallets step while test-network wallets are not offered. A skipped step is never retried and is not a failure.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

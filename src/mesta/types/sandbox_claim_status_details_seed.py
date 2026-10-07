
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_claim_status_details_seed_step import SandboxClaimStatusDetailsSeedStep


class SandboxClaimStatusDetailsSeed(UniversalBaseModel):
    step: typing.Optional[SandboxClaimStatusDetailsSeedStep] = pydantic.Field(default=None)
    """
    The step running now.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

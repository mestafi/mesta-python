
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_session_reset_error import SandboxSessionResetError
from .sandbox_session_reset_recovery_item import SandboxSessionResetRecoveryItem


class SandboxSessionReset(UniversalBaseModel):
    """
    Present only after a failed reset. The sandbox returns to its previous status with `seed.status` complete and `seed.error` set. Retry reset or delete the sandbox.
    """

    error: SandboxSessionResetError
    recovery: typing.List[SandboxSessionResetRecoveryItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .sandbox_created import SandboxCreated
from .sandbox_owner_created_session import SandboxOwnerCreatedSession
from .sandbox_owner_created_status import SandboxOwnerCreatedStatus


class SandboxOwnerCreated(SandboxCreated):
    status: SandboxOwnerCreatedStatus
    email_verified: typing_extensions.Annotated[
        bool, FieldMetadata(alias="emailVerified"), pydantic.Field(alias="emailVerified")
    ]
    session: SandboxOwnerCreatedSession

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

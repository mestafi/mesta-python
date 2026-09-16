
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .virtual_account_setup_response import VirtualAccountSetupResponse


class VirtualAccountSetupEnvelope(UniversalBaseModel):
    data: VirtualAccountSetupResponse
    request_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="requestId"),
        pydantic.Field(
            alias="requestId", description="Trace identifier for support and debugging. This is not a setup-request ID."
        ),
    ]
    """
    Trace identifier for support and debugging. This is not a setup-request ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

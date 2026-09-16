
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sender_virtual_account import SenderVirtualAccount


class SenderVirtualAccountsEnvelope(UniversalBaseModel):
    data: typing.List[SenderVirtualAccount] = pydantic.Field()
    """
    Virtual bank accounts available for the requested currency. The array currently contains at most one account.
    """

    request_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Trace identifier for support and debugging."),
    ]
    """
    Trace identifier for support and debugging.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

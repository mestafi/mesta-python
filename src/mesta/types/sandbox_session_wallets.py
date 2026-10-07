
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_session_wallets_reason import SandboxSessionWalletsReason
from .sandbox_session_wallets_senders import SandboxSessionWalletsSenders
from .sandbox_session_wallets_status import SandboxSessionWalletsStatus


class SandboxSessionWallets(UniversalBaseModel):
    """
    The merchant wallet's state. Test-network wallets are coming soon: until they are offered, `status` is `unavailable`, `reason` is `not_offered_on_plane` and `fixtures.wallets` is empty. Once they are offered, `status` is `ready` when the wallet's addresses exist, `pending` while a request is waiting and `failed` otherwise.
    """

    status: SandboxSessionWalletsStatus
    reason: typing.Optional[SandboxSessionWalletsReason] = pydantic.Field(default=None)
    """
    Present with `unavailable`: test-network wallets are not offered in the sandbox yet.
    """

    senders: SandboxSessionWalletsSenders = pydantic.Field()
    """
    Sender wallet usage and per-sender state, separate from the merchant wallet status. used counts senders for which a wallet provider client has been created.
    """

    requested_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="requestedAt"),
        pydantic.Field(alias="requestedAt", description="Set when a wallet request is waiting."),
    ] = None
    """
    Set when a wallet request is waiting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

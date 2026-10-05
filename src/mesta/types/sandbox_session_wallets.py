
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_session_wallets_senders import SandboxSessionWalletsSenders
from .sandbox_session_wallets_status import SandboxSessionWalletsStatus


class SandboxSessionWallets(UniversalBaseModel):
    """
    The merchant wallet's state: `ready` when the four test-network addresses exist, `pending` while the wallet was skipped for vendor capacity when the sample data was added, or a request is waiting, `failed` otherwise. The `wallets` entry of `seed.steps` carries the same state; `fixtures.wallets` is empty until the addresses exist.
    """

    status: SandboxSessionWalletsStatus
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


import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_session_wallets_senders_items_item import SandboxSessionWalletsSendersItemsItem


class SandboxSessionWalletsSenders(UniversalBaseModel):
    """
    Sender wallet usage and per-sender state, separate from the merchant wallet status. used counts senders for which a wallet provider client has been created.
    """

    used: int
    cap: int
    items: typing.List[SandboxSessionWalletsSendersItemsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

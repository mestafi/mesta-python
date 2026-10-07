
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_session_wallets_senders_items_item_status import SandboxSessionWalletsSendersItemsItemStatus


class SandboxSessionWalletsSendersItemsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Sender id.
    """

    status: SandboxSessionWalletsSendersItemsItemStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxClaimStatusDetailsCounts(UniversalBaseModel):
    """
    accounts: balance accounts per currency, excluding virtual accounts. All seven counts are integers.
    """

    accounts: int
    wallets: int
    webhooks: int
    senders: int
    beneficiaries: int
    orders: int
    deposits: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

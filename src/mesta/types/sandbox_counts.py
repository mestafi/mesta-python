
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxCounts(UniversalBaseModel):
    """
    Object counts: accounts are balance accounts per currency, not virtual accounts. Session counts are live; accounts, deposits and orders fall back to the counts of the sample data if a dependency is unavailable, without failing the status read.
    """

    accounts: int
    senders: int
    beneficiaries: int
    orders: int
    deposits: int
    wallets: int
    webhooks: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetBalancesMerchantsResponseDataItem(UniversalBaseModel):
    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency code (e.g., USD, EUR, GBP, USDC_ETH, USDT_TRX)
    """

    balance: typing.Optional[float] = pydantic.Field(default=None)
    """
    Current balance amount
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetBalancesSendersResponseDataItem(UniversalBaseModel):
    currency: str = pydantic.Field()
    """
    Currency code (e.g., USD, EUR, GBP)
    """

    balance: str = pydantic.Field()
    """
    Current balance as a decimal string
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SourceAddressInput(UniversalBaseModel):
    address: str = pydantic.Field()
    """
    The blockchain address to be added as a source
    """

    chain: str = pydantic.Field()
    """
    The blockchain network for the address (e.g., 'ethereum', 'polygon')
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxWallet(UniversalBaseModel):
    owner: str = pydantic.Field()
    """
    `merchant`, or a sender id.
    """

    chain: str
    address: str
    explorer: str
    funded: bool = pydantic.Field()
    """
    Whether test tokens from the network's faucet arrived.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

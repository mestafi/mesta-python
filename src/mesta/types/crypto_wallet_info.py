
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .crypto_wallet_info_chain import CryptoWalletInfoChain


class CryptoWalletInfo(UniversalBaseModel):
    address: str = pydantic.Field()
    """
    Cryptocurrency wallet address
    """

    chain: CryptoWalletInfoChain = pydantic.Field()
    """
    Blockchain network for the wallet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

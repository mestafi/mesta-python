
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class ListBalancesAccountsResponseDataItem(UniversalBaseModel):
    currency: str = pydantic.Field()
    """
    Currency code for the account
    """

    balance: str = pydantic.Field()
    """
    Current balance of the account as a decimal string
    """

    pooled_balance: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pooledBalance"),
        pydantic.Field(
            alias="pooledBalance",
            description='Optional. Your pooled merchant account balance for this currency, as a decimal string. Present only when the pooled balance is non-zero; the balance field keeps its existing sender-derived meaning. Total available = balance + pooledBalance. A currency funded only through the pooled account appears with balance "0" and pooledBalance set. Pooled Merchant Accounts is available to select merchants only — please reach out to Mesta support to have it enabled for your account.',
        ),
    ] = None
    """
    Optional. Your pooled merchant account balance for this currency, as a decimal string. Present only when the pooled balance is non-zero; the balance field keeps its existing sender-derived meaning. Total available = balance + pooledBalance. A currency funded only through the pooled account appears with balance "0" and pooledBalance set. Pooled Merchant Accounts is available to select merchants only — please reach out to Mesta support to have it enabled for your account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

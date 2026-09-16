
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_deposit_bank_account_orders_response_data_bank_details import (
    GetDepositBankAccountOrdersResponseDataBankDetails,
)
from .get_deposit_bank_account_orders_response_data_routing_details_item import (
    GetDepositBankAccountOrdersResponseDataRoutingDetailsItem,
)


class GetDepositBankAccountOrdersResponseData(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account holder name
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account holder address
    """

    account_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(alias="accountNumber", description="Bank account number"),
    ] = None
    """
    Bank account number
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reference to use for the deposit
    """

    bank_details: typing_extensions.Annotated[
        typing.Optional[GetDepositBankAccountOrdersResponseDataBankDetails],
        FieldMetadata(alias="bankDetails"),
        pydantic.Field(alias="bankDetails"),
    ] = None
    bic: typing.Optional[str] = pydantic.Field(default=None)
    """
    SWIFT/BIC code for the bank
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment provider name (e.g., 'openpayd', 'bcb')
    """

    provider_reference_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="providerReferenceId"),
        pydantic.Field(alias="providerReferenceId", description="Provider's reference identifier for this account"),
    ] = None
    """
    Provider's reference identifier for this account
    """

    sort_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sortCode"),
        pydantic.Field(alias="sortCode", description="Sort code for GBP bank accounts"),
    ] = None
    """
    Sort code for GBP bank accounts
    """

    routing_details: typing_extensions.Annotated[
        typing.Optional[typing.List[GetDepositBankAccountOrdersResponseDataRoutingDetailsItem]],
        FieldMetadata(alias="routingDetails"),
        pydantic.Field(
            alias="routingDetails", description="Routing details for the bank account. Present for USD wire transfers."
        ),
    ] = None
    """
    Routing details for the bank account. Present for USD wire transfers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

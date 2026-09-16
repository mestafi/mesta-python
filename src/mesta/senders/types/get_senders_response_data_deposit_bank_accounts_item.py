
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_senders_response_data_deposit_bank_accounts_item_bank_details import (
    GetSendersResponseDataDepositBankAccountsItemBankDetails,
)
from .get_senders_response_data_deposit_bank_accounts_item_routing_details_item import (
    GetSendersResponseDataDepositBankAccountsItemRoutingDetailsItem,
)


class GetSendersResponseDataDepositBankAccountsItem(UniversalBaseModel):
    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account holder address
    """

    account_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(alias="accountNumber", description="Bank account number or IBAN"),
    ] = None
    """
    Bank account number or IBAN
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency of the bank account (e.g. EUR, GBP)
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Banking provider
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account holder name
    """

    bic: typing.Optional[str] = pydantic.Field(default=None)
    """
    BIC/SWIFT code
    """

    bank_details: typing_extensions.Annotated[
        typing.Optional[GetSendersResponseDataDepositBankAccountsItemBankDetails],
        FieldMetadata(alias="bankDetails"),
        pydantic.Field(alias="bankDetails"),
    ] = None
    sort_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sortCode"),
        pydantic.Field(alias="sortCode", description="Sort code (for GBP accounts)"),
    ] = None
    """
    Sort code (for GBP accounts)
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment reference for the deposit
    """

    routing_details: typing_extensions.Annotated[
        typing.Optional[typing.List[GetSendersResponseDataDepositBankAccountsItemRoutingDetailsItem]],
        FieldMetadata(alias="routingDetails"),
        pydantic.Field(alias="routingDetails", description="Routing details for the bank account"),
    ] = None
    """
    Routing details for the bank account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

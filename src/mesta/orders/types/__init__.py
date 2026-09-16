
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cancel_orders_response import CancelOrdersResponse
    from .cancel_orders_response_data import CancelOrdersResponseData
    from .cancel_orders_response_data_status import CancelOrdersResponseDataStatus
    from .create_orders_response import CreateOrdersResponse
    from .create_orders_response_data import CreateOrdersResponseData
    from .get_deposit_bank_account_orders_response import GetDepositBankAccountOrdersResponse
    from .get_deposit_bank_account_orders_response_data import GetDepositBankAccountOrdersResponseData
    from .get_deposit_bank_account_orders_response_data_bank_details import (
        GetDepositBankAccountOrdersResponseDataBankDetails,
    )
    from .get_deposit_bank_account_orders_response_data_routing_details_item import (
        GetDepositBankAccountOrdersResponseDataRoutingDetailsItem,
    )
    from .get_deposit_wallet_address_orders_response import GetDepositWalletAddressOrdersResponse
    from .get_deposit_wallet_address_orders_response_data import GetDepositWalletAddressOrdersResponseData
    from .get_deposit_wallet_address_orders_response_data_chain import GetDepositWalletAddressOrdersResponseDataChain
    from .get_orders_response import GetOrdersResponse
    from .get_orders_response_data import GetOrdersResponseData
    from .get_orders_response_data_status import GetOrdersResponseDataStatus
    from .list_events_orders_response import ListEventsOrdersResponse
    from .list_events_orders_response_data_item import ListEventsOrdersResponseDataItem
    from .list_orders_request_sort_order import ListOrdersRequestSortOrder
    from .list_orders_request_status import ListOrdersRequestStatus
    from .list_orders_response import ListOrdersResponse
    from .list_orders_response_data_item import ListOrdersResponseDataItem
    from .list_orders_response_data_item_status import ListOrdersResponseDataItemStatus
_dynamic_imports: typing.Dict[str, str] = {
    "CancelOrdersResponse": ".cancel_orders_response",
    "CancelOrdersResponseData": ".cancel_orders_response_data",
    "CancelOrdersResponseDataStatus": ".cancel_orders_response_data_status",
    "CreateOrdersResponse": ".create_orders_response",
    "CreateOrdersResponseData": ".create_orders_response_data",
    "GetDepositBankAccountOrdersResponse": ".get_deposit_bank_account_orders_response",
    "GetDepositBankAccountOrdersResponseData": ".get_deposit_bank_account_orders_response_data",
    "GetDepositBankAccountOrdersResponseDataBankDetails": ".get_deposit_bank_account_orders_response_data_bank_details",
    "GetDepositBankAccountOrdersResponseDataRoutingDetailsItem": ".get_deposit_bank_account_orders_response_data_routing_details_item",
    "GetDepositWalletAddressOrdersResponse": ".get_deposit_wallet_address_orders_response",
    "GetDepositWalletAddressOrdersResponseData": ".get_deposit_wallet_address_orders_response_data",
    "GetDepositWalletAddressOrdersResponseDataChain": ".get_deposit_wallet_address_orders_response_data_chain",
    "GetOrdersResponse": ".get_orders_response",
    "GetOrdersResponseData": ".get_orders_response_data",
    "GetOrdersResponseDataStatus": ".get_orders_response_data_status",
    "ListEventsOrdersResponse": ".list_events_orders_response",
    "ListEventsOrdersResponseDataItem": ".list_events_orders_response_data_item",
    "ListOrdersRequestSortOrder": ".list_orders_request_sort_order",
    "ListOrdersRequestStatus": ".list_orders_request_status",
    "ListOrdersResponse": ".list_orders_response",
    "ListOrdersResponseDataItem": ".list_orders_response_data_item",
    "ListOrdersResponseDataItemStatus": ".list_orders_response_data_item_status",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CancelOrdersResponse",
    "CancelOrdersResponseData",
    "CancelOrdersResponseDataStatus",
    "CreateOrdersResponse",
    "CreateOrdersResponseData",
    "GetDepositBankAccountOrdersResponse",
    "GetDepositBankAccountOrdersResponseData",
    "GetDepositBankAccountOrdersResponseDataBankDetails",
    "GetDepositBankAccountOrdersResponseDataRoutingDetailsItem",
    "GetDepositWalletAddressOrdersResponse",
    "GetDepositWalletAddressOrdersResponseData",
    "GetDepositWalletAddressOrdersResponseDataChain",
    "GetOrdersResponse",
    "GetOrdersResponseData",
    "GetOrdersResponseDataStatus",
    "ListEventsOrdersResponse",
    "ListEventsOrdersResponseDataItem",
    "ListOrdersRequestSortOrder",
    "ListOrdersRequestStatus",
    "ListOrdersResponse",
    "ListOrdersResponseDataItem",
    "ListOrdersResponseDataItemStatus",
]

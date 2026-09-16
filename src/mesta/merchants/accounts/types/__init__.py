
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_accounts_request_sort_by import ListAccountsRequestSortBy
    from .list_accounts_request_sort_order import ListAccountsRequestSortOrder
    from .list_accounts_response import ListAccountsResponse
    from .list_accounts_response_data_item import ListAccountsResponseDataItem
    from .list_accounts_response_data_item_currency import ListAccountsResponseDataItemCurrency
    from .list_balances_accounts_response import ListBalancesAccountsResponse
    from .list_balances_accounts_response_data_item import ListBalancesAccountsResponseDataItem
    from .list_sender_balances_accounts_request_currency import ListSenderBalancesAccountsRequestCurrency
    from .list_sender_balances_accounts_response import ListSenderBalancesAccountsResponse
    from .list_sender_balances_accounts_response_data_item import ListSenderBalancesAccountsResponseDataItem
_dynamic_imports: typing.Dict[str, str] = {
    "ListAccountsRequestSortBy": ".list_accounts_request_sort_by",
    "ListAccountsRequestSortOrder": ".list_accounts_request_sort_order",
    "ListAccountsResponse": ".list_accounts_response",
    "ListAccountsResponseDataItem": ".list_accounts_response_data_item",
    "ListAccountsResponseDataItemCurrency": ".list_accounts_response_data_item_currency",
    "ListBalancesAccountsResponse": ".list_balances_accounts_response",
    "ListBalancesAccountsResponseDataItem": ".list_balances_accounts_response_data_item",
    "ListSenderBalancesAccountsRequestCurrency": ".list_sender_balances_accounts_request_currency",
    "ListSenderBalancesAccountsResponse": ".list_sender_balances_accounts_response",
    "ListSenderBalancesAccountsResponseDataItem": ".list_sender_balances_accounts_response_data_item",
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
    "ListAccountsRequestSortBy",
    "ListAccountsRequestSortOrder",
    "ListAccountsResponse",
    "ListAccountsResponseDataItem",
    "ListAccountsResponseDataItemCurrency",
    "ListBalancesAccountsResponse",
    "ListBalancesAccountsResponseDataItem",
    "ListSenderBalancesAccountsRequestCurrency",
    "ListSenderBalancesAccountsResponse",
    "ListSenderBalancesAccountsResponseDataItem",
]

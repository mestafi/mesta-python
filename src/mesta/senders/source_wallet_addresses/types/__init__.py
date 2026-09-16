
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_source_wallet_addresses_response import CreateSourceWalletAddressesResponse
    from .create_source_wallet_addresses_response_data_item import CreateSourceWalletAddressesResponseDataItem
    from .create_source_wallet_addresses_response_data_item_chain import (
        CreateSourceWalletAddressesResponseDataItemChain,
    )
    from .create_source_wallet_addresses_response_data_item_owner_type import (
        CreateSourceWalletAddressesResponseDataItemOwnerType,
    )
    from .create_source_wallet_addresses_response_data_item_risk_level import (
        CreateSourceWalletAddressesResponseDataItemRiskLevel,
    )
    from .list_source_wallet_addresses_request_sort_by import ListSourceWalletAddressesRequestSortBy
    from .list_source_wallet_addresses_request_sort_order import ListSourceWalletAddressesRequestSortOrder
    from .list_source_wallet_addresses_response import ListSourceWalletAddressesResponse
    from .list_source_wallet_addresses_response_data_item import ListSourceWalletAddressesResponseDataItem
    from .list_source_wallet_addresses_response_data_item_chain import ListSourceWalletAddressesResponseDataItemChain
    from .list_source_wallet_addresses_response_data_item_owner_type import (
        ListSourceWalletAddressesResponseDataItemOwnerType,
    )
    from .list_source_wallet_addresses_response_data_item_risk_level import (
        ListSourceWalletAddressesResponseDataItemRiskLevel,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSourceWalletAddressesResponse": ".create_source_wallet_addresses_response",
    "CreateSourceWalletAddressesResponseDataItem": ".create_source_wallet_addresses_response_data_item",
    "CreateSourceWalletAddressesResponseDataItemChain": ".create_source_wallet_addresses_response_data_item_chain",
    "CreateSourceWalletAddressesResponseDataItemOwnerType": ".create_source_wallet_addresses_response_data_item_owner_type",
    "CreateSourceWalletAddressesResponseDataItemRiskLevel": ".create_source_wallet_addresses_response_data_item_risk_level",
    "ListSourceWalletAddressesRequestSortBy": ".list_source_wallet_addresses_request_sort_by",
    "ListSourceWalletAddressesRequestSortOrder": ".list_source_wallet_addresses_request_sort_order",
    "ListSourceWalletAddressesResponse": ".list_source_wallet_addresses_response",
    "ListSourceWalletAddressesResponseDataItem": ".list_source_wallet_addresses_response_data_item",
    "ListSourceWalletAddressesResponseDataItemChain": ".list_source_wallet_addresses_response_data_item_chain",
    "ListSourceWalletAddressesResponseDataItemOwnerType": ".list_source_wallet_addresses_response_data_item_owner_type",
    "ListSourceWalletAddressesResponseDataItemRiskLevel": ".list_source_wallet_addresses_response_data_item_risk_level",
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
    "CreateSourceWalletAddressesResponse",
    "CreateSourceWalletAddressesResponseDataItem",
    "CreateSourceWalletAddressesResponseDataItemChain",
    "CreateSourceWalletAddressesResponseDataItemOwnerType",
    "CreateSourceWalletAddressesResponseDataItemRiskLevel",
    "ListSourceWalletAddressesRequestSortBy",
    "ListSourceWalletAddressesRequestSortOrder",
    "ListSourceWalletAddressesResponse",
    "ListSourceWalletAddressesResponseDataItem",
    "ListSourceWalletAddressesResponseDataItemChain",
    "ListSourceWalletAddressesResponseDataItemOwnerType",
    "ListSourceWalletAddressesResponseDataItemRiskLevel",
]

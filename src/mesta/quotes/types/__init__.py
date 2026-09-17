
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_quotes_request_source_currency import CreateQuotesRequestSourceCurrency
    from .create_quotes_request_transfer_type import CreateQuotesRequestTransferType
    from .create_quotes_response import CreateQuotesResponse
    from .create_quotes_response_data import CreateQuotesResponseData
    from .create_quotes_response_data_status import CreateQuotesResponseDataStatus
    from .create_quotes_response_data_transfer_type import CreateQuotesResponseDataTransferType
    from .get_quotes_response import GetQuotesResponse
    from .get_quotes_response_data import GetQuotesResponseData
    from .get_quotes_response_data_status import GetQuotesResponseDataStatus
    from .get_quotes_response_data_transfer_type import GetQuotesResponseDataTransferType
    from .list_quotes_request_sort_by import ListQuotesRequestSortBy
    from .list_quotes_request_sort_order import ListQuotesRequestSortOrder
    from .list_quotes_response import ListQuotesResponse
    from .list_quotes_response_data_item import ListQuotesResponseDataItem
    from .list_quotes_response_data_item_status import ListQuotesResponseDataItemStatus
    from .list_quotes_response_data_item_transfer_type import ListQuotesResponseDataItemTransferType
_dynamic_imports: typing.Dict[str, str] = {
    "CreateQuotesRequestSourceCurrency": ".create_quotes_request_source_currency",
    "CreateQuotesRequestTransferType": ".create_quotes_request_transfer_type",
    "CreateQuotesResponse": ".create_quotes_response",
    "CreateQuotesResponseData": ".create_quotes_response_data",
    "CreateQuotesResponseDataStatus": ".create_quotes_response_data_status",
    "CreateQuotesResponseDataTransferType": ".create_quotes_response_data_transfer_type",
    "GetQuotesResponse": ".get_quotes_response",
    "GetQuotesResponseData": ".get_quotes_response_data",
    "GetQuotesResponseDataStatus": ".get_quotes_response_data_status",
    "GetQuotesResponseDataTransferType": ".get_quotes_response_data_transfer_type",
    "ListQuotesRequestSortBy": ".list_quotes_request_sort_by",
    "ListQuotesRequestSortOrder": ".list_quotes_request_sort_order",
    "ListQuotesResponse": ".list_quotes_response",
    "ListQuotesResponseDataItem": ".list_quotes_response_data_item",
    "ListQuotesResponseDataItemStatus": ".list_quotes_response_data_item_status",
    "ListQuotesResponseDataItemTransferType": ".list_quotes_response_data_item_transfer_type",
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
    "CreateQuotesRequestSourceCurrency",
    "CreateQuotesRequestTransferType",
    "CreateQuotesResponse",
    "CreateQuotesResponseData",
    "CreateQuotesResponseDataStatus",
    "CreateQuotesResponseDataTransferType",
    "GetQuotesResponse",
    "GetQuotesResponseData",
    "GetQuotesResponseDataStatus",
    "GetQuotesResponseDataTransferType",
    "ListQuotesRequestSortBy",
    "ListQuotesRequestSortOrder",
    "ListQuotesResponse",
    "ListQuotesResponseDataItem",
    "ListQuotesResponseDataItemStatus",
    "ListQuotesResponseDataItemTransferType",
]

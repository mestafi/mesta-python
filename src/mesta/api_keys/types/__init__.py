
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_api_keys_response import CreateApiKeysResponse
    from .create_api_keys_response_data import CreateApiKeysResponseData
    from .create_api_keys_response_data_kind import CreateApiKeysResponseDataKind
    from .get_api_keys_response import GetApiKeysResponse
    from .get_api_keys_response_data import GetApiKeysResponseData
    from .get_api_keys_response_data_kind import GetApiKeysResponseDataKind
    from .list_api_keys_request_sort_by import ListApiKeysRequestSortBy
    from .list_api_keys_request_sort_order import ListApiKeysRequestSortOrder
    from .list_api_keys_response import ListApiKeysResponse
    from .list_api_keys_response_data_item import ListApiKeysResponseDataItem
    from .list_api_keys_response_data_item_kind import ListApiKeysResponseDataItemKind
    from .list_api_keys_response_meta import ListApiKeysResponseMeta
    from .update_api_keys_response import UpdateApiKeysResponse
    from .update_api_keys_response_data import UpdateApiKeysResponseData
    from .update_api_keys_response_data_kind import UpdateApiKeysResponseDataKind
_dynamic_imports: typing.Dict[str, str] = {
    "CreateApiKeysResponse": ".create_api_keys_response",
    "CreateApiKeysResponseData": ".create_api_keys_response_data",
    "CreateApiKeysResponseDataKind": ".create_api_keys_response_data_kind",
    "GetApiKeysResponse": ".get_api_keys_response",
    "GetApiKeysResponseData": ".get_api_keys_response_data",
    "GetApiKeysResponseDataKind": ".get_api_keys_response_data_kind",
    "ListApiKeysRequestSortBy": ".list_api_keys_request_sort_by",
    "ListApiKeysRequestSortOrder": ".list_api_keys_request_sort_order",
    "ListApiKeysResponse": ".list_api_keys_response",
    "ListApiKeysResponseDataItem": ".list_api_keys_response_data_item",
    "ListApiKeysResponseDataItemKind": ".list_api_keys_response_data_item_kind",
    "ListApiKeysResponseMeta": ".list_api_keys_response_meta",
    "UpdateApiKeysResponse": ".update_api_keys_response",
    "UpdateApiKeysResponseData": ".update_api_keys_response_data",
    "UpdateApiKeysResponseDataKind": ".update_api_keys_response_data_kind",
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
    "CreateApiKeysResponse",
    "CreateApiKeysResponseData",
    "CreateApiKeysResponseDataKind",
    "GetApiKeysResponse",
    "GetApiKeysResponseData",
    "GetApiKeysResponseDataKind",
    "ListApiKeysRequestSortBy",
    "ListApiKeysRequestSortOrder",
    "ListApiKeysResponse",
    "ListApiKeysResponseDataItem",
    "ListApiKeysResponseDataItemKind",
    "ListApiKeysResponseMeta",
    "UpdateApiKeysResponse",
    "UpdateApiKeysResponseData",
    "UpdateApiKeysResponseDataKind",
]

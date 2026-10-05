
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateApiKeysResponse,
        CreateApiKeysResponseData,
        CreateApiKeysResponseDataKind,
        GetApiKeysResponse,
        GetApiKeysResponseData,
        GetApiKeysResponseDataKind,
        ListApiKeysRequestSortBy,
        ListApiKeysRequestSortOrder,
        ListApiKeysResponse,
        ListApiKeysResponseDataItem,
        ListApiKeysResponseDataItemKind,
        ListApiKeysResponseMeta,
        UpdateApiKeysResponse,
        UpdateApiKeysResponseData,
        UpdateApiKeysResponseDataKind,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateApiKeysResponse": ".types",
    "CreateApiKeysResponseData": ".types",
    "CreateApiKeysResponseDataKind": ".types",
    "GetApiKeysResponse": ".types",
    "GetApiKeysResponseData": ".types",
    "GetApiKeysResponseDataKind": ".types",
    "ListApiKeysRequestSortBy": ".types",
    "ListApiKeysRequestSortOrder": ".types",
    "ListApiKeysResponse": ".types",
    "ListApiKeysResponseDataItem": ".types",
    "ListApiKeysResponseDataItemKind": ".types",
    "ListApiKeysResponseMeta": ".types",
    "UpdateApiKeysResponse": ".types",
    "UpdateApiKeysResponseData": ".types",
    "UpdateApiKeysResponseDataKind": ".types",
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

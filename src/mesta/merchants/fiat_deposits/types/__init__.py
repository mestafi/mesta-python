
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_fiat_deposits_response import GetFiatDepositsResponse
    from .list_fiat_deposits_request_currency import ListFiatDepositsRequestCurrency
    from .list_fiat_deposits_request_sort_by import ListFiatDepositsRequestSortBy
    from .list_fiat_deposits_request_sort_order import ListFiatDepositsRequestSortOrder
    from .list_fiat_deposits_response import ListFiatDepositsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetFiatDepositsResponse": ".get_fiat_deposits_response",
    "ListFiatDepositsRequestCurrency": ".list_fiat_deposits_request_currency",
    "ListFiatDepositsRequestSortBy": ".list_fiat_deposits_request_sort_by",
    "ListFiatDepositsRequestSortOrder": ".list_fiat_deposits_request_sort_order",
    "ListFiatDepositsResponse": ".list_fiat_deposits_response",
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
    "GetFiatDepositsResponse",
    "ListFiatDepositsRequestCurrency",
    "ListFiatDepositsRequestSortBy",
    "ListFiatDepositsRequestSortOrder",
    "ListFiatDepositsResponse",
]

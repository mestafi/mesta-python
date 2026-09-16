
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accept_terms_merchants_response import AcceptTermsMerchantsResponse
    from .accept_terms_merchants_response_data import AcceptTermsMerchantsResponseData
    from .get_balances_merchants_response import GetBalancesMerchantsResponse
    from .get_balances_merchants_response_data_item import GetBalancesMerchantsResponseDataItem
    from .get_merchants_response import GetMerchantsResponse
    from .get_merchants_response_data import GetMerchantsResponseData
    from .get_merchants_response_data_address import GetMerchantsResponseDataAddress
    from .get_merchants_response_data_kyb import GetMerchantsResponseDataKyb
    from .get_merchants_response_data_kyb_status import GetMerchantsResponseDataKybStatus
    from .get_merchants_response_data_status import GetMerchantsResponseDataStatus
    from .get_merchants_response_data_ubo import GetMerchantsResponseDataUbo
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptTermsMerchantsResponse": ".accept_terms_merchants_response",
    "AcceptTermsMerchantsResponseData": ".accept_terms_merchants_response_data",
    "GetBalancesMerchantsResponse": ".get_balances_merchants_response",
    "GetBalancesMerchantsResponseDataItem": ".get_balances_merchants_response_data_item",
    "GetMerchantsResponse": ".get_merchants_response",
    "GetMerchantsResponseData": ".get_merchants_response_data",
    "GetMerchantsResponseDataAddress": ".get_merchants_response_data_address",
    "GetMerchantsResponseDataKyb": ".get_merchants_response_data_kyb",
    "GetMerchantsResponseDataKybStatus": ".get_merchants_response_data_kyb_status",
    "GetMerchantsResponseDataStatus": ".get_merchants_response_data_status",
    "GetMerchantsResponseDataUbo": ".get_merchants_response_data_ubo",
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
    "AcceptTermsMerchantsResponse",
    "AcceptTermsMerchantsResponseData",
    "GetBalancesMerchantsResponse",
    "GetBalancesMerchantsResponseDataItem",
    "GetMerchantsResponse",
    "GetMerchantsResponseData",
    "GetMerchantsResponseDataAddress",
    "GetMerchantsResponseDataKyb",
    "GetMerchantsResponseDataKybStatus",
    "GetMerchantsResponseDataStatus",
    "GetMerchantsResponseDataUbo",
]

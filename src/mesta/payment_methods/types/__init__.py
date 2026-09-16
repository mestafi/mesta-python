
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .consent_decision_request_status import ConsentDecisionRequestStatus
    from .create_payment_method_request_data import CreatePaymentMethodRequestData
    from .create_payment_methods_response import CreatePaymentMethodsResponse
    from .decide_consent_payment_methods_response import DecideConsentPaymentMethodsResponse
    from .delete_payment_methods_response import DeletePaymentMethodsResponse
    from .get_payment_methods_response import GetPaymentMethodsResponse
    from .list_payment_methods_request_sort_by import ListPaymentMethodsRequestSortBy
    from .list_payment_methods_request_sort_order import ListPaymentMethodsRequestSortOrder
    from .list_payment_methods_response import ListPaymentMethodsResponse
    from .update_payment_method_request_data import UpdatePaymentMethodRequestData
    from .update_payment_methods_response import UpdatePaymentMethodsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ConsentDecisionRequestStatus": ".consent_decision_request_status",
    "CreatePaymentMethodRequestData": ".create_payment_method_request_data",
    "CreatePaymentMethodsResponse": ".create_payment_methods_response",
    "DecideConsentPaymentMethodsResponse": ".decide_consent_payment_methods_response",
    "DeletePaymentMethodsResponse": ".delete_payment_methods_response",
    "GetPaymentMethodsResponse": ".get_payment_methods_response",
    "ListPaymentMethodsRequestSortBy": ".list_payment_methods_request_sort_by",
    "ListPaymentMethodsRequestSortOrder": ".list_payment_methods_request_sort_order",
    "ListPaymentMethodsResponse": ".list_payment_methods_response",
    "UpdatePaymentMethodRequestData": ".update_payment_method_request_data",
    "UpdatePaymentMethodsResponse": ".update_payment_methods_response",
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
    "ConsentDecisionRequestStatus",
    "CreatePaymentMethodRequestData",
    "CreatePaymentMethodsResponse",
    "DecideConsentPaymentMethodsResponse",
    "DeletePaymentMethodsResponse",
    "GetPaymentMethodsResponse",
    "ListPaymentMethodsRequestSortBy",
    "ListPaymentMethodsRequestSortOrder",
    "ListPaymentMethodsResponse",
    "UpdatePaymentMethodRequestData",
    "UpdatePaymentMethodsResponse",
]

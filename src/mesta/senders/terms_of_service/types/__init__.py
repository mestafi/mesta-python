
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_acceptance_terms_of_service_response import GetAcceptanceTermsOfServiceResponse
    from .get_acceptance_terms_of_service_response_data import GetAcceptanceTermsOfServiceResponseData
    from .get_status_terms_of_service_response import GetStatusTermsOfServiceResponse
    from .get_status_terms_of_service_response_data import GetStatusTermsOfServiceResponseData
    from .get_status_terms_of_service_response_data_status import GetStatusTermsOfServiceResponseDataStatus
_dynamic_imports: typing.Dict[str, str] = {
    "GetAcceptanceTermsOfServiceResponse": ".get_acceptance_terms_of_service_response",
    "GetAcceptanceTermsOfServiceResponseData": ".get_acceptance_terms_of_service_response_data",
    "GetStatusTermsOfServiceResponse": ".get_status_terms_of_service_response",
    "GetStatusTermsOfServiceResponseData": ".get_status_terms_of_service_response_data",
    "GetStatusTermsOfServiceResponseDataStatus": ".get_status_terms_of_service_response_data_status",
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
    "GetAcceptanceTermsOfServiceResponse",
    "GetAcceptanceTermsOfServiceResponseData",
    "GetStatusTermsOfServiceResponse",
    "GetStatusTermsOfServiceResponseData",
    "GetStatusTermsOfServiceResponseDataStatus",
]


# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .authorize_auth_request_permission_check_type import AuthorizeAuthRequestPermissionCheckType
    from .authorize_auth_response import AuthorizeAuthResponse
    from .authorize_auth_response_data import AuthorizeAuthResponseData
    from .merchant_login_auth_response import MerchantLoginAuthResponse
    from .merchant_login_auth_response_data import MerchantLoginAuthResponseData
    from .merchant_login_auth_response_data_user import MerchantLoginAuthResponseDataUser
    from .merchant_login_auth_response_data_user_scope import MerchantLoginAuthResponseDataUserScope
_dynamic_imports: typing.Dict[str, str] = {
    "AuthorizeAuthRequestPermissionCheckType": ".authorize_auth_request_permission_check_type",
    "AuthorizeAuthResponse": ".authorize_auth_response",
    "AuthorizeAuthResponseData": ".authorize_auth_response_data",
    "MerchantLoginAuthResponse": ".merchant_login_auth_response",
    "MerchantLoginAuthResponseData": ".merchant_login_auth_response_data",
    "MerchantLoginAuthResponseDataUser": ".merchant_login_auth_response_data_user",
    "MerchantLoginAuthResponseDataUserScope": ".merchant_login_auth_response_data_user_scope",
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
    "AuthorizeAuthRequestPermissionCheckType",
    "AuthorizeAuthResponse",
    "AuthorizeAuthResponseData",
    "MerchantLoginAuthResponse",
    "MerchantLoginAuthResponseData",
    "MerchantLoginAuthResponseDataUser",
    "MerchantLoginAuthResponseDataUserScope",
]

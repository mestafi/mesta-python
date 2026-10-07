
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_sender_wallets_sandbox_response import CreateSenderWalletsSandboxResponse
    from .create_wallets_sandbox_response import CreateWalletsSandboxResponse
    from .get_sandbox_response import GetSandboxResponse
    from .reset_sandbox_response import ResetSandboxResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSenderWalletsSandboxResponse": ".create_sender_wallets_sandbox_response",
    "CreateWalletsSandboxResponse": ".create_wallets_sandbox_response",
    "GetSandboxResponse": ".get_sandbox_response",
    "ResetSandboxResponse": ".reset_sandbox_response",
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
    "CreateSenderWalletsSandboxResponse",
    "CreateWalletsSandboxResponse",
    "GetSandboxResponse",
    "ResetSandboxResponse",
]

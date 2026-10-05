
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_sandbox_response import CreateSandboxResponse
    from .create_sandbox_session_request_deposit_source import CreateSandboxSessionRequestDepositSource
    from .create_sender_wallets_sandbox_response import CreateSenderWalletsSandboxResponse
    from .create_wallets_sandbox_response import CreateWalletsSandboxResponse
    from .get_challenge_sandbox_response import GetChallengeSandboxResponse
    from .get_sandbox_response import GetSandboxResponse
    from .request_production_sandbox_response import RequestProductionSandboxResponse
    from .resend_code_sandbox_response import ResendCodeSandboxResponse
    from .reset_sandbox_response import ResetSandboxResponse
    from .sandbox_signup_request_from import SandboxSignupRequestFrom
    from .sign_up_sandbox_response import SignUpSandboxResponse
    from .verify_email_sandbox_response import VerifyEmailSandboxResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSandboxResponse": ".create_sandbox_response",
    "CreateSandboxSessionRequestDepositSource": ".create_sandbox_session_request_deposit_source",
    "CreateSenderWalletsSandboxResponse": ".create_sender_wallets_sandbox_response",
    "CreateWalletsSandboxResponse": ".create_wallets_sandbox_response",
    "GetChallengeSandboxResponse": ".get_challenge_sandbox_response",
    "GetSandboxResponse": ".get_sandbox_response",
    "RequestProductionSandboxResponse": ".request_production_sandbox_response",
    "ResendCodeSandboxResponse": ".resend_code_sandbox_response",
    "ResetSandboxResponse": ".reset_sandbox_response",
    "SandboxSignupRequestFrom": ".sandbox_signup_request_from",
    "SignUpSandboxResponse": ".sign_up_sandbox_response",
    "VerifyEmailSandboxResponse": ".verify_email_sandbox_response",
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
    "CreateSandboxResponse",
    "CreateSandboxSessionRequestDepositSource",
    "CreateSenderWalletsSandboxResponse",
    "CreateWalletsSandboxResponse",
    "GetChallengeSandboxResponse",
    "GetSandboxResponse",
    "RequestProductionSandboxResponse",
    "ResendCodeSandboxResponse",
    "ResetSandboxResponse",
    "SandboxSignupRequestFrom",
    "SignUpSandboxResponse",
    "VerifyEmailSandboxResponse",
]

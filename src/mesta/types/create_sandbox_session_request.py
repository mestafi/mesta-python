
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_sandbox_session_request_deposit_source import CreateSandboxSessionRequestDepositSource
from .sandbox_challenge_solution import SandboxChallengeSolution


class CreateSandboxSessionRequest(UniversalBaseModel):
    challenge: SandboxChallengeSolution
    accept_terms: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="acceptTerms"),
        pydantic.Field(
            alias="acceptTerms",
            description="Must be true: your acceptance of the Sandbox terms (https://ohana.sandbox.mesta.xyz/terms?version=sandbox-2026-10); the Sandbox privacy notice (https://docs.mesta.xyz/docs/sandbox-privacy) explains how Mesta uses your details. An agent may not set it without the person's instruction. Missing or false answers 422 with the terms URL and version in the body.",
        ),
    ]
    """
    Must be true: your acceptance of the Sandbox terms (https://ohana.sandbox.mesta.xyz/terms?version=sandbox-2026-10); the Sandbox privacy notice (https://docs.mesta.xyz/docs/sandbox-privacy) explains how Mesta uses your details. An agent may not set it without the person's instruction. Missing or false answers 422 with the terms URL and version in the body.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points. Defaults to `Sandbox {shortId}`.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 3166-1 alpha-2 code from the sandbox's merchant country list. Default US.
    """

    deposit_source: typing_extensions.Annotated[
        typing.Optional[CreateSandboxSessionRequestDepositSource],
        FieldMetadata(alias="depositSource"),
        pydantic.Field(
            alias="depositSource",
            description="`sender` is the only value accepted at launch; `merchant` answers 409 NOT_AVAILABLE_IN_SANDBOX, superseding the earlier 422 (merchant-funded sandboxes arrive in a later release).",
        ),
    ] = None
    """
    `sender` is the only value accepted at launch; `merchant` answers 409 NOT_AVAILABLE_IN_SANDBOX, superseding the earlier 422 (merchant-funded sandboxes arrive in a later release).
    """

    claim_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="claimEmail"),
        pydantic.Field(
            alias="claimEmail",
            description="Optional. The email address to send the claim link to, in a \"Claim your Mesta sandbox\" mail; the 201 then carries `claim.sentTo`, the masked address, instead of `claimUrl`. The address passes the same checks as the sign-up's email and is refused with the same codes: 400 VALIDATION_FAILED when it cannot receive mail, 429 SANDBOX_CAP_EXCEEDED for the per-email and per-domain caps, and 409 EMAIL_ALREADY_OWNS_SANDBOX when it already owns a live sandbox. An agent creating a sandbox for a person always passes the person's address, so it never holds the claim link.",
        ),
    ] = None
    """
    Optional. The email address to send the claim link to, in a "Claim your Mesta sandbox" mail; the 201 then carries `claim.sentTo`, the masked address, instead of `claimUrl`. The address passes the same checks as the sign-up's email and is refused with the same codes: 400 VALIDATION_FAILED when it cannot receive mail, 429 SANDBOX_CAP_EXCEEDED for the per-email and per-domain caps, and 409 EMAIL_ALREADY_OWNS_SANDBOX when it already owns a live sandbox. An agent creating a sandbox for a person always passes the person's address, so it never holds the claim link.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

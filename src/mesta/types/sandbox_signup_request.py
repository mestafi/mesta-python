
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_signup_request_from import SandboxSignupRequestFrom


class SandboxSignupRequest(UniversalBaseModel):
    """
    Posted by the sandbox portal's sign-up form. Scripts use POST /v1/sandbox/sessions instead.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[SandboxSignupRequestFrom],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Optional sign-up entry point."),
    ] = None
    """
    Optional sign-up entry point.
    """

    turnstile_token: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="turnstileToken"),
        pydantic.Field(alias="turnstileToken", description="The Cloudflare Turnstile token from the form."),
    ]
    """
    The Cloudflare Turnstile token from the form.
    """

    email: str
    full_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fullName"),
        pydantic.Field(
            alias="fullName",
            description="One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.",
        ),
    ]
    """
    One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.
    """

    password: str = pydantic.Field()
    """
    12 to 128 characters; common passwords are refused.
    """

    country: str
    accept_terms: typing_extensions.Annotated[
        bool, FieldMetadata(alias="acceptTerms"), pydantic.Field(alias="acceptTerms", description="Must be true.")
    ]
    """
    Must be true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

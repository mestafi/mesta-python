
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxClaimRequest(UniversalBaseModel):
    token: str = pydantic.Field()
    """
    The token from the fragment of `claimUrl`.
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

    accept_terms: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="acceptTerms"),
        pydantic.Field(alias="acceptTerms", description="Must be true; 422 with the terms URL and version otherwise."),
    ]
    """
    Must be true; 422 with the terms URL and version otherwise.
    """

    keep_pre_claim_keys: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="keepPreClaimKeys"),
        pydantic.Field(
            alias="keepPreClaimKeys",
            description="Keep the pre-claim keys, their webhook endpoints and signing key together. Otherwise revoke the keys, delete the endpoints, rotate the signing key, recreate the Mesta test endpoint and return one fresh pair once.",
        ),
    ] = None
    """
    Keep the pre-claim keys, their webhook endpoints and signing key together. Otherwise revoke the keys, delete the endpoints, rotate the signing key, recreate the Mesta test endpoint and return one fresh pair once.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

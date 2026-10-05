
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_created_docs import SandboxCreatedDocs
from .sandbox_created_plane import SandboxCreatedPlane
from .sandbox_key import SandboxKey
from .sandbox_machine_created_seed import SandboxMachineCreatedSeed
from .sandbox_machine_created_status import SandboxMachineCreatedStatus
from .sandbox_terms import SandboxTerms


class SandboxMachineCreated(UniversalBaseModel):
    status: SandboxMachineCreatedStatus
    claim_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="claimUrl"),
        pydantic.Field(
            alias="claimUrl",
            description="Create response only, while unclaimed. A single-use bearer capability in the URL fragment: whoever opens it owns the sandbox.",
        ),
    ]
    """
    Create response only, while unclaimed. A single-use bearer capability in the URL fragment: whoever opens it owns the sandbox.
    """

    seed: SandboxMachineCreatedSeed
    sandbox_id: typing_extensions.Annotated[str, FieldMetadata(alias="sandboxId"), pydantic.Field(alias="sandboxId")]
    merchant_id: typing_extensions.Annotated[str, FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId")]
    plane: SandboxCreatedPlane
    api_base_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="apiBaseUrl"), pydantic.Field(alias="apiBaseUrl")
    ]
    portal_url: typing_extensions.Annotated[str, FieldMetadata(alias="portalUrl"), pydantic.Field(alias="portalUrl")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="The non-null deadline at issuance: seven days from machine creation or 72 hours from signup or claim. Later status reads report null after verification.",
        ),
    ]
    """
    The non-null deadline at issuance: seven days from machine creation or 72 hours from signup or claim. Later status reads report null after verification.
    """

    terms: SandboxTerms
    docs: SandboxCreatedDocs
    message: str
    keys: typing.List[SandboxKey] = pydantic.Field()
    """
    Fresh pairs only. On claim with keepPreClaimKeys=true this array is empty; retained secrets are never returned again.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

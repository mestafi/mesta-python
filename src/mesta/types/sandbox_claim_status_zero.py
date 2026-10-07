
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_claim_status_details_counts import SandboxClaimStatusDetailsCounts
from .sandbox_claim_status_details_pre_claim_endpoints_item import SandboxClaimStatusDetailsPreClaimEndpointsItem
from .sandbox_claim_status_details_pre_claim_keys_item import SandboxClaimStatusDetailsPreClaimKeysItem
from .sandbox_claim_status_details_seed import SandboxClaimStatusDetailsSeed
from .sandbox_claim_status_zero_status import SandboxClaimStatusZeroStatus


class SandboxClaimStatusZero(UniversalBaseModel):
    status: typing.Optional[SandboxClaimStatusZeroStatus] = None
    sandbox_id: typing_extensions.Annotated[str, FieldMetadata(alias="sandboxId"), pydantic.Field(alias="sandboxId")]
    short_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shortId"), pydantic.Field(alias="shortId")
    ] = None
    merchant_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="merchantName"), pydantic.Field(alias="merchantName")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    seed: SandboxClaimStatusDetailsSeed
    counts: SandboxClaimStatusDetailsCounts = pydantic.Field()
    """
    accounts: balance accounts per currency, excluding virtual accounts. All seven counts are integers.
    """

    pre_claim_keys: typing_extensions.Annotated[
        typing.List[SandboxClaimStatusDetailsPreClaimKeysItem],
        FieldMetadata(alias="preClaimKeys"),
        pydantic.Field(alias="preClaimKeys", description="Pre-claim key metadata for fresh tokens; empty otherwise."),
    ]
    """
    Pre-claim key metadata for fresh tokens; empty otherwise.
    """

    pre_claim_endpoints: typing_extensions.Annotated[
        typing.List[SandboxClaimStatusDetailsPreClaimEndpointsItem],
        FieldMetadata(alias="preClaimEndpoints"),
        pydantic.Field(
            alias="preClaimEndpoints", description="Pre-claim receiver hosts for fresh tokens; empty otherwise."
        ),
    ]
    """
    Pre-claim receiver hosts for fresh tokens; empty otherwise.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

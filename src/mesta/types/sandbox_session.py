
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_counts import SandboxCounts
from .sandbox_fixtures import SandboxFixtures
from .sandbox_key_metadata import SandboxKeyMetadata
from .sandbox_seed import SandboxSeed
from .sandbox_session_plane import SandboxSessionPlane
from .sandbox_session_reset import SandboxSessionReset
from .sandbox_session_status import SandboxSessionStatus
from .sandbox_session_wallets import SandboxSessionWallets


class SandboxSession(UniversalBaseModel):
    """
    Read status only: API-key metadata never contains apiKey or apiSecret. `fixtures` is absent until the sample data is complete; its `webhook.signingKey` remains retrievable. Status reads remain available while paused, resetting or failed.
    """

    sandbox_id: typing_extensions.Annotated[str, FieldMetadata(alias="sandboxId"), pydantic.Field(alias="sandboxId")]
    merchant_id: typing_extensions.Annotated[str, FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId")]
    status: SandboxSessionStatus = pydantic.Field()
    """
    deleted, killed and expired are closed states. An operator closing one again receives 409 SANDBOX_ALREADY_CLOSED; this operator-only code is not a DELETE response.
    """

    plane: SandboxSessionPlane
    api_base_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="apiBaseUrl"), pydantic.Field(alias="apiBaseUrl")
    ]
    portal_url: typing_extensions.Annotated[str, FieldMetadata(alias="portalUrl"), pydantic.Field(alias="portalUrl")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt",
            description="Seven days from creation while unclaimed; 72 hours from the sign-up or claim until the email is verified; null afterwards.",
        ),
    ] = None
    """
    Seven days from creation while unclaimed; 72 hours from the sign-up or claim until the email is verified; null afterwards.
    """

    email_verified: typing_extensions.Annotated[
        bool, FieldMetadata(alias="emailVerified"), pydantic.Field(alias="emailVerified")
    ]
    pause_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pauseMessage"),
        pydantic.Field(
            alias="pauseMessage",
            description="Mesta's pause message, or null when no message is set. Read with executionPaused; null uses the portal's default pause notice.",
        ),
    ] = None
    """
    Mesta's pause message, or null when no message is set. Read with executionPaused; null uses the portal's default pause notice.
    """

    counts: SandboxCounts
    execution_paused: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="executionPaused"),
        pydantic.Field(
            alias="executionPaused",
            description="True while Mesta has paused the sandbox environment; every other call answers 503 SANDBOX_PAUSED meanwhile.",
        ),
    ]
    """
    True while Mesta has paused the sandbox environment; every other call answers 503 SANDBOX_PAUSED meanwhile.
    """

    wallets: SandboxSessionWallets = pydantic.Field()
    """
    The merchant wallet's state: `ready` when the four test-network addresses exist, `pending` while the wallet was skipped for vendor capacity when the sample data was added, or a request is waiting, `failed` otherwise. The `wallets` entry of `seed.steps` carries the same state; `fixtures.wallets` is empty until the addresses exist.
    """

    keys: typing.List[SandboxKeyMetadata]
    seed: SandboxSeed
    reset: typing.Optional[SandboxSessionReset] = pydantic.Field(default=None)
    """
    Present only after a failed reset. The sandbox returns to its previous status with `seed.status` complete and `seed.error` set. Retry reset or delete the sandbox.
    """

    fixtures: typing.Optional[SandboxFixtures] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

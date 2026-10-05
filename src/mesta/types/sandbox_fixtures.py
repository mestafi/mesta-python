
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_fixtures_balances_item import SandboxFixturesBalancesItem
from .sandbox_fixtures_beneficiaries_item import SandboxFixturesBeneficiariesItem
from .sandbox_fixtures_deposit_source import SandboxFixturesDepositSource
from .sandbox_fixtures_orders_item import SandboxFixturesOrdersItem
from .sandbox_fixtures_senders_item import SandboxFixturesSendersItem
from .sandbox_fixtures_webhook import SandboxFixturesWebhook
from .sandbox_wallet import SandboxWallet


class SandboxFixtures(UniversalBaseModel):
    """
    Every sample object by label, present once the sample data is complete. Labels are stable across sandboxes; ids are not.
    """

    version: str
    deposit_source: typing_extensions.Annotated[
        SandboxFixturesDepositSource, FieldMetadata(alias="depositSource"), pydantic.Field(alias="depositSource")
    ]
    senders: typing.List[SandboxFixturesSendersItem]
    beneficiaries: typing.List[SandboxFixturesBeneficiariesItem]
    orders: typing.List[SandboxFixturesOrdersItem]
    webhook: SandboxFixturesWebhook
    wallets: typing.List[SandboxWallet] = pydantic.Field()
    """
    The address array when provisioned; empty while no wallet exists. The state is the session read's `wallets` block and the `wallets` entry of `seed.steps`.
    """

    balances: typing.List[SandboxFixturesBalancesItem]
    magic_values: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="magicValues"),
        pydantic.Field(
            alias="magicValues",
            description="The values that force outcomes, as documented at https://docs.mesta.xyz/docs/sandbox-simulation.",
        ),
    ]
    """
    The values that force outcomes, as documented at https://docs.mesta.xyz/docs/sandbox-simulation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

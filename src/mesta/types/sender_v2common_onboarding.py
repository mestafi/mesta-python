
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .public_sender_capability import PublicSenderCapability
from .sender_v2common_onboarding_nature_of_payments_item import SenderV2CommonOnboardingNatureOfPaymentsItem
from .sender_v2common_onboarding_source_of_funds import SenderV2CommonOnboardingSourceOfFunds


class SenderV2CommonOnboarding(UniversalBaseModel):
    """
    Additional compliance onboarding fields required for v2 sender creation.
    """

    capabilities: typing.Optional[typing.List[PublicSenderCapability]] = pydantic.Field(default=None)
    """
    Optional virtual bank account capabilities requested during onboarding. Capability acceptance is reported in the create-sender response; sender creation does not fail solely because a requested capability is unavailable.
    """

    expected_monthly_volume_estimate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="expectedMonthlyVolumeEstimate"),
        pydantic.Field(
            alias="expectedMonthlyVolumeEstimate",
            description="Expected monthly transaction volume estimate for the sender.",
        ),
    ]
    """
    Expected monthly transaction volume estimate for the sender.
    """

    average_transaction_size: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="averageTransactionSize"),
        pydantic.Field(alias="averageTransactionSize", description="Expected average transaction size for the sender."),
    ]
    """
    Expected average transaction size for the sender.
    """

    primary_counterparty_jurisdictions: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="primaryCounterpartyJurisdictions"),
        pydantic.Field(
            alias="primaryCounterpartyJurisdictions",
            description="Primary jurisdictions the sender expects to transact with. Each value must be an ISO 3166-1 alpha-2 country code.",
        ),
    ]
    """
    Primary jurisdictions the sender expects to transact with. Each value must be an ISO 3166-1 alpha-2 country code.
    """

    nature_of_payments: typing_extensions.Annotated[
        typing.List[SenderV2CommonOnboardingNatureOfPaymentsItem],
        FieldMetadata(alias="natureOfPayments"),
        pydantic.Field(alias="natureOfPayments", description="Primary purposes for the sender's payments."),
    ]
    """
    Primary purposes for the sender's payments.
    """

    source_of_funds: typing_extensions.Annotated[
        SenderV2CommonOnboardingSourceOfFunds,
        FieldMetadata(alias="sourceOfFunds"),
        pydantic.Field(alias="sourceOfFunds", description="Primary source of funds for the sender."),
    ]
    """
    Primary source of funds for the sender.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

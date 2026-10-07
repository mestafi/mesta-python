
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .simulate_deposit_response_data_outcome import SimulateDepositResponseDataOutcome
from .simulate_deposit_response_data_owner_type import SimulateDepositResponseDataOwnerType


class SimulateDepositResponseData(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The deposit's id; readable at `GET /v1/merchant/fiat-deposits/{id}` or `/v1/merchant/stablecoin-deposits/{id}`.
    """

    owner_type: typing_extensions.Annotated[
        SimulateDepositResponseDataOwnerType, FieldMetadata(alias="ownerType"), pydantic.Field(alias="ownerType")
    ]
    owner_id: typing_extensions.Annotated[str, FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")]
    currency: str
    amount: str
    outcome: SimulateDepositResponseDataOutcome

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

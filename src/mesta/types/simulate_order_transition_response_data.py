
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .simulate_order_transition_response_data_status import SimulateOrderTransitionResponseDataStatus


class SimulateOrderTransitionResponseData(UniversalBaseModel):
    id: str
    status: SimulateOrderTransitionResponseDataStatus
    events: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Additional published event names, in order, when the transition publishes two. event holds the first; success publishes only order:success.
    """

    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `order:*` event that was published, or null for a status without one.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

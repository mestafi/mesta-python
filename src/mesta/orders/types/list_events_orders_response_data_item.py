
import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListEventsOrdersResponseDataItem(UniversalBaseModel):
    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-friendly display name of the order event
    """

    time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp when the event occurred
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListEventsResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Event name
    """

    aggregate_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="aggregateType"), pydantic.Field(alias="aggregateType")
    ] = None
    aggregate_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="aggregateId"), pydantic.Field(alias="aggregateId")
    ] = None
    merchant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId")
    ] = None
    payload: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Event payload
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

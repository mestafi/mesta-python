
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_webhooks_response_data_events_item import UpdateWebhooksResponseDataEventsItem


class UpdateWebhooksResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the webhook
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the webhook configuration
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the webhook was created (ISO 8601)"),
    ] = None
    """
    Timestamp when the webhook was created (ISO 8601)
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the webhook was last updated (ISO 8601)"),
    ] = None
    """
    Timestamp when the webhook was last updated (ISO 8601)
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Identifier of the merchant who owns this webhook"),
    ] = None
    """
    Identifier of the merchant who owns this webhook
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL where webhook events will be sent
    """

    events: typing.Optional[typing.List[UpdateWebhooksResponseDataEventsItem]] = pydantic.Field(default=None)
    """
    List of events this webhook subscribes to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

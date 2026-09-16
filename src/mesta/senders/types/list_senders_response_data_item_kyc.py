
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_senders_response_data_item_kyc_status import ListSendersResponseDataItemKycStatus


class ListSendersResponseDataItemKyc(UniversalBaseModel):
    """
    Know Your Customer verification information
    """

    status: typing.Optional[ListSendersResponseDataItemKycStatus] = pydantic.Field(default=None)
    """
    KYC verification status
    """

    status_updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="statusUpdatedAt"),
        pydantic.Field(alias="statusUpdatedAt", description="Timestamp of the last KYC status update"),
    ] = None
    """
    Timestamp of the last KYC status update
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

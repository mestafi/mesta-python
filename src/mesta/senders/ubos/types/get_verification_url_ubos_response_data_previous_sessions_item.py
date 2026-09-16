
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_verification_url_ubos_response_data_previous_sessions_item_status import (
    GetVerificationUrlUbosResponseDataPreviousSessionsItemStatus,
)


class GetVerificationUrlUbosResponseDataPreviousSessionsItem(UniversalBaseModel):
    kyc_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="kycLink"),
        pydantic.Field(alias="kycLink", description="Selfie verification URL for the session."),
    ] = None
    """
    Selfie verification URL for the session.
    """

    status: typing.Optional[GetVerificationUrlUbosResponseDataPreviousSessionsItemStatus] = pydantic.Field(default=None)
    """
    Status of the selfie verification session.
    """

    expiry_timestamp: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiryTimestamp"),
        pydantic.Field(
            alias="expiryTimestamp", description="Session expiry timestamp in milliseconds since Unix epoch."
        ),
    ] = None
    """
    Session expiry timestamp in milliseconds since Unix epoch.
    """

    created_timestamp: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdTimestamp"),
        pydantic.Field(
            alias="createdTimestamp", description="Session creation timestamp in milliseconds since Unix epoch."
        ),
    ] = None
    """
    Session creation timestamp in milliseconds since Unix epoch.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_verification_url_ubos_response_data_latest_session import GetVerificationUrlUbosResponseDataLatestSession
from .get_verification_url_ubos_response_data_previous_sessions_item import (
    GetVerificationUrlUbosResponseDataPreviousSessionsItem,
)


class GetVerificationUrlUbosResponseData(UniversalBaseModel):
    latest_session: typing_extensions.Annotated[
        typing.Optional[GetVerificationUrlUbosResponseDataLatestSession],
        FieldMetadata(alias="latestSession"),
        pydantic.Field(
            alias="latestSession",
            description="The most recent selfie verification session for the UBO, or `null` if no session exists yet.",
        ),
    ] = None
    """
    The most recent selfie verification session for the UBO, or `null` if no session exists yet.
    """

    previous_sessions: typing_extensions.Annotated[
        typing.Optional[typing.List[GetVerificationUrlUbosResponseDataPreviousSessionsItem]],
        FieldMetadata(alias="previousSessions"),
        pydantic.Field(
            alias="previousSessions",
            description="Older selfie verification sessions for the UBO in reverse chronological order.",
        ),
    ] = None
    """
    Older selfie verification sessions for the UBO in reverse chronological order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

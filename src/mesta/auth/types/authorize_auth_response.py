
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .authorize_auth_response_data import AuthorizeAuthResponseData


class AuthorizeAuthResponse(UniversalBaseModel):
    data: typing.Optional[AuthorizeAuthResponseData] = None
    request_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique identifier for the API request"),
    ] = None
    """
    Unique identifier for the API request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

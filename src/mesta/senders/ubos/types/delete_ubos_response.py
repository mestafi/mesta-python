
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class DeleteUbosResponse(UniversalBaseModel):
    request_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique identifier for the API request"),
    ]
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

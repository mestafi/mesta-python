
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TooManyRequestsErrorBodyErrorDetails(UniversalBaseModel):
    retry_after_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="retryAfterMs"),
        pydantic.Field(alias="retryAfterMs", description="Milliseconds to wait before the next request is accepted"),
    ] = None
    """
    Milliseconds to wait before the next request is accepted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

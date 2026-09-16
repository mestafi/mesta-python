
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListApiKeysResponseMeta(UniversalBaseModel):
    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of API keys
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current page number
    """

    page_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pageSize"),
        pydantic.Field(alias="pageSize", description="Number of items per page"),
    ] = None
    """
    Number of items per page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

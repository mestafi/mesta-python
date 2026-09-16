
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetSendersResponseDataIdentityDocumentFront(UniversalBaseModel):
    """
    Front side of the identity document
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to access the document front image
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="Name of the document file"),
    ] = None
    """
    Name of the document file
    """

    file_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileType"),
        pydantic.Field(alias="fileType", description="Type of the identity document"),
    ] = None
    """
    Type of the identity document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

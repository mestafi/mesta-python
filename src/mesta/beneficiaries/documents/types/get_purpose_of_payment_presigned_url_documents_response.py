
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class GetPurposeOfPaymentPresignedUrlDocumentsResponse(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pre-signed S3 URL for downloading the document
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="Original file name"),
    ] = None
    """
    Original file name
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document type
    """

    blob: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 encoded file content
    """

    expires_in: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiresIn"),
        pydantic.Field(alias="expiresIn", description="URL expiry time in seconds"),
    ] = None
    """
    URL expiry time in seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

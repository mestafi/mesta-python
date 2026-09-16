
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_presigned_url_documents_response_data_type import GetPresignedUrlDocumentsResponseDataType


class GetPresignedUrlDocumentsResponseData(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pre-signed S3 URL for downloading the document
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="Original file name of the document"),
    ] = None
    """
    Original file name of the document
    """

    type: typing.Optional[GetPresignedUrlDocumentsResponseDataType] = pydantic.Field(default=None)
    """
    Type of the document
    """

    expires_in: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiresIn"),
        pydantic.Field(alias="expiresIn", description="Number of seconds until the URL expires"),
    ] = None
    """
    Number of seconds until the URL expires
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

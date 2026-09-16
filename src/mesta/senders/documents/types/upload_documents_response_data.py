
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .upload_documents_response_data_type import UploadDocumentsResponseDataType


class UploadDocumentsResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the uploaded document
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="Original name of the uploaded file"),
    ] = None
    """
    Original name of the uploaded file
    """

    type: typing.Optional[UploadDocumentsResponseDataType] = pydantic.Field(default=None)
    """
    Type of the uploaded document
    """

    s3key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="s3Key"),
        pydantic.Field(alias="s3Key", description="Storage key for the uploaded document"),
    ] = None
    """
    Storage key for the uploaded document
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to access the uploaded document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

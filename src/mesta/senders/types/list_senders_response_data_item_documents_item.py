
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_senders_response_data_item_documents_item_type import ListSendersResponseDataItemDocumentsItemType


class ListSendersResponseDataItemDocumentsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document identifier
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document URL
    """

    type: typing.Optional[ListSendersResponseDataItemDocumentsItemType] = pydantic.Field(default=None)
    """
    Type of document
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="Name of the document file"),
    ] = None
    """
    Name of the document file
    """

    submitted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="submittedAt"),
        pydantic.Field(alias="submittedAt", description="Timestamp when the document was submitted (ISO 8601 format)"),
    ] = None
    """
    Timestamp when the document was submitted (ISO 8601 format)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

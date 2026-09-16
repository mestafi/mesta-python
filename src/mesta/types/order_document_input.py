
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .document_type import DocumentType


class OrderDocumentInput(UniversalBaseModel):
    """
    Document to attach to an order
    """

    file_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="fileName"), pydantic.Field(alias="fileName", description="Name of the file")
    ]
    """
    Name of the file
    """

    type: DocumentType
    blob: str = pydantic.Field()
    """
    Base64-encoded file content (PNG, JPG, JPEG, or PDF)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

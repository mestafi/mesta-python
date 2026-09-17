
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .create_ubos_response_data_documents_item_type import CreateUbosResponseDataDocumentsItemType


class CreateUbosResponseDataDocumentsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[CreateUbosResponseDataDocumentsItemType] = None
    url: typing.Optional[str] = None
    uploaded_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="uploadedAt"), pydantic.Field(alias="uploadedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

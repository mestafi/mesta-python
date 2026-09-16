
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PatchIndividualSenderIdentity(UniversalBaseModel):
    document_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentType"), pydantic.Field(alias="documentType")
    ] = None
    country_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="countryCode"), pydantic.Field(alias="countryCode")
    ] = None
    document_front: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentFront"), pydantic.Field(alias="documentFront")
    ] = None
    document_back: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentBack"), pydantic.Field(alias="documentBack")
    ] = None
    document_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentNumber"), pydantic.Field(alias="documentNumber")
    ] = None
    issue_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="issueDate"), pydantic.Field(alias="issueDate")
    ] = None
    expiry_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="expiryDate"), pydantic.Field(alias="expiryDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .update_ubos_request_identity_document_type import UpdateUbosRequestIdentityDocumentType


class UpdateUbosRequestIdentity(UniversalBaseModel):
    document_type: typing_extensions.Annotated[
        typing.Optional[UpdateUbosRequestIdentityDocumentType],
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType", description="Type of identity document"),
    ] = None
    """
    Type of identity document
    """

    country_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="Country code of the identity document"),
    ] = None
    """
    Country code of the identity document
    """

    document_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentNumber"),
        pydantic.Field(alias="documentNumber", description="Document identification number"),
    ] = None
    """
    Document identification number
    """

    document_front: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentFront"),
        pydantic.Field(alias="documentFront", description="Base64 encoded front image of identity document"),
    ] = None
    """
    Base64 encoded front image of identity document
    """

    document_back: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentBack"),
        pydantic.Field(alias="documentBack", description="Base64 encoded back image of identity document"),
    ] = None
    """
    Base64 encoded back image of identity document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

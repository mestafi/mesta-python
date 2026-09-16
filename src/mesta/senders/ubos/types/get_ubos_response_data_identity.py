
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_ubos_response_data_identity_document_back import GetUbosResponseDataIdentityDocumentBack
from .get_ubos_response_data_identity_document_front import GetUbosResponseDataIdentityDocumentFront
from .get_ubos_response_data_identity_document_type import GetUbosResponseDataIdentityDocumentType


class GetUbosResponseDataIdentity(UniversalBaseModel):
    """
    Identity verification information
    """

    country_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="Two-letter country code of the identity document"),
    ] = None
    """
    Two-letter country code of the identity document
    """

    document_type: typing_extensions.Annotated[
        typing.Optional[GetUbosResponseDataIdentityDocumentType],
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType", description="Type of identity document"),
    ] = None
    """
    Type of identity document
    """

    document_front: typing_extensions.Annotated[
        typing.Optional[GetUbosResponseDataIdentityDocumentFront],
        FieldMetadata(alias="documentFront"),
        pydantic.Field(alias="documentFront", description="Front side of the identity document"),
    ] = None
    """
    Front side of the identity document
    """

    document_back: typing_extensions.Annotated[
        typing.Optional[GetUbosResponseDataIdentityDocumentBack],
        FieldMetadata(alias="documentBack"),
        pydantic.Field(alias="documentBack", description="Back side of the identity document"),
    ] = None
    """
    Back side of the identity document
    """

    document_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentNumber"),
        pydantic.Field(alias="documentNumber", description="Identity document number"),
    ] = None
    """
    Identity document number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_senders_response_data_item_identity_document_type import ListSendersResponseDataItemIdentityDocumentType


class ListSendersResponseDataItemIdentity(UniversalBaseModel):
    """
    Identity verification information (for individual senders)
    """

    document_type: typing_extensions.Annotated[
        typing.Optional[ListSendersResponseDataItemIdentityDocumentType],
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType", description="Type of identity document"),
    ] = None
    """
    Type of identity document
    """

    country_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="Two-letter country code of the identity document"),
    ] = None
    """
    Two-letter country code of the identity document
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

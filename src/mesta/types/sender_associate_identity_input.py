
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SenderAssociateIdentityInput(UniversalBaseModel):
    country_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="countryCode"), pydantic.Field(alias="countryCode")
    ]
    document_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="documentType"),
        pydantic.Field(
            alias="documentType",
            description="Supported values and front/back requirements depend on the identity country.",
        ),
    ]
    """
    Supported values and front/back requirements depend on the identity country.
    """

    document_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentNumber"), pydantic.Field(alias="documentNumber")
    ]
    document_front: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentFront"),
        pydantic.Field(alias="documentFront", description="Base64 encoded front image of the identity document."),
    ] = None
    """
    Base64 encoded front image of the identity document.
    """

    document_back: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentBack"),
        pydantic.Field(alias="documentBack", description="Base64 encoded back image of the identity document."),
    ] = None
    """
    Base64 encoded back image of the identity document.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

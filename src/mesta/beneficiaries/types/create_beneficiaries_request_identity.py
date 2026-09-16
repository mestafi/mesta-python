
import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_beneficiaries_request_identity_document_type import CreateBeneficiariesRequestIdentityDocumentType


class CreateBeneficiariesRequestIdentity(UniversalBaseModel):
    """
    Identity document details
    """

    document_type: typing_extensions.Annotated[
        typing.Optional[CreateBeneficiariesRequestIdentityDocumentType],
        FieldMetadata(alias="documentType"),
        pydantic.Field(alias="documentType", description="Type of identity document"),
    ] = None
    """
    Type of identity document
    """

    document_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentNumber"),
        pydantic.Field(alias="documentNumber", description="Document number"),
    ] = None
    """
    Document number
    """

    issue_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="issueDate"),
        pydantic.Field(alias="issueDate", description="Issue date"),
    ] = None
    """
    Issue date
    """

    expiry_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="expiryDate"),
        pydantic.Field(alias="expiryDate", description="Expiry date"),
    ] = None
    """
    Expiry date
    """

    issuer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Issuing authority
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetMerchantsResponseDataUbo(UniversalBaseModel):
    """
    Ultimate Beneficial Owner information
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the UBO
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the UBO record
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Timestamp when the UBO record was created"),
    ] = None
    """
    Timestamp when the UBO record was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp when the UBO record was last updated"),
    ] = None
    """
    Timestamp when the UBO record was last updated
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="First name of the UBO"),
    ] = None
    """
    First name of the UBO
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="Last name of the UBO"),
    ] = None
    """
    Last name of the UBO
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the UBO
    """

    merchant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="Reference to the merchant"),
    ] = None
    """
    Reference to the merchant
    """

    ownership_percent: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ownershipPercent"),
        pydantic.Field(alias="ownershipPercent", description="Percentage of ownership"),
    ] = None
    """
    Percentage of ownership
    """

    identification_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="identificationNumber"),
        pydantic.Field(alias="identificationNumber", description="Identification number of the UBO"),
    ] = None
    """
    Identification number of the UBO
    """

    birth_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="birthDate"),
        pydantic.Field(alias="birthDate", description="Birth date of the UBO"),
    ] = None
    """
    Birth date of the UBO
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_ubos_response_data_sender_addresses_item import GetUbosResponseDataSenderAddressesItem
from .get_ubos_response_data_sender_documents_item import GetUbosResponseDataSenderDocumentsItem
from .get_ubos_response_data_sender_kyb import GetUbosResponseDataSenderKyb
from .get_ubos_response_data_sender_kyc import GetUbosResponseDataSenderKyc
from .get_ubos_response_data_sender_status import GetUbosResponseDataSenderStatus
from .get_ubos_response_data_sender_tos import GetUbosResponseDataSenderTos
from .get_ubos_response_data_sender_type import GetUbosResponseDataSenderType


class GetUbosResponseDataSender(UniversalBaseModel):
    """
    Associated sender information
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sender ID
    """

    version: typing.Optional[int] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    full_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fullName"), pydantic.Field(alias="fullName")
    ] = None
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    middle_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="birthDate"), pydantic.Field(alias="birthDate")
    ] = None
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    gender: typing.Optional[str] = None
    occupation: typing.Optional[str] = None
    addresses: typing.Optional[typing.List[GetUbosResponseDataSenderAddressesItem]] = None
    merchant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="merchantId"), pydantic.Field(alias="merchantId")
    ] = None
    kyb: typing.Optional[GetUbosResponseDataSenderKyb] = None
    kyc: typing.Optional[GetUbosResponseDataSenderKyc] = None
    status: typing.Optional[GetUbosResponseDataSenderStatus] = None
    type: typing.Optional[GetUbosResponseDataSenderType] = None
    website_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteUrl"), pydantic.Field(alias="websiteUrl")
    ] = None
    identification_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="identificationNumber"), pydantic.Field(alias="identificationNumber")
    ] = None
    documents: typing.Optional[typing.List[GetUbosResponseDataSenderDocumentsItem]] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    identity: typing.Optional[typing.Dict[str, typing.Any]] = None
    registration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="registrationDate"), pydantic.Field(alias="registrationDate")
    ] = None
    business_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="businessType"), pydantic.Field(alias="businessType")
    ] = None
    tos: typing.Optional[GetUbosResponseDataSenderTos] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_ubo_rules_v2senders_response_data_owner import GetUboRulesV2SendersResponseDataOwner
from .get_ubo_rules_v2senders_response_data_owner_type import GetUboRulesV2SendersResponseDataOwnerType
from .get_ubo_rules_v2senders_response_data_rules import GetUboRulesV2SendersResponseDataRules


class GetUboRulesV2SendersResponseData(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the validation rules
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version number of the rules
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="deletedAt"), pydantic.Field(alias="deletedAt")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    deleted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deletedBy"), pydantic.Field(alias="deletedBy")
    ] = None
    owner: typing.Optional[GetUboRulesV2SendersResponseDataOwner] = None
    owner_type: typing_extensions.Annotated[
        typing.Optional[GetUboRulesV2SendersResponseDataOwnerType],
        FieldMetadata(alias="ownerType"),
        pydantic.Field(alias="ownerType"),
    ] = None
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Two-letter country code (ISO 3166-1 alpha-2)
    """

    rules: typing.Optional[GetUboRulesV2SendersResponseDataRules] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

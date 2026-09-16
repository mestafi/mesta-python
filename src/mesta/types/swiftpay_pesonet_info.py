
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .swiftpay_pesonet_info_channel_subject import SwiftpayPesonetInfoChannelSubject
from .swiftpay_pesonet_info_extend_info import SwiftpayPesonetInfoExtendInfo


class SwiftpayPesonetInfo(UniversalBaseModel):
    channel_subject: typing_extensions.Annotated[
        SwiftpayPesonetInfoChannelSubject,
        FieldMetadata(alias="channelSubject"),
        pydantic.Field(
            alias="channelSubject", description="Channel subject - specifies the bank or payment service provider"
        ),
    ]
    """
    Channel subject - specifies the bank or payment service provider
    """

    extend_info: typing_extensions.Annotated[
        SwiftpayPesonetInfoExtendInfo, FieldMetadata(alias="extendInfo"), pydantic.Field(alias="extendInfo")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

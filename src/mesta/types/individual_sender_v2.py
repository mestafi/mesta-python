
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .individual_sender import IndividualSender
from .sender_v2common_onboarding import SenderV2CommonOnboarding


class IndividualSenderV2(IndividualSender, SenderV2CommonOnboarding):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

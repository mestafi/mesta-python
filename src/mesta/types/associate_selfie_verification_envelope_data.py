
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .selfie_verification_session import SelfieVerificationSession


class AssociateSelfieVerificationEnvelopeData(UniversalBaseModel):
    latest_session: typing_extensions.Annotated[
        typing.Optional[SelfieVerificationSession],
        FieldMetadata(alias="latestSession"),
        pydantic.Field(alias="latestSession"),
    ] = None
    previous_sessions: typing_extensions.Annotated[
        typing.List[SelfieVerificationSession],
        FieldMetadata(alias="previousSessions"),
        pydantic.Field(alias="previousSessions"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

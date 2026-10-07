
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxTermsNotAcceptedErrorTerms(UniversalBaseModel):
    url: str
    version: str
    privacy_notice_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="privacyNoticeUrl"),
        pydantic.Field(
            alias="privacyNoticeUrl",
            description="The Sandbox privacy notice's one published location. It is linked as information and not accepted.",
        ),
    ]
    """
    The Sandbox privacy notice's one published location. It is linked as information and not accepted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxFixturesWebhook(UniversalBaseModel):
    id: str
    url: str
    signing_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="signingKey"),
        pydantic.Field(
            alias="signingKey",
            description="Your merchant's webhook signing key, the one every delivery is signed with.",
        ),
    ]
    """
    Your merchant's webhook signing key, the one every delivery is signed with.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

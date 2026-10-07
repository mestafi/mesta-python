
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxCodeSent(UniversalBaseModel):
    sent_to: typing_extensions.Annotated[
        str, FieldMetadata(alias="sentTo"), pydantic.Field(alias="sentTo", description="Masked recipient address.")
    ]
    """
    Masked recipient address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

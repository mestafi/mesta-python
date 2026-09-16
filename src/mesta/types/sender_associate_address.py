
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SenderAssociateAddress(UniversalBaseModel):
    street: str
    street2: typing.Optional[str] = None
    city: str
    state: typing.Optional[str] = None
    postal_code: typing_extensions.Annotated[str, FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")]
    country: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

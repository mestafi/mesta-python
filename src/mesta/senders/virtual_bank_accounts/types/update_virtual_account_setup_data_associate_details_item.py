
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class UpdateVirtualAccountSetupDataAssociateDetailsItem(UniversalBaseModel):
    associate_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="associateId"), pydantic.Field(alias="associateId")
    ]
    nationality: typing.Optional[str] = None
    birth_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="birthDate"), pydantic.Field(alias="birthDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

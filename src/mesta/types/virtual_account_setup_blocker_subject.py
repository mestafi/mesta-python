
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .virtual_account_setup_blocker_subject_type import VirtualAccountSetupBlockerSubjectType


class VirtualAccountSetupBlockerSubject(UniversalBaseModel):
    """
    Sender, UBO, or representative affected by this blocker.
    """

    type: VirtualAccountSetupBlockerSubjectType
    id: typing.Optional[str] = None
    roles: typing.Optional[typing.List[str]] = None
    minimum_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minimumCount"), pydantic.Field(alias="minimumCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

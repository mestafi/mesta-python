
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .verify_sender_requirements_blocker_subject_type import VerifySenderRequirementsBlockerSubjectType


class VerifySenderRequirementsBlockerSubject(UniversalBaseModel):
    """
    The sender or existing UBO missing data, or the associate role that must be created.
    """

    type: VerifySenderRequirementsBlockerSubjectType
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the existing sender, UBO, or associate whose data is missing.
    """

    roles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Required role or roles when `type` is `associate`.
    """

    minimum_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minimumCount"),
        pydantic.Field(
            alias="minimumCount", description="Minimum number of associates with the specified role or roles."
        ),
    ] = None
    """
    Minimum number of associates with the specified role or roles.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

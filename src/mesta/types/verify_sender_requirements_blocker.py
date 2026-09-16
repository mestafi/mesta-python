
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .public_sender_capability import PublicSenderCapability
from .verify_sender_requirements_blocker_action import VerifySenderRequirementsBlockerAction
from .verify_sender_requirements_blocker_code import VerifySenderRequirementsBlockerCode
from .verify_sender_requirements_blocker_fields_item import VerifySenderRequirementsBlockerFieldsItem
from .verify_sender_requirements_blocker_subject import VerifySenderRequirementsBlockerSubject


class VerifySenderRequirementsBlocker(UniversalBaseModel):
    """
    An actionable public requirement that prevents sender verification. Its blocker semantics match setup-request blockers; internal canonical requirement keys are not exposed.
    """

    code: VerifySenderRequirementsBlockerCode = pydantic.Field()
    """
    Machine-readable blocker code.
    """

    required_by: typing_extensions.Annotated[
        typing.Optional[typing.List[PublicSenderCapability]],
        FieldMetadata(alias="requiredBy"),
        pydantic.Field(alias="requiredBy", description="Accepted capabilities that require this data or associate."),
    ] = None
    """
    Accepted capabilities that require this data or associate.
    """

    subject: typing.Optional[VerifySenderRequirementsBlockerSubject] = pydantic.Field(default=None)
    """
    The sender or existing UBO missing data, or the associate role that must be created.
    """

    fields: typing.Optional[typing.List[VerifySenderRequirementsBlockerFieldsItem]] = pydantic.Field(default=None)
    """
    Missing public properties on the identified subject. Requirements sharing the same subject and action are grouped.
    """

    action: typing.Optional[VerifySenderRequirementsBlockerAction] = pydantic.Field(default=None)
    """
    The next API action for resolving this blocker. Follow the returned method, path, and accepted body fields.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

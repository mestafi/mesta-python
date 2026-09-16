
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .virtual_account_setup_action import VirtualAccountSetupAction
from .virtual_account_setup_blocker_code import VirtualAccountSetupBlockerCode
from .virtual_account_setup_blocker_fields_item import VirtualAccountSetupBlockerFieldsItem
from .virtual_account_setup_blocker_subject import VirtualAccountSetupBlockerSubject


class VirtualAccountSetupBlocker(UniversalBaseModel):
    """
    A requirement preventing the setup request from progressing.
    """

    code: VirtualAccountSetupBlockerCode = pydantic.Field()
    """
    Machine-readable blocker code.
    """

    subject: typing.Optional[VirtualAccountSetupBlockerSubject] = pydantic.Field(default=None)
    """
    Sender, UBO, or representative affected by this blocker.
    """

    fields: typing.Optional[typing.List[VirtualAccountSetupBlockerFieldsItem]] = pydantic.Field(default=None)
    """
    Missing public properties on the identified subject. Requirements sharing the same subject and action are grouped in one blocker.
    """

    action: typing.Optional[VirtualAccountSetupAction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

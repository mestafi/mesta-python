
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .virtual_account_setup_blocker import VirtualAccountSetupBlocker
from .virtual_account_setup_response_currency import VirtualAccountSetupResponseCurrency
from .virtual_account_setup_response_unaccepted_fields_item import VirtualAccountSetupResponseUnacceptedFieldsItem
from .virtual_account_setup_status import VirtualAccountSetupStatus


class VirtualAccountSetupResponse(UniversalBaseModel):
    currency: VirtualAccountSetupResponseCurrency
    status: VirtualAccountSetupStatus
    requested_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="requestedAt"), pydantic.Field(alias="requestedAt")
    ]
    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None
    blockers: typing.List[VirtualAccountSetupBlocker]
    unaccepted_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[VirtualAccountSetupResponseUnacceptedFieldsItem]],
        FieldMetadata(alias="unacceptedFields"),
        pydantic.Field(
            alias="unacceptedFields",
            description="Recognized fields skipped because they were not current missing requirements. Omitted when every submitted field was accepted. Other valid submitted fields are still processed.",
        ),
    ] = None
    """
    Recognized fields skipped because they were not current missing requirements. Omitted when every submitted field was accepted. Other valid submitted fields are still processed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

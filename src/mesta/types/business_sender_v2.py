
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .business_sender import BusinessSender
from .business_sender_v2number_of_employees import BusinessSenderV2NumberOfEmployees
from .sender_v2common_onboarding import SenderV2CommonOnboarding


class BusinessSenderV2(BusinessSender, SenderV2CommonOnboarding):
    is_financial_institution: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isFinancialInstitution"),
        pydantic.Field(
            alias="isFinancialInstitution", description="Whether the sender operates as a financial institution."
        ),
    ]
    """
    Whether the sender operates as a financial institution.
    """

    website_absence_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="websiteAbsenceReason"),
        pydantic.Field(
            alias="websiteAbsenceReason",
            description="Reason the sender does not have a website. Required when `websiteUrl` is not provided.",
        ),
    ] = None
    """
    Reason the sender does not have a website. Required when `websiteUrl` is not provided.
    """

    number_of_employees: typing_extensions.Annotated[
        BusinessSenderV2NumberOfEmployees,
        FieldMetadata(alias="numberOfEmployees"),
        pydantic.Field(alias="numberOfEmployees", description="Employee count range for the business sender."),
    ]
    """
    Employee count range for the business sender.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

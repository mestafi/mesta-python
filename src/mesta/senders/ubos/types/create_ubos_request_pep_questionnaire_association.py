
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class CreateUbosRequestPepQuestionnaireAssociation(UniversalBaseModel):
    """
    Required when declarationType is IMMEDIATE_FAMILY or CLOSE_ASSOCIATE.
    """

    pep_full_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="pepFullName"), pydantic.Field(alias="pepFullName")
    ]
    relationship: str
    pep_job_title: typing_extensions.Annotated[
        str, FieldMetadata(alias="pepJobTitle"), pydantic.Field(alias="pepJobTitle")
    ]
    pep_country_or_jurisdiction: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pepCountryOrJurisdiction"),
        pydantic.Field(alias="pepCountryOrJurisdiction", description="ISO 3166-1 alpha-2 country code."),
    ]
    """
    ISO 3166-1 alpha-2 country code.
    """

    service_start_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="serviceStartDate"),
        pydantic.Field(alias="serviceStartDate", description="Date in the format YYYY-MM-DD."),
    ]
    """
    Date in the format YYYY-MM-DD.
    """

    service_end_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="serviceEndDate"),
        pydantic.Field(alias="serviceEndDate", description="Date in the format YYYY-MM-DD."),
    ]
    """
    Date in the format YYYY-MM-DD.
    """

    source_of_wealth: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceOfWealth"), pydantic.Field(alias="sourceOfWealth")
    ]
    total_estimated_net_worth_usd: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalEstimatedNetWorthUsd"), pydantic.Field(alias="totalEstimatedNetWorthUsd")
    ]
    accuracy_statement_accepted: typing_extensions.Annotated[
        bool, FieldMetadata(alias="accuracyStatementAccepted"), pydantic.Field(alias="accuracyStatementAccepted")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

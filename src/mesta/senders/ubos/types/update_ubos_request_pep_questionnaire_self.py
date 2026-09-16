
import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .update_ubos_request_pep_questionnaire_self_pep_category import UpdateUbosRequestPepQuestionnaireSelfPepCategory


class UpdateUbosRequestPepQuestionnaireSelf(UniversalBaseModel):
    """
    Required when declarationType is SELF.
    """

    pep_category: typing_extensions.Annotated[
        UpdateUbosRequestPepQuestionnaireSelfPepCategory,
        FieldMetadata(alias="pepCategory"),
        pydantic.Field(alias="pepCategory"),
    ]
    exact_job_title: typing_extensions.Annotated[
        str, FieldMetadata(alias="exactJobTitle"), pydantic.Field(alias="exactJobTitle")
    ]
    organization_or_goverment_branch: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationOrGovermentBranch"), pydantic.Field(alias="organizationOrGovermentBranch")
    ]
    jurisdiction: str = pydantic.Field()
    """
    ISO 3166-1 alpha-2 country code.
    """

    tenure_start_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="tenureStartDate"),
        pydantic.Field(alias="tenureStartDate", description="Date in the format YYYY-MM-DD."),
    ]
    """
    Date in the format YYYY-MM-DD.
    """

    tenure_end_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="tenureEndDate"),
        pydantic.Field(alias="tenureEndDate", description="Date in the format YYYY-MM-DD."),
    ]
    """
    Date in the format YYYY-MM-DD.
    """

    source_of_wealth: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceOfWealth"), pydantic.Field(alias="sourceOfWealth")
    ]
    source_of_funds: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceOfFunds"), pydantic.Field(alias="sourceOfFunds")
    ]
    estimated_annual_income_usd: typing_extensions.Annotated[
        float, FieldMetadata(alias="estimatedAnnualIncomeUsd"), pydantic.Field(alias="estimatedAnnualIncomeUsd")
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

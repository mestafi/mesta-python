
from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ....core.serialization import FieldMetadata
from .get_beneficiaries_response_data_rules_payment_types_item import GetBeneficiariesResponseDataRulesPaymentTypesItem
from .get_beneficiaries_response_data_rules_required_documents_item import (
    GetBeneficiariesResponseDataRulesRequiredDocumentsItem,
)


class GetBeneficiariesResponseDataRules(UniversalBaseModel):
    required_fields: typing_extensions.Annotated[
        typing.Optional[typing.List["ValidationField"]],
        FieldMetadata(alias="requiredFields"),
        pydantic.Field(alias="requiredFields", description="List of required fields based on ownerType"),
    ] = None
    """
    List of required fields based on ownerType
    """

    payment_types: typing_extensions.Annotated[
        typing.Optional[typing.List[GetBeneficiariesResponseDataRulesPaymentTypesItem]],
        FieldMetadata(alias="paymentTypes"),
        pydantic.Field(alias="paymentTypes", description="Available payment methods"),
    ] = None
    """
    Available payment methods
    """

    required_documents: typing_extensions.Annotated[
        typing.Optional[typing.List[GetBeneficiariesResponseDataRulesRequiredDocumentsItem]],
        FieldMetadata(alias="requiredDocuments"),
        pydantic.Field(
            alias="requiredDocuments", description="List of required documents for beneficiary verification"
        ),
    ] = None
    """
    List of required documents for beneficiary verification
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ....types.validation_field import ValidationField  # noqa: E402, I001

update_forward_refs(GetBeneficiariesResponseDataRules, ValidationField=ValidationField)

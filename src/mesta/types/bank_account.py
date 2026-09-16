
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BankAccount(UniversalBaseModel):
    account_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountNumber"),
        pydantic.Field(alias="accountNumber", description="Bank account number"),
    ]
    """
    Bank account number
    """

    routing_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="routingNumber"),
        pydantic.Field(alias="routingNumber", description="Wire routing number. Required for US beneficiaries"),
    ] = None
    """
    Wire routing number. Required for US beneficiaries
    """

    account_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountType"),
        pydantic.Field(
            alias="accountType",
            description="Type of account (e.g., savings, checking)- Only required for non-US/EU/GB beneficiaries",
        ),
    ] = None
    """
    Type of account (e.g., savings, checking)- Only required for non-US/EU/GB beneficiaries
    """

    bank_document_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankDocumentNumber"),
        pydantic.Field(
            alias="bankDocumentNumber",
            description="Document number of the bank (e.g 11 digit code for Argentina) - Only required for certain countries, check validation rules endpoint for the specific country",
        ),
    ] = None
    """
    Document number of the bank (e.g 11 digit code for Argentina) - Only required for certain countries, check validation rules endpoint for the specific country
    """

    bank_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankId"),
        pydantic.Field(
            alias="bankId",
            description="Bank Id, fetch this from the /v1/banks endpoint. Required for some non-US beneficiaries. For US beneficiaries, use routingNumber instead.",
        ),
    ] = None
    """
    Bank Id, fetch this from the /v1/banks endpoint. Required for some non-US beneficiaries. For US beneficiaries, use routingNumber instead.
    """

    ifsc_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ifscCode"),
        pydantic.Field(alias="ifscCode", description="IFSC code of the bank. Required for India (INR)"),
    ] = None
    """
    IFSC code of the bank. Required for India (INR)
    """

    sort_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sortCode"),
        pydantic.Field(alias="sortCode", description="Sort code of the bank. Required for UK (GBP)"),
    ] = None
    """
    Sort code of the bank. Required for UK (GBP)
    """

    bic: typing.Optional[str] = pydantic.Field(default=None)
    """
    BIC (SWIFT) code. Required for EUR payments
    """

    bsb_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bsbNumber"),
        pydantic.Field(alias="bsbNumber", description="BSB number of the bank. Required for Australia (AUD)"),
    ] = None
    """
    BSB number of the bank. Required for Australia (AUD)
    """

    remittance_purpose: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="remittancePurpose"),
        pydantic.Field(
            alias="remittancePurpose",
            description="Remittance purpose. Required for Australia (AUD). Refer to https://docs.mesta.xyz/docs/all-payment-types for the list of remittance purposes",
        ),
    ] = None
    """
    Remittance purpose. Required for Australia (AUD). Refer to https://docs.mesta.xyz/docs/all-payment-types for the list of remittance purposes
    """

    branch_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="branchCode"),
        pydantic.Field(
            alias="branchCode",
            description="Combined format of Institution Number (3 digits) and Transit Number (5 digits). Required for Canada. Example: 00607621",
        ),
    ] = None
    """
    Combined format of Institution Number (3 digits) and Transit Number (5 digits). Required for Canada. Example: 00607621
    """

    bank_account_country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankAccountCountry"),
        pydantic.Field(
            alias="bankAccountCountry",
            description="Country code of the bank account. Required if the bank account country is different from beneficiry address country",
        ),
    ] = None
    """
    Country code of the bank account. Required if the bank account country is different from beneficiry address country
    """

    bank_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankAddress"),
        pydantic.Field(alias="bankAddress", description="Address of the bank"),
    ] = None
    """
    Address of the bank
    """

    bank_city: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankCity"),
        pydantic.Field(alias="bankCity", description="City of the bank"),
    ] = None
    """
    City of the bank
    """

    bank_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankName"),
        pydantic.Field(alias="bankName", description="Name of the bank"),
    ] = None
    """
    Name of the bank
    """

    bank_post_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankPostCode"),
        pydantic.Field(alias="bankPostCode", description="Post code of the bank"),
    ] = None
    """
    Post code of the bank
    """

    bank_state: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankState"),
        pydantic.Field(alias="bankState", description="State of the bank"),
    ] = None
    """
    State of the bank
    """

    transfer_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transferType"),
        pydantic.Field(alias="transferType", description="Transfer type (e.g., swift, ach, wire)"),
    ] = None
    """
    Transfer type (e.g., swift, ach, wire)
    """

    bank_country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bankCountry"),
        pydantic.Field(
            alias="bankCountry", description="Country code of the bank. May be returned alongside bankAccountCountry."
        ),
    ] = None
    """
    Country code of the bank. May be returned alongside bankAccountCountry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bank_account_type import BankAccountType
from .crypto_wallet_info_chain import CryptoWalletInfoChain
from .instapay_info_channel_subject import InstapayInfoChannelSubject
from .instapay_info_extend_info import InstapayInfoExtendInfo
from .swiftpay_pesonet_info_channel_subject import SwiftpayPesonetInfoChannelSubject
from .swiftpay_pesonet_info_extend_info import SwiftpayPesonetInfoExtendInfo


class PaymentMethodData_BankAccount(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["bank_account"] = "bank_account"
    account_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ]
    account_type: typing_extensions.Annotated[
        typing.Optional[BankAccountType], FieldMetadata(alias="accountType"), pydantic.Field(alias="accountType")
    ] = None
    ifsc_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ifscCode"), pydantic.Field(alias="ifscCode")
    ] = None
    bic: typing.Optional[str] = None
    sort_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sortCode"), pydantic.Field(alias="sortCode")
    ] = None
    routing_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="routingNumber"), pydantic.Field(alias="routingNumber")
    ] = None
    branch_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="branchCode"), pydantic.Field(alias="branchCode")
    ] = None
    bsb_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bsbNumber"), pydantic.Field(alias="bsbNumber")
    ] = None
    remittance_purpose: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="remittancePurpose"), pydantic.Field(alias="remittancePurpose")
    ] = None
    transfer_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transferType"), pydantic.Field(alias="transferType")
    ] = None
    bank_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankName"), pydantic.Field(alias="bankName")
    ] = None
    bank_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankAddress"), pydantic.Field(alias="bankAddress")
    ] = None
    bank_city: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankCity"), pydantic.Field(alias="bankCity")
    ] = None
    bank_post_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankPostCode"), pydantic.Field(alias="bankPostCode")
    ] = None
    bank_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankState"), pydantic.Field(alias="bankState")
    ] = None
    bank_document_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankDocumentNumber"), pydantic.Field(alias="bankDocumentNumber")
    ] = None
    bank_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankId"), pydantic.Field(alias="bankId")
    ] = None
    bank_account_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankAccountCountry"), pydantic.Field(alias="bankAccountCountry")
    ] = None
    bank_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bankCountry"), pydantic.Field(alias="bankCountry")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentMethodData_Pix(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["pix"] = "pix"
    pix_key_id: typing_extensions.Annotated[str, FieldMetadata(alias="pixKeyId"), pydantic.Field(alias="pixKeyId")]
    tax_id: typing_extensions.Annotated[str, FieldMetadata(alias="taxId"), pydantic.Field(alias="taxId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentMethodData_Instapay(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["instapay"] = "instapay"
    channel_subject: typing_extensions.Annotated[
        InstapayInfoChannelSubject, FieldMetadata(alias="channelSubject"), pydantic.Field(alias="channelSubject")
    ]
    extend_info: typing_extensions.Annotated[
        InstapayInfoExtendInfo, FieldMetadata(alias="extendInfo"), pydantic.Field(alias="extendInfo")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentMethodData_SwiftpayPesonet(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["swiftpay_pesonet"] = "swiftpay_pesonet"
    channel_subject: typing_extensions.Annotated[
        SwiftpayPesonetInfoChannelSubject, FieldMetadata(alias="channelSubject"), pydantic.Field(alias="channelSubject")
    ]
    extend_info: typing_extensions.Annotated[
        SwiftpayPesonetInfoExtendInfo, FieldMetadata(alias="extendInfo"), pydantic.Field(alias="extendInfo")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentMethodData_Spei(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["spei"] = "spei"
    target_name: typing_extensions.Annotated[str, FieldMetadata(alias="targetName"), pydantic.Field(alias="targetName")]
    target_last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetLastName"), pydantic.Field(alias="targetLastName")
    ] = None
    target_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetEmail"), pydantic.Field(alias="targetEmail")
    ] = None
    target_document: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetDocument"), pydantic.Field(alias="targetDocument")
    ] = None
    target_bank_account_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="targetBankAccountId"), pydantic.Field(alias="targetBankAccountId")
    ]
    target_bank_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetBankName"), pydantic.Field(alias="targetBankName")
    ] = None
    target_bank_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetBankCode"), pydantic.Field(alias="targetBankCode")
    ] = None
    target_bank_branch_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetBankBranchId"), pydantic.Field(alias="targetBankBranchId")
    ] = None
    target_bank_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetBankId"), pydantic.Field(alias="targetBankId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentMethodData_MobileMoney(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["mobile_money"] = "mobile_money"
    phone: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentMethodData_CryptoWallet(UniversalBaseModel):
    """
    Payment method data. Structure depends on type field.
    """

    type: typing.Literal["crypto_wallet"] = "crypto_wallet"
    address: str
    chain: CryptoWalletInfoChain

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PaymentMethodData = typing_extensions.Annotated[
    typing.Union[
        PaymentMethodData_BankAccount,
        PaymentMethodData_Pix,
        PaymentMethodData_Instapay,
        PaymentMethodData_SwiftpayPesonet,
        PaymentMethodData_Spei,
        PaymentMethodData_MobileMoney,
        PaymentMethodData_CryptoWallet,
    ],
    pydantic.Field(discriminator="type"),
]

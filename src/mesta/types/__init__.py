
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .associate_selfie_verification_envelope import AssociateSelfieVerificationEnvelope
    from .associate_selfie_verification_envelope_data import AssociateSelfieVerificationEnvelopeData
    from .bad_request_error_body import BadRequestErrorBody
    from .bank_account import BankAccount
    from .bank_account_info import BankAccountInfo
    from .bank_account_type import BankAccountType
    from .beneficiary_relationship import BeneficiaryRelationship
    from .business_beneficiary import BusinessBeneficiary
    from .business_beneficiary_address import BusinessBeneficiaryAddress
    from .business_beneficiary_business_type import BusinessBeneficiaryBusinessType
    from .business_beneficiary_identity import BusinessBeneficiaryIdentity
    from .business_beneficiary_identity_document_type import BusinessBeneficiaryIdentityDocumentType
    from .business_beneficiary_payment_info import BusinessBeneficiaryPaymentInfo
    from .business_beneficiary_payment_type import BusinessBeneficiaryPaymentType
    from .business_beneficiary_type import BusinessBeneficiaryType
    from .business_sender import BusinessSender
    from .business_sender_business_type import BusinessSenderBusinessType
    from .business_sender_type import BusinessSenderType
    from .business_sender_v2 import BusinessSenderV2
    from .business_sender_v2number_of_employees import BusinessSenderV2NumberOfEmployees
    from .create_sandbox_session_request import CreateSandboxSessionRequest
    from .create_sandbox_session_request_deposit_source import CreateSandboxSessionRequestDepositSource
    from .crypto_wallet_info import CryptoWalletInfo
    from .crypto_wallet_info_chain import CryptoWalletInfoChain
    from .document_type import DocumentType
    from .error_response import ErrorResponse
    from .error_response_error import ErrorResponseError
    from .fiat_deposit_detail import FiatDepositDetail
    from .fiat_deposit_detail_currency import FiatDepositDetailCurrency
    from .fiat_deposit_detail_deposit_details import FiatDepositDetailDepositDetails
    from .fiat_deposit_detail_deposit_details_routing_codes_item import FiatDepositDetailDepositDetailsRoutingCodesItem
    from .fiat_deposit_list_item import FiatDepositListItem
    from .fiat_deposit_list_item_currency import FiatDepositListItemCurrency
    from .forbidden_error_body import ForbiddenErrorBody
    from .individual_beneficiary import IndividualBeneficiary
    from .individual_beneficiary_address import IndividualBeneficiaryAddress
    from .individual_beneficiary_identity import IndividualBeneficiaryIdentity
    from .individual_beneficiary_identity_document_type import IndividualBeneficiaryIdentityDocumentType
    from .individual_beneficiary_payment_info import IndividualBeneficiaryPaymentInfo
    from .individual_beneficiary_payment_type import IndividualBeneficiaryPaymentType
    from .individual_beneficiary_type import IndividualBeneficiaryType
    from .individual_sender import IndividualSender
    from .individual_sender_gender import IndividualSenderGender
    from .individual_sender_identity import IndividualSenderIdentity
    from .individual_sender_identity_document_type import IndividualSenderIdentityDocumentType
    from .individual_sender_occupation import IndividualSenderOccupation
    from .individual_sender_type import IndividualSenderType
    from .individual_sender_v2 import IndividualSenderV2
    from .instapay_info import InstapayInfo
    from .instapay_info_channel_subject import InstapayInfoChannelSubject
    from .instapay_info_extend_info import InstapayInfoExtendInfo
    from .mobile_money_info import MobileMoneyInfo
    from .not_found_error_body import NotFoundErrorBody
    from .order_document import OrderDocument
    from .order_document_input import OrderDocumentInput
    from .patch_business_sender import PatchBusinessSender
    from .patch_business_sender_business_type import PatchBusinessSenderBusinessType
    from .patch_business_sender_number_of_employees import PatchBusinessSenderNumberOfEmployees
    from .patch_individual_sender import PatchIndividualSender
    from .patch_individual_sender_gender import PatchIndividualSenderGender
    from .patch_individual_sender_identity import PatchIndividualSenderIdentity
    from .patch_sender_associate_address import PatchSenderAssociateAddress
    from .patch_sender_associate_identity import PatchSenderAssociateIdentity
    from .payment_method import PaymentMethod
    from .payment_method_data import (
        PaymentMethodData,
        PaymentMethodData_BankAccount,
        PaymentMethodData_CryptoWallet,
        PaymentMethodData_Instapay,
        PaymentMethodData_MobileMoney,
        PaymentMethodData_Pix,
        PaymentMethodData_Spei,
        PaymentMethodData_SwiftpayPesonet,
    )
    from .payment_method_status import PaymentMethodStatus
    from .payment_method_type import PaymentMethodType
    from .pix_info import PixInfo
    from .public_sender_capability import PublicSenderCapability
    from .purpose import Purpose
    from .purpose_of_payment import PurposeOfPayment
    from .purpose_of_payment_document import PurposeOfPaymentDocument
    from .purpose_of_payment_document_request import PurposeOfPaymentDocumentRequest
    from .sandbox_challenge import SandboxChallenge
    from .sandbox_challenge_algorithm import SandboxChallengeAlgorithm
    from .sandbox_challenge_solution import SandboxChallengeSolution
    from .sandbox_challenge_used_error import SandboxChallengeUsedError
    from .sandbox_challenge_used_error_error import SandboxChallengeUsedErrorError
    from .sandbox_challenge_used_error_error_code import SandboxChallengeUsedErrorErrorCode
    from .sandbox_challenge_used_error_response import SandboxChallengeUsedErrorResponse
    from .sandbox_claim_email_owns_sandbox_error import SandboxClaimEmailOwnsSandboxError
    from .sandbox_claim_email_owns_sandbox_error_error import SandboxClaimEmailOwnsSandboxErrorError
    from .sandbox_claim_email_owns_sandbox_error_error_code import SandboxClaimEmailOwnsSandboxErrorErrorCode
    from .sandbox_claim_request import SandboxClaimRequest
    from .sandbox_claim_status import SandboxClaimStatus
    from .sandbox_claim_status_details import SandboxClaimStatusDetails
    from .sandbox_claim_status_details_counts import SandboxClaimStatusDetailsCounts
    from .sandbox_claim_status_details_pre_claim_endpoints_item import SandboxClaimStatusDetailsPreClaimEndpointsItem
    from .sandbox_claim_status_details_pre_claim_keys_item import SandboxClaimStatusDetailsPreClaimKeysItem
    from .sandbox_claim_status_details_pre_claim_keys_item_kind import SandboxClaimStatusDetailsPreClaimKeysItemKind
    from .sandbox_claim_status_details_seed import SandboxClaimStatusDetailsSeed
    from .sandbox_claim_status_details_seed_step import SandboxClaimStatusDetailsSeedStep
    from .sandbox_claim_status_details_status import SandboxClaimStatusDetailsStatus
    from .sandbox_claim_status_request import SandboxClaimStatusRequest
    from .sandbox_claim_status_status import SandboxClaimStatusStatus
    from .sandbox_claim_status_status_status import SandboxClaimStatusStatusStatus
    from .sandbox_claim_status_zero import SandboxClaimStatusZero
    from .sandbox_claim_status_zero_status import SandboxClaimStatusZeroStatus
    from .sandbox_claimed import SandboxClaimed
    from .sandbox_claimed_seed import SandboxClaimedSeed
    from .sandbox_claimed_seed_status import SandboxClaimedSeedStatus
    from .sandbox_code_sent import SandboxCodeSent
    from .sandbox_counts import SandboxCounts
    from .sandbox_created import SandboxCreated
    from .sandbox_created_docs import SandboxCreatedDocs
    from .sandbox_created_plane import SandboxCreatedPlane
    from .sandbox_deposit_source_error import SandboxDepositSourceError
    from .sandbox_deposit_source_error_error import SandboxDepositSourceErrorError
    from .sandbox_deposit_source_error_error_code import SandboxDepositSourceErrorErrorCode
    from .sandbox_email_verified import SandboxEmailVerified
    from .sandbox_fixtures import SandboxFixtures
    from .sandbox_fixtures_balances_item import SandboxFixturesBalancesItem
    from .sandbox_fixtures_beneficiaries_item import SandboxFixturesBeneficiariesItem
    from .sandbox_fixtures_deposit_source import SandboxFixturesDepositSource
    from .sandbox_fixtures_magic_values_item import SandboxFixturesMagicValuesItem
    from .sandbox_fixtures_orders_item import SandboxFixturesOrdersItem
    from .sandbox_fixtures_orders_item_status import SandboxFixturesOrdersItemStatus
    from .sandbox_fixtures_senders_item import SandboxFixturesSendersItem
    from .sandbox_fixtures_webhook import SandboxFixturesWebhook
    from .sandbox_key import SandboxKey
    from .sandbox_key_kind import SandboxKeyKind
    from .sandbox_key_metadata import SandboxKeyMetadata
    from .sandbox_key_metadata_kind import SandboxKeyMetadataKind
    from .sandbox_machine_created import SandboxMachineCreated
    from .sandbox_machine_created_claim import SandboxMachineCreatedClaim
    from .sandbox_machine_created_seed import SandboxMachineCreatedSeed
    from .sandbox_machine_created_seed_status import SandboxMachineCreatedSeedStatus
    from .sandbox_machine_created_status import SandboxMachineCreatedStatus
    from .sandbox_not_open_error import SandboxNotOpenError
    from .sandbox_not_open_error_error import SandboxNotOpenErrorError
    from .sandbox_not_open_error_error_code import SandboxNotOpenErrorErrorCode
    from .sandbox_owner_created import SandboxOwnerCreated
    from .sandbox_owner_created_session import SandboxOwnerCreatedSession
    from .sandbox_owner_created_status import SandboxOwnerCreatedStatus
    from .sandbox_production_request import SandboxProductionRequest
    from .sandbox_production_request_volume_band import SandboxProductionRequestVolumeBand
    from .sandbox_production_requested import SandboxProductionRequested
    from .sandbox_production_requested_status import SandboxProductionRequestedStatus
    from .sandbox_provisioning_paused_error import SandboxProvisioningPausedError
    from .sandbox_provisioning_paused_error_error import SandboxProvisioningPausedErrorError
    from .sandbox_provisioning_paused_error_error_code import SandboxProvisioningPausedErrorErrorCode
    from .sandbox_reset_accepted import SandboxResetAccepted
    from .sandbox_reset_accepted_status import SandboxResetAcceptedStatus
    from .sandbox_seed import SandboxSeed
    from .sandbox_seed_current_step import SandboxSeedCurrentStep
    from .sandbox_seed_error import SandboxSeedError
    from .sandbox_seed_error_code import SandboxSeedErrorCode
    from .sandbox_seed_error_step import SandboxSeedErrorStep
    from .sandbox_seed_pointer import SandboxSeedPointer
    from .sandbox_seed_pointer_status import SandboxSeedPointerStatus
    from .sandbox_seed_status import SandboxSeedStatus
    from .sandbox_seed_step import SandboxSeedStep
    from .sandbox_seed_step_name import SandboxSeedStepName
    from .sandbox_seed_step_status import SandboxSeedStepStatus
    from .sandbox_session import SandboxSession
    from .sandbox_session_plane import SandboxSessionPlane
    from .sandbox_session_production_request import SandboxSessionProductionRequest
    from .sandbox_session_production_request_status import SandboxSessionProductionRequestStatus
    from .sandbox_session_reset import SandboxSessionReset
    from .sandbox_session_reset_error import SandboxSessionResetError
    from .sandbox_session_reset_recovery_item import SandboxSessionResetRecoveryItem
    from .sandbox_session_status import SandboxSessionStatus
    from .sandbox_session_wallets import SandboxSessionWallets
    from .sandbox_session_wallets_reason import SandboxSessionWalletsReason
    from .sandbox_session_wallets_senders import SandboxSessionWalletsSenders
    from .sandbox_session_wallets_senders_items_item import SandboxSessionWalletsSendersItemsItem
    from .sandbox_session_wallets_senders_items_item_status import SandboxSessionWalletsSendersItemsItemStatus
    from .sandbox_session_wallets_status import SandboxSessionWalletsStatus
    from .sandbox_signup_created import SandboxSignupCreated
    from .sandbox_signup_created_seed import SandboxSignupCreatedSeed
    from .sandbox_signup_created_seed_status import SandboxSignupCreatedSeedStatus
    from .sandbox_signup_request import SandboxSignupRequest
    from .sandbox_signup_request_from import SandboxSignupRequestFrom
    from .sandbox_terms import SandboxTerms
    from .sandbox_terms_not_accepted_error import SandboxTermsNotAcceptedError
    from .sandbox_terms_not_accepted_error_error import SandboxTermsNotAcceptedErrorError
    from .sandbox_terms_not_accepted_error_error_code import SandboxTermsNotAcceptedErrorErrorCode
    from .sandbox_terms_not_accepted_error_terms import SandboxTermsNotAcceptedErrorTerms
    from .sandbox_throttle_error_response import SandboxThrottleErrorResponse
    from .sandbox_throttle_error_response_error import SandboxThrottleErrorResponseError
    from .sandbox_throttle_error_response_error_details import SandboxThrottleErrorResponseErrorDetails
    from .sandbox_throttle_error_response_error_details_retry_after_ms import (
        SandboxThrottleErrorResponseErrorDetailsRetryAfterMs,
    )
    from .sandbox_verification_error_response import SandboxVerificationErrorResponse
    from .sandbox_verification_error_response_error import SandboxVerificationErrorResponseError
    from .sandbox_verification_error_response_error_code import SandboxVerificationErrorResponseErrorCode
    from .sandbox_verification_error_response_error_details import SandboxVerificationErrorResponseErrorDetails
    from .sandbox_verify_email_request import SandboxVerifyEmailRequest
    from .sandbox_wallet import SandboxWallet
    from .sandbox_wallets_response import SandboxWalletsResponse
    from .selfie_verification_session import SelfieVerificationSession
    from .selfie_verification_session_status import SelfieVerificationSessionStatus
    from .sender_associate import SenderAssociate
    from .sender_associate_address import SenderAssociateAddress
    from .sender_associate_envelope import SenderAssociateEnvelope
    from .sender_associate_identity_input import SenderAssociateIdentityInput
    from .sender_associate_kyc import SenderAssociateKyc
    from .sender_associate_kyc_status import SenderAssociateKycStatus
    from .sender_associate_list_envelope import SenderAssociateListEnvelope
    from .sender_associate_role import SenderAssociateRole
    from .sender_onboarding_info import SenderOnboardingInfo
    from .sender_onboarding_info_nature_of_payments_item import SenderOnboardingInfoNatureOfPaymentsItem
    from .sender_onboarding_info_number_of_employees import SenderOnboardingInfoNumberOfEmployees
    from .sender_onboarding_info_source_of_funds import SenderOnboardingInfoSourceOfFunds
    from .sender_v2common_onboarding import SenderV2CommonOnboarding
    from .sender_v2common_onboarding_nature_of_payments_item import SenderV2CommonOnboardingNatureOfPaymentsItem
    from .sender_v2common_onboarding_source_of_funds import SenderV2CommonOnboardingSourceOfFunds
    from .sender_virtual_account import SenderVirtualAccount
    from .sender_virtual_account_bank_details import SenderVirtualAccountBankDetails
    from .sender_virtual_account_currency import SenderVirtualAccountCurrency
    from .sender_virtual_accounts_envelope import SenderVirtualAccountsEnvelope
    from .simulate_deposit_response import SimulateDepositResponse
    from .simulate_deposit_response_data import SimulateDepositResponseData
    from .simulate_deposit_response_data_outcome import SimulateDepositResponseDataOutcome
    from .simulate_deposit_response_data_owner_type import SimulateDepositResponseDataOwnerType
    from .simulate_order_transition_response import SimulateOrderTransitionResponse
    from .simulate_order_transition_response_data import SimulateOrderTransitionResponseData
    from .simulate_order_transition_response_data_status import SimulateOrderTransitionResponseDataStatus
    from .simulate_tos_accept_response import SimulateTosAcceptResponse
    from .simulate_tos_accept_response_data import SimulateTosAcceptResponseData
    from .simulate_tos_accept_response_data_tos import SimulateTosAcceptResponseDataTos
    from .simulate_tos_accept_response_data_tos_status import SimulateTosAcceptResponseDataTosStatus
    from .simulate_webhook_fire_response import SimulateWebhookFireResponse
    from .simulate_webhook_fire_response_data import SimulateWebhookFireResponseData
    from .source_address_input import SourceAddressInput
    from .source_of_funds import SourceOfFunds
    from .spei_info import SpeiInfo
    from .stablecoin_deposit import StablecoinDeposit
    from .stablecoin_deposit_status import StablecoinDepositStatus
    from .swiftpay_pesonet_info import SwiftpayPesonetInfo
    from .swiftpay_pesonet_info_channel_subject import SwiftpayPesonetInfoChannelSubject
    from .swiftpay_pesonet_info_extend_info import SwiftpayPesonetInfoExtendInfo
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .too_many_requests_error_body_error import TooManyRequestsErrorBodyError
    from .too_many_requests_error_body_error_details import TooManyRequestsErrorBodyErrorDetails
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .validation_field import ValidationField
    from .verify_sender_requirements_blocker import VerifySenderRequirementsBlocker
    from .verify_sender_requirements_blocker_action import VerifySenderRequirementsBlockerAction
    from .verify_sender_requirements_blocker_action_method import VerifySenderRequirementsBlockerActionMethod
    from .verify_sender_requirements_blocker_code import VerifySenderRequirementsBlockerCode
    from .verify_sender_requirements_blocker_fields_item import VerifySenderRequirementsBlockerFieldsItem
    from .verify_sender_requirements_blocker_fields_item_document_type import (
        VerifySenderRequirementsBlockerFieldsItemDocumentType,
    )
    from .verify_sender_requirements_blocker_subject import VerifySenderRequirementsBlockerSubject
    from .verify_sender_requirements_blocker_subject_type import VerifySenderRequirementsBlockerSubjectType
    from .verify_sender_requirements_missing_error import VerifySenderRequirementsMissingError
    from .verify_sender_requirements_missing_error_error import VerifySenderRequirementsMissingErrorError
    from .verify_sender_requirements_missing_error_error_code import VerifySenderRequirementsMissingErrorErrorCode
    from .virtual_account_setup_action import VirtualAccountSetupAction
    from .virtual_account_setup_action_method import VirtualAccountSetupActionMethod
    from .virtual_account_setup_blocker import VirtualAccountSetupBlocker
    from .virtual_account_setup_blocker_code import VirtualAccountSetupBlockerCode
    from .virtual_account_setup_blocker_fields_item import VirtualAccountSetupBlockerFieldsItem
    from .virtual_account_setup_blocker_fields_item_document_type import (
        VirtualAccountSetupBlockerFieldsItemDocumentType,
    )
    from .virtual_account_setup_blocker_subject import VirtualAccountSetupBlockerSubject
    from .virtual_account_setup_blocker_subject_type import VirtualAccountSetupBlockerSubjectType
    from .virtual_account_setup_envelope import VirtualAccountSetupEnvelope
    from .virtual_account_setup_response import VirtualAccountSetupResponse
    from .virtual_account_setup_response_currency import VirtualAccountSetupResponseCurrency
    from .virtual_account_setup_response_unaccepted_fields_item import VirtualAccountSetupResponseUnacceptedFieldsItem
    from .virtual_account_setup_status import VirtualAccountSetupStatus
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AssociateSelfieVerificationEnvelope": ".associate_selfie_verification_envelope",
    "AssociateSelfieVerificationEnvelopeData": ".associate_selfie_verification_envelope_data",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BankAccount": ".bank_account",
    "BankAccountInfo": ".bank_account_info",
    "BankAccountType": ".bank_account_type",
    "BeneficiaryRelationship": ".beneficiary_relationship",
    "BusinessBeneficiary": ".business_beneficiary",
    "BusinessBeneficiaryAddress": ".business_beneficiary_address",
    "BusinessBeneficiaryBusinessType": ".business_beneficiary_business_type",
    "BusinessBeneficiaryIdentity": ".business_beneficiary_identity",
    "BusinessBeneficiaryIdentityDocumentType": ".business_beneficiary_identity_document_type",
    "BusinessBeneficiaryPaymentInfo": ".business_beneficiary_payment_info",
    "BusinessBeneficiaryPaymentType": ".business_beneficiary_payment_type",
    "BusinessBeneficiaryType": ".business_beneficiary_type",
    "BusinessSender": ".business_sender",
    "BusinessSenderBusinessType": ".business_sender_business_type",
    "BusinessSenderType": ".business_sender_type",
    "BusinessSenderV2": ".business_sender_v2",
    "BusinessSenderV2NumberOfEmployees": ".business_sender_v2number_of_employees",
    "CreateSandboxSessionRequest": ".create_sandbox_session_request",
    "CreateSandboxSessionRequestDepositSource": ".create_sandbox_session_request_deposit_source",
    "CryptoWalletInfo": ".crypto_wallet_info",
    "CryptoWalletInfoChain": ".crypto_wallet_info_chain",
    "DocumentType": ".document_type",
    "ErrorResponse": ".error_response",
    "ErrorResponseError": ".error_response_error",
    "FiatDepositDetail": ".fiat_deposit_detail",
    "FiatDepositDetailCurrency": ".fiat_deposit_detail_currency",
    "FiatDepositDetailDepositDetails": ".fiat_deposit_detail_deposit_details",
    "FiatDepositDetailDepositDetailsRoutingCodesItem": ".fiat_deposit_detail_deposit_details_routing_codes_item",
    "FiatDepositListItem": ".fiat_deposit_list_item",
    "FiatDepositListItemCurrency": ".fiat_deposit_list_item_currency",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "IndividualBeneficiary": ".individual_beneficiary",
    "IndividualBeneficiaryAddress": ".individual_beneficiary_address",
    "IndividualBeneficiaryIdentity": ".individual_beneficiary_identity",
    "IndividualBeneficiaryIdentityDocumentType": ".individual_beneficiary_identity_document_type",
    "IndividualBeneficiaryPaymentInfo": ".individual_beneficiary_payment_info",
    "IndividualBeneficiaryPaymentType": ".individual_beneficiary_payment_type",
    "IndividualBeneficiaryType": ".individual_beneficiary_type",
    "IndividualSender": ".individual_sender",
    "IndividualSenderGender": ".individual_sender_gender",
    "IndividualSenderIdentity": ".individual_sender_identity",
    "IndividualSenderIdentityDocumentType": ".individual_sender_identity_document_type",
    "IndividualSenderOccupation": ".individual_sender_occupation",
    "IndividualSenderType": ".individual_sender_type",
    "IndividualSenderV2": ".individual_sender_v2",
    "InstapayInfo": ".instapay_info",
    "InstapayInfoChannelSubject": ".instapay_info_channel_subject",
    "InstapayInfoExtendInfo": ".instapay_info_extend_info",
    "MobileMoneyInfo": ".mobile_money_info",
    "NotFoundErrorBody": ".not_found_error_body",
    "OrderDocument": ".order_document",
    "OrderDocumentInput": ".order_document_input",
    "PatchBusinessSender": ".patch_business_sender",
    "PatchBusinessSenderBusinessType": ".patch_business_sender_business_type",
    "PatchBusinessSenderNumberOfEmployees": ".patch_business_sender_number_of_employees",
    "PatchIndividualSender": ".patch_individual_sender",
    "PatchIndividualSenderGender": ".patch_individual_sender_gender",
    "PatchIndividualSenderIdentity": ".patch_individual_sender_identity",
    "PatchSenderAssociateAddress": ".patch_sender_associate_address",
    "PatchSenderAssociateIdentity": ".patch_sender_associate_identity",
    "PaymentMethod": ".payment_method",
    "PaymentMethodData": ".payment_method_data",
    "PaymentMethodData_BankAccount": ".payment_method_data",
    "PaymentMethodData_CryptoWallet": ".payment_method_data",
    "PaymentMethodData_Instapay": ".payment_method_data",
    "PaymentMethodData_MobileMoney": ".payment_method_data",
    "PaymentMethodData_Pix": ".payment_method_data",
    "PaymentMethodData_Spei": ".payment_method_data",
    "PaymentMethodData_SwiftpayPesonet": ".payment_method_data",
    "PaymentMethodStatus": ".payment_method_status",
    "PaymentMethodType": ".payment_method_type",
    "PixInfo": ".pix_info",
    "PublicSenderCapability": ".public_sender_capability",
    "Purpose": ".purpose",
    "PurposeOfPayment": ".purpose_of_payment",
    "PurposeOfPaymentDocument": ".purpose_of_payment_document",
    "PurposeOfPaymentDocumentRequest": ".purpose_of_payment_document_request",
    "SandboxChallenge": ".sandbox_challenge",
    "SandboxChallengeAlgorithm": ".sandbox_challenge_algorithm",
    "SandboxChallengeSolution": ".sandbox_challenge_solution",
    "SandboxChallengeUsedError": ".sandbox_challenge_used_error",
    "SandboxChallengeUsedErrorError": ".sandbox_challenge_used_error_error",
    "SandboxChallengeUsedErrorErrorCode": ".sandbox_challenge_used_error_error_code",
    "SandboxChallengeUsedErrorResponse": ".sandbox_challenge_used_error_response",
    "SandboxClaimEmailOwnsSandboxError": ".sandbox_claim_email_owns_sandbox_error",
    "SandboxClaimEmailOwnsSandboxErrorError": ".sandbox_claim_email_owns_sandbox_error_error",
    "SandboxClaimEmailOwnsSandboxErrorErrorCode": ".sandbox_claim_email_owns_sandbox_error_error_code",
    "SandboxClaimRequest": ".sandbox_claim_request",
    "SandboxClaimStatus": ".sandbox_claim_status",
    "SandboxClaimStatusDetails": ".sandbox_claim_status_details",
    "SandboxClaimStatusDetailsCounts": ".sandbox_claim_status_details_counts",
    "SandboxClaimStatusDetailsPreClaimEndpointsItem": ".sandbox_claim_status_details_pre_claim_endpoints_item",
    "SandboxClaimStatusDetailsPreClaimKeysItem": ".sandbox_claim_status_details_pre_claim_keys_item",
    "SandboxClaimStatusDetailsPreClaimKeysItemKind": ".sandbox_claim_status_details_pre_claim_keys_item_kind",
    "SandboxClaimStatusDetailsSeed": ".sandbox_claim_status_details_seed",
    "SandboxClaimStatusDetailsSeedStep": ".sandbox_claim_status_details_seed_step",
    "SandboxClaimStatusDetailsStatus": ".sandbox_claim_status_details_status",
    "SandboxClaimStatusRequest": ".sandbox_claim_status_request",
    "SandboxClaimStatusStatus": ".sandbox_claim_status_status",
    "SandboxClaimStatusStatusStatus": ".sandbox_claim_status_status_status",
    "SandboxClaimStatusZero": ".sandbox_claim_status_zero",
    "SandboxClaimStatusZeroStatus": ".sandbox_claim_status_zero_status",
    "SandboxClaimed": ".sandbox_claimed",
    "SandboxClaimedSeed": ".sandbox_claimed_seed",
    "SandboxClaimedSeedStatus": ".sandbox_claimed_seed_status",
    "SandboxCodeSent": ".sandbox_code_sent",
    "SandboxCounts": ".sandbox_counts",
    "SandboxCreated": ".sandbox_created",
    "SandboxCreatedDocs": ".sandbox_created_docs",
    "SandboxCreatedPlane": ".sandbox_created_plane",
    "SandboxDepositSourceError": ".sandbox_deposit_source_error",
    "SandboxDepositSourceErrorError": ".sandbox_deposit_source_error_error",
    "SandboxDepositSourceErrorErrorCode": ".sandbox_deposit_source_error_error_code",
    "SandboxEmailVerified": ".sandbox_email_verified",
    "SandboxFixtures": ".sandbox_fixtures",
    "SandboxFixturesBalancesItem": ".sandbox_fixtures_balances_item",
    "SandboxFixturesBeneficiariesItem": ".sandbox_fixtures_beneficiaries_item",
    "SandboxFixturesDepositSource": ".sandbox_fixtures_deposit_source",
    "SandboxFixturesMagicValuesItem": ".sandbox_fixtures_magic_values_item",
    "SandboxFixturesOrdersItem": ".sandbox_fixtures_orders_item",
    "SandboxFixturesOrdersItemStatus": ".sandbox_fixtures_orders_item_status",
    "SandboxFixturesSendersItem": ".sandbox_fixtures_senders_item",
    "SandboxFixturesWebhook": ".sandbox_fixtures_webhook",
    "SandboxKey": ".sandbox_key",
    "SandboxKeyKind": ".sandbox_key_kind",
    "SandboxKeyMetadata": ".sandbox_key_metadata",
    "SandboxKeyMetadataKind": ".sandbox_key_metadata_kind",
    "SandboxMachineCreated": ".sandbox_machine_created",
    "SandboxMachineCreatedClaim": ".sandbox_machine_created_claim",
    "SandboxMachineCreatedSeed": ".sandbox_machine_created_seed",
    "SandboxMachineCreatedSeedStatus": ".sandbox_machine_created_seed_status",
    "SandboxMachineCreatedStatus": ".sandbox_machine_created_status",
    "SandboxNotOpenError": ".sandbox_not_open_error",
    "SandboxNotOpenErrorError": ".sandbox_not_open_error_error",
    "SandboxNotOpenErrorErrorCode": ".sandbox_not_open_error_error_code",
    "SandboxOwnerCreated": ".sandbox_owner_created",
    "SandboxOwnerCreatedSession": ".sandbox_owner_created_session",
    "SandboxOwnerCreatedStatus": ".sandbox_owner_created_status",
    "SandboxProductionRequest": ".sandbox_production_request",
    "SandboxProductionRequestVolumeBand": ".sandbox_production_request_volume_band",
    "SandboxProductionRequested": ".sandbox_production_requested",
    "SandboxProductionRequestedStatus": ".sandbox_production_requested_status",
    "SandboxProvisioningPausedError": ".sandbox_provisioning_paused_error",
    "SandboxProvisioningPausedErrorError": ".sandbox_provisioning_paused_error_error",
    "SandboxProvisioningPausedErrorErrorCode": ".sandbox_provisioning_paused_error_error_code",
    "SandboxResetAccepted": ".sandbox_reset_accepted",
    "SandboxResetAcceptedStatus": ".sandbox_reset_accepted_status",
    "SandboxSeed": ".sandbox_seed",
    "SandboxSeedCurrentStep": ".sandbox_seed_current_step",
    "SandboxSeedError": ".sandbox_seed_error",
    "SandboxSeedErrorCode": ".sandbox_seed_error_code",
    "SandboxSeedErrorStep": ".sandbox_seed_error_step",
    "SandboxSeedPointer": ".sandbox_seed_pointer",
    "SandboxSeedPointerStatus": ".sandbox_seed_pointer_status",
    "SandboxSeedStatus": ".sandbox_seed_status",
    "SandboxSeedStep": ".sandbox_seed_step",
    "SandboxSeedStepName": ".sandbox_seed_step_name",
    "SandboxSeedStepStatus": ".sandbox_seed_step_status",
    "SandboxSession": ".sandbox_session",
    "SandboxSessionPlane": ".sandbox_session_plane",
    "SandboxSessionProductionRequest": ".sandbox_session_production_request",
    "SandboxSessionProductionRequestStatus": ".sandbox_session_production_request_status",
    "SandboxSessionReset": ".sandbox_session_reset",
    "SandboxSessionResetError": ".sandbox_session_reset_error",
    "SandboxSessionResetRecoveryItem": ".sandbox_session_reset_recovery_item",
    "SandboxSessionStatus": ".sandbox_session_status",
    "SandboxSessionWallets": ".sandbox_session_wallets",
    "SandboxSessionWalletsReason": ".sandbox_session_wallets_reason",
    "SandboxSessionWalletsSenders": ".sandbox_session_wallets_senders",
    "SandboxSessionWalletsSendersItemsItem": ".sandbox_session_wallets_senders_items_item",
    "SandboxSessionWalletsSendersItemsItemStatus": ".sandbox_session_wallets_senders_items_item_status",
    "SandboxSessionWalletsStatus": ".sandbox_session_wallets_status",
    "SandboxSignupCreated": ".sandbox_signup_created",
    "SandboxSignupCreatedSeed": ".sandbox_signup_created_seed",
    "SandboxSignupCreatedSeedStatus": ".sandbox_signup_created_seed_status",
    "SandboxSignupRequest": ".sandbox_signup_request",
    "SandboxSignupRequestFrom": ".sandbox_signup_request_from",
    "SandboxTerms": ".sandbox_terms",
    "SandboxTermsNotAcceptedError": ".sandbox_terms_not_accepted_error",
    "SandboxTermsNotAcceptedErrorError": ".sandbox_terms_not_accepted_error_error",
    "SandboxTermsNotAcceptedErrorErrorCode": ".sandbox_terms_not_accepted_error_error_code",
    "SandboxTermsNotAcceptedErrorTerms": ".sandbox_terms_not_accepted_error_terms",
    "SandboxThrottleErrorResponse": ".sandbox_throttle_error_response",
    "SandboxThrottleErrorResponseError": ".sandbox_throttle_error_response_error",
    "SandboxThrottleErrorResponseErrorDetails": ".sandbox_throttle_error_response_error_details",
    "SandboxThrottleErrorResponseErrorDetailsRetryAfterMs": ".sandbox_throttle_error_response_error_details_retry_after_ms",
    "SandboxVerificationErrorResponse": ".sandbox_verification_error_response",
    "SandboxVerificationErrorResponseError": ".sandbox_verification_error_response_error",
    "SandboxVerificationErrorResponseErrorCode": ".sandbox_verification_error_response_error_code",
    "SandboxVerificationErrorResponseErrorDetails": ".sandbox_verification_error_response_error_details",
    "SandboxVerifyEmailRequest": ".sandbox_verify_email_request",
    "SandboxWallet": ".sandbox_wallet",
    "SandboxWalletsResponse": ".sandbox_wallets_response",
    "SelfieVerificationSession": ".selfie_verification_session",
    "SelfieVerificationSessionStatus": ".selfie_verification_session_status",
    "SenderAssociate": ".sender_associate",
    "SenderAssociateAddress": ".sender_associate_address",
    "SenderAssociateEnvelope": ".sender_associate_envelope",
    "SenderAssociateIdentityInput": ".sender_associate_identity_input",
    "SenderAssociateKyc": ".sender_associate_kyc",
    "SenderAssociateKycStatus": ".sender_associate_kyc_status",
    "SenderAssociateListEnvelope": ".sender_associate_list_envelope",
    "SenderAssociateRole": ".sender_associate_role",
    "SenderOnboardingInfo": ".sender_onboarding_info",
    "SenderOnboardingInfoNatureOfPaymentsItem": ".sender_onboarding_info_nature_of_payments_item",
    "SenderOnboardingInfoNumberOfEmployees": ".sender_onboarding_info_number_of_employees",
    "SenderOnboardingInfoSourceOfFunds": ".sender_onboarding_info_source_of_funds",
    "SenderV2CommonOnboarding": ".sender_v2common_onboarding",
    "SenderV2CommonOnboardingNatureOfPaymentsItem": ".sender_v2common_onboarding_nature_of_payments_item",
    "SenderV2CommonOnboardingSourceOfFunds": ".sender_v2common_onboarding_source_of_funds",
    "SenderVirtualAccount": ".sender_virtual_account",
    "SenderVirtualAccountBankDetails": ".sender_virtual_account_bank_details",
    "SenderVirtualAccountCurrency": ".sender_virtual_account_currency",
    "SenderVirtualAccountsEnvelope": ".sender_virtual_accounts_envelope",
    "SimulateDepositResponse": ".simulate_deposit_response",
    "SimulateDepositResponseData": ".simulate_deposit_response_data",
    "SimulateDepositResponseDataOutcome": ".simulate_deposit_response_data_outcome",
    "SimulateDepositResponseDataOwnerType": ".simulate_deposit_response_data_owner_type",
    "SimulateOrderTransitionResponse": ".simulate_order_transition_response",
    "SimulateOrderTransitionResponseData": ".simulate_order_transition_response_data",
    "SimulateOrderTransitionResponseDataStatus": ".simulate_order_transition_response_data_status",
    "SimulateTosAcceptResponse": ".simulate_tos_accept_response",
    "SimulateTosAcceptResponseData": ".simulate_tos_accept_response_data",
    "SimulateTosAcceptResponseDataTos": ".simulate_tos_accept_response_data_tos",
    "SimulateTosAcceptResponseDataTosStatus": ".simulate_tos_accept_response_data_tos_status",
    "SimulateWebhookFireResponse": ".simulate_webhook_fire_response",
    "SimulateWebhookFireResponseData": ".simulate_webhook_fire_response_data",
    "SourceAddressInput": ".source_address_input",
    "SourceOfFunds": ".source_of_funds",
    "SpeiInfo": ".spei_info",
    "StablecoinDeposit": ".stablecoin_deposit",
    "StablecoinDepositStatus": ".stablecoin_deposit_status",
    "SwiftpayPesonetInfo": ".swiftpay_pesonet_info",
    "SwiftpayPesonetInfoChannelSubject": ".swiftpay_pesonet_info_channel_subject",
    "SwiftpayPesonetInfoExtendInfo": ".swiftpay_pesonet_info_extend_info",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "TooManyRequestsErrorBodyError": ".too_many_requests_error_body_error",
    "TooManyRequestsErrorBodyErrorDetails": ".too_many_requests_error_body_error_details",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "ValidationField": ".validation_field",
    "VerifySenderRequirementsBlocker": ".verify_sender_requirements_blocker",
    "VerifySenderRequirementsBlockerAction": ".verify_sender_requirements_blocker_action",
    "VerifySenderRequirementsBlockerActionMethod": ".verify_sender_requirements_blocker_action_method",
    "VerifySenderRequirementsBlockerCode": ".verify_sender_requirements_blocker_code",
    "VerifySenderRequirementsBlockerFieldsItem": ".verify_sender_requirements_blocker_fields_item",
    "VerifySenderRequirementsBlockerFieldsItemDocumentType": ".verify_sender_requirements_blocker_fields_item_document_type",
    "VerifySenderRequirementsBlockerSubject": ".verify_sender_requirements_blocker_subject",
    "VerifySenderRequirementsBlockerSubjectType": ".verify_sender_requirements_blocker_subject_type",
    "VerifySenderRequirementsMissingError": ".verify_sender_requirements_missing_error",
    "VerifySenderRequirementsMissingErrorError": ".verify_sender_requirements_missing_error_error",
    "VerifySenderRequirementsMissingErrorErrorCode": ".verify_sender_requirements_missing_error_error_code",
    "VirtualAccountSetupAction": ".virtual_account_setup_action",
    "VirtualAccountSetupActionMethod": ".virtual_account_setup_action_method",
    "VirtualAccountSetupBlocker": ".virtual_account_setup_blocker",
    "VirtualAccountSetupBlockerCode": ".virtual_account_setup_blocker_code",
    "VirtualAccountSetupBlockerFieldsItem": ".virtual_account_setup_blocker_fields_item",
    "VirtualAccountSetupBlockerFieldsItemDocumentType": ".virtual_account_setup_blocker_fields_item_document_type",
    "VirtualAccountSetupBlockerSubject": ".virtual_account_setup_blocker_subject",
    "VirtualAccountSetupBlockerSubjectType": ".virtual_account_setup_blocker_subject_type",
    "VirtualAccountSetupEnvelope": ".virtual_account_setup_envelope",
    "VirtualAccountSetupResponse": ".virtual_account_setup_response",
    "VirtualAccountSetupResponseCurrency": ".virtual_account_setup_response_currency",
    "VirtualAccountSetupResponseUnacceptedFieldsItem": ".virtual_account_setup_response_unaccepted_fields_item",
    "VirtualAccountSetupStatus": ".virtual_account_setup_status",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Address",
    "AssociateSelfieVerificationEnvelope",
    "AssociateSelfieVerificationEnvelopeData",
    "BadRequestErrorBody",
    "BankAccount",
    "BankAccountInfo",
    "BankAccountType",
    "BeneficiaryRelationship",
    "BusinessBeneficiary",
    "BusinessBeneficiaryAddress",
    "BusinessBeneficiaryBusinessType",
    "BusinessBeneficiaryIdentity",
    "BusinessBeneficiaryIdentityDocumentType",
    "BusinessBeneficiaryPaymentInfo",
    "BusinessBeneficiaryPaymentType",
    "BusinessBeneficiaryType",
    "BusinessSender",
    "BusinessSenderBusinessType",
    "BusinessSenderType",
    "BusinessSenderV2",
    "BusinessSenderV2NumberOfEmployees",
    "CreateSandboxSessionRequest",
    "CreateSandboxSessionRequestDepositSource",
    "CryptoWalletInfo",
    "CryptoWalletInfoChain",
    "DocumentType",
    "ErrorResponse",
    "ErrorResponseError",
    "FiatDepositDetail",
    "FiatDepositDetailCurrency",
    "FiatDepositDetailDepositDetails",
    "FiatDepositDetailDepositDetailsRoutingCodesItem",
    "FiatDepositListItem",
    "FiatDepositListItemCurrency",
    "ForbiddenErrorBody",
    "IndividualBeneficiary",
    "IndividualBeneficiaryAddress",
    "IndividualBeneficiaryIdentity",
    "IndividualBeneficiaryIdentityDocumentType",
    "IndividualBeneficiaryPaymentInfo",
    "IndividualBeneficiaryPaymentType",
    "IndividualBeneficiaryType",
    "IndividualSender",
    "IndividualSenderGender",
    "IndividualSenderIdentity",
    "IndividualSenderIdentityDocumentType",
    "IndividualSenderOccupation",
    "IndividualSenderType",
    "IndividualSenderV2",
    "InstapayInfo",
    "InstapayInfoChannelSubject",
    "InstapayInfoExtendInfo",
    "MobileMoneyInfo",
    "NotFoundErrorBody",
    "OrderDocument",
    "OrderDocumentInput",
    "PatchBusinessSender",
    "PatchBusinessSenderBusinessType",
    "PatchBusinessSenderNumberOfEmployees",
    "PatchIndividualSender",
    "PatchIndividualSenderGender",
    "PatchIndividualSenderIdentity",
    "PatchSenderAssociateAddress",
    "PatchSenderAssociateIdentity",
    "PaymentMethod",
    "PaymentMethodData",
    "PaymentMethodData_BankAccount",
    "PaymentMethodData_CryptoWallet",
    "PaymentMethodData_Instapay",
    "PaymentMethodData_MobileMoney",
    "PaymentMethodData_Pix",
    "PaymentMethodData_Spei",
    "PaymentMethodData_SwiftpayPesonet",
    "PaymentMethodStatus",
    "PaymentMethodType",
    "PixInfo",
    "PublicSenderCapability",
    "Purpose",
    "PurposeOfPayment",
    "PurposeOfPaymentDocument",
    "PurposeOfPaymentDocumentRequest",
    "SandboxChallenge",
    "SandboxChallengeAlgorithm",
    "SandboxChallengeSolution",
    "SandboxChallengeUsedError",
    "SandboxChallengeUsedErrorError",
    "SandboxChallengeUsedErrorErrorCode",
    "SandboxChallengeUsedErrorResponse",
    "SandboxClaimEmailOwnsSandboxError",
    "SandboxClaimEmailOwnsSandboxErrorError",
    "SandboxClaimEmailOwnsSandboxErrorErrorCode",
    "SandboxClaimRequest",
    "SandboxClaimStatus",
    "SandboxClaimStatusDetails",
    "SandboxClaimStatusDetailsCounts",
    "SandboxClaimStatusDetailsPreClaimEndpointsItem",
    "SandboxClaimStatusDetailsPreClaimKeysItem",
    "SandboxClaimStatusDetailsPreClaimKeysItemKind",
    "SandboxClaimStatusDetailsSeed",
    "SandboxClaimStatusDetailsSeedStep",
    "SandboxClaimStatusDetailsStatus",
    "SandboxClaimStatusRequest",
    "SandboxClaimStatusStatus",
    "SandboxClaimStatusStatusStatus",
    "SandboxClaimStatusZero",
    "SandboxClaimStatusZeroStatus",
    "SandboxClaimed",
    "SandboxClaimedSeed",
    "SandboxClaimedSeedStatus",
    "SandboxCodeSent",
    "SandboxCounts",
    "SandboxCreated",
    "SandboxCreatedDocs",
    "SandboxCreatedPlane",
    "SandboxDepositSourceError",
    "SandboxDepositSourceErrorError",
    "SandboxDepositSourceErrorErrorCode",
    "SandboxEmailVerified",
    "SandboxFixtures",
    "SandboxFixturesBalancesItem",
    "SandboxFixturesBeneficiariesItem",
    "SandboxFixturesDepositSource",
    "SandboxFixturesMagicValuesItem",
    "SandboxFixturesOrdersItem",
    "SandboxFixturesOrdersItemStatus",
    "SandboxFixturesSendersItem",
    "SandboxFixturesWebhook",
    "SandboxKey",
    "SandboxKeyKind",
    "SandboxKeyMetadata",
    "SandboxKeyMetadataKind",
    "SandboxMachineCreated",
    "SandboxMachineCreatedClaim",
    "SandboxMachineCreatedSeed",
    "SandboxMachineCreatedSeedStatus",
    "SandboxMachineCreatedStatus",
    "SandboxNotOpenError",
    "SandboxNotOpenErrorError",
    "SandboxNotOpenErrorErrorCode",
    "SandboxOwnerCreated",
    "SandboxOwnerCreatedSession",
    "SandboxOwnerCreatedStatus",
    "SandboxProductionRequest",
    "SandboxProductionRequestVolumeBand",
    "SandboxProductionRequested",
    "SandboxProductionRequestedStatus",
    "SandboxProvisioningPausedError",
    "SandboxProvisioningPausedErrorError",
    "SandboxProvisioningPausedErrorErrorCode",
    "SandboxResetAccepted",
    "SandboxResetAcceptedStatus",
    "SandboxSeed",
    "SandboxSeedCurrentStep",
    "SandboxSeedError",
    "SandboxSeedErrorCode",
    "SandboxSeedErrorStep",
    "SandboxSeedPointer",
    "SandboxSeedPointerStatus",
    "SandboxSeedStatus",
    "SandboxSeedStep",
    "SandboxSeedStepName",
    "SandboxSeedStepStatus",
    "SandboxSession",
    "SandboxSessionPlane",
    "SandboxSessionProductionRequest",
    "SandboxSessionProductionRequestStatus",
    "SandboxSessionReset",
    "SandboxSessionResetError",
    "SandboxSessionResetRecoveryItem",
    "SandboxSessionStatus",
    "SandboxSessionWallets",
    "SandboxSessionWalletsReason",
    "SandboxSessionWalletsSenders",
    "SandboxSessionWalletsSendersItemsItem",
    "SandboxSessionWalletsSendersItemsItemStatus",
    "SandboxSessionWalletsStatus",
    "SandboxSignupCreated",
    "SandboxSignupCreatedSeed",
    "SandboxSignupCreatedSeedStatus",
    "SandboxSignupRequest",
    "SandboxSignupRequestFrom",
    "SandboxTerms",
    "SandboxTermsNotAcceptedError",
    "SandboxTermsNotAcceptedErrorError",
    "SandboxTermsNotAcceptedErrorErrorCode",
    "SandboxTermsNotAcceptedErrorTerms",
    "SandboxThrottleErrorResponse",
    "SandboxThrottleErrorResponseError",
    "SandboxThrottleErrorResponseErrorDetails",
    "SandboxThrottleErrorResponseErrorDetailsRetryAfterMs",
    "SandboxVerificationErrorResponse",
    "SandboxVerificationErrorResponseError",
    "SandboxVerificationErrorResponseErrorCode",
    "SandboxVerificationErrorResponseErrorDetails",
    "SandboxVerifyEmailRequest",
    "SandboxWallet",
    "SandboxWalletsResponse",
    "SelfieVerificationSession",
    "SelfieVerificationSessionStatus",
    "SenderAssociate",
    "SenderAssociateAddress",
    "SenderAssociateEnvelope",
    "SenderAssociateIdentityInput",
    "SenderAssociateKyc",
    "SenderAssociateKycStatus",
    "SenderAssociateListEnvelope",
    "SenderAssociateRole",
    "SenderOnboardingInfo",
    "SenderOnboardingInfoNatureOfPaymentsItem",
    "SenderOnboardingInfoNumberOfEmployees",
    "SenderOnboardingInfoSourceOfFunds",
    "SenderV2CommonOnboarding",
    "SenderV2CommonOnboardingNatureOfPaymentsItem",
    "SenderV2CommonOnboardingSourceOfFunds",
    "SenderVirtualAccount",
    "SenderVirtualAccountBankDetails",
    "SenderVirtualAccountCurrency",
    "SenderVirtualAccountsEnvelope",
    "SimulateDepositResponse",
    "SimulateDepositResponseData",
    "SimulateDepositResponseDataOutcome",
    "SimulateDepositResponseDataOwnerType",
    "SimulateOrderTransitionResponse",
    "SimulateOrderTransitionResponseData",
    "SimulateOrderTransitionResponseDataStatus",
    "SimulateTosAcceptResponse",
    "SimulateTosAcceptResponseData",
    "SimulateTosAcceptResponseDataTos",
    "SimulateTosAcceptResponseDataTosStatus",
    "SimulateWebhookFireResponse",
    "SimulateWebhookFireResponseData",
    "SourceAddressInput",
    "SourceOfFunds",
    "SpeiInfo",
    "StablecoinDeposit",
    "StablecoinDepositStatus",
    "SwiftpayPesonetInfo",
    "SwiftpayPesonetInfoChannelSubject",
    "SwiftpayPesonetInfoExtendInfo",
    "TooManyRequestsErrorBody",
    "TooManyRequestsErrorBodyError",
    "TooManyRequestsErrorBodyErrorDetails",
    "UnauthorizedErrorBody",
    "ValidationField",
    "VerifySenderRequirementsBlocker",
    "VerifySenderRequirementsBlockerAction",
    "VerifySenderRequirementsBlockerActionMethod",
    "VerifySenderRequirementsBlockerCode",
    "VerifySenderRequirementsBlockerFieldsItem",
    "VerifySenderRequirementsBlockerFieldsItemDocumentType",
    "VerifySenderRequirementsBlockerSubject",
    "VerifySenderRequirementsBlockerSubjectType",
    "VerifySenderRequirementsMissingError",
    "VerifySenderRequirementsMissingErrorError",
    "VerifySenderRequirementsMissingErrorErrorCode",
    "VirtualAccountSetupAction",
    "VirtualAccountSetupActionMethod",
    "VirtualAccountSetupBlocker",
    "VirtualAccountSetupBlockerCode",
    "VirtualAccountSetupBlockerFieldsItem",
    "VirtualAccountSetupBlockerFieldsItemDocumentType",
    "VirtualAccountSetupBlockerSubject",
    "VirtualAccountSetupBlockerSubjectType",
    "VirtualAccountSetupEnvelope",
    "VirtualAccountSetupResponse",
    "VirtualAccountSetupResponseCurrency",
    "VirtualAccountSetupResponseUnacceptedFieldsItem",
    "VirtualAccountSetupStatus",
]

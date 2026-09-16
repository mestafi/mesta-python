
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_ubos_request_address import CreateUbosRequestAddress
    from .create_ubos_request_identity import CreateUbosRequestIdentity
    from .create_ubos_request_identity_document_type import CreateUbosRequestIdentityDocumentType
    from .create_ubos_request_pep_questionnaire import CreateUbosRequestPepQuestionnaire
    from .create_ubos_request_pep_questionnaire_association import CreateUbosRequestPepQuestionnaireAssociation
    from .create_ubos_request_pep_questionnaire_declaration_type import CreateUbosRequestPepQuestionnaireDeclarationType
    from .create_ubos_request_pep_questionnaire_self import CreateUbosRequestPepQuestionnaireSelf
    from .create_ubos_request_pep_questionnaire_self_pep_category import (
        CreateUbosRequestPepQuestionnaireSelfPepCategory,
    )
    from .create_ubos_response import CreateUbosResponse
    from .create_ubos_response_data import CreateUbosResponseData
    from .create_ubos_response_data_documents_item import CreateUbosResponseDataDocumentsItem
    from .create_ubos_response_data_documents_item_type import CreateUbosResponseDataDocumentsItemType
    from .create_ubos_response_data_kyc import CreateUbosResponseDataKyc
    from .create_ubos_response_data_kyc_status import CreateUbosResponseDataKycStatus
    from .create_ubos_response_data_pep_questionnaire import CreateUbosResponseDataPepQuestionnaire
    from .create_ubos_response_data_pep_questionnaire_association import (
        CreateUbosResponseDataPepQuestionnaireAssociation,
    )
    from .create_ubos_response_data_pep_questionnaire_declaration_type import (
        CreateUbosResponseDataPepQuestionnaireDeclarationType,
    )
    from .create_ubos_response_data_pep_questionnaire_self import CreateUbosResponseDataPepQuestionnaireSelf
    from .create_ubos_response_data_pep_questionnaire_self_pep_category import (
        CreateUbosResponseDataPepQuestionnaireSelfPepCategory,
    )
    from .delete_ubos_response import DeleteUbosResponse
    from .get_ubos_response import GetUbosResponse
    from .get_ubos_response_data import GetUbosResponseData
    from .get_ubos_response_data_address import GetUbosResponseDataAddress
    from .get_ubos_response_data_documents_item import GetUbosResponseDataDocumentsItem
    from .get_ubos_response_data_documents_item_type import GetUbosResponseDataDocumentsItemType
    from .get_ubos_response_data_identity import GetUbosResponseDataIdentity
    from .get_ubos_response_data_identity_document_back import GetUbosResponseDataIdentityDocumentBack
    from .get_ubos_response_data_identity_document_front import GetUbosResponseDataIdentityDocumentFront
    from .get_ubos_response_data_identity_document_type import GetUbosResponseDataIdentityDocumentType
    from .get_ubos_response_data_kyc import GetUbosResponseDataKyc
    from .get_ubos_response_data_kyc_status import GetUbosResponseDataKycStatus
    from .get_ubos_response_data_sender import GetUbosResponseDataSender
    from .get_ubos_response_data_sender_addresses_item import GetUbosResponseDataSenderAddressesItem
    from .get_ubos_response_data_sender_documents_item import GetUbosResponseDataSenderDocumentsItem
    from .get_ubos_response_data_sender_kyb import GetUbosResponseDataSenderKyb
    from .get_ubos_response_data_sender_kyc import GetUbosResponseDataSenderKyc
    from .get_ubos_response_data_sender_status import GetUbosResponseDataSenderStatus
    from .get_ubos_response_data_sender_tos import GetUbosResponseDataSenderTos
    from .get_ubos_response_data_sender_type import GetUbosResponseDataSenderType
    from .get_verification_url_ubos_request_action import GetVerificationUrlUbosRequestAction
    from .get_verification_url_ubos_response import GetVerificationUrlUbosResponse
    from .get_verification_url_ubos_response_data import GetVerificationUrlUbosResponseData
    from .get_verification_url_ubos_response_data_latest_session import GetVerificationUrlUbosResponseDataLatestSession
    from .get_verification_url_ubos_response_data_latest_session_status import (
        GetVerificationUrlUbosResponseDataLatestSessionStatus,
    )
    from .get_verification_url_ubos_response_data_previous_sessions_item import (
        GetVerificationUrlUbosResponseDataPreviousSessionsItem,
    )
    from .get_verification_url_ubos_response_data_previous_sessions_item_status import (
        GetVerificationUrlUbosResponseDataPreviousSessionsItemStatus,
    )
    from .update_ubos_request_identity import UpdateUbosRequestIdentity
    from .update_ubos_request_identity_document_type import UpdateUbosRequestIdentityDocumentType
    from .update_ubos_request_pep_questionnaire import UpdateUbosRequestPepQuestionnaire
    from .update_ubos_request_pep_questionnaire_association import UpdateUbosRequestPepQuestionnaireAssociation
    from .update_ubos_request_pep_questionnaire_declaration_type import UpdateUbosRequestPepQuestionnaireDeclarationType
    from .update_ubos_request_pep_questionnaire_self import UpdateUbosRequestPepQuestionnaireSelf
    from .update_ubos_request_pep_questionnaire_self_pep_category import (
        UpdateUbosRequestPepQuestionnaireSelfPepCategory,
    )
    from .update_ubos_response import UpdateUbosResponse
    from .update_ubos_response_data import UpdateUbosResponseData
    from .update_ubos_response_data_address import UpdateUbosResponseDataAddress
    from .update_ubos_response_data_documents_item import UpdateUbosResponseDataDocumentsItem
    from .update_ubos_response_data_documents_item_type import UpdateUbosResponseDataDocumentsItemType
    from .update_ubos_response_data_identity import UpdateUbosResponseDataIdentity
    from .update_ubos_response_data_identity_document_type import UpdateUbosResponseDataIdentityDocumentType
    from .update_ubos_response_data_kyc import UpdateUbosResponseDataKyc
    from .update_ubos_response_data_kyc_status import UpdateUbosResponseDataKycStatus
    from .update_ubos_response_data_pep_questionnaire import UpdateUbosResponseDataPepQuestionnaire
    from .update_ubos_response_data_pep_questionnaire_association import (
        UpdateUbosResponseDataPepQuestionnaireAssociation,
    )
    from .update_ubos_response_data_pep_questionnaire_declaration_type import (
        UpdateUbosResponseDataPepQuestionnaireDeclarationType,
    )
    from .update_ubos_response_data_pep_questionnaire_self import UpdateUbosResponseDataPepQuestionnaireSelf
    from .update_ubos_response_data_pep_questionnaire_self_pep_category import (
        UpdateUbosResponseDataPepQuestionnaireSelfPepCategory,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateUbosRequestAddress": ".create_ubos_request_address",
    "CreateUbosRequestIdentity": ".create_ubos_request_identity",
    "CreateUbosRequestIdentityDocumentType": ".create_ubos_request_identity_document_type",
    "CreateUbosRequestPepQuestionnaire": ".create_ubos_request_pep_questionnaire",
    "CreateUbosRequestPepQuestionnaireAssociation": ".create_ubos_request_pep_questionnaire_association",
    "CreateUbosRequestPepQuestionnaireDeclarationType": ".create_ubos_request_pep_questionnaire_declaration_type",
    "CreateUbosRequestPepQuestionnaireSelf": ".create_ubos_request_pep_questionnaire_self",
    "CreateUbosRequestPepQuestionnaireSelfPepCategory": ".create_ubos_request_pep_questionnaire_self_pep_category",
    "CreateUbosResponse": ".create_ubos_response",
    "CreateUbosResponseData": ".create_ubos_response_data",
    "CreateUbosResponseDataDocumentsItem": ".create_ubos_response_data_documents_item",
    "CreateUbosResponseDataDocumentsItemType": ".create_ubos_response_data_documents_item_type",
    "CreateUbosResponseDataKyc": ".create_ubos_response_data_kyc",
    "CreateUbosResponseDataKycStatus": ".create_ubos_response_data_kyc_status",
    "CreateUbosResponseDataPepQuestionnaire": ".create_ubos_response_data_pep_questionnaire",
    "CreateUbosResponseDataPepQuestionnaireAssociation": ".create_ubos_response_data_pep_questionnaire_association",
    "CreateUbosResponseDataPepQuestionnaireDeclarationType": ".create_ubos_response_data_pep_questionnaire_declaration_type",
    "CreateUbosResponseDataPepQuestionnaireSelf": ".create_ubos_response_data_pep_questionnaire_self",
    "CreateUbosResponseDataPepQuestionnaireSelfPepCategory": ".create_ubos_response_data_pep_questionnaire_self_pep_category",
    "DeleteUbosResponse": ".delete_ubos_response",
    "GetUbosResponse": ".get_ubos_response",
    "GetUbosResponseData": ".get_ubos_response_data",
    "GetUbosResponseDataAddress": ".get_ubos_response_data_address",
    "GetUbosResponseDataDocumentsItem": ".get_ubos_response_data_documents_item",
    "GetUbosResponseDataDocumentsItemType": ".get_ubos_response_data_documents_item_type",
    "GetUbosResponseDataIdentity": ".get_ubos_response_data_identity",
    "GetUbosResponseDataIdentityDocumentBack": ".get_ubos_response_data_identity_document_back",
    "GetUbosResponseDataIdentityDocumentFront": ".get_ubos_response_data_identity_document_front",
    "GetUbosResponseDataIdentityDocumentType": ".get_ubos_response_data_identity_document_type",
    "GetUbosResponseDataKyc": ".get_ubos_response_data_kyc",
    "GetUbosResponseDataKycStatus": ".get_ubos_response_data_kyc_status",
    "GetUbosResponseDataSender": ".get_ubos_response_data_sender",
    "GetUbosResponseDataSenderAddressesItem": ".get_ubos_response_data_sender_addresses_item",
    "GetUbosResponseDataSenderDocumentsItem": ".get_ubos_response_data_sender_documents_item",
    "GetUbosResponseDataSenderKyb": ".get_ubos_response_data_sender_kyb",
    "GetUbosResponseDataSenderKyc": ".get_ubos_response_data_sender_kyc",
    "GetUbosResponseDataSenderStatus": ".get_ubos_response_data_sender_status",
    "GetUbosResponseDataSenderTos": ".get_ubos_response_data_sender_tos",
    "GetUbosResponseDataSenderType": ".get_ubos_response_data_sender_type",
    "GetVerificationUrlUbosRequestAction": ".get_verification_url_ubos_request_action",
    "GetVerificationUrlUbosResponse": ".get_verification_url_ubos_response",
    "GetVerificationUrlUbosResponseData": ".get_verification_url_ubos_response_data",
    "GetVerificationUrlUbosResponseDataLatestSession": ".get_verification_url_ubos_response_data_latest_session",
    "GetVerificationUrlUbosResponseDataLatestSessionStatus": ".get_verification_url_ubos_response_data_latest_session_status",
    "GetVerificationUrlUbosResponseDataPreviousSessionsItem": ".get_verification_url_ubos_response_data_previous_sessions_item",
    "GetVerificationUrlUbosResponseDataPreviousSessionsItemStatus": ".get_verification_url_ubos_response_data_previous_sessions_item_status",
    "UpdateUbosRequestIdentity": ".update_ubos_request_identity",
    "UpdateUbosRequestIdentityDocumentType": ".update_ubos_request_identity_document_type",
    "UpdateUbosRequestPepQuestionnaire": ".update_ubos_request_pep_questionnaire",
    "UpdateUbosRequestPepQuestionnaireAssociation": ".update_ubos_request_pep_questionnaire_association",
    "UpdateUbosRequestPepQuestionnaireDeclarationType": ".update_ubos_request_pep_questionnaire_declaration_type",
    "UpdateUbosRequestPepQuestionnaireSelf": ".update_ubos_request_pep_questionnaire_self",
    "UpdateUbosRequestPepQuestionnaireSelfPepCategory": ".update_ubos_request_pep_questionnaire_self_pep_category",
    "UpdateUbosResponse": ".update_ubos_response",
    "UpdateUbosResponseData": ".update_ubos_response_data",
    "UpdateUbosResponseDataAddress": ".update_ubos_response_data_address",
    "UpdateUbosResponseDataDocumentsItem": ".update_ubos_response_data_documents_item",
    "UpdateUbosResponseDataDocumentsItemType": ".update_ubos_response_data_documents_item_type",
    "UpdateUbosResponseDataIdentity": ".update_ubos_response_data_identity",
    "UpdateUbosResponseDataIdentityDocumentType": ".update_ubos_response_data_identity_document_type",
    "UpdateUbosResponseDataKyc": ".update_ubos_response_data_kyc",
    "UpdateUbosResponseDataKycStatus": ".update_ubos_response_data_kyc_status",
    "UpdateUbosResponseDataPepQuestionnaire": ".update_ubos_response_data_pep_questionnaire",
    "UpdateUbosResponseDataPepQuestionnaireAssociation": ".update_ubos_response_data_pep_questionnaire_association",
    "UpdateUbosResponseDataPepQuestionnaireDeclarationType": ".update_ubos_response_data_pep_questionnaire_declaration_type",
    "UpdateUbosResponseDataPepQuestionnaireSelf": ".update_ubos_response_data_pep_questionnaire_self",
    "UpdateUbosResponseDataPepQuestionnaireSelfPepCategory": ".update_ubos_response_data_pep_questionnaire_self_pep_category",
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
    "CreateUbosRequestAddress",
    "CreateUbosRequestIdentity",
    "CreateUbosRequestIdentityDocumentType",
    "CreateUbosRequestPepQuestionnaire",
    "CreateUbosRequestPepQuestionnaireAssociation",
    "CreateUbosRequestPepQuestionnaireDeclarationType",
    "CreateUbosRequestPepQuestionnaireSelf",
    "CreateUbosRequestPepQuestionnaireSelfPepCategory",
    "CreateUbosResponse",
    "CreateUbosResponseData",
    "CreateUbosResponseDataDocumentsItem",
    "CreateUbosResponseDataDocumentsItemType",
    "CreateUbosResponseDataKyc",
    "CreateUbosResponseDataKycStatus",
    "CreateUbosResponseDataPepQuestionnaire",
    "CreateUbosResponseDataPepQuestionnaireAssociation",
    "CreateUbosResponseDataPepQuestionnaireDeclarationType",
    "CreateUbosResponseDataPepQuestionnaireSelf",
    "CreateUbosResponseDataPepQuestionnaireSelfPepCategory",
    "DeleteUbosResponse",
    "GetUbosResponse",
    "GetUbosResponseData",
    "GetUbosResponseDataAddress",
    "GetUbosResponseDataDocumentsItem",
    "GetUbosResponseDataDocumentsItemType",
    "GetUbosResponseDataIdentity",
    "GetUbosResponseDataIdentityDocumentBack",
    "GetUbosResponseDataIdentityDocumentFront",
    "GetUbosResponseDataIdentityDocumentType",
    "GetUbosResponseDataKyc",
    "GetUbosResponseDataKycStatus",
    "GetUbosResponseDataSender",
    "GetUbosResponseDataSenderAddressesItem",
    "GetUbosResponseDataSenderDocumentsItem",
    "GetUbosResponseDataSenderKyb",
    "GetUbosResponseDataSenderKyc",
    "GetUbosResponseDataSenderStatus",
    "GetUbosResponseDataSenderTos",
    "GetUbosResponseDataSenderType",
    "GetVerificationUrlUbosRequestAction",
    "GetVerificationUrlUbosResponse",
    "GetVerificationUrlUbosResponseData",
    "GetVerificationUrlUbosResponseDataLatestSession",
    "GetVerificationUrlUbosResponseDataLatestSessionStatus",
    "GetVerificationUrlUbosResponseDataPreviousSessionsItem",
    "GetVerificationUrlUbosResponseDataPreviousSessionsItemStatus",
    "UpdateUbosRequestIdentity",
    "UpdateUbosRequestIdentityDocumentType",
    "UpdateUbosRequestPepQuestionnaire",
    "UpdateUbosRequestPepQuestionnaireAssociation",
    "UpdateUbosRequestPepQuestionnaireDeclarationType",
    "UpdateUbosRequestPepQuestionnaireSelf",
    "UpdateUbosRequestPepQuestionnaireSelfPepCategory",
    "UpdateUbosResponse",
    "UpdateUbosResponseData",
    "UpdateUbosResponseDataAddress",
    "UpdateUbosResponseDataDocumentsItem",
    "UpdateUbosResponseDataDocumentsItemType",
    "UpdateUbosResponseDataIdentity",
    "UpdateUbosResponseDataIdentityDocumentType",
    "UpdateUbosResponseDataKyc",
    "UpdateUbosResponseDataKycStatus",
    "UpdateUbosResponseDataPepQuestionnaire",
    "UpdateUbosResponseDataPepQuestionnaireAssociation",
    "UpdateUbosResponseDataPepQuestionnaireDeclarationType",
    "UpdateUbosResponseDataPepQuestionnaireSelf",
    "UpdateUbosResponseDataPepQuestionnaireSelfPepCategory",
]

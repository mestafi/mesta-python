
# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_beneficiaries_request_owner_type import GetBeneficiariesRequestOwnerType
    from .get_beneficiaries_response import GetBeneficiariesResponse
    from .get_beneficiaries_response_data import GetBeneficiariesResponseData
    from .get_beneficiaries_response_data_owner import GetBeneficiariesResponseDataOwner
    from .get_beneficiaries_response_data_owner_type import GetBeneficiariesResponseDataOwnerType
    from .get_beneficiaries_response_data_rules import GetBeneficiariesResponseDataRules
    from .get_beneficiaries_response_data_rules_payment_types_item import (
        GetBeneficiariesResponseDataRulesPaymentTypesItem,
    )
    from .get_beneficiaries_response_data_rules_payment_types_item_type import (
        GetBeneficiariesResponseDataRulesPaymentTypesItemType,
    )
    from .get_beneficiaries_response_data_rules_required_documents_item import (
        GetBeneficiariesResponseDataRulesRequiredDocumentsItem,
    )
    from .list_countries_beneficiaries_response import ListCountriesBeneficiariesResponse
    from .list_document_types_beneficiaries_request_owner_type import ListDocumentTypesBeneficiariesRequestOwnerType
    from .list_document_types_beneficiaries_response import ListDocumentTypesBeneficiariesResponse
    from .list_document_types_beneficiaries_response_data import ListDocumentTypesBeneficiariesResponseData
    from .list_document_types_beneficiaries_response_data_owner import ListDocumentTypesBeneficiariesResponseDataOwner
    from .list_document_types_beneficiaries_response_data_owner_type import (
        ListDocumentTypesBeneficiariesResponseDataOwnerType,
    )
    from .list_document_types_beneficiaries_response_data_rules import ListDocumentTypesBeneficiariesResponseDataRules
    from .list_document_types_beneficiaries_response_data_rules_required_documents_item import (
        ListDocumentTypesBeneficiariesResponseDataRulesRequiredDocumentsItem,
    )
    from .list_payment_types_beneficiaries_request_owner_type import ListPaymentTypesBeneficiariesRequestOwnerType
    from .list_payment_types_beneficiaries_response import ListPaymentTypesBeneficiariesResponse
    from .list_payment_types_beneficiaries_response_data import ListPaymentTypesBeneficiariesResponseData
    from .list_payment_types_beneficiaries_response_data_owner import ListPaymentTypesBeneficiariesResponseDataOwner
    from .list_payment_types_beneficiaries_response_data_owner_type import (
        ListPaymentTypesBeneficiariesResponseDataOwnerType,
    )
    from .list_payment_types_beneficiaries_response_data_rules import ListPaymentTypesBeneficiariesResponseDataRules
    from .list_payment_types_beneficiaries_response_data_rules_payment_types_item import (
        ListPaymentTypesBeneficiariesResponseDataRulesPaymentTypesItem,
    )
    from .list_payment_types_beneficiaries_response_data_rules_payment_types_item_type import (
        ListPaymentTypesBeneficiariesResponseDataRulesPaymentTypesItemType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetBeneficiariesRequestOwnerType": ".get_beneficiaries_request_owner_type",
    "GetBeneficiariesResponse": ".get_beneficiaries_response",
    "GetBeneficiariesResponseData": ".get_beneficiaries_response_data",
    "GetBeneficiariesResponseDataOwner": ".get_beneficiaries_response_data_owner",
    "GetBeneficiariesResponseDataOwnerType": ".get_beneficiaries_response_data_owner_type",
    "GetBeneficiariesResponseDataRules": ".get_beneficiaries_response_data_rules",
    "GetBeneficiariesResponseDataRulesPaymentTypesItem": ".get_beneficiaries_response_data_rules_payment_types_item",
    "GetBeneficiariesResponseDataRulesPaymentTypesItemType": ".get_beneficiaries_response_data_rules_payment_types_item_type",
    "GetBeneficiariesResponseDataRulesRequiredDocumentsItem": ".get_beneficiaries_response_data_rules_required_documents_item",
    "ListCountriesBeneficiariesResponse": ".list_countries_beneficiaries_response",
    "ListDocumentTypesBeneficiariesRequestOwnerType": ".list_document_types_beneficiaries_request_owner_type",
    "ListDocumentTypesBeneficiariesResponse": ".list_document_types_beneficiaries_response",
    "ListDocumentTypesBeneficiariesResponseData": ".list_document_types_beneficiaries_response_data",
    "ListDocumentTypesBeneficiariesResponseDataOwner": ".list_document_types_beneficiaries_response_data_owner",
    "ListDocumentTypesBeneficiariesResponseDataOwnerType": ".list_document_types_beneficiaries_response_data_owner_type",
    "ListDocumentTypesBeneficiariesResponseDataRules": ".list_document_types_beneficiaries_response_data_rules",
    "ListDocumentTypesBeneficiariesResponseDataRulesRequiredDocumentsItem": ".list_document_types_beneficiaries_response_data_rules_required_documents_item",
    "ListPaymentTypesBeneficiariesRequestOwnerType": ".list_payment_types_beneficiaries_request_owner_type",
    "ListPaymentTypesBeneficiariesResponse": ".list_payment_types_beneficiaries_response",
    "ListPaymentTypesBeneficiariesResponseData": ".list_payment_types_beneficiaries_response_data",
    "ListPaymentTypesBeneficiariesResponseDataOwner": ".list_payment_types_beneficiaries_response_data_owner",
    "ListPaymentTypesBeneficiariesResponseDataOwnerType": ".list_payment_types_beneficiaries_response_data_owner_type",
    "ListPaymentTypesBeneficiariesResponseDataRules": ".list_payment_types_beneficiaries_response_data_rules",
    "ListPaymentTypesBeneficiariesResponseDataRulesPaymentTypesItem": ".list_payment_types_beneficiaries_response_data_rules_payment_types_item",
    "ListPaymentTypesBeneficiariesResponseDataRulesPaymentTypesItemType": ".list_payment_types_beneficiaries_response_data_rules_payment_types_item_type",
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
    "GetBeneficiariesRequestOwnerType",
    "GetBeneficiariesResponse",
    "GetBeneficiariesResponseData",
    "GetBeneficiariesResponseDataOwner",
    "GetBeneficiariesResponseDataOwnerType",
    "GetBeneficiariesResponseDataRules",
    "GetBeneficiariesResponseDataRulesPaymentTypesItem",
    "GetBeneficiariesResponseDataRulesPaymentTypesItemType",
    "GetBeneficiariesResponseDataRulesRequiredDocumentsItem",
    "ListCountriesBeneficiariesResponse",
    "ListDocumentTypesBeneficiariesRequestOwnerType",
    "ListDocumentTypesBeneficiariesResponse",
    "ListDocumentTypesBeneficiariesResponseData",
    "ListDocumentTypesBeneficiariesResponseDataOwner",
    "ListDocumentTypesBeneficiariesResponseDataOwnerType",
    "ListDocumentTypesBeneficiariesResponseDataRules",
    "ListDocumentTypesBeneficiariesResponseDataRulesRequiredDocumentsItem",
    "ListPaymentTypesBeneficiariesRequestOwnerType",
    "ListPaymentTypesBeneficiariesResponse",
    "ListPaymentTypesBeneficiariesResponseData",
    "ListPaymentTypesBeneficiariesResponseDataOwner",
    "ListPaymentTypesBeneficiariesResponseDataOwnerType",
    "ListPaymentTypesBeneficiariesResponseDataRules",
    "ListPaymentTypesBeneficiariesResponseDataRulesPaymentTypesItem",
    "ListPaymentTypesBeneficiariesResponseDataRulesPaymentTypesItemType",
]

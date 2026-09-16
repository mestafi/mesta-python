
import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.beneficiary_relationship import BeneficiaryRelationship
from ..types.error_response import ErrorResponse
from ..types.purpose_of_payment import PurposeOfPayment
from ..types.purpose_of_payment_document_request import PurposeOfPaymentDocumentRequest
from .types.create_beneficiaries_request_address import CreateBeneficiariesRequestAddress
from .types.create_beneficiaries_request_business_type import CreateBeneficiariesRequestBusinessType
from .types.create_beneficiaries_request_identity import CreateBeneficiariesRequestIdentity
from .types.create_beneficiaries_request_payment_methods_item import CreateBeneficiariesRequestPaymentMethodsItem
from .types.create_beneficiaries_request_type import CreateBeneficiariesRequestType
from .types.create_beneficiaries_response import CreateBeneficiariesResponse
from .types.delete_beneficiaries_response import DeleteBeneficiariesResponse
from .types.get_beneficiaries_response import GetBeneficiariesResponse
from .types.list_beneficiaries_request_sort_by import ListBeneficiariesRequestSortBy
from .types.list_beneficiaries_request_sort_order import ListBeneficiariesRequestSortOrder
from .types.list_beneficiaries_response import ListBeneficiariesResponse
from .types.lookup_bank_beneficiaries_response import LookupBankBeneficiariesResponse
from .types.simulate_verification_result_beneficiaries_request_result import (
    SimulateVerificationResultBeneficiariesRequestResult,
)
from .types.simulate_verification_result_beneficiaries_response import SimulateVerificationResultBeneficiariesResponse
from .types.update_beneficiaries_request_address import UpdateBeneficiariesRequestAddress
from .types.update_beneficiaries_request_type import UpdateBeneficiariesRequestType
from .types.update_beneficiaries_response import UpdateBeneficiariesResponse
from .types.verify_beneficiaries_response import VerifyBeneficiariesResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawBeneficiariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete(
        self, beneficiary_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteBeneficiariesResponse]:
        """
        Deletes a beneficiary account.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier for the beneficiary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteBeneficiariesResponse]
            Beneficiary Deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/beneficiaries/{encode_path_param(beneficiary_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBeneficiariesResponse,
                    parse_obj_as(
                        type_=DeleteBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def simulate_verification_result(
        self,
        beneficiary_id: str,
        *,
        result: SimulateVerificationResultBeneficiariesRequestResult,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SimulateVerificationResultBeneficiariesResponse]:
        """
        Settles a pending beneficiary verification with a simulated provider decision so you can drive onboarding end to end without waiting on the identity provider. Available in test environments only — disabled in production.

        Verification must already have been started via the corresponding `/verify` call; otherwise the request is rejected with `MOCK_VERIFICATION_NOT_INITIATED`.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier for the beneficiary.

        result : SimulateVerificationResultBeneficiariesRequestResult
            The verification outcome to simulate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimulateVerificationResultBeneficiariesResponse]
            Simulated verification result applied.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/beneficiaries/{encode_path_param(beneficiary_id)}/mock-verification-result",
            method="POST",
            json={
                "result": result,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimulateVerificationResultBeneficiariesResponse,
                    parse_obj_as(
                        type_=SimulateVerificationResultBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def verify(
        self, beneficiary_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VerifyBeneficiariesResponse]:
        """
        Verifies a specific beneficiary account by initiating sanction/watchlist screenings.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier for the beneficiary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VerifyBeneficiariesResponse]
            Beneficiary verification initiated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/beneficiaries/{encode_path_param(beneficiary_id)}/verify",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VerifyBeneficiariesResponse,
                    parse_obj_as(
                        type_=VerifyBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def lookup_bank(
        self, *, country_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LookupBankBeneficiariesResponse]:
        """
        Retrieve a list of bank Ids for a specific country.

        Parameters
        ----------
        country_code : str
            ISO 3166-1 alpha-2 country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LookupBankBeneficiariesResponse]
            Bank list retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/beneficiaries/banks",
            method="GET",
            params={
                "countryCode": country_code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LookupBankBeneficiariesResponse,
                    parse_obj_as(
                        type_=LookupBankBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListBeneficiariesRequestSortBy] = None,
        sort_order: typing.Optional[ListBeneficiariesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListBeneficiariesResponse]:
        """
        Retrieves a paginated list of beneficiaries using the V2 API. Unlike v1, the v2 API separates payment methods from beneficiary data. Payment methods are available on the detail endpoint.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (zero-based)

        page_size : typing.Optional[int]
            Number of items per page

        sort_by : typing.Optional[ListBeneficiariesRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[ListBeneficiariesRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListBeneficiariesResponse]
            List of beneficiaries with payment methods
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/beneficiaries",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBeneficiariesResponse]:
        """
        Retrieve a single beneficiary by ID with their associated payment methods.

        Parameters
        ----------
        id : str
            Beneficiary ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBeneficiariesResponse]
            Beneficiary details with payment methods
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/beneficiaries/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBeneficiariesResponse,
                    parse_obj_as(
                        type_=GetBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id: str,
        *,
        type: typing.Optional[UpdateBeneficiariesRequestType] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        address: typing.Optional[UpdateBeneficiariesRequestAddress] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        beneficiary_relationship: typing.Optional[BeneficiaryRelationship] = OMIT,
        purpose_of_payment: typing.Optional[PurposeOfPayment] = OMIT,
        purpose_of_payment_document: typing.Optional[PurposeOfPaymentDocumentRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateBeneficiariesResponse]:
        """
        Partially update a beneficiary. Only the provided fields will be updated.

        Parameters
        ----------
        id : str
            Beneficiary ID

        type : typing.Optional[UpdateBeneficiariesRequestType]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        middle_name : typing.Optional[str]

        full_name : typing.Optional[str]

        email : typing.Optional[str]

        phone : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        address : typing.Optional[UpdateBeneficiariesRequestAddress]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        beneficiary_relationship : typing.Optional[BeneficiaryRelationship]

        purpose_of_payment : typing.Optional[PurposeOfPayment]

        purpose_of_payment_document : typing.Optional[PurposeOfPaymentDocumentRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateBeneficiariesResponse]
            Beneficiary updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/beneficiaries/{encode_path_param(id)}",
            method="PATCH",
            json={
                "type": type,
                "firstName": first_name,
                "lastName": last_name,
                "middleName": middle_name,
                "fullName": full_name,
                "email": email,
                "phone": phone,
                "birthDate": birth_date,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=UpdateBeneficiariesRequestAddress, direction="write"
                ),
                "metadata": metadata,
                "beneficiaryRelationship": beneficiary_relationship,
                "purposeOfPayment": purpose_of_payment,
                "purposeOfPaymentDocument": convert_and_respect_annotation_metadata(
                    object_=purpose_of_payment_document, annotation=PurposeOfPaymentDocumentRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateBeneficiariesResponse,
                    parse_obj_as(
                        type_=UpdateBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        type: CreateBeneficiariesRequestType,
        address: CreateBeneficiariesRequestAddress,
        payment_methods: typing.Sequence[CreateBeneficiariesRequestPaymentMethodsItem],
        beneficiary_relationship: BeneficiaryRelationship,
        purpose_of_payment: PurposeOfPayment,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        business_registration_number: typing.Optional[str] = OMIT,
        business_type: typing.Optional[CreateBeneficiariesRequestBusinessType] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        merchant_id: typing.Optional[str] = OMIT,
        identity: typing.Optional[CreateBeneficiariesRequestIdentity] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        purpose_of_payment_document: typing.Optional[PurposeOfPaymentDocumentRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateBeneficiariesResponse]:
        """
        Create a new beneficiary with mandatory compliance fields. Same as V2 but `beneficiaryRelationship` and `purposeOfPayment` are required.

        Parameters
        ----------
        type : CreateBeneficiariesRequestType
            Type of beneficiary

        address : CreateBeneficiariesRequestAddress
            Beneficiary address

        payment_methods : typing.Sequence[CreateBeneficiariesRequestPaymentMethodsItem]
            At least one payment method must be provided

        beneficiary_relationship : BeneficiaryRelationship

        purpose_of_payment : PurposeOfPayment

        first_name : typing.Optional[str]
            First name (required for individual type)

        last_name : typing.Optional[str]
            Last name (required for individual type)

        middle_name : typing.Optional[str]
            Middle name (optional, individual type only)

        full_name : typing.Optional[str]
            Full business name (required for business type)

        business_registration_number : typing.Optional[str]
            Business registration number (required for business type)

        business_type : typing.Optional[CreateBeneficiariesRequestBusinessType]
            Type of business (optional)

        email : typing.Optional[str]
            Beneficiary email

        phone : typing.Optional[str]
            Beneficiary phone number

        birth_date : typing.Optional[dt.date]
            Date of birth (YYYY-MM-DD, individual type)

        merchant_id : typing.Optional[str]
            Merchant ID (optional, auto-assigned from API key)

        identity : typing.Optional[CreateBeneficiariesRequestIdentity]
            Identity document details

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Custom metadata

        purpose_of_payment_document : typing.Optional[PurposeOfPaymentDocumentRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateBeneficiariesResponse]
            Beneficiary created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/beneficiaries",
            method="POST",
            json={
                "type": type,
                "firstName": first_name,
                "lastName": last_name,
                "middleName": middle_name,
                "fullName": full_name,
                "businessRegistrationNumber": business_registration_number,
                "businessType": business_type,
                "email": email,
                "phone": phone,
                "birthDate": birth_date,
                "merchantId": merchant_id,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CreateBeneficiariesRequestAddress, direction="write"
                ),
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=CreateBeneficiariesRequestIdentity, direction="write"
                ),
                "paymentMethods": convert_and_respect_annotation_metadata(
                    object_=payment_methods,
                    annotation=typing.Sequence[CreateBeneficiariesRequestPaymentMethodsItem],
                    direction="write",
                ),
                "metadata": metadata,
                "beneficiaryRelationship": beneficiary_relationship,
                "purposeOfPayment": purpose_of_payment,
                "purposeOfPaymentDocument": convert_and_respect_annotation_metadata(
                    object_=purpose_of_payment_document, annotation=PurposeOfPaymentDocumentRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateBeneficiariesResponse,
                    parse_obj_as(
                        type_=CreateBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBeneficiariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete(
        self, beneficiary_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteBeneficiariesResponse]:
        """
        Deletes a beneficiary account.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier for the beneficiary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteBeneficiariesResponse]
            Beneficiary Deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/beneficiaries/{encode_path_param(beneficiary_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteBeneficiariesResponse,
                    parse_obj_as(
                        type_=DeleteBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def simulate_verification_result(
        self,
        beneficiary_id: str,
        *,
        result: SimulateVerificationResultBeneficiariesRequestResult,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SimulateVerificationResultBeneficiariesResponse]:
        """
        Settles a pending beneficiary verification with a simulated provider decision so you can drive onboarding end to end without waiting on the identity provider. Available in test environments only — disabled in production.

        Verification must already have been started via the corresponding `/verify` call; otherwise the request is rejected with `MOCK_VERIFICATION_NOT_INITIATED`.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier for the beneficiary.

        result : SimulateVerificationResultBeneficiariesRequestResult
            The verification outcome to simulate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimulateVerificationResultBeneficiariesResponse]
            Simulated verification result applied.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/beneficiaries/{encode_path_param(beneficiary_id)}/mock-verification-result",
            method="POST",
            json={
                "result": result,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimulateVerificationResultBeneficiariesResponse,
                    parse_obj_as(
                        type_=SimulateVerificationResultBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def verify(
        self, beneficiary_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VerifyBeneficiariesResponse]:
        """
        Verifies a specific beneficiary account by initiating sanction/watchlist screenings.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier for the beneficiary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VerifyBeneficiariesResponse]
            Beneficiary verification initiated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/beneficiaries/{encode_path_param(beneficiary_id)}/verify",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VerifyBeneficiariesResponse,
                    parse_obj_as(
                        type_=VerifyBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def lookup_bank(
        self, *, country_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LookupBankBeneficiariesResponse]:
        """
        Retrieve a list of bank Ids for a specific country.

        Parameters
        ----------
        country_code : str
            ISO 3166-1 alpha-2 country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LookupBankBeneficiariesResponse]
            Bank list retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/beneficiaries/banks",
            method="GET",
            params={
                "countryCode": country_code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LookupBankBeneficiariesResponse,
                    parse_obj_as(
                        type_=LookupBankBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListBeneficiariesRequestSortBy] = None,
        sort_order: typing.Optional[ListBeneficiariesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListBeneficiariesResponse]:
        """
        Retrieves a paginated list of beneficiaries using the V2 API. Unlike v1, the v2 API separates payment methods from beneficiary data. Payment methods are available on the detail endpoint.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (zero-based)

        page_size : typing.Optional[int]
            Number of items per page

        sort_by : typing.Optional[ListBeneficiariesRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[ListBeneficiariesRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListBeneficiariesResponse]
            List of beneficiaries with payment methods
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/beneficiaries",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBeneficiariesResponse]:
        """
        Retrieve a single beneficiary by ID with their associated payment methods.

        Parameters
        ----------
        id : str
            Beneficiary ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBeneficiariesResponse]
            Beneficiary details with payment methods
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/beneficiaries/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBeneficiariesResponse,
                    parse_obj_as(
                        type_=GetBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id: str,
        *,
        type: typing.Optional[UpdateBeneficiariesRequestType] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        address: typing.Optional[UpdateBeneficiariesRequestAddress] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        beneficiary_relationship: typing.Optional[BeneficiaryRelationship] = OMIT,
        purpose_of_payment: typing.Optional[PurposeOfPayment] = OMIT,
        purpose_of_payment_document: typing.Optional[PurposeOfPaymentDocumentRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateBeneficiariesResponse]:
        """
        Partially update a beneficiary. Only the provided fields will be updated.

        Parameters
        ----------
        id : str
            Beneficiary ID

        type : typing.Optional[UpdateBeneficiariesRequestType]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        middle_name : typing.Optional[str]

        full_name : typing.Optional[str]

        email : typing.Optional[str]

        phone : typing.Optional[str]

        birth_date : typing.Optional[dt.date]

        address : typing.Optional[UpdateBeneficiariesRequestAddress]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        beneficiary_relationship : typing.Optional[BeneficiaryRelationship]

        purpose_of_payment : typing.Optional[PurposeOfPayment]

        purpose_of_payment_document : typing.Optional[PurposeOfPaymentDocumentRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateBeneficiariesResponse]
            Beneficiary updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/beneficiaries/{encode_path_param(id)}",
            method="PATCH",
            json={
                "type": type,
                "firstName": first_name,
                "lastName": last_name,
                "middleName": middle_name,
                "fullName": full_name,
                "email": email,
                "phone": phone,
                "birthDate": birth_date,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=UpdateBeneficiariesRequestAddress, direction="write"
                ),
                "metadata": metadata,
                "beneficiaryRelationship": beneficiary_relationship,
                "purposeOfPayment": purpose_of_payment,
                "purposeOfPaymentDocument": convert_and_respect_annotation_metadata(
                    object_=purpose_of_payment_document, annotation=PurposeOfPaymentDocumentRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateBeneficiariesResponse,
                    parse_obj_as(
                        type_=UpdateBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        type: CreateBeneficiariesRequestType,
        address: CreateBeneficiariesRequestAddress,
        payment_methods: typing.Sequence[CreateBeneficiariesRequestPaymentMethodsItem],
        beneficiary_relationship: BeneficiaryRelationship,
        purpose_of_payment: PurposeOfPayment,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        middle_name: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        business_registration_number: typing.Optional[str] = OMIT,
        business_type: typing.Optional[CreateBeneficiariesRequestBusinessType] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        merchant_id: typing.Optional[str] = OMIT,
        identity: typing.Optional[CreateBeneficiariesRequestIdentity] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        purpose_of_payment_document: typing.Optional[PurposeOfPaymentDocumentRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateBeneficiariesResponse]:
        """
        Create a new beneficiary with mandatory compliance fields. Same as V2 but `beneficiaryRelationship` and `purposeOfPayment` are required.

        Parameters
        ----------
        type : CreateBeneficiariesRequestType
            Type of beneficiary

        address : CreateBeneficiariesRequestAddress
            Beneficiary address

        payment_methods : typing.Sequence[CreateBeneficiariesRequestPaymentMethodsItem]
            At least one payment method must be provided

        beneficiary_relationship : BeneficiaryRelationship

        purpose_of_payment : PurposeOfPayment

        first_name : typing.Optional[str]
            First name (required for individual type)

        last_name : typing.Optional[str]
            Last name (required for individual type)

        middle_name : typing.Optional[str]
            Middle name (optional, individual type only)

        full_name : typing.Optional[str]
            Full business name (required for business type)

        business_registration_number : typing.Optional[str]
            Business registration number (required for business type)

        business_type : typing.Optional[CreateBeneficiariesRequestBusinessType]
            Type of business (optional)

        email : typing.Optional[str]
            Beneficiary email

        phone : typing.Optional[str]
            Beneficiary phone number

        birth_date : typing.Optional[dt.date]
            Date of birth (YYYY-MM-DD, individual type)

        merchant_id : typing.Optional[str]
            Merchant ID (optional, auto-assigned from API key)

        identity : typing.Optional[CreateBeneficiariesRequestIdentity]
            Identity document details

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Custom metadata

        purpose_of_payment_document : typing.Optional[PurposeOfPaymentDocumentRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateBeneficiariesResponse]
            Beneficiary created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/beneficiaries",
            method="POST",
            json={
                "type": type,
                "firstName": first_name,
                "lastName": last_name,
                "middleName": middle_name,
                "fullName": full_name,
                "businessRegistrationNumber": business_registration_number,
                "businessType": business_type,
                "email": email,
                "phone": phone,
                "birthDate": birth_date,
                "merchantId": merchant_id,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CreateBeneficiariesRequestAddress, direction="write"
                ),
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=CreateBeneficiariesRequestIdentity, direction="write"
                ),
                "paymentMethods": convert_and_respect_annotation_metadata(
                    object_=payment_methods,
                    annotation=typing.Sequence[CreateBeneficiariesRequestPaymentMethodsItem],
                    direction="write",
                ),
                "metadata": metadata,
                "beneficiaryRelationship": beneficiary_relationship,
                "purposeOfPayment": purpose_of_payment,
                "purposeOfPaymentDocument": convert_and_respect_annotation_metadata(
                    object_=purpose_of_payment_document, annotation=PurposeOfPaymentDocumentRequest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateBeneficiariesResponse,
                    parse_obj_as(
                        type_=CreateBeneficiariesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

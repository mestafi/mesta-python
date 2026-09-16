
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error_response import ErrorResponse
from .types.get_beneficiaries_request_owner_type import GetBeneficiariesRequestOwnerType
from .types.get_beneficiaries_response import GetBeneficiariesResponse
from .types.list_countries_beneficiaries_response import ListCountriesBeneficiariesResponse
from .types.list_document_types_beneficiaries_request_owner_type import ListDocumentTypesBeneficiariesRequestOwnerType
from .types.list_document_types_beneficiaries_response import ListDocumentTypesBeneficiariesResponse
from .types.list_payment_types_beneficiaries_request_owner_type import ListPaymentTypesBeneficiariesRequestOwnerType
from .types.list_payment_types_beneficiaries_response import ListPaymentTypesBeneficiariesResponse
from pydantic import ValidationError


class RawBeneficiariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        owner_type: GetBeneficiariesRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetBeneficiariesResponse]:
        """
        Retrieves all validation rules required for creating a beneficiary, including required fields and payment information requirements.

        Parameters
        ----------
        owner_type : GetBeneficiariesRequestOwnerType

        country : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBeneficiariesResponse]
            Successfully retrieved beneficiary validation rules
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries",
            method="GET",
            params={
                "ownerType": owner_type,
                "country": country,
            },
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

    def list_document_types(
        self,
        *,
        owner_type: ListDocumentTypesBeneficiariesRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDocumentTypesBeneficiariesResponse]:
        """
        Retrieves the list of required documents for beneficiary verification based on country and owner type. Note that some countries may not require any documents.

        Parameters
        ----------
        owner_type : ListDocumentTypesBeneficiariesRequestOwnerType
            Type of beneficiary entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDocumentTypesBeneficiariesResponse]
            Successfully retrieved document requirements
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries/document-types",
            method="GET",
            params={
                "ownerType": owner_type,
                "country": country,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDocumentTypesBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListDocumentTypesBeneficiariesResponse,  # type: ignore
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

    def list_payment_types(
        self,
        *,
        owner_type: ListPaymentTypesBeneficiariesRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListPaymentTypesBeneficiariesResponse]:
        """
        Retrieves the list of supported payment types and their required fields for a beneficiary in a specific country. Use this to determine what payment information needs to be collected.

        Parameters
        ----------
        owner_type : ListPaymentTypesBeneficiariesRequestOwnerType
            Type of beneficiary entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPaymentTypesBeneficiariesResponse]
            Successfully retrieved supported payment types
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries/payment-types",
            method="GET",
            params={
                "ownerType": owner_type,
                "country": country,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentTypesBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListPaymentTypesBeneficiariesResponse,  # type: ignore
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

    def list_countries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListCountriesBeneficiariesResponse]:
        """
        Retrieve a list of countries to which payments can be delivered.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCountriesBeneficiariesResponse]
            List of supported beneficiary countries
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries/countries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCountriesBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListCountriesBeneficiariesResponse,  # type: ignore
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


class AsyncRawBeneficiariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        owner_type: GetBeneficiariesRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetBeneficiariesResponse]:
        """
        Retrieves all validation rules required for creating a beneficiary, including required fields and payment information requirements.

        Parameters
        ----------
        owner_type : GetBeneficiariesRequestOwnerType

        country : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBeneficiariesResponse]
            Successfully retrieved beneficiary validation rules
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries",
            method="GET",
            params={
                "ownerType": owner_type,
                "country": country,
            },
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

    async def list_document_types(
        self,
        *,
        owner_type: ListDocumentTypesBeneficiariesRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDocumentTypesBeneficiariesResponse]:
        """
        Retrieves the list of required documents for beneficiary verification based on country and owner type. Note that some countries may not require any documents.

        Parameters
        ----------
        owner_type : ListDocumentTypesBeneficiariesRequestOwnerType
            Type of beneficiary entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDocumentTypesBeneficiariesResponse]
            Successfully retrieved document requirements
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries/document-types",
            method="GET",
            params={
                "ownerType": owner_type,
                "country": country,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDocumentTypesBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListDocumentTypesBeneficiariesResponse,  # type: ignore
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

    async def list_payment_types(
        self,
        *,
        owner_type: ListPaymentTypesBeneficiariesRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListPaymentTypesBeneficiariesResponse]:
        """
        Retrieves the list of supported payment types and their required fields for a beneficiary in a specific country. Use this to determine what payment information needs to be collected.

        Parameters
        ----------
        owner_type : ListPaymentTypesBeneficiariesRequestOwnerType
            Type of beneficiary entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPaymentTypesBeneficiariesResponse]
            Successfully retrieved supported payment types
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries/payment-types",
            method="GET",
            params={
                "ownerType": owner_type,
                "country": country,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPaymentTypesBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListPaymentTypesBeneficiariesResponse,  # type: ignore
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

    async def list_countries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListCountriesBeneficiariesResponse]:
        """
        Retrieve a list of countries to which payments can be delivered.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCountriesBeneficiariesResponse]
            List of supported beneficiary countries
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/beneficiaries/countries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCountriesBeneficiariesResponse,
                    parse_obj_as(
                        type_=ListCountriesBeneficiariesResponse,  # type: ignore
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

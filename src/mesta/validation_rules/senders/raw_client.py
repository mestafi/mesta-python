
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error_response import ErrorResponse
from .types.get_ubo_rules_v1senders_request_owner_type import GetUboRulesV1SendersRequestOwnerType
from .types.get_ubo_rules_v1senders_response import GetUboRulesV1SendersResponse
from .types.get_ubo_rules_v2senders_request_owner_type import GetUboRulesV2SendersRequestOwnerType
from .types.get_ubo_rules_v2senders_response import GetUboRulesV2SendersResponse
from .types.get_v1senders_request_owner_type import GetV1SendersRequestOwnerType
from .types.get_v1senders_response import GetV1SendersResponse
from .types.get_v2senders_request_owner_type import GetV2SendersRequestOwnerType
from .types.get_v2senders_response import GetV2SendersResponse
from .types.list_countries_senders_response import ListCountriesSendersResponse
from .types.list_document_types_v1senders_request_owner_type import ListDocumentTypesV1SendersRequestOwnerType
from .types.list_document_types_v1senders_response import ListDocumentTypesV1SendersResponse
from .types.list_document_types_v2senders_request_owner_type import ListDocumentTypesV2SendersRequestOwnerType
from .types.list_document_types_v2senders_response import ListDocumentTypesV2SendersResponse
from pydantic import ValidationError


class RawSendersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v1(
        self,
        *,
        owner_type: GetV1SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetV1SendersResponse]:
        """
        Retrieves all validation rules required for creating a sender in a specific country. Use these rules to validate sender information before submission.

        Parameters
        ----------
        owner_type : GetV1SendersRequestOwnerType
            Type of sender entity (individual or business)

        country : str
            Two-letter ISO country code (e.g., IN for India)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1SendersResponse]
            Sender validation rules retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders",
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
                    GetV1SendersResponse,
                    parse_obj_as(
                        type_=GetV1SendersResponse,  # type: ignore
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

    def get_ubo_rules_v1(
        self,
        *,
        owner_type: GetUboRulesV1SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetUboRulesV1SendersResponse]:
        """
        Retrieves validation rules for UBO information based on country and owner type. These rules specify all required fields for UBO verification.

        Parameters
        ----------
        owner_type : GetUboRulesV1SendersRequestOwnerType
            Type of sender entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUboRulesV1SendersResponse]
            UBO validation rules retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders/ubo",
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
                    GetUboRulesV1SendersResponse,
                    parse_obj_as(
                        type_=GetUboRulesV1SendersResponse,  # type: ignore
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

    def list_document_types_v1(
        self,
        *,
        owner_type: ListDocumentTypesV1SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDocumentTypesV1SendersResponse]:
        """
        Retrieves the list of required documents for sender verification. This includes business registration documents and identity proofs.

        Parameters
        ----------
        owner_type : ListDocumentTypesV1SendersRequestOwnerType
            Type of sender entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDocumentTypesV1SendersResponse]
            Required document types retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders/document-types",
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
                    ListDocumentTypesV1SendersResponse,
                    parse_obj_as(
                        type_=ListDocumentTypesV1SendersResponse,  # type: ignore
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

    def get_v2(
        self,
        *,
        owner_type: GetV2SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetV2SendersResponse]:
        """
        Retrieves all validation rules required for creating a sender in a specific country. V2 adds structured `supportedDocumentTypes` on identity fields, indicating which document types are available per country and their file upload requirements. The `documentNumber`, `documentFront`, and `documentBack` nested fields are removed as their requirements are conveyed by `supportedDocumentTypes`.

        Parameters
        ----------
        owner_type : GetV2SendersRequestOwnerType
            Type of sender entity (individual or business)

        country : str
            Two-letter ISO country code (e.g., IN for India)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV2SendersResponse]
            Sender validation rules retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/validation-rules/senders",
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
                    GetV2SendersResponse,
                    parse_obj_as(
                        type_=GetV2SendersResponse,  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_ubo_rules_v2(
        self,
        *,
        owner_type: GetUboRulesV2SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetUboRulesV2SendersResponse]:
        """
        Retrieves validation rules for UBO (Ultimate Beneficial Owner) information. V2 adds structured `supportedDocumentTypes` on the identity documentType field, indicating available document types per country and their file upload requirements.

        Parameters
        ----------
        owner_type : GetUboRulesV2SendersRequestOwnerType
            Type of sender entity (must be business for UBO rules)

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUboRulesV2SendersResponse]
            UBO validation rules retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/validation-rules/senders/ubo",
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
                    GetUboRulesV2SendersResponse,
                    parse_obj_as(
                        type_=GetUboRulesV2SendersResponse,  # type: ignore
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

    def list_document_types_v2(
        self,
        *,
        owner_type: ListDocumentTypesV2SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDocumentTypesV2SendersResponse]:
        """
        Retrieves the list of required documents for sender verification. This includes business registration documents and identity proofs. Same as V1.

        Parameters
        ----------
        owner_type : ListDocumentTypesV2SendersRequestOwnerType
            Type of sender entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDocumentTypesV2SendersResponse]
            Required document types retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/validation-rules/senders/document-types",
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
                    ListDocumentTypesV2SendersResponse,
                    parse_obj_as(
                        type_=ListDocumentTypesV2SendersResponse,  # type: ignore
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
    ) -> HttpResponse[ListCountriesSendersResponse]:
        """
        Retrieve a list of countries from which senders can originate payments.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCountriesSendersResponse]
            List of supported sender countries
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders/countries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCountriesSendersResponse,
                    parse_obj_as(
                        type_=ListCountriesSendersResponse,  # type: ignore
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


class AsyncRawSendersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v1(
        self,
        *,
        owner_type: GetV1SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetV1SendersResponse]:
        """
        Retrieves all validation rules required for creating a sender in a specific country. Use these rules to validate sender information before submission.

        Parameters
        ----------
        owner_type : GetV1SendersRequestOwnerType
            Type of sender entity (individual or business)

        country : str
            Two-letter ISO country code (e.g., IN for India)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1SendersResponse]
            Sender validation rules retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders",
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
                    GetV1SendersResponse,
                    parse_obj_as(
                        type_=GetV1SendersResponse,  # type: ignore
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

    async def get_ubo_rules_v1(
        self,
        *,
        owner_type: GetUboRulesV1SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetUboRulesV1SendersResponse]:
        """
        Retrieves validation rules for UBO information based on country and owner type. These rules specify all required fields for UBO verification.

        Parameters
        ----------
        owner_type : GetUboRulesV1SendersRequestOwnerType
            Type of sender entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUboRulesV1SendersResponse]
            UBO validation rules retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders/ubo",
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
                    GetUboRulesV1SendersResponse,
                    parse_obj_as(
                        type_=GetUboRulesV1SendersResponse,  # type: ignore
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

    async def list_document_types_v1(
        self,
        *,
        owner_type: ListDocumentTypesV1SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDocumentTypesV1SendersResponse]:
        """
        Retrieves the list of required documents for sender verification. This includes business registration documents and identity proofs.

        Parameters
        ----------
        owner_type : ListDocumentTypesV1SendersRequestOwnerType
            Type of sender entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDocumentTypesV1SendersResponse]
            Required document types retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders/document-types",
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
                    ListDocumentTypesV1SendersResponse,
                    parse_obj_as(
                        type_=ListDocumentTypesV1SendersResponse,  # type: ignore
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

    async def get_v2(
        self,
        *,
        owner_type: GetV2SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetV2SendersResponse]:
        """
        Retrieves all validation rules required for creating a sender in a specific country. V2 adds structured `supportedDocumentTypes` on identity fields, indicating which document types are available per country and their file upload requirements. The `documentNumber`, `documentFront`, and `documentBack` nested fields are removed as their requirements are conveyed by `supportedDocumentTypes`.

        Parameters
        ----------
        owner_type : GetV2SendersRequestOwnerType
            Type of sender entity (individual or business)

        country : str
            Two-letter ISO country code (e.g., IN for India)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV2SendersResponse]
            Sender validation rules retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/validation-rules/senders",
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
                    GetV2SendersResponse,
                    parse_obj_as(
                        type_=GetV2SendersResponse,  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_ubo_rules_v2(
        self,
        *,
        owner_type: GetUboRulesV2SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetUboRulesV2SendersResponse]:
        """
        Retrieves validation rules for UBO (Ultimate Beneficial Owner) information. V2 adds structured `supportedDocumentTypes` on the identity documentType field, indicating available document types per country and their file upload requirements.

        Parameters
        ----------
        owner_type : GetUboRulesV2SendersRequestOwnerType
            Type of sender entity (must be business for UBO rules)

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUboRulesV2SendersResponse]
            UBO validation rules retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/validation-rules/senders/ubo",
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
                    GetUboRulesV2SendersResponse,
                    parse_obj_as(
                        type_=GetUboRulesV2SendersResponse,  # type: ignore
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

    async def list_document_types_v2(
        self,
        *,
        owner_type: ListDocumentTypesV2SendersRequestOwnerType,
        country: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDocumentTypesV2SendersResponse]:
        """
        Retrieves the list of required documents for sender verification. This includes business registration documents and identity proofs. Same as V1.

        Parameters
        ----------
        owner_type : ListDocumentTypesV2SendersRequestOwnerType
            Type of sender entity

        country : str
            Two-letter ISO country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDocumentTypesV2SendersResponse]
            Required document types retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/validation-rules/senders/document-types",
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
                    ListDocumentTypesV2SendersResponse,
                    parse_obj_as(
                        type_=ListDocumentTypesV2SendersResponse,  # type: ignore
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
    ) -> AsyncHttpResponse[ListCountriesSendersResponse]:
        """
        Retrieve a list of countries from which senders can originate payments.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCountriesSendersResponse]
            List of supported sender countries
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/validation-rules/senders/countries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCountriesSendersResponse,
                    parse_obj_as(
                        type_=ListCountriesSendersResponse,  # type: ignore
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

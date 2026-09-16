
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error_response import ErrorResponse
from .types.get_fiat_deposits_response import GetFiatDepositsResponse
from .types.list_fiat_deposits_request_currency import ListFiatDepositsRequestCurrency
from .types.list_fiat_deposits_request_sort_by import ListFiatDepositsRequestSortBy
from .types.list_fiat_deposits_request_sort_order import ListFiatDepositsRequestSortOrder
from .types.list_fiat_deposits_response import ListFiatDepositsResponse
from pydantic import ValidationError


class RawFiatDepositsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListFiatDepositsRequestSortBy] = None,
        sort_order: typing.Optional[ListFiatDepositsRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        currency: typing.Optional[ListFiatDepositsRequestCurrency] = None,
        merchant_id: typing.Optional[str] = None,
        sender_id: typing.Optional[str] = None,
        deposit_bank_account_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListFiatDepositsResponse]:
        """
        Retrieve a paginated list of fiat deposits for a merchant. Only completed deposits are returned. Supports filtering by currency, sender, and deposit bank account.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListFiatDepositsRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListFiatDepositsRequestSortOrder]
            Sort order

        search : typing.Optional[str]
            Search query

        currency : typing.Optional[ListFiatDepositsRequestCurrency]
            Filter by fiat currency

        merchant_id : typing.Optional[str]
            Filter by merchant ID

        sender_id : typing.Optional[str]
            Filter by sender ID

        deposit_bank_account_id : typing.Optional[str]
            Filter by deposit bank account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFiatDepositsResponse]
            Fiat deposits retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/merchant/fiat-deposits",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "search": search,
                "currency": currency,
                "merchantId": merchant_id,
                "senderId": sender_id,
                "depositBankAccountId": deposit_bank_account_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFiatDepositsResponse,
                    parse_obj_as(
                        type_=ListFiatDepositsResponse,  # type: ignore
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

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFiatDepositsResponse]:
        """
        Retrieve a specific fiat deposit by its ID.

        Parameters
        ----------
        id : str
            Fiat deposit ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFiatDepositsResponse]
            Fiat deposit retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/merchant/fiat-deposits/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFiatDepositsResponse,
                    parse_obj_as(
                        type_=GetFiatDepositsResponse,  # type: ignore
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


class AsyncRawFiatDepositsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListFiatDepositsRequestSortBy] = None,
        sort_order: typing.Optional[ListFiatDepositsRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        currency: typing.Optional[ListFiatDepositsRequestCurrency] = None,
        merchant_id: typing.Optional[str] = None,
        sender_id: typing.Optional[str] = None,
        deposit_bank_account_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListFiatDepositsResponse]:
        """
        Retrieve a paginated list of fiat deposits for a merchant. Only completed deposits are returned. Supports filtering by currency, sender, and deposit bank account.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListFiatDepositsRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListFiatDepositsRequestSortOrder]
            Sort order

        search : typing.Optional[str]
            Search query

        currency : typing.Optional[ListFiatDepositsRequestCurrency]
            Filter by fiat currency

        merchant_id : typing.Optional[str]
            Filter by merchant ID

        sender_id : typing.Optional[str]
            Filter by sender ID

        deposit_bank_account_id : typing.Optional[str]
            Filter by deposit bank account ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFiatDepositsResponse]
            Fiat deposits retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/merchant/fiat-deposits",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "search": search,
                "currency": currency,
                "merchantId": merchant_id,
                "senderId": sender_id,
                "depositBankAccountId": deposit_bank_account_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFiatDepositsResponse,
                    parse_obj_as(
                        type_=ListFiatDepositsResponse,  # type: ignore
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

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFiatDepositsResponse]:
        """
        Retrieve a specific fiat deposit by its ID.

        Parameters
        ----------
        id : str
            Fiat deposit ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFiatDepositsResponse]
            Fiat deposit retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/merchant/fiat-deposits/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFiatDepositsResponse,
                    parse_obj_as(
                        type_=GetFiatDepositsResponse,  # type: ignore
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

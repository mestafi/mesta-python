
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
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error_response import ErrorResponse
from .types.list_transactions_request_sort_order import ListTransactionsRequestSortOrder
from .types.list_transactions_response import ListTransactionsResponse
from pydantic import ValidationError


class RawTransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        sender_id: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        virtual_transaction_id: typing.Optional[str] = None,
        order_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[ListTransactionsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTransactionsResponse]:
        """
        Retrieves a paginated list of merchant transactions with optional filtering.

        Parameters
        ----------
        currency : typing.Optional[str]
            Filter by currency code

        type : typing.Optional[str]
            Filter by transaction type

        sender_id : typing.Optional[str]
            Filter by sender ID

        transaction_id : typing.Optional[str]
            Filter by transaction ID

        virtual_transaction_id : typing.Optional[str]
            Filter by virtual transaction ID

        order_id : typing.Optional[str]
            Filter by order ID

        page_size : typing.Optional[int]
            Records per page

        page : typing.Optional[int]
            Page number

        sort_by : typing.Optional[str]
            Sort column

        sort_order : typing.Optional[ListTransactionsRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTransactionsResponse]
            Merchant transactions retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/merchant-transactions",
            method="GET",
            params={
                "currency": currency,
                "type": type,
                "senderId": sender_id,
                "transactionId": transaction_id,
                "virtualTransactionId": virtual_transaction_id,
                "orderId": order_id,
                "pageSize": page_size,
                "page": page,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsResponse,
                    parse_obj_as(
                        type_=ListTransactionsResponse,  # type: ignore
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


class AsyncRawTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        currency: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        sender_id: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        virtual_transaction_id: typing.Optional[str] = None,
        order_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[ListTransactionsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTransactionsResponse]:
        """
        Retrieves a paginated list of merchant transactions with optional filtering.

        Parameters
        ----------
        currency : typing.Optional[str]
            Filter by currency code

        type : typing.Optional[str]
            Filter by transaction type

        sender_id : typing.Optional[str]
            Filter by sender ID

        transaction_id : typing.Optional[str]
            Filter by transaction ID

        virtual_transaction_id : typing.Optional[str]
            Filter by virtual transaction ID

        order_id : typing.Optional[str]
            Filter by order ID

        page_size : typing.Optional[int]
            Records per page

        page : typing.Optional[int]
            Page number

        sort_by : typing.Optional[str]
            Sort column

        sort_order : typing.Optional[ListTransactionsRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTransactionsResponse]
            Merchant transactions retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/merchant-transactions",
            method="GET",
            params={
                "currency": currency,
                "type": type,
                "senderId": sender_id,
                "transactionId": transaction_id,
                "virtualTransactionId": virtual_transaction_id,
                "orderId": order_id,
                "pageSize": page_size,
                "page": page,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsResponse,
                    parse_obj_as(
                        type_=ListTransactionsResponse,  # type: ignore
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


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
from .types.get_stablecoin_deposits_response import GetStablecoinDepositsResponse
from .types.list_stablecoin_deposits_request_currency import ListStablecoinDepositsRequestCurrency
from .types.list_stablecoin_deposits_request_sort_by import ListStablecoinDepositsRequestSortBy
from .types.list_stablecoin_deposits_request_sort_order import ListStablecoinDepositsRequestSortOrder
from .types.list_stablecoin_deposits_request_status import ListStablecoinDepositsRequestStatus
from .types.list_stablecoin_deposits_request_swa_risk_level import ListStablecoinDepositsRequestSwaRiskLevel
from .types.list_stablecoin_deposits_response import ListStablecoinDepositsResponse
from pydantic import ValidationError


class RawStablecoinDepositsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListStablecoinDepositsRequestSortBy] = None,
        sort_order: typing.Optional[ListStablecoinDepositsRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        currency: typing.Optional[ListStablecoinDepositsRequestCurrency] = None,
        merchant_id: typing.Optional[str] = None,
        sender_id: typing.Optional[str] = None,
        status: typing.Optional[ListStablecoinDepositsRequestStatus] = None,
        swa_risk_level: typing.Optional[ListStablecoinDepositsRequestSwaRiskLevel] = None,
        source_wallet_address: typing.Optional[str] = None,
        deposit_wallet_address_id: typing.Optional[str] = None,
        is_pooled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListStablecoinDepositsResponse]:
        """
        Retrieve a paginated list of stablecoin deposits for a merchant. Supports filtering by currency, status, sender, and risk level.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListStablecoinDepositsRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListStablecoinDepositsRequestSortOrder]
            Sort order

        search : typing.Optional[str]
            Search query

        currency : typing.Optional[ListStablecoinDepositsRequestCurrency]
            Filter by stablecoin currency

        merchant_id : typing.Optional[str]
            Filter by merchant ID

        sender_id : typing.Optional[str]
            Filter by sender ID

        status : typing.Optional[ListStablecoinDepositsRequestStatus]
            Filter by deposit status

        swa_risk_level : typing.Optional[ListStablecoinDepositsRequestSwaRiskLevel]
            Filter by SWA risk level

        source_wallet_address : typing.Optional[str]
            Filter by source wallet address

        deposit_wallet_address_id : typing.Optional[str]
            Filter by deposit wallet address ID

        is_pooled : typing.Optional[bool]
            Optional. true returns only pooled merchant account deposits (merchant-level top-ups, no sender attribution); false returns only sender-attributed deposits; omit for all deposits. Pooled Merchant Accounts is available to select merchants only — please reach out to Mesta support to have it enabled for your account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListStablecoinDepositsResponse]
            Stablecoin deposits retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/merchant/stablecoin-deposits",
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
                "status": status,
                "swaRiskLevel": swa_risk_level,
                "sourceWalletAddress": source_wallet_address,
                "depositWalletAddressId": deposit_wallet_address_id,
                "isPooled": is_pooled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListStablecoinDepositsResponse,
                    parse_obj_as(
                        type_=ListStablecoinDepositsResponse,  # type: ignore
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
    ) -> HttpResponse[GetStablecoinDepositsResponse]:
        """
        Retrieve a specific stablecoin deposit by its ID.

        Parameters
        ----------
        id : str
            Stablecoin deposit ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStablecoinDepositsResponse]
            Stablecoin deposit retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/merchant/stablecoin-deposits/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStablecoinDepositsResponse,
                    parse_obj_as(
                        type_=GetStablecoinDepositsResponse,  # type: ignore
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


class AsyncRawStablecoinDepositsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListStablecoinDepositsRequestSortBy] = None,
        sort_order: typing.Optional[ListStablecoinDepositsRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        currency: typing.Optional[ListStablecoinDepositsRequestCurrency] = None,
        merchant_id: typing.Optional[str] = None,
        sender_id: typing.Optional[str] = None,
        status: typing.Optional[ListStablecoinDepositsRequestStatus] = None,
        swa_risk_level: typing.Optional[ListStablecoinDepositsRequestSwaRiskLevel] = None,
        source_wallet_address: typing.Optional[str] = None,
        deposit_wallet_address_id: typing.Optional[str] = None,
        is_pooled: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListStablecoinDepositsResponse]:
        """
        Retrieve a paginated list of stablecoin deposits for a merchant. Supports filtering by currency, status, sender, and risk level.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListStablecoinDepositsRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListStablecoinDepositsRequestSortOrder]
            Sort order

        search : typing.Optional[str]
            Search query

        currency : typing.Optional[ListStablecoinDepositsRequestCurrency]
            Filter by stablecoin currency

        merchant_id : typing.Optional[str]
            Filter by merchant ID

        sender_id : typing.Optional[str]
            Filter by sender ID

        status : typing.Optional[ListStablecoinDepositsRequestStatus]
            Filter by deposit status

        swa_risk_level : typing.Optional[ListStablecoinDepositsRequestSwaRiskLevel]
            Filter by SWA risk level

        source_wallet_address : typing.Optional[str]
            Filter by source wallet address

        deposit_wallet_address_id : typing.Optional[str]
            Filter by deposit wallet address ID

        is_pooled : typing.Optional[bool]
            Optional. true returns only pooled merchant account deposits (merchant-level top-ups, no sender attribution); false returns only sender-attributed deposits; omit for all deposits. Pooled Merchant Accounts is available to select merchants only — please reach out to Mesta support to have it enabled for your account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListStablecoinDepositsResponse]
            Stablecoin deposits retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/merchant/stablecoin-deposits",
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
                "status": status,
                "swaRiskLevel": swa_risk_level,
                "sourceWalletAddress": source_wallet_address,
                "depositWalletAddressId": deposit_wallet_address_id,
                "isPooled": is_pooled,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListStablecoinDepositsResponse,
                    parse_obj_as(
                        type_=ListStablecoinDepositsResponse,  # type: ignore
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
    ) -> AsyncHttpResponse[GetStablecoinDepositsResponse]:
        """
        Retrieve a specific stablecoin deposit by its ID.

        Parameters
        ----------
        id : str
            Stablecoin deposit ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStablecoinDepositsResponse]
            Stablecoin deposit retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/merchant/stablecoin-deposits/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStablecoinDepositsResponse,
                    parse_obj_as(
                        type_=GetStablecoinDepositsResponse,  # type: ignore
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


import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.conflict_error import ConflictError
from ...errors.gone_error import GoneError
from ...errors.service_unavailable_error import ServiceUnavailableError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.error_response import ErrorResponse
from .types.create_claims_response import CreateClaimsResponse
from .types.get_status_claims_response import GetStatusClaimsResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawClaimsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_status(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetStatusClaimsResponse]:
        """
        A non-consuming read of a claim token: `fresh`, `seeding` (with the current `seed.step`), `expired`, `used` or `killed`, with the counts of the sample data and, for `fresh`, the keys created before the claim and the endpoint hosts. The token travels in the body because request paths are logged. No authentication; 20 per hour per network address, a `seeding` answer uncounted. A fresh answer is also uncounted. Expired, unknown and malformed tokens return data containing only status: expired, with no sandbox metadata.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`. Sent in the body, never in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStatusClaimsResponse]
            The token's state.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sandbox/claims/status",
            method="POST",
            json={
                "token": token,
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
                    GetStatusClaimsResponse,
                    parse_obj_as(
                        type_=GetStatusClaimsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def create(
        self,
        *,
        token: str,
        email: str,
        full_name: str,
        password: str,
        accept_terms: bool,
        keep_pre_claim_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateClaimsResponse]:
        """
        Makes the caller the owner of an unclaimed sandbox: writes the email, name and password onto the sandbox's user, re-stamps the terms acceptance, revokes the keys created before the claim and the webhook endpoints created before it, rotates the webhook signing key and recreates the Mesta test endpoint, and mints one fresh standard pair returned once, unless `keepPreClaimKeys` is true. Returns the sandbox and a portal session. The sandbox then has 72 hours to verify the email. Single use, atomic on the token and the email. No authentication; 20 per hour per network address; a 409 SANDBOX_SEEDING answer is uncounted and leaves the token valid. keepPreClaimKeys keeps the keys, endpoints and signing key together; keys in the success body is then an empty array. The 20-per-rolling-hour claim counter counts token-check refusals only; probes answering `seeding` and claims answering SANDBOX_SEEDING are uncounted.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`.

        email : str

        full_name : str
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.

        password : str
            12 to 128 characters; common passwords are refused.

        accept_terms : bool
            Must be true; 422 with the terms URL and version otherwise.

        keep_pre_claim_keys : typing.Optional[bool]
            Keep the pre-claim keys, their webhook endpoints and signing key together. Otherwise revoke the keys, delete the endpoints, rotate the signing key, recreate the Mesta test endpoint and return one fresh pair once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateClaimsResponse]
            The claimed sandbox, with the fresh key pair once unless the pre-claim keys were kept, and a portal session.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sandbox/claims",
            method="POST",
            json={
                "token": token,
                "email": email,
                "fullName": full_name,
                "password": password,
                "acceptTerms": accept_terms,
                "keepPreClaimKeys": keep_pre_claim_keys,
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
                    CreateClaimsResponse,
                    parse_obj_as(
                        type_=CreateClaimsResponse,  # type: ignore
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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


class AsyncRawClaimsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_status(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetStatusClaimsResponse]:
        """
        A non-consuming read of a claim token: `fresh`, `seeding` (with the current `seed.step`), `expired`, `used` or `killed`, with the counts of the sample data and, for `fresh`, the keys created before the claim and the endpoint hosts. The token travels in the body because request paths are logged. No authentication; 20 per hour per network address, a `seeding` answer uncounted. A fresh answer is also uncounted. Expired, unknown and malformed tokens return data containing only status: expired, with no sandbox metadata.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`. Sent in the body, never in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStatusClaimsResponse]
            The token's state.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sandbox/claims/status",
            method="POST",
            json={
                "token": token,
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
                    GetStatusClaimsResponse,
                    parse_obj_as(
                        type_=GetStatusClaimsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def create(
        self,
        *,
        token: str,
        email: str,
        full_name: str,
        password: str,
        accept_terms: bool,
        keep_pre_claim_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateClaimsResponse]:
        """
        Makes the caller the owner of an unclaimed sandbox: writes the email, name and password onto the sandbox's user, re-stamps the terms acceptance, revokes the keys created before the claim and the webhook endpoints created before it, rotates the webhook signing key and recreates the Mesta test endpoint, and mints one fresh standard pair returned once, unless `keepPreClaimKeys` is true. Returns the sandbox and a portal session. The sandbox then has 72 hours to verify the email. Single use, atomic on the token and the email. No authentication; 20 per hour per network address; a 409 SANDBOX_SEEDING answer is uncounted and leaves the token valid. keepPreClaimKeys keeps the keys, endpoints and signing key together; keys in the success body is then an empty array. The 20-per-rolling-hour claim counter counts token-check refusals only; probes answering `seeding` and claims answering SANDBOX_SEEDING are uncounted.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`.

        email : str

        full_name : str
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.

        password : str
            12 to 128 characters; common passwords are refused.

        accept_terms : bool
            Must be true; 422 with the terms URL and version otherwise.

        keep_pre_claim_keys : typing.Optional[bool]
            Keep the pre-claim keys, their webhook endpoints and signing key together. Otherwise revoke the keys, delete the endpoints, rotate the signing key, recreate the Mesta test endpoint and return one fresh pair once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateClaimsResponse]
            The claimed sandbox, with the fresh key pair once unless the pre-claim keys were kept, and a portal session.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sandbox/claims",
            method="POST",
            json={
                "token": token,
                "email": email,
                "fullName": full_name,
                "password": password,
                "acceptTerms": accept_terms,
                "keepPreClaimKeys": keep_pre_claim_keys,
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
                    CreateClaimsResponse,
                    parse_obj_as(
                        type_=CreateClaimsResponse,  # type: ignore
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

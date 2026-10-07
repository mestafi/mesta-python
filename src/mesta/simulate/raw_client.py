
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.simulate_deposit_response import SimulateDepositResponse
from ..types.simulate_order_transition_response import SimulateOrderTransitionResponse
from ..types.simulate_tos_accept_response import SimulateTosAcceptResponse
from ..types.simulate_webhook_fire_response import SimulateWebhookFireResponse
from .types.simulate_deposit_request_outcome import SimulateDepositRequestOutcome
from .types.simulate_deposit_request_owner_type import SimulateDepositRequestOwnerType
from .types.simulate_order_transition_request_reason_code import SimulateOrderTransitionRequestReasonCode
from .types.simulate_order_transition_request_status import SimulateOrderTransitionRequestStatus
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawSimulateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def deposit(
        self,
        *,
        owner_type: SimulateDepositRequestOwnerType,
        owner_id: str,
        currency: str,
        amount: str,
        outcome: SimulateDepositRequestOutcome,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SimulateDepositResponse]:
        """
        Writes a settled or rejected deposit for a sender or your merchant, fiat or stablecoin, with its ledger entries and its `fiat_deposit:*` or `stablecoin_deposit:*` event. A settled deposit raises the balance when the call returns. The owner must be yours (404 otherwise). Budget: 50 calls and 500,000 currency units per sandbox per rolling day (409 SANDBOX_CAP_EXCEEDED above). Requires `merchant:sender:write` for a sender and `merchant:sandbox:write` for your own merchant (ownerType merchant); a portal session of the merchant satisfies either. Sandbox only. Guide: https://docs.mesta.xyz/docs/funding-test-senders.

        Parameters
        ----------
        owner_type : SimulateDepositRequestOwnerType

        owner_id : str
            The sender's id, or your merchant id.

        currency : str
            Any fiat or stablecoin currency the sandbox serves, for example USD or USDC_POL.

        amount : str
            A decimal string; up to 18 decimals for stablecoins, 2 for fiat.

        outcome : SimulateDepositRequestOutcome
            `settled` credits the balance and publishes the settled event; `rejected` writes a rejected deposit with no balance change.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimulateDepositResponse]
            The deposit.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/simulate/deposits",
            method="POST",
            json={
                "ownerType": owner_type,
                "ownerId": owner_id,
                "currency": currency,
                "amount": amount,
                "outcome": outcome,
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
                    SimulateDepositResponse,
                    parse_obj_as(
                        type_=SimulateDepositResponse,  # type: ignore
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

    def transition_order(
        self,
        id: str,
        *,
        status: SimulateOrderTransitionRequestStatus,
        reason_code: typing.Optional[SimulateOrderTransitionRequestReasonCode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SimulateOrderTransitionResponse]:
        """
        Stops the order's running workflow, moves the order to the given status and publishes the matching `order:*` event (none for need_review, payment_submitted, refund_in_progress and refunded). `reasonCode` is required for cancelled and rejected and must come from the catalogue; the remark is never free text. The order must be yours (404 otherwise). Shares a budget of 200 calls per sandbox per rolling day with POST /v1/simulate/webhooks/fire. Requires `merchant:order:write`. Sandbox only.

        Parameters
        ----------
        id : str
            The order id.

        status : SimulateOrderTransitionRequestStatus
            The target status. No event exists for need_review, payment_submitted, refund_in_progress and refunded.

        reason_code : typing.Optional[SimulateOrderTransitionRequestReasonCode]
            Required for `cancelled` (requested_by_sender, duplicate_order, quote_expired) and `rejected` (compliance_declined, beneficiary_unverified, invalid_payment_details). Any other value answers 400.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimulateOrderTransitionResponse]
            The order's new status and the event published.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/simulate/orders/{encode_path_param(id)}/transition",
            method="POST",
            json={
                "status": status,
                "reasonCode": reason_code,
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
                    SimulateOrderTransitionResponse,
                    parse_obj_as(
                        type_=SimulateOrderTransitionResponse,  # type: ignore
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

    def accept_sender_terms(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SimulateTosAcceptResponse]:
        """
        Accepts the sender's pending terms of service and publishes `sender:tos_accepted`, in place of the link a real sender would open. The sender must be yours (404 otherwise). Requires `merchant:sender:write`. Sandbox only.

        Parameters
        ----------
        id : str
            The sender id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimulateTosAcceptResponse]
            Accepted.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/simulate/senders/{encode_path_param(id)}/tos-accept",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimulateTosAcceptResponse,
                    parse_obj_as(
                        type_=SimulateTosAcceptResponse,  # type: ignore
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

    def fire_webhook(
        self, *, event: str, aggregate_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SimulateWebhookFireResponse]:
        """
        Publishes a real external event again for one of your objects, so the whole pipeline runs: queueing, signing, delivery and the delivery log. Counts against the sandbox's daily delivery budget and shares a budget of 200 calls per sandbox per rolling day with `POST /v1/simulate/orders/{id}/transition`. Requires `merchant:webhook-events:replay`. Sandbox only. Outbound webhook deliveries (not this HTTP response) carry `Mesta-Signature: t=<Unix seconds>,v1=<signature>` on both environments, where the signature is a lowercase hex HMAC-SHA256 over `${t}.` followed by the raw body bytes. Reject a t more than 300 seconds from the receiver clock and compare signatures in constant time. Each retry and resend has a new t and signature. Sandbox delivery bodies carry a top-level `environment`, set to `sandbox` and inside the signed bytes; production bodies carry none until the announced cutover date, then `production`. After verifying the signature, a production endpoint accepts an event with no `environment` or with `production` and rejects any other value, and a sandbox endpoint accepts only `sandbox`, so the same check keeps working through the cutover; use one endpoint and one signing key per environment. `X-Webhook-Signature`, a lowercase hex HMAC-SHA256 of the raw body alone, is kept for existing production integrations; its sunset will be announced. `X-Mesta-Plane: sandbox` is sent only on sandbox deliveries and is absent on production. Sandbox deliveries make three attempts (two retries); production keeps five attempts.

        Parameters
        ----------
        event : str
            A live event name, for example order:success.

        aggregate_id : str
            The id of one of your objects of the event's entity type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SimulateWebhookFireResponse]
            Published.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/simulate/webhooks/fire",
            method="POST",
            json={
                "event": event,
                "aggregateId": aggregate_id,
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
                    SimulateWebhookFireResponse,
                    parse_obj_as(
                        type_=SimulateWebhookFireResponse,  # type: ignore
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


class AsyncRawSimulateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def deposit(
        self,
        *,
        owner_type: SimulateDepositRequestOwnerType,
        owner_id: str,
        currency: str,
        amount: str,
        outcome: SimulateDepositRequestOutcome,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SimulateDepositResponse]:
        """
        Writes a settled or rejected deposit for a sender or your merchant, fiat or stablecoin, with its ledger entries and its `fiat_deposit:*` or `stablecoin_deposit:*` event. A settled deposit raises the balance when the call returns. The owner must be yours (404 otherwise). Budget: 50 calls and 500,000 currency units per sandbox per rolling day (409 SANDBOX_CAP_EXCEEDED above). Requires `merchant:sender:write` for a sender and `merchant:sandbox:write` for your own merchant (ownerType merchant); a portal session of the merchant satisfies either. Sandbox only. Guide: https://docs.mesta.xyz/docs/funding-test-senders.

        Parameters
        ----------
        owner_type : SimulateDepositRequestOwnerType

        owner_id : str
            The sender's id, or your merchant id.

        currency : str
            Any fiat or stablecoin currency the sandbox serves, for example USD or USDC_POL.

        amount : str
            A decimal string; up to 18 decimals for stablecoins, 2 for fiat.

        outcome : SimulateDepositRequestOutcome
            `settled` credits the balance and publishes the settled event; `rejected` writes a rejected deposit with no balance change.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimulateDepositResponse]
            The deposit.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/simulate/deposits",
            method="POST",
            json={
                "ownerType": owner_type,
                "ownerId": owner_id,
                "currency": currency,
                "amount": amount,
                "outcome": outcome,
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
                    SimulateDepositResponse,
                    parse_obj_as(
                        type_=SimulateDepositResponse,  # type: ignore
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

    async def transition_order(
        self,
        id: str,
        *,
        status: SimulateOrderTransitionRequestStatus,
        reason_code: typing.Optional[SimulateOrderTransitionRequestReasonCode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SimulateOrderTransitionResponse]:
        """
        Stops the order's running workflow, moves the order to the given status and publishes the matching `order:*` event (none for need_review, payment_submitted, refund_in_progress and refunded). `reasonCode` is required for cancelled and rejected and must come from the catalogue; the remark is never free text. The order must be yours (404 otherwise). Shares a budget of 200 calls per sandbox per rolling day with POST /v1/simulate/webhooks/fire. Requires `merchant:order:write`. Sandbox only.

        Parameters
        ----------
        id : str
            The order id.

        status : SimulateOrderTransitionRequestStatus
            The target status. No event exists for need_review, payment_submitted, refund_in_progress and refunded.

        reason_code : typing.Optional[SimulateOrderTransitionRequestReasonCode]
            Required for `cancelled` (requested_by_sender, duplicate_order, quote_expired) and `rejected` (compliance_declined, beneficiary_unverified, invalid_payment_details). Any other value answers 400.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimulateOrderTransitionResponse]
            The order's new status and the event published.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/simulate/orders/{encode_path_param(id)}/transition",
            method="POST",
            json={
                "status": status,
                "reasonCode": reason_code,
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
                    SimulateOrderTransitionResponse,
                    parse_obj_as(
                        type_=SimulateOrderTransitionResponse,  # type: ignore
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

    async def accept_sender_terms(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SimulateTosAcceptResponse]:
        """
        Accepts the sender's pending terms of service and publishes `sender:tos_accepted`, in place of the link a real sender would open. The sender must be yours (404 otherwise). Requires `merchant:sender:write`. Sandbox only.

        Parameters
        ----------
        id : str
            The sender id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimulateTosAcceptResponse]
            Accepted.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/simulate/senders/{encode_path_param(id)}/tos-accept",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SimulateTosAcceptResponse,
                    parse_obj_as(
                        type_=SimulateTosAcceptResponse,  # type: ignore
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

    async def fire_webhook(
        self, *, event: str, aggregate_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SimulateWebhookFireResponse]:
        """
        Publishes a real external event again for one of your objects, so the whole pipeline runs: queueing, signing, delivery and the delivery log. Counts against the sandbox's daily delivery budget and shares a budget of 200 calls per sandbox per rolling day with `POST /v1/simulate/orders/{id}/transition`. Requires `merchant:webhook-events:replay`. Sandbox only. Outbound webhook deliveries (not this HTTP response) carry `Mesta-Signature: t=<Unix seconds>,v1=<signature>` on both environments, where the signature is a lowercase hex HMAC-SHA256 over `${t}.` followed by the raw body bytes. Reject a t more than 300 seconds from the receiver clock and compare signatures in constant time. Each retry and resend has a new t and signature. Sandbox delivery bodies carry a top-level `environment`, set to `sandbox` and inside the signed bytes; production bodies carry none until the announced cutover date, then `production`. After verifying the signature, a production endpoint accepts an event with no `environment` or with `production` and rejects any other value, and a sandbox endpoint accepts only `sandbox`, so the same check keeps working through the cutover; use one endpoint and one signing key per environment. `X-Webhook-Signature`, a lowercase hex HMAC-SHA256 of the raw body alone, is kept for existing production integrations; its sunset will be announced. `X-Mesta-Plane: sandbox` is sent only on sandbox deliveries and is absent on production. Sandbox deliveries make three attempts (two retries); production keeps five attempts.

        Parameters
        ----------
        event : str
            A live event name, for example order:success.

        aggregate_id : str
            The id of one of your objects of the event's entity type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SimulateWebhookFireResponse]
            Published.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/simulate/webhooks/fire",
            method="POST",
            json={
                "event": event,
                "aggregateId": aggregate_id,
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
                    SimulateWebhookFireResponse,
                    parse_obj_as(
                        type_=SimulateWebhookFireResponse,  # type: ignore
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

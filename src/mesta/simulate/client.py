
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.simulate_deposit_response import SimulateDepositResponse
from ..types.simulate_order_transition_response import SimulateOrderTransitionResponse
from ..types.simulate_tos_accept_response import SimulateTosAcceptResponse
from ..types.simulate_webhook_fire_response import SimulateWebhookFireResponse
from .raw_client import AsyncRawSimulateClient, RawSimulateClient
from .types.simulate_deposit_request_outcome import SimulateDepositRequestOutcome
from .types.simulate_deposit_request_owner_type import SimulateDepositRequestOwnerType
from .types.simulate_order_transition_request_reason_code import SimulateOrderTransitionRequestReasonCode
from .types.simulate_order_transition_request_status import SimulateOrderTransitionRequestStatus

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SimulateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSimulateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSimulateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSimulateClient
        """
        return self._raw_client

    def deposit(
        self,
        *,
        owner_type: SimulateDepositRequestOwnerType,
        owner_id: str,
        currency: str,
        amount: str,
        outcome: SimulateDepositRequestOutcome,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateDepositResponse:
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
        SimulateDepositResponse
            The deposit.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.simulate.deposit(
            owner_type="sender",
            owner_id="00000000-0000-4000-a000-000000000001",
            currency="USD",
            amount="500.00",
            outcome="settled",
        )
        """
        _response = self._raw_client.deposit(
            owner_type=owner_type,
            owner_id=owner_id,
            currency=currency,
            amount=amount,
            outcome=outcome,
            request_options=request_options,
        )
        return _response.data

    def transition_order(
        self,
        id: str,
        *,
        status: SimulateOrderTransitionRequestStatus,
        reason_code: typing.Optional[SimulateOrderTransitionRequestReasonCode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateOrderTransitionResponse:
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
        SimulateOrderTransitionResponse
            The order's new status and the event published.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.simulate.transition_order(
            id="id",
            status="rejected",
            reason_code="compliance_declined",
        )
        """
        _response = self._raw_client.transition_order(
            id, status=status, reason_code=reason_code, request_options=request_options
        )
        return _response.data

    def accept_sender_terms(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SimulateTosAcceptResponse:
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
        SimulateTosAcceptResponse
            Accepted.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.simulate.accept_sender_terms(
            id="id",
        )
        """
        _response = self._raw_client.accept_sender_terms(id, request_options=request_options)
        return _response.data

    def fire_webhook(
        self, *, event: str, aggregate_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimulateWebhookFireResponse:
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
        SimulateWebhookFireResponse
            Published.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.simulate.fire_webhook(
            event="order:success",
            aggregate_id="00000000-0000-4000-a000-000000000006",
        )
        """
        _response = self._raw_client.fire_webhook(
            event=event, aggregate_id=aggregate_id, request_options=request_options
        )
        return _response.data


class AsyncSimulateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSimulateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSimulateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSimulateClient
        """
        return self._raw_client

    async def deposit(
        self,
        *,
        owner_type: SimulateDepositRequestOwnerType,
        owner_id: str,
        currency: str,
        amount: str,
        outcome: SimulateDepositRequestOutcome,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateDepositResponse:
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
        SimulateDepositResponse
            The deposit.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.simulate.deposit(
                owner_type="sender",
                owner_id="00000000-0000-4000-a000-000000000001",
                currency="USD",
                amount="500.00",
                outcome="settled",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit(
            owner_type=owner_type,
            owner_id=owner_id,
            currency=currency,
            amount=amount,
            outcome=outcome,
            request_options=request_options,
        )
        return _response.data

    async def transition_order(
        self,
        id: str,
        *,
        status: SimulateOrderTransitionRequestStatus,
        reason_code: typing.Optional[SimulateOrderTransitionRequestReasonCode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateOrderTransitionResponse:
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
        SimulateOrderTransitionResponse
            The order's new status and the event published.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.simulate.transition_order(
                id="id",
                status="rejected",
                reason_code="compliance_declined",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transition_order(
            id, status=status, reason_code=reason_code, request_options=request_options
        )
        return _response.data

    async def accept_sender_terms(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SimulateTosAcceptResponse:
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
        SimulateTosAcceptResponse
            Accepted.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.simulate.accept_sender_terms(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_sender_terms(id, request_options=request_options)
        return _response.data

    async def fire_webhook(
        self, *, event: str, aggregate_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SimulateWebhookFireResponse:
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
        SimulateWebhookFireResponse
            Published.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.simulate.fire_webhook(
                event="order:success",
                aggregate_id="00000000-0000-4000-a000-000000000006",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fire_webhook(
            event=event, aggregate_id=aggregate_id, request_options=request_options
        )
        return _response.data

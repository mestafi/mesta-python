
from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import MestaEnvironment

if typing.TYPE_CHECKING:
    from .api_keys.client import ApiKeysClient, AsyncApiKeysClient
    from .auth.client import AsyncAuthClient, AuthClient
    from .beneficiaries.client import AsyncBeneficiariesClient, BeneficiariesClient
    from .events.client import AsyncEventsClient, EventsClient
    from .merchants.client import AsyncMerchantsClient, MerchantsClient
    from .orders.client import AsyncOrdersClient, OrdersClient
    from .payment_methods.client import AsyncPaymentMethodsClient, PaymentMethodsClient
    from .quotes.client import AsyncQuotesClient, QuotesClient
    from .senders.client import AsyncSendersClient, SendersClient
    from .transfers.client import AsyncTransfersClient, TransfersClient
    from .validation_rules.client import AsyncValidationRulesClient, ValidationRulesClient
    from .wallet_addresses.client import AsyncWalletAddressesClient, WalletAddressesClient
    from .webhooks.client import AsyncWebhooksClient, WebhooksClient


class Mesta:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MestaEnvironment
        The environment to use for requests from the client. from .environment import MestaEnvironment



        Defaults to MestaEnvironment.PRODUCTION



    api_secret : str
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from mesta import Mesta

    client = Mesta(
        api_secret="YOUR_API_SECRET",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MestaEnvironment = MestaEnvironment.PRODUCTION,
        api_secret: str,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_secret=api_secret,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._merchants: typing.Optional[MerchantsClient] = None
        self._wallet_addresses: typing.Optional[WalletAddressesClient] = None
        self._senders: typing.Optional[SendersClient] = None
        self._beneficiaries: typing.Optional[BeneficiariesClient] = None
        self._quotes: typing.Optional[QuotesClient] = None
        self._orders: typing.Optional[OrdersClient] = None
        self._webhooks: typing.Optional[WebhooksClient] = None
        self._payment_methods: typing.Optional[PaymentMethodsClient] = None
        self._validation_rules: typing.Optional[ValidationRulesClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._auth: typing.Optional[AuthClient] = None
        self._api_keys: typing.Optional[ApiKeysClient] = None
        self._transfers: typing.Optional[TransfersClient] = None

    @property
    def merchants(self):
        if self._merchants is None:
            from .merchants.client import MerchantsClient  # noqa: E402

            self._merchants = MerchantsClient(client_wrapper=self._client_wrapper)
        return self._merchants

    @property
    def wallet_addresses(self):
        if self._wallet_addresses is None:
            from .wallet_addresses.client import WalletAddressesClient  # noqa: E402

            self._wallet_addresses = WalletAddressesClient(client_wrapper=self._client_wrapper)
        return self._wallet_addresses

    @property
    def senders(self):
        if self._senders is None:
            from .senders.client import SendersClient  # noqa: E402

            self._senders = SendersClient(client_wrapper=self._client_wrapper)
        return self._senders

    @property
    def beneficiaries(self):
        if self._beneficiaries is None:
            from .beneficiaries.client import BeneficiariesClient  # noqa: E402

            self._beneficiaries = BeneficiariesClient(client_wrapper=self._client_wrapper)
        return self._beneficiaries

    @property
    def quotes(self):
        if self._quotes is None:
            from .quotes.client import QuotesClient  # noqa: E402

            self._quotes = QuotesClient(client_wrapper=self._client_wrapper)
        return self._quotes

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import OrdersClient  # noqa: E402

            self._orders = OrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient  # noqa: E402

            self._webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def payment_methods(self):
        if self._payment_methods is None:
            from .payment_methods.client import PaymentMethodsClient  # noqa: E402

            self._payment_methods = PaymentMethodsClient(client_wrapper=self._client_wrapper)
        return self._payment_methods

    @property
    def validation_rules(self):
        if self._validation_rules is None:
            from .validation_rules.client import ValidationRulesClient  # noqa: E402

            self._validation_rules = ValidationRulesClient(client_wrapper=self._client_wrapper)
        return self._validation_rules

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient  # noqa: E402

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AuthClient  # noqa: E402

            self._auth = AuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient  # noqa: E402

            self._api_keys = ApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def transfers(self):
        if self._transfers is None:
            from .transfers.client import TransfersClient  # noqa: E402

            self._transfers = TransfersClient(client_wrapper=self._client_wrapper)
        return self._transfers


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp  # type: ignore[import-not-found]
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncMesta:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MestaEnvironment
        The environment to use for requests from the client. from .environment import MestaEnvironment



        Defaults to MestaEnvironment.PRODUCTION



    api_secret : str
    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from mesta import AsyncMesta

    client = AsyncMesta(
        api_secret="YOUR_API_SECRET",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MestaEnvironment = MestaEnvironment.PRODUCTION,
        api_secret: str,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_secret=api_secret,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._merchants: typing.Optional[AsyncMerchantsClient] = None
        self._wallet_addresses: typing.Optional[AsyncWalletAddressesClient] = None
        self._senders: typing.Optional[AsyncSendersClient] = None
        self._beneficiaries: typing.Optional[AsyncBeneficiariesClient] = None
        self._quotes: typing.Optional[AsyncQuotesClient] = None
        self._orders: typing.Optional[AsyncOrdersClient] = None
        self._webhooks: typing.Optional[AsyncWebhooksClient] = None
        self._payment_methods: typing.Optional[AsyncPaymentMethodsClient] = None
        self._validation_rules: typing.Optional[AsyncValidationRulesClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._auth: typing.Optional[AsyncAuthClient] = None
        self._api_keys: typing.Optional[AsyncApiKeysClient] = None
        self._transfers: typing.Optional[AsyncTransfersClient] = None

    @property
    def merchants(self):
        if self._merchants is None:
            from .merchants.client import AsyncMerchantsClient  # noqa: E402

            self._merchants = AsyncMerchantsClient(client_wrapper=self._client_wrapper)
        return self._merchants

    @property
    def wallet_addresses(self):
        if self._wallet_addresses is None:
            from .wallet_addresses.client import AsyncWalletAddressesClient  # noqa: E402

            self._wallet_addresses = AsyncWalletAddressesClient(client_wrapper=self._client_wrapper)
        return self._wallet_addresses

    @property
    def senders(self):
        if self._senders is None:
            from .senders.client import AsyncSendersClient  # noqa: E402

            self._senders = AsyncSendersClient(client_wrapper=self._client_wrapper)
        return self._senders

    @property
    def beneficiaries(self):
        if self._beneficiaries is None:
            from .beneficiaries.client import AsyncBeneficiariesClient  # noqa: E402

            self._beneficiaries = AsyncBeneficiariesClient(client_wrapper=self._client_wrapper)
        return self._beneficiaries

    @property
    def quotes(self):
        if self._quotes is None:
            from .quotes.client import AsyncQuotesClient  # noqa: E402

            self._quotes = AsyncQuotesClient(client_wrapper=self._client_wrapper)
        return self._quotes

    @property
    def orders(self):
        if self._orders is None:
            from .orders.client import AsyncOrdersClient  # noqa: E402

            self._orders = AsyncOrdersClient(client_wrapper=self._client_wrapper)
        return self._orders

    @property
    def webhooks(self):
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient  # noqa: E402

            self._webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        return self._webhooks

    @property
    def payment_methods(self):
        if self._payment_methods is None:
            from .payment_methods.client import AsyncPaymentMethodsClient  # noqa: E402

            self._payment_methods = AsyncPaymentMethodsClient(client_wrapper=self._client_wrapper)
        return self._payment_methods

    @property
    def validation_rules(self):
        if self._validation_rules is None:
            from .validation_rules.client import AsyncValidationRulesClient  # noqa: E402

            self._validation_rules = AsyncValidationRulesClient(client_wrapper=self._client_wrapper)
        return self._validation_rules

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient  # noqa: E402

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def auth(self):
        if self._auth is None:
            from .auth.client import AsyncAuthClient  # noqa: E402

            self._auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        return self._auth

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient  # noqa: E402

            self._api_keys = AsyncApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def transfers(self):
        if self._transfers is None:
            from .transfers.client import AsyncTransfersClient  # noqa: E402

            self._transfers = AsyncTransfersClient(client_wrapper=self._client_wrapper)
        return self._transfers


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MestaEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")

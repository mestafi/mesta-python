
from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMerchantsClient, RawMerchantsClient
from .types.accept_terms_merchants_response import AcceptTermsMerchantsResponse
from .types.get_balances_merchants_response import GetBalancesMerchantsResponse
from .types.get_merchants_response import GetMerchantsResponse

if typing.TYPE_CHECKING:
    from .accounts.client import AccountsClient, AsyncAccountsClient
    from .fiat_deposits.client import AsyncFiatDepositsClient, FiatDepositsClient
    from .source_wallet_addresses.client import AsyncSourceWalletAddressesClient, SourceWalletAddressesClient
    from .stablecoin_deposits.client import AsyncStablecoinDepositsClient, StablecoinDepositsClient
    from .transactions.client import AsyncTransactionsClient, TransactionsClient


class MerchantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMerchantsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._accounts: typing.Optional[AccountsClient] = None
        self._transactions: typing.Optional[TransactionsClient] = None
        self._stablecoin_deposits: typing.Optional[StablecoinDepositsClient] = None
        self._fiat_deposits: typing.Optional[FiatDepositsClient] = None
        self._source_wallet_addresses: typing.Optional[SourceWalletAddressesClient] = None

    @property
    def with_raw_response(self) -> RawMerchantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMerchantsClient
        """
        return self._raw_client

    def get(self, merchant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetMerchantsResponse:
        """
        Retrieves detailed information about a specific merchant, including account details and UBO (Ultimate Beneficial Owner) information.

        Parameters
        ----------
        merchant_id : str
            Unique identifier of the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMerchantsResponse
            Merchant information retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.merchants.get(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.get(merchant_id, request_options=request_options)
        return _response.data

    def accept_terms(
        self, merchant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptTermsMerchantsResponse:
        """
        Records the merchant's acceptance of Terms of Service. Captures acceptance timestamp, user identity, and IP address.

        Parameters
        ----------
        merchant_id : str
            ID of the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptTermsMerchantsResponse
            Terms accepted successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.merchants.accept_terms(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.accept_terms(merchant_id, request_options=request_options)
        return _response.data

    def get_balances(
        self, merchant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBalancesMerchantsResponse:
        """
        Retrieves the current balances for a merchant across all currencies and stablecoins.

        Parameters
        ----------
        merchant_id : str
            Unique identifier of the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBalancesMerchantsResponse
            Merchant balances retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.merchants.get_balances(
            merchant_id="merchantId",
        )
        """
        _response = self._raw_client.get_balances(merchant_id, request_options=request_options)
        return _response.data

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AccountsClient  # noqa: E402

            self._accounts = AccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import TransactionsClient  # noqa: E402

            self._transactions = TransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions

    @property
    def stablecoin_deposits(self):
        if self._stablecoin_deposits is None:
            from .stablecoin_deposits.client import StablecoinDepositsClient  # noqa: E402

            self._stablecoin_deposits = StablecoinDepositsClient(client_wrapper=self._client_wrapper)
        return self._stablecoin_deposits

    @property
    def fiat_deposits(self):
        if self._fiat_deposits is None:
            from .fiat_deposits.client import FiatDepositsClient  # noqa: E402

            self._fiat_deposits = FiatDepositsClient(client_wrapper=self._client_wrapper)
        return self._fiat_deposits

    @property
    def source_wallet_addresses(self):
        if self._source_wallet_addresses is None:
            from .source_wallet_addresses.client import SourceWalletAddressesClient  # noqa: E402

            self._source_wallet_addresses = SourceWalletAddressesClient(client_wrapper=self._client_wrapper)
        return self._source_wallet_addresses


class AsyncMerchantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMerchantsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._accounts: typing.Optional[AsyncAccountsClient] = None
        self._transactions: typing.Optional[AsyncTransactionsClient] = None
        self._stablecoin_deposits: typing.Optional[AsyncStablecoinDepositsClient] = None
        self._fiat_deposits: typing.Optional[AsyncFiatDepositsClient] = None
        self._source_wallet_addresses: typing.Optional[AsyncSourceWalletAddressesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawMerchantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMerchantsClient
        """
        return self._raw_client

    async def get(
        self, merchant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMerchantsResponse:
        """
        Retrieves detailed information about a specific merchant, including account details and UBO (Ultimate Beneficial Owner) information.

        Parameters
        ----------
        merchant_id : str
            Unique identifier of the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMerchantsResponse
            Merchant information retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchants.get(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(merchant_id, request_options=request_options)
        return _response.data

    async def accept_terms(
        self, merchant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AcceptTermsMerchantsResponse:
        """
        Records the merchant's acceptance of Terms of Service. Captures acceptance timestamp, user identity, and IP address.

        Parameters
        ----------
        merchant_id : str
            ID of the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AcceptTermsMerchantsResponse
            Terms accepted successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchants.accept_terms(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_terms(merchant_id, request_options=request_options)
        return _response.data

    async def get_balances(
        self, merchant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBalancesMerchantsResponse:
        """
        Retrieves the current balances for a merchant across all currencies and stablecoins.

        Parameters
        ----------
        merchant_id : str
            Unique identifier of the merchant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBalancesMerchantsResponse
            Merchant balances retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchants.get_balances(
                merchant_id="merchantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_balances(merchant_id, request_options=request_options)
        return _response.data

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AsyncAccountsClient  # noqa: E402

            self._accounts = AsyncAccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import AsyncTransactionsClient  # noqa: E402

            self._transactions = AsyncTransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions

    @property
    def stablecoin_deposits(self):
        if self._stablecoin_deposits is None:
            from .stablecoin_deposits.client import AsyncStablecoinDepositsClient  # noqa: E402

            self._stablecoin_deposits = AsyncStablecoinDepositsClient(client_wrapper=self._client_wrapper)
        return self._stablecoin_deposits

    @property
    def fiat_deposits(self):
        if self._fiat_deposits is None:
            from .fiat_deposits.client import AsyncFiatDepositsClient  # noqa: E402

            self._fiat_deposits = AsyncFiatDepositsClient(client_wrapper=self._client_wrapper)
        return self._fiat_deposits

    @property
    def source_wallet_addresses(self):
        if self._source_wallet_addresses is None:
            from .source_wallet_addresses.client import AsyncSourceWalletAddressesClient  # noqa: E402

            self._source_wallet_addresses = AsyncSourceWalletAddressesClient(client_wrapper=self._client_wrapper)
        return self._source_wallet_addresses

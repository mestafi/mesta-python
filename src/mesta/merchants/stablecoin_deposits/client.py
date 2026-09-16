
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawStablecoinDepositsClient, RawStablecoinDepositsClient
from .types.get_stablecoin_deposits_response import GetStablecoinDepositsResponse
from .types.list_stablecoin_deposits_request_currency import ListStablecoinDepositsRequestCurrency
from .types.list_stablecoin_deposits_request_sort_by import ListStablecoinDepositsRequestSortBy
from .types.list_stablecoin_deposits_request_sort_order import ListStablecoinDepositsRequestSortOrder
from .types.list_stablecoin_deposits_request_status import ListStablecoinDepositsRequestStatus
from .types.list_stablecoin_deposits_request_swa_risk_level import ListStablecoinDepositsRequestSwaRiskLevel
from .types.list_stablecoin_deposits_response import ListStablecoinDepositsResponse


class StablecoinDepositsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStablecoinDepositsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStablecoinDepositsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStablecoinDepositsClient
        """
        return self._raw_client

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
    ) -> ListStablecoinDepositsResponse:
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
        ListStablecoinDepositsResponse
            Stablecoin deposits retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.merchants.stablecoin_deposits.list(
            search="abc123",
            merchant_id="550e8400-e29b-41d4-a716-446655440000",
            sender_id="550e8400-e29b-41d4-a716-446655440001",
            source_wallet_address="0x1234567890abcdef1234567890abcdef12345678",
            deposit_wallet_address_id="550e8400-e29b-41d4-a716-446655440002",
        )
        """
        _response = self._raw_client.list(
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            currency=currency,
            merchant_id=merchant_id,
            sender_id=sender_id,
            status=status,
            swa_risk_level=swa_risk_level,
            source_wallet_address=source_wallet_address,
            deposit_wallet_address_id=deposit_wallet_address_id,
            is_pooled=is_pooled,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetStablecoinDepositsResponse:
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
        GetStablecoinDepositsResponse
            Stablecoin deposit retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.merchants.stablecoin_deposits.get(
            id="550e8400-e29b-41d4-a716-446655440000",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data


class AsyncStablecoinDepositsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStablecoinDepositsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStablecoinDepositsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStablecoinDepositsClient
        """
        return self._raw_client

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
    ) -> ListStablecoinDepositsResponse:
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
        ListStablecoinDepositsResponse
            Stablecoin deposits retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchants.stablecoin_deposits.list(
                search="abc123",
                merchant_id="550e8400-e29b-41d4-a716-446655440000",
                sender_id="550e8400-e29b-41d4-a716-446655440001",
                source_wallet_address="0x1234567890abcdef1234567890abcdef12345678",
                deposit_wallet_address_id="550e8400-e29b-41d4-a716-446655440002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            currency=currency,
            merchant_id=merchant_id,
            sender_id=sender_id,
            status=status,
            swa_risk_level=swa_risk_level,
            source_wallet_address=source_wallet_address,
            deposit_wallet_address_id=deposit_wallet_address_id,
            is_pooled=is_pooled,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStablecoinDepositsResponse:
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
        GetStablecoinDepositsResponse
            Stablecoin deposit retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchants.stablecoin_deposits.get(
                id="550e8400-e29b-41d4-a716-446655440000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

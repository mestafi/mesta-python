
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawQuotesClient, RawQuotesClient
from .types.create_quotes_request_source_currency import CreateQuotesRequestSourceCurrency
from .types.create_quotes_request_transfer_type import CreateQuotesRequestTransferType
from .types.create_quotes_response import CreateQuotesResponse
from .types.get_quotes_response import GetQuotesResponse
from .types.list_quotes_request_sort_by import ListQuotesRequestSortBy
from .types.list_quotes_request_sort_order import ListQuotesRequestSortOrder
from .types.list_quotes_response import ListQuotesResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class QuotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQuotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQuotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQuotesClient
        """
        return self._raw_client

    def get(self, quote_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetQuotesResponse:
        """
        Retrieve the details of a specific quote by its unique identifier (quoteId).

        Parameters
        ----------
        quote_id : str
            Unique identifier for the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuotesResponse
            Quote retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.quotes.get(
            quote_id="quoteId",
        )
        """
        _response = self._raw_client.get(quote_id, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort_by: typing.Optional[ListQuotesRequestSortBy] = None,
        sort_order: typing.Optional[ListQuotesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListQuotesResponse:
        """
        Retrieves a paginated list of quotes with optional filtering.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Records per page

        page : typing.Optional[int]
            Page number

        sort_by : typing.Optional[ListQuotesRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListQuotesRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListQuotesResponse
            Quotes list retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.quotes.list()
        """
        _response = self._raw_client.list(
            page_size=page_size, page=page, sort_by=sort_by, sort_order=sort_order, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        target_currency: str,
        source_currency: CreateQuotesRequestSourceCurrency,
        target_amount: typing.Optional[float] = OMIT,
        source_amount: typing.Optional[float] = OMIT,
        developer_fee: typing.Optional[str] = OMIT,
        transfer_type: typing.Optional[CreateQuotesRequestTransferType] = OMIT,
        firc_required: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateQuotesResponse:
        """
        Obtain a quote for converting USD or USDC to another specified currency. For web3 merchants, sourceCurrency is required and must be a stable coin. For web2 merchants, sourceCurrency is optional and defaults to USD if omitted.

        Parameters
        ----------
        target_currency : str
            ISO currency code for the order target currency.

        source_currency : CreateQuotesRequestSourceCurrency
            The source currency code (e.g., USD, USDC_ETH).

        target_amount : typing.Optional[float]
            The amount of target currency to convert.

        source_amount : typing.Optional[float]
            The amount of source currency to convert.

        developer_fee : typing.Optional[str]
            Developer fee amount in source currency

        transfer_type : typing.Optional[CreateQuotesRequestTransferType]
            Transfer type (only required for USD payins or payouts). Use `internal` to request a quote for an internal sender-to-sender transfer — sourceCurrency and targetCurrency must both be USD, and developerFee is not allowed. Internal transfers are only enabled for select merchants and use cases; see the Create Internal Transfer endpoint.

        firc_required : typing.Optional[bool]
            Request a Foreign Inward Remittance Certificate (FIRC) for this transfer. Only applicable when targetCurrency is INR; ignored for other currencies. May incur an additional fee in future.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateQuotesResponse
            Quote created successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.quotes.create(
            target_currency="targetCurrency",
            source_currency="USD",
        )
        """
        _response = self._raw_client.create(
            target_currency=target_currency,
            source_currency=source_currency,
            target_amount=target_amount,
            source_amount=source_amount,
            developer_fee=developer_fee,
            transfer_type=transfer_type,
            firc_required=firc_required,
            request_options=request_options,
        )
        return _response.data


class AsyncQuotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQuotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQuotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQuotesClient
        """
        return self._raw_client

    async def get(self, quote_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetQuotesResponse:
        """
        Retrieve the details of a specific quote by its unique identifier (quoteId).

        Parameters
        ----------
        quote_id : str
            Unique identifier for the quote.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetQuotesResponse
            Quote retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.quotes.get(
                quote_id="quoteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(quote_id, request_options=request_options)
        return _response.data

    async def list(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort_by: typing.Optional[ListQuotesRequestSortBy] = None,
        sort_order: typing.Optional[ListQuotesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListQuotesResponse:
        """
        Retrieves a paginated list of quotes with optional filtering.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Records per page

        page : typing.Optional[int]
            Page number

        sort_by : typing.Optional[ListQuotesRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListQuotesRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListQuotesResponse
            Quotes list retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.quotes.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page_size=page_size, page=page, sort_by=sort_by, sort_order=sort_order, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        target_currency: str,
        source_currency: CreateQuotesRequestSourceCurrency,
        target_amount: typing.Optional[float] = OMIT,
        source_amount: typing.Optional[float] = OMIT,
        developer_fee: typing.Optional[str] = OMIT,
        transfer_type: typing.Optional[CreateQuotesRequestTransferType] = OMIT,
        firc_required: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateQuotesResponse:
        """
        Obtain a quote for converting USD or USDC to another specified currency. For web3 merchants, sourceCurrency is required and must be a stable coin. For web2 merchants, sourceCurrency is optional and defaults to USD if omitted.

        Parameters
        ----------
        target_currency : str
            ISO currency code for the order target currency.

        source_currency : CreateQuotesRequestSourceCurrency
            The source currency code (e.g., USD, USDC_ETH).

        target_amount : typing.Optional[float]
            The amount of target currency to convert.

        source_amount : typing.Optional[float]
            The amount of source currency to convert.

        developer_fee : typing.Optional[str]
            Developer fee amount in source currency

        transfer_type : typing.Optional[CreateQuotesRequestTransferType]
            Transfer type (only required for USD payins or payouts). Use `internal` to request a quote for an internal sender-to-sender transfer — sourceCurrency and targetCurrency must both be USD, and developerFee is not allowed. Internal transfers are only enabled for select merchants and use cases; see the Create Internal Transfer endpoint.

        firc_required : typing.Optional[bool]
            Request a Foreign Inward Remittance Certificate (FIRC) for this transfer. Only applicable when targetCurrency is INR; ignored for other currencies. May incur an additional fee in future.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateQuotesResponse
            Quote created successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.quotes.create(
                target_currency="targetCurrency",
                source_currency="USD",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            target_currency=target_currency,
            source_currency=source_currency,
            target_amount=target_amount,
            source_amount=source_amount,
            developer_fee=developer_fee,
            transfer_type=transfer_type,
            firc_required=firc_required,
            request_options=request_options,
        )
        return _response.data

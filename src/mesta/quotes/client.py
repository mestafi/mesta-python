
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawQuotesClient, RawQuotesClient
from .types.create_quotes_request import CreateQuotesRequest
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
        self, *, request: CreateQuotesRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateQuotesResponse:
        """
        Obtain a quote for converting USD or USDC to another specified currency. For web3 merchants, sourceCurrency is required and must be a stable coin. For web2 merchants, sourceCurrency is optional and defaults to USD if omitted.

        Parameters
        ----------
        request : CreateQuotesRequest

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
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
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
        self, *, request: CreateQuotesRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateQuotesResponse:
        """
        Obtain a quote for converting USD or USDC to another specified currency. For web3 merchants, sourceCurrency is required and must be a stable coin. For web2 merchants, sourceCurrency is optional and defaults to USD if omitted.

        Parameters
        ----------
        request : CreateQuotesRequest

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
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data

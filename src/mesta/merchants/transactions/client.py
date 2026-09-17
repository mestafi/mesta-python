
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawTransactionsClient, RawTransactionsClient
from .types.list_transactions_request_sort_order import ListTransactionsRequestSortOrder
from .types.list_transactions_response import ListTransactionsResponse


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransactionsClient
        """
        return self._raw_client

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
    ) -> ListTransactionsResponse:
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
        ListTransactionsResponse
            Merchant transactions retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.merchants.transactions.list(
            sort_by="createdAt",
        )
        """
        _response = self._raw_client.list(
            currency=currency,
            type=type,
            sender_id=sender_id,
            transaction_id=transaction_id,
            virtual_transaction_id=virtual_transaction_id,
            order_id=order_id,
            page_size=page_size,
            page=page,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransactionsClient
        """
        return self._raw_client

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
    ) -> ListTransactionsResponse:
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
        ListTransactionsResponse
            Merchant transactions retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.merchants.transactions.list(
                sort_by="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            currency=currency,
            type=type,
            sender_id=sender_id,
            transaction_id=transaction_id,
            virtual_transaction_id=virtual_transaction_id,
            order_id=order_id,
            page_size=page_size,
            page=page,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

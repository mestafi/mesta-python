
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.source_address_input import SourceAddressInput
from .raw_client import AsyncRawSourceWalletAddressesClient, RawSourceWalletAddressesClient
from .types.create_source_wallet_addresses_response import CreateSourceWalletAddressesResponse
from .types.list_source_wallet_addresses_request_sort_by import ListSourceWalletAddressesRequestSortBy
from .types.list_source_wallet_addresses_request_sort_order import ListSourceWalletAddressesRequestSortOrder
from .types.list_source_wallet_addresses_response import ListSourceWalletAddressesResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SourceWalletAddressesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceWalletAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceWalletAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceWalletAddressesClient
        """
        return self._raw_client

    def list(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListSourceWalletAddressesRequestSortBy] = None,
        sort_order: typing.Optional[ListSourceWalletAddressesRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSourceWalletAddressesResponse:
        """
        Retrieves all source wallet addresses for a specific sender. Supports pagination, sorting, and search.

        Parameters
        ----------
        id : str
            ID of the sender

        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListSourceWalletAddressesRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[ListSourceWalletAddressesRequestSortOrder]
            Sort direction

        search : typing.Optional[str]
            Search query to filter results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSourceWalletAddressesResponse
            List of source wallet addresses retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.source_wallet_addresses.list(
            id="id",
        )
        """
        _response = self._raw_client.list(
            id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        id: str,
        *,
        request: typing.Sequence[SourceAddressInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSourceWalletAddressesResponse:
        """
        Creates new source addresses for a specific sender. Multiple addresses can be created in a single request.

        Parameters
        ----------
        id : str
            ID of the sender

        request : typing.Sequence[SourceAddressInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSourceWalletAddressesResponse
            Source wallet address created successfully

        Examples
        --------
        from mesta import Mesta, SourceAddressInput

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.source_wallet_addresses.create(
            id="id",
            request=[
                SourceAddressInput(
                    address="address",
                    chain="chain",
                )
            ],
        )
        """
        _response = self._raw_client.create(id, request=request, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, source_wallet_address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific source wallet address for a sender.

        Parameters
        ----------
        id : str
            ID of the sender

        source_wallet_address_id : str
            ID of the source wallet address to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.source_wallet_addresses.delete(
            id="id",
            source_wallet_address_id="sourceWalletAddressId",
        )
        """
        _response = self._raw_client.delete(id, source_wallet_address_id, request_options=request_options)
        return _response.data


class AsyncSourceWalletAddressesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceWalletAddressesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceWalletAddressesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceWalletAddressesClient
        """
        return self._raw_client

    async def list(
        self,
        id: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListSourceWalletAddressesRequestSortBy] = None,
        sort_order: typing.Optional[ListSourceWalletAddressesRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSourceWalletAddressesResponse:
        """
        Retrieves all source wallet addresses for a specific sender. Supports pagination, sorting, and search.

        Parameters
        ----------
        id : str
            ID of the sender

        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListSourceWalletAddressesRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[ListSourceWalletAddressesRequestSortOrder]
            Sort direction

        search : typing.Optional[str]
            Search query to filter results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSourceWalletAddressesResponse
            List of source wallet addresses retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.source_wallet_addresses.list(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        id: str,
        *,
        request: typing.Sequence[SourceAddressInput],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSourceWalletAddressesResponse:
        """
        Creates new source addresses for a specific sender. Multiple addresses can be created in a single request.

        Parameters
        ----------
        id : str
            ID of the sender

        request : typing.Sequence[SourceAddressInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSourceWalletAddressesResponse
            Source wallet address created successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta, SourceAddressInput

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.source_wallet_addresses.create(
                id="id",
                request=[
                    SourceAddressInput(
                        address="address",
                        chain="chain",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(id, request=request, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, source_wallet_address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a specific source wallet address for a sender.

        Parameters
        ----------
        id : str
            ID of the sender

        source_wallet_address_id : str
            ID of the source wallet address to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.source_wallet_addresses.delete(
                id="id",
                source_wallet_address_id="sourceWalletAddressId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, source_wallet_address_id, request_options=request_options)
        return _response.data

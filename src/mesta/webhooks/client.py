
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.create_webhooks_request_events_item import CreateWebhooksRequestEventsItem
from .types.create_webhooks_response import CreateWebhooksResponse
from .types.delete_webhooks_response import DeleteWebhooksResponse
from .types.get_webhooks_response import GetWebhooksResponse
from .types.list_webhooks_request_event import ListWebhooksRequestEvent
from .types.list_webhooks_request_sort_by import ListWebhooksRequestSortBy
from .types.list_webhooks_request_sort_order import ListWebhooksRequestSortOrder
from .types.list_webhooks_response import ListWebhooksResponse
from .types.update_webhooks_request_events_item import UpdateWebhooksRequestEventsItem
from .types.update_webhooks_response import UpdateWebhooksResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhooksClient
        """
        return self._raw_client

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListWebhooksRequestSortBy] = None,
        sort_order: typing.Optional[ListWebhooksRequestSortOrder] = None,
        event: typing.Optional[ListWebhooksRequestEvent] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhooksResponse:
        """
        Retrieves a list of all registered webhooks for the calling client.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of webhooks per page

        sort_by : typing.Optional[ListWebhooksRequestSortBy]
            Field to sort the webhooks by

        sort_order : typing.Optional[ListWebhooksRequestSortOrder]
            Sort order (ascending or descending)

        event : typing.Optional[ListWebhooksRequestEvent]
            Filter webhooks by specific event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse
            Successfully retrieved registered webhooks

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list()
        """
        _response = self._raw_client.list(
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            event=event,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        events: typing.Sequence[CreateWebhooksRequestEventsItem],
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhooksResponse:
        """
        Registers a new webhook for a specific event.

        Parameters
        ----------
        events : typing.Sequence[CreateWebhooksRequestEventsItem]

        url : str
            The URL where events will be posted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhooksResponse
            Webhook successfully registered

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create(
            events=["order:*", "sender:kyb_approved", "fiat_deposit:settled"],
            url="https://example.com/webhooks/mesta",
        )
        """
        _response = self._raw_client.create(events=events, url=url, request_options=request_options)
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetWebhooksResponse:
        """
        Retrieves a specific webhook by its unique identifier.

        Parameters
        ----------
        id : str
            Unique identifier for the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Successfully retrieved webhook

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.webhooks.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteWebhooksResponse:
        """
        Deletes a registered webhook.

        Parameters
        ----------
        id : str
            Unique identifier for the webhook to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhooksResponse
            Delete Webhook Successful

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def update(
        self,
        id: str,
        *,
        events: typing.Sequence[UpdateWebhooksRequestEventsItem],
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhooksResponse:
        """
        Updates a registered webhook.

        Parameters
        ----------
        id : str
            Unique identifier for the webhook to be updated.

        events : typing.Sequence[UpdateWebhooksRequestEventsItem]

        url : str
            The URL where events will be posted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhooksResponse
            Webhook successfully updated

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.webhooks.update(
            id="id",
            events=["order:*"],
            url="url",
        )
        """
        _response = self._raw_client.update(id, events=events, url=url, request_options=request_options)
        return _response.data


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhooksClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListWebhooksRequestSortBy] = None,
        sort_order: typing.Optional[ListWebhooksRequestSortOrder] = None,
        event: typing.Optional[ListWebhooksRequestEvent] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhooksResponse:
        """
        Retrieves a list of all registered webhooks for the calling client.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of webhooks per page

        sort_by : typing.Optional[ListWebhooksRequestSortBy]
            Field to sort the webhooks by

        sort_order : typing.Optional[ListWebhooksRequestSortOrder]
            Sort order (ascending or descending)

        event : typing.Optional[ListWebhooksRequestEvent]
            Filter webhooks by specific event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse
            Successfully retrieved registered webhooks

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            event=event,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        events: typing.Sequence[CreateWebhooksRequestEventsItem],
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhooksResponse:
        """
        Registers a new webhook for a specific event.

        Parameters
        ----------
        events : typing.Sequence[CreateWebhooksRequestEventsItem]

        url : str
            The URL where events will be posted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhooksResponse
            Webhook successfully registered

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.create(
                events=["order:*", "sender:kyb_approved", "fiat_deposit:settled"],
                url="https://example.com/webhooks/mesta",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(events=events, url=url, request_options=request_options)
        return _response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetWebhooksResponse:
        """
        Retrieves a specific webhook by its unique identifier.

        Parameters
        ----------
        id : str
            Unique identifier for the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Successfully retrieved webhook

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhooksResponse:
        """
        Deletes a registered webhook.

        Parameters
        ----------
        id : str
            Unique identifier for the webhook to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhooksResponse
            Delete Webhook Successful

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: str,
        *,
        events: typing.Sequence[UpdateWebhooksRequestEventsItem],
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhooksResponse:
        """
        Updates a registered webhook.

        Parameters
        ----------
        id : str
            Unique identifier for the webhook to be updated.

        events : typing.Sequence[UpdateWebhooksRequestEventsItem]

        url : str
            The URL where events will be posted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhooksResponse
            Webhook successfully updated

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.update(
                id="id",
                events=["order:*"],
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(id, events=events, url=url, request_options=request_options)
        return _response.data

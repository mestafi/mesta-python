
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawTermsOfServiceClient, RawTermsOfServiceClient
from .types.get_acceptance_terms_of_service_response import GetAcceptanceTermsOfServiceResponse
from .types.get_status_terms_of_service_response import GetStatusTermsOfServiceResponse


class TermsOfServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTermsOfServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTermsOfServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTermsOfServiceClient
        """
        return self._raw_client

    def get_status(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStatusTermsOfServiceResponse:
        """
        Retrieves the current Terms of Service acceptance status for a specific sender, along with the active shareable acceptance link. In the current sender flow, a TOS acceptance link is generated during sender creation. Use this endpoint to check whether the sender has accepted the TOS, retrieve the active acceptance link, and verify whether the link has expired.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusTermsOfServiceResponse
            TOS status retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.terms_of_service.get_status(
            sender_id="senderId",
        )
        """
        _response = self._raw_client.get_status(sender_id, request_options=request_options)
        return _response.data

    def get_acceptance(
        self, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAcceptanceTermsOfServiceResponse:
        """
        Retrieves the Terms of Service acceptance details for a given token. This is a public endpoint that does not require authentication.

        Parameters
        ----------
        token : str
            TOS acceptance token (base64url encoded)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAcceptanceTermsOfServiceResponse
            TOS acceptance details retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.terms_of_service.get_acceptance(
            token="token",
        )
        """
        _response = self._raw_client.get_acceptance(token, request_options=request_options)
        return _response.data


class AsyncTermsOfServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTermsOfServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTermsOfServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTermsOfServiceClient
        """
        return self._raw_client

    async def get_status(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStatusTermsOfServiceResponse:
        """
        Retrieves the current Terms of Service acceptance status for a specific sender, along with the active shareable acceptance link. In the current sender flow, a TOS acceptance link is generated during sender creation. Use this endpoint to check whether the sender has accepted the TOS, retrieve the active acceptance link, and verify whether the link has expired.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusTermsOfServiceResponse
            TOS status retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.terms_of_service.get_status(
                sender_id="senderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(sender_id, request_options=request_options)
        return _response.data

    async def get_acceptance(
        self, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAcceptanceTermsOfServiceResponse:
        """
        Retrieves the Terms of Service acceptance details for a given token. This is a public endpoint that does not require authentication.

        Parameters
        ----------
        token : str
            TOS acceptance token (base64url encoded)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAcceptanceTermsOfServiceResponse
            TOS acceptance details retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.terms_of_service.get_acceptance(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_acceptance(token, request_options=request_options)
        return _response.data

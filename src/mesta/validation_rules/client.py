
from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawValidationRulesClient, RawValidationRulesClient
from .types.list_states_validation_rules_response import ListStatesValidationRulesResponse

if typing.TYPE_CHECKING:
    from .beneficiaries.client import AsyncBeneficiariesClient, BeneficiariesClient
    from .senders.client import AsyncSendersClient, SendersClient


class ValidationRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValidationRulesClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._senders: typing.Optional[SendersClient] = None
        self._beneficiaries: typing.Optional[BeneficiariesClient] = None

    @property
    def with_raw_response(self) -> RawValidationRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValidationRulesClient
        """
        return self._raw_client

    def list_states(
        self, *, country: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListStatesValidationRulesResponse:
        """
        Retrieve a list of states/provinces for a given country code. Returns state codes in ISO 3166-2 format.

        Parameters
        ----------
        country : str
            ISO 3166-1 alpha-2 country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListStatesValidationRulesResponse
            List of states for the country

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.validation_rules.list_states(
            country="US",
        )
        """
        _response = self._raw_client.list_states(country=country, request_options=request_options)
        return _response.data

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


class AsyncValidationRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValidationRulesClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._senders: typing.Optional[AsyncSendersClient] = None
        self._beneficiaries: typing.Optional[AsyncBeneficiariesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawValidationRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValidationRulesClient
        """
        return self._raw_client

    async def list_states(
        self, *, country: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListStatesValidationRulesResponse:
        """
        Retrieve a list of states/provinces for a given country code. Returns state codes in ISO 3166-2 format.

        Parameters
        ----------
        country : str
            ISO 3166-1 alpha-2 country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListStatesValidationRulesResponse
            List of states for the country

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.validation_rules.list_states(
                country="US",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_states(country=country, request_options=request_options)
        return _response.data

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

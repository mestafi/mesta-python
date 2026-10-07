
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSandboxClient, RawSandboxClient
from .types.create_sender_wallets_sandbox_response import CreateSenderWalletsSandboxResponse
from .types.create_wallets_sandbox_response import CreateWalletsSandboxResponse
from .types.get_sandbox_response import GetSandboxResponse
from .types.reset_sandbox_response import ResetSandboxResponse


class SandboxClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSandboxClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSandboxClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSandboxClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSandboxResponse:
        """
        The sandbox's status, deadline, `emailVerified`, `executionPaused`, `pauseMessage`, all seven `counts`, the `wallets` state (`unavailable` until test-network wallets are offered), the progress of the sample data (`seed.status`, `seed.step`, `seed.steps`, `seed.error`), the `fixtures` block once the sample data is complete, and its keys by id with `kind`, `expiresAt` and `lastUsedAt`; never an API key secret. The `fixtures` include the retrievable webhook signing key. Requires `merchant:sandbox:read` (included in the initial standard integration key; narrower keys must request it) or a session of the sandbox's merchant. Another sandbox's id is 404. A failed sandbox's keys can read this route for 24 hours and nothing else.

        Parameters
        ----------
        id : str
            The sandbox id, `sbx_…`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSandboxResponse
            The sandbox.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Marks the sandbox deleted: keys revoked, users signed out, running orders stopped, every row purged within 24 hours. The owner's email is free to create again at once. Requires `merchant:sandbox:write`; a key or a session while the sandbox is unclaimed, a session once it is claimed.

        Parameters
        ----------
        id : str
            The sandbox id.

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
        client.sandbox.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def reset(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ResetSandboxResponse:
        """
        Restores balances and removes your orders, quotes and deposits; the sample senders and beneficiaries stay. Stops running orders, deletes the orders, quotes and deposits and the senders, beneficiaries and payment methods you created, deletes the ledger history, restores altered or deleted sample objects under their original ids and adds the sample deposits and orders again. Reset leaves webhook endpoints, their URLs, their events and the signing key exactly as you set them, and clears the delivery-log entries of the orders, quotes and deposits it removes. Keys, wallets and deposit instructions are untouched. Status reads remain available; every other request answers 409 SANDBOX_RESETTING until it finishes, in seconds. Requires `merchant:sandbox:write`, key or session; no step-up. 50 per sandbox per rolling day.

        Parameters
        ----------
        id : str
            The sandbox id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResetSandboxResponse
            Reset started.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.reset(
            id="id",
        )
        """
        _response = self._raw_client.reset(id, request_options=request_options)
        return _response.data

    def create_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateWalletsSandboxResponse:
        """
        Test-network wallets are coming soon. Until they are offered, this route answers 409 NOT_AVAILABLE_IN_SANDBOX without Retry-After, and the session read reports `wallets.status` `unavailable`. Once they are offered, it creates your merchant's wallet when the wallet was skipped while the sample data was added: attempted once, and counted against the sandbox environment's daily wallet ceiling. Requires `merchant:sandbox:write`, key or session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWalletsSandboxResponse
            Wallet creation requested; read the wallet addresses when available.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.create_wallets()
        """
        _response = self._raw_client.create_wallets(request_options=request_options)
        return _response.data

    def create_sender_wallets(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateSenderWalletsSandboxResponse:
        """
        Test-network wallets are coming soon. Until they are offered, this route answers 409 NOT_AVAILABLE_IN_SANDBOX without Retry-After. Once they are offered, it creates the sender's wallet, once per sender; five senders per sandbox can hold wallets and the sixth answers 409 SANDBOX_CAP_EXCEEDED. The sender must be yours (404 otherwise). Requires `merchant:sender:write`, key or session.

        Parameters
        ----------
        id : str
            The sender id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSenderWalletsSandboxResponse
            Wallet creation requested; read the wallet addresses when available.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.create_sender_wallets(
            id="id",
        )
        """
        _response = self._raw_client.create_sender_wallets(id, request_options=request_options)
        return _response.data


class AsyncSandboxClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSandboxClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSandboxClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSandboxClient
        """
        return self._raw_client

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSandboxResponse:
        """
        The sandbox's status, deadline, `emailVerified`, `executionPaused`, `pauseMessage`, all seven `counts`, the `wallets` state (`unavailable` until test-network wallets are offered), the progress of the sample data (`seed.status`, `seed.step`, `seed.steps`, `seed.error`), the `fixtures` block once the sample data is complete, and its keys by id with `kind`, `expiresAt` and `lastUsedAt`; never an API key secret. The `fixtures` include the retrievable webhook signing key. Requires `merchant:sandbox:read` (included in the initial standard integration key; narrower keys must request it) or a session of the sandbox's merchant. Another sandbox's id is 404. A failed sandbox's keys can read this route for 24 hours and nothing else.

        Parameters
        ----------
        id : str
            The sandbox id, `sbx_…`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSandboxResponse
            The sandbox.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Marks the sandbox deleted: keys revoked, users signed out, running orders stopped, every row purged within 24 hours. The owner's email is free to create again at once. Requires `merchant:sandbox:write`; a key or a session while the sandbox is unclaimed, a session once it is claimed.

        Parameters
        ----------
        id : str
            The sandbox id.

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
            await client.sandbox.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def reset(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ResetSandboxResponse:
        """
        Restores balances and removes your orders, quotes and deposits; the sample senders and beneficiaries stay. Stops running orders, deletes the orders, quotes and deposits and the senders, beneficiaries and payment methods you created, deletes the ledger history, restores altered or deleted sample objects under their original ids and adds the sample deposits and orders again. Reset leaves webhook endpoints, their URLs, their events and the signing key exactly as you set them, and clears the delivery-log entries of the orders, quotes and deposits it removes. Keys, wallets and deposit instructions are untouched. Status reads remain available; every other request answers 409 SANDBOX_RESETTING until it finishes, in seconds. Requires `merchant:sandbox:write`, key or session; no step-up. 50 per sandbox per rolling day.

        Parameters
        ----------
        id : str
            The sandbox id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResetSandboxResponse
            Reset started.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.reset(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset(id, request_options=request_options)
        return _response.data

    async def create_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateWalletsSandboxResponse:
        """
        Test-network wallets are coming soon. Until they are offered, this route answers 409 NOT_AVAILABLE_IN_SANDBOX without Retry-After, and the session read reports `wallets.status` `unavailable`. Once they are offered, it creates your merchant's wallet when the wallet was skipped while the sample data was added: attempted once, and counted against the sandbox environment's daily wallet ceiling. Requires `merchant:sandbox:write`, key or session.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWalletsSandboxResponse
            Wallet creation requested; read the wallet addresses when available.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.create_wallets()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_wallets(request_options=request_options)
        return _response.data

    async def create_sender_wallets(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateSenderWalletsSandboxResponse:
        """
        Test-network wallets are coming soon. Until they are offered, this route answers 409 NOT_AVAILABLE_IN_SANDBOX without Retry-After. Once they are offered, it creates the sender's wallet, once per sender; five senders per sandbox can hold wallets and the sixth answers 409 SANDBOX_CAP_EXCEEDED. The sender must be yours (404 otherwise). Requires `merchant:sender:write`, key or session.

        Parameters
        ----------
        id : str
            The sender id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSenderWalletsSandboxResponse
            Wallet creation requested; read the wallet addresses when available.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.create_sender_wallets(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sender_wallets(id, request_options=request_options)
        return _response.data

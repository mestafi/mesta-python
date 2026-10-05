
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawClaimsClient, RawClaimsClient
from .types.create_claims_response import CreateClaimsResponse
from .types.get_status_claims_response import GetStatusClaimsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ClaimsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClaimsClient
        """
        return self._raw_client

    def get_status(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStatusClaimsResponse:
        """
        A non-consuming read of a claim token: `fresh`, `seeding` (with the current `seed.step`), `expired`, `used` or `killed`, with the counts of the sample data and, for `fresh`, the keys created before the claim and the endpoint hosts. The token travels in the body because request paths are logged. No authentication; 20 per hour per network address, a `seeding` answer uncounted. A fresh answer is also uncounted. Expired, unknown and malformed tokens return data containing only status: expired, with no sandbox metadata.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`. Sent in the body, never in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusClaimsResponse
            The token's state.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.claims.get_status(
            token="token",
        )
        """
        _response = self._raw_client.get_status(token=token, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        token: str,
        email: str,
        full_name: str,
        password: str,
        accept_terms: bool,
        keep_pre_claim_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateClaimsResponse:
        """
        Makes the caller the owner of an unclaimed sandbox: writes the email, name and password onto the sandbox's user, re-stamps the terms acceptance, revokes the keys created before the claim and the webhook endpoints created before it, rotates the webhook signing key and recreates the Mesta test endpoint, and mints one fresh standard pair returned once, unless `keepPreClaimKeys` is true. Returns the sandbox and a portal session. The sandbox then has 72 hours to verify the email. Single use, atomic on the token and the email. No authentication; 20 per hour per network address; a 409 SANDBOX_SEEDING answer is uncounted and leaves the token valid. keepPreClaimKeys keeps the keys, endpoints and signing key together; keys in the success body is then an empty array. The 20-per-rolling-hour claim counter counts token-check refusals only; probes answering `seeding` and claims answering SANDBOX_SEEDING are uncounted.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`.

        email : str

        full_name : str
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.

        password : str
            12 to 128 characters; common passwords are refused.

        accept_terms : bool
            Must be true; 422 with the terms URL and version otherwise.

        keep_pre_claim_keys : typing.Optional[bool]
            Keep the pre-claim keys, their webhook endpoints and signing key together. Otherwise revoke the keys, delete the endpoints, rotate the signing key, recreate the Mesta test endpoint and return one fresh pair once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateClaimsResponse
            The claimed sandbox, with the fresh key pair once unless the pre-claim keys were kept, and a portal session.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.claims.create(
            token="token",
            email="email",
            full_name="Example Developer",
            password="password",
            accept_terms=True,
        )
        """
        _response = self._raw_client.create(
            token=token,
            email=email,
            full_name=full_name,
            password=password,
            accept_terms=accept_terms,
            keep_pre_claim_keys=keep_pre_claim_keys,
            request_options=request_options,
        )
        return _response.data


class AsyncClaimsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClaimsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClaimsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClaimsClient
        """
        return self._raw_client

    async def get_status(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStatusClaimsResponse:
        """
        A non-consuming read of a claim token: `fresh`, `seeding` (with the current `seed.step`), `expired`, `used` or `killed`, with the counts of the sample data and, for `fresh`, the keys created before the claim and the endpoint hosts. The token travels in the body because request paths are logged. No authentication; 20 per hour per network address, a `seeding` answer uncounted. A fresh answer is also uncounted. Expired, unknown and malformed tokens return data containing only status: expired, with no sandbox metadata.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`. Sent in the body, never in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusClaimsResponse
            The token's state.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.claims.get_status(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(token=token, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        token: str,
        email: str,
        full_name: str,
        password: str,
        accept_terms: bool,
        keep_pre_claim_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateClaimsResponse:
        """
        Makes the caller the owner of an unclaimed sandbox: writes the email, name and password onto the sandbox's user, re-stamps the terms acceptance, revokes the keys created before the claim and the webhook endpoints created before it, rotates the webhook signing key and recreates the Mesta test endpoint, and mints one fresh standard pair returned once, unless `keepPreClaimKeys` is true. Returns the sandbox and a portal session. The sandbox then has 72 hours to verify the email. Single use, atomic on the token and the email. No authentication; 20 per hour per network address; a 409 SANDBOX_SEEDING answer is uncounted and leaves the token valid. keepPreClaimKeys keeps the keys, endpoints and signing key together; keys in the success body is then an empty array. The 20-per-rolling-hour claim counter counts token-check refusals only; probes answering `seeding` and claims answering SANDBOX_SEEDING are uncounted.

        Parameters
        ----------
        token : str
            The token from the fragment of `claimUrl`.

        email : str

        full_name : str
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.

        password : str
            12 to 128 characters; common passwords are refused.

        accept_terms : bool
            Must be true; 422 with the terms URL and version otherwise.

        keep_pre_claim_keys : typing.Optional[bool]
            Keep the pre-claim keys, their webhook endpoints and signing key together. Otherwise revoke the keys, delete the endpoints, rotate the signing key, recreate the Mesta test endpoint and return one fresh pair once.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateClaimsResponse
            The claimed sandbox, with the fresh key pair once unless the pre-claim keys were kept, and a portal session.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.claims.create(
                token="token",
                email="email",
                full_name="Example Developer",
                password="password",
                accept_terms=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            token=token,
            email=email,
            full_name=full_name,
            password=password,
            accept_terms=accept_terms,
            keep_pre_claim_keys=keep_pre_claim_keys,
            request_options=request_options,
        )
        return _response.data

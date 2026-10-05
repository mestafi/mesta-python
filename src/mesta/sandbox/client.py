
from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sandbox_challenge_solution import SandboxChallengeSolution
from .raw_client import AsyncRawSandboxClient, RawSandboxClient
from .types.create_sandbox_response import CreateSandboxResponse
from .types.create_sandbox_session_request_deposit_source import CreateSandboxSessionRequestDepositSource
from .types.create_sender_wallets_sandbox_response import CreateSenderWalletsSandboxResponse
from .types.create_wallets_sandbox_response import CreateWalletsSandboxResponse
from .types.get_challenge_sandbox_response import GetChallengeSandboxResponse
from .types.get_sandbox_response import GetSandboxResponse
from .types.request_production_sandbox_response import RequestProductionSandboxResponse
from .types.resend_code_sandbox_response import ResendCodeSandboxResponse
from .types.reset_sandbox_response import ResetSandboxResponse
from .types.sandbox_signup_request_from import SandboxSignupRequestFrom
from .types.sign_up_sandbox_response import SignUpSandboxResponse
from .types.verify_email_sandbox_response import VerifyEmailSandboxResponse

if typing.TYPE_CHECKING:
    from .claims.client import AsyncClaimsClient, ClaimsClient
# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SandboxClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSandboxClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._claims: typing.Optional[ClaimsClient] = None

    @property
    def with_raw_response(self) -> RawSandboxClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSandboxClient
        """
        return self._raw_client

    def get_challenge(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetChallengeSandboxResponse:
        """
        Returns a proof-of-work challenge for POST /v1/sandbox/sessions. No authentication. Rate-limited per network address (60 per 5 minutes). Solve it by counting `number` from 0 until sha256(salt + number) equals `challenge`; the reference solvers are at https://docs.mesta.xyz/docs/sandbox-create. The challenge is valid for 300 seconds and can be redeemed once. Not runnable from this page: the solution must be computed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChallengeSandboxResponse
            A challenge.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.get_challenge()
        """
        _response = self._raw_client.get_challenge(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        challenge: SandboxChallengeSolution,
        accept_terms: bool,
        name: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        deposit_source: typing.Optional[CreateSandboxSessionRequestDepositSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSandboxResponse:
        """
        Creates a sandbox from a solved challenge: a merchant, one standard key pair and the terms acceptance are written and returned at once with 201; the sample senders, beneficiaries, deposits and orders are added afterwards as a job whose progress GET /v1/sandbox/sessions/{id} reports. The API secret and the claim URL are returned once and never stored; store the response the moment it arrives. No authentication and no Idempotency-Key: the redeemed challenge is the replay handle, and re-presenting it within 24 hours answers 409 CHALLENGE_USED with the sandboxId it produced. Checks run in this order: the provisioning switch (503), the body and country (400 VALIDATION_FAILED, 409 NOT_AVAILABLE_IN_SANDBOX or 422 TERMS_NOT_ACCEPTED), the stateless solution screen (400 or 410), the creation caps (429), then single-use solution redemption (400, 410 or 409). An unclaimed sandbox expires seven days after creation unless someone opens claimUrl and verifies an email address. Not runnable from this page: the solution must be computed.

        Parameters
        ----------
        challenge : SandboxChallengeSolution

        accept_terms : bool
            Must be true: your acceptance of the Sandbox terms (https://ohana.sandbox.mesta.xyz/terms?version=sandbox-2026-10); the Sandbox privacy notice (https://docs.mesta.xyz/docs/sandbox-privacy) explains how Mesta uses your details. An agent may not set it without the person's instruction. Missing or false answers 422 with the terms URL and version in the body.

        name : typing.Optional[str]
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points. Defaults to Sandbox {shortId}.

        country : typing.Optional[str]
            ISO 3166-1 alpha-2 code from the sandbox's merchant country list. Default US.

        deposit_source : typing.Optional[CreateSandboxSessionRequestDepositSource]
            `sender` is the only value accepted at launch; `merchant` answers 409 NOT_AVAILABLE_IN_SANDBOX, superseding the earlier 422 (merchant-funded sandboxes arrive in a later release).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSandboxResponse
            The sandbox, with the key pair and the claim URL, once.

        Examples
        --------
        import datetime

        from mesta import Mesta, SandboxChallengeSolution

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.create(
            challenge=SandboxChallengeSolution(
                challenge="c107eca74592b0fdfd64956fc1ae13a283519c10e796a9a0e84606efe3f55966",
                salt="00112233445566778899aabbccddeeff.1790672400000",
                maxnumber=2097152,
                expires_at=datetime.datetime.fromisoformat(
                    "2026-09-29 09:00:00+00:00",
                ),
                signature="9d2e_example",
                number=12345,
            ),
            accept_terms=True,
            name="Northwind Cross-Border Inc.",
            country="US",
            deposit_source="sender",
        )
        """
        _response = self._raw_client.create(
            challenge=challenge,
            accept_terms=accept_terms,
            name=name,
            country=country,
            deposit_source=deposit_source,
            request_options=request_options,
        )
        return _response.data

    def sign_up(
        self,
        *,
        turnstile_token: str,
        email: str,
        full_name: str,
        password: str,
        country: str,
        accept_terms: bool,
        from_: typing.Optional[SandboxSignupRequestFrom] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignUpSandboxResponse:
        """
        The browser shape, posted by the sandbox portal's sign-up form with a Cloudflare Turnstile token; CORS admits that origin only, so scripts use POST /v1/sandbox/sessions. Creates the sandbox already claimed by the given email with status `claimed`, `emailVerified: false`, no claimUrl, a portal `session`, and 72 hours to enter the emailed code. One live sandbox per verified email address.

        Parameters
        ----------
        turnstile_token : str
            The Cloudflare Turnstile token from the form.

        email : str

        full_name : str
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.

        password : str
            12 to 128 characters; common passwords are refused.

        country : str

        accept_terms : bool
            Must be true.

        from_ : typing.Optional[SandboxSignupRequestFrom]
            Optional sign-up entry point.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignUpSandboxResponse
            The sandbox, with the key pair once and a portal session.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.sign_up(
            turnstile_token="turnstileToken",
            email="email",
            full_name="Example Developer",
            password="password",
            country="US",
            accept_terms=True,
        )
        """
        _response = self._raw_client.sign_up(
            turnstile_token=turnstile_token,
            email=email,
            full_name=full_name,
            password=password,
            country=country,
            accept_terms=accept_terms,
            from_=from_,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSandboxResponse:
        """
        The sandbox's status, deadline, `emailVerified`, `executionPaused`, `pauseMessage`, all seven `counts`, `wallets.senders` usage and per-sender states, the progress of the sample data (`seed.status`, `seed.step`, `seed.steps`, `seed.error`), the `fixtures` block once the sample data is complete, and its keys by id with `kind`, `expiresAt` and `lastUsedAt`; never an API key secret. The `fixtures` include the retrievable webhook signing key. Requires `merchant:sandbox:read` (included in the initial standard integration key; narrower keys must request it) or a session of the sandbox's merchant. Another sandbox's id is 404. A failed sandbox's keys can read this route for 24 hours and nothing else.

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

    def verify_email(
        self, id: str, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyEmailSandboxResponse:
        """
        Enters the six-digit code emailed at sign-up or claim. Success clears `expiresAt` on the sandbox and only on keys flagged expires_with_sandbox (never a retiring predecessor): the sandbox now persists until deleted. Requires a portal session. 20 attempts per hour per network address; five wrong attempts void the code. Wrong attempts return 400 with attemptsRemaining down to zero; a further attempt returns 410 VERIFICATION_CODE_EXPIRED. Resend is an explicit owner action, never automatic.

        Parameters
        ----------
        id : str
            The sandbox id.

        code : str
            The six-digit code from the email. Valid ten minutes; void after five wrong attempts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyEmailSandboxResponse
            Email verified; sandbox expiry cleared. Only expires_with_sandbox keys are cleared; retiring keys keep their deadline.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.verify_email(
            id="id",
            code="123456",
        )
        """
        _response = self._raw_client.verify_email(id, code=code, request_options=request_options)
        return _response.data

    def resend_code(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResendCodeSandboxResponse:
        """
        Sends the replacement code, never the unexpired code again, no sooner than 60 seconds after the last mail; three codes per address per hour and ten per day. A resend never refreshes the attempt allowance of the old code: it voids that code and gives the replacement five fresh attempts. Requires a portal session.

        Parameters
        ----------
        id : str
            The sandbox id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResendCodeSandboxResponse
            Sent.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.resend_code(
            id="id",
        )
        """
        _response = self._raw_client.resend_code(id, request_options=request_options)
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

    def request_production(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestProductionSandboxResponse:
        """
        Records the request on the sandbox after a successful mail and sends one message to Mesta's sales team with the sandbox id, merchant name and owner email. Once a day, from a verified owner's session. Production access requires KYB and Mesta's acceptance; the sandbox is not an approval. The sales mail is sent first; only success records requestedAt. A dispatch pause or dependency fault leaves the request repeatable, without consuming its daily allowance.

        Parameters
        ----------
        id : str
            The sandbox id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestProductionSandboxResponse
            Requested.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.sandbox.request_production(
            id="id",
        )
        """
        _response = self._raw_client.request_production(id, request_options=request_options)
        return _response.data

    def create_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateWalletsSandboxResponse:
        """
        Creates your merchant's wallet with four test-network addresses (Ethereum Sepolia and Polygon Amoy share one, Solana devnet, Tron Nile) when it was skipped while the sample data was added; the home page's wallets card shows "wallets pending" in that case. Attempted once; counted against the sandbox environment's daily wallet ceiling. Requires `merchant:sandbox:write`, key or session.

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
        Creates the sender's wallet with four test-network addresses, once per sender; five senders per sandbox can hold wallets and the sixth answers 409 SANDBOX_CAP_EXCEEDED. The sender must be yours (404 otherwise). Requires `merchant:sender:write`, key or session. The portal's "Generate test wallets" makes this call.

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

    @property
    def claims(self):
        if self._claims is None:
            from .claims.client import ClaimsClient  # noqa: E402

            self._claims = ClaimsClient(client_wrapper=self._client_wrapper)
        return self._claims


class AsyncSandboxClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSandboxClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._claims: typing.Optional[AsyncClaimsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawSandboxClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSandboxClient
        """
        return self._raw_client

    async def get_challenge(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChallengeSandboxResponse:
        """
        Returns a proof-of-work challenge for POST /v1/sandbox/sessions. No authentication. Rate-limited per network address (60 per 5 minutes). Solve it by counting `number` from 0 until sha256(salt + number) equals `challenge`; the reference solvers are at https://docs.mesta.xyz/docs/sandbox-create. The challenge is valid for 300 seconds and can be redeemed once. Not runnable from this page: the solution must be computed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChallengeSandboxResponse
            A challenge.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.get_challenge()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_challenge(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        challenge: SandboxChallengeSolution,
        accept_terms: bool,
        name: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        deposit_source: typing.Optional[CreateSandboxSessionRequestDepositSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSandboxResponse:
        """
        Creates a sandbox from a solved challenge: a merchant, one standard key pair and the terms acceptance are written and returned at once with 201; the sample senders, beneficiaries, deposits and orders are added afterwards as a job whose progress GET /v1/sandbox/sessions/{id} reports. The API secret and the claim URL are returned once and never stored; store the response the moment it arrives. No authentication and no Idempotency-Key: the redeemed challenge is the replay handle, and re-presenting it within 24 hours answers 409 CHALLENGE_USED with the sandboxId it produced. Checks run in this order: the provisioning switch (503), the body and country (400 VALIDATION_FAILED, 409 NOT_AVAILABLE_IN_SANDBOX or 422 TERMS_NOT_ACCEPTED), the stateless solution screen (400 or 410), the creation caps (429), then single-use solution redemption (400, 410 or 409). An unclaimed sandbox expires seven days after creation unless someone opens claimUrl and verifies an email address. Not runnable from this page: the solution must be computed.

        Parameters
        ----------
        challenge : SandboxChallengeSolution

        accept_terms : bool
            Must be true: your acceptance of the Sandbox terms (https://ohana.sandbox.mesta.xyz/terms?version=sandbox-2026-10); the Sandbox privacy notice (https://docs.mesta.xyz/docs/sandbox-privacy) explains how Mesta uses your details. An agent may not set it without the person's instruction. Missing or false answers 422 with the terms URL and version in the body.

        name : typing.Optional[str]
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points. Defaults to Sandbox {shortId}.

        country : typing.Optional[str]
            ISO 3166-1 alpha-2 code from the sandbox's merchant country list. Default US.

        deposit_source : typing.Optional[CreateSandboxSessionRequestDepositSource]
            `sender` is the only value accepted at launch; `merchant` answers 409 NOT_AVAILABLE_IN_SANDBOX, superseding the earlier 422 (merchant-funded sandboxes arrive in a later release).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSandboxResponse
            The sandbox, with the key pair and the claim URL, once.

        Examples
        --------
        import asyncio
        import datetime

        from mesta import AsyncMesta, SandboxChallengeSolution

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.create(
                challenge=SandboxChallengeSolution(
                    challenge="c107eca74592b0fdfd64956fc1ae13a283519c10e796a9a0e84606efe3f55966",
                    salt="00112233445566778899aabbccddeeff.1790672400000",
                    maxnumber=2097152,
                    expires_at=datetime.datetime.fromisoformat(
                        "2026-09-29 09:00:00+00:00",
                    ),
                    signature="9d2e_example",
                    number=12345,
                ),
                accept_terms=True,
                name="Northwind Cross-Border Inc.",
                country="US",
                deposit_source="sender",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            challenge=challenge,
            accept_terms=accept_terms,
            name=name,
            country=country,
            deposit_source=deposit_source,
            request_options=request_options,
        )
        return _response.data

    async def sign_up(
        self,
        *,
        turnstile_token: str,
        email: str,
        full_name: str,
        password: str,
        country: str,
        accept_terms: bool,
        from_: typing.Optional[SandboxSignupRequestFrom] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignUpSandboxResponse:
        """
        The browser shape, posted by the sandbox portal's sign-up form with a Cloudflare Turnstile token; CORS admits that origin only, so scripts use POST /v1/sandbox/sessions. Creates the sandbox already claimed by the given email with status `claimed`, `emailVerified: false`, no claimUrl, a portal `session`, and 72 hours to enter the emailed code. One live sandbox per verified email address.

        Parameters
        ----------
        turnstile_token : str
            The Cloudflare Turnstile token from the form.

        email : str

        full_name : str
            One to 64 Unicode letters or decimal digits, spaces, or . & ' -; no trailing newline. The server validates Unicode code points.

        password : str
            12 to 128 characters; common passwords are refused.

        country : str

        accept_terms : bool
            Must be true.

        from_ : typing.Optional[SandboxSignupRequestFrom]
            Optional sign-up entry point.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignUpSandboxResponse
            The sandbox, with the key pair once and a portal session.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.sign_up(
                turnstile_token="turnstileToken",
                email="email",
                full_name="Example Developer",
                password="password",
                country="US",
                accept_terms=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_up(
            turnstile_token=turnstile_token,
            email=email,
            full_name=full_name,
            password=password,
            country=country,
            accept_terms=accept_terms,
            from_=from_,
            request_options=request_options,
        )
        return _response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSandboxResponse:
        """
        The sandbox's status, deadline, `emailVerified`, `executionPaused`, `pauseMessage`, all seven `counts`, `wallets.senders` usage and per-sender states, the progress of the sample data (`seed.status`, `seed.step`, `seed.steps`, `seed.error`), the `fixtures` block once the sample data is complete, and its keys by id with `kind`, `expiresAt` and `lastUsedAt`; never an API key secret. The `fixtures` include the retrievable webhook signing key. Requires `merchant:sandbox:read` (included in the initial standard integration key; narrower keys must request it) or a session of the sandbox's merchant. Another sandbox's id is 404. A failed sandbox's keys can read this route for 24 hours and nothing else.

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

    async def verify_email(
        self, id: str, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifyEmailSandboxResponse:
        """
        Enters the six-digit code emailed at sign-up or claim. Success clears `expiresAt` on the sandbox and only on keys flagged expires_with_sandbox (never a retiring predecessor): the sandbox now persists until deleted. Requires a portal session. 20 attempts per hour per network address; five wrong attempts void the code. Wrong attempts return 400 with attemptsRemaining down to zero; a further attempt returns 410 VERIFICATION_CODE_EXPIRED. Resend is an explicit owner action, never automatic.

        Parameters
        ----------
        id : str
            The sandbox id.

        code : str
            The six-digit code from the email. Valid ten minutes; void after five wrong attempts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyEmailSandboxResponse
            Email verified; sandbox expiry cleared. Only expires_with_sandbox keys are cleared; retiring keys keep their deadline.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.verify_email(
                id="id",
                code="123456",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_email(id, code=code, request_options=request_options)
        return _response.data

    async def resend_code(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResendCodeSandboxResponse:
        """
        Sends the replacement code, never the unexpired code again, no sooner than 60 seconds after the last mail; three codes per address per hour and ten per day. A resend never refreshes the attempt allowance of the old code: it voids that code and gives the replacement five fresh attempts. Requires a portal session.

        Parameters
        ----------
        id : str
            The sandbox id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResendCodeSandboxResponse
            Sent.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.resend_code(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resend_code(id, request_options=request_options)
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

    async def request_production(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequestProductionSandboxResponse:
        """
        Records the request on the sandbox after a successful mail and sends one message to Mesta's sales team with the sandbox id, merchant name and owner email. Once a day, from a verified owner's session. Production access requires KYB and Mesta's acceptance; the sandbox is not an approval. The sales mail is sent first; only success records requestedAt. A dispatch pause or dependency fault leaves the request repeatable, without consuming its daily allowance.

        Parameters
        ----------
        id : str
            The sandbox id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestProductionSandboxResponse
            Requested.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sandbox.request_production(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_production(id, request_options=request_options)
        return _response.data

    async def create_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateWalletsSandboxResponse:
        """
        Creates your merchant's wallet with four test-network addresses (Ethereum Sepolia and Polygon Amoy share one, Solana devnet, Tron Nile) when it was skipped while the sample data was added; the home page's wallets card shows "wallets pending" in that case. Attempted once; counted against the sandbox environment's daily wallet ceiling. Requires `merchant:sandbox:write`, key or session.

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
        Creates the sender's wallet with four test-network addresses, once per sender; five senders per sandbox can hold wallets and the sixth answers 409 SANDBOX_CAP_EXCEEDED. The sender must be yours (404 otherwise). Requires `merchant:sender:write`, key or session. The portal's "Generate test wallets" makes this call.

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

    @property
    def claims(self):
        if self._claims is None:
            from .claims.client import AsyncClaimsClient  # noqa: E402

            self._claims = AsyncClaimsClient(client_wrapper=self._client_wrapper)
        return self._claims

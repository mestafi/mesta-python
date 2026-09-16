
from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSendersClient, RawSendersClient
from .types.create_senders_request import CreateSendersRequest
from .types.create_senders_response import CreateSendersResponse
from .types.delete_senders_response import DeleteSendersResponse
from .types.get_balances_senders_response import GetBalancesSendersResponse
from .types.get_senders_response import GetSendersResponse
from .types.list_senders_request_sort_by import ListSendersRequestSortBy
from .types.list_senders_request_sort_order import ListSendersRequestSortOrder
from .types.list_senders_request_status import ListSendersRequestStatus
from .types.list_senders_response import ListSendersResponse
from .types.simulate_deposit_senders_response import SimulateDepositSendersResponse
from .types.simulate_verification_result_senders_request_result import SimulateVerificationResultSendersRequestResult
from .types.simulate_verification_result_senders_response import SimulateVerificationResultSendersResponse
from .types.update_senders_request_body import UpdateSendersRequestBody
from .types.update_senders_response import UpdateSendersResponse
from .types.verify_senders_response import VerifySendersResponse

if typing.TYPE_CHECKING:
    from .associates.client import AssociatesClient, AsyncAssociatesClient
    from .deposit_bank_accounts.client import AsyncDepositBankAccountsClient, DepositBankAccountsClient
    from .documents.client import AsyncDocumentsClient, DocumentsClient
    from .source_wallet_addresses.client import AsyncSourceWalletAddressesClient, SourceWalletAddressesClient
    from .terms_of_service.client import AsyncTermsOfServiceClient, TermsOfServiceClient
    from .ubos.client import AsyncUbosClient, UbosClient
    from .virtual_bank_accounts.client import AsyncVirtualBankAccountsClient, VirtualBankAccountsClient
# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SendersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSendersClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._associates: typing.Optional[AssociatesClient] = None
        self._virtual_bank_accounts: typing.Optional[VirtualBankAccountsClient] = None
        self._source_wallet_addresses: typing.Optional[SourceWalletAddressesClient] = None
        self._ubos: typing.Optional[UbosClient] = None
        self._documents: typing.Optional[DocumentsClient] = None
        self._terms_of_service: typing.Optional[TermsOfServiceClient] = None
        self._deposit_bank_accounts: typing.Optional[DepositBankAccountsClient] = None

    @property
    def with_raw_response(self) -> RawSendersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSendersClient
        """
        return self._raw_client

    def list(
        self,
        *,
        id: typing.Optional[str] = None,
        status: typing.Optional[ListSendersRequestStatus] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort_by: typing.Optional[ListSendersRequestSortBy] = None,
        sort_order: typing.Optional[ListSendersRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSendersResponse:
        """
        Retrieves a list of all senders associated with a merchant.

        Parameters
        ----------
        id : typing.Optional[str]
            Filter senders by specific ID

        status : typing.Optional[ListSendersRequestStatus]
            Filter senders by their verification status

        page_size : typing.Optional[int]
            Records per page

        page : typing.Optional[int]
            Page number

        sort_by : typing.Optional[ListSendersRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListSendersRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSendersResponse
            Sender list retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.list()
        """
        _response = self._raw_client.list(
            id=id,
            status=status,
            page_size=page_size,
            page=page,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def create(
        self, *, request: CreateSendersRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateSendersResponse:
        """
        ## Overview
        * Creates a new sender
        * Supports both individual and business senders
        * Includes additional onboarding fields used for compliance review
        * Requirements vary by country and ownerType

        ## Validation Rules
        * **Important**: Always check validation rules before creating a sender
        * Validation rules endpoint: `GET /v2/validation-rules/senders`
        * Required query parameters:
           * `ownerType=[individual|business]`
          * `country=[ISO 3166-1 alpha-2 code]`
        * Example request:
        ```
        GET /v2/validation-rules/senders?ownerType=individual&country=MX
        ```

        ## Additional v2 Notes
        * `expectedMonthlyVolumeEstimate`, `averageTransactionSize`, `primaryCounterpartyJurisdictions`, `natureOfPayments`, and `sourceOfFunds` are required for both sender types
        * Each value in `primaryCounterpartyJurisdictions` must be an ISO 3166-1 alpha-2 country code (for example: `US`, `IN`, `GB`)
        * `isFinancialInstitution` and `numberOfEmployees` are required for business senders
        * `websiteAbsenceReason` is required for business senders when `websiteUrl` is not provided
        * If `isFinancialInstitution` is `true`, upload the FI registration proof using `POST /v1/senders/{senderId}/documents` with document type `fi_registration_proof` before calling `POST /v1/senders/{senderId}/verify`

        Parameters
        ----------
        request : CreateSendersRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSendersResponse
            Sender created successfully

        Examples
        --------
        import datetime

        from mesta import Address, IndividualSenderIdentity, IndividualSenderV2, Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.create(
            request=IndividualSenderV2(
                expected_monthly_volume_estimate=1.1,
                average_transaction_size=1.1,
                primary_counterparty_jurisdictions=["primaryCounterpartyJurisdictions"],
                nature_of_payments=["payroll"],
                source_of_funds="advance_from_director",
                type="individual",
                first_name="firstName",
                last_name="lastName",
                birth_date=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                email="email",
                phone="phone",
                addresses=[
                    Address(
                        street="street",
                        city="city",
                        postal_code="12345 or 00000",
                        country="country",
                    )
                ],
                identity=IndividualSenderIdentity(
                    document_type="PASSPORT",
                    country_code="countryCode",
                    document_number="documentNumber",
                ),
                gender="male",
                occupation="accountant",
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    def get(self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSendersResponse:
        """
        Retrieves detailed information about a specific sender account.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSendersResponse
            Sender retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.get(
            sender_id="senderId",
        )
        """
        _response = self._raw_client.get(sender_id, request_options=request_options)
        return _response.data

    def delete(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSendersResponse:
        """
        Deletes a sender account.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSendersResponse
            Delete Sender Successful

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.delete(
            sender_id="senderId",
        )
        """
        _response = self._raw_client.delete(sender_id, request_options=request_options)
        return _response.data

    def update(
        self,
        sender_id: str,
        *,
        request: UpdateSendersRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSendersResponse:
        """
        Updates an existing sender's information. Note that certain fields cannot be modified after initial creation:

        - type (individual/business)
        - identificationNumber (for business senders)
        - taxIdentificationNumber (for business senders)

        Before updating a sender, always check the validation rules using:
        GET /v2/validation-rules/senders?ownerType=[individual|business]&country=[ISO 3166-1 alpha-2 code]

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request : UpdateSendersRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSendersResponse
            Sender updated successfully

        Examples
        --------
        from mesta import Mesta, PatchIndividualSender

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.update(
            sender_id="senderId",
            request=PatchIndividualSender(),
        )
        """
        _response = self._raw_client.update(sender_id, request=request, request_options=request_options)
        return _response.data

    def simulate_verification_result(
        self,
        sender_id: str,
        *,
        result: SimulateVerificationResultSendersRequestResult,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateVerificationResultSendersResponse:
        """
        Settles a pending sender verification with a simulated provider decision so you can drive onboarding end to end without waiting on the identity provider. Available in test environments only — disabled in production.

        Verification must already have been started via the corresponding `/verify` call; otherwise the request is rejected with `MOCK_VERIFICATION_NOT_INITIATED`. For a business sender the same result is applied to the sender's KYB and to every UBO and unlinked associate on it, matching how the provider settles them individually.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        result : SimulateVerificationResultSendersRequestResult
            The verification outcome to simulate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimulateVerificationResultSendersResponse
            Simulated verification result applied.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.simulate_verification_result(
            sender_id="senderId",
            result="APPROVED",
        )
        """
        _response = self._raw_client.simulate_verification_result(
            sender_id, result=result, request_options=request_options
        )
        return _response.data

    def verify(
        self,
        sender_id: str,
        *,
        request_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VerifySendersResponse:
        """
        Runs the authoritative union of base sender, country-specific, accepted-capability, and persisted UBO/associate requirements, minus canonical data already stored. If no blockers remain, it initiates the existing verification process. If requirements are incomplete, verification does not start and the API returns actionable `CAPABILITY_REQUIREMENTS_MISSING` blockers.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request_id : typing.Optional[int]
            Unique identifier for the Verify Sender request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifySendersResponse
            Sender Verification Requested

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.verify(
            sender_id="senderId",
        )
        """
        _response = self._raw_client.verify(sender_id, request_id=request_id, request_options=request_options)
        return _response.data

    def get_balances(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBalancesSendersResponse:
        """
        Retrieves the account balances for a specific sender across all supported currencies. Returns an array of currency-balance pairs for all currencies where the sender has an account.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBalancesSendersResponse
            Balances retrieved successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.get_balances(
            sender_id="senderId",
        )
        """
        _response = self._raw_client.get_balances(sender_id, request_options=request_options)
        return _response.data

    def simulate_deposit(
        self,
        sender_id: str,
        *,
        amount: float,
        currency: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateDepositSendersResponse:
        """
        Credits a sender's deposit account with simulated funds so you can test order flows end to end without moving real money.

        **Available in test environments only.** This endpoint is disabled in production and returns `403 FORBIDDEN` there.

        The credit is applied asynchronously: a successful call only confirms that the simulated deposit was accepted. The funds land once the banking provider's webhook is processed, which normally takes a few seconds. Poll `GET /v1/senders/{senderId}/balances` to confirm the balance has moved.

        **Limits**

        - `amount` must be greater than `0` and no more than `200` per request. Repeat the call to fund larger balances.
        - Rate limited to 10 requests per 2 hours for this endpoint, counted per source IP address. Every rejected request also consumes quota, including `401`, `403`, `400` and `404` responses.
        - Simulated deposits are only supported for deposit accounts held with a banking provider that offers a deposit simulator. Accounts on other providers return `MOCK_DEPOSIT_NOT_SUPPORTED_FOR_ACCOUNT`.

        **Permissions**

        The API key must carry the `merchant:sender:write` permission (`merchant:*:*` also matches). Without it the request is rejected with `403 FORBIDDEN`.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender

        amount : float
            Amount to credit, in the deposit currency. Must be greater than 0 and no more than 200 per request.

        currency : typing.Optional[str]
            Currency of the deposit account to credit, for example `USD`, `EUR`, `GBP` or `MXN`. The sender must already have a deposit account in this currency. Optional in the contract but effectively required in practice: always pass it explicitly, because omitting it can resolve a different deposit account than you intend and fail with `NO_DEPOSIT_BANK_ACCOUNT_FOUND`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimulateDepositSendersResponse
            Simulated deposit accepted. The credit is applied asynchronously — poll `GET /v1/senders/{senderId}/balances` to confirm.

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.senders.simulate_deposit(
            sender_id="senderId",
            amount=1.1,
            currency="USD",
        )
        """
        _response = self._raw_client.simulate_deposit(
            sender_id, amount=amount, currency=currency, request_options=request_options
        )
        return _response.data

    @property
    def associates(self):
        if self._associates is None:
            from .associates.client import AssociatesClient  # noqa: E402

            self._associates = AssociatesClient(client_wrapper=self._client_wrapper)
        return self._associates

    @property
    def virtual_bank_accounts(self):
        if self._virtual_bank_accounts is None:
            from .virtual_bank_accounts.client import VirtualBankAccountsClient  # noqa: E402

            self._virtual_bank_accounts = VirtualBankAccountsClient(client_wrapper=self._client_wrapper)
        return self._virtual_bank_accounts

    @property
    def source_wallet_addresses(self):
        if self._source_wallet_addresses is None:
            from .source_wallet_addresses.client import SourceWalletAddressesClient  # noqa: E402

            self._source_wallet_addresses = SourceWalletAddressesClient(client_wrapper=self._client_wrapper)
        return self._source_wallet_addresses

    @property
    def ubos(self):
        if self._ubos is None:
            from .ubos.client import UbosClient  # noqa: E402

            self._ubos = UbosClient(client_wrapper=self._client_wrapper)
        return self._ubos

    @property
    def documents(self):
        if self._documents is None:
            from .documents.client import DocumentsClient  # noqa: E402

            self._documents = DocumentsClient(client_wrapper=self._client_wrapper)
        return self._documents

    @property
    def terms_of_service(self):
        if self._terms_of_service is None:
            from .terms_of_service.client import TermsOfServiceClient  # noqa: E402

            self._terms_of_service = TermsOfServiceClient(client_wrapper=self._client_wrapper)
        return self._terms_of_service

    @property
    def deposit_bank_accounts(self):
        if self._deposit_bank_accounts is None:
            from .deposit_bank_accounts.client import DepositBankAccountsClient  # noqa: E402

            self._deposit_bank_accounts = DepositBankAccountsClient(client_wrapper=self._client_wrapper)
        return self._deposit_bank_accounts


class AsyncSendersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSendersClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._associates: typing.Optional[AsyncAssociatesClient] = None
        self._virtual_bank_accounts: typing.Optional[AsyncVirtualBankAccountsClient] = None
        self._source_wallet_addresses: typing.Optional[AsyncSourceWalletAddressesClient] = None
        self._ubos: typing.Optional[AsyncUbosClient] = None
        self._documents: typing.Optional[AsyncDocumentsClient] = None
        self._terms_of_service: typing.Optional[AsyncTermsOfServiceClient] = None
        self._deposit_bank_accounts: typing.Optional[AsyncDepositBankAccountsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawSendersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSendersClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        id: typing.Optional[str] = None,
        status: typing.Optional[ListSendersRequestStatus] = None,
        page_size: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        sort_by: typing.Optional[ListSendersRequestSortBy] = None,
        sort_order: typing.Optional[ListSendersRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSendersResponse:
        """
        Retrieves a list of all senders associated with a merchant.

        Parameters
        ----------
        id : typing.Optional[str]
            Filter senders by specific ID

        status : typing.Optional[ListSendersRequestStatus]
            Filter senders by their verification status

        page_size : typing.Optional[int]
            Records per page

        page : typing.Optional[int]
            Page number

        sort_by : typing.Optional[ListSendersRequestSortBy]
            Sort column

        sort_order : typing.Optional[ListSendersRequestSortOrder]
            Sort order

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSendersResponse
            Sender list retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            id=id,
            status=status,
            page_size=page_size,
            page=page,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self, *, request: CreateSendersRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateSendersResponse:
        """
        ## Overview
        * Creates a new sender
        * Supports both individual and business senders
        * Includes additional onboarding fields used for compliance review
        * Requirements vary by country and ownerType

        ## Validation Rules
        * **Important**: Always check validation rules before creating a sender
        * Validation rules endpoint: `GET /v2/validation-rules/senders`
        * Required query parameters:
           * `ownerType=[individual|business]`
          * `country=[ISO 3166-1 alpha-2 code]`
        * Example request:
        ```
        GET /v2/validation-rules/senders?ownerType=individual&country=MX
        ```

        ## Additional v2 Notes
        * `expectedMonthlyVolumeEstimate`, `averageTransactionSize`, `primaryCounterpartyJurisdictions`, `natureOfPayments`, and `sourceOfFunds` are required for both sender types
        * Each value in `primaryCounterpartyJurisdictions` must be an ISO 3166-1 alpha-2 country code (for example: `US`, `IN`, `GB`)
        * `isFinancialInstitution` and `numberOfEmployees` are required for business senders
        * `websiteAbsenceReason` is required for business senders when `websiteUrl` is not provided
        * If `isFinancialInstitution` is `true`, upload the FI registration proof using `POST /v1/senders/{senderId}/documents` with document type `fi_registration_proof` before calling `POST /v1/senders/{senderId}/verify`

        Parameters
        ----------
        request : CreateSendersRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSendersResponse
            Sender created successfully

        Examples
        --------
        import asyncio
        import datetime

        from mesta import (
            Address,
            AsyncMesta,
            IndividualSenderIdentity,
            IndividualSenderV2,
        )

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.create(
                request=IndividualSenderV2(
                    expected_monthly_volume_estimate=1.1,
                    average_transaction_size=1.1,
                    primary_counterparty_jurisdictions=[
                        "primaryCounterpartyJurisdictions"
                    ],
                    nature_of_payments=["payroll"],
                    source_of_funds="advance_from_director",
                    type="individual",
                    first_name="firstName",
                    last_name="lastName",
                    birth_date=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                    email="email",
                    phone="phone",
                    addresses=[
                        Address(
                            street="street",
                            city="city",
                            postal_code="12345 or 00000",
                            country="country",
                        )
                    ],
                    identity=IndividualSenderIdentity(
                        document_type="PASSPORT",
                        country_code="countryCode",
                        document_number="documentNumber",
                    ),
                    gender="male",
                    occupation="accountant",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    async def get(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSendersResponse:
        """
        Retrieves detailed information about a specific sender account.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSendersResponse
            Sender retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.get(
                sender_id="senderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(sender_id, request_options=request_options)
        return _response.data

    async def delete(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSendersResponse:
        """
        Deletes a sender account.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSendersResponse
            Delete Sender Successful

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.delete(
                sender_id="senderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(sender_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        sender_id: str,
        *,
        request: UpdateSendersRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSendersResponse:
        """
        Updates an existing sender's information. Note that certain fields cannot be modified after initial creation:

        - type (individual/business)
        - identificationNumber (for business senders)
        - taxIdentificationNumber (for business senders)

        Before updating a sender, always check the validation rules using:
        GET /v2/validation-rules/senders?ownerType=[individual|business]&country=[ISO 3166-1 alpha-2 code]

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request : UpdateSendersRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSendersResponse
            Sender updated successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta, PatchIndividualSender

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.update(
                sender_id="senderId",
                request=PatchIndividualSender(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(sender_id, request=request, request_options=request_options)
        return _response.data

    async def simulate_verification_result(
        self,
        sender_id: str,
        *,
        result: SimulateVerificationResultSendersRequestResult,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateVerificationResultSendersResponse:
        """
        Settles a pending sender verification with a simulated provider decision so you can drive onboarding end to end without waiting on the identity provider. Available in test environments only — disabled in production.

        Verification must already have been started via the corresponding `/verify` call; otherwise the request is rejected with `MOCK_VERIFICATION_NOT_INITIATED`. For a business sender the same result is applied to the sender's KYB and to every UBO and unlinked associate on it, matching how the provider settles them individually.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        result : SimulateVerificationResultSendersRequestResult
            The verification outcome to simulate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimulateVerificationResultSendersResponse
            Simulated verification result applied.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.simulate_verification_result(
                sender_id="senderId",
                result="APPROVED",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simulate_verification_result(
            sender_id, result=result, request_options=request_options
        )
        return _response.data

    async def verify(
        self,
        sender_id: str,
        *,
        request_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VerifySendersResponse:
        """
        Runs the authoritative union of base sender, country-specific, accepted-capability, and persisted UBO/associate requirements, minus canonical data already stored. If no blockers remain, it initiates the existing verification process. If requirements are incomplete, verification does not start and the API returns actionable `CAPABILITY_REQUIREMENTS_MISSING` blockers.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender.

        request_id : typing.Optional[int]
            Unique identifier for the Verify Sender request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifySendersResponse
            Sender Verification Requested

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.verify(
                sender_id="senderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify(sender_id, request_id=request_id, request_options=request_options)
        return _response.data

    async def get_balances(
        self, sender_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBalancesSendersResponse:
        """
        Retrieves the account balances for a specific sender across all supported currencies. Returns an array of currency-balance pairs for all currencies where the sender has an account.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBalancesSendersResponse
            Balances retrieved successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.get_balances(
                sender_id="senderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_balances(sender_id, request_options=request_options)
        return _response.data

    async def simulate_deposit(
        self,
        sender_id: str,
        *,
        amount: float,
        currency: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SimulateDepositSendersResponse:
        """
        Credits a sender's deposit account with simulated funds so you can test order flows end to end without moving real money.

        **Available in test environments only.** This endpoint is disabled in production and returns `403 FORBIDDEN` there.

        The credit is applied asynchronously: a successful call only confirms that the simulated deposit was accepted. The funds land once the banking provider's webhook is processed, which normally takes a few seconds. Poll `GET /v1/senders/{senderId}/balances` to confirm the balance has moved.

        **Limits**

        - `amount` must be greater than `0` and no more than `200` per request. Repeat the call to fund larger balances.
        - Rate limited to 10 requests per 2 hours for this endpoint, counted per source IP address. Every rejected request also consumes quota, including `401`, `403`, `400` and `404` responses.
        - Simulated deposits are only supported for deposit accounts held with a banking provider that offers a deposit simulator. Accounts on other providers return `MOCK_DEPOSIT_NOT_SUPPORTED_FOR_ACCOUNT`.

        **Permissions**

        The API key must carry the `merchant:sender:write` permission (`merchant:*:*` also matches). Without it the request is rejected with `403 FORBIDDEN`.

        Parameters
        ----------
        sender_id : str
            Unique identifier for the sender

        amount : float
            Amount to credit, in the deposit currency. Must be greater than 0 and no more than 200 per request.

        currency : typing.Optional[str]
            Currency of the deposit account to credit, for example `USD`, `EUR`, `GBP` or `MXN`. The sender must already have a deposit account in this currency. Optional in the contract but effectively required in practice: always pass it explicitly, because omitting it can resolve a different deposit account than you intend and fail with `NO_DEPOSIT_BANK_ACCOUNT_FOUND`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimulateDepositSendersResponse
            Simulated deposit accepted. The credit is applied asynchronously — poll `GET /v1/senders/{senderId}/balances` to confirm.

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.senders.simulate_deposit(
                sender_id="senderId",
                amount=1.1,
                currency="USD",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simulate_deposit(
            sender_id, amount=amount, currency=currency, request_options=request_options
        )
        return _response.data

    @property
    def associates(self):
        if self._associates is None:
            from .associates.client import AsyncAssociatesClient  # noqa: E402

            self._associates = AsyncAssociatesClient(client_wrapper=self._client_wrapper)
        return self._associates

    @property
    def virtual_bank_accounts(self):
        if self._virtual_bank_accounts is None:
            from .virtual_bank_accounts.client import AsyncVirtualBankAccountsClient  # noqa: E402

            self._virtual_bank_accounts = AsyncVirtualBankAccountsClient(client_wrapper=self._client_wrapper)
        return self._virtual_bank_accounts

    @property
    def source_wallet_addresses(self):
        if self._source_wallet_addresses is None:
            from .source_wallet_addresses.client import AsyncSourceWalletAddressesClient  # noqa: E402

            self._source_wallet_addresses = AsyncSourceWalletAddressesClient(client_wrapper=self._client_wrapper)
        return self._source_wallet_addresses

    @property
    def ubos(self):
        if self._ubos is None:
            from .ubos.client import AsyncUbosClient  # noqa: E402

            self._ubos = AsyncUbosClient(client_wrapper=self._client_wrapper)
        return self._ubos

    @property
    def documents(self):
        if self._documents is None:
            from .documents.client import AsyncDocumentsClient  # noqa: E402

            self._documents = AsyncDocumentsClient(client_wrapper=self._client_wrapper)
        return self._documents

    @property
    def terms_of_service(self):
        if self._terms_of_service is None:
            from .terms_of_service.client import AsyncTermsOfServiceClient  # noqa: E402

            self._terms_of_service = AsyncTermsOfServiceClient(client_wrapper=self._client_wrapper)
        return self._terms_of_service

    @property
    def deposit_bank_accounts(self):
        if self._deposit_bank_accounts is None:
            from .deposit_bank_accounts.client import AsyncDepositBankAccountsClient  # noqa: E402

            self._deposit_bank_accounts = AsyncDepositBankAccountsClient(client_wrapper=self._client_wrapper)
        return self._deposit_bank_accounts

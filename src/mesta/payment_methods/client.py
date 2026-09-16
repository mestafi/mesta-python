
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment_method_status import PaymentMethodStatus
from ..types.payment_method_type import PaymentMethodType
from .raw_client import AsyncRawPaymentMethodsClient, RawPaymentMethodsClient
from .types.consent_decision_request_status import ConsentDecisionRequestStatus
from .types.create_payment_method_request_data import CreatePaymentMethodRequestData
from .types.create_payment_methods_response import CreatePaymentMethodsResponse
from .types.decide_consent_payment_methods_response import DecideConsentPaymentMethodsResponse
from .types.delete_payment_methods_response import DeletePaymentMethodsResponse
from .types.get_payment_methods_response import GetPaymentMethodsResponse
from .types.list_payment_methods_request_sort_by import ListPaymentMethodsRequestSortBy
from .types.list_payment_methods_request_sort_order import ListPaymentMethodsRequestSortOrder
from .types.list_payment_methods_response import ListPaymentMethodsResponse
from .types.update_payment_method_request_data import UpdatePaymentMethodRequestData
from .types.update_payment_methods_response import UpdatePaymentMethodsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PaymentMethodsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentMethodsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentMethodsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentMethodsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListPaymentMethodsRequestSortBy] = None,
        sort_order: typing.Optional[ListPaymentMethodsRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        beneficiary_id: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodType] = None,
        status: typing.Optional[PaymentMethodStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPaymentMethodsResponse:
        """
        Retrieve a paginated list of payment methods. Filter by beneficiary, type, or status.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListPaymentMethodsRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[ListPaymentMethodsRequestSortOrder]
            Sort order

        search : typing.Optional[str]
            Search query

        beneficiary_id : typing.Optional[str]
            Filter by beneficiary ID

        type : typing.Optional[PaymentMethodType]
            Filter by payment method type

        status : typing.Optional[PaymentMethodStatus]
            Filter by status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPaymentMethodsResponse
            Paginated list of payment methods

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.payment_methods.list()
        """
        _response = self._raw_client.list(
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            beneficiary_id=beneficiary_id,
            type=type,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        beneficiary_id: str,
        type: PaymentMethodType,
        data: CreatePaymentMethodRequestData,
        label: typing.Optional[str] = OMIT,
        requires_user_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePaymentMethodsResponse:
        """
        Create a new payment method for a beneficiary. The payment method type determines the required data fields.

        Parameters
        ----------
        beneficiary_id : str
            ID of the beneficiary this payment method belongs to

        type : PaymentMethodType

        data : CreatePaymentMethodRequestData
            Payment method data. Structure depends on the type field. See BankAccountInfo, PixInfo, InstapayInfo, etc.

        label : typing.Optional[str]
            Display label for the payment method

        requires_user_consent : typing.Optional[bool]
            Whether user consent is required before approval

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePaymentMethodsResponse
            Payment method created successfully

        Examples
        --------
        from mesta import BankAccountInfo, Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.payment_methods.create(
            beneficiary_id="550e8400-e29b-41d4-a716-446655440001",
            type="bank_account",
            data=BankAccountInfo(
                account_number="1234567890",
            ),
        )
        """
        _response = self._raw_client.create(
            beneficiary_id=beneficiary_id,
            type=type,
            data=data,
            label=label,
            requires_user_consent=requires_user_consent,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetPaymentMethodsResponse:
        """
        Retrieve a specific payment method by its ID.

        Parameters
        ----------
        id : str
            Payment method ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentMethodsResponse
            Payment method details

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.payment_methods.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def update(
        self,
        id: str,
        *,
        type: PaymentMethodType,
        data: UpdatePaymentMethodRequestData,
        label: typing.Optional[str] = OMIT,
        requires_user_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePaymentMethodsResponse:
        """
        Update an existing payment method. All required fields must be provided.

        Parameters
        ----------
        id : str
            Payment method ID

        type : PaymentMethodType

        data : UpdatePaymentMethodRequestData
            Payment method data. Structure depends on the type field.

        label : typing.Optional[str]
            Display label for the payment method

        requires_user_consent : typing.Optional[bool]
            Whether user consent is required before approval

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePaymentMethodsResponse
            Payment method updated successfully

        Examples
        --------
        from mesta import BankAccountInfo, Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.payment_methods.update(
            id="id",
            type="bank_account",
            data=BankAccountInfo(
                account_number="1234567890",
            ),
        )
        """
        _response = self._raw_client.update(
            id,
            type=type,
            data=data,
            label=label,
            requires_user_consent=requires_user_consent,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePaymentMethodsResponse:
        """
        Delete a payment method by its ID.

        Parameters
        ----------
        id : str
            Payment method ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePaymentMethodsResponse
            Payment method deleted successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.payment_methods.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def decide_consent(
        self,
        id: str,
        *,
        status: typing.Optional[ConsentDecisionRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DecideConsentPaymentMethodsResponse:
        """
        Approve or decline a payment method that requires user consent.

        Parameters
        ----------
        id : str
            Payment method ID

        status : typing.Optional[ConsentDecisionRequestStatus]
            The consent decision — either approve or decline the payment method

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecideConsentPaymentMethodsResponse
            Consent decision applied successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.payment_methods.decide_consent(
            id="id",
        )
        """
        _response = self._raw_client.decide_consent(id, status=status, request_options=request_options)
        return _response.data


class AsyncPaymentMethodsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentMethodsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentMethodsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentMethodsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[ListPaymentMethodsRequestSortBy] = None,
        sort_order: typing.Optional[ListPaymentMethodsRequestSortOrder] = None,
        search: typing.Optional[str] = None,
        beneficiary_id: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodType] = None,
        status: typing.Optional[PaymentMethodStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPaymentMethodsResponse:
        """
        Retrieve a paginated list of payment methods. Filter by beneficiary, type, or status.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed)

        page_size : typing.Optional[int]
            Number of records per page

        sort_by : typing.Optional[ListPaymentMethodsRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[ListPaymentMethodsRequestSortOrder]
            Sort order

        search : typing.Optional[str]
            Search query

        beneficiary_id : typing.Optional[str]
            Filter by beneficiary ID

        type : typing.Optional[PaymentMethodType]
            Filter by payment method type

        status : typing.Optional[PaymentMethodStatus]
            Filter by status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPaymentMethodsResponse
            Paginated list of payment methods

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payment_methods.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search=search,
            beneficiary_id=beneficiary_id,
            type=type,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        beneficiary_id: str,
        type: PaymentMethodType,
        data: CreatePaymentMethodRequestData,
        label: typing.Optional[str] = OMIT,
        requires_user_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePaymentMethodsResponse:
        """
        Create a new payment method for a beneficiary. The payment method type determines the required data fields.

        Parameters
        ----------
        beneficiary_id : str
            ID of the beneficiary this payment method belongs to

        type : PaymentMethodType

        data : CreatePaymentMethodRequestData
            Payment method data. Structure depends on the type field. See BankAccountInfo, PixInfo, InstapayInfo, etc.

        label : typing.Optional[str]
            Display label for the payment method

        requires_user_consent : typing.Optional[bool]
            Whether user consent is required before approval

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePaymentMethodsResponse
            Payment method created successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta, BankAccountInfo

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payment_methods.create(
                beneficiary_id="550e8400-e29b-41d4-a716-446655440001",
                type="bank_account",
                data=BankAccountInfo(
                    account_number="1234567890",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            beneficiary_id=beneficiary_id,
            type=type,
            data=data,
            label=label,
            requires_user_consent=requires_user_consent,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPaymentMethodsResponse:
        """
        Retrieve a specific payment method by its ID.

        Parameters
        ----------
        id : str
            Payment method ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentMethodsResponse
            Payment method details

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payment_methods.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: str,
        *,
        type: PaymentMethodType,
        data: UpdatePaymentMethodRequestData,
        label: typing.Optional[str] = OMIT,
        requires_user_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePaymentMethodsResponse:
        """
        Update an existing payment method. All required fields must be provided.

        Parameters
        ----------
        id : str
            Payment method ID

        type : PaymentMethodType

        data : UpdatePaymentMethodRequestData
            Payment method data. Structure depends on the type field.

        label : typing.Optional[str]
            Display label for the payment method

        requires_user_consent : typing.Optional[bool]
            Whether user consent is required before approval

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePaymentMethodsResponse
            Payment method updated successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta, BankAccountInfo

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payment_methods.update(
                id="id",
                type="bank_account",
                data=BankAccountInfo(
                    account_number="1234567890",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id,
            type=type,
            data=data,
            label=label,
            requires_user_consent=requires_user_consent,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePaymentMethodsResponse:
        """
        Delete a payment method by its ID.

        Parameters
        ----------
        id : str
            Payment method ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePaymentMethodsResponse
            Payment method deleted successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payment_methods.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def decide_consent(
        self,
        id: str,
        *,
        status: typing.Optional[ConsentDecisionRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DecideConsentPaymentMethodsResponse:
        """
        Approve or decline a payment method that requires user consent.

        Parameters
        ----------
        id : str
            Payment method ID

        status : typing.Optional[ConsentDecisionRequestStatus]
            The consent decision — either approve or decline the payment method

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecideConsentPaymentMethodsResponse
            Consent decision applied successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payment_methods.decide_consent(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decide_consent(id, status=status, request_options=request_options)
        return _response.data

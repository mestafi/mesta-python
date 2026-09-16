
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawDocumentsClient, RawDocumentsClient
from .types.get_presigned_url_documents_request_type import GetPresignedUrlDocumentsRequestType
from .types.get_presigned_url_documents_response import GetPresignedUrlDocumentsResponse
from .types.get_purpose_of_payment_presigned_url_documents_response import (
    GetPurposeOfPaymentPresignedUrlDocumentsResponse,
)


class DocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocumentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDocumentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocumentsClient
        """
        return self._raw_client

    def get_presigned_url(
        self,
        beneficiary_id: str,
        document_id: str,
        *,
        type: typing.Optional[GetPresignedUrlDocumentsRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPresignedUrlDocumentsResponse:
        """
        Generates a pre-signed URL to download a beneficiary's uploaded document. The URL expires after 300 seconds.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier of the beneficiary

        document_id : str
            Unique identifier of the document

        type : typing.Optional[GetPresignedUrlDocumentsRequestType]
            Type of document to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPresignedUrlDocumentsResponse
            Pre-signed URL generated successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.beneficiaries.documents.get_presigned_url(
            beneficiary_id="beneficiaryId",
            document_id="documentId",
        )
        """
        _response = self._raw_client.get_presigned_url(
            beneficiary_id, document_id, type=type, request_options=request_options
        )
        return _response.data

    def get_purpose_of_payment_presigned_url(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPurposeOfPaymentPresignedUrlDocumentsResponse:
        """
        Generate a pre-signed URL for downloading the purpose of payment document attached to a beneficiary. The URL expires in 300 seconds.

        Parameters
        ----------
        id : str
            Beneficiary ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPurposeOfPaymentPresignedUrlDocumentsResponse
            Presigned URL generated successfully

        Examples
        --------
        from mesta import Mesta

        client = Mesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )
        client.beneficiaries.documents.get_purpose_of_payment_presigned_url(
            id="id",
        )
        """
        _response = self._raw_client.get_purpose_of_payment_presigned_url(id, request_options=request_options)
        return _response.data


class AsyncDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocumentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDocumentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocumentsClient
        """
        return self._raw_client

    async def get_presigned_url(
        self,
        beneficiary_id: str,
        document_id: str,
        *,
        type: typing.Optional[GetPresignedUrlDocumentsRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPresignedUrlDocumentsResponse:
        """
        Generates a pre-signed URL to download a beneficiary's uploaded document. The URL expires after 300 seconds.

        Parameters
        ----------
        beneficiary_id : str
            Unique identifier of the beneficiary

        document_id : str
            Unique identifier of the document

        type : typing.Optional[GetPresignedUrlDocumentsRequestType]
            Type of document to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPresignedUrlDocumentsResponse
            Pre-signed URL generated successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.beneficiaries.documents.get_presigned_url(
                beneficiary_id="beneficiaryId",
                document_id="documentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_presigned_url(
            beneficiary_id, document_id, type=type, request_options=request_options
        )
        return _response.data

    async def get_purpose_of_payment_presigned_url(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPurposeOfPaymentPresignedUrlDocumentsResponse:
        """
        Generate a pre-signed URL for downloading the purpose of payment document attached to a beneficiary. The URL expires in 300 seconds.

        Parameters
        ----------
        id : str
            Beneficiary ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPurposeOfPaymentPresignedUrlDocumentsResponse
            Presigned URL generated successfully

        Examples
        --------
        import asyncio

        from mesta import AsyncMesta

        client = AsyncMesta(
            api_secret="YOUR_API_SECRET",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.beneficiaries.documents.get_purpose_of_payment_presigned_url(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_purpose_of_payment_presigned_url(id, request_options=request_options)
        return _response.data

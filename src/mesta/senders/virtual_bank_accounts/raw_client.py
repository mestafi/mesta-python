
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.conflict_error import ConflictError
from ...errors.forbidden_error import ForbiddenError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.sender_virtual_accounts_envelope import SenderVirtualAccountsEnvelope
from ...types.virtual_account_setup_envelope import VirtualAccountSetupEnvelope
from .types.cancel_setup_virtual_bank_accounts_request_currency import CancelSetupVirtualBankAccountsRequestCurrency
from .types.get_setup_status_virtual_bank_accounts_request_currency import (
    GetSetupStatusVirtualBankAccountsRequestCurrency,
)
from .types.get_virtual_bank_accounts_request_currency import GetVirtualBankAccountsRequestCurrency
from .types.request_setup_virtual_bank_accounts_request_currency import RequestSetupVirtualBankAccountsRequestCurrency
from .types.update_setup_data_virtual_bank_accounts_request_currency import (
    UpdateSetupDataVirtualBankAccountsRequestCurrency,
)
from .types.update_virtual_account_setup_data_associate_details_item import (
    UpdateVirtualAccountSetupDataAssociateDetailsItem,
)
from .types.update_virtual_account_setup_data_sender_details import UpdateVirtualAccountSetupDataSenderDetails
from .types.update_virtual_account_setup_data_ubo_details_item import UpdateVirtualAccountSetupDataUboDetailsItem
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawVirtualBankAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_setup_status(
        self,
        sender_id: str,
        currency: GetSetupStatusVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VirtualAccountSetupEnvelope]:
        """
        Returns the sender's current virtual bank account status for the currency. No request ID is required. This read can reconcile status but cannot start account setup. The endpoint follows the sender's current account configuration; if Mesta changes that configuration, a request associated with the previous configuration is no longer returned and the merchant should POST again for the current configuration.

        Parameters
        ----------
        sender_id : str

        currency : GetSetupStatusVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VirtualAccountSetupEnvelope]
            Current setup-request state.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def request_setup(
        self,
        sender_id: str,
        currency: RequestSetupVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VirtualAccountSetupEnvelope]:
        """
        Creates or reuses the current virtual bank account request for this sender and currency. It is evaluated immediately and may begin setup automatically when all requirements are satisfied. Follow returned blocker actions when more information or verification is needed.

        Parameters
        ----------
        sender_id : str

        currency : RequestSetupVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VirtualAccountSetupEnvelope]
            Current setup-request state.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_setup(
        self,
        sender_id: str,
        currency: CancelSetupVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VirtualAccountSetupEnvelope]:
        """
        Cancels the current request before account setup begins or after failure. Provisioning and completed requests cannot be cancelled. A later POST creates a fresh current request.

        Parameters
        ----------
        sender_id : str

        currency : CancelSetupVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VirtualAccountSetupEnvelope]
            Cancelled setup-request state.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_setup_data(
        self,
        sender_id: str,
        currency: UpdateSetupDataVirtualBankAccountsRequestCurrency,
        *,
        sender_details: typing.Optional[UpdateVirtualAccountSetupDataSenderDetails] = OMIT,
        ubo_details: typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataUboDetailsItem]] = OMIT,
        associate_details: typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataAssociateDetailsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VirtualAccountSetupEnvelope]:
        """
        Fills supported missing sender, UBO, or existing-representative values, then re-evaluates the current setup request. Fields that are not current blockers are skipped and identified in unacceptedFields; other submitted fields are still processed. Existing values cannot be overwritten. To reuse the registered address as the trading address, set senderDetails.tradingAddressSameAsRegistered to true. If a manual tradingAddress is also supplied, the reuse flag takes precedence. Documents and new representatives use their dedicated APIs.

        Parameters
        ----------
        sender_id : str

        currency : UpdateSetupDataVirtualBankAccountsRequestCurrency

        sender_details : typing.Optional[UpdateVirtualAccountSetupDataSenderDetails]
            Previously absent business-sender details required by the requested account.

        ubo_details : typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataUboDetailsItem]]

        associate_details : typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataAssociateDetailsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VirtualAccountSetupEnvelope]
            Re-evaluated setup-request state. Recognized submitted fields that were not current blockers are identified in unacceptedFields.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request/data",
            method="PATCH",
            json={
                "senderDetails": convert_and_respect_annotation_metadata(
                    object_=sender_details, annotation=UpdateVirtualAccountSetupDataSenderDetails, direction="write"
                ),
                "uboDetails": convert_and_respect_annotation_metadata(
                    object_=ubo_details,
                    annotation=typing.Sequence[UpdateVirtualAccountSetupDataUboDetailsItem],
                    direction="write",
                ),
                "associateDetails": convert_and_respect_annotation_metadata(
                    object_=associate_details,
                    annotation=typing.Sequence[UpdateVirtualAccountSetupDataAssociateDetailsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self,
        sender_id: str,
        currency: GetVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SenderVirtualAccountsEnvelope]:
        """
        Returns the virtual bank accounts available to the sender for the requested currency. The response is an array and currently contains at most one account.

        Parameters
        ----------
        sender_id : str

        currency : GetVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SenderVirtualAccountsEnvelope]
            Sender virtual bank accounts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SenderVirtualAccountsEnvelope,
                    parse_obj_as(
                        type_=SenderVirtualAccountsEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawVirtualBankAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_setup_status(
        self,
        sender_id: str,
        currency: GetSetupStatusVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VirtualAccountSetupEnvelope]:
        """
        Returns the sender's current virtual bank account status for the currency. No request ID is required. This read can reconcile status but cannot start account setup. The endpoint follows the sender's current account configuration; if Mesta changes that configuration, a request associated with the previous configuration is no longer returned and the merchant should POST again for the current configuration.

        Parameters
        ----------
        sender_id : str

        currency : GetSetupStatusVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VirtualAccountSetupEnvelope]
            Current setup-request state.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def request_setup(
        self,
        sender_id: str,
        currency: RequestSetupVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VirtualAccountSetupEnvelope]:
        """
        Creates or reuses the current virtual bank account request for this sender and currency. It is evaluated immediately and may begin setup automatically when all requirements are satisfied. Follow returned blocker actions when more information or verification is needed.

        Parameters
        ----------
        sender_id : str

        currency : RequestSetupVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VirtualAccountSetupEnvelope]
            Current setup-request state.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_setup(
        self,
        sender_id: str,
        currency: CancelSetupVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VirtualAccountSetupEnvelope]:
        """
        Cancels the current request before account setup begins or after failure. Provisioning and completed requests cannot be cancelled. A later POST creates a fresh current request.

        Parameters
        ----------
        sender_id : str

        currency : CancelSetupVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VirtualAccountSetupEnvelope]
            Cancelled setup-request state.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_setup_data(
        self,
        sender_id: str,
        currency: UpdateSetupDataVirtualBankAccountsRequestCurrency,
        *,
        sender_details: typing.Optional[UpdateVirtualAccountSetupDataSenderDetails] = OMIT,
        ubo_details: typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataUboDetailsItem]] = OMIT,
        associate_details: typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataAssociateDetailsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VirtualAccountSetupEnvelope]:
        """
        Fills supported missing sender, UBO, or existing-representative values, then re-evaluates the current setup request. Fields that are not current blockers are skipped and identified in unacceptedFields; other submitted fields are still processed. Existing values cannot be overwritten. To reuse the registered address as the trading address, set senderDetails.tradingAddressSameAsRegistered to true. If a manual tradingAddress is also supplied, the reuse flag takes precedence. Documents and new representatives use their dedicated APIs.

        Parameters
        ----------
        sender_id : str

        currency : UpdateSetupDataVirtualBankAccountsRequestCurrency

        sender_details : typing.Optional[UpdateVirtualAccountSetupDataSenderDetails]
            Previously absent business-sender details required by the requested account.

        ubo_details : typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataUboDetailsItem]]

        associate_details : typing.Optional[typing.Sequence[UpdateVirtualAccountSetupDataAssociateDetailsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VirtualAccountSetupEnvelope]
            Re-evaluated setup-request state. Recognized submitted fields that were not current blockers are identified in unacceptedFields.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}/setup-request/data",
            method="PATCH",
            json={
                "senderDetails": convert_and_respect_annotation_metadata(
                    object_=sender_details, annotation=UpdateVirtualAccountSetupDataSenderDetails, direction="write"
                ),
                "uboDetails": convert_and_respect_annotation_metadata(
                    object_=ubo_details,
                    annotation=typing.Sequence[UpdateVirtualAccountSetupDataUboDetailsItem],
                    direction="write",
                ),
                "associateDetails": convert_and_respect_annotation_metadata(
                    object_=associate_details,
                    annotation=typing.Sequence[UpdateVirtualAccountSetupDataAssociateDetailsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualAccountSetupEnvelope,
                    parse_obj_as(
                        type_=VirtualAccountSetupEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self,
        sender_id: str,
        currency: GetVirtualBankAccountsRequestCurrency,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SenderVirtualAccountsEnvelope]:
        """
        Returns the virtual bank accounts available to the sender for the requested currency. The response is an array and currently contains at most one account.

        Parameters
        ----------
        sender_id : str

        currency : GetVirtualBankAccountsRequestCurrency

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SenderVirtualAccountsEnvelope]
            Sender virtual bank accounts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/{encode_path_param(sender_id)}/virtual-bank-accounts/{encode_path_param(currency)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SenderVirtualAccountsEnvelope,
                    parse_obj_as(
                        type_=SenderVirtualAccountsEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

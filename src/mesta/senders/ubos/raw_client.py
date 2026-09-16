
import datetime as dt
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
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.address import Address
from ...types.error_response import ErrorResponse
from .types.create_ubos_request_address import CreateUbosRequestAddress
from .types.create_ubos_request_identity import CreateUbosRequestIdentity
from .types.create_ubos_request_pep_questionnaire import CreateUbosRequestPepQuestionnaire
from .types.create_ubos_response import CreateUbosResponse
from .types.delete_ubos_response import DeleteUbosResponse
from .types.get_ubos_response import GetUbosResponse
from .types.get_verification_url_ubos_request_action import GetVerificationUrlUbosRequestAction
from .types.get_verification_url_ubos_response import GetVerificationUrlUbosResponse
from .types.update_ubos_request_identity import UpdateUbosRequestIdentity
from .types.update_ubos_request_pep_questionnaire import UpdateUbosRequestPepQuestionnaire
from .types.update_ubos_response import UpdateUbosResponse
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawUbosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        first_name: str,
        last_name: str,
        birth_date: dt.date,
        phone: str,
        email: str,
        ownership_percent: float,
        address: CreateUbosRequestAddress,
        sender_id: str,
        identity: CreateUbosRequestIdentity,
        pep_declaration: bool,
        nationality: typing.Optional[str] = OMIT,
        identification_number: typing.Optional[str] = OMIT,
        verification_report: typing.Optional[str] = OMIT,
        verification_report_file_name: typing.Optional[str] = OMIT,
        sof_document: typing.Optional[str] = OMIT,
        pep_questionnaire: typing.Optional[CreateUbosRequestPepQuestionnaire] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateUbosResponse]:
        """
        Creates a new UBO (Ultimate Beneficial Owner) for a specific sender. Note: Document requirements (documentFront, documentBack) vary by country. Please refer to the validation-rules endpoint with ownerType='business' and the specific country to determine exact documentation requirements. Multiple UBOs can be added by calling this endpoint multiple times. The total ownership percentage across all UBOs should not exceed 100%.

        Additional v2 details:
        * `pepDeclaration` is required.
        * `verificationReport` and `verificationReportFileName` are supported.
        * The total request payload size must be less than 10 MB.
        * `sofDocument` is required when any of the following is true:
          * UBO age is less than 25
          * UBO age is greater than 60
          * `pepDeclaration` is `true`
          * `address.country` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`
          * `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`
        * `pepQuestionnaire` is supported. It is required when `pepDeclaration` is `true`.
        * `pepQuestionnaire.declarationType` controls which section is required: `self` (for `SELF`) or `association` (for `IMMEDIATE_FAMILY` and `CLOSE_ASSOCIATE`).

        Parameters
        ----------
        first_name : str
            First name of the UBO.

        last_name : str
            Last name of the UBO.

        birth_date : dt.date
            Birthdate of the UBO in the format YYYY-MM-DD.

        phone : str
            Phone number of the UBO in international format (for example, +11234567890).

        email : str
            Email address of the UBO.

        ownership_percent : float
            Ownership percentage of the UBO in the company.

        address : CreateUbosRequestAddress
            UBO postal address.

        sender_id : str
            Unique identifier for the sender.

        identity : CreateUbosRequestIdentity
            Identity information for the UBO.

        pep_declaration : bool
            Whether the UBO is politically exposed. This field is required.

        nationality : typing.Optional[str]
            UBO nationality as an ISO 3166-1 alpha-2 country code. This is distinct from residence and identity-document country.

        identification_number : typing.Optional[str]
            Tax identification number for the UBO. Required for a non-US UBO when `usd_account` is requested.

        verification_report : typing.Optional[str]
            Optional base64 encoded verification report document.

        verification_report_file_name : typing.Optional[str]
            Optional file name for the verification report.

        sof_document : typing.Optional[str]
            Base64 encoded source-of-funds document. Required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`.

        pep_questionnaire : typing.Optional[CreateUbosRequestPepQuestionnaire]
            Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateUbosResponse]
            Ultimate Beneficial Owner created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/senders/ubo",
            method="POST",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "birthDate": birth_date,
                "phone": phone,
                "email": email,
                "ownershipPercent": ownership_percent,
                "nationality": nationality,
                "identificationNumber": identification_number,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CreateUbosRequestAddress, direction="write"
                ),
                "senderId": sender_id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=CreateUbosRequestIdentity, direction="write"
                ),
                "verificationReport": verification_report,
                "verificationReportFileName": verification_report_file_name,
                "pepDeclaration": pep_declaration,
                "sofDocument": sof_document,
                "pepQuestionnaire": convert_and_respect_annotation_metadata(
                    object_=pep_questionnaire,
                    annotation=typing.Optional[CreateUbosRequestPepQuestionnaire],
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
                    CreateUbosResponse,
                    parse_obj_as(
                        type_=CreateUbosResponse,  # type: ignore
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GetUbosResponse]:
        """
        Retrieves details of a specific Ultimate Beneficial Owner (UBO)

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUbosResponse]
            Ultimate Beneficial Owner details retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUbosResponse,
                    parse_obj_as(
                        type_=GetUbosResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteUbosResponse]:
        """
        Deletes an existing UBO (Ultimate Beneficial Owner)

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteUbosResponse]
            UBO deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteUbosResponse,
                    parse_obj_as(
                        type_=DeleteUbosResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    def update(
        self,
        id: str,
        *,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        nationality: typing.Optional[str] = OMIT,
        identification_number: typing.Optional[str] = OMIT,
        ownership_percent: typing.Optional[float] = OMIT,
        address: typing.Optional[Address] = OMIT,
        identity: typing.Optional[UpdateUbosRequestIdentity] = OMIT,
        verification_report: typing.Optional[str] = OMIT,
        verification_report_file_name: typing.Optional[str] = OMIT,
        pep_declaration: typing.Optional[bool] = OMIT,
        sof_document: typing.Optional[str] = OMIT,
        pep_questionnaire: typing.Optional[UpdateUbosRequestPepQuestionnaire] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateUbosResponse]:
        """
        Updates an existing Ultimate Beneficial Owner (UBO). In addition to the base UBO fields, this endpoint supports `pepDeclaration`, `verificationReport`, and `sofDocument`. `sofDocument` is required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`. `pepQuestionnaire` is supported. When `pepDeclaration` is `true`, include `pepQuestionnaire` with `declarationType` and the matching conditional section (`self` or `association`).

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        first_name : typing.Optional[str]
            First name of the UBO

        last_name : typing.Optional[str]
            Last name of the UBO

        birth_date : typing.Optional[dt.date]
            Birth date of the UBO

        email : typing.Optional[str]
            Email address of the UBO

        phone : typing.Optional[str]
            Phone number of the UBO in international format (e.g., +11234567890)

        nationality : typing.Optional[str]
            UBO nationality as an ISO 3166-1 alpha-2 country code. This is distinct from residence and identity-document country.

        identification_number : typing.Optional[str]
            Tax identification number for the UBO. Required for a non-US UBO when `usd_account` is requested.

        ownership_percent : typing.Optional[float]
            Percentage of the sender owned by this UBO.

        address : typing.Optional[Address]

        identity : typing.Optional[UpdateUbosRequestIdentity]

        verification_report : typing.Optional[str]
            Optional base64 encoded verification report document.

        verification_report_file_name : typing.Optional[str]
            Optional file name for the verification report.

        pep_declaration : typing.Optional[bool]
            Whether the UBO is politically exposed.

        sof_document : typing.Optional[str]
            Base64 encoded source-of-funds document. Required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`.

        pep_questionnaire : typing.Optional[UpdateUbosRequestPepQuestionnaire]
            Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateUbosResponse]
            Ultimate Beneficial Owner updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}",
            method="PATCH",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "birthDate": birth_date,
                "email": email,
                "phone": phone,
                "nationality": nationality,
                "identificationNumber": identification_number,
                "ownershipPercent": ownership_percent,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=Address, direction="write"
                ),
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=UpdateUbosRequestIdentity, direction="write"
                ),
                "verificationReport": verification_report,
                "verificationReportFileName": verification_report_file_name,
                "pepDeclaration": pep_declaration,
                "sofDocument": sof_document,
                "pepQuestionnaire": convert_and_respect_annotation_metadata(
                    object_=pep_questionnaire,
                    annotation=typing.Optional[UpdateUbosRequestPepQuestionnaire],
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
                    UpdateUbosResponse,
                    parse_obj_as(
                        type_=UpdateUbosResponse,  # type: ignore
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    def get_verification_url(
        self,
        id: str,
        *,
        action: typing.Optional[GetVerificationUrlUbosRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVerificationUrlUbosResponse]:
        """
        Fetches the latest selfie verification session for a UBO and, optionally, generates or regenerates a verification link.

        Action behavior:
        * no `action`: return the current verification-session state without creating a new link.
        * `GENERATE`: create the first verification link only when no previous selfie session exists.
        * `REGENERATE`: create a fresh verification link only when the latest session is `DECLINED` or `EXPIRED`.

        Response behavior:
        * `latestSession`: the most recent selfie verification session, or `null` if none exists.
        * `previousSessions`: older selfie verification sessions in reverse chronological order.

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        action : typing.Optional[GetVerificationUrlUbosRequestAction]
            Optional action for selfie-link creation. Omit it to fetch the current session state only. Use `GENERATE` to create the first link when no session exists. Use `REGENERATE` only when the latest session is `DECLINED` or `EXPIRED`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetVerificationUrlUbosResponse]
            UBO verification session fetched successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}/verification-url",
            method="GET",
            params={
                "action": action,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVerificationUrlUbosResponse,
                    parse_obj_as(
                        type_=GetVerificationUrlUbosResponse,  # type: ignore
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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


class AsyncRawUbosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        first_name: str,
        last_name: str,
        birth_date: dt.date,
        phone: str,
        email: str,
        ownership_percent: float,
        address: CreateUbosRequestAddress,
        sender_id: str,
        identity: CreateUbosRequestIdentity,
        pep_declaration: bool,
        nationality: typing.Optional[str] = OMIT,
        identification_number: typing.Optional[str] = OMIT,
        verification_report: typing.Optional[str] = OMIT,
        verification_report_file_name: typing.Optional[str] = OMIT,
        sof_document: typing.Optional[str] = OMIT,
        pep_questionnaire: typing.Optional[CreateUbosRequestPepQuestionnaire] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateUbosResponse]:
        """
        Creates a new UBO (Ultimate Beneficial Owner) for a specific sender. Note: Document requirements (documentFront, documentBack) vary by country. Please refer to the validation-rules endpoint with ownerType='business' and the specific country to determine exact documentation requirements. Multiple UBOs can be added by calling this endpoint multiple times. The total ownership percentage across all UBOs should not exceed 100%.

        Additional v2 details:
        * `pepDeclaration` is required.
        * `verificationReport` and `verificationReportFileName` are supported.
        * The total request payload size must be less than 10 MB.
        * `sofDocument` is required when any of the following is true:
          * UBO age is less than 25
          * UBO age is greater than 60
          * `pepDeclaration` is `true`
          * `address.country` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`
          * `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`
        * `pepQuestionnaire` is supported. It is required when `pepDeclaration` is `true`.
        * `pepQuestionnaire.declarationType` controls which section is required: `self` (for `SELF`) or `association` (for `IMMEDIATE_FAMILY` and `CLOSE_ASSOCIATE`).

        Parameters
        ----------
        first_name : str
            First name of the UBO.

        last_name : str
            Last name of the UBO.

        birth_date : dt.date
            Birthdate of the UBO in the format YYYY-MM-DD.

        phone : str
            Phone number of the UBO in international format (for example, +11234567890).

        email : str
            Email address of the UBO.

        ownership_percent : float
            Ownership percentage of the UBO in the company.

        address : CreateUbosRequestAddress
            UBO postal address.

        sender_id : str
            Unique identifier for the sender.

        identity : CreateUbosRequestIdentity
            Identity information for the UBO.

        pep_declaration : bool
            Whether the UBO is politically exposed. This field is required.

        nationality : typing.Optional[str]
            UBO nationality as an ISO 3166-1 alpha-2 country code. This is distinct from residence and identity-document country.

        identification_number : typing.Optional[str]
            Tax identification number for the UBO. Required for a non-US UBO when `usd_account` is requested.

        verification_report : typing.Optional[str]
            Optional base64 encoded verification report document.

        verification_report_file_name : typing.Optional[str]
            Optional file name for the verification report.

        sof_document : typing.Optional[str]
            Base64 encoded source-of-funds document. Required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`.

        pep_questionnaire : typing.Optional[CreateUbosRequestPepQuestionnaire]
            Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateUbosResponse]
            Ultimate Beneficial Owner created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/senders/ubo",
            method="POST",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "birthDate": birth_date,
                "phone": phone,
                "email": email,
                "ownershipPercent": ownership_percent,
                "nationality": nationality,
                "identificationNumber": identification_number,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=CreateUbosRequestAddress, direction="write"
                ),
                "senderId": sender_id,
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=CreateUbosRequestIdentity, direction="write"
                ),
                "verificationReport": verification_report,
                "verificationReportFileName": verification_report_file_name,
                "pepDeclaration": pep_declaration,
                "sofDocument": sof_document,
                "pepQuestionnaire": convert_and_respect_annotation_metadata(
                    object_=pep_questionnaire,
                    annotation=typing.Optional[CreateUbosRequestPepQuestionnaire],
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
                    CreateUbosResponse,
                    parse_obj_as(
                        type_=CreateUbosResponse,  # type: ignore
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUbosResponse]:
        """
        Retrieves details of a specific Ultimate Beneficial Owner (UBO)

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUbosResponse]
            Ultimate Beneficial Owner details retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUbosResponse,
                    parse_obj_as(
                        type_=GetUbosResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteUbosResponse]:
        """
        Deletes an existing UBO (Ultimate Beneficial Owner)

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteUbosResponse]
            UBO deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteUbosResponse,
                    parse_obj_as(
                        type_=DeleteUbosResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    async def update(
        self,
        id: str,
        *,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        birth_date: typing.Optional[dt.date] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        nationality: typing.Optional[str] = OMIT,
        identification_number: typing.Optional[str] = OMIT,
        ownership_percent: typing.Optional[float] = OMIT,
        address: typing.Optional[Address] = OMIT,
        identity: typing.Optional[UpdateUbosRequestIdentity] = OMIT,
        verification_report: typing.Optional[str] = OMIT,
        verification_report_file_name: typing.Optional[str] = OMIT,
        pep_declaration: typing.Optional[bool] = OMIT,
        sof_document: typing.Optional[str] = OMIT,
        pep_questionnaire: typing.Optional[UpdateUbosRequestPepQuestionnaire] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateUbosResponse]:
        """
        Updates an existing Ultimate Beneficial Owner (UBO). In addition to the base UBO fields, this endpoint supports `pepDeclaration`, `verificationReport`, and `sofDocument`. `sofDocument` is required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`. `pepQuestionnaire` is supported. When `pepDeclaration` is `true`, include `pepQuestionnaire` with `declarationType` and the matching conditional section (`self` or `association`).

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        first_name : typing.Optional[str]
            First name of the UBO

        last_name : typing.Optional[str]
            Last name of the UBO

        birth_date : typing.Optional[dt.date]
            Birth date of the UBO

        email : typing.Optional[str]
            Email address of the UBO

        phone : typing.Optional[str]
            Phone number of the UBO in international format (e.g., +11234567890)

        nationality : typing.Optional[str]
            UBO nationality as an ISO 3166-1 alpha-2 country code. This is distinct from residence and identity-document country.

        identification_number : typing.Optional[str]
            Tax identification number for the UBO. Required for a non-US UBO when `usd_account` is requested.

        ownership_percent : typing.Optional[float]
            Percentage of the sender owned by this UBO.

        address : typing.Optional[Address]

        identity : typing.Optional[UpdateUbosRequestIdentity]

        verification_report : typing.Optional[str]
            Optional base64 encoded verification report document.

        verification_report_file_name : typing.Optional[str]
            Optional file name for the verification report.

        pep_declaration : typing.Optional[bool]
            Whether the UBO is politically exposed.

        sof_document : typing.Optional[str]
            Base64 encoded source-of-funds document. Required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`.

        pep_questionnaire : typing.Optional[UpdateUbosRequestPepQuestionnaire]
            Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateUbosResponse]
            Ultimate Beneficial Owner updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}",
            method="PATCH",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "birthDate": birth_date,
                "email": email,
                "phone": phone,
                "nationality": nationality,
                "identificationNumber": identification_number,
                "ownershipPercent": ownership_percent,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=Address, direction="write"
                ),
                "identity": convert_and_respect_annotation_metadata(
                    object_=identity, annotation=UpdateUbosRequestIdentity, direction="write"
                ),
                "verificationReport": verification_report,
                "verificationReportFileName": verification_report_file_name,
                "pepDeclaration": pep_declaration,
                "sofDocument": sof_document,
                "pepQuestionnaire": convert_and_respect_annotation_metadata(
                    object_=pep_questionnaire,
                    annotation=typing.Optional[UpdateUbosRequestPepQuestionnaire],
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
                    UpdateUbosResponse,
                    parse_obj_as(
                        type_=UpdateUbosResponse,  # type: ignore
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

    async def get_verification_url(
        self,
        id: str,
        *,
        action: typing.Optional[GetVerificationUrlUbosRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetVerificationUrlUbosResponse]:
        """
        Fetches the latest selfie verification session for a UBO and, optionally, generates or regenerates a verification link.

        Action behavior:
        * no `action`: return the current verification-session state without creating a new link.
        * `GENERATE`: create the first verification link only when no previous selfie session exists.
        * `REGENERATE`: create a fresh verification link only when the latest session is `DECLINED` or `EXPIRED`.

        Response behavior:
        * `latestSession`: the most recent selfie verification session, or `null` if none exists.
        * `previousSessions`: older selfie verification sessions in reverse chronological order.

        Parameters
        ----------
        id : str
            Unique identifier of the UBO

        action : typing.Optional[GetVerificationUrlUbosRequestAction]
            Optional action for selfie-link creation. Omit it to fetch the current session state only. Use `GENERATE` to create the first link when no session exists. Use `REGENERATE` only when the latest session is `DECLINED` or `EXPIRED`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetVerificationUrlUbosResponse]
            UBO verification session fetched successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/senders/ubo/{encode_path_param(id)}/verification-url",
            method="GET",
            params={
                "action": action,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetVerificationUrlUbosResponse,
                    parse_obj_as(
                        type_=GetVerificationUrlUbosResponse,  # type: ignore
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
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

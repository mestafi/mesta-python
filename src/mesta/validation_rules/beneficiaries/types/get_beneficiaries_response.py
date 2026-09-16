
from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ....core.serialization import FieldMetadata
from .get_beneficiaries_response_data import GetBeneficiariesResponseData


class GetBeneficiariesResponse(UniversalBaseModel):
    data: typing.Optional[GetBeneficiariesResponseData] = None
    request_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requestId"),
        pydantic.Field(alias="requestId", description="Unique identifier for the API request"),
    ] = None
    """
    Unique identifier for the API request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetBeneficiariesResponse)

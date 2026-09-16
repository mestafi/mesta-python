
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.payment_method import PaymentMethod


class ListPaymentMethodsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[PaymentMethod]] = None
    total: typing.Optional[int] = None
    has_next: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasNext"),
        pydantic.Field(alias="hasNext", description="Whether there are more results available"),
    ] = None
    """
    Whether there are more results available
    """

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


import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_transactions_response_data_item import ListTransactionsResponseDataItem


class ListTransactionsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ListTransactionsResponseDataItem]] = pydantic.Field(default=None)
    """
    List of merchant transactions
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of transactions matching the query
    """

    has_next: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasNext"),
        pydantic.Field(
            alias="hasNext", description="Indicates if there are more transactions available for pagination"
        ),
    ] = None
    """
    Indicates if there are more transactions available for pagination
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

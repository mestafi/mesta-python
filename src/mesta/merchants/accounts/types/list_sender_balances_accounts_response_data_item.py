
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class ListSenderBalancesAccountsResponseDataItem(UniversalBaseModel):
    sender_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="senderId"),
        pydantic.Field(alias="senderId", description="Unique identifier for the sender"),
    ]
    """
    Unique identifier for the sender
    """

    currency: str = pydantic.Field()
    """
    Currency code for the balance
    """

    balance: str = pydantic.Field()
    """
    Current balance as a decimal string
    """

    sender_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="senderName"), pydantic.Field(alias="senderName", description="Name of the sender")
    ]
    """
    Name of the sender
    """

    sender_email: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="senderEmail"),
        pydantic.Field(alias="senderEmail", description="Email address of the sender"),
    ]
    """
    Email address of the sender
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

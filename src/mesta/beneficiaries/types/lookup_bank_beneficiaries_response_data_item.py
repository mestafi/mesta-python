
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class LookupBankBeneficiariesResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the bank
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the bank
    """

    supported_account_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="supportedAccountTypes"),
        pydantic.Field(alias="supportedAccountTypes", description="List of account types supported by this bank"),
    ] = None
    """
    List of account types supported by this bank
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

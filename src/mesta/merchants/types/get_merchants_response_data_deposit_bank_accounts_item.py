
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetMerchantsResponseDataDepositBankAccountsItem(UniversalBaseModel):
    is_test_data: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isTestData"),
        pydantic.Field(
            alias="isTestData",
            description="Sandbox only, and always `true`: these deposit instructions are sample data. The holder, bank and account details receive nothing, so never send a real transfer to them; add funds with a simulated deposit (`POST /v1/simulate/deposits`) instead. Absent in production.",
        ),
    ] = None
    """
    Sandbox only, and always `true`: these deposit instructions are sample data. The holder, bank and account details receive nothing, so never send a real transfer to them; add funds with a simulated deposit (`POST /v1/simulate/deposits`) instead. Absent in production.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

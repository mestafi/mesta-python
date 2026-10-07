
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxMachineCreatedClaim(UniversalBaseModel):
    """
    Present instead of `claimUrl` when the request carried `claimEmail`: the claim link went to that address.
    """

    sent_to: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sentTo"),
        pydantic.Field(
            alias="sentTo",
            description="The masked address the claim link was emailed to, for example `d***@example.com`.",
        ),
    ]
    """
    The masked address the claim link was emailed to, for example `d***@example.com`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

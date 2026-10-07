
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sandbox_production_request_volume_band import SandboxProductionRequestVolumeBand


class SandboxProductionRequest(UniversalBaseModel):
    """
    The Go live form's answers, sent to Mesta's sales team with the request and stored with the sandbox until it is purged. A new request replaces them.
    """

    legal_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="legalName"),
        pydantic.Field(alias="legalName", description="Your business's legal name."),
    ]
    """
    Your business's legal name.
    """

    country: str = pydantic.Field()
    """
    Your business's country, as an ISO 3166-1 alpha-2 code.
    """

    use_case: typing_extensions.Annotated[
        str, FieldMetadata(alias="useCase"), pydantic.Field(alias="useCase", description="What you will use Mesta for.")
    ]
    """
    What you will use Mesta for.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    Your business's website, an https URL.
    """

    volume_band: typing_extensions.Annotated[
        typing.Optional[SandboxProductionRequestVolumeBand],
        FieldMetadata(alias="volumeBand"),
        pydantic.Field(alias="volumeBand", description="Your expected monthly volume in USD."),
    ] = None
    """
    Your expected monthly volume in USD.
    """

    target_month: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="targetMonth"),
        pydantic.Field(alias="targetMonth", description="The month you aim to go live, as YYYY-MM."),
    ] = None
    """
    The month you aim to go live, as YYYY-MM.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional note to Mesta.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

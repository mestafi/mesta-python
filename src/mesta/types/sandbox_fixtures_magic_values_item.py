
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxFixturesMagicValuesItem(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Stable key, for example `quote_source_amount_cents_99`.
    """

    value: str = pydantic.Field()
    """
    What to send, for example `.99` or `SANDBOX DECLINE`.
    """

    applies_to: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="appliesTo"),
        pydantic.Field(
            alias="appliesTo",
            description='Where the value goes, for example "the cents of `sourceAmount` in `POST /v1/quotes`".',
        ),
    ]
    """
    Where the value goes, for example "the cents of `sourceAmount` in `POST /v1/quotes`".
    """

    outcome: typing.List[str] = pydantic.Field()
    """
    The events it produces, in order when one follows another (for example `["order:success", "order:returned"]`). Where the effect depends on the object, the description says which event applies to a person, a business or a beneficiary.
    """

    description: str = pydantic.Field()
    """
    One sentence saying what the value does.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

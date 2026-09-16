
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .virtual_account_setup_action_method import VirtualAccountSetupActionMethod


class VirtualAccountSetupAction(UniversalBaseModel):
    """
    Next API action that can resolve a blocker.
    """

    method: VirtualAccountSetupActionMethod
    path: str = pydantic.Field()
    """
    API path to call. IDs are populated for the affected sender or subject.
    """

    body_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="bodyFields"),
        pydantic.Field(
            alias="bodyFields",
            description="Top-level request-body fields accepted for this action. Nested object and array shapes are defined by the action endpoint's request schema.",
        ),
    ] = None
    """
    Top-level request-body fields accepted for this action. Nested object and array shapes are defined by the action endpoint's request schema.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

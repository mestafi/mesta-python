
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .verify_sender_requirements_blocker import VerifySenderRequirementsBlocker
from .verify_sender_requirements_missing_error_error_code import VerifySenderRequirementsMissingErrorErrorCode


class VerifySenderRequirementsMissingErrorError(UniversalBaseModel):
    """
    Standard Mesta error envelope. Property names are uppercase.
    """

    code: typing_extensions.Annotated[
        VerifySenderRequirementsMissingErrorErrorCode, FieldMetadata(alias="CODE"), pydantic.Field(alias="CODE")
    ]
    message: typing_extensions.Annotated[str, FieldMetadata(alias="MESSAGE"), pydantic.Field(alias="MESSAGE")]
    details: typing_extensions.Annotated[
        typing.List[VerifySenderRequirementsBlocker],
        FieldMetadata(alias="DETAILS"),
        pydantic.Field(
            alias="DETAILS",
            description="Actionable verification blockers. These have the same public semantics as setup-request blockers.",
        ),
    ]
    """
    Actionable verification blockers. These have the same public semantics as setup-request blockers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

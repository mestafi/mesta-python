
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetBeneficiariesResponseDataRulesRequiredDocumentsItem(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    Type identifier for the required document
    """

    description: str = pydantic.Field()
    """
    Human-readable description of the required document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

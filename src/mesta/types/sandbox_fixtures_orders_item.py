
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_fixtures_orders_item_status import SandboxFixturesOrdersItemStatus


class SandboxFixturesOrdersItem(UniversalBaseModel):
    id: str
    status: SandboxFixturesOrdersItemStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

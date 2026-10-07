
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SandboxChallengeSolution(UniversalBaseModel):
    challenge: str = pydantic.Field()
    """
    Lowercase hex SHA-256 digest to match.
    """

    salt: str = pydantic.Field()
    """
    Sixteen random bytes as hex, a period, and the expiry as Unix milliseconds. The salt is opaque to solvers; hash it unchanged.
    """

    maxnumber: int = pydantic.Field()
    """
    Exclusive upper bound of the hidden number. Expected work is maxnumber / 2 hashes.
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(
            alias="expiresAt", description="Repeats the timestamp inside `salt`. A challenge is valid for 300 seconds."
        ),
    ]
    """
    Repeats the timestamp inside `salt`. A challenge is valid for 300 seconds.
    """

    signature: str = pydantic.Field()
    """
    Mesta's HMAC over challenge, salt and maxnumber. Return it unchanged.
    """

    number: int = pydantic.Field()
    """
    The matching number, less than maxnumber.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

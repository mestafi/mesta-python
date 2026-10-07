
import typing

SandboxSessionStatus = typing.Union[
    typing.Literal["unclaimed", "claimed", "resetting", "expired", "failed", "deleted", "killed"], typing.Any
]


import typing

SandboxSeedErrorCode = typing.Union[
    typing.Literal[
        "SEED_STEP_TIMEOUT", "PORTAL_UNAVAILABLE", "CONDUCTOR_UNAVAILABLE", "INTERNAL_ROUTE_FAILED", "SEED_FAILED"
    ],
    typing.Any,
]

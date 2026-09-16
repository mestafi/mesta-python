
import typing

VirtualAccountSetupStatus = typing.Union[
    typing.Literal[
        "waiting_for_data",
        "waiting_for_verification",
        "waiting_for_activation",
        "ready",
        "provisioning",
        "completed",
        "failed",
        "cancelled",
    ],
    typing.Any,
]

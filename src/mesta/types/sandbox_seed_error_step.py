
import typing

SandboxSeedErrorStep = typing.Union[
    typing.Literal[
        "merchant",
        "keys",
        "terms",
        "merchant_setup",
        "webhook",
        "wallets",
        "senders",
        "deposits",
        "beneficiaries",
        "orders",
        "fixtures",
    ],
    typing.Any,
]

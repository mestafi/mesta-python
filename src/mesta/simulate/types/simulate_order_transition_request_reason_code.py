
import typing

SimulateOrderTransitionRequestReasonCode = typing.Union[
    typing.Literal[
        "requested_by_sender",
        "duplicate_order",
        "quote_expired",
        "compliance_declined",
        "beneficiary_unverified",
        "invalid_payment_details",
    ],
    typing.Any,
]

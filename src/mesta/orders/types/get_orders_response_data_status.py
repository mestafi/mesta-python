
import typing

GetOrdersResponseDataStatus = typing.Union[
    typing.Literal[
        "created",
        "awaiting_beneficiary_verification",
        "awaiting_funds",
        "awaiting_funds_timeout",
        "need_review",
        "funds_received",
        "in_progress",
        "sent_to_beneficiary",
        "success",
        "failed",
        "cancelled",
        "refund_in_progress",
        "refunded",
        "payment_submitted",
        "rejected",
        "returned",
    ],
    typing.Any,
]

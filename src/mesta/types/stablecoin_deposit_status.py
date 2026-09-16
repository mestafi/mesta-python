
import typing

StablecoinDepositStatus = typing.Union[
    typing.Literal["created", "compliance_review_required", "compliance_review_succeeded", "compliance_review_failed"],
    typing.Any,
]

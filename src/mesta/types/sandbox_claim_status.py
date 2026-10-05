
import typing

from .sandbox_claim_status_status import SandboxClaimStatusStatus
from .sandbox_claim_status_zero import SandboxClaimStatusZero

SandboxClaimStatus = typing.Union[SandboxClaimStatusZero, SandboxClaimStatusStatus]

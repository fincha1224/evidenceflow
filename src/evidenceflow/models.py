"""Core data models."""

from dataclasses import dataclass, field

from .status import VerificationStatus


@dataclass(frozen=True)
class Evidence:
    source: str
    confidence: float
    independent: bool = True

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True)
class Claim:
    text: str
    evidence: tuple[Evidence, ...] = ()


@dataclass(frozen=True)
class Verdict:
    status: VerificationStatus
    reason: str
    audit_trail: tuple[str, ...] = field(default_factory=tuple)
    model_status: VerificationStatus | None = None

"""Transparent policy checks for proposed verdicts."""

from dataclasses import dataclass

from .models import Claim, Verdict
from .status import VerificationStatus


@dataclass(frozen=True)
class VerificationPolicy:
    min_confidence: float = 0.75
    min_independent_sources: int = 2

    def apply(self, claim: Claim, proposed: Verdict) -> Verdict:
        """Apply policy rules without ever upgrading model status."""

        status = proposed.status
        trail = list(proposed.audit_trail)
        applied_reasons: list[str] = []

        def cap_status(current: VerificationStatus, maximum: VerificationStatus) -> VerificationStatus:
            """Return the weaker of current status and the allowed maximum."""
            return current if current.rank() <= maximum.rank() else maximum

        # Policy rules only cap status; they never raise it.
        if not claim.evidence:
            status = cap_status(status, VerificationStatus.UNCONFIRMED)
            reason = (
                "No supporting evidence was provided, so the status "
                "cannot exceed UNCONFIRMED."
            )
            trail.append(reason)
            applied_reasons.append(reason)

        if any(item.confidence < self.min_confidence for item in claim.evidence):
            status = cap_status(status, VerificationStatus.LIKELY)
            reason = (
                f"At least one evidence item is below the minimum confidence of "
                f"{self.min_confidence:.2f}, so the status cannot exceed LIKELY."
            )
            trail.append(reason)
            applied_reasons.append(reason)

        independent_sources = {
            item.source for item in claim.evidence if item.independent
        }

        if len(independent_sources) < self.min_independent_sources:
            status = cap_status(status, VerificationStatus.LIKELY)
            reason = (
                f"Only {len(independent_sources)} distinct independent source(s) were found; "
                f"{self.min_independent_sources} are required for VERIFIED."
            )
            trail.append(reason)
            applied_reasons.append(reason)

        final_reason = applied_reasons[-1] if applied_reasons else "Policy checks passed."

        return Verdict(
            status=status,
            reason=final_reason,
            audit_trail=tuple(trail),
            model_status=proposed.status,
        )

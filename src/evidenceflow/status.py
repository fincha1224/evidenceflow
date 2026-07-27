"""Ordered verification states."""

from enum import Enum


class VerificationStatus(Enum):
    UNCONFIRMED = 1
    LIKELY = 2
    VERIFIED = 3

    def rank(self) -> int:
        """Return the status strength as an integer."""
        return self.value

"""Tests for EvidenceFlow policy behavior."""

import unittest

from evidenceflow import Claim, Evidence, Verdict, VerificationPolicy, VerificationStatus


class VerificationPolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = VerificationPolicy(min_confidence=0.75, min_independent_sources=2)

    def test_no_evidence_caps_at_unconfirmed(self) -> None:
        claim = Claim("A claim with no evidence")
        proposed = Verdict(VerificationStatus.VERIFIED, "Model proposal")
        result = self.policy.apply(claim, proposed)
        self.assertEqual(result.status, VerificationStatus.UNCONFIRMED)
        self.assertEqual(result.model_status, VerificationStatus.VERIFIED)

    def test_low_confidence_caps_at_likely(self) -> None:
        claim = Claim("A claim with one weak source", (
            Evidence("source-a", 0.90, True),
            Evidence("source-b", 0.60, True),
        ))
        proposed = Verdict(VerificationStatus.VERIFIED, "Model proposal")
        result = self.policy.apply(claim, proposed)
        self.assertEqual(result.status, VerificationStatus.LIKELY)

    def test_too_few_independent_sources_caps_at_likely(self) -> None:
        claim = Claim("A claim repeated by one source", (
            Evidence("source-a", 0.90, True),
            Evidence("source-a", 0.95, True),
        ))
        proposed = Verdict(VerificationStatus.VERIFIED, "Model proposal")
        result = self.policy.apply(claim, proposed)
        self.assertEqual(result.status, VerificationStatus.LIKELY)

    def test_policy_never_upgrades(self) -> None:
        claim = Claim("A well-supported claim", (
            Evidence("source-a", 0.95, True),
            Evidence("source-b", 0.92, True),
        ))
        proposed = Verdict(VerificationStatus.UNCONFIRMED, "Model proposal")
        result = self.policy.apply(claim, proposed)
        self.assertEqual(result.status, VerificationStatus.UNCONFIRMED)

    def test_verified_survives_when_all_checks_pass(self) -> None:
        claim = Claim("A well-supported claim", (
            Evidence("source-a", 0.95, True),
            Evidence("source-b", 0.92, True),
        ))
        proposed = Verdict(VerificationStatus.VERIFIED, "Model proposal")
        result = self.policy.apply(claim, proposed)
        self.assertEqual(result.status, VerificationStatus.VERIFIED)
        self.assertEqual(result.reason, "Policy checks passed.")


if __name__ == "__main__":
    unittest.main()

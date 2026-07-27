"""Small runnable example."""

from evidenceflow import Claim, Evidence, Verdict, VerificationPolicy, VerificationStatus

claim = Claim(
    "The organization launched the program in 2026.",
    (
        Evidence("official-site", 0.96, True),
        Evidence("independent-report", 0.88, True),
    ),
)

proposed = Verdict(
    status=VerificationStatus.VERIFIED,
    reason="Model proposed VERIFIED.",
)

result = VerificationPolicy().apply(claim, proposed)

print("Final status:", result.status.name)
print("Model status:", result.model_status.name)
print("Reason:", result.reason)
print("Audit trail:")
for item in result.audit_trail:
    print("-", item)

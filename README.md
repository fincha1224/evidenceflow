# EvidenceFlow v2

A compact research prototype for applying verification policy to AI-proposed claim verdicts.

## Research question

How should AI-generated evidence influence high-impact decisions?

The policy is intentionally conservative: it may lower a proposed status, but it never raises one.

# EvidenceFlow

EvidenceFlow is a compact research prototype exploring one practical question:

> **How should AI-generated evidence be evaluated before it influences decisions that affect people?**

Modern AI systems produce probabilistic outputs rather than established facts. In many real-world settings, those outputs become part of larger decision-making workflows that require transparency, accountability, and human oversight.

EvidenceFlow explores a simple policy layer that evaluates AI-generated evidence before a recommendation is accepted. Rather than treating model outputs as final decisions, the project treats them as one source of evidence alongside confidence thresholds, independent evidence sources, and explicit policy rules.

The prototype intentionally remains small so every rule can be inspected, discussed, and challenged.

## Research Motivation

While building production AI systems for multilingual communication, workflow automation, and document verification, I became increasingly interested in a broader engineering question:

> **When should an AI-generated answer be trusted enough to influence a decision?**

EvidenceFlow is my first research prototype exploring that question through transparent policy evaluation instead of increasingly complex models.

## Run tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```

## Design

- `status.py` defines ordered verification states.
- `models.py` defines evidence, claims, and verdicts.
- `policy.py` applies transparent capping rules.
- tests verify no-evidence, low-confidence, source-diversity, and never-upgrade behavior.

## Architecture

```
                 AI Model
                     │
                     ▼
            Proposed Verdict
                     │
                     ▼
          Verification Policy
        ┌───────────────────────┐
        │ Confidence Thresholds │
        │ Evidence Availability │
        │ Source Diversity      │
        │ Policy Constraints    │
        └───────────────────────┘
                     │
                     ▼
              Final Verdict

```

The verification policy can lower the confidence of a proposed verdict, but it never upgrades it. This conservative design preserves the distinction between what the model proposed and what the policy permits.

## Limitations

EvidenceFlow is a research prototype designed to explore transparent evaluation of AI-generated evidence.

The current implementation intentionally uses:

- synthetic evidence
- manually specified policy thresholds
- deterministic decision rules
- simplified evaluation logic

The project does not perform real-world identity verification, factual verification, biometric analysis, or production risk assessment. Its purpose is to investigate transparent policy evaluation rather than production deployment.
All examples are synthetic. This is not a production verification system.

## Future Work

This prototype intentionally keeps the policy simple so every decision rule is transparent and easy to inspect.

Future directions include:

- calibrated uncertainty estimation
- evidence weighting instead of fixed thresholds
- provenance and evidence lineage
- conflicting evidence resolution
- human feedback integration
- policy learning from historical decisions
- fairness and consistency evaluation
- retrieval-augmented evidence verification

The long-term objective is to explore practical engineering approaches for trustworthy AI-assisted decision systems rather than increasingly complex prediction models.

## Design Principles

1. AI outputs should be treated as evidence, not unquestionable facts.
2. Policy decisions should remain transparent and explainable.
3. Human review is a valid outcome rather than a system failure.
4. Conservative policy should reduce confidence when evidence is insufficient, but never manufacture certainty.
5. Every recommendation should be auditable.

## About the Author

EvidenceFlow was developed as part of an ongoing exploration into trustworthy AI systems and transparent decision support.

My background spans graduate research in cybersecurity, enterprise security engineering, and the design of production AI systems for multilingual communication, workflow automation, and document verification. Those experiences motivated a broader research question: how should AI-generated evidence be evaluated before it influences decisions that matter?

This project represents an early step toward answering that question through practical engineering rather than increasingly complex models.

---

> *Building production AI systems changed the kinds of engineering problems I cared about. The challenge was no longer getting models to generate answers—it was deciding when those answers were reliable enough to influence decisions that mattered.*

## References

EvidenceFlow was influenced by ideas from trustworthy AI, uncertainty estimation, AI safety, and evidence-based decision systems.

1. Amodei, D., et al. (2016). *Concrete Problems in AI Safety.*
   https://arxiv.org/abs/1606.06565

2. Anthropic. (2023). *Constitutional AI: Harmlessness from AI Feedback.*
   https://arxiv.org/abs/2212.08073

3. NIST. (2023). *AI Risk Management Framework (AI RMF 1.0).*
   https://www.nist.gov/itl/ai-risk-management-framework

4. ISO/IEC 23894:2023.
   *Artificial Intelligence — Risk Management.*

5. Pearl, J. (2018).
   *The Book of Why.*
   Basic Books.
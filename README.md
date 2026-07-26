# EvidenceFlow v2

A compact research prototype for applying verification policy to AI-proposed claim verdicts.

## Research question

How should AI-generated evidence influence high-impact decisions?

The policy is intentionally conservative: it may lower a proposed status, but it never raises one.

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

All examples are synthetic. This is not a production verification system.

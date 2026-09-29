# Physics — Root Coverage Audit

**Audit date:** 2026-09-29  
**Canonical root:** `physics/`

The detailed Physics coverage/depth/quality audit already exists at:

- [`13_connections/02_coverage_audit.md`](./13_connections/02_coverage_audit.md)

This root file is the canonical governance entrypoint expected by repository-level tooling. Do not duplicate the full domain audit here.

## Root contract

Physics is organized by conceptual dependency and should keep the durable chain:

```text
phenomenon
→ measurable quantity
→ model
→ mathematics/derivation
→ assumptions
→ domain of validity
→ limiting cases/failure
→ evidence/experiment
→ knowledge connection
```

The domain owns physical laws, models, measurement and selected advanced bridges. Engineering design choices belong to the relevant engineering domain, especially [`../electrical_engineering/`](../electrical_engineering/README.md).

## Review rule

For substantive Physics changes, update the detailed audit when coverage/depth status changes. This root file should remain a stable pointer unless canonical ownership or audit location changes.
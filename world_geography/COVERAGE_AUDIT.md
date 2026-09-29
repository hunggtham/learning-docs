# World Geography — Root Coverage Audit

**Audit date:** 2026-09-29  
**Canonical root:** `world_geography/`

The detailed geography coverage audit already exists at:

- [`CORE_COVERAGE_AUDIT.md`](./CORE_COVERAGE_AUDIT.md)

This root file is the stable governance entrypoint expected by repository tooling. Do not duplicate the detailed audit here.

## Root contract

The domain should preserve its central model:

```text
pattern
+ process
+ network/flow
+ scale
+ evidence
```

Regional/country material should explain causal structure rather than become an encyclopedia of facts:

```text
physical constraints/resources
→ settlement
→ production/economy
→ transport/network
→ cities/trade
→ institutions/history interaction
→ hazards/transformation
```

Geography must not be written as geographic determinism. History, institutions and technology can alter or reverse spatial constraints.

## Review rule

Update [`CORE_COVERAGE_AUDIT.md`](./CORE_COVERAGE_AUDIT.md) when core coverage status changes. Keep this root file only as the canonical pointer unless the detailed audit location changes.
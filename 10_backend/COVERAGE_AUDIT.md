# Backend — Coverage Audit

**Audit date:** 2026-09-29  
**Canonical root:** `10_backend/`  
**Entrypoint:** [`README.md`](./README.md)

## 1. Canonical ownership

`10_backend/` owns application-level backend engineering: request handling, API contracts, identity/session, persistence usage, cache behavior, asynchronous work, failure handling, testing, observability, module/service boundaries and language/framework implementation tracks.

The canonical conceptual owner is [`backend_core/`](./backend_core/README.md). Java, Spring and Python are implementation tracks. A framework-specific chapter should explain how the framework realizes a backend invariant; it should not redefine the invariant differently from `backend_core/`.

Deeper owners outside this domain remain:

- database internals → [`../computer_science/05_data_databases/`](../computer_science/05_data_databases/README.md);
- networks/distributed systems → [`../computer_science/06_networks_distributed_systems/`](../computer_science/06_networks_distributed_systems/README.md);
- security/reliability foundations → [`../computer_science/07_security_reliability/`](../computer_science/07_security_reliability/README.md);
- software engineering foundations → [`../computer_science/09_software_engineering/`](../computer_science/09_software_engineering/README.md);
- host/runtime operations → [`../linux/`](../linux/README.md);
- deployment/platform/SRE → [`../devops_platform_engineering/`](../devops_platform_engineering/README.md).

## 2. Coverage currently strong

### Backend core

The root learning path already covers the important end-to-end sequence:

```text
request lifecycle
→ HTTP/API semantics
→ identity/session
→ persistence/transaction
→ cache/invalidation
→ async jobs/messaging
→ timeout/retry/idempotency
→ testing/contracts
→ observability/debugging
→ module/service boundaries
→ production case studies
```

This is a good canonical spine because it follows state and side effects instead of framework APIs.

`backend_core/` already has its own detailed coverage audit and explicitly separates contract, mechanism, failure mode and evidence. Root governance should therefore avoid duplicating that audit and instead check coherence across implementation tracks.

### Java / Spring / Python separation

The current root structure correctly distinguishes:

- Java language/runtime engineering;
- Spring as one Java backend implementation ecosystem;
- Python language/runtime/backend engineering;
- framework-independent backend core.

This boundary prevents the common structural error `Spring = backend` or `language syntax = backend architecture`.

### Production-oriented reasoning

The documented advanced loops are appropriate:

- correctness;
- latency;
- durability;
- safe change;
- scale/capacity.

These axes are more durable than product/version-specific APIs and should remain the review lens for future additions.

## 3. Invariants for future changes

A backend chapter should answer, where relevant:

1. What contract is exposed?
2. What state changes?
3. What invariant must survive failure?
4. Where is the durable boundary?
5. What can time out independently?
6. What can be retried or replayed?
7. Can retry duplicate a side effect?
8. What telemetry distinguishes competing failure hypotheses?
9. How is compatibility preserved during rollout or migration?
10. Which lower-level domain owns the underlying mechanism?

Do not accept a chapter whose explanation is only “use annotation/API X”.

## 4. Important boundaries to preserve

### ORM is not database internals

Backend may explain transaction usage, isolation consequences, N+1 behavior, connection pools and migration contracts. WAL, B-tree internals, MVCC implementation or distributed consensus belong to Computer Science unless needed only as a short prerequisite bridge.

### Messaging is not distributed-systems duplication

Backend owns application semantics such as idempotency, consumer side effects, poison messages, retry policy and outbox usage. Broker consensus, partition protocol and distributed algorithm internals remain external owners.

### Observability is evidence, not logging syntax

Framework logging configuration may appear as an implementation example, but the canonical question is what evidence identifies a request, operation, dependency, durable transition or failed side effect.

### Service boundaries are not a microservices checklist

A new service boundary needs an explicit reason: ownership, scaling, failure isolation, deployment independence, compliance or organizational boundary. “Microservices are more scalable” is not sufficient.

## 5. Gaps / next depth

### P1 — Cross-track contract matrix

Add a small matrix or route showing how the same invariant is implemented in Java/Spring/Python:

```text
backend invariant
→ Java/runtime consequence
→ Spring mechanism
→ Python/runtime/framework consequence
→ test/evidence
```

The purpose is comparison, not duplicated tutorials.

### P1 — Data migration and mixed-version application behavior

Expand root-level coverage of:

- expand/contract migration;
- backward/forward compatibility;
- dual-read/dual-write transition risks;
- old/new application versions running simultaneously;
- rollback after schema or event-contract change.

### P1 — Dependency and capacity budgets

Strengthen the chain:

```text
request SLO
→ timeout budget
→ connection/thread/event-loop pool
→ downstream concurrency
→ queue depth/age
→ backpressure
→ overload behavior
```

This should link to Linux and DevOps rather than reproduce their internals.

### P2 — Authentication/authorization evidence path

Connect identity/session chapters more explicitly to effective authority, audit evidence and credential propagation across async jobs/services. Reuse the Computer Science security connection route instead of duplicating threat-model theory.

### P2 — Recovery semantics catalog

Build a reusable distinction among:

- retry;
- replay;
- reconciliation;
- compensation;
- restore;
- rollback.

A production case should say which one is being used and why.

### P2 — External integration contracts

Add stronger treatment of third-party APIs/webhooks/payment-like side effects:

- callback authenticity;
- duplicate delivery;
- eventual status reconciliation;
- provider timeout vs business outcome;
- idempotency keys;
- rate limits and circuit breaking;
- evidence retained for disputes/recovery.

## 6. Review protocol

When a backend PR adds or rewrites substantial content, review in this order:

```text
canonical owner
→ contract/invariant
→ state and durable boundary
→ failure semantics
→ retry/recovery semantics
→ telemetry/evidence
→ compatibility during change
→ framework/language realization
→ internal links
```

If the explanation remains correct after replacing Spring/FastAPI/database/vendor names with generic roles, the conceptual layer is probably in the correct owner. If the explanation collapses when the product name is removed, it is probably implementation-specific and should stay in the relevant track.

## 7. Current assessment

**Root structure: strong.**  
**Backend core conceptual coverage: strong.**  
**Implementation-track separation: strong.**  
**Cross-track comparison: partial.**  
**Migration/mixed-version reasoning: needs more depth.**  
**Capacity/dependency-budget integration: needs more depth.**  
**Recovery-semantics vocabulary: should be standardized.**

The next improvements should deepen cross-track reasoning and production change/failure semantics rather than add another framework tutorial.
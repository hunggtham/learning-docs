# Fault tolerance, observability và reliability

Reliable system (신뢰성 높은 시스템) không phải system không bao giờ fail. Components inevitably fail; reliability engineering designs detection, containment, recovery and capacity so user-visible service meets defined objectives.

## Fault, error và failure

Dependability literature often distinguishes fault = underlying cause, error = incorrect internal state, failure = externally visible service deviation. A bit flip fault may corrupt state; checksum detects error before user-visible failure.

Terminology varies, but distinction encourages defense before external impact.

## Redundancy

Replication, extra instances, RAID/erasure coding và multi-zone deployment add redundancy. Redundancy helps only if failures sufficiently independent. Two replicas on same power rack are not protection from rack outage.

Correlated failure and shared dependencies are common hidden single points.

## Retry

Retry turns transient failure into success but adds load. Exponential backoff + jitter prevents synchronized retry storms. Retry budget limits amplification.

Only retry operations whose semantics are safe or made idempotent. Timeout + retry without idempotency can duplicate payment/order.

## Timeout

Without timeout, waiting on remote dependency can consume thread/connection forever. Timeout too short causes false failure/retry; too long delays recovery and holds resources. Timeout should reflect latency SLO and end-to-end deadline, not arbitrary constants copied everywhere.

Deadline propagation gives downstream remaining budget rather than each layer resetting full timeout.

## Circuit breaker

When dependency failing, circuit breaker temporarily reject/fallback instead of sending all requests, reducing wasted work and allowing recovery. But it is stateful and can create synchronized reopen/load spikes; half-open probing helps.

Load shedding rejects low-priority/excess work before total collapse. Queue limits are reliability tools.

## Bulkhead

Separate pools/quotas isolate failure domain: one slow tenant/dependency should not consume all threads/connections. Ship bulkheads inspired name. Resource partitioning trades utilization efficiency for fault isolation.

## Observability

Observability (옵저버빌리티 / khả năng quan sát) asks how well internal state can be inferred from outputs/telemetry. Logs, metrics and traces are tools, not observability definition.

Golden signals often include latency, traffic, errors, saturation. RED (Rate, Errors, Duration) useful for services; USE (Utilization, Saturation, Errors) for resources.

## SLI, SLO, SLA

SLI is measured indicator (e.g. successful requests under 300 ms). SLO is target (99.9% over window). SLA is external/business agreement with consequences, not synonym of SLO.

Error budget = allowed unreliability under SLO, enabling trade-off between feature velocity and reliability work.

## Availability math intuition

If independent components are in series and all required, availability multiplies. Two 99.9% required independent services give ~99.8001% combined, not 99.9. Parallel redundant components can improve availability if failover works and failures independent.

Reliability architecture therefore considers dependency graph, not component score alone.

## Graceful degradation

Under failure, system may serve stale cache, disable recommendations, reduce quality or read-only mode rather than total outage. Degradation must preserve critical correctness/security; serving stale authorization policy may be unsafe.

## Chaos/fault injection

Testing failure modes deliberately verifies assumptions about timeouts, failover and recovery. Injected faults should have blast-radius controls and hypotheses. Chaos without observability is just causing incidents.

## Mental Model

> Reliability = **assume failure, bound blast radius, detect quickly, recover predictably, and define acceptable user impact quantitatively**.

## Common Misconceptions

**“High availability = never fail.”** Availability is measured fraction/service objective; components can fail while system remains available.

**“More replicas always safer.”** Shared failure domains, bad deploys and replicated corruption can take all copies.

**“Monitoring = observability.”** Monitoring watches known signals; observability broader ability to infer unknown/internal conditions through telemetry.

## Kết nối

[Distributed partial failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) supplies failure model; [idempotency](../08_software_systems/04_time_serialization_and_idempotency.md) enables safe retries; [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md) explains saturation and queue collapse.

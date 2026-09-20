# State, queues, backpressure và system boundaries

Many production systems can be understood as producers, queues/buffers and consumers moving state/events across boundaries. Queue smooths bursts and decouples rates, but it does not create capacity. Without backpressure or load shedding, overload only moves into memory/latency.

## Why queues exist

Producer may create work faster temporarily than consumer processes. Queue stores temporal difference. It also decouples availability: producer can enqueue while downstream temporarily unavailable if broker durable enough.

But for sustained arrival `λ > μ` service rate, queue grows without bound. Stable system requires long-term service capacity exceed admitted load or rejection/degradation.

## Bounded vs unbounded queue

Unbounded queue converts overload into ever-growing latency and eventually memory/disk exhaustion. Bounded queue forces explicit policy: block producer, reject new, drop oldest/newest, prioritize or spill elsewhere.

Choice is business semantics: dropping metrics may be acceptable; dropping payment command not.

## Backpressure

Backpressure propagates signal upstream that consumer cannot keep up. TCP receive/congestion windows, Reactive Streams demand, bounded channels and thread-pool queues are forms.

If upstream ignores signal and buffers locally, system has not solved overload. Backpressure must extend through chain or termination policy apply.

## Messaging semantics

At-most-once may lose but no retry duplicates; at-least-once retries but duplicates possible; exactly-once effects require stronger coordination/deduplication and scope definition.

Message broker delivery acknowledgement is not same as business transaction completion. Consumer may commit DB then crash before ack → redelivery; idempotent handler/outbox/inbox patterns handle.

## Ordering

Global total order expensive and often unnecessary. Partitioned logs provide order within partition/key. If business invariant requires per-account order, partition by account may suffice.

Concurrency can reorder completion even if dequeue order fixed. Ordering contract must specify enqueue, delivery, processing or commit order.

## State placement

State can live client, application memory, cache, database, log or external service. Placement affects availability, scaling and recovery. Local in-memory session makes horizontal scaling need sticky routing/replication; external session store adds network dependency.

“Stateless service” usually means durable/user session state externalized, not literally no temporary state.

## Event log and state

Event-sourcing stores sequence of domain events as source; current state derived by replay/folding. It enables history/audit but schema evolution, replay cost, event correctness and external side effects complex. Not every system needs it.

Change Data Capture streams database changes to downstream indexes/analytics; consistency lag must be accepted/monitored.

## Backpressure vs rate limiting

Rate limiter protects boundary by limiting admitted request rate per identity/system. Backpressure is dynamic downstream pressure. Both may coexist: limiter prevents abuse/overload; backpressure reacts current capacity.

## Queueing and retry storms

If dependency slows, queues grow; timeout triggers retries; retries increase arrival rate; overload worsens. Circuit breaker, retry budget, bounded queues and deadlines break feedback loop.

## Mental Model

> Queue is **stored waiting time**. It absorbs burst, not sustained capacity deficit. Every queue should have capacity, admission policy, failure semantics, ordering scope and observability.

## Common Misconceptions

**“Async queue makes system faster.”** It changes when caller waits and smooths load; total work/capacity unchanged.

**“Kafka/RabbitMQ guarantees exactly once everywhere.”** Broker guarantees have scope; external DB/API side effects need coordination/idempotency.

**“Unbounded queue is safer because không reject.”** It often fails later with worse latency/resource exhaustion.

## Kết nối

[Linear queues](../01_algorithms_data_structures/03_linear_data_structures.md) are local abstraction; [TCP backpressure](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) network example; [fault tolerance](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) uses load shedding/circuit breakers; next [time/idempotency](./04_time_serialization_and_idempotency.md) handles retry effects.

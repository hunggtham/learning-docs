# Time, clocks, serialization và idempotency

Three deceptively simple things cause many production bugs: time zones/clocks, representation crossing boundaries, and retries. They meet whenever a request/event is serialized, transmitted, stored and possibly repeated later.

## Wall clock vs monotonic clock

Wall clock tells civil timestamp and can jump due NTP correction/manual/timezone rules. Monotonic clock only moves forward relative duration and is appropriate timeout/elapsed measurement.

Using wall clock subtraction for timeout can fail if clock adjusts backward/forward. Use runtime monotonic time for duration.

## UTC, timezone và calendar

Instant is point on global timeline. Local date-time is representation under timezone rules. `2026-11-01 01:30` may be ambiguous in DST region. Asia/Seoul currently has no DST but software global should not assume.

Store events as instant/timestamp with clear timezone semantics; preserve user timezone separately when business concept is local schedule. “Every day at 9AM Seoul” is not same as fixed UTC offset forever in all zones.

## Distributed clocks

Server timestamps from different machines can skew. For ordering causal operations, database sequence/log offset/logical clock may be more meaningful than wall time. Time-based IDs need collision/clock-regression strategy.

## Serialization

Serialization maps in-memory/logical values to wire/storage format. JSON has text, numbers, strings, arrays/objects but limited exact numeric typing; JavaScript numbers are binary64, so 64-bit integer IDs can lose precision in JS if sent as JSON number beyond safe integer range.

Protocol Buffers/Avro schemas define field numbers/types and compatibility rules. Binary formats compact/typed but require schema discipline.

## Schema evolution

Messages outlive code during rolling deploys, queues or stored events. Additive optional fields are generally safer; deleting/reusing field numbers/types can break old readers.

Readers should often tolerate unknown fields; writers may need defaults. Compatibility can be backward (new reader old data), forward (old reader new data) or full depending ecosystem.

## Idempotency

Operation f is idempotent if applying same intended operation multiple times has same effect as once:

\[
f(f(x)) = f(x)
\]

HTTP PUT intended semantics often idempotent; POST not inherently. Business action can be made idempotent with key.

Payment request with `idempotency_key = order-123-charge-1`: server atomically records key→result and returns same result on retry instead of charge again.

## Exactly-once effect through deduplication

Network cannot always tell client if timed-out request executed. Retry + dedup store/transaction creates exactly-once-like effect for scoped operation. Key must represent same logical request, retained long enough, and payload mismatch handled.

Dedup record creation and side effect must be atomic or coordinated; otherwise crash between effect and key recording still duplicates.

## Optimistic versioning

Resource update can include version/ETag. Client reads v5, sends update “if version=5”; server atomically updates to v6. Concurrent stale writer fails instead of silently overwrite. HTTP `If-Match`/ETag and DB version columns use same compare-and-swap model.

## IDs

Auto-increment gives ordered local IDs but coordination/hotspot in distributed setting. UUID random/time-ordered variants trade locality, generation independence and information leakage differently. ID should encode only semantics needed; don't assume chronological ordering unless format guarantees and clock constraints understood.

## Mental Model

> Crossing a boundary requires **explicit representation + version contract**. Repeating a boundary call requires **idempotency/dedup contract**. Measuring duration requires **monotonic time**, while business calendars require timezone-aware civil time.

## Common Misconceptions

**“UTC solves every time problem.”** It solves global instant representation, not local calendar recurrence/business timezone semantics.

**“JSON number safely stores any database integer.”** JavaScript interoperability can lose integers beyond 2^53−1.

**“HTTP retry is safe if transport says request failed.”** Timeout can happen after server commit but before response arrives.

## Kết nối

[Encoding](../00_computation_information/01_information_bits_and_encoding.md), [distributed time/failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [transactions](../05_data_databases/02_transactions_acid_and_concurrency_control.md) and [fault-tolerant retry](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) converge here.

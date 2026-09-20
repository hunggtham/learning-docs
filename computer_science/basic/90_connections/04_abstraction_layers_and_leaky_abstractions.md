# Knowledge Connection — Abstraction layers và leaky abstractions

Computer systems are possible because no one thinks about all layers simultaneously. Browser developer sees DOM/HTTP; backend sees objects/transactions; database sees pages/logs; kernel sees processes/pages/sockets; CPU sees instructions/cache lines. Each layer offers an abstraction contract.

## Why abstraction is essential

Without abstraction, to append text to file developer would need control SSD voltage cells. Filesystem turns blocks into files; runtime turns memory into objects; TCP turns packets into byte stream; SQL turns pages/indexes into relations/query results.

Abstraction creates **local reasoning**: solve problem using model without reproducing lower-layer mechanics.

## Leaky abstraction

Joel Spolsky popularized “Law of Leaky Abstractions”: non-trivial abstractions leak to some degree. Meaning: hidden details can become observable when performance, failure or edge cases matter.

Examples:

- SQL/ORM leaks index/cardinality because query latency depends physical plan.
- TCP byte stream leaks network loss/RTT through latency/timeouts.
- GC leaks allocation/lifetime via pauses/heap pressure.
- Virtual memory leaks page/TLB locality via performance.
- Cloud object storage mounted as filesystem leaks different rename/consistency semantics.

Leak does not make abstraction useless. It defines when engineer must descend a layer.

## Layer contract and observability

Each layer transforms guarantees:

```text
Application semantics
↓
Language/runtime semantics
↓
OS abstractions
↓
ISA/memory model
↓
Microarchitecture
↓
Hardware physics
```

Across network:

```text
Application protocol
↓
TLS
↓
Transport
↓
IP
↓
Link
↓
Physical medium
```

A bug can be reasoned at highest layer where evidence explains behavior. Descend only when contract no longer explains observation.

## Boundary mismatch examples

### ORM N+1

Application thinks `order.customer` property access is local; ORM lazily issues query per order. Object abstraction hides remote/database cost. Fix requires understanding boundary cost and batching/join.

### Thread-per-request

Programmer thinks blocked thread cheap; OS thread has stack/scheduler overhead. At 100k idle connections, runtime model leaks. Async/virtual threads change representation.

### File write durability

App thinks `write()` “saved”; OS buffers; device cache not stable. Durability requirement leaks through file abstraction, requiring fsync/WAL.

### `HashMap` O(1)

Algorithm layer says expected constant; microarchitecture sees cache misses/object allocations; adversarial collisions see O(n). Performance/security leak assumptions.

## Choosing abstraction level for debugging

Start with symptom and observable contract:

- Wrong business state → application/transaction invariants.
- Query slow → plan/index/cardinality then storage/cache.
- CPU hot → profile source/JIT then cache/branch if needed.
- Request timeout → traces/queues/downstream/network.
- Memory growth → allocation/retention/GC then OS RSS/page cache.

Avoid descending to assembly for every problem; avoid refusing to descend when high-level model fails.

## Encapsulation and escape hatches

Good abstraction offers safe common path plus measured escape hatch: SQL hints/raw SQL, memory-mapped I/O, native interop, custom allocator, transport configuration. Escape hatch should be explicit because caller now inherits lower-level constraints.

## Layer inversion hazards

If business layer depends on storage-page details, coupling makes change hard. Conversely infrastructure code cannot ignore domain semantics like idempotency/transaction boundaries. Architecture should point dependencies toward stable policy while adapters know mechanisms.

## Mental Model

> Abstraction is a **lossy compression of lower-layer reality**: it preserves properties most users need and hides the rest. When hidden variables become relevant, descend deliberately, learn the leaked mechanism, then return to the highest useful model.

## Cross-references

- [What Computer Science studies](../00_computation_information/00_what_computer_science_studies.md)
- [Abstraction/modularity/API](../08_software_systems/00_abstraction_modularity_interfaces_and_apis.md)
- [Source code → CPU](./00_source_code_to_cpu.md)
- [Browser → database](./01_browser_to_database_request.md)
- [Cross-cutting trade-offs](./03_cross_cutting_tradeoffs.md)

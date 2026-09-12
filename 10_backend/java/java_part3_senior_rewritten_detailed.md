# Java Core — Part 3: Senior — Rewritten Detailed
## Java dưới góc nhìn runtime, concurrency, performance, API design và production engineering

> Part 3 không nhằm giúp bạn nhớ thêm nhiều class trong JDK. Một Senior Java engineer phải có khả năng giải thích vì sao code đúng hoặc sai dưới concurrency, biết object tồn tại ở đâu và vì sao không được GC, biết method call có thể được JIT optimize thế nào, biết khi nào thread đang chạy hay đang chờ, biết DB/HTTP resource nào đang bị giữ, và biết lấy bằng chứng từ JVM trước khi tuning.
>
> Các tư duy kiểu Senior, Language Idiom, Programming Pattern và Design Pattern được hòa vào nội dung. Khi một pattern được nhắc tên, nó được giải thích cùng trade-off và failure mode thay vì xuất hiện như một checklist để học thuộc.

---

# 1. Senior Java không đồng nghĩa với thuộc nhiều API

Một developer có thể biết hàng trăm methods nhưng vẫn khó xử lý incident. Senior skill nằm ở khả năng nhìn code theo năm câu hỏi: state nằm ở đâu, ai sở hữu state/resource, execution context nào đang chạy, contract concurrency/transaction nào bảo vệ correctness, và failure có thể xảy ra ở boundary nào.

Ví dụ:

```java
cache.computeIfAbsent(
    key,
    this::loadFromDatabase);
```

Beginner thấy “cache miss thì load DB”. Senior hỏi thêm: map có concurrent không, mapping function có chạy dưới internal synchronization không, DB call có block lâu không, key cardinality có unbounded không, failed load có bị cache không, multiple app instances có cùng cache không, và stale policy là gì.

Senior Java là tư duy về **correctness + capacity + ownership + observability**, không phải cú pháp nâng cao.

---

# 2. Make invalid states khó biểu diễn

Giả sử:

```java
void transfer(
    long fromAccountId,
    long toAccountId,
    BigDecimal amount,
    String currency) {
}
```

Compiler không ngăn bạn đảo hai account IDs hoặc truyền currency invalid.

Strong domain types:

```java
record AccountId(long value) {
    AccountId {
        if (value <= 0) {
            throw new IllegalArgumentException();
        }
    }
}
```

```java
record Money(
        BigDecimal amount,
        Currency currency) {
    Money {
        Objects.requireNonNull(amount);
        Objects.requireNonNull(currency);

        if (amount.signum() < 0) {
            throw new IllegalArgumentException();
        }
    }
}
```

làm invalid state bị chặn ở construction boundary.

Đây là Value Object thinking. Bạn không “validate cùng rule ở mọi service”; bạn parse/construct type một lần rồi core tin type contract.

---

# 3. Identity và Value Semantics

Entity identity:

```text
User ID 42
```

vẫn là cùng user dù name đổi.

Value object:

```text
Money 10,000 KRW
```

được định nghĩa bởi value.

Nếu bạn dùng `equals` cho JPA entity theo mutable fields, set/map behavior có thể thay khi entity đổi. Nếu dùng generated ID trước khi persist, equality của transient entity cũng cần design.

Không có một universal entity equality recipe. Bạn phải hiểu lifecycle của identity.

Records rất phù hợp value semantics, nhưng không phải mọi record là domain value object chỉ vì compiler generate `equals`.

---

# 4. Stable Hash Keys là correctness issue

HashMap key fields không nên mutate trong khi key đang nằm trong map.

Tương tự cache key object cần stable equality/hash.

Nếu domain key mutable, dùng immutable snapshot/value key thay vì entity object.

```java
Map<UserId, User>
```

thường tốt hơn:

```java
Map<UserEntity, Data>
```

nếu entity equality lifecycle phức tạp.

Đây là lý do equality contract có thể trở thành system-level correctness, không chỉ Java interview question.

---

# 5. Records ở level Senior

Record phù hợp message/config/result/value-like structure vì constructor/accessors/equality rõ và shallowly immutable.

Nhưng:

```java
record Policy(
    List<Rule> rules) {
}
```

không thực sự immutable nếu list mutable.

Defensive constructor:

```java
record Policy(
    List<Rule> rules) {

    Policy {
        rules =
            List.copyOf(rules);
    }
}
```

Nếu `Rule` mutable, object graph vẫn chưa deep immutable.

Senior phải reason ownership graph chứ không chỉ `final`/record keyword.

---

# 6. Sealed Types + Pattern Matching

Sealed hierarchy:

```java
sealed interface PaymentResult
    permits Approved,
            Declined,
            TechnicalFailure {
}
```

Java 21 switch:

```java
return switch (result) {
    case Approved a ->
        handleApproved(a);

    case Declined d ->
        handleDeclined(d);

    case TechnicalFailure f ->
        retryOrFail(f);
};
```

Compiler biết hierarchy closed và có thể enforce exhaustiveness.

Cách này rất mạnh cho finite result/error/state algebra.

Nhưng nếu subclasses có behavior tự nhiên và open extension là requirement, polymorphism/interface extension có thể phù hợp hơn. Sealed không phải “modern replacement inheritance”; nó là modeling tool cho closed worlds.

---

# 7. Source code không chạy trực tiếp

Compiler tạo bytecode.

```bash
javac UserService.java
javap -c UserService
```

`javap -c` cho instructions.

Bạn không cần đọc bytecode hàng ngày, nhưng nó hữu ích khi muốn biết autoboxing, switch, lambda hoặc compiler-generated bridge methods thực sự biến thành gì.

Ví dụ lambdas thường dùng `invokedynamic` machinery thay vì đơn giản tạo anonymous inner class như nhiều người tưởng.

---

# 8. JVM Stack Frame và Operand Stack

Mỗi method invocation có frame chứa local variables, operand stack và bookkeeping.

Bytecode thường load operands lên stack, execute instruction rồi store result.

Điều này giải thích vì sao JVM được gọi stack-based virtual machine.

Bạn không cần optimize code theo bytecode manually. Nhưng khi đọc `javap`, biết local slots/operand stack giúp hiểu control flow và verifier errors.

---

# 9. JIT Compilation

JVM ban đầu có thể interpret và compile code theo tiers. Khi runtime profile cho thấy method/call-site hot, JIT compile machine code optimized.

Optimizations có thể gồm:

```text
inlining
dead-code elimination
escape analysis
loop optimizations
devirtualization
```

Do đó performance của Java method sau warm-up khác cold start.

Đây là nguyên nhân microbenchmark naive dễ sai.

---

# 10. Inlining

Method call:

```java
money.add(other)
```

có overhead abstractly, nhưng JIT có thể inline method body vào caller nếu profitable.

Small method không nhất thiết “chậm vì call nhiều”.

Vì vậy đừng viết giant methods để “tránh function-call overhead”.

Maintainable abstraction thường cho JIT nhiều cơ hội optimize.

Measure hot path thực tế thay vì đoán.

---

# 11. Deoptimization

JIT optimize dựa assumptions/profile.

Ví dụ call-site chủ yếu thấy một implementation nên JIT devirtualize/inline. Sau đó class khác xuất hiện và assumption không còn đúng; JVM có thể deoptimize và recompile.

Performance có thể thay đổi trong runtime.

Một latency spike không phải luôn GC; class loading/deopt/JIT transitions cũng có thể góp phần trong specialist cases.

JFR/compiler logs giúp khi thực sự cần.

---

# 12. Escape Analysis

Object:

```java
Point p = new Point(x, y);
return p.x() + p.y();
```

nếu JIT chứng minh object không escape method/thread context, allocation có thể được scalar-replaced/eliminated.

Điều này cho thấy `new` không luôn tương đương expensive heap allocation.

Đừng viết object pools cho tiny DTOs chỉ để “giảm GC” nếu chưa đo allocation/GC pressure.

Pooling còn làm ownership/concurrency phức tạp.

---

# 13. Class Lifecycle: Loading, Linking, Initialization

Concept:

```text
load
→ verify
→ prepare
→ resolve
→ initialize
```

Static initialization xảy ra khi class được initialized theo triggers cụ thể.

Static block:

```java
static {
    expensiveRemoteCall();
}
```

là risky. Class initialization lock/failure có thể làm startup/runtime khó debug.

Keep static initialization boring: constants/pure setup. External I/O nên có explicit lifecycle.

---

# 14. Class Initialization Failure

Nếu static initializer throw:

```java
ExceptionInInitializerError
```

và subsequent use có thể gặp `NoClassDefFoundError` liên quan class initialization failure.

Root cause nằm ở first failure, không phải later symptom.

Khi production thấy `NoClassDefFoundError`, inspect cause chain và earlier logs.

---

# 15. Class Identity = Name + Defining ClassLoader

Hai classes cùng binary name:

```text
com.example.Plugin
```

nhưng loaded bởi different classloaders là distinct runtime classes.

Bạn có thể gặp:

```text
ClassCastException:
com.example.Plugin cannot be cast
to com.example.Plugin
```

nghe vô lý nhưng classloaders khác.

App servers, plugin systems, hot reload, test tools và agents tạo scenarios này.

---

# 16. Parent Delegation

Typical classloader delegation tìm parent trước để core/shared classes không bị duplicate.

Custom plugin isolation có thể thay strategy.

Context ClassLoader tồn tại để libraries/frameworks tìm resources/providers trong environment mà defining loader không đủ.

Không custom classloader nếu không có strong reason; leaks/type identity/security complexity lớn.

---

# 17. Java Memory Model là bắt buộc

Concurrency không thể reason bằng “thread chạy lần lượt chắc thấy value”.

Java Memory Model định nghĩa visibility, ordering và synchronization semantics.

Một **data race** xảy ra khi multiple threads access shared variable, ít nhất một write, và accesses không được ordered bởi synchronization phù hợp.

Data race có thể tạo stale reads, lost updates và behaviors compiler/CPU được phép thực hiện.

---

# 18. Happens-Before

Nếu action A happens-before B, effects A visible/ordered đối với B theo JMM.

Key relationships gồm monitor unlock → subsequent lock cùng monitor, volatile write → subsequent read cùng variable, actions trước `Thread.start` → thread actions, thread actions → successful `join`.

Reason bằng happens-before thay vì folklore như “volatile flush CPU cache”.

---

# 19. `volatile` không phải transaction

```java
volatile int count;
```

`count++` vẫn read-modify-write và race.

```java
if (balance >= amount) {
    balance -= amount;
}
```

cần compound invariant; volatile không khóa check+update.

Use synchronized/lock/atomic state transition.

Volatile tốt cho one-variable publication/status flags.

---

# 20. Final Fields và Safe Publication

Final fields có special JMM initialization guarantees nếu object construction đúng và `this` không escape trước constructor complete.

Bad:

```java
class Listener {
    Listener(EventBus bus) {
        bus.register(this);
        this.config = loadConfig();
    }
}
```

`this` escape trước fully initialized; another thread có thể observe partially constructed state.

Constructor should finish invariant before publishing reference.

Safe publication có thể qua final/volatile/synchronized/concurrent collections/static initialization, tùy case.

---

# 21. Double-Checked Locking

Modern correct form requires volatile:

```java
private static volatile Service instance;

static Service getInstance() {
    Service local = instance;

    if (local == null) {
        synchronized (Service.class) {
            local = instance;

            if (local == null) {
                local = new Service();
                instance = local;
            }
        }
    }

    return local;
}
```

Nhưng simpler alternatives exist: eager static initialization, holder idiom, DI container.

Đừng dùng DCL chỉ vì interview familiarity.

---

# 22. `synchronized` vẫn là primitive rất tốt

Synchronized gives mutual exclusion + visibility with simpler syntax/lifecycle than manual Lock.

```java
synchronized (lock) {
    checkInvariant();
    updateState();
}
```

Lock **invariant**, không lock random line.

If state fields must change together, protect them under same lock.

Keep lock object private to prevent external code locking it.

---

# 23. Critical Section phải nhỏ nhưng đủ

Bạn muốn giữ lock ngắn để giảm contention.

Nhưng đừng release giữa check và update nếu invariant cần atomic.

Bad:

```text
lock
check
unlock

remote computation?

lock
update based on stale check
```

Correctness first, then reduce work by computing immutable/preparable data outside lock and commit state change inside.

---

# 24. Deadlock và Lock Ordering

Thread A:

```text
lock account1
wait account2
```

Thread B:

```text
lock account2
wait account1
```

Deadlock.

Global ordering:

```java
Account first =
    id1.compareTo(id2) < 0
        ? a
        : b;
```

always lock lower ID first.

Consistent lock order is powerful.

Thread dump shows `BLOCKED`/owned monitors and deadlock detector can identify cycles.

---

# 25. `ReentrantLock`

Use when you need:

```text
tryLock
lockInterruptibly
multiple Conditions
fairness options
```

Always:

```java
lock.lock();

try {
    ...
} finally {
    lock.unlock();
}
```

Fair lock reduces starvation but often lowers throughput. Do not turn fairness on because it sounds ethically better; it is scheduling trade-off.

---

# 26. ReadWriteLock

Many readers can hold read lock; writer exclusive.

Useful if read-heavy and read critical sections significant.

But modern synchronization/JIT/cache behavior means it is not automatically faster than single lock.

Benchmark.

---

# 27. StampedLock

Supports optimistic reads.

Flow:

```java
long stamp =
    lock.tryOptimisticRead();

State snapshot = read();

if (!lock.validate(stamp)) {
    stamp =
        lock.readLock();

    try {
        snapshot = read();
    } finally {
        lock.unlockRead(stamp);
    }
}
```

Powerful but API is less ergonomic/reentrant semantics differ. Use only when contention/profile justifies.

---

# 28. CAS Thinking

Compare-and-set:

```text
if current == expected
    set update atomically
else fail
```

AtomicReference:

```java
while (true) {
    State old = ref.get();
    State next =
        old.transition(command);

    if (ref.compareAndSet(
            old,
            next)) {
        return;
    }
}
```

This can make multi-field invariant atomic if state is one immutable object.

CAS loop may retry under contention.

Lock-free is not automatically simpler/faster; use high-level concurrent utilities first.

---

# 29. ABA Problem

CAS sees value A, another thread changes A→B→A, CAS sees A again and cannot tell intervening change.

Some algorithms care. Versioned/stamped references can address.

Most application code should not build custom lock-free structures; know concept for library/runtime code.

---

# 30. LongAdder Semantics

LongAdder scales increments under contention by distributing state.

Excellent for metrics counters.

If correctness requires atomic “read current exact value then reset/decision”, AtomicLong/lock may be more appropriate.

Performance primitive choice must follow semantic guarantee.

---

# 31. ConcurrentHashMap Atomic Methods

```java
map.compute(
    key,
    (k, old) ->
      transition(old));
```

can atomically update entry relative map's concurrency semantics.

Avoid external check-then-act.

Mapping/remapping functions should not perform long remote calls or complex modifications of same map.

Use map operations to express atomic per-key transition.

---

# 32. Weakly Consistent Iteration

Concurrent collections often don't throw `ConcurrentModificationException` and provide weakly consistent views.

Iterator may reflect some concurrent updates, not a frozen snapshot.

If you require exact snapshot, create immutable copy or lock appropriately.

Thread-safe collection structure does not automatically satisfy application-level consistency across multiple operations.

---

# 33. CopyOnWriteArrayList

Reads operate on stable snapshot array; writes copy.

Listener list with 10 listeners and rare registration: excellent.

10k-element list with frequent writes: expensive.

Understand workload ratio and memory copy cost.

---

# 34. BlockingQueue as Backpressure

Bounded queue is one of the simplest production backpressure tools.

```java
BlockingQueue<Job> queue =
    new ArrayBlockingQueue<>(500);
```

If producer faster than consumers, queue fills and `put()` waits.

This prevents unlimited memory growth.

Capacity selection is business/performance policy: how much burst buffer is acceptable before slowdown/rejection?

---

# 35. Semaphore as Bulkhead

Remote vendor only permits 20 concurrent requests:

```java
Semaphore permits =
    new Semaphore(20);

permits.acquire();

try {
    return client.call();
} finally {
    permits.release();
}
```

This protects downstream even if 100k virtual threads exist.

Bulkhead isolates resource capacity and prevents one dependency from consuming all concurrency.

---

# 36. Coordination Primitives

`CountDownLatch` lets threads wait for N events.

`CyclicBarrier` coordinates repeated phase meeting.

`Phaser` handles dynamic/multi-phase parties.

Use them for coordination, not general shared-state locking.

Structured concurrency may offer clearer lifecycle for task trees in modern Java, but preview/final status depends Java version.

---

# 37. Thread Pool = workers + queue + saturation policy

A pool with 16 threads and unbounded queue may keep accepting work until heap dies.

A pool with bounded 1000 queue will reach saturation visibly.

At saturation, choose reject/caller-runs/drop according business semantics.

No universal thread count formula. CPU-bound pool close to cores; blocking workloads depend wait/compute ratio, but virtual threads change model.

Measure CPU utilization, queue delay and downstream capacity.

---

# 38. Graceful Executor Shutdown

Owning component:

```java
executor.shutdown();

if (!executor.awaitTermination(
        30,
        TimeUnit.SECONDS)) {

    executor.shutdownNow();
}
```

`shutdown()` stops new tasks and lets submitted tasks complete.

`shutdownNow()` attempts interruption and returns tasks never started.

Tasks must cooperate with interruption.

Resource lifecycle belongs to owner; don't leave executors running across tests/deploys.

---

# 39. CompletableFuture Execution Topology

A future chain hides threads unless you track executors.

```java
supplyAsync(load, ioExecutor)
    .thenApply(transform)
    .thenComposeAsync(
        this::remote,
        ioExecutor)
```

Which stage runs where matters for blocking.

Common pool contamination can cause unrelated features to contend.

Explicit executors make capacity visible.

---

# 40. `thenApply` vs `thenCompose`

If function returns value:

```java
thenApply(User::name)
```

If function returns future:

```java
thenCompose(
    user ->
      loadOrders(user.id()))
```

Using `thenApply` for future-returning function creates nested:

```text
CompletableFuture<
    CompletableFuture<X>>
```

This is same map vs flatMap concept across Optional/Stream/reactive APIs.

---

# 41. CompletableFuture Exceptions

`exceptionally` recovers by supplying value.

`handle` transforms success/error.

`whenComplete` observes but usually preserves original outcome unless callback throws.

If multiple fan-out branches fail, which failure surfaces can depend composition.

Preserve causes and log at ownership boundary, not every stage.

---

# 42. Future Timeouts do not cancel underlying work automatically in every pattern

CompletableFuture timeout methods can complete future exceptionally/default, but underlying operation may continue depending how task/resource cancellation is implemented.

Timeout is caller waiting policy; cancellation is separate.

Remote HTTP client must have its own request/socket timeout/cancellation.

Don't assume one timeout kills everything downstream.

---

# 43. Fan-Out / Fan-In Load Amplification

Request fans to 10 downstream calls concurrently.

At 1000 incoming requests, up to 10k calls.

Parallelization can lower individual latency while destroying system capacity.

Bound concurrency, batch requests or redesign data ownership.

Senior performance optimization is system-level, not single-request-level.

---

# 44. Virtual Threads Java 21

Virtual threads restore simple thread-per-request/task style for blocking I/O at large concurrency.

```java
try (var executor =
     Executors
       .newVirtualThreadPerTaskExecutor()) {

    List<Future<Response>>
        futures = ...
}
```

Don't create fixed pool of 100 virtual threads. That artificially removes their scalability.

Use semaphore/connection pools for actual scarce resources.

---

# 45. Virtual Threads do not make CPU faster

100k CPU-bound virtual threads on 8 cores still compete for 8 cores.

For CPU workloads, bounded parallelism near cores remains relevant.

Virtual threads shine when threads spend time blocked on I/O.

Throughput improves because JVM doesn't need one expensive platform thread per blocking task.

---

# 46. Pinning

Early virtual-thread generations could pin carrier platform thread in certain synchronized/native/blocking situations.

Modern JDKs have improved this significantly across releases. Therefore old blanket advice “never synchronized with virtual threads” is outdated.

Use JFR/jcmd events to identify actual pinning before refactor.

Version matters.

---

# 47. ThreadLocal with Virtual Threads

Each virtual thread can have ThreadLocal values, but huge numbers of threads magnify memory footprint if each ThreadLocal stores heavy state.

Also thread-local context can obscure dependencies.

Modern ScopedValue is designed for scoped immutable context and became final in Java 25. That topic belongs Master Supplement, but Senior should already avoid using ThreadLocal as arbitrary global storage.

---

# 48. Structured Concurrency Awareness

Structured concurrency treats related child tasks as a lexical/lifecycle unit: fork tasks, join, cancel siblings on failure, leave scope only when child lifecycle resolved.

In Java 21 it was preview and continued evolving through later releases, so exact API is version-sensitive.

Learn concept before signatures: task lifetime should not escape its parent accidentally.

---

# 49. GC Roots và Reachability

An object is collectable when no longer reachable through GC roots according to reference semantics.

Roots include thread stacks, static fields, JNI references and other JVM structures.

A “memory leak” in Java means objects remain reachable accidentally even though business no longer needs them.

GC cannot collect reachable garbage by business meaning.

---

# 50. Static Collection Leak

```java
static final Map<String, User>
    CACHE = new HashMap<>();
```

if entries never removed, they remain reachable forever.

Changing collector does not fix.

Need eviction/ownership/lifecycle.

Heap dump dominator tree can reveal retained size path.

---

# 51. Listener Leak

Register listener:

```java
publisher.addListener(listener);
```

but never unregister.

Publisher long-lived retains listener, listener may retain entire object graph.

Lifecycle subscription should return registration handle/AutoCloseable or explicit remove.

---

# 52. ThreadLocal Leak

Thread pool worker lives long. ThreadLocal value may live as long as worker if not removed.

Pattern:

```java
try {
    CONTEXT.set(value);
    work();
} finally {
    CONTEXT.remove();
}
```

ThreadLocal lifecycle must match task/request, not thread pool lifetime.

Master Supplement will explain internals/ScopedValue.

---

# 53. Queue Backlog Leak

Unbounded queue is logical retention.

Producer > consumer:

```text
queue size ↑
heap ↑
latency ↑
```

Not classic reference bug; capacity design bug.

Observe queue depth.

Bound or load-shed.

---

# 54. ClassLoader Leak

Application server/reload creates new classloader, but old loader remains referenced by ThreadLocal, thread, static registry, JDBC driver, MBean, logging callback.

All classes/metaspace/object graphs loaded by old loader stay alive.

Symptom: metaspace grows after redeploy.

This is why lifecycle cleanup matters beyond heap objects.

---

# 55. Generational GC Mental Model

Many objects die young.

Generational collectors exploit this by focusing young regions frequently and promoting survivors.

Exact mechanics differ collectors/releases.

Do not design correctness around “object goes to old after N collections”; it's implementation detail.

---

# 56. G1 GC

G1 divides heap into regions and aims predictable pause targets while collecting regions with useful reclaim value.

It's common default in modern server JDKs.

Useful log:

```bash
-Xlog:gc*
```

Don't start with dozens of G1 tuning flags. Modern JVM ergonomics are good; first measure allocation, heap occupancy, pause cause.

---

# 57. Humongous Objects

In G1, very large objects relative region size use special humongous allocation treatment.

Large byte arrays/strings/buffers can create fragmentation/GC pressure.

If logs show humongous allocation issues, investigate payload sizes, serialization/buffering, not just increase heap.

---

# 58. ZGC

ZGC is low-latency concurrent collector designed for very small pause times across large heaps, with modern generational evolution in recent JDKs.

It may trade CPU/throughput/resources differently from G1.

Choose based SLO:

```text
latency
throughput
heap
CPU headroom
```

not “ZGC newest so best”.

---

# 59. Serial and Parallel GC Awareness

Serial GC can be appropriate small heaps/simple workloads.

Parallel GC targets throughput with parallel stop-the-world work.

Collector choice is workload decision.

A CLI batch that needs max throughput may prefer different GC than latency-sensitive API.

---

# 60. Heap Sizing

`-Xmx` sets max heap.

Container memory 2 GB with:

```text
-Xmx2g
```

leaves no room for metaspace, thread stacks, direct buffers, code cache, native libraries and JVM itself.

Need native headroom.

Use percentage-based container-aware options where appropriate and measure RSS.

---

# 61. `Xms == Xmx` Trade-Off

Fixing initial = max can reduce heap resizing variability and ensure memory available early, but commits/reserves larger memory footprint and can hurt container density.

No universal production rule.

Workload/deployment economics decide.

---

# 62. Metaspace

Class metadata lives metaspace/native memory.

Dynamic class generation/redeploy/classloader leaks can grow it.

Heap dump alone may not explain metaspace OOM.

Use classloader stats/JFR/NMT.

---

# 63. Thread Stack Memory

Each platform thread reserves/uses stack memory controlled partly by `-Xss`.

Thousands of platform threads can consume huge native memory even if heap small.

Virtual threads use different stack representation/scaling, one reason they support large concurrency.

Don't reduce Xss aggressively without understanding deep stack/StackOverflow risks.

---

# 64. Direct Memory

DirectByteBuffer allocates native/off-heap memory.

Network frameworks may use direct buffers heavily.

Heap graph may show small wrapper objects while RSS grows due to native buffers.

Observe direct memory metrics/NMT/framework allocator.

---

# 65. Native Memory Tracking

Enable NMT at JVM startup, e.g. appropriate `-XX:NativeMemoryTracking=summary/detail`.

Then:

```bash
jcmd <pid> VM.native_memory summary
```

Breaks down categories like Java Heap, Class, Thread, Code, GC, Compiler, Internal.

NMT has overhead, especially detail. Use according incident policy.

---

# 66. `jcmd` là Swiss Army Knife

List processes:

```bash
jcmd
```

Thread dump:

```bash
jcmd <pid> Thread.print
```

Heap info:

```bash
jcmd <pid> GC.heap_info
```

JFR:

```bash
jcmd <pid> JFR.start ...
jcmd <pid> JFR.dump ...
```

VM flags/classloader/native memory commands vary version.

Learn `jcmd <pid> help`.

---

# 67. Đọc Thread Dump

Thread states:

```text
RUNNABLE
BLOCKED
WAITING
TIMED_WAITING
```

RUNNABLE không always CPU-running; native socket I/O may appear differently depending JVM/OS.

Look for many identical stacks, lock owners, pool waits, DB client waits.

One dump is snapshot. Take repeated dumps several seconds apart to see persistence/progress.

---

# 68. Deadlock in Thread Dump

JVM can identify Java-level monitor/ownable synchronizer deadlocks.

If found, inspect lock acquisition paths and define consistent ordering.

Don't just increase thread pool.

---

# 69. JFR

Java Flight Recorder captures low-overhead events.

Typical investigation:

```text
CPU samples
allocation
GC pauses
monitor contention
thread park
socket/file I/O
exceptions
class loading
virtual thread events
```

Run continuous low-overhead recording where policy allows so incident history exists before problem.

---

# 70. Performance: Latency vs Throughput

Latency = time one operation takes.

Throughput = operations per time.

Optimization can trade them.

Batching increases throughput but may delay individual item.

Large queue can temporarily maximize throughput but destroys tail latency.

Define SLO before tuning.

---

# 71. Tail Latency

Average 100 ms with p99 3 s means 1% requests terrible.

Users often feel tail.

Track p50/p95/p99.

GC, DB locks, remote service jitter, queueing and contention show strongest in tails.

---

# 72. Little's Law Awareness

Concept:

```text
concurrency ≈ throughput × latency
```

If 1000 req/s and average 0.5s, roughly 500 concurrent in-flight operations.

This helps reason thread/connection/queue capacity.

Not a magic sizing formula but useful system intuition.

---

# 73. Allocation Rate

High allocation can increase GC CPU and memory bandwidth even if heap never OOMs.

JFR can show allocation hotspots.

Fix unnecessary materialization/large intermediate objects only if profile shows cost.

Don't make code unreadable to avoid tiny short-lived objects JIT/GC handle well.

---

# 74. Boxing Cost

Hot loop:

```java
Stream<Integer>
```

creates/uses wrappers vs `IntStream`.

Metrics/data-processing hot paths may benefit primitive APIs.

Business CRUD rarely needs premature boxing optimization.

Measure allocation profiles.

---

# 75. String Concatenation

Modern compiler/JDK uses optimized concat strategies.

Simple:

```java
String s =
    a + ":" + b;
```

fine.

Loop building huge text still benefits builder/streaming.

Performance advice must consider modern JDK, not Java 6 folklore.

---

# 76. False Sharing Awareness

Two threads update unrelated counters located same cache line, causing cache coherence traffic.

This is hardware-level performance issue.

Do not pad random fields. Only investigate if low-level benchmark/profile shows cache contention.

JVM/JDK internals may use padding techniques unavailable/stable for normal app APIs.

---

# 77. JMH Mindset

Microbenchmark pitfalls include JIT warm-up, dead-code elimination, constant folding, GC, branch prediction.

JMH provides forks, warmup, measurement, Blackhole patterns.

Example “nanoTime around one call” is not enough for library-level performance claims.

Benchmark representative data and deployment JDK.

---

# 78. Buffered I/O

System calls are expensive relative memory operations.

Buffering aggregates reads/writes.

But double buffering large payloads can waste memory.

Know underlying API: `Files.newBufferedReader` already buffered semantics; adding redundant layers may not help.

---

# 79. Direct ByteBuffer

Direct buffers can reduce copies in native I/O paths but allocate/free differently and use native memory.

Good for high-performance networking/file I/O; unnecessary for ordinary small file parsing.

Cleaner/native lifetime historically less deterministic than heap.

Use frameworks/JDK APIs carefully and observe direct memory.

---

# 80. FileChannel Transfer

`transferTo`/`transferFrom` may use efficient OS-assisted transfer depending platform/JDK.

Useful large file transfer/server paths.

Do not assume zero-copy guarantee across all environments; benchmark.

---

# 81. Memory-Mapped Files

`FileChannel.map` maps file region into virtual memory.

Useful random/large file access patterns.

But unmapping/lifecycle, page faults, file truncation and address-space behavior create complexity.

Specialist technique, not default file read API.

---

# 82. Java HTTP Client Production Engineering

Reuse client with connection management.

Set connect timeout.

Set request timeout.

Handle status separately from transport failure.

Read body bounded; large body may require streaming handler.

TLS/DNS/proxy settings matter.

Remote-call code is a failure boundary and should translate exceptions.

---

# 83. Deadline Propagation

Incoming request has deadline D.

Each child call timeout should be <= remaining D minus local margin.

If retry, each attempt consumes budget.

This prevents downstream work continuing after caller has already timed out.

Java Core does not provide one universal deadline propagation framework; design context explicitly or use framework support later.

---

# 84. Retry

Retry only transient and safely repeatable operations.

Exponential backoff:

```text
100ms
200ms
400ms
```

add jitter to avoid synchronized retry storms.

Limit attempts and total time.

HTTP 400 validation should not retry. Connection reset maybe retry if idempotent.

Payment POST requires idempotency protection.

---

# 85. Circuit Breaker

Track recent failures; open circuit and fail fast while downstream unhealthy; allow probes later.

Circuit breaker protects system, not correctness of one call.

It belongs resilience library/framework level, but Senior Java should understand pattern independent of Spring.

---

# 86. Bulkhead

Separate capacity per dependency/workload.

Payment 20 concurrent, report 5, email 50.

Can be semaphore, executor, connection pool.

If one subsystem stalls, it doesn't consume all threads/requests.

---

# 87. Reflection Cost không chỉ nanoseconds

Reflection adds runtime type/access failures, encapsulation break, harder refactor/AOT compatibility and metadata lookup.

Frameworks use it legitimately.

Application hot path should not scan methods repeatedly; cache metadata if infrastructure requires.

Main cost often complexity, not raw invoke ns.

---

# 88. MethodHandle Awareness

MethodHandle is typed low-level dynamic invocation primitive.

It supports lookup, `MethodType`, adaptation/composition and underpins features like dynamic languages/lambdas.

Libraries may prefer it over raw reflection for advanced dynamic dispatch.

Application business code rarely needs.

Master Supplement goes deeper.

---

# 89. Dynamic Proxy

JDK Proxy intercepts interface calls and is core design concept behind framework clients/AOP.

Invocation handler must correctly handle `equals/hashCode/toString` semantics, exception unwrapping and classloader/interface visibility.

Naive proxy code can wrap target exceptions in `InvocationTargetException`.

Frameworks handle many details.

---

# 90. Annotation Processing vs Runtime Reflection

Runtime annotation:

```text
class loaded
→ reflection scans metadata
→ behavior
```

Compile-time processor:

```text
javac
→ annotation processor
→ generated source/resource
→ compiled
```

Compile-time generation moves work/errors earlier and avoids runtime reflection, but build complexity increases.

MapStruct-like tools show this model.

Master Supplement covers processor APIs.

---

# 91. Annotation không tạo behavior

`@Retry`
`@Transactional`
`@Inject`

are metadata.

Some engine must read it via compiler/runtime processing and act.

When annotation “doesn't work”, ask who processes it and whether object/call path is under that engine.

This mental model is essential before Spring.

---

# 92. JDBC Transaction Boundary là Business Boundary

Repository method:

```java
saveOrder()
```

không necessarily whole transaction.

Business:

```text
create order
reserve local stock rows
write ledger
```

may need one transaction.

Transaction should be at use-case/application boundary where atomic requirement is known.

Spring later makes declarative policy easier, but concept belongs Java/database design.

---

# 93. Keep DB Transaction Short

Don't:

```text
open transaction
query/update
call remote HTTP 5s
send email
commit
```

Connection/locks held during remote wait.

Remote effects aren't rolled back by DB.

Short local transaction + outbox/state machine is often better.

---

# 94. JDBC Isolation và Locking

Transaction isolation must be matched to DB implementation and business anomaly tolerance.

READ COMMITTED may allow different reads across statements.

SERIALIZABLE stronger but may abort/block more.

Use optimistic versioning or explicit locks where business needs.

Don't set SERIALIZABLE globally “for safety”.

---

# 95. Query Timeout

Statement:

```java
statement.setQueryTimeout(seconds);
```

driver/database support semantics vary.

Also connection acquire timeout, network/socket timeout and transaction timeout exist.

One layer timeout doesn't guarantee all.

---

# 96. Connection Pool Awareness

Raw DataSource in production often backed by pool.

Pool size controls concurrent DB work.

If app has 20 connections and 1000 virtual threads, 980 wait.

That's intentional backpressure if DB only supports 20 effectively.

Observe acquisition wait/active/idle and DB metrics.

---

# 97. Native Serialization Security

Deserializing untrusted Java serialization has historical gadget-chain/code-execution risks.

Do not expose `ObjectInputStream` to arbitrary network/file data.

`ObjectInputFilter` can restrict classes/graphs in legacy cases, but migration away from unsafe serialization is often preferable.

Serialization format is trust boundary.

---

# 98. `SecureRandom`

Use for tokens/cryptographic nonces/keys.

```java
SecureRandom secure =
    new SecureRandom();
```

`Random`, `ThreadLocalRandom` are predictable enough that they should not protect secrets.

UUID random may be fine as identifier but not automatically secret token with required entropy/policy.

---

# 99. Password Hashing

Do not:

```java
SHA-256(password)
```

as password storage.

Password hashing requires adaptive, salted algorithms/policies such as Argon2/bcrypt/scrypt/PBKDF2 depending approved ecosystem.

Use maintained security library/framework.

Cryptographic design is a specialist domain.

---

# 100. Secrets

Passwords/API keys/private keys should not be source constants or logs.

Read from environment/secret manager/secure file boundary.

Avoid keeping secrets in String longer than necessary in special high-security contexts, though general Java ecosystem APIs may require strings.

Most importantly: never log them.

---

# 101. Exception Architecture

Classify:

```text
domain/business rejection
validation
transient infrastructure
permanent infrastructure/config
programming bug
cancellation/interruption
```

Caller policy differs.

A `UserNotFoundException` is not same as `DatabaseUnavailableException`.

Retry/HTTP mapping/log level should reflect category.

---

# 102. Preserve Cause

Wrap:

```java
throw new PaymentUnavailableException(
    "Payment provider failed",
    e);
```

Cause chain is production evidence.

Do not replace detailed low-level error with `"something failed"` without cause.

But don't leak cause text directly to external client.

---

# 103. `InterruptedException`

Interruption is cancellation/control signal.

If method can propagate, do so.

If converting:

```java
Thread.currentThread()
      .interrupt();
```

before throwing unchecked if policy requires.

Swallowing interruption can prevent executor/application shutdown.

---

# 104. Log Once at Ownership Boundary

If repository logs ERROR + rethrows, service logs ERROR + rethrows, controller logs ERROR, same failure appears three times.

Low layers add context in exception; ownership/request boundary logs once with trace/request context.

Expected business errors may be INFO/WARN/no stack, not ERROR.

---

# 105. Java Library API Design

Public API is expensive to change.

Keep visibility narrow.

Accept abstractions:

```java
Collection<T>
```

when you don't need List indexing.

Return interface:

```java
List<T>
```

not concrete `ArrayList`.

But don't over-generalize parameter if method requires order/random access semantics.

API contract should match actual requirements.

---

# 106. Defensive Copy in Public API

Constructor receiving collection:

```java
this.items =
    List.copyOf(items);
```

Getter can return immutable list.

This protects internal invariant.

If elements mutable, document/clone/map immutable views according ownership.

Public API needs explicit null/thread-safety/mutation contracts.

---

# 107. Binary, Source và Behavioral Compatibility

Changing method signature breaks source/binary.

Adding abstract interface method can break implementors unless default.

Changing `equals`/ordering behavior may break behavioral compatibility even if compile succeeds.

Libraries must think versioning beyond compiler errors.

SemVer only works if you understand public contracts.

---

# 108. Overload Ambiguity

Overloads with null:

```java
send(String x)
send(byte[] x)
```

call:

```java
send(null);
```

ambiguous.

Boxing/varargs/generics make worse.

Design API so common calls obvious. Use distinct names when semantic operations differ.

---

# 109. Functional Core, Imperative Shell

Pure-ish core:

```java
OrderResult calculate(
    Order order,
    PricingPolicy policy)
```

no DB/network/clock hidden.

Imperative shell loads data, calls core, saves result.

This pattern improves testability and separates deterministic logic from effects.

Java does not need be “functional language” to benefit.

---

# 110. Streams không nên giấu control flow

Good:

```java
orders.stream()
      .filter(...)
      .map(...)
      .toList();
```

Bad:

```java
stream.map(x -> {
    database.save(x);
    metrics.increment();
    remote.call(x);
    return mutateGlobal(x);
})
```

Side effects inside lazy pipeline make timing/error/order obscure.

Imperative loop may be clearer.

---

# 111. Strategy, Factory, Decorator, Adapter, Proxy, Command, State

Modern Java often implements classic patterns with fewer classes.

Strategy can be lambda.

Factory can be static factory.

Decorator wraps interface.

Adapter isolates vendor.

Proxy intercepts calls.

Command can be `Runnable`/record command.

State can be sealed state types + transition methods.

Do not create pattern bureaucracy; understand intent/trade-off.

---

# 112. Dependency Inversion

Core defines:

```java
interface OrderRepository
interface PaymentGateway
```

Infrastructure depends inward by implementing.

Use case doesn't import JDBC/HTTP SDK.

Spring later wires adapters.

This is the strongest bridge from Java Core to Spring architecture.

---

# 113. Ports and Adapters

Application core ports represent capabilities it needs.

Inbound adapter: REST/CLI/message invokes use case.

Outbound adapters: DB/payment/email implement ports.

Framework is at edge.

This architecture is useful when boundaries/complexity justify, not mandatory for simple CRUD.

---

# 114. Repository and Unit of Work

Repository abstracts aggregate persistence operations.

Unit of Work groups changes in transaction.

JPA persistence context is one implementation style; JDBC service transaction another.

Don't make repository abstraction hide arbitrary remote/business operations.

---

# 115. Domain Events

Domain event says meaningful fact:

```text
OrderPlaced
PaymentApproved
```

In-process domain event can decouple local handlers.

But publication reliability differs from distributed broker event.

Don't confuse object event with durable message.

---

# 116. Idempotency

Operation executed twice should not duplicate business effect when design requires.

Payment:

```text
Idempotency-Key
```

Message consumer stores processed event ID or uses unique business constraint.

Retry without idempotency can duplicate side effects.

This is distributed correctness foundation.

---

# 117. At-Least-Once Delivery

Many brokers deliver at least once, meaning duplicate is normal.

Consumer must assume message may repeat.

Exactly-once marketing claims often have scoped semantics; end-to-end business side effects still need idempotency/transactions.

---

# 118. Outbox Pattern

Within local DB transaction:

```text
business row changes
+
outbox row
```

commit together.

Publisher later sends outbox to broker.

Crash/retry may duplicate publish, so consumer idempotent.

Outbox solves dual-write durability gap, not all distributed problems.

---

# 119. Saga / Compensation

Multiple services can't share simple local transaction.

Saga sequences local transactions + compensations.

Compensation is business action, not exact rollback.

Refund may itself fail and need retry/manual intervention.

Model process state explicitly.

---

# 120. Testing Behavior, not Implementation

A unit test should assert observable contract.

If test asserts private helper called exactly 3 times, harmless refactor breaks test.

Mocks are useful at effect boundaries but over-mocking couples tests to implementation.

Fake repository can test state transitions naturally.

---

# 121. Deterministic Tests

Control:

```text
Clock
random
UUID
environment
external services
threads
```

Inject dependencies/fakes.

Never use `Thread.sleep(500)` as primary concurrency synchronization if latch/future can express completion.

Flaky test is production-quality signal: timing assumptions may be wrong.

---

# 122. Contract Tests

If multiple repository implementations must share semantics, run same contract suite.

If HTTP vendor adapter must honor schema, test stub server contract.

Contract testing protects boundary, not internal method calls.

---

# 123. Concurrency Tests

Concurrency bugs probabilistic.

Use latches/barriers to orchestrate interleavings, repeated stress, and specialized tools like jcstress for JMM-level code.

A test passing 100 times does not mathematically prove lock-free algorithm correct.

Avoid custom concurrency primitives unless necessary.

---

# 124. Property-Based Testing Awareness

Instead of fixed examples only, generate many inputs and assert invariant.

Example money addition:

```text
a + zero == a
```

Parser round-trip.

Sorting output is ordered + permutation of input.

Libraries exist; concept useful even with manual generated tests.

---

# 125. Logging, Metrics, Traces

Logs = detailed events.

Metrics = aggregated numeric signals.

Traces = request/operation causality across components.

JFR = JVM runtime events/profile.

Production observability combines them.

Logging every request body is not observability strategy.

---

# 126. Structured Logging

Prefer fields:

```text
orderId
requestId
operation
status
durationMs
errorCode
```

over free text impossible to query.

Use logging framework later, but Java core code should pass contextual info through boundaries rather than global static mutable context.

---

# 127. Correlation ID

Unique request/operation ID helps link logs.

In distributed system, trace IDs often serve technical correlation.

Do not use trace ID as business idempotency key unless semantics align.

Context propagation must cross executor/HTTP boundaries intentionally.

---

# 128. Metric Cardinality

Tag:

```text
status=success
region=kr
```

bounded.

Tag:

```text
userId=millions values
```

explodes time series.

Metrics design is memory/cost/performance concern.

Keep high-cardinality IDs in logs/traces.

---

# 129. Resource Ownership

Function that creates resource should clearly transfer/retain ownership.

```java
InputStream open()
```

caller owns close if contract says so.

Method receiving stream should not close unless documented.

Ambiguous ownership causes leaks or premature close.

Use `AutoCloseable`/try-with-resources.

---

# 130. Shutdown Hook

```java
Runtime.getRuntime()
       .addShutdownHook(
           new Thread(
             this::shutdown));
```

can cleanup on normal JVM shutdown signals.

But not guaranteed on `kill -9`, crash or machine loss.

Durability cannot depend solely on shutdown hooks.

Frameworks like Spring provide lifecycle abstraction; concept remains.

---

# 131. Immutable Snapshot

Shared configuration/state can be represented immutable object and replaced atomically:

```java
volatile Config config;
```

Readers take snapshot reference; writer builds new Config then publish.

This reduces fine-grained locking compared mutating many fields.

Snapshot pattern useful for routing/config/cache metadata.

---

# 132. Cache is Data Consistency System

Cache decisions:

```text
key
TTL
max size
eviction
stale tolerance
source of truth
update/invalidation
multi-instance
```

Unbounded `ConcurrentHashMap` is not production cache.

Libraries like Caffeine offer eviction/metrics; distributed cache adds network/serialization.

But pattern semantics come first.

---

# 133. Cache Stampede

Popular entry expires; thousands requests load same DB value.

Mitigation single-flight/per-key synchronization, refresh-ahead, stale serving, TTL jitter.

If loader is under lock, ensure slow loader doesn't block unrelated keys.

---

# 134. Negative Caching

Repeated non-existent key can hammer DB.

Cache “not found” briefly if semantics allow.

But newly created data may remain invisible until negative TTL expires.

Trade consistency for load.

---

# 135. Time Correctness

Use `Instant` for exact timeline events.

Use `LocalDate` for birthday/business date.

Use `ZonedDateTime` when zone rules matter.

Store zone ID separately if future local scheduling matters.

Don't use server default timezone implicitly.

Inject `Clock` for logic/testing.

---

# 136. `nanoTime` vs `currentTimeMillis`

Measure elapsed duration:

```java
long start =
    System.nanoTime();

...
long elapsed =
    System.nanoTime() - start;
```

`nanoTime` monotonic-purpose, no epoch meaning.

`currentTimeMillis` wall-clock can jump due time corrections.

Don't store `nanoTime` as timestamp.

---

# 137. Money Correctness

Use BigDecimal from String/valueOf.

Define scale/rounding.

Compare numeric value via `compareTo` when domain ignores scale.

Better create `Money` type carrying Currency and policy.

Avoid double.

These aren't “financial best practices” only; they prevent deterministic data bugs.

---

# 138. Collections at Senior Level

Complexity table isn't enough.

`ArrayList` often beats LinkedList due cache locality.

Pre-size when large known capacity:

```java
new ArrayList<>(expected);
```

but don't over-allocate huge lists blindly.

EnumSet/EnumMap excellent for enum domains.

Java 21 Sequenced Collections improve first/last/reversed semantics.

---

# 139. Streams at Senior Level

Laziness + single-use + side-effect constraints matter.

Parallel stream shares common pool by default and may amplify blocking.

Custom Collector must satisfy identity/associativity/combiner contracts for parallel correctness.

Use stream for transformation, loop for stateful control when clearer.

---

# 140. Package by Feature vs Technical Layers

Feature package:

```text
order/
payment/
customer/
```

supports cohesive boundaries.

Package-private types prevent leakage.

Technical package global can encourage every service importing every repository.

No universal structure; enforce dependency direction.

JPMS optional stronger module boundary.

---

# 141. JDK Upgrade is Engineering Project

8→11 includes removed modules/APIs, new HTTP, GC/default changes.

11→17 includes strong encapsulation, language/runtime changes.

17→21 includes virtual threads, pattern matching, GC/runtime improvements.

21→25 includes another LTS and major runtime/language/library evolution.

Don't only change `<java.version>`.

Run tests, dependency compatibility, performance baseline, GC/JFR, startup, container memory and deprecated/internal API scans.

---

# 142. `--release`

Build target must match runtime platform.

Maven/Gradle configure compiler release.

Third-party dependencies may require newer runtime even if your source uses old syntax.

Inspect packaged artifact and CI runtime.

---

# 143. Java 25 and Java 26 Context

As of the update date of this document, Java 25 is the current LTS family and Java 26 is the current non-LTS family. Java 21, 17, 11 and 8 remain important enterprise baselines.

Learning strategy: understand Java 8 fundamentals, write modern code with 17/21 baseline awareness, and know 25/26 evolution. Don't force production upgrade before framework/vendor compatibility.

Master Supplement covers Scoped Values, FFM, Stream Gatherers, Class-File API and newer release deltas.

---

# 144. Code Review: Method

Ask whether name reflects intent, inputs/outputs have semantic types, null policy clear, side effects obvious, exceptions meaningful, blocking/timeout visible, transaction/concurrency context assumed.

A short method can still be bad if hidden remote call. A long method can be okay if linear algorithm is clearer than artificial fragmentation.

Review contracts, not line count.

---

# 145. Code Review: Class

Ask responsibility/cohesion, mutable state, thread safety, lifecycle, dependency count, visibility, invariants, equality.

If class needs 15 collaborators, maybe God service/use-case boundaries wrong.

If class has mutable shared fields but no synchronization/thread-confinement contract, risk.

---

# 146. Code Review: Concurrency

Identify shared mutable state.

What establishes happens-before?

What operation must be atomic?

Locks order?

Queue bounded?

Cancellation/interrupt?

Executor ownership?

Downstream capacity?

Without answers, concurrent code isn't “probably okay”.

---

# 147. Code Review: I/O

Who closes resource?

Charset?

Large data loaded whole memory?

Timeout?

Path traversal?

Partial read/write?

Retry/idempotency?

Error translation?

These questions catch production issues earlier than syntax review.

---

# 148. Code Review: Persistence

Transaction boundary?

Connection ownership?

PreparedStatement?

Query timeout?

Isolation?

Batch size?

Remote calls inside transaction?

Pool capacity?

These principles carry into Spring/JPA.

---

# 149. Boolean Parameter Explosion

```java
send(
    message,
    true,
    false,
    true);
```

impossible to read.

Use enum/options/command object/named methods.

But don't create builder for two clear booleans if names at call site already available through method split.

---

# 150. Primitive Obsession

IDs/currency/status/email as raw primitive/string everywhere cause argument mixing and repeated validation.

Introduce semantic types where concept matters.

Don't wrap every integer into class in trivial internal loop.

---

# 151. God Service

One service handles order, payment, inventory, email, reports, filesystem.

Changes unrelated collide.

Split by capability/use case and define ports.

Don't just create `Utils` and move methods; responsibility still needs owner.

---

# 152. Catch-Log-Rethrow Everywhere

Creates duplicate logs.

Either handle, translate/add context, or let propagate.

Log once where operation ownership/context complete.

Preserve cause.

---

# 153. Hidden Blocking

Method name:

```java
User getUser()
```

may call remote DB/HTTP and block seconds.

API/module docs/naming/context should make expensive boundaries visible.

Reactive/event-loop code especially sensitive to hidden blocking.

---

# 154. Unbounded Everything

Unbounded queue, cache, thread creation, retry, payload, result set all share one failure mode: overload converts into memory/latency collapse.

Bound resources.

Capacity is part of correctness.

---

# 155. Incident: CPU 100%

Collect JFR/profile before restart if possible.

Find hot stacks.

Check GC CPU, busy loops, regex, serialization, crypto, lock spin, compilation.

Thread count isn't enough.

Fix hottest evidence, not suspected framework.

---

# 156. Incident: Slow, CPU Low

Likely waiting.

Thread dumps/traces reveal:

```text
socket read
DB pool
DB lock
future.get
monitor
queue
disk
```

Check downstream latency/pool saturation.

Adding CPUs won't fix wait.

---

# 157. Incident: RSS grows but Heap looks fine

Possible:

```text
direct memory
thread stacks
metaspace
native library
JIT code cache
GC structures
```

Use NMT, thread count, direct buffer metrics, classloader stats.

Do not increase Xmx blindly; it may worsen container OOM.

---

# 158. Incident: Frequent Full GC

Ask why old/live set high.

Heap too small?

Leak/retention?

Allocation burst?

Humongous objects?

Explicit System.gc?

Metadata pressure?

GC logs/JFR/heap dump provide evidence.

Changing collector without understanding live set may only change symptom.

---

# 159. Incident: Thread Count grows

Could be executor/thread leak, one-thread-per-request platform model under overload, scheduler creation, client library leak.

With virtual threads, high virtual-thread count may be expected; distinguish platform vs virtual and what they're waiting on.

Ownership/lifecycle review.

---

# 160. Java 21 Integration

Pattern switch and record patterns encourage data-oriented modeling for closed structures.

Sequenced collections simplify order APIs.

Virtual threads simplify blocking concurrency.

Don't force all features into code. Use when they reduce accidental complexity.

---

# 161. Preview Features

Preview means API/language may change and compile/run requires flags tied to version.

Structured Concurrency/Scoped Values had preview/incubator evolution across 21–24 before Scoped Values final in 25.

Production baseline should explicitly decide whether preview allowed.

Never describe preview as stable final API.

---

# 162. “Always use interface” is wrong

Interface useful for abstraction/extension/boundary.

Private helper class with one implementation and no meaningful contract may not need.

Too many interfaces create navigation noise.

Choose based on substitution/boundary.

---

# 163. “Never use static” is wrong

Pure utility/static factory/constants are good.

Static mutable global dependencies/state are risky.

Judge hidden state/lifecycle, not keyword.

---

# 164. “Composition always better than inheritance” is too absolute

Composition often more flexible.

Inheritance works for true stable is-a hierarchy/framework template.

Use Liskov substitutability and change pressure.

---

# 165. “Exceptions are slow”

Constructing/throwing exceptions with stack traces can be expensive, so don't use exceptions for hot normal control flow.

But don't return magic error codes everywhere to avoid hypothetical cost.

Correct error semantics first; profile.

---

# 166. “Streams are slow”

Streams can have overhead and boxing, but often JIT optimize well enough.

If pipeline clearer and not hot bottleneck, use it.

For tight performance-critical loops, benchmark loop vs stream.

No slogan.

---

# 167. “Virtual threads replace async”

Virtual threads make blocking style scale.

Async/reactive remains useful for streaming/backpressure/composition APIs and certain architectures.

They solve different complexity dimensions.

---

# 168. Senior Practice Project

Build plain Java production-style core before Spring.

Domain: orders/payments/inventory.

Use value objects, sealed result types, repository/payment ports.

Implement JDBC repository with transactions/query timeouts and connection pool library if allowed.

Implement Java HTTP Client payment adapter with deadline/retry/idempotency.

Use virtual threads for blocking request simulation plus semaphore bulkhead.

Implement transactional outbox table + publisher simulation.

Add JFR profiling and GC logging under load.

Write unit/contract/concurrency tests.

The project should make every resource owner explicit.

---

# 169. Spring Readiness Gate

Before Spring, you should understand DI/ports without container, proxy concept via Dynamic Proxy, transaction boundary with JDBC, annotations as metadata, reflection/class loading, thread safety/JMM and executor lifecycle.

Then Spring annotations become convenient declarations over concepts you already understand.

`@Transactional` maps to transaction interceptor/manager.

`@Async` maps to executor/proxy.

`@Repository` maps persistence adapter.

`@ConfigurationProperties` maps typed configuration.

Without Java Core mental model, Spring becomes memorization.

---

# 170. Kết luận Part 3

A Senior Java engineer nhìn application như hệ thống resources và contracts:

```text
Input
→ validation / typed model
→ use case
→ concurrency/transaction boundaries
→ I/O resources
→ output / side effects
```

JVM view:

```text
class loading
→ bytecode
→ JIT
→ threads / stacks
→ heap + native memory
→ GC
→ OS resources
```

Production view:

```text
load
→ queue/pool
→ latency
→ downstream capacity
→ failures/retries
→ observability
```

Nếu bạn có thể trace cả ba lớp cùng lúc, bạn đã vượt khỏi “biết Java syntax” và bắt đầu engineering bằng Java.

Master Supplement tiếp theo không nhằm thêm nhiều best practices. Nó sẽ bổ sung các vùng low-level/library-author hiện chưa cover đủ như VarHandle memory ordering, LockSupport/AQS, Spliterator/Gatherers/Flow, reference queues/Cleaner, NIO Selector, FFM/JNI, Java Agents/Instrumentation, Class-File API, MethodHandle sâu, object layout, advanced GC/JFR/JMX và Java 22–26 evolution.

---

# References for version-sensitive topics

Oracle Java SE Support Roadmap:
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle JDK 25 release notes:
https://www.oracle.com/java/technologies/javase/25all-relnotes.html

Oracle JDK 26 release notes:
https://www.oracle.com/java/technologies/javase/26all-relnotes.html

OpenJDK JEP index:
https://openjdk.org/jeps/0

Java Language Specification:
https://docs.oracle.com/javase/specs/

Java API Documentation:
https://docs.oracle.com/en/java/javase/

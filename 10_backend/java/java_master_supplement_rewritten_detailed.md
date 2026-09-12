# Java Core — Master Supplement — Rewritten Detailed
## Low-level Runtime, Library Engineering, Modern JDK và những phần còn thiếu để tiến tới “Master Java”

> Tài liệu này là phần thứ tư sau **Beginner → Intermediate → Senior**. Nó không lặp lại cú pháp Java, Collections, Stream cơ bản, JDBC căn bản, JMM căn bản hay JVM/GC overview đã có ở ba file trước. Mục tiêu ở đây là đi vào những vùng mà một Senior application developer có thể chưa cần dùng hằng ngày nhưng một người muốn hiểu Java ở level “master” cần biết: low-level concurrency primitives, class-file/runtime machinery, native interoperability, reference processing, selector/event-loop, library extension points, build/runtime tooling, API compatibility và evolution của JDK hiện đại.
>
> Các phần “Senior Note”, “Language Idiom”, “Programming Pattern”, “Design Pattern” không được tách thành các box lặp đi lặp lại. Khi một pattern hoặc nguyên tắc quan trọng, nó được giải thích trực tiếp tại chỗ cùng với nguyên nhân, failure mode và trade-off. Mục tiêu là đọc như một cuốn sách học, không phải một cheat sheet.
>
> Baseline version của supplement này là **Java 25 LTS** với awareness tới **Java 26**, là release mới nhất tại thời điểm cập nhật. Java 26 là non-LTS; Java 25 là LTS hiện tại. Các preview/incubator APIs được đánh dấu rõ để tránh nhầm với API final.

---

# 1. “Master Java” thực sự có nghĩa gì?

Master Java không có nghĩa là thuộc hết `java.*` hoặc nhớ mọi option của JVM. JDK quá lớn và thay đổi theo từng release. Người thực sự giỏi Java có ba năng lực quan trọng hơn trí nhớ API.

Thứ nhất, họ hiểu **semantic model**. Khi thấy một API mới, họ hỏi ownership, mutability, concurrency, lifecycle, error và compatibility contracts. Thứ hai, họ hiểu **runtime** đủ sâu để giải thích hiện tượng production: class nào được load bởi loader nào, object nào đang giữ memory, thread đang parked hay blocked, JIT có thể inline/deoptimize ra sao, GC barrier có vai trò gì. Thứ ba, họ biết **tìm bằng chứng** trong JLS, JVMS, Javadoc, OpenJDK source, JEP, JFR, `jcmd`, heap dump và class files thay vì đoán.

Do đó supplement này chủ yếu dạy cách “mở nắp” Java. Nhiều API ở đây bạn có thể không bao giờ dùng trực tiếp trong CRUD backend, nhưng hiểu chúng giúp bạn đọc source Spring, Netty, Reactor, Hibernate, Kafka client, logging libraries hoặc JDK itself mà không thấy chúng như black box.

---

# 2. Version strategy: Java 25 LTS, Java 26 và vì sao không nên dừng ở Java 21

Java 8, 11, 17, 21 và 25 là các LTS generations quan trọng. Java 25 là LTS hiện tại; Java 26 là feature release hiện tại nhưng không phải LTS. Khi vận hành enterprise, bạn có thể vẫn ở 17 hoặc 21 vì framework/vendor policy. Khi học, bạn nên biết những gì đã final ở 25 và những gì mới/preview ở 26 để không bị mắc kẹt trong mental model cũ.

Điều quan trọng là phân biệt **language feature**, **library API**, **JVM/runtime feature** và **tooling feature**. Ví dụ Scoped Values là library/runtime API final ở Java 25. Stream Gatherers trở thành standard API ở Java 24. Foreign Function & Memory API final ở Java 22. Class-File API trở thành standard ở Java 24. HTTP/3 support cho `HttpClient` xuất hiện trong Java 26. Structured Concurrency ở Java 26 vẫn là preview, nên exact API có thể tiếp tục đổi.

Khi đọc một bài viết, hãy hỏi “feature này final ở release nào?” trước khi dùng trong library production. Preview API thường yêu cầu `--enable-preview`, gắn với đúng release và không mang compatibility guarantee như standard API.

---

# 3. VarHandle: khi `volatile` và Atomic classes chưa đủ

`VarHandle` là low-level typed reference tới variable-like storage location. Nó cho phép đọc, ghi và atomic update với **memory ordering semantics** rõ hơn `volatile` field đơn thuần. Đây là API chính thức thay thế nhiều use case trước đây phải dựa vào `sun.misc.Unsafe`.

Giả sử class có field:

```java
final class Counter {
    volatile int value;
}
```

Bạn có thể lookup `VarHandle`:

```java
private static final VarHandle VALUE;

static {
    try {
        VALUE = MethodHandles.lookup()
                .findVarHandle(
                    Counter.class,
                    "value",
                    int.class);
    } catch (ReflectiveOperationException e) {
        throw new ExceptionInInitializerError(e);
    }
}
```

Sau đó:

```java
int current =
    (int) VALUE.getVolatile(counter);

VALUE.setVolatile(counter, 10);
```

Điểm đáng học không phải syntax lookup, mà là **access modes**. `get`/`set` có plain semantics. `getOpaque`/`setOpaque` cung cấp weaker ordering. `getAcquire` và `setRelease` tạo acquire/release ordering. `getVolatile`/`setVolatile` cho strongest volatile-style ordering. Ngoài ra còn CAS, compare-and-exchange, get-and-add và bitwise atomics tùy type.

Nếu bạn đang viết application service bình thường, dùng `volatile`, `AtomicInteger`, `AtomicReference` hoặc locks dễ đúng hơn. `VarHandle` hợp khi xây concurrent library/data structure và cần kiểm soát chính xác memory ordering để tránh cost không cần thiết.

---

# 4. Acquire/Release/Opaque: memory ordering không chỉ có “volatile hoặc không”

Một lỗi phổ biến là nghĩ Java memory model chỉ có hai mức: normal field và volatile field. Thực tế low-level APIs có ordering strength khác nhau.

**Plain** access gần ordinary field access, không tạo synchronization ordering đặc biệt.

**Opaque** đảm bảo một mức coherence tối thiểu cho cùng variable nhưng cho phép reorder rộng hơn volatile. Nó hữu ích cho low-level progress/status information nơi bạn không cần publish cả object graph.

**Release write** đảm bảo writes trước nó không bị reorder đi sau release. **Acquire read** đảm bảo reads/writes sau nó không bị reorder đi trước acquire. Khi một release store được paired với acquire load quan sát giá trị đó, bạn có publication ordering giống một one-way handoff.

**Volatile** mạnh hơn, tạo total synchronization order theo JMM cho volatile actions.

Bạn không nên chọn weaker mode chỉ vì “nhanh hơn”. Chọn mode yếu hơn nghĩa bạn đang viết proof về memory ordering. Nếu proof sai, bug có thể chỉ xuất hiện trên architecture/JIT/load nhất định. Đây là territory của concurrent library authors.

---

# 5. Compare-and-set qua VarHandle

CAS:

```java
boolean updated =
    VALUE.compareAndSet(
        counter,
        expected,
        update);
```

cho phép atomic state transition không dùng monitor lock.

Một lock-free state machine có thể dùng immutable state:

```java
while (true) {
    State oldState =
        (State) STATE.getVolatile(this);

    State newState =
        oldState.apply(command);

    if (STATE.compareAndSet(
            this,
            oldState,
            newState)) {
        return;
    }
}
```

Điểm khó nằm ở invariants, retry behavior, ABA và progress guarantees. CAS loop không tự động tốt hơn lock. Nếu contention cao, nhiều threads có thể spin/retry và đốt CPU. Nếu transition expensive, recomputation cost cũng lớn. High-level lock hoặc `AtomicReference` thường rõ hơn.

Một library tốt sẽ đóng `VarHandle` bên trong class và expose API an toàn; caller không cần hiểu memory ordering của từng field. Đây là nguyên tắc quan trọng của low-level library design: **encapsulate memory semantics**.

---

# 6. LockSupport: primitive phía dưới nhiều synchronizers

`LockSupport` cung cấp:

```java
LockSupport.park();
LockSupport.unpark(thread);
```

Nó là primitive parking/unparking được dùng trong nhiều synchronizers của `java.util.concurrent`.

Mental model quan trọng là **permit**. Một thread có tối đa conceptually một permit. `unpark(thread)` làm permit available; nếu thread sau đó `park()`, permit được consume và thread có thể tiếp tục ngay. Nếu `park()` xảy ra trước, thread block cho tới unpark, interruption hoặc spurious return.

Điều này khác `Object.wait()` ở chỗ không cần monitor protocol như `synchronized` + `notify`, và `unpark` trước `park` không bị “mất signal” theo cùng cách.

Tuy nhiên `park()` **có thể return spuriously**, nên luôn phải nằm trong condition loop:

```java
while (!condition()) {
    LockSupport.park();
}
```

Đừng dùng `LockSupport` để viết queue/synchronizer application-level nếu `BlockingQueue`, Semaphore, Lock hoặc latch đã phù hợp. Nó là building block cho library internals.

---

# 7. AbstractQueuedSynchronizer: nền của nhiều locks trong JDK

`AbstractQueuedSynchronizer`, thường gọi AQS, là framework để xây blocking synchronizers. `ReentrantLock`, `Semaphore`, `CountDownLatch` và nhiều utilities dựa trên hoặc liên quan pattern này.

AQS quản lý một integer state và một queue của waiting nodes/threads. Subclass định nghĩa ý nghĩa state bằng các methods như conceptually `tryAcquire`, `tryRelease`, `tryAcquireShared`, `tryReleaseShared`. AQS lo phần khó của queueing, parking, wake-up và cancellation.

Trong **exclusive mode**, chỉ một owner hoặc một limited ownership state được acquire, như lock. Trong **shared mode**, nhiều threads có thể proceed khi shared permits/state cho phép, như semaphore/latch.

Bạn không cần subclass AQS để viết backend application. Nhưng nếu đọc JDK concurrent source hoặc một custom library, hiểu AQS giúp bạn thấy `ReentrantLock.lock()` không phải magic: fast path thử acquire state, slow path enqueue, park, wake và retry.

---

# 8. Reentrancy và vì sao library APIs phải document nó

Một synchronizer **reentrant** cho phép thread đang giữ lock acquire lại same lock mà không deadlock chính nó. `ReentrantLock` và Java intrinsic monitors có reentrant behavior.

Reentrancy có lợi khi public method giữ lock gọi private/helper method cũng cần same invariant.

Nhưng reentrancy làm reasoning phức tạp nếu unknown callback chạy trong locked section. Callback có thể gọi ngược vào object, thay state ở một point bạn không dự kiến.

Một API thread-safe nên document rằng callbacks có được gọi dưới lock không. Tốt hơn, nhiều library designs copy data/prepare callback rồi release lock trước khi gọi unknown code, miễn invariant cho phép.

“Không gọi unknown code dưới lock” là một nguyên tắc cực mạnh vì unknown code có thể block, acquire locks khác, throw, reenter hoặc call remote I/O.

---

# 9. ThreadLocal internals và lý do leak trong thread pool

`ThreadLocal<T>` không phải một global map từ thread ID tới value do ThreadLocal object giữ. Mỗi `Thread` conceptually có một internal ThreadLocalMap; ThreadLocal object đóng vai trò key.

Điều này tạo lifecycle trap trong thread pool. Worker thread sống rất lâu:

```text
request A
→ ThreadLocal.set(userA)
→ task kết thúc nhưng không remove
→ worker thread vẫn sống
→ value vẫn bị retain
```

Request B có thể reuse thread và thấy stale context nếu code không overwrite đúng, đồng thời memory được giữ lâu.

Pattern:

```java
try {
    CONTEXT.set(context);
    work();
} finally {
    CONTEXT.remove();
}
```

Nếu ThreadLocal chứa object graph lớn, leak càng nghiêm trọng.

Một subtle detail là ThreadLocalMap dùng weak references cho keys nhưng values có thể vẫn được giữ cho tới cleanup khi key đã GC. Vì vậy “ThreadLocal key là weak nên không leak” là hiểu sai.

---

# 10. InheritableThreadLocal và vì sao nó không giải context propagation hiện đại

`InheritableThreadLocal` copy/inherit value khi child thread được tạo. Điều này có vẻ tiện cho request context, nhưng thread pools reuse threads nên “child creation” không trùng task boundary. Context có thể không update như mong đợi.

Virtual threads tạo nhiều threads mới hơn nên inheritance semantics khác thread pool reuse, nhưng immutable scoped context vẫn là model dễ reason hơn.

Trong framework ecosystem, tracing/security/MDC có dedicated propagation mechanisms. Không nên tự xây global request context bằng `InheritableThreadLocal` rồi hy vọng mọi executor/reactive pipeline đúng.

---

# 11. ScopedValue: immutable scoped context của Java 25

Scoped Values final ở Java 25. Ý tưởng là share immutable contextual value tới callees trong một dynamic scope mà không cần mutable per-thread slot như ThreadLocal.

Conceptual example:

```java
static final ScopedValue<UserContext>
    USER =
        ScopedValue.newInstance();

ScopedValue.where(
        USER,
        context)
    .run(() -> {
        serviceCall();
    });
```

Bên trong scope:

```java
UserContext context =
    USER.get();
```

Điểm mạnh là binding có lexical/dynamic scope rõ. Sau khi scope kết thúc, binding biến mất. Caller không “quên remove” như ThreadLocal.

ScopedValue phù hợp read-only context như request ID, security identity, tracing metadata, tenant context, đặc biệt khi dùng cùng virtual threads và structured concurrency.

Nó không phải replacement cho ordinary method parameters mọi nơi. Nếu dependency là business data cần rõ trong API, vẫn truyền parameter. ScopedValue hợp contextual data cross-cutting.

---

# 12. ScopedValue vs ThreadLocal

ThreadLocal phù hợp mutable thread-local state và legacy APIs, nhưng lifecycle dễ mơ hồ.

ScopedValue hướng tới immutable contextual binding. Child execution có thể inherit context theo structured mechanisms và binding không thể tùy tiện mutate.

Nếu bạn cần một counter mutable local thread, ScopedValue không phải tool tương đương. Nếu bạn cần “request context đọc ở many layers” mà không muốn mutable hidden state, ScopedValue có mental model tốt hơn.

Một master-level lesson là không biến context mechanism thành dependency injection substitute. User ID có thể là contextual ở logging/security layer nhưng command handler business cần user ID để quyết định permission thì explicit parameter hoặc security abstraction có thể rõ hơn.

---

# 13. ForkJoinPool và Work Stealing

`ForkJoinPool` được thiết kế cho task decomposition, đặc biệt CPU-bound recursive computations.

Worker có local deque. Khi worker hết việc, nó **steal** task từ worker khác. Work stealing giúp balance load với less centralized contention.

`RecursiveTask<V>` trả result:

```java
final class SumTask
        extends RecursiveTask<Long> {

    protected Long compute() {
        if (smallEnough()) {
            return sequentialSum();
        }

        SumTask left = splitLeft();
        SumTask right = splitRight();

        left.fork();

        long rightResult =
            right.compute();

        return left.join()
             + rightResult;
    }
}
```

Granularity cực quan trọng. Split quá nhỏ làm scheduling overhead lớn. Split quá lớn làm parallelism kém.

---

# 14. Common ForkJoinPool và hidden shared capacity

Parallel streams và một số CompletableFuture async operations có thể dùng common pool.

Điều này tạo hidden coupling: feature A chạy CPU-heavy parallel stream và feature B dùng `CompletableFuture.supplyAsync()` không executor; chúng tranh same pool.

Blocking I/O trong common ForkJoinPool có thể giảm available workers. `ForkJoinPool.ManagedBlocker` tồn tại cho advanced cases để pool biết blocking và có thể compensate workers, nhưng application code thường nên tránh dùng common pool cho uncontrolled blocking.

Nếu capacity/failure isolation quan trọng, tạo explicit executor.

---

# 15. Spliterator: engine traversal phía dưới Stream

`Spliterator<T>` có hai responsibilities: traverse elements và split source thành parts để parallel processing.

Core methods conceptually:

```java
boolean tryAdvance(
    Consumer<? super T> action);

Spliterator<T> trySplit();

long estimateSize();

int characteristics();
```

`trySplit()` trả một spliterator khác đại diện một portion, trong khi original giữ phần còn lại. Parallel stream dùng cơ chế này để partition work.

ArrayList có thể split rất tốt theo index ranges. Linked structure khó split cân bằng hơn.

Nếu bạn viết custom data source và muốn stream parallel hiệu quả, custom Spliterator quan trọng hơn custom Stream class.

---

# 16. Spliterator characteristics

Characteristics mô tả contract data source:

```text
ORDERED
DISTINCT
SORTED
SIZED
NONNULL
IMMUTABLE
CONCURRENT
SUBSIZED
```

Stream runtime có thể optimize dựa information này.

Đừng khai sai. Nếu bạn claim `SIZED` nhưng estimate không chính xác theo contract, downstream optimizations có thể sai. Nếu claim `SORTED`, comparator/order semantics phải đúng.

Một pattern chung trong library engineering là metadata càng mạnh càng cho runtime nhiều optimization, nhưng metadata sai nguy hiểm hơn metadata yếu.

---

# 17. Stream Gatherers: custom intermediate operation đã thành standard ở Java 24

Trước Gatherers, Stream API có các intermediate operations fixed như map/filter/flatMap. Những transformations như sliding window, incremental scan hoặc stateful custom intermediate stage khá khó biểu diễn mà không collect rồi xử lý ngoài stream.

`Gatherer` cho phép custom intermediate transformation với lifecycle/state/integration semantics. JDK cung cấp `Gatherers` utility.

Fixed windows:

```java
stream.gather(
    Gatherers.windowFixed(3))
```

input:

```text
A B C D E F G
```

conceptual output:

```text
[A B C]
[D E F]
[G]
```

Sliding window size 3:

```text
[A B C]
[B C D]
[C D E]
...
```

---

# 18. `scan`, `fold` và `mapConcurrent`

`Gatherers.scan` thực hiện prefix/incremental accumulation. Nếu input `1,2,3`, scan sum có thể emit `1,3,6`.

`fold` reduction-like nhưng có thể hỗ trợ ordered transformation scenarios không có natural combiner.

`mapConcurrent(maxConcurrency, mapper)` thực hiện mapping concurrently với configured max concurrency, dùng virtual threads trong JDK implementation hiện tại. Đây là điểm quan trọng: API concurrency có **bounded maxConcurrency** chứ không fan-out vô hạn.

Bạn vẫn phải nghĩ downstream capacity. `mapConcurrent(1000, remoteCall)` có thể đánh chết service nếu vendor chỉ cho 20 concurrent requests.

Gatherers là ví dụ rất đẹp về JDK evolution: khi một abstraction lặp lại đủ nhiều trong ecosystem, platform có thể chuẩn hóa nó.

---

# 19. `java.util.concurrent.Flow`: Reactive Streams contract trong JDK

Flow định nghĩa bốn core interfaces:

```text
Publisher<T>
Subscriber<T>
Subscription
Processor<T,R>
```

Publisher phát data. Subscriber nhận data. Subscription nối hai bên và carry demand/cancellation. Processor vừa subscriber vừa publisher.

Điểm quan trọng nhất là **backpressure**. Subscriber gọi:

```java
subscription.request(n);
```

nói nó sẵn sàng nhận thêm n items.

Publisher không được xem subscriber như sink vô hạn.

---

# 20. Subscriber lifecycle

Subscriber nhận:

```text
onSubscribe(subscription)
onNext(item)...
onError(error)
hoặc
onComplete()
```

`onSubscribe` phải đến trước data.

Sau terminal signal (`onError` hoặc `onComplete`), stream kết thúc.

`request` demand thường phải positive; violations có semantics theo reactive streams rules.

Reactive protocol là asynchronous contract, không chỉ callback API.

---

# 21. SubmissionPublisher

JDK có `SubmissionPublisher<T>` làm basic Publisher implementation.

Nó hữu ích để học/demo/in-process publishing nhưng không phải replacement cho Reactor/Kafka/broker.

Bạn vẫn phải quan tâm buffer, executor, slow subscribers và drop/submit semantics.

Nếu consumer chậm, publisher buffer có giới hạn/cost. Reactive Streams không làm memory/backpressure problem biến mất; nó cung cấp protocol để quản lý nó.

---

# 22. Strong, Weak, Soft và Phantom References

Normal reference là **strong reference**. Object reachable strongly thì không được GC.

`WeakReference<T>` không giữ object sống. Nếu chỉ còn weak references, GC có thể reclaim object và `get()` trở null.

Weak references phù hợp canonicalization/metadata mappings trong một số cases. `WeakHashMap` dùng weak keys, useful khi entry lifetime gắn với key reachability.

Nhưng weak cache không phải general-purpose cache policy. GC pressure quyết định collection, không business TTL.

---

# 23. SoftReference: tại sao không nên dùng làm cache mặc định

Soft references historically được giữ lâu hơn weak references tùy memory pressure. Điều này từng được dùng làm memory-sensitive cache.

Vấn đề là eviction policy bị giao cho GC và khó predict. Cache production cần max size, TTL, metrics, hit rate và predictable behavior.

Dùng Caffeine/explicit cache library tốt hơn SoftReference cho business cache.

SoftReference vẫn quan trọng để hiểu reference processing và legacy code.

---

# 24. PhantomReference và ReferenceQueue

PhantomReference không cho retrieve referent bằng `get()`; mục tiêu là được notified sau khi object trở phantom reachable để quản lý post-mortem/native resource bookkeeping.

Typical setup:

```java
ReferenceQueue<Resource> queue =
    new ReferenceQueue<>();

PhantomReference<Resource> ref =
    new PhantomReference<>(
        resource,
        queue);
```

Bạn phải giữ PhantomReference object itself reachable để nhận queue notification.

ReferenceQueue cho bạn biết reference object đã được enqueued theo reference processing lifecycle.

Đây là low-level technique. Explicit resource close vẫn tốt hơn vì deterministic.

---

# 25. Cleaner: safety net, không phải lifecycle chính

`Cleaner` cung cấp cleanup action khi object phantom reachable.

Pattern quan trọng là cleanup action không được capture referent mạnh, nếu không object sẽ không bao giờ unreachable.

Concept:

```java
final class NativeBuffer
        implements AutoCloseable {

    private static final Cleaner CLEANER =
        Cleaner.create();

    private final State state;
    private final Cleaner.Cleanable cleanable;

    NativeBuffer(...) {
        state = new State(...);
        cleanable =
            CLEANER.register(
                this,
                state);
    }

    public void close() {
        cleanable.clean();
    }
}
```

`close()` vẫn là primary deterministic path. Cleaner là fallback nếu caller quên close.

Nếu resource critical như file descriptor/socket/native allocation, relying only on GC timing có thể exhaust resource trước GC chạy.

---

# 26. NIO SocketChannel

Classic `Socket` có blocking stream model. NIO `SocketChannel` hỗ trợ channel APIs và có thể cấu hình blocking/non-blocking.

```java
SocketChannel channel =
    SocketChannel.open();

channel.connect(
    new InetSocketAddress(
        host,
        port));
```

Read/write dùng `ByteBuffer`.

Trong blocking mode, call chờ I/O giống normal blocking model. Trong non-blocking mode, read/write/connect có thể return mà operation chưa hoàn tất.

Non-blocking không có nghĩa “async magically faster”; nó đổi execution model để một thread multiplex nhiều connections.

---

# 27. ServerSocketChannel

Server accepts connections:

```java
ServerSocketChannel server =
    ServerSocketChannel.open();

server.bind(
    new InetSocketAddress(port));
```

Blocking:

```java
SocketChannel client =
    server.accept();
```

Non-blocking:

```java
server.configureBlocking(false);
```

`accept()` có thể return null nếu chưa có connection.

Để tránh polling loop, bạn dùng `Selector`.

---

# 28. Selector và Event Loop

Selector multiplex nhiều selectable channels trên một thread.

Register interests:

```text
OP_ACCEPT
OP_CONNECT
OP_READ
OP_WRITE
```

Event loop concept:

```text
selector.select()
→ selected keys
→ handle accept/read/write/connect
→ update interests
→ repeat
```

Một thread có thể manage thousands connections nếu handlers không block.

Đây là nền mental model của Netty/NIO servers.

---

# 29. SelectionKey và partial I/O

Network write không guarantee toàn buffer được gửi trong một call.

```java
channel.write(buffer);
```

có thể write một phần; `buffer.hasRemaining()` vẫn true. Bạn phải giữ state và đăng ký OP_WRITE để tiếp tục sau.

Read cũng có thể nhận partial protocol frame.

Đây là lý do event-loop networking cần per-connection state machine và buffers.

Nếu handler gọi DB/blocking HTTP 500 ms trên selector thread, toàn bộ connections khác bị stall. Event-loop rule là **never block the event loop**.

---

# 30. InterestOps và busy-spin bug

Nếu luôn register `OP_WRITE`, socket thường luôn writable, selector có thể wake liên tục và CPU 100%.

Chỉ request OP_WRITE khi bạn có pending data và previous write không hoàn tất; remove interest khi buffer drained.

Đây là một classic NIO event-loop bug và cho thấy readiness notification phải gắn với state machine.

---

# 31. Asynchronous Channels

JDK có `AsynchronousSocketChannel`, `AsynchronousServerSocketChannel`, `AsynchronousFileChannel`.

API dùng Future hoặc CompletionHandler style.

Ví dụ read:

```java
channel.read(
    buffer,
    attachment,
    new CompletionHandler<>() {
        public void completed(
                Integer bytes,
                State state) {
            ...
        }

        public void failed(
                Throwable error,
                State state) {
            ...
        }
    });
```

Model này khác selector event loop nhưng implementation/OS support có thể still use thread pools/platform mechanisms.

Virtual threads đã làm blocking-style networking hấp dẫn hơn cho many cases. AsynchronousChannel vẫn cần biết để đọc legacy/high-performance code.

---

# 32. WatchService

`WatchService` monitor filesystem events.

```java
WatchService watcher =
    FileSystems.getDefault()
        .newWatchService();

path.register(
    watcher,
    ENTRY_CREATE,
    ENTRY_MODIFY,
    ENTRY_DELETE);
```

Take keys/events rồi reset key.

Filesystem event systems có coalescing, overflow và platform-specific behavior. Không assume every change maps exactly one event.

Nếu correctness critical, event chỉ nên trigger rescan/reconciliation.

---

# 33. ZIP/GZIP/JAR APIs và Zip Slip

GZIP là compression stream cho single stream:

```java
GZIPInputStream
GZIPOutputStream
```

ZIP là archive nhiều entries:

```java
ZipInputStream
ZipOutputStream
ZipFile
```

JAR là ZIP với Java metadata/conventions.

Khi extract ZIP từ untrusted source, entry name có thể:

```text
../../etc/passwd
```

Nếu resolve trực tiếp:

```java
target.resolve(entry.getName())
```

attacker có thể escape output directory.

Normalize rồi verify resolved path vẫn nằm trong target root. Đây là Zip Slip defense.

---

# 34. ProcessBuilder và child process management

Run external command:

```java
Process process =
    new ProcessBuilder(
        "git",
        "status")
        .start();
```

Child process có stdin/stdout/stderr pipes.

Nếu child ghi nhiều stdout/stderr và parent không drain, pipe buffer có thể full và child block. Parent meanwhile `waitFor()` tạo deadlock-like hang.

Use `redirectErrorStream(true)`, redirect files hoặc consume both streams concurrently.

Always consider timeout:

```java
process.waitFor(
    10,
    TimeUnit.SECONDS);
```

Then terminate if required.

---

# 35. ProcessHandle

`ProcessHandle` cho inspect process ID, parent/children, info, liveness và termination.

```java
ProcessHandle.current().pid();
```

Useful tooling/launcher/supervisor code.

Process lifecycle is OS resource boundary. Child process có thể spawn grandchildren; killing parent không luôn cleanup tree automatically. Cross-platform process management cần careful semantics.

---

# 36. RandomGenerator API

Java 17 đưa abstraction `RandomGenerator` và families.

Bạn có thể request algorithm:

```java
RandomGenerator rng =
    RandomGenerator.getDefault();
```

JDK có generators cho different statistical/performance/parallel requirements.

`ThreadLocalRandom` hợp thread-concurrent non-security random.

`SplittableRandom`/splittable generators phù hợp parallel streams/simulation.

`SecureRandom` vẫn dành cryptographic security.

Đừng chọn algorithm bằng benchmark duy nhất; requirement là reproducibility, parallel splitting, statistical quality hay security?

---

# 37. Unicode: `char` không phải “một ký tự”

Java `char` là 16-bit UTF-16 code unit. Một Unicode code point ngoài BMP cần surrogate pair, tức hai chars.

```java
String text = "😀";
text.length(); // 2
```

User thấy một emoji nhưng length 2.

Đếm code points:

```java
int count =
    text.codePointCount(
        0,
        text.length());
```

Iterate:

```java
text.codePoints()
```

Nếu xử lý identifiers/user-visible text/international names, đừng assume `charAt(i)` là complete character.

Grapheme cluster còn phức tạp hơn code point vì combining marks/emoji sequences; JDK basic code-point APIs không giải quyết toàn bộ user-perceived characters.

---

# 38. Unicode Normalization

Visual-similar strings có thể có code point sequences khác.

Ví dụ accented character có thể là precomposed code point hoặc base + combining mark.

Use:

```java
Normalizer.normalize(
    text,
    Normalizer.Form.NFC);
```

khi protocol/domain cần canonical form.

Nhưng normalization policy phải ở boundary và consistent. Không blindly normalize passwords/opaque tokens nơi exact bytes matter.

Security còn có Unicode confusable/homoglyph issues mà normalization không solve hết.

---

# 39. Collator và locale-aware ordering

`String.compareTo` so Unicode code units lexicographically, không phải language-specific collation.

`Collator` hỗ trợ locale-aware comparison:

```java
Collator collator =
    Collator.getInstance(
        Locale.KOREAN);
```

Useful sorting human names/text.

Database collation và Java Collator có thể khác, nên pagination/order between DB and Java must be designed consistently.

---

# 40. Native Java Serialization internals

A Serializable class có stream class descriptor và `serialVersionUID`.

Nếu bạn không declare, JVM computes UID từ class details. Seemingly harmless class change có thể đổi UID và break deserialize old data.

Explicit:

```java
private static final long
    serialVersionUID = 1L;
```

không magically make changes compatible; nó chỉ giữ version identifier. Nếu fields/types/invariants đổi, custom migration vẫn cần.

Methods như `writeObject`, `readObject`, `readResolve`, `writeReplace` customize behavior và tăng attack surface/complexity.

Native serialization nên được xem là legacy/closed-trusted mechanism, không default external format.

---

# 41. `transient` và `Externalizable`

`transient` field không được default serialization ghi.

Có thể dùng cho derived/cache/sensitive state, nhưng deserialized object phải restore invariant.

`Externalizable` cho full control `writeExternal/readExternal`, yêu cầu public no-arg constructor semantics và rất manual.

Nếu bạn đang thiết kế new wire/storage protocol, schema-oriented formats thường dễ version/manage hơn native Java serialization.

---

# 42. Java Cryptography Architecture: Provider model

JCA/JCE APIs thường request algorithm by name:

```java
MessageDigest.getInstance(
    "SHA-256");

Cipher.getInstance(
    "AES/GCM/NoPadding");
```

JVM chọn implementation từ registered `Provider`s.

Provider architecture tách API khỏi cryptographic implementation.

Bạn có thể inspect:

```java
Security.getProviders();
```

Enterprise/FIPS environments có thể require approved provider.

Không hard-code provider trừ khi policy/interoperability cần; nếu hard-code, deployment phải guarantee provider tồn tại.

---

# 43. MAC khác Hash

Hash:

```text
message → digest
```

ai cũng compute được.

MAC dùng secret key:

```text
secret + message → authentication tag
```

HMAC:

```java
Mac mac =
    Mac.getInstance(
        "HmacSHA256");
```

Dùng để authenticate message integrity giữa parties chia secret.

Plain SHA-256 không chứng minh message từ trusted sender.

---

# 44. Digital Signature

Signature dùng private key để sign và public key để verify.

```java
Signature signature =
    Signature.getInstance(
        "SHA256withRSA");
```

Real algorithm choices nên theo modern security guidance; RSA/ECDSA/EdDSA trade-offs.

Signature authenticity phụ thuộc key trust/distribution, không chỉ math.

Certificate/PKI giải quyết binding public key với identity.

---

# 45. KeyStore, TrustStore và TLS mental model

`KeyStore` có thể chứa private keys, secret keys, certificates.

TLS client/server config liên quan identity keys và trust anchors.

`SSLContext` được initialize từ KeyManagers/TrustManagers/SecureRandom.

Một lỗi TLS thường thuộc categories:

```text
DNS/host mismatch
expired certificate
unknown CA
missing intermediate
protocol/cipher mismatch
client-cert requirement
```

“PKIX path building failed” thường là trust-chain problem, không phải network unreachable.

---

# 46. `keytool` và `jarsigner`

`keytool` quản lý keystore/certificates:

```bash
keytool -list \
  -keystore app.p12
```

`jarsigner` sign/verify JAR signatures.

Artifact signing giúp verify origin/integrity theo trust model, nhưng secure software supply chain còn cần dependency provenance, CI security và key management.

Master Java engineer cần biết tool tồn tại và đọc output, không nhất thiết tự làm PKI chuyên gia.

---

# 47. Annotation Processing: compile-time metaprogramming

Runtime reflection đọc class sau compile. Annotation processor chạy trong compilation.

Processor implement:

```java
Processor
```

thường extend:

```java
AbstractProcessor
```

và làm việc với:

```text
RoundEnvironment
Elements
Types
Filer
Messager
```

Flow:

```text
javac parses source
→ processors see annotated elements
→ processor generates source/resources
→ additional rounds compile generated source
```

Lombok dùng compiler integration riêng phức tạp; MapStruct-style codegen là ví dụ dễ hiểu hơn về compile-time generation.

---

# 48. Annotation Processor rounds

Generated code có thể tạo annotations/elements mới, nên compiler chạy multiple rounds.

Processor phải handle rounds idempotently và `processingOver()`.

Không assume một lần.

`Filer` tạo generated source/class/resource. `Messager` emit compiler diagnostics.

Processor errors nên report tại element liên quan để IDE/build cho developer feedback tốt.

---

# 49. Source generation và API design

Nếu processor generate:

```java
UserMapperImpl
```

generated class name/package trở thành part của integration contract nếu user code reference trực tiếp.

Tốt hơn expose stable annotation/runtime interface và treat generated details internal where possible.

Generated code cần deterministic để build cache/reproducibility tốt.

Annotation processing chạy build-time nên performance của processor ảnh hưởng every compile.

---

# 50. Java Agents và Instrumentation

Java agent chạy code trước `main` qua:

```java
public static void premain(
    String agentArgs,
    Instrumentation inst) {
}
```

Dynamic attach có thể dùng `agentmain`.

`Instrumentation` cho inspect loaded classes, redefine/retransform class tùy capability và register `ClassFileTransformer`.

APM/profilers/mock/instrumentation tools dùng agents để insert probes.

Agent chạy trong target JVM với quyền lực lớn. Bug agent có thể ảnh hưởng toàn application.

---

# 51. ClassFileTransformer

Transformer nhận class bytes trong loading/retransformation pipeline và có thể return transformed bytes.

Bạn phải hiểu class-file validity, stack maps/verification, recursion/classloader interactions.

Không manually edit byte array offsets. Dùng Class-File API hoặc mature bytecode library.

Instrument method entry/exit naïvely có thể phá exceptions, synchronized semantics hoặc performance.

---

# 52. Class-File API từ Java 24

JDK 24 standardizes `java.lang.classfile` API để parse, generate và transform class files.

Mục tiêu là tránh mỗi tool/library phải maintain parser theo class-file evolution.

Concept:

```java
ClassFile cf =
    ClassFile.of();

ClassModel model =
    cf.parse(bytes);
```

API model class/method/field/attributes/instructions và hỗ trợ transformation.

Nếu bạn viết agent/codegen/build tool, đây là API quan trọng. Nếu bạn viết CRUD service, chỉ cần awareness.

---

# 53. Class-file structure

Class file bắt đầu magic:

```text
0xCAFEBABE
```

rồi minor/major version, constant pool, access flags, this/super, interfaces, fields, methods, attributes.

Major version quyết định runtime compatibility; JVM cũ thấy newer major sẽ reject.

Class file không phải “serialized Java source”. Generic info, debug info, annotations và bytecode nằm trong attributes/constant-pool references; source-level constructs có thể biến đổi đáng kể.

---

# 54. Constant Pool

Constant pool chứa constants và symbolic references: class names, method/field refs, strings, method handles/types, dynamic constants...

Bytecode instructions thường refer indexes vào constant pool.

Linking resolution biến symbolic reference thành runtime entity khi cần.

Hiểu constant pool giúp đọc `javap -v`, `invokedynamic`, dynamic constants và linkage errors.

---

# 55. Method descriptors

JVM descriptor encode parameter/return types.

Ví dụ:

```java
String f(int x, long y)
```

descriptor:

```text
(IJ)Ljava/lang/String;
```

Primitive codes: `I` int, `J` long, `V` void; object `L...;`; array `[...`.

Bytecode/tooling uses descriptors, không Java generic syntax.

---

# 56. StackMapTable và verifier

Modern class files có stack map frames giúp verifier check type state at control-flow points efficiently.

Nếu bytecode transformer generate invalid frames, class load có thể fail `VerifyError`.

Mature Class-File API/ASM compute/manage frames giúp tránh manual nightmare.

Đây là ví dụ tại sao bytecode engineering là specialist field dù syntax transformation nhìn đơn giản.

---

# 57. `invokedynamic`

Traditional invokevirtual call-site references method symbolically theo fixed dispatch rules. `invokedynamic` cho runtime bootstrap logic link call site dynamically.

Instruction references bootstrap method metadata. First linkage computes CallSite/target; later invocation có thể reuse optimized target.

Java lambdas dùng `invokedynamic` + `LambdaMetafactory`. Modern string concatenation cũng dùng dynamic concat machinery.

Điều này cho JVM/library authors linh hoạt implement language features mà không thêm bytecode instruction cho từng feature.

---

# 58. Lambda không đơn giản là anonymous class

Source:

```java
Function<String, Integer>
    length =
        String::length;
```

compiler thường emits invokedynamic call site, bootstrap tới LambdaMetafactory.

Runtime có thể produce object/behavior optimized tùy capture/state.

Do đó assumptions như “mỗi lambda luôn tạo một anonymous class file” là sai trong modern Java.

Captured lambda có different allocation/lifecycle behavior so non-capturing; JIT có thể optimize further.

---

# 59. MethodHandle

MethodHandle là strongly typed executable reference.

Lookup:

```java
MethodHandles.Lookup lookup =
    MethodHandles.lookup();

MethodHandle mh =
    lookup.findVirtual(
        String.class,
        "length",
        MethodType.methodType(
            int.class));
```

Invoke exact:

```java
int length =
    (int) mh.invokeExact("hello");
```

`invokeExact` yêu cầu exact MethodType; `invoke` cho adaptation conversions rộng hơn.

MethodHandle có thể được JIT optimize better than arbitrary reflection in dynamic frameworks, nhưng API type gymnastics phức tạp.

---

# 60. MethodHandle combinators

Bạn có thể transform handles:

```text
bindTo
insertArguments
dropArguments
filterArguments
filterReturnValue
guardWithTest
foldArguments
```

Những combinators cho build dynamic invocation pipelines không generate bytecode manually.

Dynamic language runtime, serialization frameworks, proxy systems có thể dùng.

Application-level dispatch nên dùng ordinary interfaces/lambdas trước.

---

# 61. Hidden Classes

Hidden classes được thiết kế cho frameworks generate runtime classes không cần discoverability/lifecycle như normal named classes.

Chúng không dễ được tìm qua normal class loading/name lookup và có GC/unloading properties useful dynamic language/framework implementations.

Lambda runtime đã liên quan hidden-class direction trong modern JDK internals.

Nếu bạn viết proxy/runtime code generation, hidden classes giải quyết pollution/leak của generating endless named classes.

---

# 62. Dynamic Constants (`condy`)

`CONSTANT_Dynamic` cho constant-pool entry được bootstrap dynamically tại linkage, giống invokedynamic nhưng cho value thay vì call site.

Nó cho language/runtime/library authors lazy/computed constants mà JVM có thể treat như constant after resolution.

Normal application code hiếm khi author condy trực tiếp, nhưng Class-File API/bytecode tools có thể.

Java 26 Lazy Constants API ở source/library level là concept liên quan nhưng không đơn giản đồng nhất với condy.

---

# 63. Foreign Function & Memory API: Java gọi native code mà không phải sống trong JNI boilerplate

FFM final ở Java 22, package:

```java
java.lang.foreign
```

Nó giải quyết hai vấn đề lớn: access memory ngoài Java heap an toàn hơn và gọi native functions qua linker/method handles.

Core concepts:

```text
MemorySegment
Arena
MemoryLayout
Linker
SymbolLookup
FunctionDescriptor
```

FFM không làm native code “an toàn như Java”. C function vẫn có thể corrupt memory bên native side. Nhưng Java-side bounds/lifetime checking mạnh hơn raw JNI/Unsafe patterns.

---

# 64. MemorySegment

MemorySegment là bounded region của memory.

Có heap segments và native segments.

Operations check bounds/alignment/lifetime based API.

Thay vì raw address `long`, segment carries spatial/temporal safety metadata.

Nếu access outside segment:

```text
exception
```

thay vì silently corrupt adjacent Java/native memory từ Java API.

---

# 65. Arena và temporal safety

Arena controls native segment lifetime.

```java
try (Arena arena =
         Arena.ofConfined()) {

    MemorySegment segment =
        arena.allocate(1024);

    ...
}
```

Sau arena close, access segment fail.

Confined arena có thread-confinement semantics. Shared arena supports cross-thread access with different lifecycle considerations.

This is RAII-like resource scope in Java: deterministic close beats waiting GC.

---

# 66. MemoryLayout

Native structs/arrays có layout.

```java
MemoryLayout layout =
    MemoryLayout.structLayout(
        ValueLayout.JAVA_INT
            .withName("x"),
        ValueLayout.JAVA_INT
            .withName("y"));
```

Layout helps derive offsets/VarHandles/access.

Alignment/endian/platform ABI matter. Native layout phải match C ABI exactly.

Never assume Java type sizes/layout equal arbitrary C compiler struct without ABI understanding.

---

# 67. Linker, SymbolLookup và FunctionDescriptor

Lookup native symbol:

```java
SymbolLookup lookup = ...;
MemorySegment symbol =
    lookup.find("strlen")
          .orElseThrow();
```

FunctionDescriptor describes native signature.

Linker creates downcall MethodHandle.

Calling native function now fits MethodHandle execution model.

Native access can be restricted; modern Java requires explicit native-access enablement in relevant deployment situations. Treat this as security/operational contract.

---

# 68. Upcalls

FFM can create native function pointer that calls Java MethodHandle.

Useful callbacks from C library.

Lifecycle is critical: upcall stub memory and arena must live while native side might invoke callback.

If arena closes early and native calls stale pointer, behavior/failure can be severe.

This is ownership across language boundary; document lifetime explicitly.

---

# 69. JNI awareness

JNI is older native interop mechanism using generated/native glue and JNI environment APIs.

It is powerful but verbose and error-prone: local/global references, pin/copy arrays, exception checking, thread attachment, native crashes.

You still need JNI awareness because many libraries use it, but new code should evaluate FFM first when feasible.

A segfault in JNI/FFM/native library can crash entire JVM, not throw catchable Java exception.

---

# 70. `Unsafe` migration

`sun.misc.Unsafe` historically exposed raw memory, CAS, field offsets, object allocation, fences and many JVM internals.

Modern replacements cover many areas:

```text
VarHandle
FFM
MethodHandle
Cleaner
standard concurrent APIs
```

Some libraries still use Unsafe for performance/backward compatibility.

Don't copy Unsafe code from Stack Overflow. It bypasses Java safety and encapsulation, breaks across JVM evolution and AOT/security boundaries.

---

# 71. GC TLAB

Most small object allocation can happen in Thread Local Allocation Buffer, a per-thread chunk of Eden/young allocation area.

Fast-path allocation becomes pointer bump with little synchronization.

This is one reason `new` for small short-lived objects is extremely cheap in HotSpot.

When TLAB exhausted, thread requests/refills; large objects may bypass.

JFR/GC logs can show allocation pressure. Don't object-pool tiny objects to avoid “expensive malloc” mental model from C.

---

# 72. Write Barriers

GC needs know when references change.

JIT inserts **write barriers** around reference stores so collector can maintain remembered sets/card tables/concurrent marking invariants.

Example:

```java
oldObject.field =
    youngObject;
```

generational collector needs know old region now points to young object so young collection doesn't scan entire old heap.

Barrier cost is part of object/reference mutation cost, usually tiny but fundamental.

---

# 73. Card Tables và Remembered Sets

A card table divides memory into coarse regions/cards and marks cards dirty on reference writes. Collector scans dirty cards rather than entire old generation.

G1 uses remembered sets/region metadata to track cross-region references with more sophisticated machinery.

This explains why “only young generation is collected” can still correctly find references from old objects.

Application developers don't tune card tables normally; understanding them helps read GC/JIT discussions.

---

# 74. Safepoints

Safepoint is JVM state where threads are at locations suitable for certain global VM operations.

Historically GC stop-the-world phases, deoptimization, class redefinition and VM operations may require safepoint coordination.

Time-to-safepoint can contribute pause separately from GC work.

Modern JVM also has mechanisms like handshakes for more targeted operations, reducing need for global safepoint in some cases.

When JFR/log says long pause, distinguish “reach safepoint” from “operation at safepoint”.

---

# 75. Stop-the-world không có nghĩa mọi GC đều hoàn toàn STW

Modern collectors perform significant work concurrently with application threads.

However they still have some stop-the-world phases.

G1, ZGC, Shenandoah differ in which phases are concurrent and pause profiles.

The useful question is not “collector concurrent?” but “what are pause distributions, CPU overhead, allocation headroom and throughput under my workload?”.

---

# 76. Serial GC, Parallel GC, G1, ZGC, Shenandoah

Serial GC uses single-threaded collection work and suits small/simple footprints.

Parallel GC emphasizes throughput using multiple GC threads, with larger pauses acceptable.

G1 is general-purpose regional collector with pause-target goals and common modern default.

ZGC targets extremely low pauses with highly concurrent work; modern ZGC is generational.

Shenandoah is another low-pause concurrent collector available in OpenJDK distributions; modern releases include generational evolution.

Collector choice belongs SLO/capacity testing, not fashion.

---

# 77. Object Layout

A Java object in HotSpot conceptually contains header + instance fields + padding/alignment.

Header historically includes mark word and class metadata pointer/reference. Exact layout depends JVM flags, compressed references, collector and JDK evolution.

Object alignment often means size rounds to multiple boundary.

This matters in millions of objects: a few bytes padding/header multiply into hundreds MB.

Use JOL (Java Object Layout) tool for evidence instead of manually assuming sizes.

---

# 78. Compressed References

On suitable heaps/configs HotSpot can encode object/class references in narrower representation, reducing memory footprint and improving cache locality.

This is why reference field might effectively use 4 bytes rather than native 8-byte pointer in certain configurations.

Thresholds/modes depend heap/addressing/JVM.

Do not hard-code object-size assumptions into application logic.

---

# 79. Compact Object Headers trong Java 25

Java 25 includes Compact Object Headers as a production feature/runtime improvement. Goal is reducing object header footprint by encoding metadata more compactly.

Effect can be significant for object-heavy workloads by reducing heap footprint/cache traffic.

You usually don't change source code to benefit; upgrade/runtime flags/defaults govern behavior according release.

This is another reminder that JDK upgrade can improve application memory without code change, so re-baseline performance after upgrades.

---

# 80. CDS và AppCDS

Class Data Sharing stores preprocessed class metadata in archive shared/mapped at startup, reducing startup time and memory across processes.

AppCDS extends sharing to application classes.

Modern JDK/Boot ecosystems increasingly automate training/archive creation.

CDS primarily optimizes class loading/startup footprint, not business algorithm throughput.

When startup matters, measure class-loading/JIT/AOT separately.

---

# 81. Project Leyden/AOT direction

Modern Java is adding AOT cache/training mechanisms while preserving JVM dynamic optimization model.

The direction is not simply “replace JIT with native compilation”. Goal is shift some class loading/linking/compilation/profile work ahead of startup and reuse it.

Java 25/26 include AOT cache improvements. Exact commands/features evolve quickly, so use version-specific docs.

A master engineer should understand dimensions:

```text
build/training cost
startup
warm-up
peak throughput
portability
profile representativeness
```

---

# 82. JFR continuous recording

JFR is valuable when recording already running **before** incident.

Continuous low-overhead recording with bounded disk/age can preserve last minutes.

Example conceptual command:

```bash
jcmd <pid> JFR.start \
  name=continuous \
  settings=profile \
  maxage=30m \
  maxsize=1g \
  filename=app.jfr
```

Exact options/profile depend environment.

During incident you dump current recording instead of starting after symptom disappears.

---

# 83. Custom JFR Events

Application/library can define custom event:

```java
@Name("com.example.OrderProcessed")
class OrderProcessedEvent
        extends Event {

    long orderId;
    long durationNanos;
}
```

Use:

```java
event.begin();
...
event.commit();
```

JFR event should be meaningful and low-overhead. Don't emit huge strings/secrets/high-frequency events without threshold/sampling strategy.

Custom events make correlation between business operation and JVM behavior extremely powerful.

---

# 84. JMX và MXBeans

JMX exposes management objects via MBeans/MXBeans.

Platform MXBeans:

```java
ManagementFactory
    .getMemoryMXBean();

ManagementFactory
    .getThreadMXBean();

ManagementFactory
    .getGarbageCollectorMXBeans();
```

Useful for monitoring/tools.

Remote JMX historically has security/network complexity; modern observability often exports metrics differently. Still, understanding MXBeans helps because many JVM metrics originate from same management data.

---

# 85. ThreadMXBean

Can inspect thread IDs/info, CPU time, deadlock detection depending JVM capability.

Programmatic diagnostics tool:

```java
ThreadMXBean bean =
    ManagementFactory
        .getThreadMXBean();
```

Library/test tools can detect deadlocks or thread CPU hotspots.

Avoid polling expensive full stack dumps at extremely high frequency.

---

# 86. `jdeps`

`jdeps` analyzes class/module dependencies.

Useful trước upgrade/module migration:

```bash
jdeps app.jar
```

Can identify JDK internal APIs, package/module dependencies and transitive relationships.

When moving 8→17/21/25, `jdeps --jdk-internals` can help find unsupported internal APIs.

---

# 87. `jdeprscan`

Scans class/JAR usage of deprecated APIs against JDK.

Useful continuous modernization:

```bash
jdeprscan app.jar
```

Deprecation today may become removal later. Fix during regular upgrades instead of waiting one giant migration.

---

# 88. `jlink`

JPMS modules allow building custom runtime image with only needed modules.

```bash
jlink \
  --module-path ... \
  --add-modules com.example.app \
  --output runtime
```

Benefits smaller deployment/runtime control.

But many frameworks/libs are classpath-oriented or use reflection/resources dynamically; integration testing required.

Containers often ship full JRE/JDK anyway, so size benefit must justify complexity.

---

# 89. `jpackage`

`jpackage` creates native application packages/installers/bundles including runtime image.

Useful desktop/distributed applications where user should not install JDK manually.

It can combine with jlink-generated runtime.

Server containers usually use different packaging practices, but tool belongs JDK mastery.

---

# 90. `jhsdb`

HotSpot Serviceability Agent tooling can inspect JVM/core dumps at low level.

Use cases include post-mortem when process crashed or normal attach unavailable.

Commands can inspect heap, stack, classloader, VM structures.

This is advanced incident tooling; operation privileges/version matching matter.

---

# 91. JAR Manifest

`META-INF/MANIFEST.MF` contains attributes.

Executable JAR:

```text
Main-Class: com.example.Main
```

then:

```bash
java -jar app.jar
```

Manifest line formatting/classpath semantics have quirks; build tool should generate.

Signed JAR also stores signature metadata under META-INF.

---

# 92. Multi-Release JAR

A library can ship base classes plus version-specific implementations under:

```text
META-INF/versions/9/
META-INF/versions/21/
```

Runtime selects appropriate version.

This allows one artifact support broad JDKs while using newer APIs internally on new runtime.

But testing matrix becomes complex: you must test every supported runtime path. Avoid unless library compatibility genuinely requires.

---

# 93. Automatic Modules và module naming

A normal JAR on module path may become automatic module with derived/name metadata.

Stable `Automatic-Module-Name` manifest attribute helps library avoid filename-derived module-name changes before fully modularizing.

Public module/package names are compatibility surface. Renaming later breaks consumers.

---

# 94. ServiceLoader sâu hơn

Service provider interface:

```java
public interface Codec {
    byte[] encode(Object value);
}
```

Providers can be declared in module descriptor:

```java
provides Codec
    with JsonCodec;
```

Consumer:

```java
ServiceLoader<Codec>
    loader =
        ServiceLoader.load(
            Codec.class);
```

`ServiceLoader.Provider<T>` allows inspect provider type/lazy instantiate.

This is Plugin/Strategy discovery built into Java.

Provider constructor/lifecycle/error handling must be designed; one broken provider can affect discovery.

---

# 95. ModuleLayer

JPMS can create additional module layers at runtime.

Useful plugin systems loading modules/configuration separate from boot layer.

A layer has module configuration + class loaders.

This gives stronger module boundaries than raw custom classloader but is advanced.

Application code rarely needs ModuleLayer; plugin/container frameworks may.

---

# 96. Custom ClassLoader

Subclass ClassLoader and override `findClass`/resource loading as appropriate.

Correct delegation is hard. Parent-first avoids duplicate core classes; child-first may isolate plugin versions but risks type identity conflicts.

When plugin interface is loaded by parent but plugin bundles own duplicate interface, cast fails even same class name.

Design shared API classloader boundary intentionally.

---

# 97. Resource Loading

`Class.getResource` path semantics differ leading slash vs relative package.

`ClassLoader.getResource` generally uses absolute classpath-like names without leading slash.

In JAR, resource isn't necessarily physical file; converting resource URL to `File` may fail.

Use stream:

```java
try (InputStream in =
    MyClass.class
        .getResourceAsStream(
            "/config/default.json")) {
}
```

Frameworks packaged in fat JARs make file assumptions especially dangerous.

---

# 98. Advanced Generics: reifiable types

Reifiable type has enough runtime representation after erasure, examples:

```text
int
String
List<?>
raw List
arrays of reifiable component
```

`List<String>` is non-reifiable.

This explains restrictions:

```java
new List<String>[10] // illegal
obj instanceof List<String> // illegal
```

Runtime cannot fully check element type after erasure.

---

# 99. Generic arrays

Arrays are covariant/reified; generics invariant/erased. Mixing creates unsoundness.

If you need generic collection of T, prefer `List<T>`.

Low-level generic container may use:

```java
@SuppressWarnings("unchecked")
T[] array =
    (T[]) new Object[size];
```

internally, but must encapsulate unsafe cast and ensure no incompatible values enter.

Suppress warning at smallest proven-safe boundary.

---

# 100. Bridge Methods

Suppose generic interface:

```java
interface Box<T> {
    T get();
}
```

Implementation:

```java
class StringBox
        implements Box<String> {

    public String get() {
        return "...";
    }
}
```

After erasure interface method resembles `Object get()`. Compiler may generate synthetic bridge method returning Object and delegating to String-return method to preserve polymorphism/binary compatibility.

Reflection/stack traces can show bridge methods.

This is why `Method.isBridge()` exists.

---

# 101. Wildcard Capture

Method gets `List<?>`. You cannot `set` arbitrary Object because actual element type unknown.

A helper generic method can “capture” wildcard type:

```java
void reverse(List<?> list) {
    reverseCaptured(list);
}

private <T> void reverseCaptured(
        List<T> list) {
    ...
}
```

Compiler invents a consistent captured T for that specific list.

Wildcard capture errors seem cryptic, but mental model is “unknown but fixed type”, not “any type”.

---

# 102. Intersection Types

Bound:

```java
<T extends Closeable
        & Comparable<T>>
```

requires T satisfy multiple contracts.

Casts can use intersections in some contexts:

```java
(Runnable & Serializable)
    () -> run();
```

Compiler/lambda target typing uses intersection types internally.

Useful library generics; application API should avoid overly clever signatures if readability suffers.

---

# 103. Type Tokens

Because `List<String>.class` doesn't exist, frameworks often use type token objects carrying generic `Type`.

Pattern:

```java
new TypeReference<
    List<User>>() {}
```

anonymous subclass captures generic superclass metadata inspectable by reflection.

Jackson/Gson-like libraries use this.

This is workaround around erasure. Modern APIs may use `ParameterizedType`/custom type descriptors.

---

# 104. Overload resolution vs Override dispatch

Overload is compile-time based on **static argument types**.

Override is runtime dispatch based on receiver object's runtime class.

Example:

```java
void print(Object x)
void print(String x)
```

If variable static type Object holds String:

```java
Object x = "hello";
print(x);
```

compiler chooses `print(Object)`.

But:

```java
Animal a =
    new Dog();

a.sound();
```

override dispatch chooses Dog's `sound()`.

Confusing these causes interview and real API bugs.

---

# 105. Static Method Hiding

Static methods are resolved by class/reference static type; they are hidden, not overridden polymorphically.

```java
class A {
    static void f() {}
}

class B extends A {
    static void f() {}
}
```

`A x = new B(); x.f()` resolves A.f by static binding.

Avoid polymorphic expectations on static methods.

---

# 106. Constructor/Initialization Order

Rough flow constructing subclass object:

```text
allocate object / default values
→ superclass initialization/constructor
→ instance initializers/field initializers
→ subclass constructor body
```

Exact ordering of field initializers relative constructor chain matters.

Danger: superclass constructor calls overridable method. Override executes before subclass fields initialized.

```java
class Base {
    Base() {
        initialize();
    }

    void initialize() {}
}
```

Subclass override may see default null/0 state.

Never call overridable methods from constructors unless design carefully guarantees safety.

---

# 107. URI vs URL

`URI` is identifier/reference syntax model. It may be relative and doesn't imply network access.

`URL` historically combines locator with connection behavior.

Modern Java HTTP APIs use `URI` for request target:

```java
HttpRequest.newBuilder(
    URI.create(...))
```

When manipulating URLs, don't string-concatenate query/path blindly. Encode components according URI rules; `URLEncoder` historically targets form/query encoding semantics, not arbitrary full URL escaping.

---

# 108. DNS behavior

Host lookup may cache positive/negative results according JVM/security/provider settings and OS resolver.

DNS TTL and client connection pools influence failover.

If service IP changes, long-lived keepalive connections may continue old address; DNS re-resolution only matters on new connection.

Do not build failover assumptions without understanding client/DNS/load balancer behavior.

---

# 109. ProxySelector

Java networking can use `ProxySelector` to choose proxies for URI.

System properties/environment enterprise networks may route HTTP differently from local.

When app works local but cannot reach Internet in corporate environment, proxy/TLS trust/DNS often involved.

HTTP client builder can configure proxy explicitly.

---

# 110. WebSocket Client

Java HTTP client includes WebSocket client APIs.

WebSocket is long-lived bidirectional message connection, not ordinary request/response.

You implement listener callbacks and demand messages.

Need handle fragmentation, backpressure, reconnect, heartbeat, close status and message size.

Do not keep unlimited pending messages when consumer slow.

---

# 111. API Documentation là contract

Javadoc không nên lặp method name bằng prose vô nghĩa.

Public API docs phải nói:

```text
nullability
ownership/mutation
thread safety
blocking behavior
exceptions
ordering
complexity where relevant
lifecycle
```

For library:

```java
/**
 * Returns an immutable snapshot...
 *
 * @throws IllegalStateException
 *         if the session is closed
 */
```

documentation có thể quan trọng ngang type signature.

---

# 112. `@apiNote`, `@implSpec`, `@implNote`

Javadoc tags cho phân biệt contract audiences.

`@apiNote`: useful guidance cho API users nhưng không normative contract.

`@implSpec`: implementation requirements subclasses/implementors phải tuân thủ.

`@implNote`: notes về current implementation, có thể thay mà không phải contract.

Library authors nên dùng để tránh consumers phụ thuộc accident implementation detail.

---

# 113. Thread-Safety Documentation

Một class nên nói rõ:

```text
immutable
thread-safe
conditionally thread-safe
not thread-safe
thread-confined
```

Nếu method thread-safe individually nhưng sequence không atomic, docs phải clarify.

Ví dụ synchronized map:

```java
if (!map.containsKey(k)) {
    map.put(k, v);
}
```

two method calls individually synchronized nhưng compound sequence vẫn race nếu external synchronization không đúng.

Documentation is part of concurrency design.

---

# 114. Memory Ownership Documentation

For buffers/collections/resources, state:

```text
caller retains ownership?
callee copies?
returned array mutable?
method retains reference after return?
caller must close?
```

Zero-copy APIs đặc biệt cần ownership/lifetime rõ.

A buffer passed to async operation cannot be reused until completion unless API copies it.

Many high-performance bugs are ownership bugs, not syntax bugs.

---

# 115. Designing Extension Points

If library exposes interface for third-party implementation, you lose ability to add abstract methods later without breaking implementors.

Default methods can evolve interfaces but may have semantic conflicts.

Extension point should be minimal, stable, documented, and avoid leaking implementation classes.

Sometimes callback/lambda/SPI/provider configuration is more evolvable than subclassing abstract base.

Don't expose extension just “in case”; public extension surface is long-term compatibility commitment.

---

# 116. Reentrancy và callbacks

Suppose collection method holds lock then calls user-provided predicate:

```java
synchronized (...) {
    predicate.test(element);
}
```

Predicate may call collection again, possibly reentrant or acquire another lock.

Even reentrant monitor doesn't prevent lock-order deadlock with external locks.

Library code should treat user callback as arbitrary code. Snapshot data/release lock before callback if invariant allows.

This principle appears in observers, comparators, hashCode/equals callbacks and CompletableFuture chains.

---

# 117. Cancellation as first-class concern

Every long-running operation should answer:

```text
Can caller cancel?
How is cancellation signaled?
Does blocking I/O unblock?
Are child tasks cancelled?
Who cleans resources?
```

Thread interrupt is one mechanism, not universal cancellation token.

Future cancellation may interrupt task if configured; socket close can unblock I/O; structured concurrency propagates cancellation structurally.

If cancellation ignored, shutdown/deadline cannot be reliable.

---

# 118. Backpressure beyond Reactive Streams

Backpressure means producer adapts to consumer capacity.

Tools:

```text
bounded BlockingQueue
Semaphore
CallerRunsPolicy
rate limiter
TCP flow control
Flow request(n)
batching
load shedding
```

Unbounded buffering is not backpressure.

Every async boundary should have capacity policy. If producer can outpace consumer indefinitely, memory or latency eventually explodes.

---

# 119. Load Shedding

When saturated, rejecting early may preserve healthy work.

Examples:

```text
queue.offer() returns false
HTTP 429/503
drop low-priority telemetry
skip optional refresh
```

The right strategy is business-specific.

A system that accepts everything and times out 60 seconds later is often less reliable than one that rejects quickly under load.

---

# 120. Fairness vs Throughput

Fair locks/queues serve waiters roughly arrival order, reducing starvation.

But fairness prevents barging and can lower throughput/cache locality.

Non-fair `ReentrantLock` default often performs better.

Use fairness only when wait-time/starvation semantics matter, not because “fair sounds correct”.

---

# 121. Priority Inversion Awareness

High-priority task waits on lock held by low-priority thread; medium-priority CPU tasks prevent low-priority from running/releasing lock.

General JVM application rarely controls OS priorities reliably enough to “solve” with thread priority.

Better avoid long locks and mixed-priority resource sharing.

Realtime systems need specialized design/runtime.

---

# 122. False Sharing

Two unrelated hot counters on same CPU cache line cause coherence invalidations when different cores write.

Symptoms show high CPU/cache misses despite no logical lock contention.

Libraries may pad/separate data.

Don't randomly pad normal fields; use profiler/hardware counters/JMH.

This belongs mechanical-sympathy optimization after correctness.

---

# 123. Mechanical Sympathy

Mechanical sympathy means designing with awareness of hardware/runtime: cache lines, memory bandwidth, branch prediction, allocation, syscalls, NUMA, network.

It does **not** mean writing unreadable low-level code everywhere.

High-level Java often lets JIT optimize better than hand tricks.

Use hardware knowledge to interpret profiles and choose data layout/algorithms on hot paths.

---

# 124. Object Pooling

Pooling database connections/threads/native expensive resources makes sense because creation is costly or external capacity bounded.

Pooling tiny Java objects often hurts:

```text
synchronization
stale state
retention
cache misses
complex ownership
```

Modern allocation/GC is optimized for short-lived objects.

Pool only after profiling shows allocation/initialization cost and object reuse semantics are safe.

---

# 125. Escape Analysis không phải language guarantee

JIT may scalar-replace/eliminate object today, but source semantics cannot depend on optimization occurring.

Performance can change with JDK, code shape, profiling.

Do not say “this object never allocates” unless you mean observed compiled code for specific runtime.

Write semantically correct code first.

---

# 126. Polymorphism và JIT

Interface call doesn't always stay expensive virtual dispatch.

If call site is monomorphic/bimorphic, JIT can inline/devirtualize with guards.

Too many implementations at hot megamorphic call site can reduce inlining.

This is specialist optimization. Do not remove interfaces across architecture just to help hypothetical JIT.

Profile inlining decisions on truly hot code.

---

# 127. Code Cache

JIT-compiled machine code lives in code cache/native memory.

Large dynamic applications/frameworks can fill code cache in unusual scenarios, affecting compilation/performance.

JFR/jcmd/VM diagnostics expose code cache stats.

Container RSS includes code cache outside heap.

Again: Xmx is not process memory.

---

# 128. ClassLoader Leaks sâu hơn

A classloader can unload only when loader and all classes/objects aren't reachable.

A long-lived thread context classloader pointing old webapp loader can pin entire deployment.

Other roots: ThreadLocal, static registry in parent loader, JDBC DriverManager, MBeans, executors, logging callbacks.

Heap dump dominator/path-to-GC-root helps find.

Reload environments are especially susceptible.

---

# 129. Reflection access after strong encapsulation

Modern Java module system strongly encapsulates JDK internals.

Old reflection code may fail with `InaccessibleObjectException`.

`--add-opens` can temporarily open package to reflection:

```bash
--add-opens \
java.base/java.lang=ALL-UNNAMED
```

but treat as migration escape hatch, not permanent architecture if avoidable.

Use supported public APIs.

---

# 130. `final` semantics ngày càng quan trọng

Final fields/classes/methods help invariants/JIT and future platform integrity.

JDK is tightening restrictions around deep reflection/mutation of final fields over releases.

Frameworks historically used reflection to set private/final fields; modern code generation/constructor binding is more robust.

Do not depend on illegal deep mutation of immutable objects.

---

# 131. Native Crash Diagnostics

A native crash can produce `hs_err_pid*.log` or core dump.

Common causes:

```text
JNI bug
native library
JVM bug
unsafe memory access
hardware
driver
FFM misuse/native callee bug
```

`hs_err` includes problematic frame, thread, registers, loaded libraries, VM flags, heap summary.

If problematic frame is `[C] libfoo.so`, investigate native side, not Java exception handling.

---

# 132. Correlating JFR + GC + Native Memory

One symptom may have multiple signals.

Latency spike:
JFR shows allocation burst → GC log shows young pauses → RSS stable.

RSS growth:
heap live set stable → NMT shows Thread/Native growing.

CPU spike:
JFR samples in compression → GC normal.

Master diagnostics correlates layers instead of interpreting one metric alone.

---

# 133. File Descriptors

Sockets, files, pipes use OS file descriptors/handles.

Leak can fail with:

```text
Too many open files
```

even heap healthy.

Check OS limits and process FD count.

Try-with-resources closes Java wrappers; connection pools deliberately keep sockets open within configured capacity.

Large FD limit is not substitute for fixing leak.

---

# 134. Signals và process termination

SIGTERM typically used graceful shutdown in Unix/container. JVM runs shutdown hooks and normal framework shutdown if process can handle signal.

SIGKILL cannot be caught; no cleanup.

Crash/power loss also bypasses hooks.

Therefore durable correctness must not rely on “we will flush in shutdown hook”. Persist critical state before acknowledging operation.

---

# 135. Serialization Formats và Java Types

JSON numbers don't distinguish `int`/`long`/BigDecimal exactly the same way Java does. Dates are strings/numbers with contract. Maps with non-string keys need encoding rules.

Protobuf/Avro have explicit schemas/evolution semantics.

When crossing boundary, Java type is not wire contract automatically.

Design schema separately, then map types.

This insight prevents leaking records/entities as permanent integration protocol.

---

# 136. Enum Evolution

Adding enum constant can break exhaustive switch written against older assumptions, serializers/databases/consumers.

Persisting `ordinal()` is fragile because reorder changes meaning.

External protocol should use stable string/code and unknown-value strategy.

Library consumers may have switch without default; adding constant can create runtime behavior differences.

Closed enum is source-compatible addition but potentially behavioral compatibility change.

---

# 137. Date/Time Edge Cases

Leap years:

```text
2024-02-29 exists
2025-02-29 invalid
```

End-of-month:

```java
LocalDate.of(2026, 1, 31)
    .plusMonths(1)
```

uses date adjustment semantics; understand expected business rule.

Timezone rules update with IANA tzdata. Historical/future offsets can change when governments change law.

Persist `Instant` for actual event; persist ZoneId if future local schedule needs regional rules.

`System.nanoTime` for duration, wall clock for timestamp.

---

# 138. Concurrent Collections memory visibility

Concurrent collection methods define happens-before relationships for successful publication/access per API specification.

Putting fully constructed object into `ConcurrentHashMap` then another thread retrieving through map provides safe publication according collection contract.

This doesn't make object mutations after retrieval thread-safe.

Container thread safety and element thread safety are separate.

---

# 139. Fail-fast, weakly consistent, snapshot iteration

Normal `ArrayList` iterator is fail-fast-ish: detects structural modifications best-effort and throws `ConcurrentModificationException`. It is bug detector, not synchronization guarantee.

`ConcurrentHashMap` iterator is weakly consistent: can proceed during modifications, reflect some updates, no fail-fast guarantee.

`CopyOnWriteArrayList` iterator sees snapshot array from iterator creation.

Choose semantics based use case, not “concurrent collection always newest data”.

---

# 140. Immutability is graph-wide

A class with final fields can still expose mutable graph.

```java
record Team(
    List<Member> members) {
}
```

List may be immutable but `Member` mutable.

Deep immutability requires reachable state immutable or defensively isolated.

You don't always need deep immutability. Just document ownership/mutation contract.

---

# 141. Deprecation, forRemoval và continuous modernization

`@Deprecated` warns API should not be used. `forRemoval=true` signals stronger intent removal.

`since` documents version.

Deprecation is migration window, not immediate failure.

Use compiler warnings, `jdeprscan`, dependency upgrade cadence.

Waiting ten years creates “upgrade cliff”.

---

# 142. Source, Binary và Runtime Compatibility

Source compatible means recompilation works.

Binary compatible means already compiled clients link against new library.

Behavioral compatible means semantics expectations still hold.

Changing generic signature can be source-impacting while erasure keeps binary method descriptor. Changing default method can alter dispatch.

Compatibility is multi-dimensional.

Library versioning must test compiled old clients where necessary.

---

# 143. Classpath Hell và Linkage Errors

`NoClassDefFoundError`: required class unavailable/initialization failed at runtime.

`NoSuchMethodError`: caller compiled expecting method but runtime class version lacks it.

`AbstractMethodError`: binary mismatch where implementation doesn't implement method expected by runtime interface/class evolution.

`IncompatibleClassChangeError`: class/interface/static-instance shape mismatch.

These usually indicate dependency/classloader mismatch, not code branch bug.

Use:

```bash
java -verbose:class
jdeps
dependency:tree
jar tf
```

and inspect actual artifact.

---

# 144. Preview, Incubator, Experimental: đừng trộn

**Preview feature** is fully specified candidate language/VM/API requiring opt-in and may change/remove before final.

Compile/run:

```bash
javac --enable-preview \
      --release 26 ...

java --enable-preview ...
```

**Incubator modules/APIs** are non-final APIs delivered to gather feedback, usually in `jdk.incubator.*`.

**Experimental JVM features** may use `-XX` flags and have even weaker stability.

Production policy should explicitly decide what is allowed.

---

# 145. Java 25 language/runtime delta quan trọng

Java 25 finalizes several language features aimed at teaching/simplicity and constructors. Module Import Declarations became permanent. Compact Source Files and Instance Main Methods became permanent, reducing ceremony for small programs. Flexible Constructor Bodies became permanent, allowing certain statements before explicit superclass constructor invocation under strict initialization safety rules.

These do not radically change enterprise architecture, but they affect language mental model and teaching.

Java 25 also finalizes Scoped Values, includes Compact Object Headers and modern GC/AOT/runtime changes. Structured Concurrency remains preview in 25 rather than final.

---

# 146. Compact Source Files và Instance Main Methods

Small beginner program can avoid full class boilerplate according Java 25 final language feature.

This is mostly pedagogy/scripting-like ergonomics, not a reason enterprise code should abandon named classes/packages.

Large applications still benefit explicit type/module structure.

Understanding feature matters because modern tutorials may no longer start with `public static void main`.

---

# 147. Flexible Constructor Bodies

Historically explicit `super(...)`/`this(...)` had to be first statement. Modern feature allows a constrained prologue before constructor invocation, while preventing access to uninitialized `this` state.

Use case: validate/compute constructor arguments before calling `super`.

The language enforces initialization safety; it does not allow arbitrary use of object before superclass construction.

This removes awkward static helper patterns in some inheritance constructors.

---

# 148. Java 25 Scoped Values final và Structured Concurrency preview

Scoped Values are standard/final in Java 25.

Structured Concurrency remains preview and continues evolving. Do not couple stable library public API directly to preview structured-concurrency classes unless consumers opt into same release/preview.

Use concept—structured task lifetime/cancellation/error—regardless of exact preview API.

---

# 149. Java 26 HTTP/3 support

Java 26 `HttpClient` adds HTTP/3 capability so applications/libraries can communicate with HTTP/3 servers with minimal API change.

HTTP/3 runs over QUIC/UDP and changes transport behavior, connection establishment and network middlebox considerations.

You should not assume setting HTTP/3 always faster. Server/network support, loss pattern, connection reuse and fallback matter.

Existing HttpClient API abstraction demonstrates good library evolution: protocol capability can improve without rewriting application request model.

---

# 150. Java 26 Structured Concurrency Sixth Preview

Structured Concurrency remains preview in Java 26.

The API treats related concurrent subtasks as one unit for join, failure/cancellation and observability.

Even if signatures change, key design lesson is stable: child tasks should have bounded lifetime nested inside parent operation.

This avoids “fire future into global executor and forget ownership”.

---

# 151. Java 26 Primitive Patterns Fourth Preview

Pattern matching continues expanding to primitives in `instanceof`/switch contexts as preview.

Goal is uniform data-oriented pattern matching and safe conversion semantics.

Because preview can change, don't write library baseline requiring it unless project explicitly uses Java 26 preview.

Learn semantics but keep stable production code on final features by default.

---

# 152. Java 26 Lazy Constants

Java 26 contains second preview of Lazy Constants API.

A lazy constant is initialized at most once on demand but then treated with constant-like immutability/optimization semantics.

This addresses “expensive final value but don't want initialize at class load” use cases more explicitly than ad-hoc double-checked locking.

Because it is preview, exact API should be read from Java 26 docs before use.

---

# 153. Java 26 Vector API vẫn là Incubator

Vector API remains incubator in Java 26.

It lets developers express SIMD computations that JIT maps to vector CPU instructions predictably.

Use cases: numeric processing, codecs, ML primitives, cryptography-like loops where supported.

Not normal CRUD tool.

Incubator status means package/module/API can change; libraries should avoid exposing incubator types in stable public API.

---

# 154. Choosing release baseline

Application production baseline should follow:

```text
framework support
vendor support
runtime/container certification
library compatibility
operations capability
security update policy
```

Learning baseline can be newer.

For a Spring Boot 4 application, Java 21 or 25 may be practical depending organization. For internal library supporting broad consumers, baseline might stay 17/21.

Don't confuse “latest feature knowledge” with “must deploy latest non-LTS”.

---

# 155. Master practical project A: build a bounded executor

Implement a small `Executor`/task queue wrapper around `ThreadPoolExecutor` with explicit bounded queue, rejection policy, metrics, graceful shutdown and cancellation.

Write load test where producer outpaces consumer.

Observe queue latency, rejection and memory.

Then compare with virtual-thread-per-task + Semaphore bulkhead.

Goal is not outperform JDK; goal is internalize capacity model.

---

# 156. Master practical project B: mini Flow publisher

Implement a simple `Flow.Publisher<T>` supporting one or multiple subscribers.

Correctly handle:

```text
onSubscribe
request(n)
cancel
onNext
onComplete
onError
```

Never emit more than requested.

Test slow subscriber.

You will quickly understand why reactive libraries are complex and why protocol correctness matters.

---

# 157. Master practical project C: NIO echo server

Build Selector-based TCP echo server.

Maintain per-connection read/write buffers.

Handle partial reads/writes, OP_WRITE registration, disconnect, malformed input and backpressure.

Then compare code complexity with virtual-thread blocking server.

This gives concrete intuition for event-loop vs thread-per-connection models.

---

# 158. Master practical project D: Java Agent

Write agent that records method entry counts for selected package.

Use Instrumentation + ClassFile API or mature bytecode library.

Avoid instrumenting agent itself recursively.

Add JFR custom event.

You will learn class loading timing, bytecode transformation and agent risk.

---

# 159. Master practical project E: FFM

Call a simple C function such as `strlen` or small custom native library using FFM.

Then map a native struct with MemoryLayout.

Experiment with confined Arena lifetime and access-after-close exception.

Do one callback/upcall to understand lifetime.

This teaches native ownership without full JNI boilerplate.

---

# 160. Master practical project F: ReferenceQueue

Create objects referenced only through WeakReference/PhantomReference and observe ReferenceQueue notifications under GC pressure.

Build small cleanup tracker with explicit close + Cleaner fallback.

Goal is understand reachability/lifecycle, not build production cache.

---

# 161. Master practical project G: JDK upgrade lab

Take Java 8/11 style project.

Upgrade stepwise to 17, 21, 25.

Use:

```text
jdeps
jdeprscan
--release
GC logs
JFR
dependency tree
tests
```

Replace internal APIs, legacy date/time, old HTTP client, illegal reflection.

Benchmark startup/throughput/memory after each major jump.

This is one of the most valuable real enterprise mastery exercises.

---

# 162. Master self-check: concurrency

Bạn nên có thể giải thích tại sao VarHandle có plain/opaque/acquire/release/volatile modes và khi nào không nên dùng. Bạn phải hiểu LockSupport permit/spurious wake, AQS exclusive/shared mode, ThreadLocal leak, ScopedValue lifecycle, ForkJoin work stealing, blocking queue backpressure và cancellation ownership.

Quan trọng hơn, bạn phải biết khi nào **không** viết low-level code và chọn high-level utility.

---

# 163. Master self-check: runtime

Bạn nên đọc được `javap -v` ở mức nhận biết constant pool, descriptor, bytecode, invokedynamic, synthetic/bridge methods.

Bạn phải giải thích class loading/linking/initialization, loader identity, classloader leak, strong encapsulation, hidden classes và agents.

Bạn không cần viết bytecode bằng tay nhưng phải hiểu framework instrumentation hoạt động ở layer nào.

---

# 164. Master self-check: memory/GC

Bạn phải phân biệt heap, metaspace, code cache, direct/native memory, thread stacks.

Bạn phải hiểu GC roots, TLAB, barriers/card tables, safepoints và collector trade-offs.

Khi RSS cao nhưng heap thấp, bạn biết dùng NMT/thread/direct buffer clues thay vì chỉ tăng Xmx.

Khi heap leak, bạn biết path-to-GC-root/ownership trước collector tuning.

---

# 165. Master self-check: systems I/O

Bạn phải hiểu Selector readiness, partial I/O, event-loop blocking và OP_WRITE busy-spin. Bạn phải hiểu file descriptor limits, child-process pipe deadlock, DNS/proxy/TLS layers và HTTP deadline/backpressure.

Bạn phải biết virtual threads thay đổi thread scaling nhưng không thay downstream resource capacity.

---

# 166. Master self-check: library engineering

Bạn phải hiểu generic erasure/reifiable/bridge/wildcard capture, API source/binary/behavioral compatibility, extension point risks, Javadoc contract, thread-safety documentation và ownership.

Bạn phải biết ServiceLoader/module layer/classloader/plugin boundary, multi-release JAR và module naming.

Public API là long-term compatibility commitment, không chỉ `public` keyword.

---

# 167. Master self-check: native/security

Bạn phải phân biệt hash/MAC/signature/encryption, key/trust store, provider model và SecureRandom.

Bạn phải hiểu FFM MemorySegment/Arena/lifetime, JNI/native crash risk và vì sao Unsafe nên được thay bằng supported APIs.

Bạn không cần tự viết crypto protocol hay native allocator; mastery bao gồm biết specialist boundary và không tự phát minh thứ nguy hiểm.

---

# 168. Master self-check: modern JDK

Bạn phải biết feature nào final và feature nào preview/incubator.

Java 25: LTS, Scoped Values final, modern language simplifications, runtime improvements.

Java 26: HTTP/3 standard client capability, Structured Concurrency vẫn preview, primitive pattern matching vẫn preview, Lazy Constants preview và Vector API incubator.

Bạn phải có thói quen đọc JEP/release docs thay vì nhớ blog.

---

# 169. Master learning pyramid

Lớp đầu là language/type system: generics, overloading, initialization, sealed/patterns.

Lớp hai là core libraries: collections, streams/gatherers, concurrency, I/O/networking, security, time, Flow.

Lớp ba là runtime: class files, class loading, JIT, GC, memory model, references, native memory.

Lớp bốn là systems: OS files/sockets/processes/signals/native interoperability, observability.

Lớp năm là library/framework engineering: SPI, annotation processing, agents, compatibility, modules, API contracts.

Lớp sáu là evolution: JEPs, preview/incubator, release upgrade strategy.

Bạn không “hoàn thành một lớp rồi không bao giờ quay lại”. Mastery là quay lại các lớp khi gặp problem thật và đào sâu bằng evidence/source.

---

# 170. Priority học sau ba file core

Nếu mục tiêu của bạn là Java backend/Spring Senior, ưu tiên cao nhất trong supplement là ThreadLocal/ScopedValue, ForkJoin/common-pool awareness, references/Cleaner, Selector mental model, class loading/linkage errors, annotation processing/agents awareness, FFM awareness, GC barriers/object layout overview, JFR/JMX/tooling, compatibility và modern JDK 25/26.

VarHandle/AQS/MethodHandle/Class-File API/ModuleLayer/FFM deep internals là ưu tiên tiếp theo khi bạn đọc framework/JDK source hoặc build infrastructure.

False sharing, custom classloader, bytecode transformers, lock-free CAS algorithms và native ABI details là specialist depth. Học khi công việc hoặc curiosity cần, không phải prerequisites để làm tốt Spring backend.

---

# 171. Khi nào có thể nói “Master Java”?

Không có exam chính thức biến bạn thành master. Một dấu hiệu thực tế là bạn có thể gặp một behavior lạ và biết **đúng layer để điều tra**.

`NoSuchMethodError` → binary dependency/classloader.

Latency high CPU low → waits, locks, I/O, pools.

RSS high heap normal → native/direct/thread/metaspace.

Transactional framework annotation không chạy → proxy/instrumentation/call path.

Virtual threads nhiều nhưng throughput không tăng → downstream capacity/CPU/pinning.

Memory leak → reachability/ownership/path-to-root.

Library upgrade break → source/binary/behavioral compatibility.

Khi bạn có thể dịch framework symptoms về Java/JVM/OS contracts và đọc source/docs để xác minh, đó là level mastery có giá trị.

---

# 172. Nguồn nên đọc sau supplement

**Java Language Specification (JLS)** là nguồn chuẩn cho language semantics: overload, generics, initialization, expressions, memory model language-level rules.

**Java Virtual Machine Specification (JVMS)** giải class files, bytecode, loading/linking, verification, instruction set.

**Java SE API Javadocs** là contract chính thức của libraries. Đọc phần class-level documentation và method contracts, không chỉ signatures.

**OpenJDK JEPs** giải motivation, design, alternatives và status của new features.

**OpenJDK source** cho implementation. Đừng nhầm implementation hiện tại với specification guarantee.

**JFR/JDK tooling docs** giúp chuyển knowledge thành production diagnostics.

---

# 173. Cách đọc OpenJDK source

Đừng bắt đầu bằng `HotSpot` C++ code nếu chưa có câu hỏi.

Bắt đầu từ class Java bạn đã biết, ví dụ `ConcurrentHashMap`, `CompletableFuture`, `ReentrantLock`, `ArrayList`.

Đọc public contract trước, rồi fields, helper methods và comments.

Khi gặp native/intrinsic, trace xuống HotSpot nếu câu hỏi cần.

Luôn phân biệt:

```text
specification says must
implementation happens to do
```

Một optimization/internal field không phải public contract.

---

# 174. Cách đọc JEP

JEP thường có sections:

```text
Summary
Goals
Non-Goals
Motivation
Description
Alternatives
Risks
```

Đừng chỉ đọc Summary.

Non-Goals rất quan trọng để tránh kỳ vọng sai.

Risks/Alternatives cho biết trade-offs đã cân nhắc.

Preview JEPs có thể thay qua multiple releases; compare versions để hiểu feedback-driven evolution.

---

# 175. Cách học low-level mà không sa vào trivia

Mỗi chủ đề hãy gắn với một câu hỏi thực tế.

VarHandle: “memory ordering nào cần cho lock-free state?”

AQS: “ReentrantLock park/wake waiters thế nào?”

Class-file API: “agent sửa bytecode ra sao?”

FFM: “Java quản lý native memory lifetime thế nào?”

GC barriers: “young GC biết old→young references ở đâu?”

Selector: “một thread phục vụ nhiều sockets mà không polling busy thế nào?”

Nếu không có question/use case, low-level details biến thành trivia dễ quên.

---

# 176. Final roadmap sau Java Master Supplement

Sau bốn file:

```text
01 Java Beginner
02 Java Intermediate
03 Java Senior
04 Java Master Supplement
```

không nên tiếp tục tạo “Java Advanced++++” chung nữa. Từ đây, mastery nên tách theo chuyên môn.

Một Java backend engineer có thể đi sâu **Spring/Spring Boot**, persistence/JPA/SQL, distributed systems, security, Kafka/messaging, observability và cloud.

Một JVM/performance engineer đi sâu HotSpot, GC, JIT compiler, profiling, Linux/perf, hardware performance counters.

Một library/framework engineer đi sâu class-file, agents, MethodHandles, annotation processing, JPMS, compatibility và API design.

Một systems Java engineer đi sâu NIO/Netty, FFM/native, protocols và low-latency concurrency.

Mastery thực tế là depth ở một hoặc vài nhánh, trong khi vẫn giữ mental model rộng của Java platform.

---

# 177. Version-sensitive references

Oracle Java SE Support Roadmap  
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle Java Downloads / current releases  
https://www.oracle.com/java/technologies/downloads/

JDK 25 release notes  
https://www.oracle.com/java/technologies/javase/25-relnote-issues.html

JDK 26 release notes  
https://www.oracle.com/java/technologies/javase/26-relnote-issues.html

Java 24 Gatherers API  
https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/stream/Gatherers.html

Foreign Function and Memory API  
https://docs.oracle.com/en/java/javase/22/core/foreign-function-and-memory-api.html

Java Language Specification  
https://docs.oracle.com/javase/specs/

OpenJDK JEP Index  
https://openjdk.org/jeps/0

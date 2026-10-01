# Java cốt lõi (core / 핵심) — Master Supplement — Rewritten Detailed

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Java cốt lõi (core / 핵심) — Master Supplement — Rewritten Detailed**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Low-level thời gian chạy (runtime / 런타임), thư viện (library / 라이브러리) kỹ thuật (engineering / 엔지니어링), hiện đại (modern / 현대적) JDK và những phần còn thiếu để tiến tới “Master Java”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vị trí của Master Supplement trong mạch học (learning flow / 학습 흐름)** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Low-level thời gian chạy (runtime / 런타임), thư viện (library / 라이브러리) kỹ thuật (engineering / 엔지니어링), hiện đại (modern / 현대적) JDK và những phần còn thiếu để tiến tới “Master Java”

> Tài liệu này là phần thứ tư sau **Beginner → Intermediate → cấp cao (senior / 시니어)**. Nó không lặp lại cú pháp Java, Collections, Stream cơ bản, JDBC căn bản, JMM căn bản hay JVM/GC overview đã có ở ba tệp (file / 파일) trước. Mục tiêu ở đây là đi vào những vùng mà một cấp cao (senior / 시니어) ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자) có thể chưa cần dùng hằng ngày nhưng một người muốn hiểu Java ở mức (level / 수준) “master” cần biết: low-level tính đồng thời (concurrency / 동시성) primitives, class-file/thời gian chạy (runtime / 런타임) machinery, bản địa (native / 네이티브) interoperability, tham chiếu (reference / 참조) processing, selector/event-loop, thư viện (library / 라이브러리) extension points, bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) tooling, API tính tương thích (compatibility / 호환성) và evolution của JDK hiện đại.
>
> Các phần “cấp cao (senior / 시니어) ghi chú (note / 노트)”, “lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)”, “mẫu lập trình (programming pattern / 프로그래밍 패턴)”, “mẫu thiết kế (design pattern / 디자인 패턴)” không được tách thành các box lặp đi lặp lại. Khi một mẫu (pattern / 패턴) hoặc nguyên tắc quan trọng, nó được giải thích trực tiếp tại chỗ cùng với nguyên nhân, dạng thất bại (failure mode / 실패 모드) và sự đánh đổi (trade-off / 트레이드오프). Mục tiêu là đọc như một cuốn sách học, không phải một cheat sheet.
>
> Baseline phiên bản (version / 버전) của supplement này là **Java 25 LTS** với awareness tới **Java 26**, là bản phát hành (release / 릴리스) mới nhất tại thời điểm cập nhật. Java 26 là non-LTS; Java 25 là LTS hiện tại. Các preview/incubator APIs được đánh dấu rõ để tránh nhầm với API final.

> **Chuyển mạch:** Trong **Java cốt lõi (core / 핵심) — Master Supplement — Rewritten Detailed**, **Low-level thời gian chạy (runtime / 런타임), thư viện (library / 라이브러리) kỹ thuật (engineering / 엔지니어링), hiện đại (modern / 현대적) JDK và những phần còn thiếu để tiến tới “Master Java”** xác định đầu vào; **Vị trí của Master Supplement trong mạch học (learning flow / 학습 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tại sao Master vẫn phải hiểu Java 8 → 11 → 17 → 21 thay vì chỉ nhìn Java 25/26** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vị trí của Master Supplement trong mạch học (learning flow / 학습 흐름)

Master Supplement chỉ nên đọc sau [Java Part 3 — Senior](./java_part3_senior_rewritten_detailed.md). Đây không phải “Part 3 nhưng nhiều API hơn”; nó là phần bù cho low-level thời gian chạy (runtime / 런타임), khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) kỹ thuật (engineering / 엔지니어링) và hiện đại (modern / 현대적) JDK internals. Nếu một chủ đề application-level đã được giải thích đủ ở ba phần trước, tệp (file / 파일) này không lặp lại chỉ để tăng số lượng nội dung.

---

# 1. “Master Java” thực sự có nghĩa gì?

Master Java không có nghĩa là thuộc hết `java.*` hoặc nhớ mọi option của JVM. JDK quá lớn và thay đổi theo từng bản phát hành (release / 릴리스). Người thực sự giỏi Java có ba năng lực quan trọng hơn trí nhớ API.

Thứ nhất, họ hiểu **mô hình ngữ nghĩa (semantic model / 의미 모델)**. Khi thấy một API mới, họ hỏi quyền sở hữu (ownership / 소유권), mutability, tính đồng thời (concurrency / 동시성), vòng đời (lifecycle / 생명주기), lỗi (error / 오류) và tính tương thích (compatibility / 호환성) contracts. Thứ hai, họ hiểu **thời gian chạy (runtime / 런타임)** đủ sâu để giải thích hiện tượng môi trường vận hành (production / 운영 환경): lớp (class / 클래스) nào được tải (load / 로드) bởi loader nào, đối tượng (object / 객체) nào đang giữ bộ nhớ (memory / 메모리), luồng thực thi (thread / 스레드) đang parked hay blocked, JIT có thể inline/deoptimize ra sao, GC barrier có vai trò gì. Thứ ba, họ biết **tìm bằng chứng** trong JLS, JVMS, Javadoc, OpenJDK nguồn (source / 소스), JEP, JFR, `jcmd`, vùng nhớ động (heap / 힙) dump và lớp (class / 클래스) files thay vì đoán.

Do đó supplement này chủ yếu dạy cách “mở nắp” Java. Nhiều API ở đây bạn có thể không bao giờ dùng trực tiếp trong CRUD backend, nhưng hiểu chúng giúp bạn đọc nguồn (source / 소스) Spring, Netty, Reactor, Hibernate, Kafka máy khách (client / 클라이언트), logging libraries hoặc JDK itself mà không thấy chúng như black box.

---

# 2. phiên bản (version / 버전) chiến lược (strategy / 전략): Java 25 LTS, Java 26 và vì sao không nên dừng ở Java 21

Java 8, 11, 17, 21 và 25 là các LTS generations quan trọng. Java 25 là LTS hiện tại; Java 26 là tính năng (feature / 기능) bản phát hành (release / 릴리스) hiện tại nhưng không phải LTS. Khi vận hành enterprise, bạn có thể vẫn ở 17 hoặc 21 vì khung phần mềm (framework / 프레임워크)/vendor chính sách (policy / 정책). Khi học, bạn nên biết những gì đã final ở 25 và những gì mới/preview ở 26 để không bị mắc kẹt trong mô hình tư duy (mental model / 사고 모델) cũ.

Điều quan trọng là phân biệt **ngôn ngữ (language / 언어) tính năng (feature / 기능)**, **thư viện (library / 라이브러리) API**, **JVM/thời gian chạy (runtime / 런타임) tính năng (feature / 기능)** và **tooling tính năng (feature / 기능)**. Ví dụ Scoped Values là thư viện (library / 라이브러리)/thời gian chạy (runtime / 런타임) API final ở Java 25. Stream Gatherers trở thành tiêu chuẩn (standard / 표준) API ở Java 24. Foreign hàm (function / 함수) & bộ nhớ (memory / 메모리) API final ở Java 22. Class-File API trở thành tiêu chuẩn (standard / 표준) ở Java 24. HTTP/3 hỗ trợ (support / 지원) cho `HttpClient` xuất hiện trong Java 26. Structured tính đồng thời (concurrency / 동시성) ở Java 26 vẫn là preview, nên chính xác (exact / 정확한) API có thể tiếp tục đổi.

Khi đọc một bài viết, hãy hỏi “tính năng (feature / 기능) này final ở bản phát hành (release / 릴리스) nào?” trước khi dùng trong thư viện (library / 라이브러리) môi trường vận hành (production / 운영 환경). Preview API thường yêu cầu `--enable-preview`, gắn với đúng bản phát hành (release / 릴리스) và không mang tính tương thích (compatibility / 호환성) guarantee như tiêu chuẩn (standard / 표준) API.

---

# 3. VarHandle: khi `volatile` và Atomic classes chưa đủ

`VarHandle` là low-level typed tham chiếu (reference / 참조) tới variable-like lưu trữ (storage / 저장소) location. Nó cho phép đọc, ghi và atomic cập nhật (update / 업데이트) với **bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) ngữ nghĩa (semantics / 의미론)** rõ hơn `volatile` trường dữ liệu (field / 필드) đơn thuần. Đây là API chính thức thay thế nhiều use trường hợp (case / 사례) trước đây phải dựa vào `sun.misc.Unsafe`.

Giả sử lớp (class / 클래스) có trường dữ liệu (field / 필드):

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

Điểm đáng học không phải cú pháp (syntax / 문법) lookup, mà là **truy cập (access / 접근) modes**. `get`/`set` có plain ngữ nghĩa (semantics / 의미론). `getOpaque`/`setOpaque` cung cấp weaker thứ tự (ordering / 순서). `getAcquire` và `setRelease` tạo acquire/bản phát hành (release / 릴리스) thứ tự (ordering / 순서). `getVolatile`/`setVolatile` cho strongest volatile-style thứ tự (ordering / 순서). Ngoài ra còn CAS, compare-and-exchange, get-and-add và bitwise atomics tùy kiểu (type / 타입).

Nếu bạn đang viết ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스) bình thường, dùng `volatile`, `AtomicInteger`, `AtomicReference` hoặc locks dễ đúng hơn. `VarHandle` hợp khi xây concurrent thư viện (library / 라이브러리)/cấu trúc dữ liệu (data structure / 자료구조) và cần kiểm soát chính xác bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) để tránh chi phí (cost / 비용) không cần thiết.

---

# 4. Acquire/bản phát hành (release / 릴리스)/Opaque: bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) không chỉ có “volatile hoặc không”

Một lỗi phổ biến là nghĩ Java bộ nhớ (memory / 메모리) mô hình (model / 모델) chỉ có hai mức: normal trường dữ liệu (field / 필드) và volatile trường dữ liệu (field / 필드). Thực tế low-level APIs có thứ tự (ordering / 순서) strength khác nhau.

**Plain** truy cập (access / 접근) gần ordinary trường dữ liệu (field / 필드) truy cập (access / 접근), không tạo synchronization thứ tự (ordering / 순서) đặc biệt.

**Opaque** đảm bảo một mức coherence tối thiểu cho cùng variable nhưng cho phép reorder rộng hơn volatile. Nó hữu ích cho low-level progress/status thông tin (information / 정보) nơi bạn không cần publish cả đối tượng (object / 객체) đồ thị (graph / 그래프).

**bản phát hành (release / 릴리스) ghi (write / 쓰기)** đảm bảo writes trước nó không bị reorder đi sau bản phát hành (release / 릴리스). **Acquire read** đảm bảo reads/writes sau nó không bị reorder đi trước acquire. Khi một bản phát hành (release / 릴리스) store được paired với acquire tải (load / 로드) quan sát giá trị đó, bạn có publication thứ tự (ordering / 순서) giống một one-way handoff.

**Volatile** mạnh hơn, tạo total synchronization thứ tự (order / 순서) theo JMM cho volatile actions.

Bạn không nên chọn weaker chế độ (mode / 모드) chỉ vì “nhanh hơn”. Chọn chế độ (mode / 모드) yếu hơn nghĩa bạn đang viết proof về bộ nhớ (memory / 메모리) thứ tự (ordering / 순서). Nếu proof sai, bug có thể chỉ xuất hiện trên kiến trúc (architecture / 아키텍처)/JIT/tải (load / 로드) nhất định. Đây là territory của concurrent thư viện (library / 라이브러리) authors.

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

cho phép atomic chuyển tiếp trạng thái (state transition / 상태 전이) không dùng monitor khóa (lock / 잠금).

Một lock-free máy trạng thái (state machine / 상태 머신) có thể dùng immutable trạng thái (state / 상태):

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

Điểm khó nằm ở invariants, thử lại (retry / 재시도) hành vi (behavior / 동작), ABA và progress guarantees. CAS vòng lặp (loop / 루프) không tự động tốt hơn khóa (lock / 잠금). Nếu contention cao, nhiều threads có thể spin/thử lại (retry / 재시도) và đốt CPU. Nếu chuyển tiếp (transition / 전이) expensive, recomputation chi phí (cost / 비용) cũng lớn. High-level khóa (lock / 잠금) hoặc `AtomicReference` thường rõ hơn.

Một thư viện (library / 라이브러리) tốt sẽ đóng `VarHandle` bên trong lớp (class / 클래스) và expose API an toàn; caller không cần hiểu bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) của từng trường dữ liệu (field / 필드). Đây là nguyên tắc quan trọng của low-level thư viện (library / 라이브러리) thiết kế (design / 설계): **encapsulate bộ nhớ (memory / 메모리) ngữ nghĩa (semantics / 의미론)**.

---

# 6. LockSupport: thành phần nguyên thủy (primitive / 기본 요소) phía dưới nhiều synchronizers

`LockSupport` cung cấp:

```java
LockSupport.park();
LockSupport.unpark(thread);
```

Nó là thành phần nguyên thủy (primitive / 기본 요소) parking/unparking được dùng trong nhiều synchronizers của `java.util.concurrent`.

Mô hình tư duy (mental model / 사고 모델) quan trọng là **permit**. Một luồng thực thi (thread / 스레드) có tối đa conceptually một permit. `unpark(thread)` làm permit available; nếu luồng thực thi (thread / 스레드) sau đó `park()`, permit được consume và luồng thực thi (thread / 스레드) có thể tiếp tục ngay. Nếu `park()` xảy ra trước, luồng thực thi (thread / 스레드) khối (block / 블록) cho tới unpark, interruption hoặc spurious return.

Điều này khác `Object.wait()` ở chỗ không cần monitor giao thức (protocol / 프로토콜) như `synchronized` + `notify`, và `unpark` trước `park` không bị “mất tín hiệu (signal / 신호)” theo cùng cách.

Tuy nhiên `park()` **có thể return spuriously**, nên luôn phải nằm trong điều kiện (condition / 조건) vòng lặp (loop / 루프):

```java
while (!condition()) {
    LockSupport.park();
}
```

Đừng dùng `LockSupport` để viết hàng đợi (queue / 큐)/synchronizer application-level nếu `BlockingQueue`, Semaphore, khóa (lock / 잠금) hoặc latch đã phù hợp. Nó là building khối (block / 블록) cho thư viện (library / 라이브러리) internals.

---

# 7. AbstractQueuedSynchronizer: nền của nhiều locks trong JDK

`AbstractQueuedSynchronizer`, thường gọi AQS, là khung phần mềm (framework / 프레임워크) để xây blocking synchronizers. `ReentrantLock`, `Semaphore`, `CountDownLatch` và nhiều utilities dựa trên hoặc liên quan mẫu (pattern / 패턴) này.

AQS quản lý một integer trạng thái (state / 상태) và một hàng đợi (queue / 큐) của waiting nodes/threads. Subclass định nghĩa ý nghĩa trạng thái (state / 상태) bằng các methods như conceptually `tryAcquire`, `tryRelease`, `tryAcquireShared`, `tryReleaseShared`. AQS lo phần khó của queueing, parking, wake-up và cancellation.

Trong **exclusive chế độ (mode / 모드)**, chỉ một đơn vị sở hữu (owner / 오너) hoặc một limited quyền sở hữu (ownership / 소유권) trạng thái (state / 상태) được acquire, như khóa (lock / 잠금). Trong **dùng chung (shared / 공유) chế độ (mode / 모드)**, nhiều threads có thể proceed khi dùng chung (shared / 공유) permits/trạng thái (state / 상태) cho phép, như semaphore/latch.

Bạn không cần subclass AQS để viết backend ứng dụng (application / 애플리케이션). Nhưng nếu đọc JDK concurrent nguồn (source / 소스) hoặc một custom thư viện (library / 라이브러리), hiểu AQS giúp bạn thấy `ReentrantLock.lock()` không phải magic: fast đường dẫn (path / 경로) thử acquire trạng thái (state / 상태), slow đường dẫn (path / 경로) enqueue, park, wake và thử lại (retry / 재시도).

---

# 8. Reentrancy và vì sao thư viện (library / 라이브러리) APIs phải document nó

Một synchronizer **reentrant** cho phép luồng thực thi (thread / 스레드) đang giữ khóa (lock / 잠금) acquire lại same khóa (lock / 잠금) mà không deadlock chính nó. `ReentrantLock` và Java intrinsic monitors có reentrant hành vi (behavior / 동작).

Reentrancy có lợi khi công khai (public / 공개) phương thức (method / 메서드) giữ khóa (lock / 잠금) gọi private/helper phương thức (method / 메서드) cũng cần same bất biến (invariant / 불변식).

Nhưng reentrancy làm lập luận (reasoning / 추론) phức tạp nếu unknown callback chạy trong locked section. Callback có thể gọi ngược vào đối tượng (object / 객체), thay trạng thái (state / 상태) ở một điểm (point / 지점) bạn không dự kiến.

Một API thread-safe nên document rằng callbacks có được gọi dưới khóa (lock / 잠금) không. Tốt hơn, nhiều thư viện (library / 라이브러리) designs bản sao (copy / 복사) dữ liệu (data / 데이터)/prepare callback rồi bản phát hành (release / 릴리스) khóa (lock / 잠금) trước khi gọi unknown mã (code / 코드), miễn bất biến (invariant / 불변식) cho phép.

“Không gọi unknown mã (code / 코드) dưới khóa (lock / 잠금)” là một nguyên tắc cực mạnh vì unknown mã (code / 코드) có thể khối (block / 블록), acquire locks khác, throw, reenter hoặc lời gọi (call / 호출) remote I/O.

---

# 9. ThreadLocal internals và lý do leak trong luồng thực thi (thread / 스레드) pool

`ThreadLocal<T>` không phải một toàn cục (global / 전역) map từ luồng thực thi (thread / 스레드) ID tới giá trị (value / 값) do ThreadLocal đối tượng (object / 객체) giữ. Mỗi `Thread` conceptually có một nội bộ (internal / 내부) ThreadLocalMap; ThreadLocal đối tượng (object / 객체) đóng vai trò key.

Điều này tạo vòng đời (lifecycle / 생명주기) trap trong luồng thực thi (thread / 스레드) pool. Worker luồng thực thi (thread / 스레드) sống rất lâu:

```text
request A
→ ThreadLocal.set(userA)
→ task kết thúc nhưng không remove
→ worker thread vẫn sống
→ value vẫn bị retain
```

Yêu cầu (request / 요청) B có thể reuse luồng thực thi (thread / 스레드) và thấy stale ngữ cảnh (context / 맥락) nếu mã (code / 코드) không overwrite đúng, đồng thời bộ nhớ (memory / 메모리) được giữ lâu.

Mẫu (pattern / 패턴):

```java
try {
    CONTEXT.set(context);
    work();
} finally {
    CONTEXT.remove();
}
```

Nếu ThreadLocal chứa đối tượng (object / 객체) đồ thị (graph / 그래프) lớn, leak càng nghiêm trọng.

Một subtle detail là ThreadLocalMap dùng weak references cho keys nhưng values có thể vẫn được giữ cho tới cleanup khi key đã GC. Vì vậy “ThreadLocal key là weak nên không leak” là hiểu sai.

---

# 10. InheritableThreadLocal và vì sao nó không giải ngữ cảnh (context / 맥락) propagation hiện đại

`InheritableThreadLocal` bản sao (copy / 복사)/inherit giá trị (value / 값) khi child luồng thực thi (thread / 스레드) được tạo. Điều này có vẻ tiện cho yêu cầu (request / 요청) ngữ cảnh (context / 맥락), nhưng luồng thực thi (thread / 스레드) pools reuse threads nên “child creation” không trùng tác vụ (task / 작업) ranh giới (boundary / 경계). ngữ cảnh (context / 맥락) có thể không cập nhật (update / 업데이트) như mong đợi.

Virtual threads tạo nhiều threads mới hơn nên inheritance ngữ nghĩa (semantics / 의미론) khác luồng thực thi (thread / 스레드) pool reuse, nhưng immutable scoped ngữ cảnh (context / 맥락) vẫn là mô hình (model / 모델) dễ reason hơn.

Trong khung phần mềm (framework / 프레임워크) ecosystem, tracing/bảo mật (security / 보안)/MDC có dedicated propagation mechanisms. Không nên tự xây toàn cục (global / 전역) yêu cầu (request / 요청) ngữ cảnh (context / 맥락) bằng `InheritableThreadLocal` rồi hy vọng mọi executor/reactive chuỗi xử lý (pipeline / 파이프라인) đúng.

---

# 11. ScopedValue: immutable scoped ngữ cảnh (context / 맥락) của Java 25

Scoped Values final ở Java 25. Ý tưởng là share immutable contextual giá trị (value / 값) tới callees trong một động (dynamic / 동적) phạm vi (scope / 범위) mà không cần mutable per-thread slot như ThreadLocal.

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

Bên trong phạm vi (scope / 범위):

```java
UserContext context =
    USER.get();
```

Điểm mạnh là binding có lexical/động (dynamic / 동적) phạm vi (scope / 범위) rõ. Sau khi phạm vi (scope / 범위) kết thúc, binding biến mất. Caller không “quên remove” như ThreadLocal.

ScopedValue phù hợp read-only ngữ cảnh (context / 맥락) như yêu cầu (request / 요청) ID, bảo mật (security / 보안) định danh (identity / 식별자), tracing siêu dữ liệu (metadata / 메타데이터), tenant ngữ cảnh (context / 맥락), đặc biệt khi dùng cùng virtual threads và structured tính đồng thời (concurrency / 동시성).

Nó không phải replacement cho ordinary phương thức (method / 메서드) parameters mọi nơi. Nếu phụ thuộc (dependency / 의존성) là nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) cần rõ trong API, vẫn truyền parameter. ScopedValue hợp contextual dữ liệu (data / 데이터) cross-cutting.

---

# 12. ScopedValue vs ThreadLocal

ThreadLocal phù hợp mutable thread-local trạng thái (state / 상태) và legacy APIs, nhưng vòng đời (lifecycle / 생명주기) dễ mơ hồ.

ScopedValue hướng tới immutable contextual binding. Child thực thi (execution / 실행) có thể inherit ngữ cảnh (context / 맥락) theo structured mechanisms và binding không thể tùy tiện mutate.

Nếu bạn cần một counter mutable cục bộ (local / 로컬) luồng thực thi (thread / 스레드), ScopedValue không phải công cụ (tool / 도구) tương đương. Nếu bạn cần “yêu cầu (request / 요청) ngữ cảnh (context / 맥락) đọc ở many layers” mà không muốn mutable hidden trạng thái (state / 상태), ScopedValue có mô hình tư duy (mental model / 사고 모델) tốt hơn.

Một master-level lesson là không biến ngữ cảnh (context / 맥락) cơ chế (mechanism / 메커니즘) thành phụ thuộc (dependency / 의존성) injection substitute. người dùng (user / 사용자) ID có thể là contextual ở logging/bảo mật (security / 보안) tầng (layer / 계층) nhưng command handler nghiệp vụ (business / 비즈니스) cần người dùng (user / 사용자) ID để quyết định permission thì tường minh (explicit / 명시적) parameter hoặc bảo mật (security / 보안) lớp trừu tượng (abstraction / 추상화) có thể rõ hơn.

---

# 13. ForkJoinPool và công việc (work / 작업) Stealing

`ForkJoinPool` được thiết kế cho tác vụ (task / 작업) decomposition, đặc biệt CPU-bound recursive computations.

Worker có cục bộ (local / 로컬) deque. Khi worker hết việc, nó **steal** tác vụ (task / 작업) từ worker khác. công việc (work / 작업) stealing giúp balance tải (load / 로드) với less centralized contention.

`RecursiveTask<V>` trả kết quả (result / 결과):

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

# 14. dùng chung (common / 공통) ForkJoinPool và hidden dùng chung (shared / 공유) sức chứa (capacity / 용량)

Parallel streams và một số CompletableFuture async operations có thể dùng dùng chung (common / 공통) pool.

Điều này tạo hidden coupling: tính năng (feature / 기능) A chạy CPU-heavy parallel stream và tính năng (feature / 기능) B dùng `CompletableFuture.supplyAsync()` không executor; chúng tranh same pool.

Blocking I/O trong dùng chung (common / 공통) ForkJoinPool có thể giảm available workers. `ForkJoinPool.ManagedBlocker` tồn tại cho advanced cases để pool biết blocking và có thể compensate workers, nhưng ứng dụng (application / 애플리케이션) mã (code / 코드) thường nên tránh dùng dùng chung (common / 공통) pool cho uncontrolled blocking.

Nếu sức chứa (capacity / 용량)/thất bại (failure / 실패) isolation quan trọng, tạo tường minh (explicit / 명시적) executor.

---

# 15. Spliterator: engine traversal phía dưới Stream

`Spliterator<T>` có hai responsibilities: traverse elements và split nguồn (source / 소스) thành parts để parallel processing.

Cốt lõi (core / 핵심) methods conceptually:

```java
boolean tryAdvance(
    Consumer<? super T> action);

Spliterator<T> trySplit();

long estimateSize();

int characteristics();
```

`trySplit()` trả một spliterator khác đại diện một portion, trong khi original giữ phần còn lại. Parallel stream dùng cơ chế này để partition công việc (work / 작업).

ArrayList có thể split rất tốt theo chỉ mục (index / 인덱스) ranges. Linked cấu trúc (structure / 구조) khó split cân bằng hơn.

Nếu bạn viết custom dữ liệu (data / 데이터) nguồn (source / 소스) và muốn stream parallel hiệu quả, custom Spliterator quan trọng hơn custom Stream lớp (class / 클래스).

---

# 16. Spliterator characteristics

Characteristics mô tả đặc tả hợp đồng (contract / 계약) dữ liệu (data / 데이터) nguồn (source / 소스):

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

Stream thời gian chạy (runtime / 런타임) có thể optimize dựa thông tin (information / 정보) này.

Đừng khai sai. Nếu bạn claim `SIZED` nhưng estimate không chính xác theo đặc tả hợp đồng (contract / 계약), downstream optimizations có thể sai. Nếu claim `SORTED`, comparator/thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론) phải đúng.

Một mẫu (pattern / 패턴) chung trong thư viện (library / 라이브러리) kỹ thuật (engineering / 엔지니어링) là siêu dữ liệu (metadata / 메타데이터) càng mạnh càng cho thời gian chạy (runtime / 런타임) nhiều tối ưu hóa (optimization / 최적화), nhưng siêu dữ liệu (metadata / 메타데이터) sai nguy hiểm hơn siêu dữ liệu (metadata / 메타데이터) yếu.

---

# 17. Stream Gatherers: custom intermediate thao tác (operation / 연산) đã thành tiêu chuẩn (standard / 표준) ở Java 24

Trước Gatherers, Stream API có các intermediate operations fixed như map/filter/flatMap. Những transformations như sliding cửa sổ (window / 윈도우), incremental scan hoặc stateful custom intermediate stage khá khó biểu diễn mà không collect rồi xử lý ngoài stream.

`Gatherer` cho phép custom intermediate transformation với vòng đời (lifecycle / 생명주기)/trạng thái (state / 상태)/tích hợp (integration / 통합) ngữ nghĩa (semantics / 의미론). JDK cung cấp `Gatherers` utility.

Fixed windows:

```java
stream.gather(
    Gatherers.windowFixed(3))
```

Đầu vào (input / 입력):

```text
A B C D E F G
```

conceptual đầu ra (output / 출력):

```text
[A B C]
[D E F]
[G]
```

Sliding cửa sổ (window / 윈도우) kích thước (size / 크기) 3:

```text
[A B C]
[B C D]
[C D E]
...
```

---

# 18. `scan`, `fold` và `mapConcurrent`

`Gatherers.scan` thực hiện prefix/incremental accumulation. Nếu đầu vào (input / 입력) `1,2,3`, scan sum có thể emit `1,3,6`.

`fold` reduction-like nhưng có thể hỗ trợ ordered transformation scenarios không có natural combiner.

`mapConcurrent(maxConcurrency, mapper)` thực hiện ánh xạ (mapping / 매핑) concurrently với configured max tính đồng thời (concurrency / 동시성), dùng virtual threads trong JDK hiện thực (implementation / 구현) hiện tại. Đây là điểm quan trọng: API tính đồng thời (concurrency / 동시성) có **bounded maxConcurrency** chứ không fan-out vô hạn.

Bạn vẫn phải nghĩ downstream sức chứa (capacity / 용량). `mapConcurrent(1000, remoteCall)` có thể đánh chết dịch vụ (service / 서비스) nếu vendor chỉ cho 20 concurrent requests.

Gatherers là ví dụ rất đẹp về JDK evolution: khi một lớp trừu tượng (abstraction / 추상화) lặp lại đủ nhiều trong ecosystem, nền tảng (platform / 플랫폼) có thể chuẩn hóa nó.

---

# 19. `java.util.concurrent.Flow`: Reactive Streams đặc tả hợp đồng (contract / 계약) trong JDK

Luồng (flow / 흐름) định nghĩa bốn cốt lõi (core / 핵심) interfaces:

```text
Publisher<T>
Subscriber<T>
Subscription
Processor<T,R>
```

Publisher phát dữ liệu (data / 데이터). Subscriber nhận dữ liệu (data / 데이터). Subscription nối hai bên và carry demand/cancellation. Processor vừa subscriber vừa publisher.

Điểm quan trọng nhất là **backpressure**. Subscriber gọi:

```java
subscription.request(n);
```

nói nó sẵn sàng nhận thêm n items.

Publisher không được xem subscriber như sink vô hạn.

---

# 20. Subscriber vòng đời (lifecycle / 생명주기)

Subscriber nhận:

```text
onSubscribe(subscription)
onNext(item)...
onError(error)
hoặc
onComplete()
```

`onSubscribe` phải đến trước dữ liệu (data / 데이터).

Sau terminal tín hiệu (signal / 신호) (`onError` hoặc `onComplete`), stream kết thúc.

`request` demand thường phải positive; violations có ngữ nghĩa (semantics / 의미론) theo reactive streams rules.

Reactive giao thức (protocol / 프로토콜) là asynchronous đặc tả hợp đồng (contract / 계약), không chỉ callback API.

---

# 21. SubmissionPublisher

JDK có `SubmissionPublisher<T>` làm basic Publisher hiện thực (implementation / 구현).

Nó hữu ích để học/demo/in-process publishing nhưng không phải replacement cho Reactor/Kafka/broker.

Bạn vẫn phải quan tâm buffer, executor, slow subscribers và drop/submit ngữ nghĩa (semantics / 의미론).

Nếu bên tiêu thụ (consumer / 소비자) chậm, publisher buffer có giới hạn/chi phí (cost / 비용). Reactive Streams không làm bộ nhớ (memory / 메모리)/backpressure bài toán (problem / 문제) biến mất; nó cung cấp giao thức (protocol / 프로토콜) để quản lý nó.

---

# 22. Strong, Weak, Soft và Phantom References

Normal tham chiếu (reference / 참조) là **strong tham chiếu (reference / 참조)**. đối tượng (object / 객체) reachable strongly thì không được GC.

`WeakReference<T>` không giữ đối tượng (object / 객체) sống. Nếu chỉ còn weak references, GC có thể reclaim đối tượng (object / 객체) và `get()` trở null.

Weak references phù hợp canonicalization/siêu dữ liệu (metadata / 메타데이터) mappings trong một số cases. `WeakHashMap` dùng weak keys, useful khi entry thời gian tồn tại (lifetime / 수명) gắn với key reachability.

Nhưng weak bộ nhớ đệm (cache / 캐시) không phải general-purpose bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책). GC pressure quyết định collection, không nghiệp vụ (business / 비즈니스) TTL.

---

# 23. SoftReference: tại sao không nên dùng làm bộ nhớ đệm (cache / 캐시) mặc định

Soft references historically được giữ lâu hơn weak references tùy bộ nhớ (memory / 메모리) pressure. Điều này từng được dùng làm memory-sensitive bộ nhớ đệm (cache / 캐시).

Vấn đề là eviction chính sách (policy / 정책) bị giao cho GC và khó predict. bộ nhớ đệm (cache / 캐시) môi trường vận hành (production / 운영 환경) cần max kích thước (size / 크기), TTL, metrics, hit tỷ lệ (rate / 비율) và predictable hành vi (behavior / 동작).

Dùng Caffeine/tường minh (explicit / 명시적) bộ nhớ đệm (cache / 캐시) thư viện (library / 라이브러리) tốt hơn SoftReference cho nghiệp vụ (business / 비즈니스) bộ nhớ đệm (cache / 캐시).

SoftReference vẫn quan trọng để hiểu tham chiếu (reference / 참조) processing và legacy mã (code / 코드).

---

# 24. PhantomReference và ReferenceQueue

PhantomReference không cho retrieve referent bằng `get()`; mục tiêu là được notified sau khi đối tượng (object / 객체) trở phantom reachable để quản lý post-mortem/bản địa (native / 네이티브) tài nguyên (resource / 자원) bookkeeping.

Typical setup:

```java
ReferenceQueue<Resource> queue =
    new ReferenceQueue<>();

PhantomReference<Resource> ref =
    new PhantomReference<>(
        resource,
        queue);
```

Bạn phải giữ PhantomReference đối tượng (object / 객체) itself reachable để nhận hàng đợi (queue / 큐) notification.

ReferenceQueue cho bạn biết tham chiếu (reference / 참조) đối tượng (object / 객체) đã được enqueued theo tham chiếu (reference / 참조) processing vòng đời (lifecycle / 생명주기).

Đây là low-level technique. tường minh (explicit / 명시적) tài nguyên (resource / 자원) close vẫn tốt hơn vì deterministic.

---

# 25. Cleaner: an toàn (safety / 안전) net, không phải vòng đời (lifecycle / 생명주기) chính

`Cleaner` cung cấp cleanup hành động (action / 동작) khi đối tượng (object / 객체) phantom reachable.

Mẫu (pattern / 패턴) quan trọng là cleanup hành động (action / 동작) không được capture referent mạnh, nếu không đối tượng (object / 객체) sẽ không bao giờ unreachable.

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

`close()` vẫn là primary deterministic đường dẫn (path / 경로). Cleaner là fallback nếu caller quên close.

Nếu tài nguyên (resource / 자원) trọng yếu (critical / 중요) như tệp (file / 파일) descriptor/socket/bản địa (native / 네이티브) allocation, relying only on GC timing có thể exhaust tài nguyên (resource / 자원) trước GC chạy.

---

# 26. NIO SocketChannel

Classic `Socket` có blocking stream mô hình (model / 모델). NIO `SocketChannel` hỗ trợ channel APIs và có thể cấu hình blocking/non-blocking.

```java
SocketChannel channel =
    SocketChannel.open();

channel.connect(
    new InetSocketAddress(
        host,
        port));
```

Read/ghi (write / 쓰기) dùng `ByteBuffer`.

Trong blocking chế độ (mode / 모드), lời gọi (call / 호출) chờ I/O giống normal blocking mô hình (model / 모델). Trong non-blocking chế độ (mode / 모드), read/ghi (write / 쓰기)/connect có thể return mà thao tác (operation / 연산) chưa hoàn tất.

Non-blocking không có nghĩa “async magically faster”; nó đổi mô hình thực thi (execution model / 실행 모델) để một luồng thực thi (thread / 스레드) multiplex nhiều connections.

---

# 27. ServerSocketChannel

Máy chủ (server / 서버) accepts connections:

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

`accept()` có thể return null nếu chưa có liên kết (connection / 연결).

Để tránh polling vòng lặp (loop / 루프), bạn dùng `Selector`.

---

# 28. Selector và vòng lặp sự kiện (event loop / 이벤트 루프)

Selector multiplex nhiều selectable channels trên một luồng thực thi (thread / 스레드).

Register interests:

```text
OP_ACCEPT
OP_CONNECT
OP_READ
OP_WRITE
```

Vòng lặp sự kiện (event loop / 이벤트 루프) concept:

```text
selector.select()
→ selected keys
→ handle accept/read/write/connect
→ update interests
→ repeat
```

Một luồng thực thi (thread / 스레드) có thể manage thousands connections nếu handlers không khối (block / 블록).

Đây là nền mô hình tư duy (mental model / 사고 모델) của Netty/NIO servers.

---

# 29. SelectionKey và partial I/O

Mạng (network / 네트워크) ghi (write / 쓰기) không guarantee toàn buffer được gửi trong một lời gọi (call / 호출).

```java
channel.write(buffer);
```

có thể ghi (write / 쓰기) một phần; `buffer.hasRemaining()` vẫn true. Bạn phải giữ trạng thái (state / 상태) và đăng ký OP_WRITE để tiếp tục sau.

Read cũng có thể nhận partial giao thức (protocol / 프로토콜) frame.

Đây là lý do event-loop networking cần per-connection máy trạng thái (state machine / 상태 머신) và buffers.

Nếu handler gọi DB/blocking HTTP 500 ms trên selector luồng thực thi (thread / 스레드), toàn bộ connections khác bị stall. Event-loop quy tắc (rule / 규칙) là **never khối (block / 블록) the vòng lặp sự kiện (event loop / 이벤트 루프)**.

---

# 30. InterestOps và busy-spin bug

Nếu luôn register `OP_WRITE`, socket thường luôn writable, selector có thể wake liên tục và CPU 100%.

Chỉ yêu cầu (request / 요청) OP_WRITE khi bạn có pending dữ liệu (data / 데이터) và previous ghi (write / 쓰기) không hoàn tất; remove interest khi buffer drained.

Đây là một classic NIO event-loop bug và cho thấy readiness notification phải gắn với máy trạng thái (state machine / 상태 머신).

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

Mô hình (model / 모델) này khác selector vòng lặp sự kiện (event loop / 이벤트 루프) nhưng hiện thực (implementation / 구현)/OS hỗ trợ (support / 지원) có thể still use luồng thực thi (thread / 스레드) pools/nền tảng (platform / 플랫폼) mechanisms.

Virtual threads đã làm blocking-style networking hấp dẫn hơn cho many cases. AsynchronousChannel vẫn cần biết để đọc legacy/high-performance mã (code / 코드).

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

Filesystem sự kiện (event / 이벤트) các hệ thống (systems / 시스템들) có coalescing, overflow và platform-specific hành vi (behavior / 동작). Không assume every thay đổi (change / 변경) maps exactly one sự kiện (event / 이벤트).

Nếu tính đúng đắn (correctness / 정확성) trọng yếu (critical / 중요), sự kiện (event / 이벤트) chỉ nên trigger rescan/reconciliation.

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

JAR là ZIP với Java siêu dữ liệu (metadata / 메타데이터)/conventions.

Khi extract ZIP từ untrusted nguồn (source / 소스), entry name có thể:

```text
../../etc/passwd
```

Nếu resolve trực tiếp:

```java
target.resolve(entry.getName())
```

attacker có thể escape đầu ra (output / 출력) directory.

Normalize rồi verify resolved đường dẫn (path / 경로) vẫn nằm trong mục tiêu (target / 대상) gốc (root / 루트). Đây là Zip Slip defense.

---

# 34. ProcessBuilder và child tiến trình (process / 프로세스) management

Run bên ngoài (external / 외부) command:

```java
Process process =
    new ProcessBuilder(
        "git",
        "status")
        .start();
```

Child tiến trình (process / 프로세스) có stdin/stdout/stderr pipes.

Nếu child ghi nhiều stdout/stderr và parent không drain, pipe buffer có thể full và child khối (block / 블록). Parent meanwhile `waitFor()` tạo deadlock-like hang.

Use `redirectErrorStream(true)`, redirect files hoặc consume both streams concurrently.

Always consider hết thời gian chờ (timeout / 타임아웃):

```java
process.waitFor(
    10,
    TimeUnit.SECONDS);
```

Then terminate if required.

---

# 35. ProcessHandle

`ProcessHandle` cho inspect tiến trình (process / 프로세스) ID, parent/children, info, liveness và termination.

```java
ProcessHandle.current().pid();
```

Useful tooling/launcher/supervisor mã (code / 코드).

Tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) is OS tài nguyên (resource / 자원) ranh giới (boundary / 경계). Child tiến trình (process / 프로세스) có thể spawn grandchildren; killing parent không luôn cleanup cây (tree / 트리) automatically. Cross-platform tiến trình (process / 프로세스) management cần careful ngữ nghĩa (semantics / 의미론).

---

# 36. RandomGenerator API

Java 17 đưa lớp trừu tượng (abstraction / 추상화) `RandomGenerator` và families.

Bạn có thể yêu cầu (request / 요청) thuật toán (algorithm / 알고리즘):

```java
RandomGenerator rng =
    RandomGenerator.getDefault();
```

JDK có generators cho different statistical/hiệu năng (performance / 성능)/parallel requirements.

`ThreadLocalRandom` hợp thread-concurrent non-security random.

`SplittableRandom`/splittable generators phù hợp parallel streams/simulation.

`SecureRandom` vẫn dành cryptographic bảo mật (security / 보안).

Đừng chọn thuật toán (algorithm / 알고리즘) bằng benchmark duy nhất; yêu cầu (requirement / 요구사항) là reproducibility, parallel splitting, statistical chất lượng (quality / 품질) hay bảo mật (security / 보안)?

---

# 37. Unicode: `char` không phải “một ký tự”

Java `char` là 16-bit UTF-16 mã (code / 코드) đơn vị (unit / 단위). Một Unicode mã (code / 코드) điểm (point / 지점) ngoài BMP cần surrogate pair, tức hai chars.

```java
String text = "😀";
text.length(); // 2
```

Người dùng (user / 사용자) thấy một emoji nhưng length 2.

Đếm mã (code / 코드) points:

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

Nếu xử lý identifiers/user-visible văn bản (text / 텍스트)/international names, đừng assume `charAt(i)` là complete character.

Grapheme cluster còn phức tạp hơn mã (code / 코드) điểm (point / 지점) vì combining marks/emoji sequences; JDK basic code-point APIs không giải quyết toàn bộ user-perceived characters.

---

# 38. Unicode Normalization

Visual-similar strings có thể có mã (code / 코드) điểm (point / 지점) sequences khác.

Ví dụ accented character có thể là precomposed mã (code / 코드) điểm (point / 지점) hoặc cơ sở (base / 기반) + combining mark.

Use:

```java
Normalizer.normalize(
    text,
    Normalizer.Form.NFC);
```

khi giao thức (protocol / 프로토콜)/lĩnh vực (domain / 도메인) cần chuẩn gốc (canonical / 정본) form.

Nhưng normalization chính sách (policy / 정책) phải ở ranh giới (boundary / 경계) và consistent. Không blindly normalize passwords/opaque tokens nơi chính xác (exact / 정확한) bytes matter.

Bảo mật (security / 보안) còn có Unicode confusable/homoglyph issues mà normalization không solve hết.

---

# 39. Collator và locale-aware thứ tự (ordering / 순서)

`String.compareTo` so Unicode mã (code / 코드) units lexicographically, không phải language-specific collation.

`Collator` hỗ trợ locale-aware comparison:

```java
Collator collator =
    Collator.getInstance(
        Locale.KOREAN);
```

Useful sorting human names/văn bản (text / 텍스트).

Cơ sở dữ liệu (database / 데이터베이스) collation và Java Collator có thể khác, nên pagination/thứ tự (order / 순서) between DB and Java must be designed consistently.

---

# 40. bản địa (native / 네이티브) Java Serialization internals

A Serializable lớp (class / 클래스) có stream lớp (class / 클래스) descriptor và `serialVersionUID`.

Nếu bạn không declare, JVM computes UID từ lớp (class / 클래스) details. Seemingly harmless lớp (class / 클래스) thay đổi (change / 변경) có thể đổi UID và break deserialize old dữ liệu (data / 데이터).

Tường minh (explicit / 명시적):

```java
private static final long
    serialVersionUID = 1L;
```

không magically make changes compatible; nó chỉ giữ phiên bản (version / 버전) identifier. Nếu fields/types/invariants đổi, custom di chuyển (migration / 마이그레이션) vẫn cần.

Methods như `writeObject`, `readObject`, `readResolve`, `writeReplace` customize hành vi (behavior / 동작) và tăng attack surface/độ phức tạp (complexity / 복잡도).

Bản địa (native / 네이티브) serialization nên được xem là legacy/closed-trusted cơ chế (mechanism / 메커니즘), không default bên ngoài (external / 외부) format.

---

# 41. `transient` và `Externalizable`

`transient` trường dữ liệu (field / 필드) không được default serialization ghi.

Có thể dùng cho derived/bộ nhớ đệm (cache / 캐시)/sensitive trạng thái (state / 상태), nhưng deserialized đối tượng (object / 객체) phải restore bất biến (invariant / 불변식).

`Externalizable` cho full điều khiển (control / 제어) `writeExternal/readExternal`, yêu cầu công khai (public / 공개) no-arg constructor ngữ nghĩa (semantics / 의미론) và rất manual.

Nếu bạn đang thiết kế new wire/lưu trữ (storage / 저장소) giao thức (protocol / 프로토콜), schema-oriented formats thường dễ phiên bản (version / 버전)/manage hơn bản địa (native / 네이티브) Java serialization.

---

# 42. Java Cryptography kiến trúc (architecture / 아키텍처): Provider mô hình (model / 모델)

JCA/JCE APIs thường yêu cầu (request / 요청) thuật toán (algorithm / 알고리즘) by name:

```java
MessageDigest.getInstance(
    "SHA-256");

Cipher.getInstance(
    "AES/GCM/NoPadding");
```

JVM chọn hiện thực (implementation / 구현) từ registered `Provider`s.

Provider kiến trúc (architecture / 아키텍처) tách API khỏi cryptographic hiện thực (implementation / 구현).

Bạn có thể inspect:

```java
Security.getProviders();
```

Enterprise/FIPS environments có thể require approved provider.

Không hard-code provider trừ khi chính sách (policy / 정책)/interoperability cần; nếu hard-code, triển khai (deployment / 배포) phải guarantee provider tồn tại.

---

# 43. MAC khác băm (hash / 해시)

Băm (hash / 해시):

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

Signature dùng private key để sign và công khai (public / 공개) key để verify.

```java
Signature signature =
    Signature.getInstance(
        "SHA256withRSA");
```

Real thuật toán (algorithm / 알고리즘) choices nên theo hiện đại (modern / 현대적) bảo mật (security / 보안) guidance; RSA/ECDSA/EdDSA trade-offs.

Signature authenticity phụ thuộc key trust/phân phối (distribution / 분포), không chỉ math.

Certificate/PKI giải quyết binding công khai (public / 공개) key với định danh (identity / 식별자).

---

# 45. KeyStore, TrustStore và TLS mô hình tư duy (mental model / 사고 모델)

`KeyStore` có thể chứa private keys, secret keys, certificates.

TLS máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (config / 설정) liên quan định danh (identity / 식별자) keys và trust anchors.

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

“PKIX đường dẫn (path / 경로) building failed” thường là trust-chain bài toán (problem / 문제), không phải mạng (network / 네트워크) unreachable.

---

# 46. `keytool` và `jarsigner`

`keytool` quản lý keystore/certificates:

```bash
keytool -list \
  -keystore app.p12
```

`jarsigner` sign/verify JAR signatures.

Sản phẩm tạo ra (artifact / 산출물) signing giúp verify origin/integrity theo trust mô hình (model / 모델), nhưng secure software supply chuỗi (chain / 사슬) còn cần phụ thuộc (dependency / 의존성) provenance, CI bảo mật (security / 보안) và key management.

Master Java engineer cần biết công cụ (tool / 도구) tồn tại và đọc đầu ra (output / 출력), không nhất thiết tự làm PKI chuyên gia.

---

# 47. Annotation Processing: compile-time metaprogramming

Thời gian chạy (runtime / 런타임) reflection đọc lớp (class / 클래스) sau compile. Annotation processor chạy trong compilation.

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

Luồng (flow / 흐름):

```text
javac parses source
→ processors see annotated elements
→ processor generates source/resources
→ additional rounds compile generated source
```

Lombok dùng trình biên dịch (compiler / 컴파일러) tích hợp (integration / 통합) riêng phức tạp; MapStruct-style codegen là ví dụ dễ hiểu hơn về compile-time generation.

---

# 48. Annotation Processor rounds

Generated mã (code / 코드) có thể tạo annotations/elements mới, nên trình biên dịch (compiler / 컴파일러) chạy multiple rounds.

Processor phải handle rounds idempotently và `processingOver()`.

Không assume một lần.

`Filer` tạo generated nguồn (source / 소스)/lớp (class / 클래스)/tài nguyên (resource / 자원). `Messager` emit trình biên dịch (compiler / 컴파일러) diagnostics.

Processor errors nên report tại element liên quan để IDE/bản dựng (build / 빌드) cho nhà phát triển (developer / 개발자) phản hồi (feedback / 피드백) tốt.

---

# 49. nguồn (source / 소스) generation và API thiết kế (design / 설계)

Nếu processor generate:

```java
UserMapperImpl
```

generated lớp (class / 클래스) name/gói (package / 패키지) trở thành part của tích hợp (integration / 통합) đặc tả hợp đồng (contract / 계약) nếu người dùng (user / 사용자) mã (code / 코드) tham chiếu (reference / 참조) trực tiếp.

Tốt hơn expose stable annotation/thời gian chạy (runtime / 런타임) giao diện (interface / 인터페이스) và treat generated details nội bộ (internal / 내부) where possible.

Generated mã (code / 코드) cần deterministic để bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시)/reproducibility tốt.

Annotation processing chạy build-time nên hiệu năng (performance / 성능) của processor ảnh hưởng every compile.

---

# 50. Java Agents và Instrumentation

Java tác nhân (agent / 에이전트) chạy mã (code / 코드) trước `main` qua:

```java
public static void premain(
    String agentArgs,
    Instrumentation inst) {
}
```

Động (dynamic / 동적) attach có thể dùng `agentmain`.

`Instrumentation` cho inspect loaded classes, redefine/retransform lớp (class / 클래스) tùy năng lực (capability / 역량) và register `ClassFileTransformer`.

APM/profilers/mock/instrumentation tools dùng agents để insert probes.

Tác nhân (agent / 에이전트) chạy trong mục tiêu (target / 대상) JVM với quyền lực lớn. Bug tác nhân (agent / 에이전트) có thể ảnh hưởng toàn ứng dụng (application / 애플리케이션).

---

# 51. ClassFileTransformer

Transformer nhận lớp (class / 클래스) bytes trong loading/retransformation chuỗi xử lý (pipeline / 파이프라인) và có thể return transformed bytes.

Bạn phải hiểu class-file validity, ngăn xếp (stack / 스택) maps/xác minh (verification / 확인), recursion/classloader interactions.

Không manually edit byte array offsets. Dùng Class-File API hoặc mature bytecode thư viện (library / 라이브러리).

Instrument phương thức (method / 메서드) entry/exit naïvely có thể phá exceptions, synchronized ngữ nghĩa (semantics / 의미론) hoặc hiệu năng (performance / 성능).

---

# 52. Class-File API từ Java 24

JDK 24 standardizes `java.lang.classfile` API để parse, generate và transform lớp (class / 클래스) files.

Mục tiêu là tránh mỗi công cụ (tool / 도구)/thư viện (library / 라이브러리) phải maintain parser theo class-file evolution.

Concept:

```java
ClassFile cf =
    ClassFile.of();

ClassModel model =
    cf.parse(bytes);
```

API mô hình (model / 모델) lớp (class / 클래스)/phương thức (method / 메서드)/trường dữ liệu (field / 필드)/attributes/instructions và hỗ trợ transformation.

Nếu bạn viết tác nhân (agent / 에이전트)/codegen/bản dựng (build / 빌드) công cụ (tool / 도구), đây là API quan trọng. Nếu bạn viết CRUD dịch vụ (service / 서비스), chỉ cần awareness.

---

# 53. Class-file cấu trúc (structure / 구조)

Tệp lớp (class file / 클래스 파일) bắt đầu magic:

```text
0xCAFEBABE
```

rồi minor/major phiên bản (version / 버전), constant pool, truy cập (access / 접근) flags, this/super, interfaces, fields, methods, attributes.

Major phiên bản (version / 버전) quyết định thời gian chạy (runtime / 런타임) tính tương thích (compatibility / 호환성); JVM cũ thấy newer major sẽ reject.

Tệp lớp (class file / 클래스 파일) không phải “serialized Java nguồn (source / 소스)”. Generic info, gỡ lỗi (debug / 디버그) info, annotations và bytecode nằm trong attributes/constant-pool references; tầng mã nguồn (source-level / 소스 수준) constructs có thể biến đổi đáng kể.

---

# 54. Constant Pool

Constant pool chứa constants và symbolic references: lớp (class / 클래스) names, phương thức (method / 메서드)/trường dữ liệu (field / 필드) refs, strings, phương thức (method / 메서드) handles/types, động (dynamic / 동적) constants...

Bytecode instructions thường refer indexes vào constant pool.

Linking resolution biến symbolic tham chiếu (reference / 참조) thành thời gian chạy (runtime / 런타임) thực thể (entity / 엔터티) khi cần.

Hiểu constant pool giúp đọc `javap -v`, `invokedynamic`, động (dynamic / 동적) constants và linkage errors.

---

# 55. phương thức (method / 메서드) descriptors

JVM descriptor encode parameter/return types.

Ví dụ:

```java
String f(int x, long y)
```

descriptor:

```text
(IJ)Ljava/lang/String;
```

Thành phần nguyên thủy (primitive / 기본 요소) codes: `I` int, `J` long, `V` void; đối tượng (object / 객체) `L...;`; array `[...`.

Bytecode/tooling uses descriptors, không Java generic cú pháp (syntax / 문법).

---

# 56. StackMapTable và verifier

Hiện đại (modern / 현대적) lớp (class / 클래스) files có ngăn xếp (stack / 스택) map frames giúp verifier check kiểu (type / 타입) trạng thái (state / 상태) at control-flow points efficiently.

Nếu bytecode transformer generate invalid frames, lớp (class / 클래스) tải (load / 로드) có thể thất bại (fail / 실패) `VerifyError`.

Mature Class-File API/ASM compute/manage frames giúp tránh manual nightmare.

Đây là ví dụ tại sao bytecode kỹ thuật (engineering / 엔지니어링) là specialist trường dữ liệu (field / 필드) dù cú pháp (syntax / 문법) transformation nhìn đơn giản.

---

# 57. `invokedynamic`

Traditional invokevirtual call-site references phương thức (method / 메서드) symbolically theo fixed dispatch rules. `invokedynamic` cho thời gian chạy (runtime / 런타임) bootstrap lô-gic (logic / 논리) link lời gọi (call / 호출) site dynamically.

Instruction references bootstrap phương thức (method / 메서드) siêu dữ liệu (metadata / 메타데이터). First linkage computes CallSite/mục tiêu (target / 대상); later invocation có thể reuse optimized mục tiêu (target / 대상).

Java lambdas dùng `invokedynamic` + `LambdaMetafactory`. hiện đại (modern / 현대적) string concatenation cũng dùng động (dynamic / 동적) concat machinery.

Điều này cho JVM/thư viện (library / 라이브러리) authors linh hoạt implement ngôn ngữ (language / 언어) features mà không thêm lệnh bytecode (bytecode instruction / 바이트코드 명령어) cho từng tính năng (feature / 기능).

---

# 58. Lambda không đơn giản là anonymous lớp (class / 클래스)

Nguồn (source / 소스):

```java
Function<String, Integer>
    length =
        String::length;
```

Trình biên dịch (compiler / 컴파일러) thường emits invokedynamic lời gọi (call / 호출) site, bootstrap tới LambdaMetafactory.

Thời gian chạy (runtime / 런타임) có thể produce đối tượng (object / 객체)/hành vi (behavior / 동작) optimized tùy capture/trạng thái (state / 상태).

Do đó các giả định (assumptions / 가정들) như “mỗi lambda luôn tạo một anonymous tệp lớp (class file / 클래스 파일)” là sai trong hiện đại (modern / 현대적) Java.

Captured lambda có different allocation/vòng đời (lifecycle / 생명주기) hành vi (behavior / 동작) so non-capturing; JIT có thể optimize further.

---

# 59. MethodHandle

MethodHandle là strongly typed executable tham chiếu (reference / 참조).

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

Invoke chính xác (exact / 정확한):

```java
int length =
    (int) mh.invokeExact("hello");
```

`invokeExact` yêu cầu chính xác (exact / 정확한) MethodType; `invoke` cho adaptation conversions rộng hơn.

MethodHandle có thể được JIT optimize better than arbitrary reflection in động (dynamic / 동적) frameworks, nhưng API kiểu (type / 타입) gymnastics phức tạp.

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

Những combinators cho bản dựng (build / 빌드) động (dynamic / 동적) invocation pipelines không generate bytecode manually.

Động (dynamic / 동적) ngôn ngữ (language / 언어) thời gian chạy (runtime / 런타임), serialization frameworks, proxy các hệ thống (systems / 시스템들) có thể dùng.

Application-level dispatch nên dùng ordinary interfaces/lambdas trước.

---

# 61. Hidden Classes

Hidden classes được thiết kế cho frameworks generate thời gian chạy (runtime / 런타임) classes không cần discoverability/vòng đời (lifecycle / 생명주기) như normal named classes.

Chúng không dễ được tìm qua normal nạp lớp (class loading / 클래스 로딩)/name lookup và có GC/unloading properties useful động (dynamic / 동적) ngôn ngữ (language / 언어)/khung phần mềm (framework / 프레임워크) implementations.

Lambda thời gian chạy (runtime / 런타임) đã liên quan hidden-class direction trong hiện đại (modern / 현대적) JDK internals.

Nếu bạn viết proxy/thời gian chạy (runtime / 런타임) mã (code / 코드) generation, hidden classes giải quyết pollution/leak của generating endless named classes.

---

# 62. động (dynamic / 동적) Constants (`condy`)

`CONSTANT_Dynamic` cho constant-pool entry được bootstrap dynamically tại linkage, giống invokedynamic nhưng cho giá trị (value / 값) thay vì lời gọi (call / 호출) site.

Nó cho ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리) authors lazy/computed constants mà JVM có thể treat như constant after resolution.

Normal ứng dụng (application / 애플리케이션) mã (code / 코드) hiếm khi author condy trực tiếp, nhưng Class-File API/bytecode tools có thể.

Java 26 Lazy Constants API ở nguồn (source / 소스)/thư viện (library / 라이브러리) mức (level / 수준) là concept liên quan nhưng không đơn giản đồng nhất với condy.

---

# 63. Foreign hàm (function / 함수) & bộ nhớ (memory / 메모리) API: Java gọi bản địa (native / 네이티브) mã (code / 코드) mà không phải sống trong JNI boilerplate

FFM final ở Java 22, gói (package / 패키지):

```java
java.lang.foreign
```

Nó giải quyết hai vấn đề lớn: truy cập (access / 접근) bộ nhớ (memory / 메모리) ngoài Java vùng nhớ động (heap / 힙) an toàn hơn và gọi bản địa (native / 네이티브) functions qua linker/phương thức (method / 메서드) handles.

Cốt lõi (core / 핵심) concepts:

```text
MemorySegment
Arena
MemoryLayout
Linker
SymbolLookup
FunctionDescriptor
```

FFM không làm bản địa (native / 네이티브) mã (code / 코드) “an toàn như Java”. C hàm (function / 함수) vẫn có thể corrupt bộ nhớ (memory / 메모리) bên bản địa (native / 네이티브) side. Nhưng Java-side bounds/thời gian tồn tại (lifetime / 수명) checking mạnh hơn raw JNI/Unsafe patterns.

---

# 64. MemorySegment

MemorySegment là bounded region của bộ nhớ (memory / 메모리).

Có vùng nhớ động (heap / 힙) segments và bản địa (native / 네이티브) segments.

Operations check bounds/alignment/thời gian tồn tại (lifetime / 수명) based API.

Thay vì raw address `long`, segment carries spatial/temporal an toàn (safety / 안전) siêu dữ liệu (metadata / 메타데이터).

Nếu truy cập (access / 접근) outside segment:

```text
exception
```

thay vì silently corrupt adjacent Java/bản địa (native / 네이티브) bộ nhớ (memory / 메모리) từ Java API.

---

# 65. Arena và temporal an toàn (safety / 안전)

Arena controls bản địa (native / 네이티브) segment thời gian tồn tại (lifetime / 수명).

```java
try (Arena arena =
         Arena.ofConfined()) {

    MemorySegment segment =
        arena.allocate(1024);

    ...
}
```

Sau arena close, truy cập (access / 접근) segment thất bại (fail / 실패).

Confined arena có thread-confinement ngữ nghĩa (semantics / 의미론). dùng chung (shared / 공유) arena supports cross-thread truy cập (access / 접근) with different vòng đời (lifecycle / 생명주기) considerations.

This is RAII-like tài nguyên (resource / 자원) phạm vi (scope / 범위) in Java: deterministic close beats waiting GC.

---

# 66. MemoryLayout

Bản địa (native / 네이티브) structs/arrays có bố cục (layout / 레이아웃).

```java
MemoryLayout layout =
    MemoryLayout.structLayout(
        ValueLayout.JAVA_INT
            .withName("x"),
        ValueLayout.JAVA_INT
            .withName("y"));
```

Bố cục (layout / 레이아웃) helps derive offsets/VarHandles/truy cập (access / 접근).

Alignment/endian/nền tảng (platform / 플랫폼) ABI matter. bản địa (native / 네이티브) bố cục (layout / 레이아웃) phải match C ABI exactly.

Never assume Java kiểu (type / 타입) sizes/bố cục (layout / 레이아웃) equal arbitrary C trình biên dịch (compiler / 컴파일러) struct without ABI understanding.

---

# 67. Linker, SymbolLookup và FunctionDescriptor

Lookup bản địa (native / 네이티브) symbol:

```java
SymbolLookup lookup = ...;
MemorySegment symbol =
    lookup.find("strlen")
          .orElseThrow();
```

FunctionDescriptor describes bản địa (native / 네이티브) signature.

Linker creates downcall MethodHandle.

Calling bản địa (native / 네이티브) hàm (function / 함수) now fits MethodHandle mô hình thực thi (execution model / 실행 모델).

Bản địa (native / 네이티브) truy cập (access / 접근) can be restricted; hiện đại (modern / 현대적) Java requires tường minh (explicit / 명시적) native-access enablement in relevant triển khai (deployment / 배포) situations. Treat this as bảo mật (security / 보안)/operational đặc tả hợp đồng (contract / 계약).

---

# 68. Upcalls

FFM can create bản địa (native / 네이티브) hàm (function / 함수) pointer that calls Java MethodHandle.

Useful callbacks from C thư viện (library / 라이브러리).

Vòng đời (lifecycle / 생명주기) is trọng yếu (critical / 중요): upcall stub bộ nhớ (memory / 메모리) and arena must live while bản địa (native / 네이티브) side might invoke callback.

If arena closes early and bản địa (native / 네이티브) calls stale pointer, hành vi (behavior / 동작)/thất bại (failure / 실패) can be severe.

This is quyền sở hữu (ownership / 소유권) across ngôn ngữ (language / 언어) ranh giới (boundary / 경계); document thời gian tồn tại (lifetime / 수명) explicitly.

---

# 69. JNI awareness

JNI is older bản địa (native / 네이티브) interop cơ chế (mechanism / 메커니즘) using generated/bản địa (native / 네이티브) glue and JNI môi trường (environment / 환경) APIs.

It is powerful but verbose and error-prone: cục bộ (local / 로컬)/toàn cục (global / 전역) references, pin/bản sao (copy / 복사) arrays, exception checking, luồng thực thi (thread / 스레드) attachment, bản địa (native / 네이티브) crashes.

You still need JNI awareness because many libraries use it, but new mã (code / 코드) should evaluate FFM first when feasible.

A segfault in JNI/FFM/bản địa (native / 네이티브) thư viện (library / 라이브러리) can crash entire JVM, not throw catchable Java exception.

---

# 70. `Unsafe` di chuyển (migration / 마이그레이션)

`sun.misc.Unsafe` historically exposed raw bộ nhớ (memory / 메모리), CAS, trường dữ liệu (field / 필드) offsets, đối tượng (object / 객체) allocation, fences and many JVM internals.

Hiện đại (modern / 현대적) replacements cover many areas:

```text
VarHandle
FFM
MethodHandle
Cleaner
standard concurrent APIs
```

Some libraries still use Unsafe for hiệu năng (performance / 성능)/backward tính tương thích (compatibility / 호환성).

Don't bản sao (copy / 복사) Unsafe mã (code / 코드) from ngăn xếp (stack / 스택) Overflow. It bypasses Java an toàn (safety / 안전) and encapsulation, breaks across JVM evolution and AOT/bảo mật (security / 보안) boundaries.

---

# 71. GC TLAB

Most small đối tượng (object / 객체) allocation can happen in luồng thực thi (thread / 스레드) cục bộ (local / 로컬) Allocation Buffer, a per-thread chunk of Eden/young allocation area.

Fast-path allocation becomes pointer bump with little synchronization.

This is one reason `new` for small short-lived objects is extremely cheap in HotSpot.

When TLAB exhausted, luồng thực thi (thread / 스레드) requests/refills; large objects may bypass.

JFR/GC logs can show allocation pressure. Don't object-pool tiny objects to avoid “expensive malloc” mô hình tư duy (mental model / 사고 모델) from C.

---

# 72. ghi (write / 쓰기) Barriers

GC needs know when references thay đổi (change / 변경).

JIT inserts **ghi (write / 쓰기) barriers** around tham chiếu (reference / 참조) stores so collector can maintain remembered sets/card tables/concurrent marking invariants.

Example:

```java
oldObject.field =
    youngObject;
```

generational collector needs know old region now points to young đối tượng (object / 객체) so young collection doesn't scan entire old vùng nhớ động (heap / 힙).

Barrier chi phí (cost / 비용) is part of đối tượng (object / 객체)/tham chiếu (reference / 참조) mutation chi phí (cost / 비용), usually tiny but fundamental.

---

# 73. Card Tables và Remembered Sets

A card bảng (table / 테이블) divides bộ nhớ (memory / 메모리) into coarse regions/cards and marks cards dirty on tham chiếu (reference / 참조) writes. Collector scans dirty cards rather than entire old generation.

G1 uses remembered sets/region siêu dữ liệu (metadata / 메타데이터) to nhánh học (track / 트랙) cross-region references with more sophisticated machinery.

This explains why “only young generation is collected” can still correctly find references from old objects.

Ứng dụng (application / 애플리케이션) developers don't tune card tables normally; understanding them helps read GC/JIT discussions.

---

# 74. Safepoints

Safepoint is JVM trạng thái (state / 상태) where threads are at locations suitable for certain toàn cục (global / 전역) VM operations.

Historically GC stop-the-world phases, deoptimization, lớp (class / 클래스) redefinition and VM operations may require safepoint coordination.

Time-to-safepoint can contribute pause separately from GC công việc (work / 작업).

Hiện đại (modern / 현대적) JVM also has mechanisms like handshakes for more targeted operations, reducing need for toàn cục (global / 전역) safepoint in some cases.

When JFR/log says long pause, distinguish “reach safepoint” from “thao tác (operation / 연산) at safepoint”.

---

# 75. Stop-the-world không có nghĩa mọi GC đều hoàn toàn STW

Hiện đại (modern / 현대적) collectors perform significant công việc (work / 작업) concurrently with ứng dụng (application / 애플리케이션) threads.

However they still have some stop-the-world phases.

G1, ZGC, Shenandoah differ in which phases are concurrent and pause profiles.

The useful question is not “collector concurrent?” but “what are pause distributions, CPU overhead, allocation headroom and thông lượng (throughput / 처리량) under my tải công việc (workload / 워크로드)?”.

---

# 76. Serial GC, Parallel GC, G1, ZGC, Shenandoah

Serial GC uses single-threaded collection công việc (work / 작업) and suits small/simple footprints.

Parallel GC emphasizes thông lượng (throughput / 처리량) using multiple GC threads, with larger pauses acceptable.

G1 is general-purpose regional collector with pause-target goals and dùng chung (common / 공통) hiện đại (modern / 현대적) default.

ZGC targets extremely low pauses with highly concurrent công việc (work / 작업); hiện đại (modern / 현대적) ZGC is generational.

Shenandoah is another low-pause concurrent collector available in OpenJDK distributions; hiện đại (modern / 현대적) releases include generational evolution.

Collector choice belongs SLO/sức chứa (capacity / 용량) testing, not fashion.

---

# 77. đối tượng (object / 객체) bố cục (layout / 레이아웃)

A Java đối tượng (object / 객체) in HotSpot conceptually contains header + instance fields + padding/alignment.

Header historically includes mark word and lớp (class / 클래스) siêu dữ liệu (metadata / 메타데이터) pointer/tham chiếu (reference / 참조). chính xác (exact / 정확한) bố cục (layout / 레이아웃) depends JVM flags, compressed references, collector and JDK evolution.

Đối tượng (object / 객체) alignment often means kích thước (size / 크기) rounds to multiple ranh giới (boundary / 경계).

This matters in millions of objects: a few bytes padding/header multiply into hundreds MB.

Use JOL (Java object Layout) công cụ (tool / 도구) for bằng chứng (evidence / 증거) instead of manually assuming sizes.

---

# 78. Compressed References

On suitable heaps/configs HotSpot can encode đối tượng (object / 객체)/lớp (class / 클래스) references in narrower biểu diễn (representation / 표현), reducing bộ nhớ (memory / 메모리) footprint and improving bộ nhớ đệm (cache / 캐시) locality.

This is why tham chiếu (reference / 참조) trường dữ liệu (field / 필드) might effectively use 4 bytes rather than bản địa (native / 네이티브) 8-byte pointer in certain configurations.

Thresholds/modes depend vùng nhớ động (heap / 힙)/addressing/JVM.

Do not hard-code object-size các giả định (assumptions / 가정들) into ứng dụng (application / 애플리케이션) lô-gic (logic / 논리).

---

# 79. Compact đối tượng (object / 객체) Headers trong Java 25

Java 25 includes Compact đối tượng (object / 객체) Headers as a môi trường vận hành (production / 운영 환경) tính năng (feature / 기능)/thời gian chạy (runtime / 런타임) improvement. Goal is reducing đối tượng (object / 객체) header footprint by encoding siêu dữ liệu (metadata / 메타데이터) more compactly.

Tác động (effect / 효과) can be significant for object-heavy workloads by reducing vùng nhớ động (heap / 힙) footprint/bộ nhớ đệm (cache / 캐시) traffic.

You usually don't thay đổi (change / 변경) mã nguồn (source code / 소스 코드) to benefit; upgrade/thời gian chạy (runtime / 런타임) flags/defaults govern hành vi (behavior / 동작) according bản phát hành (release / 릴리스).

This is another reminder that JDK upgrade can improve ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) without mã (code / 코드) thay đổi (change / 변경), so re-baseline hiệu năng (performance / 성능) after upgrades.

---

# 80. CDS và AppCDS

Lớp (class / 클래스) dữ liệu (data / 데이터) Sharing stores preprocessed lớp (class / 클래스) siêu dữ liệu (metadata / 메타데이터) in archive dùng chung (shared / 공유)/mapped at startup, reducing startup thời gian (time / 시간) and bộ nhớ (memory / 메모리) across processes.

AppCDS extends sharing to ứng dụng (application / 애플리케이션) classes.

Hiện đại (modern / 현대적) JDK/Boot ecosystems increasingly automate huấn luyện (training / 학습)/archive creation.

CDS primarily optimizes nạp lớp (class loading / 클래스 로딩)/startup footprint, not nghiệp vụ (business / 비즈니스) thuật toán (algorithm / 알고리즘) thông lượng (throughput / 처리량).

When startup matters, measure class-loading/JIT/AOT separately.

---

# 81. dự án (project / 프로젝트) Leyden/AOT direction

Hiện đại (modern / 현대적) Java is adding AOT bộ nhớ đệm (cache / 캐시)/huấn luyện (training / 학습) mechanisms while preserving JVM động (dynamic / 동적) tối ưu hóa (optimization / 최적화) mô hình (model / 모델).

The direction is not simply “replace JIT with bản địa (native / 네이티브) compilation”. Goal is shift some nạp lớp (class loading / 클래스 로딩)/linking/compilation/profile công việc (work / 작업) ahead of startup and reuse it.

Java 25/26 include AOT bộ nhớ đệm (cache / 캐시) improvements. chính xác (exact / 정확한) commands/features evolve quickly, so use version-specific docs.

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

JFR is valuable when recording already running **before** sự cố (incident / 인시던트).

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

Chính xác (exact / 정확한) options/profile depend môi trường (environment / 환경).

During sự cố (incident / 인시던트) you dump hiện tại (current / 현재) recording instead of starting after symptom disappears.

---

# 83. Custom JFR Events

Ứng dụng (application / 애플리케이션)/thư viện (library / 라이브러리) can define custom sự kiện (event / 이벤트):

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

JFR sự kiện (event / 이벤트) should be meaningful and low-overhead. Don't emit huge strings/secrets/high-frequency events without threshold/sampling chiến lược (strategy / 전략).

Custom events make correlation between nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) and JVM hành vi (behavior / 동작) extremely powerful.

---

# 84. JMX và MXBeans

JMX exposes management objects via MBeans/MXBeans.

Nền tảng (platform / 플랫폼) MXBeans:

```java
ManagementFactory
    .getMemoryMXBean();

ManagementFactory
    .getThreadMXBean();

ManagementFactory
    .getGarbageCollectorMXBeans();
```

Useful for monitoring/tools.

Remote JMX historically has bảo mật (security / 보안)/mạng (network / 네트워크) độ phức tạp (complexity / 복잡도); hiện đại (modern / 현대적) khả năng quan sát (observability / 관측 가능성) often exports metrics differently. Still, understanding MXBeans helps because many JVM metrics originate from same management dữ liệu (data / 데이터).

---

# 85. ThreadMXBean

Can inspect luồng thực thi (thread / 스레드) IDs/info, CPU thời gian (time / 시간), deadlock detection depending JVM năng lực (capability / 역량).

Programmatic diagnostics công cụ (tool / 도구):

```java
ThreadMXBean bean =
    ManagementFactory
        .getThreadMXBean();
```

Thư viện (library / 라이브러리)/kiểm thử (test / 테스트) tools can detect deadlocks or luồng thực thi (thread / 스레드) CPU hotspots.

Avoid polling expensive full ngăn xếp (stack / 스택) dumps at extremely high frequency.

---

# 86. `jdeps`

`jdeps` analyzes lớp (class / 클래스)/mô-đun (module / 모듈) dependencies.

Useful trước upgrade/mô-đun (module / 모듈) di chuyển (migration / 마이그레이션):

```bash
jdeps app.jar
```

Can identify JDK nội bộ (internal / 내부) APIs, gói (package / 패키지)/mô-đun (module / 모듈) dependencies and transitive relationships.

When moving 8→17/21/25, `jdeps --jdk-internals` can help find unsupported nội bộ (internal / 내부) APIs.

---

# 87. `jdeprscan`

Scans lớp (class / 클래스)/JAR usage of deprecated APIs against JDK.

Useful continuous modernization:

```bash
jdeprscan app.jar
```

Deprecation today may become removal later. Fix during regular upgrades instead of waiting one giant di chuyển (migration / 마이그레이션).

---

# 88. `jlink`

JPMS modules allow building custom thời gian chạy (runtime / 런타임) ảnh (image / 이미지) with only needed modules.

```bash
jlink \
  --module-path ... \
  --add-modules com.example.app \
  --output runtime
```

Benefits smaller triển khai (deployment / 배포)/thời gian chạy (runtime / 런타임) điều khiển (control / 제어).

But many frameworks/libs are classpath-oriented or use reflection/resources dynamically; tích hợp (integration / 통합) testing required.

Containers often ship full JRE/JDK anyway, so kích thước (size / 크기) benefit must justify độ phức tạp (complexity / 복잡도).

---

# 89. `jpackage`

`jpackage` creates bản địa (native / 네이티브) ứng dụng (application / 애플리케이션) packages/installers/bundles including thời gian chạy (runtime / 런타임) ảnh (image / 이미지).

Useful desktop/phân tán (distributed / 분산) applications where người dùng (user / 사용자) should not install JDK manually.

It can combine with jlink-generated thời gian chạy (runtime / 런타임).

Máy chủ (server / 서버) containers usually use different packaging practices, but công cụ (tool / 도구) belongs JDK mastery.

---

# 90. `jhsdb`

HotSpot Serviceability tác nhân (agent / 에이전트) tooling can inspect JVM/cốt lõi (core / 핵심) dumps at low mức (level / 수준).

Use cases include post-mortem when tiến trình (process / 프로세스) crashed or normal attach unavailable.

Commands can inspect vùng nhớ động (heap / 힙), ngăn xếp (stack / 스택), classloader, VM structures.

This is advanced sự cố (incident / 인시던트) tooling; thao tác (operation / 연산) privileges/phiên bản (version / 버전) matching matter.

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

Manifest line formatting/classpath ngữ nghĩa (semantics / 의미론) have quirks; bản dựng (build / 빌드) công cụ (tool / 도구) should generate.

Signed JAR also stores signature siêu dữ liệu (metadata / 메타데이터) under META-INF.

---

# 92. Multi-Release JAR

A thư viện (library / 라이브러리) can ship cơ sở (base / 기반) classes plus version-specific implementations under:

```text
META-INF/versions/9/
META-INF/versions/21/
```

Thời gian chạy (runtime / 런타임) selects appropriate phiên bản (version / 버전).

This allows one sản phẩm tạo ra (artifact / 산출물) hỗ trợ (support / 지원) broad JDKs while using newer APIs internally on new thời gian chạy (runtime / 런타임).

But testing ma trận (matrix / 행렬) becomes complex: you must kiểm thử (test / 테스트) every supported thời gian chạy (runtime / 런타임) đường dẫn (path / 경로). Avoid unless thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성) genuinely requires.

---

# 93. Automatic Modules và mô-đun (module / 모듈) naming

A normal JAR on mô-đun (module / 모듈) đường dẫn (path / 경로) may become automatic mô-đun (module / 모듈) with derived/name siêu dữ liệu (metadata / 메타데이터).

Stable `Automatic-Module-Name` manifest attribute helps thư viện (library / 라이브러리) avoid filename-derived module-name changes before fully modularizing.

Công khai (public / 공개) mô-đun (module / 모듈)/gói (package / 패키지) names are tính tương thích (compatibility / 호환성) surface. Renaming later breaks consumers.

---

# 94. ServiceLoader sâu hơn

Dịch vụ (service / 서비스) provider giao diện (interface / 인터페이스):

```java
public interface Codec {
    byte[] encode(Object value);
}
```

Providers can be declared in mô-đun (module / 모듈) descriptor:

```java
provides Codec
    with JsonCodec;
```

Bên tiêu thụ (consumer / 소비자):

```java
ServiceLoader<Codec>
    loader =
        ServiceLoader.load(
            Codec.class);
```

`ServiceLoader.Provider<T>` allows inspect provider kiểu (type / 타입)/lazy instantiate.

This is Plugin/chiến lược (strategy / 전략) discovery built into Java.

Provider constructor/vòng đời (lifecycle / 생명주기)/lỗi (error / 오류) handling must be designed; one broken provider can affect discovery.

---

# 95. ModuleLayer

JPMS can create additional mô-đun (module / 모듈) layers at thời gian chạy (runtime / 런타임).

Useful plugin các hệ thống (systems / 시스템들) loading modules/cấu hình (configuration / 구성) separate from boot tầng (layer / 계층).

A tầng (layer / 계층) has mô-đun (module / 모듈) cấu hình (configuration / 구성) + lớp (class / 클래스) loaders.

This gives stronger mô-đun (module / 모듈) boundaries than raw custom classloader but is advanced.

Ứng dụng (application / 애플리케이션) mã (code / 코드) rarely needs ModuleLayer; plugin/bộ chứa (container / 컨테이너) frameworks may.

---

# 96. Custom ClassLoader

Subclass ClassLoader and override `findClass`/tài nguyên (resource / 자원) loading as appropriate.

Correct delegation is hard. Parent-first avoids duplicate cốt lõi (core / 핵심) classes; child-first may isolate plugin versions but risks kiểu (type / 타입) định danh (identity / 식별자) conflicts.

When plugin giao diện (interface / 인터페이스) is loaded by parent but plugin bundles own duplicate giao diện (interface / 인터페이스), cast fails even same lớp (class / 클래스) name.

Thiết kế (design / 설계) dùng chung (shared / 공유) API classloader ranh giới (boundary / 경계) intentionally.

---

# 97. tài nguyên (resource / 자원) Loading

`Class.getResource` đường dẫn (path / 경로) ngữ nghĩa (semantics / 의미론) differ leading slash vs relative gói (package / 패키지).

`ClassLoader.getResource` generally uses absolute classpath-like names without leading slash.

In JAR, tài nguyên (resource / 자원) isn't necessarily vật lý (physical / 물리적) tệp (file / 파일); converting tài nguyên (resource / 자원) URL to `File` may thất bại (fail / 실패).

Use stream:

```java
try (InputStream in =
    MyClass.class
        .getResourceAsStream(
            "/config/default.json")) {
}
```

Frameworks packaged in fat JARs make tệp (file / 파일) các giả định (assumptions / 가정들) especially dangerous.

---

# 98. Advanced Generics: reifiable types

Reifiable kiểu (type / 타입) has enough thời gian chạy (runtime / 런타임) biểu diễn (representation / 표현) after erasure, examples:

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

Thời gian chạy (runtime / 런타임) cannot fully check element kiểu (type / 타입) after erasure.

---

# 99. Generic arrays

Arrays are covariant/reified; generics bất biến (invariant / 불변식)/erased. Mixing creates unsoundness.

If you need generic collection of T, prefer `List<T>`.

Low-level generic bộ chứa (container / 컨테이너) may use:

```java
@SuppressWarnings("unchecked")
T[] array =
    (T[]) new Object[size];
```

internally, but must encapsulate unsafe cast and ensure no incompatible values enter.

Suppress warning at smallest proven-safe ranh giới (boundary / 경계).

---

# 100. cầu nối (bridge / 브리지) Methods

Suppose generic giao diện (interface / 인터페이스):

```java
interface Box<T> {
    T get();
}
```

Hiện thực (implementation / 구현):

```java
class StringBox
        implements Box<String> {

    public String get() {
        return "...";
    }
}
```

After erasure giao diện (interface / 인터페이스) phương thức (method / 메서드) resembles `Object get()`. trình biên dịch (compiler / 컴파일러) may generate synthetic cầu nối (bridge / 브리지) phương thức (method / 메서드) returning đối tượng (object / 객체) and delegating to String-return phương thức (method / 메서드) to preserve polymorphism/nhị phân (binary / 이진) tính tương thích (compatibility / 호환성).

Reflection/ngăn xếp (stack / 스택) traces can show cầu nối (bridge / 브리지) methods.

This is why `Method.isBridge()` exists.

---

# 101. Wildcard Capture

Phương thức (method / 메서드) gets `List<?>`. You cannot `set` arbitrary đối tượng (object / 객체) because actual element kiểu (type / 타입) unknown.

A helper generic phương thức (method / 메서드) can “capture” wildcard kiểu (type / 타입):

```java
void reverse(List<?> list) {
    reverseCaptured(list);
}

private <T> void reverseCaptured(
        List<T> list) {
    ...
}
```

Trình biên dịch (compiler / 컴파일러) invents a consistent captured T for that specific danh sách (list / 목록).

Wildcard capture errors seem cryptic, but mô hình tư duy (mental model / 사고 모델) is “unknown but fixed kiểu (type / 타입)”, not “any kiểu (type / 타입)”.

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

Trình biên dịch (compiler / 컴파일러)/lambda mục tiêu (target / 대상) typing uses intersection types internally.

Useful thư viện (library / 라이브러리) generics; ứng dụng (application / 애플리케이션) API should avoid overly clever signatures if readability suffers.

---

# 103. kiểu (type / 타입) Tokens

Because `List<String>.class` doesn't exist, frameworks often use kiểu (type / 타입) đơn vị từ (token / 토큰) objects carrying generic `Type`.

Mẫu (pattern / 패턴):

```java
new TypeReference<
    List<User>>() {}
```

anonymous subclass captures generic superclass siêu dữ liệu (metadata / 메타데이터) inspectable by reflection.

Jackson/Gson-like libraries use this.

This is workaround around erasure. hiện đại (modern / 현대적) APIs may use `ParameterizedType`/custom kiểu (type / 타입) descriptors.

---

# 104. Overload resolution vs Override dispatch

Overload is compile-time based on **static argument types**.

Override is thời gian chạy (runtime / 런타임) dispatch based on receiver đối tượng (object / 객체)'s thời gian chạy (runtime / 런타임) lớp (class / 클래스).

Example:

```java
void print(Object x)
void print(String x)
```

If variable static kiểu (type / 타입) đối tượng (object / 객체) holds String:

```java
Object x = "hello";
print(x);
```

Trình biên dịch (compiler / 컴파일러) chooses `print(Object)`.

But:

```java
Animal a =
    new Dog();

a.sound();
```

override dispatch chooses Dog's `sound()`.

Confusing these causes interview and real API bugs.

---

# 105. Static phương thức (method / 메서드) Hiding

Static methods are resolved by lớp (class / 클래스)/tham chiếu (reference / 참조) static kiểu (type / 타입); they are hidden, not overridden polymorphically.

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

# 106. Constructor/Initialization thứ tự (order / 순서)

Rough luồng (flow / 흐름) constructing subclass đối tượng (object / 객체):

```text
allocate object / default values
→ superclass initialization/constructor
→ instance initializers/field initializers
→ subclass constructor body
```

Chính xác (exact / 정확한) thứ tự (ordering / 순서) of trường dữ liệu (field / 필드) initializers relative constructor chuỗi (chain / 사슬) matters.

Danger: superclass constructor calls overridable phương thức (method / 메서드). Override executes before subclass fields initialized.

```java
class Base {
    Base() {
        initialize();
    }

    void initialize() {}
}
```

Subclass override may see default null/0 trạng thái (state / 상태).

Never lời gọi (call / 호출) overridable methods from constructors unless thiết kế (design / 설계) carefully guarantees an toàn (safety / 안전).

---

# 107. URI vs URL

`URI` is identifier/tham chiếu (reference / 참조) cú pháp (syntax / 문법) mô hình (model / 모델). It may be relative and doesn't imply truy cập mạng (network access / 네트워크 접근).

`URL` historically combines locator with liên kết (connection / 연결) hành vi (behavior / 동작).

Hiện đại (modern / 현대적) Java HTTP APIs use `URI` for yêu cầu (request / 요청) mục tiêu (target / 대상):

```java
HttpRequest.newBuilder(
    URI.create(...))
```

When manipulating URLs, don't string-concatenate truy vấn (query / 쿼리)/đường dẫn (path / 경로) blindly. Encode components according URI rules; `URLEncoder` historically targets form/truy vấn (query / 쿼리) encoding ngữ nghĩa (semantics / 의미론), not arbitrary full URL escaping.

---

# 108. DNS hành vi (behavior / 동작)

Host lookup may bộ nhớ đệm (cache / 캐시) positive/negative results according JVM/bảo mật (security / 보안)/provider settings and OS resolver.

DNS TTL and máy khách (client / 클라이언트) liên kết (connection / 연결) pools influence failover.

If dịch vụ (service / 서비스) IP changes, long-lived keepalive connections may continue old address; DNS re-resolution only matters on new liên kết (connection / 연결).

Do not bản dựng (build / 빌드) failover các giả định (assumptions / 가정들) without understanding máy khách (client / 클라이언트)/DNS/bộ cân bằng tải (load balancer / 로드 밸런서) hành vi (behavior / 동작).

---

# 109. ProxySelector

Java networking can use `ProxySelector` to choose proxies for URI.

Hệ thống (system / 시스템) properties/môi trường (environment / 환경) enterprise networks may tuyến (route / 경로) HTTP differently from cục bộ (local / 로컬).

When app works cục bộ (local / 로컬) but cannot reach Internet in corporate môi trường (environment / 환경), proxy/TLS trust/DNS often involved.

HTTP máy khách (client / 클라이언트) builder can configure proxy explicitly.

---

# 110. WebSocket máy khách (client / 클라이언트)

Java HTTP máy khách (client / 클라이언트) includes WebSocket máy khách (client / 클라이언트) APIs.

WebSocket is long-lived bidirectional message liên kết (connection / 연결), not ordinary yêu cầu (request / 요청)/phản hồi (response / 응답).

You implement listener callbacks and demand messages.

Need handle fragmentation, backpressure, reconnect, heartbeat, close status and message kích thước (size / 크기).

Do not keep unlimited pending messages when bên tiêu thụ (consumer / 소비자) slow.

---

# 111. API Documentation là đặc tả hợp đồng (contract / 계약)

Javadoc không nên lặp phương thức (method / 메서드) name bằng prose vô nghĩa.

API công khai (public API / 공개 API) docs phải nói:

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

For thư viện (library / 라이브러리):

```java
/**
 * Returns an immutable snapshot...
 *
 * @throws IllegalStateException
 *         if the session is closed
 */
```

documentation có thể quan trọng ngang kiểu (type / 타입) signature.

---

# 112. `@apiNote`, `@implSpec`, `@implNote`

Javadoc tags cho phân biệt đặc tả hợp đồng (contract / 계약) audiences.

`@apiNote`: useful guidance cho API users nhưng không normative đặc tả hợp đồng (contract / 계약).

`@implSpec`: hiện thực (implementation / 구현) requirements subclasses/implementors phải tuân thủ.

`@implNote`: notes về hiện tại (current / 현재) hiện thực (implementation / 구현), có thể thay mà không phải đặc tả hợp đồng (contract / 계약).

Thư viện (library / 라이브러리) authors nên dùng để tránh consumers phụ thuộc accident hiện thực (implementation / 구현) detail.

---

# 113. Thread-Safety Documentation

Một lớp (class / 클래스) nên nói rõ:

```text
immutable
thread-safe
conditionally thread-safe
not thread-safe
thread-confined
```

Nếu phương thức (method / 메서드) thread-safe individually nhưng chuỗi (sequence / 시퀀스) không atomic, docs phải clarify.

Ví dụ synchronized map:

```java
if (!map.containsKey(k)) {
    map.put(k, v);
}
```

two phương thức (method / 메서드) calls individually synchronized nhưng compound chuỗi (sequence / 시퀀스) vẫn race nếu bên ngoài (external / 외부) synchronization không đúng.

Documentation is part of tính đồng thời (concurrency / 동시성) thiết kế (design / 설계).

---

# 114. bộ nhớ (memory / 메모리) quyền sở hữu (ownership / 소유권) Documentation

For buffers/collections/resources, trạng thái (state / 상태):

```text
caller retains ownership?
callee copies?
returned array mutable?
method retains reference after return?
caller must close?
```

Zero-copy APIs đặc biệt cần quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) rõ.

A buffer passed to async thao tác (operation / 연산) cannot be reused until completion unless API copies it.

Many high-performance bugs are quyền sở hữu (ownership / 소유권) bugs, not cú pháp (syntax / 문법) bugs.

---

# 115. Designing Extension Points

If thư viện (library / 라이브러리) exposes giao diện (interface / 인터페이스) for third-party hiện thực (implementation / 구현), you lose ability to add abstract methods later without breaking implementors.

Default methods can evolve interfaces but may have ngữ nghĩa (semantic / 의미적) conflicts.

Extension điểm (point / 지점) should be minimal, stable, documented, and avoid leaking hiện thực (implementation / 구현) classes.

Sometimes callback/lambda/SPI/provider cấu hình (configuration / 구성) is more evolvable than subclassing abstract cơ sở (base / 기반).

Don't expose extension just “in trường hợp (case / 사례)”; công khai (public / 공개) extension surface is long-term tính tương thích (compatibility / 호환성) commitment.

---

# 116. Reentrancy và callbacks

Suppose collection phương thức (method / 메서드) holds khóa (lock / 잠금) then calls user-provided predicate:

```java
synchronized (...) {
    predicate.test(element);
}
```

Predicate may lời gọi (call / 호출) collection again, possibly reentrant or acquire another khóa (lock / 잠금).

Even reentrant monitor doesn't prevent lock-order deadlock with bên ngoài (external / 외부) locks.

Thư viện (library / 라이브러리) mã (code / 코드) should treat người dùng (user / 사용자) callback as arbitrary mã (code / 코드). Snapshot dữ liệu (data / 데이터)/bản phát hành (release / 릴리스) khóa (lock / 잠금) before callback if bất biến (invariant / 불변식) allows.

This principle appears in observers, comparators, hashCode/equals callbacks and CompletableFuture chains.

---

# 117. Cancellation as first-class concern

Every long-running thao tác (operation / 연산) should answer:

```text
Can caller cancel?
How is cancellation signaled?
Does blocking I/O unblock?
Are child tasks cancelled?
Who cleans resources?
```

Luồng thực thi (thread / 스레드) interrupt is one cơ chế (mechanism / 메커니즘), not universal cancellation đơn vị từ (token / 토큰).

Future cancellation may interrupt tác vụ (task / 작업) if configured; socket close can unblock I/O; structured tính đồng thời (concurrency / 동시성) propagates cancellation structurally.

If cancellation ignored, shutdown/deadline cannot be reliable.

---

# 118. Backpressure beyond Reactive Streams

Backpressure means producer adapts to bên tiêu thụ (consumer / 소비자) sức chứa (capacity / 용량).

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

Every async ranh giới (boundary / 경계) should have sức chứa (capacity / 용량) chính sách (policy / 정책). If producer can outpace bên tiêu thụ (consumer / 소비자) indefinitely, bộ nhớ (memory / 메모리) or độ trễ (latency / 지연 시간) eventually explodes.

---

# 119. tải (load / 로드) Shedding

When saturated, rejecting early may preserve healthy công việc (work / 작업).

Examples:

```text
queue.offer() returns false
HTTP 429/503
drop low-priority telemetry
skip optional refresh
```

The right chiến lược (strategy / 전략) is business-specific.

A hệ thống (system / 시스템) that accepts everything and times out 60 seconds later is often less reliable than one that rejects quickly under tải (load / 로드).

---

# 120. Fairness vs thông lượng (throughput / 처리량)

Fair locks/queues serve waiters roughly arrival thứ tự (order / 순서), reducing starvation.

But fairness prevents barging and can lower thông lượng (throughput / 처리량)/bộ nhớ đệm (cache / 캐시) locality.

Non-fair `ReentrantLock` default often performs better.

Use fairness only when wait-time/starvation ngữ nghĩa (semantics / 의미론) matter, not because “fair sounds correct”.

---

# 121. Priority Inversion Awareness

High-priority tác vụ (task / 작업) waits on khóa (lock / 잠금) held by low-priority luồng thực thi (thread / 스레드); medium-priority CPU tasks prevent low-priority from running/releasing khóa (lock / 잠금).

General JVM ứng dụng (application / 애플리케이션) rarely controls OS priorities reliably enough to “solve” with luồng thực thi (thread / 스레드) priority.

Better avoid long locks and mixed-priority tài nguyên (resource / 자원) sharing.

Realtime các hệ thống (systems / 시스템들) need specialized thiết kế (design / 설계)/thời gian chạy (runtime / 런타임).

---

# 122. False Sharing

Two unrelated hot counters on same CPU bộ nhớ đệm (cache / 캐시) line cause coherence invalidations when different cores ghi (write / 쓰기).

Symptoms show high CPU/bộ nhớ đệm (cache / 캐시) misses despite no logical tranh chấp khóa (lock contention / 잠금 경합).

Libraries may pad/separate dữ liệu (data / 데이터).

Don't randomly pad normal fields; use profiler/hardware counters/JMH.

This belongs mechanical-sympathy tối ưu hóa (optimization / 최적화) after tính đúng đắn (correctness / 정확성).

---

# 123. Mechanical Sympathy

Mechanical sympathy means designing with awareness of hardware/thời gian chạy (runtime / 런타임): bộ nhớ đệm (cache / 캐시) lines, bộ nhớ (memory / 메모리) bandwidth, branch prediction, allocation, syscalls, NUMA, mạng (network / 네트워크).

It does **not** mean writing unreadable low-level mã (code / 코드) everywhere.

High-level Java often lets JIT optimize better than hand tricks.

Use hardware kiến thức (knowledge / 지식) to interpret profiles and choose dữ liệu (data / 데이터) bố cục (layout / 레이아웃)/algorithms on hot paths.

---

# 124. đối tượng (object / 객체) Pooling

Pooling cơ sở dữ liệu (database / 데이터베이스) connections/threads/bản địa (native / 네이티브) expensive resources makes sense because creation is costly or bên ngoài (external / 외부) sức chứa (capacity / 용량) bounded.

Pooling tiny Java objects often hurts:

```text
synchronization
stale state
retention
cache misses
complex ownership
```

Hiện đại (modern / 현대적) allocation/GC is optimized for short-lived objects.

Pool only after profiling shows allocation/initialization chi phí (cost / 비용) and đối tượng (object / 객체) reuse ngữ nghĩa (semantics / 의미론) are safe.

---

# 125. Escape phân tích (analysis / 분석) không phải ngôn ngữ (language / 언어) guarantee

JIT may scalar-replace/eliminate đối tượng (object / 객체) today, but nguồn (source / 소스) ngữ nghĩa (semantics / 의미론) cannot depend on tối ưu hóa (optimization / 최적화) occurring.

Hiệu năng (performance / 성능) can thay đổi (change / 변경) with JDK, mã (code / 코드) shape, profiling.

Do not say “this đối tượng (object / 객체) never allocates” unless you mean observed compiled mã (code / 코드) for specific thời gian chạy (runtime / 런타임).

Ghi (write / 쓰기) semantically correct mã (code / 코드) first.

---

# 126. Polymorphism và JIT

Giao diện (interface / 인터페이스) lời gọi (call / 호출) doesn't always stay expensive virtual dispatch.

If lời gọi (call / 호출) site is monomorphic/bimorphic, JIT can inline/devirtualize with guards.

Too many implementations at hot megamorphic lời gọi (call / 호출) site can reduce inlining.

This is specialist tối ưu hóa (optimization / 최적화). Do not remove interfaces across kiến trúc (architecture / 아키텍처) just to help hypothetical JIT.

Profile inlining decisions on truly hot mã (code / 코드).

---

# 127. mã (code / 코드) bộ nhớ đệm (cache / 캐시)

JIT-compiled mã máy (machine code / 기계어) lives in mã (code / 코드) bộ nhớ đệm (cache / 캐시)/bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

Large động (dynamic / 동적) applications/frameworks can fill mã (code / 코드) bộ nhớ đệm (cache / 캐시) in unusual scenarios, affecting compilation/hiệu năng (performance / 성능).

JFR/jcmd/VM diagnostics expose mã (code / 코드) bộ nhớ đệm (cache / 캐시) stats.

Bộ chứa (container / 컨테이너) RSS includes mã (code / 코드) bộ nhớ đệm (cache / 캐시) outside vùng nhớ động (heap / 힙).

Again: Xmx is not tiến trình (process / 프로세스) bộ nhớ (memory / 메모리).

---

# 128. ClassLoader Leaks sâu hơn

A classloader can unload only when loader and all classes/objects aren't reachable.

A long-lived luồng thực thi (thread / 스레드) ngữ cảnh (context / 맥락) classloader pointing old webapp loader can pin entire triển khai (deployment / 배포).

Other roots: ThreadLocal, static registry in parent loader, JDBC DriverManager, MBeans, executors, logging callbacks.

Vùng nhớ vùng nhớ động (heap / 힙) dump dominator/path-to-GC-root helps find.

Reload environments are especially susceptible.

---

# 129. Reflection truy cập (access / 접근) after strong encapsulation

Hiện đại (modern / 현대적) Java mô-đun (module / 모듈) hệ thống (system / 시스템) strongly encapsulates JDK internals.

Old reflection mã (code / 코드) may thất bại (fail / 실패) with `InaccessibleObjectException`.

`--add-opens` can temporarily open gói (package / 패키지) to reflection:

```bash
--add-opens \
java.base/java.lang=ALL-UNNAMED
```

but treat as di chuyển (migration / 마이그레이션) escape hatch, not permanent kiến trúc (architecture / 아키텍처) if avoidable.

Use supported công khai (public / 공개) APIs.

---

# 130. `final` ngữ nghĩa (semantics / 의미론) ngày càng quan trọng

Final fields/classes/methods help invariants/JIT and future nền tảng (platform / 플랫폼) integrity.

JDK is tightening restrictions around deep reflection/mutation of final fields over releases.

Frameworks historically used reflection to set private/final fields; hiện đại (modern / 현대적) mã (code / 코드) generation/constructor binding is more robust.

Do not depend on illegal deep mutation of immutable objects.

---

# 131. bản địa (native / 네이티브) Crash Diagnostics

A bản địa (native / 네이티브) crash can produce `hs_err_pid*.log` or cốt lõi (core / 핵심) dump.

Dùng chung (common / 공통) causes:

```text
JNI bug
native library
JVM bug
unsafe memory access
hardware
driver
FFM misuse/native callee bug
```

`hs_err` includes problematic frame, luồng thực thi (thread / 스레드), registers, loaded libraries, VM flags, vùng nhớ động (heap / 힙) summary.

If problematic frame is `[C] libfoo.so`, investigate bản địa (native / 네이티브) side, not Java exception handling.

---

# 132. Correlating JFR + GC + bản địa (native / 네이티브) bộ nhớ (memory / 메모리)

One symptom may have multiple signals.

Độ trễ (latency / 지연 시간) spike:
JFR shows allocation burst → GC log shows young pauses → RSS stable.

RSS growth:
vùng nhớ động (heap / 힙) live set stable → NMT shows luồng thực thi (thread / 스레드)/bản địa (native / 네이티브) growing.

CPU spike:
JFR samples in compression → GC normal.

Master diagnostics correlates layers instead of interpreting one chỉ số (metric / 지표) alone.

---

# 133. tệp (file / 파일) Descriptors

Sockets, files, pipes use OS tệp (file / 파일) descriptors/handles.

Leak can thất bại (fail / 실패) with:

```text
Too many open files
```

even vùng nhớ động (heap / 힙) healthy.

Check OS limits and tiến trình (process / 프로세스) FD count.

Try-with-resources closes Java wrappers; liên kết (connection / 연결) pools deliberately keep sockets open within configured sức chứa (capacity / 용량).

Large FD limit is not substitute for fixing leak.

---

# 134. Signals và tiến trình (process / 프로세스) termination

SIGTERM typically used graceful shutdown in Unix/bộ chứa (container / 컨테이너). JVM runs shutdown hooks and normal khung phần mềm (framework / 프레임워크) shutdown if tiến trình (process / 프로세스) can handle tín hiệu (signal / 신호).

SIGKILL cannot be caught; no cleanup.

Crash/power mất mát (loss / 손실) also bypasses hooks.

Therefore durable tính đúng đắn (correctness / 정확성) must not rely on “we will flush in shutdown hook”. Persist trọng yếu (critical / 중요) trạng thái (state / 상태) before acknowledging thao tác (operation / 연산).

---

# 135. Serialization Formats và Java Types

JSON numbers don't distinguish `int`/`long`/BigDecimal exactly the same way Java does. Dates are strings/numbers with đặc tả hợp đồng (contract / 계약). Maps with non-string keys need encoding rules.

Protobuf/Avro have tường minh (explicit / 명시적) schemas/evolution ngữ nghĩa (semantics / 의미론).

When crossing ranh giới (boundary / 경계), Java kiểu (type / 타입) is not wire đặc tả hợp đồng (contract / 계약) automatically.

Thiết kế (design / 설계) lược đồ (schema / 스키마) separately, then map types.

This insight prevents leaking records/entities as permanent tích hợp (integration / 통합) giao thức (protocol / 프로토콜).

---

# 136. Enum Evolution

Adding enum constant can break exhaustive switch written against older các giả định (assumptions / 가정들), serializers/databases/consumers.

Persisting `ordinal()` is fragile because reorder changes meaning.

Bên ngoài (external / 외부) giao thức (protocol / 프로토콜) should use stable string/mã (code / 코드) and unknown-value chiến lược (strategy / 전략).

Thư viện (library / 라이브러리) consumers may have switch without default; adding constant can create hành vi thời gian chạy (runtime behavior / 런타임 동작) differences.

Closed enum is source-compatible addition but potentially behavioral tính tương thích (compatibility / 호환성) thay đổi (change / 변경).

---

# 137. Date/thời gian (time / 시간) Edge Cases

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

uses date adjustment ngữ nghĩa (semantics / 의미론); understand expected nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙).

Timezone rules cập nhật (update / 업데이트) with IANA tzdata. Historical/future offsets can thay đổi (change / 변경) when governments thay đổi (change / 변경) law.

Persist `Instant` for actual sự kiện (event / 이벤트); persist ZoneId if future cục bộ (local / 로컬) schedule needs regional rules.

`System.nanoTime` for duration, wall clock for timestamp.

---

# 138. Concurrent Collections bộ nhớ (memory / 메모리) visibility

Concurrent collection methods define happens-before relationships for successful publication/truy cập (access / 접근) per API specification.

Putting fully constructed đối tượng (object / 객체) into `ConcurrentHashMap` then another luồng thực thi (thread / 스레드) retrieving through map provides safe publication according collection đặc tả hợp đồng (contract / 계약).

This doesn't make đối tượng (object / 객체) mutations after retrieval thread-safe.

Bộ chứa (container / 컨테이너) luồng thực thi (thread / 스레드) an toàn (safety / 안전) and element luồng thực thi (thread / 스레드) an toàn (safety / 안전) are separate.

---

# 139. Fail-fast, weakly consistent, snapshot iteration

Normal `ArrayList` iterator is fail-fast-ish: detects structural modifications best-effort and throws `ConcurrentModificationException`. It is bug detector, not synchronization guarantee.

`ConcurrentHashMap` iterator is weakly consistent: can proceed during modifications, reflect some updates, no fail-fast guarantee.

`CopyOnWriteArrayList` iterator sees snapshot array from iterator creation.

Choose ngữ nghĩa (semantics / 의미론) based use trường hợp (case / 사례), not “concurrent collection always newest dữ liệu (data / 데이터)”.

---

# 140. Immutability is graph-wide

A lớp (class / 클래스) with final fields can still expose mutable đồ thị (graph / 그래프).

```java
record Team(
    List<Member> members) {
}
```

Danh sách (list / 목록) may be immutable but `Member` mutable.

Deep immutability requires reachable trạng thái (state / 상태) immutable or defensively isolated.

You don't always need deep immutability. Just document quyền sở hữu (ownership / 소유권)/mutation đặc tả hợp đồng (contract / 계약).

---

# 141. Deprecation, forRemoval và continuous modernization

`@Deprecated` warns API should not be used. `forRemoval=true` signals stronger intent removal.

`since` documents phiên bản (version / 버전).

Deprecation is di chuyển (migration / 마이그레이션) cửa sổ (window / 윈도우), not immediate thất bại (failure / 실패).

Use trình biên dịch (compiler / 컴파일러) warnings, `jdeprscan`, phụ thuộc (dependency / 의존성) upgrade cadence.

Waiting ten years creates “upgrade cliff”.

---

# 142. nguồn (source / 소스), nhị phân (binary / 이진) và thời gian chạy (runtime / 런타임) tính tương thích (compatibility / 호환성)

Nguồn (source / 소스) compatible means recompilation works.

Nhị phân (binary / 이진) compatible means already compiled clients link against new thư viện (library / 라이브러리).

Behavioral compatible means ngữ nghĩa (semantics / 의미론) expectations still hold.

Changing generic signature can be source-impacting while erasure keeps nhị phân (binary / 이진) phương thức (method / 메서드) descriptor. Changing default phương thức (method / 메서드) can alter dispatch.

Tính tương thích (compatibility / 호환성) is multi-dimensional.

Thư viện (library / 라이브러리) versioning must kiểm thử (test / 테스트) compiled old clients where necessary.

---

# 143. Classpath Hell và Linkage Errors

`NoClassDefFoundError`: required lớp (class / 클래스) unavailable/initialization failed at thời gian chạy (runtime / 런타임).

`NoSuchMethodError`: caller compiled expecting phương thức (method / 메서드) but thời gian chạy (runtime / 런타임) lớp (class / 클래스) phiên bản (version / 버전) lacks it.

`AbstractMethodError`: nhị phân (binary / 이진) mismatch where hiện thực (implementation / 구현) doesn't implement phương thức (method / 메서드) expected by thời gian chạy (runtime / 런타임) giao diện (interface / 인터페이스)/lớp (class / 클래스) evolution.

`IncompatibleClassChangeError`: lớp (class / 클래스)/giao diện (interface / 인터페이스)/static-instance shape mismatch.

These usually indicate phụ thuộc (dependency / 의존성)/classloader mismatch, not mã (code / 코드) branch bug.

Use:

```bash
java -verbose:class
jdeps
dependency:tree
jar tf
```

and inspect actual sản phẩm tạo ra (artifact / 산출물).

---

> **Chuyển mạch:** Vị trí của Master Supplement xác định prerequisite và phạm vi phiên bản cần giữ. Phần **Java 8 → 11 → 17 → 21** giải thích vì sao các thay đổi runtime và API cũ vẫn ảnh hưởng quyết định hiện tại, rồi bàn giao sang các case vận hành.

## Tại sao Master vẫn phải hiểu Java 8 → 11 → 17 → 21 thay vì chỉ nhìn Java 25/26

Master Supplement dùng Java 25/26 để giải thích nền tảng (platform / 플랫폼) mới, nhưng khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) engineer thường phải hỗ trợ (support / 지원) mã (code / 코드) được viết từ nhiều generation. Vì vậy bốn mốc 8, 11, 17 và 21 phải được xem như **tính tương thích (compatibility / 호환성) boundaries**.

Java 8 là ranh giới (boundary / 경계) nơi functional interfaces/default methods trở thành mainstream. Default methods đặc biệt quan trọng với thư viện (library / 라이브러리) evolution: giao diện (interface / 인터페이스) có thể thêm hành vi (behavior / 동작) mà không ngay lập tức phá mọi hiện thực (implementation / 구현) cũ. Lambdas dựa mục tiêu (target / 대상) typing và `invokedynamic`, nên bytecode/thời gian chạy (runtime / 런타임) mô hình (model / 모델) khác anonymous lớp (class / 클래스) dù nguồn (source / 소스) intent có thể tương tự.

Java 11 là ranh giới (boundary / 경계) của post-modular JDK phân phối (distribution / 분포). thư viện (library / 라이브러리) từng dựa JAXB/JAX-WS “có trong JDK” phải khai phụ thuộc (dependency / 의존성) riêng; jlink/mô-đun (module / 모듈) ecosystem và tiêu chuẩn (standard / 표준) HTTP máy khách (client / 클라이언트) thay triển khai (deployment / 배포) các giả định (assumptions / 가정들). Nếu thư viện (library / 라이브러리) claim hỗ trợ (support / 지원) 8 và 11+, CI phải thật sự kiểm thử (test / 테스트) multiple runtimes thay vì compile một lần rồi suy đoán.

Java 17 là ranh giới (boundary / 경계) của strong encapsulation. Frameworks làm DI/ORM/serialization bằng reflection phải tách giữa reflection vào ứng dụng (application / 애플리케이션) classes — legitimate use trường hợp (case / 사례) — và illegal truy cập (access / 접근) vào JDK internals. `--add-opens` là triển khai (deployment / 배포) escape hatch, không phải API công khai (public API / 공개 API) guarantee. Records/sealed types cũng tạo nguồn (source / 소스) các mô hình (models / 모델들) mới mà mã (code / 코드) generators/serializers cần hiểu.

Java 21 là ranh giới (boundary / 경계) của tính đồng thời (concurrency / 동시성) mô hình (model / 모델). Frameworks/executors/pools viết với giả định (assumption / 가정) “mỗi yêu cầu (request / 요청) = expensive OS-backed nền tảng (platform / 플랫폼) luồng thực thi (thread / 스레드)” cần được xem lại khi virtual threads được dùng. Instrumentation, `ThreadLocal`, blocking detection, pool sizing và khả năng quan sát (observability / 관측 가능성) phải phân biệt nền tảng (platform / 플랫폼) với virtual threads.

Khi thiết kế thư viện (library / 라이브러리) multi-release, hãy xác định **minimum supported Java**, **bản dựng (build / 빌드) JDK**, **kiểm thử (test / 테스트) ma trận (matrix / 행렬)**, **optional fast paths** và **API công khai (public API / 공개 API) kiểu (type / 타입) surface**. Đừng expose Java 21-only kiểu (type / 타입) trong API công khai (public API / 공개 API) của thư viện (library / 라이브러리) claim Java 17 tính tương thích (compatibility / 호환성) rồi cố giải bằng reflection. Nếu muốn hiện thực (implementation / 구현) tối ưu theo thời gian chạy (runtime / 런타임) mới, Multi-Release JAR hoặc thời gian chạy (runtime / 런타임) tính năng (feature / 기능) detection có thể phù hợp nhưng làm kiểm thử (test / 테스트)/packaging phức tạp hơn.

---

# 144. Preview, Incubator, Experimental: đừng trộn

**Preview tính năng (feature / 기능)** is fully specified candidate ngôn ngữ (language / 언어)/VM/API requiring opt-in and may thay đổi (change / 변경)/remove before final.

Compile/run:

```bash
javac --enable-preview \
      --release 26 ...

java --enable-preview ...
```

**Incubator modules/APIs** are non-final APIs delivered to gather phản hồi (feedback / 피드백), usually in `jdk.incubator.*`.

**Experimental JVM features** may use `-XX` flags and have even weaker stability.

Môi trường vận hành (production / 운영 환경) chính sách (policy / 정책) should explicitly decide what is allowed.

---

# 145. Java 25 ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) delta quan trọng

Java 25 finalizes several ngôn ngữ (language / 언어) features aimed at teaching/simplicity and constructors. mô-đun (module / 모듈) Import Declarations became permanent. Compact nguồn (source / 소스) Files and Instance Main Methods became permanent, reducing ceremony for small programs. Flexible Constructor Bodies became permanent, allowing certain statements before tường minh (explicit / 명시적) superclass constructor invocation under strict initialization an toàn (safety / 안전) rules.

These do not radically thay đổi (change / 변경) enterprise kiến trúc (architecture / 아키텍처), but they affect ngôn ngữ (language / 언어) mô hình tư duy (mental model / 사고 모델) and teaching.

Java 25 also finalizes Scoped Values, includes Compact đối tượng (object / 객체) Headers and hiện đại (modern / 현대적) GC/AOT/thời gian chạy (runtime / 런타임) changes. Structured tính đồng thời (concurrency / 동시성) remains preview in 25 rather than final.

---

# 146. Compact nguồn (source / 소스) Files và Instance Main Methods

Small beginner program can avoid full lớp (class / 클래스) boilerplate according Java 25 final ngôn ngữ (language / 언어) tính năng (feature / 기능).

This is mostly pedagogy/scripting-like ergonomics, not a reason enterprise mã (code / 코드) should abandon named classes/packages.

Large applications still benefit tường minh (explicit / 명시적) kiểu (type / 타입)/mô-đun (module / 모듈) cấu trúc (structure / 구조).

Understanding tính năng (feature / 기능) matters because hiện đại (modern / 현대적) tutorials may no longer start with `public static void main`.

---

# 147. Flexible Constructor Bodies

Historically tường minh (explicit / 명시적) `super(...)`/`this(...)` had to be first statement. hiện đại (modern / 현대적) tính năng (feature / 기능) allows a constrained prologue before constructor invocation, while preventing truy cập (access / 접근) to uninitialized `this` trạng thái (state / 상태).

Use trường hợp (case / 사례): validate/compute constructor arguments before calling `super`.

The ngôn ngữ (language / 언어) enforces initialization an toàn (safety / 안전); it does not allow arbitrary use of đối tượng (object / 객체) before superclass construction.

This removes awkward static helper patterns in some inheritance constructors.

---

# 148. Java 25 Scoped Values final và Structured tính đồng thời (concurrency / 동시성) preview

Scoped Values are tiêu chuẩn (standard / 표준)/final in Java 25.

Structured tính đồng thời (concurrency / 동시성) remains preview and continues evolving. Do not couple stable thư viện (library / 라이브러리) API công khai (public API / 공개 API) directly to preview structured-concurrency classes unless consumers opt into same bản phát hành (release / 릴리스)/preview.

Use concept—structured tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명)/cancellation/lỗi (error / 오류)—regardless of chính xác (exact / 정확한) preview API.

---

# 149. Java 26 HTTP/3 hỗ trợ (support / 지원)

Java 26 `HttpClient` adds HTTP/3 năng lực (capability / 역량) so applications/libraries can communicate with HTTP/3 servers with minimal API thay đổi (change / 변경).

HTTP/3 runs over QUIC/UDP and changes vận chuyển (transport / 전송) hành vi (behavior / 동작), liên kết (connection / 연결) establishment and mạng (network / 네트워크) middlebox considerations.

You should not assume setting HTTP/3 always faster. máy chủ (server / 서버)/mạng (network / 네트워크) hỗ trợ (support / 지원), mất mát (loss / 손실) mẫu (pattern / 패턴), liên kết (connection / 연결) reuse and fallback matter.

Existing HttpClient API lớp trừu tượng (abstraction / 추상화) demonstrates good thư viện (library / 라이브러리) evolution: giao thức (protocol / 프로토콜) năng lực (capability / 역량) can improve without rewriting ứng dụng (application / 애플리케이션) yêu cầu (request / 요청) mô hình (model / 모델).

---

# 150. Java 26 Structured tính đồng thời (concurrency / 동시성) Sixth Preview

Structured tính đồng thời (concurrency / 동시성) remains preview in Java 26.

The API treats related concurrent subtasks as one đơn vị (unit / 단위) for phép nối (join / 조인), thất bại (failure / 실패)/cancellation and khả năng quan sát (observability / 관측 가능성).

Even if signatures thay đổi (change / 변경), key thiết kế (design / 설계) lesson is stable: child tasks should have bounded thời gian tồn tại (lifetime / 수명) nested inside parent thao tác (operation / 연산).

This avoids “fire future into toàn cục (global / 전역) executor and forget quyền sở hữu (ownership / 소유권)”.

---

# 151. Java 26 thành phần nguyên thủy (primitive / 기본 요소) Patterns Fourth Preview

Mẫu (pattern / 패턴) matching continues expanding to primitives in `instanceof`/switch contexts as preview.

Goal is uniform data-oriented mẫu (pattern / 패턴) matching and safe conversion ngữ nghĩa (semantics / 의미론).

Because preview can thay đổi (change / 변경), don't ghi (write / 쓰기) thư viện (library / 라이브러리) baseline requiring it unless dự án (project / 프로젝트) explicitly uses Java 26 preview.

Learn ngữ nghĩa (semantics / 의미론) but keep stable môi trường vận hành (production / 운영 환경) mã (code / 코드) on final features by default.

---

# 152. Java 26 Lazy Constants

Java 26 contains second preview of Lazy Constants API.

A lazy constant is initialized at most once on demand but then treated with constant-like immutability/tối ưu hóa (optimization / 최적화) ngữ nghĩa (semantics / 의미론).

This addresses “expensive final giá trị (value / 값) but don't want initialize at lớp (class / 클래스) tải (load / 로드)” use cases more explicitly than ad-hoc double-checked locking.

Because it is preview, chính xác (exact / 정확한) API should be read from Java 26 docs before use.

---

# 153. Java 26 véc-tơ (vector / 벡터) API vẫn là Incubator

Véc-tơ (vector / 벡터) API remains incubator in Java 26.

It lets developers express SIMD computations that JIT maps to véc-tơ (vector / 벡터) CPU instructions predictably.

Use cases: numeric processing, codecs, ML primitives, cryptography-like loops where supported.

Not normal CRUD công cụ (tool / 도구).

Incubator status means gói (package / 패키지)/mô-đun (module / 모듈)/API can thay đổi (change / 변경); libraries should avoid exposing incubator types in stable API công khai (public API / 공개 API).

---

# 154. Choosing bản phát hành (release / 릴리스) baseline

Ứng dụng (application / 애플리케이션) môi trường vận hành (production / 운영 환경) baseline should follow:

```text
framework support
vendor support
runtime/container certification
library compatibility
operations capability
security update policy
```

Học tập (learning / 학습) baseline can be newer.

For a Spring Boot 4 ứng dụng (application / 애플리케이션), Java 21 or 25 may be practical depending organization. For nội bộ (internal / 내부) thư viện (library / 라이브러리) supporting broad consumers, baseline might stay 17/21.

Don't confuse “latest tính năng (feature / 기능) kiến thức (knowledge / 지식)” with “must deploy latest non-LTS”.

---

# 155. Master practical dự án (project / 프로젝트) A: bản dựng (build / 빌드) a bounded executor

Implement a small `Executor`/tác vụ (task / 작업) hàng đợi (queue / 큐) wrapper around `ThreadPoolExecutor` with tường minh (explicit / 명시적) bounded hàng đợi (queue / 큐), rejection chính sách (policy / 정책), metrics, graceful shutdown and cancellation.

Ghi (write / 쓰기) kiểm thử tải (load test / 부하 테스트) where producer outpaces bên tiêu thụ (consumer / 소비자).

Observe hàng đợi (queue / 큐) độ trễ (latency / 지연 시간), rejection and bộ nhớ (memory / 메모리).

Then compare with virtual-thread-per-task + Semaphore bulkhead.

Goal is not outperform JDK; goal is internalize sức chứa (capacity / 용량) mô hình (model / 모델).

---

# 156. Master practical dự án (project / 프로젝트) B: mini luồng (flow / 흐름) publisher

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

Kiểm thử (test / 테스트) slow subscriber.

You will quickly understand why reactive libraries are complex and why giao thức (protocol / 프로토콜) tính đúng đắn (correctness / 정확성) matters.

---

# 157. Master practical dự án (project / 프로젝트) C: NIO echo máy chủ (server / 서버)

Bản dựng (build / 빌드) Selector-based TCP echo máy chủ (server / 서버).

Maintain per-connection read/ghi (write / 쓰기) buffers.

Handle partial reads/writes, OP_WRITE registration, disconnect, malformed đầu vào (input / 입력) and backpressure.

Then compare mã (code / 코드) độ phức tạp (complexity / 복잡도) with virtual-thread blocking máy chủ (server / 서버).

This gives concrete intuition for event-loop vs thread-per-connection các mô hình (models / 모델들).

---

# 158. Master practical dự án (project / 프로젝트) D: Java tác nhân (agent / 에이전트)

Ghi (write / 쓰기) tác nhân (agent / 에이전트) that records phương thức (method / 메서드) entry counts for selected gói (package / 패키지).

Use Instrumentation + ClassFile API or mature bytecode thư viện (library / 라이브러리).

Avoid instrumenting tác nhân (agent / 에이전트) itself recursively.

Add JFR custom sự kiện (event / 이벤트).

You will learn nạp lớp (class loading / 클래스 로딩) timing, bytecode transformation and tác nhân (agent / 에이전트) rủi ro (risk / 위험).

---

# 159. Master practical dự án (project / 프로젝트) E: FFM

Lời gọi (call / 호출) a simple C hàm (function / 함수) such as `strlen` or small custom bản địa (native / 네이티브) thư viện (library / 라이브러리) using FFM.

Then map a bản địa (native / 네이티브) struct with MemoryLayout.

Experiment with confined Arena thời gian tồn tại (lifetime / 수명) and access-after-close exception.

Do one callback/upcall to understand thời gian tồn tại (lifetime / 수명).

This teaches bản địa (native / 네이티브) quyền sở hữu (ownership / 소유권) without full JNI boilerplate.

---

# 160. Master practical dự án (project / 프로젝트) F: ReferenceQueue

Create objects referenced only through WeakReference/PhantomReference and observe ReferenceQueue notifications under GC pressure.

Bản dựng (build / 빌드) small cleanup tracker with tường minh (explicit / 명시적) close + Cleaner fallback.

Goal is understand reachability/vòng đời (lifecycle / 생명주기), not bản dựng (build / 빌드) môi trường vận hành (production / 운영 환경) bộ nhớ đệm (cache / 캐시).

---

# 161. Master practical dự án (project / 프로젝트) G: JDK upgrade lab

Take Java 8/11 style dự án (project / 프로젝트).

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

Replace nội bộ (internal / 내부) APIs, legacy date/thời gian (time / 시간), old HTTP máy khách (client / 클라이언트), illegal reflection.

Benchmark startup/thông lượng (throughput / 처리량)/bộ nhớ (memory / 메모리) after each major jump.

This is one of the most valuable real enterprise mastery exercises.

---

# 162. Master self-check: tính đồng thời (concurrency / 동시성)

Bạn nên có thể giải thích tại sao VarHandle có plain/opaque/acquire/bản phát hành (release / 릴리스)/volatile modes và khi nào không nên dùng. Bạn phải hiểu LockSupport permit/spurious wake, AQS exclusive/dùng chung (shared / 공유) chế độ (mode / 모드), ThreadLocal leak, ScopedValue vòng đời (lifecycle / 생명주기), ForkJoin công việc (work / 작업) stealing, blocking hàng đợi (queue / 큐) backpressure và cancellation quyền sở hữu (ownership / 소유권).

Quan trọng hơn, bạn phải biết khi nào **không** viết low-level mã (code / 코드) và chọn high-level utility.

---

# 163. Master self-check: thời gian chạy (runtime / 런타임)

Bạn nên đọc được `javap -v` ở mức nhận biết constant pool, descriptor, bytecode, invokedynamic, synthetic/cầu nối (bridge / 브리지) methods.

Bạn phải giải thích nạp lớp (class loading / 클래스 로딩)/linking/initialization, loader định danh (identity / 식별자), classloader leak, strong encapsulation, hidden classes và agents.

Bạn không cần viết bytecode bằng tay nhưng phải hiểu khung phần mềm (framework / 프레임워크) instrumentation hoạt động ở tầng (layer / 계층) nào.

---

# 164. Master self-check: bộ nhớ (memory / 메모리)/GC

Bạn phải phân biệt vùng nhớ động (heap / 힙), metaspace, mã (code / 코드) bộ nhớ đệm (cache / 캐시), direct/bản địa (native / 네이티브) bộ nhớ (memory / 메모리), luồng thực thi (thread / 스레드) stacks.

Bạn phải hiểu GC roots, TLAB, barriers/card tables, safepoints và collector trade-offs.

Khi RSS cao nhưng vùng nhớ động (heap / 힙) thấp, bạn biết dùng NMT/luồng thực thi (thread / 스레드)/direct buffer clues thay vì chỉ tăng Xmx.

Khi vùng nhớ động (heap / 힙) leak, bạn biết path-to-GC-root/quyền sở hữu (ownership / 소유권) trước collector tuning.

---

# 165. Master self-check: các hệ thống (systems / 시스템들) I/O

Bạn phải hiểu Selector readiness, partial I/O, event-loop blocking và OP_WRITE busy-spin. Bạn phải hiểu tệp (file / 파일) descriptor limits, child-process pipe deadlock, DNS/proxy/TLS layers và HTTP deadline/backpressure.

Bạn phải biết virtual threads thay đổi luồng thực thi (thread / 스레드) scaling nhưng không thay downstream tài nguyên (resource / 자원) sức chứa (capacity / 용량).

---

# 166. Master self-check: thư viện (library / 라이브러리) kỹ thuật (engineering / 엔지니어링)

Bạn phải hiểu generic erasure/reifiable/cầu nối (bridge / 브리지)/wildcard capture, API nguồn (source / 소스)/nhị phân (binary / 이진)/behavioral tính tương thích (compatibility / 호환성), extension điểm (point / 지점) risks, Javadoc đặc tả hợp đồng (contract / 계약), thread-safety documentation và quyền sở hữu (ownership / 소유권).

Bạn phải biết ServiceLoader/mô-đun (module / 모듈) tầng (layer / 계층)/classloader/plugin ranh giới (boundary / 경계), multi-release JAR và mô-đun (module / 모듈) naming.

API công khai (public API / 공개 API) là long-term tính tương thích (compatibility / 호환성) commitment, không chỉ `public` từ khóa (keyword / 키워드).

---

# 167. Master self-check: bản địa (native / 네이티브)/bảo mật (security / 보안)

Bạn phải phân biệt băm (hash / 해시)/MAC/signature/encryption, key/trust store, provider mô hình (model / 모델) và SecureRandom.

Bạn phải hiểu FFM MemorySegment/Arena/thời gian tồn tại (lifetime / 수명), JNI/bản địa (native / 네이티브) crash rủi ro (risk / 위험) và vì sao Unsafe nên được thay bằng supported APIs.

Bạn không cần tự viết crypto giao thức (protocol / 프로토콜) hay bản địa (native / 네이티브) allocator; mastery bao gồm biết specialist ranh giới (boundary / 경계) và không tự phát minh thứ nguy hiểm.

---

# 168. Master self-check: hiện đại (modern / 현대적) JDK

Bạn phải biết tính năng (feature / 기능) nào final và tính năng (feature / 기능) nào preview/incubator.

Java 25: LTS, Scoped Values final, hiện đại (modern / 현대적) ngôn ngữ (language / 언어) simplifications, thời gian chạy (runtime / 런타임) improvements.

Java 26: HTTP/3 tiêu chuẩn (standard / 표준) máy khách (client / 클라이언트) năng lực (capability / 역량), Structured tính đồng thời (concurrency / 동시성) vẫn preview, thành phần nguyên thủy (primitive / 기본 요소) mẫu (pattern / 패턴) matching vẫn preview, Lazy Constants preview và véc-tơ (vector / 벡터) API incubator.

Bạn phải có thói quen đọc JEP/bản phát hành (release / 릴리스) docs thay vì nhớ blog.

---

# 169. Master học tập (learning / 학습) pyramid

Lớp đầu là ngôn ngữ (language / 언어)/hệ kiểu (type system / 타입 시스템): generics, overloading, initialization, sealed/patterns.

Lớp hai là cốt lõi (core / 핵심) libraries: collections, streams/gatherers, tính đồng thời (concurrency / 동시성), I/O/networking, bảo mật (security / 보안), thời gian (time / 시간), luồng (flow / 흐름).

Lớp ba là thời gian chạy (runtime / 런타임): lớp (class / 클래스) files, nạp lớp (class loading / 클래스 로딩), JIT, GC, bộ nhớ (memory / 메모리) mô hình (model / 모델), references, bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

Lớp bốn là các hệ thống (systems / 시스템들): OS files/sockets/processes/signals/bản địa (native / 네이티브) interoperability, khả năng quan sát (observability / 관측 가능성).

Lớp năm là thư viện (library / 라이브러리)/khung phần mềm (framework / 프레임워크) kỹ thuật (engineering / 엔지니어링): SPI, annotation processing, agents, tính tương thích (compatibility / 호환성), modules, API contracts.

Lớp sáu là evolution: JEPs, preview/incubator, bản phát hành (release / 릴리스) upgrade chiến lược (strategy / 전략).

Bạn không “hoàn thành một lớp rồi không bao giờ quay lại”. Mastery là quay lại các lớp khi gặp bài toán (problem / 문제) thật và đào sâu bằng bằng chứng (evidence / 증거)/nguồn (source / 소스).

---

# 170. Priority học sau ba tệp (file / 파일) cốt lõi (core / 핵심)

Nếu mục tiêu của bạn là Java backend/Spring cấp cao (senior / 시니어), ưu tiên cao nhất trong supplement là ThreadLocal/ScopedValue, ForkJoin/common-pool awareness, references/Cleaner, Selector mô hình tư duy (mental model / 사고 모델), nạp lớp (class loading / 클래스 로딩)/linkage errors, annotation processing/agents awareness, FFM awareness, GC barriers/đối tượng (object / 객체) bố cục (layout / 레이아웃) overview, JFR/JMX/tooling, tính tương thích (compatibility / 호환성) và hiện đại (modern / 현대적) JDK 25/26.

VarHandle/AQS/MethodHandle/Class-File API/ModuleLayer/FFM deep internals là ưu tiên tiếp theo khi bạn đọc khung phần mềm (framework / 프레임워크)/JDK nguồn (source / 소스) hoặc bản dựng (build / 빌드) hạ tầng (infrastructure / 인프라).

False sharing, custom classloader, bytecode transformers, lock-free CAS algorithms và bản địa (native / 네이티브) ABI details là specialist độ sâu (depth / 깊이). Học khi công việc hoặc curiosity cần, không phải prerequisites để làm tốt Spring backend.

---

# 171. Khi nào có thể nói “Master Java”?

Không có exam chính thức biến bạn thành master. Một dấu hiệu thực tế là bạn có thể gặp một hành vi (behavior / 동작) lạ và biết **đúng tầng (layer / 계층) để điều tra**.

`NoSuchMethodError` → nhị phân (binary / 이진) phụ thuộc (dependency / 의존성)/classloader.

Độ trễ (latency / 지연 시간) high CPU low → waits, locks, I/O, pools.

RSS high vùng nhớ động (heap / 힙) normal → bản địa (native / 네이티브)/direct/luồng thực thi (thread / 스레드)/metaspace.

Transactional khung phần mềm (framework / 프레임워크) annotation không chạy → proxy/instrumentation/lời gọi (call / 호출) đường dẫn (path / 경로).

Virtual threads nhiều nhưng thông lượng (throughput / 처리량) không tăng → downstream sức chứa (capacity / 용량)/CPU/pinning.

Bộ nhớ (memory / 메모리) leak → reachability/quyền sở hữu (ownership / 소유권)/path-to-root.

Thư viện (library / 라이브러리) upgrade break → nguồn (source / 소스)/nhị phân (binary / 이진)/behavioral tính tương thích (compatibility / 호환성).

Khi bạn có thể dịch khung phần mềm (framework / 프레임워크) symptoms về Java/JVM/OS contracts và đọc nguồn (source / 소스)/docs để xác minh, đó là mức (level / 수준) mastery có giá trị.

---

# 172. Nguồn nên đọc sau supplement

**Java ngôn ngữ (language / 언어) Specification (JLS)** là nguồn chuẩn cho ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론): overload, generics, initialization, expressions, bộ nhớ (memory / 메모리) mô hình (model / 모델) language-level rules.

**Java Virtual Machine Specification (JVMS)** giải lớp (class / 클래스) files, bytecode, loading/linking, xác minh (verification / 확인), instruction set.

**Java SE API Javadocs** là đặc tả hợp đồng (contract / 계약) chính thức của libraries. Đọc phần class-level documentation và phương thức (method / 메서드) contracts, không chỉ signatures.

**OpenJDK JEPs** giải motivation, thiết kế (design / 설계), alternatives và status của new features.

**OpenJDK nguồn (source / 소스)** cho hiện thực (implementation / 구현). Đừng nhầm hiện thực (implementation / 구현) hiện tại với specification guarantee.

**JFR/JDK tooling docs** giúp chuyển kiến thức (knowledge / 지식) thành môi trường vận hành (production / 운영 환경) diagnostics.

---

# 173. Cách đọc OpenJDK nguồn (source / 소스)

Đừng bắt đầu bằng `HotSpot` C++ mã (code / 코드) nếu chưa có câu hỏi.

Bắt đầu từ lớp (class / 클래스) Java bạn đã biết, ví dụ `ConcurrentHashMap`, `CompletableFuture`, `ReentrantLock`, `ArrayList`.

Đọc công khai (public / 공개) đặc tả hợp đồng (contract / 계약) trước, rồi fields, helper methods và comments.

Khi gặp bản địa (native / 네이티브)/intrinsic, dấu vết (trace / 추적) xuống HotSpot nếu câu hỏi cần.

Luôn phân biệt:

```text
specification says must
implementation happens to do
```

Một tối ưu hóa (optimization / 최적화)/nội bộ (internal / 내부) trường dữ liệu (field / 필드) không phải công khai (public / 공개) đặc tả hợp đồng (contract / 계약).

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

VarHandle: “bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) nào cần cho lock-free trạng thái (state / 상태)?”

AQS: “ReentrantLock park/wake waiters thế nào?”

Class-file API: “tác nhân (agent / 에이전트) sửa bytecode ra sao?”

FFM: “Java quản lý bản địa (native / 네이티브) bộ nhớ (memory / 메모리) thời gian tồn tại (lifetime / 수명) thế nào?”

GC barriers: “young GC biết old→young references ở đâu?”

Selector: “một luồng thực thi (thread / 스레드) phục vụ nhiều sockets mà không polling busy thế nào?”

Nếu không có question/use trường hợp (case / 사례), low-level details biến thành trivia dễ quên.

---

# 176. Final roadmap sau Java Master Supplement

Sau bốn tệp (file / 파일):

```text
01 Java Beginner
02 Java Intermediate
03 Java Senior
04 Java Master Supplement
```

không nên tiếp tục tạo “Java Advanced++++” chung nữa. Từ đây, mastery nên tách theo chuyên môn.

Một Java backend engineer có thể đi sâu **Spring/Spring Boot**, persistence/JPA/SQL, phân tán (distributed / 분산) các hệ thống (systems / 시스템들), bảo mật (security / 보안), Kafka/messaging, khả năng quan sát (observability / 관측 가능성) và cloud.

Một JVM/hiệu năng (performance / 성능) engineer đi sâu HotSpot, GC, Trình biên dịch JIT (JIT compiler / JIT 컴파일러), profiling, Linux/perf, hardware hiệu năng (performance / 성능) counters.

Một thư viện (library / 라이브러리)/khung phần mềm (framework / 프레임워크) engineer đi sâu class-file, agents, MethodHandles, annotation processing, JPMS, tính tương thích (compatibility / 호환성) và API thiết kế (design / 설계).

Một các hệ thống (systems / 시스템들) Java engineer đi sâu NIO/Netty, FFM/bản địa (native / 네이티브), protocols và low-latency tính đồng thời (concurrency / 동시성).

Mastery thực tế là độ sâu (depth / 깊이) ở một hoặc vài nhánh, trong khi vẫn giữ mô hình tư duy (mental model / 사고 모델) rộng của Java nền tảng (platform / 플랫폼).

---

# 177. Version-sensitive references

Oracle Java SE hỗ trợ (support / 지원) Roadmap
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle Java Downloads / hiện tại (current / 현재) releases
https://www.oracle.com/java/technologies/downloads/

JDK 25 bản phát hành (release / 릴리스) notes
https://www.oracle.com/java/technologies/javase/25-relnote-issues.html

JDK 26 bản phát hành (release / 릴리스) notes
https://www.oracle.com/java/technologies/javase/26-relnote-issues.html

Java 24 Gatherers API
https://docs.oracle.com/en/java/javase/24/docs/api/java.cơ sở (base / 기반)/java/util/stream/Gatherers.html

Foreign hàm (function / 함수) and bộ nhớ (memory / 메모리) API
https://docs.oracle.com/en/java/javase/22/cốt lõi (core / 핵심)/foreign-function-and-memory-api.html

Java ngôn ngữ (language / 언어) Specification
https://docs.oracle.com/javase/specs/

OpenJDK JEP chỉ mục (index / 인덱스)
https://openjdk.org/jeps/0

> **Bàn giao:** Sau **Tại sao Master vẫn phải hiểu Java 8 → 11 → 17 → 21 thay vì chỉ nhìn Java 25/26**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

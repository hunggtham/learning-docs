# Java cốt lõi (core / 핵심) — Part 3: cấp cao (senior / 시니어) — Rewritten Detailed

> **Mạch đọc:** [README](../README.md) là owner của **Java cốt lõi (core / 핵심) — Part 3: cấp cao (senior / 시니어) — Rewritten Detailed**; dùng README để đặt Part 3 giữa Intermediate và Master Supplement. Từ **Java dưới góc nhìn runtime, concurrency, performance, API design và production engineering** nối qua learning flow, profiling, JVM evidence, DB/HTTP resources và failure modes, rồi chuẩn bị các câu hỏi low-level của Master.

## Java dưới góc nhìn thời gian chạy (runtime / 런타임), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), API thiết kế (design / 설계) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)

> Part 3 không nhằm giúp bạn nhớ thêm nhiều lớp (class / 클래스) trong JDK. Một cấp cao (senior / 시니어) Java engineer phải có khả năng giải thích vì sao mã (code / 코드) đúng hoặc sai dưới tính đồng thời (concurrency / 동시성), biết đối tượng (object / 객체) tồn tại ở đâu và vì sao không được GC, biết phương thức (method / 메서드) lời gọi (call / 호출) có thể được JIT optimize thế nào, biết khi nào luồng thực thi (thread / 스레드) đang chạy hay đang chờ, biết DB/HTTP tài nguyên (resource / 자원) nào đang bị giữ, và biết lấy bằng chứng từ JVM trước khi tuning.
>
> Các tư duy kiểu cấp cao (senior / 시니어), lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구), mẫu lập trình (programming pattern / 프로그래밍 패턴) và mẫu thiết kế (design pattern / 디자인 패턴) được hòa vào nội dung. Khi một mẫu (pattern / 패턴) được nhắc tên, nó được giải thích cùng sự đánh đổi (trade-off / 트레이드오프) và dạng thất bại (failure mode / 실패 모드) thay vì xuất hiện như một checklist để học thuộc.

> **Chuyển mạch:** Trong **Java cốt lõi (core / 핵심) — Part 3: cấp cao (senior / 시니어) — Rewritten Detailed**, **Java dưới góc nhìn thời gian chạy (runtime / 런타임), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), API thiết kế (design / 설계) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)** xác định đầu vào; **Vị trí của Part 3 trong mạch học (learning flow / 학습 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Profiling môi trường vận hành (production / 운영 환경): chọn bằng chứng theo loại bottleneck** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vị trí của Part 3 trong mạch học (learning flow / 학습 흐름)

Part 3 giả định bạn đã đọc [Java Part 2 — Intermediate](./java_part2_intermediate_rewritten_detailed.md). Mục tiêu là đưa kiến thức Java sang môi trường vận hành (production / 운영 환경): Java bộ nhớ (memory / 메모리) mô hình (model / 모델) sâu hơn, luồng thực thi (thread / 스레드)/executor saturation, JVM/JIT/GC, profiling, cơ sở dữ liệu (database / 데이터베이스)/HTTP tài nguyên (resource / 자원) boundaries, API tính tương thích (compatibility / 호환성) và sự cố (incident / 인시던트) debugging. Những internals quá thấp như AQS, VarHandle, agents, Class-File API và FFM được để cho [Java Master Supplement](./java_master_supplement_rewritten_detailed.md) để không làm hỏng mạch học (learning flow / 학습 흐름).

---

# 1. cấp cao (senior / 시니어) Java không đồng nghĩa với thuộc nhiều API

Một nhà phát triển (developer / 개발자) có thể biết hàng trăm methods nhưng vẫn khó xử lý sự cố (incident / 인시던트). cấp cao (senior / 시니어) skill nằm ở khả năng nhìn mã (code / 코드) theo năm câu hỏi: trạng thái (state / 상태) nằm ở đâu, ai sở hữu trạng thái (state / 상태)/tài nguyên (resource / 자원), thực thi (execution / 실행) ngữ cảnh (context / 맥락) nào đang chạy, đặc tả hợp đồng (contract / 계약) tính đồng thời (concurrency / 동시성)/giao dịch (transaction / 트랜잭션) nào bảo vệ tính đúng đắn (correctness / 정확성), và thất bại (failure / 실패) có thể xảy ra ở ranh giới (boundary / 경계) nào.

Ví dụ:

```java
cache.computeIfAbsent(
    key,
    this::loadFromDatabase);
```

Beginner thấy “trượt bộ nhớ đệm (cache miss / 캐시 미스) thì tải (load / 로드) DB”. cấp cao (senior / 시니어) hỏi thêm: map có concurrent không, ánh xạ (mapping / 매핑) hàm (function / 함수) có chạy dưới nội bộ (internal / 내부) synchronization không, DB lời gọi (call / 호출) có khối (block / 블록) lâu không, key cardinality có unbounded không, failed tải (load / 로드) có bị bộ nhớ đệm (cache / 캐시) không, multiple app instances có cùng bộ nhớ đệm (cache / 캐시) không, và stale chính sách (policy / 정책) là gì.

Cấp cao (senior / 시니어) Java là tư duy về **tính đúng đắn (correctness / 정확성) + sức chứa (capacity / 용량) + quyền sở hữu (ownership / 소유권) + khả năng quan sát (observability / 관측 가능성)**, không phải cú pháp nâng cao.

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

Trình biên dịch (compiler / 컴파일러) không ngăn bạn đảo hai account IDs hoặc truyền currency invalid.

Strong lĩnh vực (domain / 도메인) types:

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

làm invalid trạng thái (state / 상태) bị chặn ở construction ranh giới (boundary / 경계).

Đây là giá trị (value / 값) đối tượng (object / 객체) thinking. Bạn không “validate cùng quy tắc (rule / 규칙) ở mọi dịch vụ (service / 서비스)”; bạn parse/construct kiểu (type / 타입) một lần rồi cốt lõi (core / 핵심) tin kiểu (type / 타입) đặc tả hợp đồng (contract / 계약).

---

# 3. định danh (identity / 식별자) và giá trị (value / 값) ngữ nghĩa (semantics / 의미론)

Thực thể (entity / 엔터티) định danh (identity / 식별자):

```text
User ID 42
```

vẫn là cùng người dùng (user / 사용자) dù name đổi.

Giá trị (value / 값) đối tượng (object / 객체):

```text
Money 10,000 KRW
```

được định nghĩa bởi giá trị (value / 값).

Nếu bạn dùng `equals` cho JPA thực thể (entity / 엔터티) theo mutable fields, set/map hành vi (behavior / 동작) có thể thay khi thực thể (entity / 엔터티) đổi. Nếu dùng generated ID trước khi persist, equality của transient thực thể (entity / 엔터티) cũng cần thiết kế (design / 설계).

Không có một universal thực thể (entity / 엔터티) equality recipe. Bạn phải hiểu vòng đời (lifecycle / 생명주기) của định danh (identity / 식별자).

Records rất phù hợp giá trị (value / 값) ngữ nghĩa (semantics / 의미론), nhưng không phải mọi bản ghi (record / 레코드) là lĩnh vực (domain / 도메인) giá trị (value / 값) đối tượng (object / 객체) chỉ vì trình biên dịch (compiler / 컴파일러) generate `equals`.

---

# 4. Stable băm (hash / 해시) Keys là tính đúng đắn (correctness / 정확성) issue

HashMap key fields không nên mutate trong khi key đang nằm trong map.

Tương tự bộ nhớ đệm (cache / 캐시) key đối tượng (object / 객체) cần stable equality/băm (hash / 해시).

Nếu lĩnh vực (domain / 도메인) key mutable, dùng immutable snapshot/giá trị (value / 값) key thay vì thực thể (entity / 엔터티) đối tượng (object / 객체).

```java
Map<UserId, User>
```

thường tốt hơn:

```java
Map<UserEntity, Data>
```

nếu thực thể (entity / 엔터티) equality vòng đời (lifecycle / 생명주기) phức tạp.

Đây là lý do equality đặc tả hợp đồng (contract / 계약) có thể trở thành system-level tính đúng đắn (correctness / 정확성), không chỉ Java interview question.

---

# 5. Records ở mức (level / 수준) cấp cao (senior / 시니어)

Bản ghi (record / 레코드) phù hợp message/cấu hình (config / 설정)/kết quả (result / 결과)/value-like cấu trúc (structure / 구조) vì constructor/accessors/equality rõ và shallowly immutable.

Nhưng:

```java
record Policy(
    List<Rule> rules) {
}
```

không thực sự immutable nếu danh sách (list / 목록) mutable.

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

Nếu `Rule` mutable, đối tượng (object / 객체) đồ thị (graph / 그래프) vẫn chưa deep immutable.

Cấp cao (senior / 시니어) phải reason quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프) chứ không chỉ `final`/bản ghi (record / 레코드) từ khóa (keyword / 키워드).

---

# 6. Sealed Types + mẫu (pattern / 패턴) Matching

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

Trình biên dịch (compiler / 컴파일러) biết hierarchy closed và có thể enforce exhaustiveness.

Cách này rất mạnh cho finite kết quả (result / 결과)/lỗi (error / 오류)/trạng thái (state / 상태) algebra.

Nhưng nếu subclasses có hành vi (behavior / 동작) tự nhiên và open extension là yêu cầu (requirement / 요구사항), polymorphism/giao diện (interface / 인터페이스) extension có thể phù hợp hơn. Sealed không phải “hiện đại (modern / 현대적) replacement inheritance”; nó là modeling công cụ (tool / 도구) cho closed worlds.

---

# 7. mã nguồn (source code / 소스 코드) không chạy trực tiếp

Trình biên dịch (compiler / 컴파일러) tạo bytecode.

```bash
javac UserService.java
javap -c UserService
```

`javap -c` cho instructions.

Bạn không cần đọc bytecode hàng ngày, nhưng nó hữu ích khi muốn biết autoboxing, switch, lambda hoặc compiler-generated cầu nối (bridge / 브리지) methods thực sự biến thành gì.

Ví dụ lambdas thường dùng `invokedynamic` machinery thay vì đơn giản tạo anonymous inner lớp (class / 클래스) như nhiều người tưởng.

---

# 8. JVM ngăn xếp (stack / 스택) Frame và Operand ngăn xếp (stack / 스택)

Mỗi phương thức (method / 메서드) invocation có frame chứa cục bộ (local / 로컬) variables, operand ngăn xếp (stack / 스택) và bookkeeping.

Bytecode thường tải (load / 로드) operands lên ngăn xếp (stack / 스택), execute instruction rồi store kết quả (result / 결과).

Điều này giải thích vì sao JVM được gọi stack-based virtual machine.

Bạn không cần optimize mã (code / 코드) theo bytecode manually. Nhưng khi đọc `javap`, biết cục bộ (local / 로컬) slots/operand ngăn xếp (stack / 스택) giúp hiểu điều khiển (control / 제어) luồng (flow / 흐름) và verifier errors.

---

# 9. JIT Compilation

JVM ban đầu có thể interpret và compile mã (code / 코드) theo tiers. Khi thời gian chạy (runtime / 런타임) profile cho thấy phương thức (method / 메서드)/call-site hot, JIT compile mã máy (machine code / 기계어) optimized.

Optimizations có thể gồm:

```text
inlining
dead-code elimination
escape analysis
loop optimizations
devirtualization
```

Do đó hiệu năng (performance / 성능) của Java phương thức (method / 메서드) sau warm-up khác cold start.

Đây là nguyên nhân microbenchmark naive dễ sai.

---

# 10. Inlining

Phương thức (method / 메서드) lời gọi (call / 호출):

```java
money.add(other)
```

có overhead abstractly, nhưng JIT có thể inline phương thức (method / 메서드) body vào caller nếu profitable.

Small phương thức (method / 메서드) không nhất thiết “chậm vì lời gọi (call / 호출) nhiều”.

Vì vậy đừng viết giant methods để “tránh function-call overhead”.

Maintainable lớp trừu tượng (abstraction / 추상화) thường cho JIT nhiều cơ hội optimize.

Measure đường xử lý nóng (hot path / 핫 패스) thực tế thay vì đoán.

---

# 11. Deoptimization

JIT optimize dựa các giả định (assumptions / 가정들)/profile.

Ví dụ call-site chủ yếu thấy một hiện thực (implementation / 구현) nên JIT devirtualize/inline. Sau đó lớp (class / 클래스) khác xuất hiện và giả định (assumption / 가정) không còn đúng; JVM có thể deoptimize và recompile.

Hiệu năng (performance / 성능) có thể thay đổi trong thời gian chạy (runtime / 런타임).

Một độ trễ (latency / 지연 시간) spike không phải luôn GC; nạp lớp (class loading / 클래스 로딩)/deopt/JIT transitions cũng có thể góp phần trong specialist cases.

JFR/trình biên dịch (compiler / 컴파일러) logs giúp khi thực sự cần.

---

# 12. Escape phân tích (analysis / 분석)

Đối tượng (object / 객체):

```java
Point p = new Point(x, y);
return p.x() + p.y();
```

nếu JIT chứng minh đối tượng (object / 객체) không escape phương thức (method / 메서드)/luồng thực thi (thread / 스레드) ngữ cảnh (context / 맥락), allocation có thể được scalar-replaced/eliminated.

Điều này cho thấy `new` không luôn tương đương expensive vùng nhớ động (heap / 힙) allocation.

Đừng viết đối tượng (object / 객체) pools cho tiny DTOs chỉ để “giảm GC” nếu chưa đo allocation/GC pressure.

Pooling còn làm quyền sở hữu (ownership / 소유권)/tính đồng thời (concurrency / 동시성) phức tạp.

---

# 13. lớp (class / 클래스) vòng đời (lifecycle / 생명주기): Loading, Linking, Initialization

Concept:

```text
load
→ verify
→ prepare
→ resolve
→ initialize
```

Static initialization xảy ra khi lớp (class / 클래스) được initialized theo triggers cụ thể.

Static khối (block / 블록):

```java
static {
    expensiveRemoteCall();
}
```

là risky. lớp (class / 클래스) initialization khóa (lock / 잠금)/thất bại (failure / 실패) có thể làm startup/thời gian chạy (runtime / 런타임) khó gỡ lỗi (debug / 디버그).

Keep static initialization boring: constants/pure setup. bên ngoài (external / 외부) I/O nên có tường minh (explicit / 명시적) vòng đời (lifecycle / 생명주기).

---

# 14. lớp (class / 클래스) Initialization thất bại (failure / 실패)

Nếu static initializer throw:

```java
ExceptionInInitializerError
```

và subsequent use có thể gặp `NoClassDefFoundError` liên quan lớp (class / 클래스) initialization thất bại (failure / 실패).

Nguyên nhân gốc (root cause / 근본 원인) nằm ở first thất bại (failure / 실패), không phải later symptom.

Khi môi trường vận hành (production / 운영 환경) thấy `NoClassDefFoundError`, inspect cause chuỗi (chain / 사슬) và earlier logs.

---

# 15. lớp (class / 클래스) định danh (identity / 식별자) = Name + Defining ClassLoader

Hai classes cùng nhị phân (binary / 이진) name:

```text
com.example.Plugin
```

nhưng loaded bởi different classloaders là distinct thời gian chạy (runtime / 런타임) classes.

Bạn có thể gặp:

```text
ClassCastException:
com.example.Plugin cannot be cast
to com.example.Plugin
```

nghe vô lý nhưng classloaders khác.

App servers, plugin các hệ thống (systems / 시스템들), hot reload, kiểm thử (test / 테스트) tools và agents tạo scenarios này.

---

# 16. Parent Delegation

Typical classloader delegation tìm parent trước để cốt lõi (core / 핵심)/dùng chung (shared / 공유) classes không bị duplicate.

Custom plugin isolation có thể thay chiến lược (strategy / 전략).

Ngữ cảnh (context / 맥락) ClassLoader tồn tại để libraries/frameworks tìm resources/providers trong môi trường (environment / 환경) mà defining loader không đủ.

Không custom classloader nếu không có strong reason; leaks/kiểu (type / 타입) định danh (identity / 식별자)/bảo mật (security / 보안) độ phức tạp (complexity / 복잡도) lớn.

---

# 17. Java bộ nhớ (memory / 메모리) mô hình (model / 모델) là bắt buộc

Tính đồng thời (concurrency / 동시성) không thể reason bằng “luồng thực thi (thread / 스레드) chạy lần lượt chắc thấy giá trị (value / 값)”.

Java bộ nhớ (memory / 메모리) mô hình (model / 모델) định nghĩa visibility, thứ tự (ordering / 순서) và synchronization ngữ nghĩa (semantics / 의미론).

Một **dữ liệu (data / 데이터) race** xảy ra khi multiple threads truy cập (access / 접근) dùng chung (shared / 공유) variable, ít nhất một ghi (write / 쓰기), và accesses không được ordered bởi synchronization phù hợp.

Dữ liệu (data / 데이터) race có thể tạo stale reads, lost updates và behaviors trình biên dịch (compiler / 컴파일러)/CPU được phép thực hiện.

---

# 18. Happens-Before

Nếu hành động (action / 동작) A happens-before B, effects A visible/ordered đối với B theo JMM.

Key relationships gồm monitor unlock → subsequent khóa (lock / 잠금) cùng monitor, volatile ghi (write / 쓰기) → subsequent read cùng variable, actions trước `Thread.start` → luồng thực thi (thread / 스레드) actions, luồng thực thi (thread / 스레드) actions → successful `join`.

Reason bằng happens-before thay vì folklore như “volatile flush CPU bộ nhớ đệm (cache / 캐시)”.

---

# 19. `volatile` không phải giao dịch (transaction / 트랜잭션)

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
volatile int count;
```

`count++` vẫn read-modify-write và race.

```java
if (balance >= amount) {
    balance -= amount;
}
```

cần compound bất biến (invariant / 불변식); volatile không khóa check+cập nhật (update / 업데이트).

Use synchronized/khóa (lock / 잠금)/atomic chuyển tiếp trạng thái (state transition / 상태 전이).

Volatile tốt cho one-variable publication/status flags.

---

# 20. Final Fields và Safe Publication

Final fields có special JMM initialization guarantees nếu đối tượng (object / 객체) construction đúng và `this` không escape trước constructor complete.

Bad:

```java
class Listener {
    Listener(EventBus bus) {
        bus.register(this);
        this.config = loadConfig();
    }
}
```

`this` escape trước fully initialized; another luồng thực thi (thread / 스레드) có thể observe partially constructed trạng thái (state / 상태).

Constructor should finish bất biến (invariant / 불변식) before publishing tham chiếu (reference / 참조).

Safe publication có thể qua final/volatile/synchronized/concurrent collections/static initialization, tùy trường hợp (case / 사례).

---

# 21. Double-Checked Locking

Hiện đại (modern / 현대적) correct form requires volatile:

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

Nhưng simpler alternatives exist: eager static initialization, holder idiom, DI bộ chứa (container / 컨테이너).

Đừng dùng DCL chỉ vì interview familiarity.

---

# 22. `synchronized` vẫn là thành phần nguyên thủy (primitive / 기본 요소) rất tốt

Synchronized gives mutual exclusion + visibility with simpler cú pháp (syntax / 문법)/vòng đời (lifecycle / 생명주기) than manual khóa (lock / 잠금).

```java
synchronized (lock) {
    checkInvariant();
    updateState();
}
```

Khóa (lock / 잠금) **bất biến (invariant / 불변식)**, không khóa (lock / 잠금) random line.

If trạng thái (state / 상태) fields must thay đổi (change / 변경) together, protect them under same khóa (lock / 잠금).

Keep khóa (lock / 잠금) đối tượng (object / 객체) private to prevent bên ngoài (external / 외부) mã (code / 코드) locking it.

---

# 23. trọng yếu (critical / 중요) Section phải nhỏ nhưng đủ

Bạn muốn giữ khóa (lock / 잠금) ngắn để giảm contention.

Nhưng đừng bản phát hành (release / 릴리스) giữa check và cập nhật (update / 업데이트) nếu bất biến (invariant / 불변식) cần atomic.

Bad:

```text
lock
check
unlock

remote computation?

lock
update based on stale check
```

Tính đúng đắn (correctness / 정확성) first, then reduce công việc (work / 작업) by computing immutable/preparable dữ liệu (data / 데이터) outside khóa (lock / 잠금) and lần ghi nhận (commit / 커밋) trạng thái (state / 상태) thay đổi (change / 변경) inside.

---

# 24. Deadlock và khóa (lock / 잠금) thứ tự (ordering / 순서)

Luồng thực thi (thread / 스레드) A:

```text
lock account1
wait account2
```

Luồng thực thi (thread / 스레드) B:

```text
lock account2
wait account1
```

Deadlock.

Toàn cục (global / 전역) thứ tự (ordering / 순서):

```java
Account first =
    id1.compareTo(id2) < 0
        ? a
        : b;
```

always khóa (lock / 잠금) lower ID first.

Consistent khóa (lock / 잠금) thứ tự (order / 순서) is powerful.

Luồng thực thi (thread / 스레드) dump shows `BLOCKED`/owned monitors and deadlock detector can identify cycles.

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

Fair khóa (lock / 잠금) reduces starvation but often lowers thông lượng (throughput / 처리량). Do not turn fairness on because it sounds ethically better; it is scheduling sự đánh đổi (trade-off / 트레이드오프).

---

# 26. ReadWriteLock

Many readers can hold read khóa (lock / 잠금); writer exclusive.

Useful if read-heavy and read trọng yếu (critical / 중요) sections significant.

But hiện đại (modern / 현대적) synchronization/JIT/bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) means it is not automatically faster than single khóa (lock / 잠금).

Benchmark.

---

# 27. StampedLock

Supports optimistic reads.

Luồng (flow / 흐름):

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

Powerful but API is less ergonomic/reentrant ngữ nghĩa (semantics / 의미론) differ. Use only when contention/profile justifies.

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

This can make multi-field bất biến (invariant / 불변식) atomic if trạng thái (state / 상태) is one immutable đối tượng (object / 객체).

CAS vòng lặp (loop / 루프) may thử lại (retry / 재시도) under contention.

Lock-free is not automatically simpler/faster; use high-level concurrent utilities first.

---

# 29. ABA bài toán (problem / 문제)

CAS sees giá trị (value / 값) A, another luồng thực thi (thread / 스레드) changes A→B→A, CAS sees A again and cannot tell intervening thay đổi (change / 변경).

Some algorithms care. Versioned/stamped references can address.

Most ứng dụng (application / 애플리케이션) mã (code / 코드) should not bản dựng (build / 빌드) custom lock-free structures; know concept for thư viện (library / 라이브러리)/thời gian chạy (runtime / 런타임) mã (code / 코드).

---

# 30. LongAdder ngữ nghĩa (semantics / 의미론)

LongAdder scales increments under contention by distributing trạng thái (state / 상태).

Excellent for metrics counters.

If tính đúng đắn (correctness / 정확성) requires atomic “read hiện tại (current / 현재) chính xác (exact / 정확한) giá trị (value / 값) then reset/quyết định (decision / 결정)”, AtomicLong/khóa (lock / 잠금) may be more appropriate.

Hiệu năng (performance / 성능) thành phần nguyên thủy (primitive / 기본 요소) choice must follow ngữ nghĩa (semantic / 의미적) guarantee.

---

# 31. ConcurrentHashMap Atomic Methods

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
map.compute(
    key,
    (k, old) ->
      transition(old));
```

can atomically cập nhật (update / 업데이트) entry relative map's tính đồng thời (concurrency / 동시성) ngữ nghĩa (semantics / 의미론).

Avoid bên ngoài (external / 외부) check-then-act.

Ánh xạ (mapping / 매핑)/remapping functions should not perform long remote calls or complex modifications of same map.

Use map operations to express atomic per-key chuyển tiếp (transition / 전이).

---

# 32. Weakly Consistent Iteration

Concurrent collections often don't throw `ConcurrentModificationException` and provide weakly consistent views.

Iterator may reflect some concurrent updates, not a frozen snapshot.

If you require chính xác (exact / 정확한) snapshot, create immutable bản sao (copy / 복사) or khóa (lock / 잠금) appropriately.

Thread-safe collection cấu trúc (structure / 구조) does not automatically satisfy application-level consistency across multiple operations.

---

# 33. CopyOnWriteArrayList

Reads operate on stable snapshot array; writes bản sao (copy / 복사).

Listener danh sách (list / 목록) with 10 listeners and rare registration: excellent.

10k-element danh sách (list / 목록) with frequent writes: expensive.

Understand tải công việc (workload / 워크로드) ratio and bộ nhớ (memory / 메모리) bản sao (copy / 복사) chi phí (cost / 비용).

---

# 34. BlockingQueue as Backpressure

Bounded hàng đợi (queue / 큐) is one of the simplest môi trường vận hành (production / 운영 환경) backpressure tools.

```java
BlockingQueue<Job> queue =
    new ArrayBlockingQueue<>(500);
```

If producer faster than consumers, hàng đợi (queue / 큐) fills and `put()` waits.

This prevents unlimited bộ nhớ (memory / 메모리) growth.

Sức chứa (capacity / 용량) selection is nghiệp vụ (business / 비즈니스)/hiệu năng (performance / 성능) chính sách (policy / 정책): how much burst buffer is acceptable before slowdown/rejection?

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

Bulkhead isolates tài nguyên (resource / 자원) sức chứa (capacity / 용량) and prevents one phụ thuộc (dependency / 의존성) from consuming all tính đồng thời (concurrency / 동시성).

---

# 36. Coordination Primitives

`CountDownLatch` lets threads wait for N events.

`CyclicBarrier` coordinates repeated phase meeting.

`Phaser` handles động (dynamic / 동적)/multi-phase parties.

Use them for coordination, not general shared-state locking.

Structured tính đồng thời (concurrency / 동시성) may offer clearer vòng đời (lifecycle / 생명주기) for tác vụ (task / 작업) trees in hiện đại (modern / 현대적) Java, but preview/final status depends Java phiên bản (version / 버전).

---

# 37. luồng thực thi (thread / 스레드) Pool = workers + hàng đợi (queue / 큐) + saturation chính sách (policy / 정책)

A pool with 16 threads and unbounded hàng đợi (queue / 큐) may keep accepting công việc (work / 작업) until vùng nhớ động (heap / 힙) dies.

A pool with bounded 1000 hàng đợi (queue / 큐) will reach saturation visibly.

At saturation, choose reject/caller-runs/drop according nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

No universal luồng thực thi (thread / 스레드) count formula. CPU-bound pool close to cores; blocking workloads depend wait/compute ratio, but virtual threads thay đổi (change / 변경) mô hình (model / 모델).

Measure CPU utilization, hàng đợi (queue / 큐) delay and downstream sức chứa (capacity / 용량).

---

# 38. Graceful Executor Shutdown

Owning thành phần (component / 컴포넌트):

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

Tài nguyên (resource / 자원) vòng đời (lifecycle / 생명주기) belongs to đơn vị sở hữu (owner / 오너); don't leave executors running across tests/deploys.

---

# 39. CompletableFuture thực thi (execution / 실행) Topology

A future chuỗi (chain / 사슬) hides threads unless you nhánh học (track / 트랙) executors.

```java
supplyAsync(load, ioExecutor)
    .thenApply(transform)
    .thenComposeAsync(
        this::remote,
        ioExecutor)
```

Which stage runs where matters for blocking.

Dùng chung (common / 공통) pool contamination can cause unrelated features to contend.

Tường minh (explicit / 명시적) executors make sức chứa (capacity / 용량) visible.

---

# 40. `thenApply` vs `thenCompose`

If hàm (function / 함수) returns giá trị (value / 값):

```java
thenApply(User::name)
```

If hàm (function / 함수) returns future:

```java
thenCompose(
    user ->
      loadOrders(user.id()))
```

Using `thenApply` for future-returning hàm (function / 함수) creates nested:

```text
CompletableFuture<
    CompletableFuture<X>>
```

This is same map vs flatMap concept across Optional/Stream/reactive APIs.

---

# 41. CompletableFuture Exceptions

`exceptionally` recovers by supplying giá trị (value / 값).

`handle` transforms success/lỗi (error / 오류).

`whenComplete` observes but usually preserves original kết quả (outcome / 결과) unless callback throws.

If multiple fan-out branches thất bại (fail / 실패), which thất bại (failure / 실패) surfaces can depend composition.

Preserve causes and log at quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계), not every stage.

---

# 42. Future Timeouts do not cancel underlying công việc (work / 작업) automatically in every mẫu (pattern / 패턴)

CompletableFuture hết thời gian chờ (timeout / 타임아웃) methods can complete future exceptionally/default, but underlying thao tác (operation / 연산) may continue depending how tác vụ (task / 작업)/tài nguyên (resource / 자원) cancellation is implemented.

Hết thời gian chờ (timeout / 타임아웃) is caller waiting chính sách (policy / 정책); cancellation is separate.

Remote HTTP máy khách (client / 클라이언트) must have its own yêu cầu (request / 요청)/socket hết thời gian chờ (timeout / 타임아웃)/cancellation.

Don't assume one hết thời gian chờ (timeout / 타임아웃) kills everything downstream.

---

# 43. Fan-Out / Fan-In tải (load / 로드) Amplification

Yêu cầu (request / 요청) fans to 10 downstream calls concurrently.

At 1000 incoming requests, up to 10k calls.

Parallelization can lower individual độ trễ (latency / 지연 시간) while destroying hệ thống (system / 시스템) sức chứa (capacity / 용량).

Bound tính đồng thời (concurrency / 동시성), batch requests or redesign dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권).

Cấp cao (senior / 시니어) hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) is system-level, not single-request-level.

---

# 44. Virtual Threads Java 21

Virtual threads restore simple thread-per-request/tác vụ (task / 작업) style for blocking I/O at large tính đồng thời (concurrency / 동시성).

```java
try (var executor =
     Executors
       .newVirtualThreadPerTaskExecutor()) {

    List<Future<Response>>
        futures = ...
}
```

Don't create fixed pool of 100 virtual threads. That artificially removes their scalability.

Use semaphore/liên kết (connection / 연결) pools for actual scarce resources.

---

# 45. Virtual Threads do not make CPU faster

100k CPU-bound virtual threads on 8 cores still compete for 8 cores.

For CPU workloads, bounded parallelism near cores remains relevant.

Virtual threads shine when threads spend thời gian (time / 시간) blocked on I/O.

Thông lượng (throughput / 처리량) improves because JVM doesn't need one expensive nền tảng (platform / 플랫폼) luồng thực thi (thread / 스레드) per blocking tác vụ (task / 작업).

---

# 46. Pinning

Early virtual-thread generations could pin carrier nền tảng (platform / 플랫폼) luồng thực thi (thread / 스레드) in certain synchronized/bản địa (native / 네이티브)/blocking situations.

Hiện đại (modern / 현대적) JDKs have improved this significantly across releases. Therefore old blanket advice “never synchronized with virtual threads” is outdated.

Use JFR/jcmd events to identify actual pinning before refactor.

Phiên bản (version / 버전) matters.

---

# 47. ThreadLocal with Virtual Threads

Each virtual luồng thực thi (thread / 스레드) can have ThreadLocal values, but huge numbers of threads magnify bộ nhớ (memory / 메모리) footprint if each ThreadLocal stores heavy trạng thái (state / 상태).

Also thread-local ngữ cảnh (context / 맥락) can obscure dependencies.

Hiện đại (modern / 현대적) ScopedValue is designed for scoped immutable ngữ cảnh (context / 맥락) and became final in Java 25. That topic belongs Master Supplement, but cấp cao (senior / 시니어) should already avoid using ThreadLocal as arbitrary toàn cục (global / 전역) lưu trữ (storage / 저장소).

---

# 48. Structured tính đồng thời (concurrency / 동시성) Awareness

Structured tính đồng thời (concurrency / 동시성) treats related child tasks as a lexical/vòng đời (lifecycle / 생명주기) đơn vị (unit / 단위): fork tasks, phép nối (join / 조인), cancel siblings on thất bại (failure / 실패), leave phạm vi (scope / 범위) only when child vòng đời (lifecycle / 생명주기) resolved.

In Java 21 it was preview and continued evolving through later releases, so chính xác (exact / 정확한) API is version-sensitive.

Learn concept before signatures: tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) should not escape its parent accidentally.

---

# 49. GC Roots và Reachability

An đối tượng (object / 객체) is collectable when no longer reachable through GC roots according to tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론).

Roots include luồng thực thi (thread / 스레드) stacks, static fields, JNI references and other JVM structures.

A “bộ nhớ (memory / 메모리) leak” in Java means objects remain reachable accidentally even though nghiệp vụ (business / 비즈니스) no longer needs them.

GC cannot collect reachable garbage by nghiệp vụ (business / 비즈니스) meaning.

---

# 50. Static Collection Leak

Phần này giải thích cơ chế Java/Spring trước khi đưa ra code hoặc bảng. Hãy giữ invariant, lifecycle, edge case và cách quan sát kết quả khi thử trên ứng dụng thật.

```java
static final Map<String, User>
    CACHE = new HashMap<>();
```

if entries never removed, they remain reachable forever.

Changing collector does not fix.

Need eviction/quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기).

Vùng nhớ vùng nhớ động (heap / 힙) dump dominator cây (tree / 트리) can reveal retained kích thước (size / 크기) đường dẫn (path / 경로).

---

# 51. Listener Leak

Register listener:

```java
publisher.addListener(listener);
```

but never unregister.

Publisher long-lived retains listener, listener may retain entire đối tượng (object / 객체) đồ thị (graph / 그래프).

Vòng đời (lifecycle / 생명주기) subscription should return registration handle/AutoCloseable or tường minh (explicit / 명시적) remove.

---

# 52. ThreadLocal Leak

Luồng thực thi (thread / 스레드) pool worker lives long. ThreadLocal giá trị (value / 값) may live as long as worker if not removed.

Mẫu (pattern / 패턴):

```java
try {
    CONTEXT.set(value);
    work();
} finally {
    CONTEXT.remove();
}
```

ThreadLocal vòng đời (lifecycle / 생명주기) must match tác vụ (task / 작업)/yêu cầu (request / 요청), not luồng thực thi (thread / 스레드) pool thời gian tồn tại (lifetime / 수명).

Master Supplement will explain internals/ScopedValue.

---

# 53. hàng đợi (queue / 큐) Backlog Leak

Unbounded hàng đợi (queue / 큐) is logical retention.

Producer > bên tiêu thụ (consumer / 소비자):

```text
queue size ↑
heap ↑
latency ↑
```

Not classic tham chiếu (reference / 참조) bug; sức chứa (capacity / 용량) thiết kế (design / 설계) bug.

Observe hàng đợi (queue / 큐) độ sâu (depth / 깊이).

Bound or load-shed.

---

# 54. ClassLoader Leak

Ứng dụng (application / 애플리케이션) máy chủ (server / 서버)/reload creates new classloader, but old loader remains referenced by ThreadLocal, luồng thực thi (thread / 스레드), static registry, JDBC driver, MBean, logging callback.

All classes/metaspace/đối tượng (object / 객체) graphs loaded by old loader stay alive.

Symptom: metaspace grows after redeploy.

This is why vòng đời (lifecycle / 생명주기) cleanup matters beyond vùng nhớ động (heap / 힙) objects.

---

# 55. Generational GC mô hình tư duy (mental model / 사고 모델)

Many objects die young.

Generational collectors exploit this by focusing young regions frequently and promoting survivors.

Chính xác (exact / 정확한) mechanics differ collectors/releases.

Do not thiết kế (design / 설계) tính đúng đắn (correctness / 정확성) around “đối tượng (object / 객체) goes to old after N collections”; it's hiện thực (implementation / 구현) detail.

---

# 56. G1 GC

G1 divides vùng nhớ động (heap / 힙) into regions and aims predictable pause targets while collecting regions with useful reclaim giá trị (value / 값).

It's dùng chung (common / 공통) default in hiện đại (modern / 현대적) máy chủ (server / 서버) JDKs.

Useful log:

```bash
-Xlog:gc*
```

Don't start with dozens of G1 tuning flags. hiện đại (modern / 현대적) JVM ergonomics are good; first measure allocation, vùng nhớ động (heap / 힙) occupancy, pause cause.

---

# 57. Humongous Objects

In G1, very large objects relative region kích thước (size / 크기) use special humongous allocation treatment.

Large byte arrays/strings/buffers can create fragmentation/GC pressure.

If logs show humongous allocation issues, investigate payload sizes, serialization/buffering, not just increase vùng nhớ động (heap / 힙).

---

# 58. ZGC

ZGC is low-latency concurrent collector designed for very small pause times across large heaps, with hiện đại (modern / 현대적) generational evolution in recent JDKs.

It may trade CPU/thông lượng (throughput / 처리량)/resources differently from G1.

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

Parallel GC targets thông lượng (throughput / 처리량) with parallel stop-the-world công việc (work / 작업).

Collector choice is tải công việc (workload / 워크로드) quyết định (decision / 결정).

A CLI batch that needs max thông lượng (throughput / 처리량) may prefer different GC than latency-sensitive API.

---

# 60. vùng nhớ động (heap / 힙) Sizing

`-Xmx` sets max vùng nhớ động (heap / 힙).

Bộ chứa (container / 컨테이너) bộ nhớ (memory / 메모리) 2 GB with:

```text
-Xmx2g
```

leaves no room for metaspace, luồng thực thi (thread / 스레드) stacks, direct buffers, mã (code / 코드) bộ nhớ đệm (cache / 캐시), bản địa (native / 네이티브) libraries and JVM itself.

Need bản địa (native / 네이티브) headroom.

Use percentage-based container-aware options where appropriate and measure RSS.

---

# 61. `Xms == Xmx` sự đánh đổi (trade-off / 트레이드오프)

Fixing initial = max can reduce vùng nhớ động (heap / 힙) resizing variability and ensure bộ nhớ (memory / 메모리) available early, but commits/reserves larger bộ nhớ (memory / 메모리) footprint and can hurt bộ chứa (container / 컨테이너) density.

No universal môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙).

Tải công việc (workload / 워크로드)/triển khai (deployment / 배포) economics decide.

---

# 62. Metaspace

Lớp (class / 클래스) siêu dữ liệu (metadata / 메타데이터) lives metaspace/bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

Động (dynamic / 동적) lớp (class / 클래스) generation/redeploy/classloader leaks can grow it.

Vùng nhớ vùng nhớ động (heap / 힙) dump alone may not explain metaspace OOM.

Use classloader stats/JFR/NMT.

---

# 63. luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) bộ nhớ (memory / 메모리)

Each nền tảng (platform / 플랫폼) luồng thực thi (thread / 스레드) reserves/uses ngăn xếp (stack / 스택) bộ nhớ (memory / 메모리) controlled partly by `-Xss`.

Thousands of nền tảng (platform / 플랫폼) threads can consume huge bản địa (native / 네이티브) bộ nhớ (memory / 메모리) even if vùng nhớ động (heap / 힙) small.

Virtual threads use different ngăn xếp (stack / 스택) biểu diễn (representation / 표현)/scaling, one reason they hỗ trợ (support / 지원) large tính đồng thời (concurrency / 동시성).

Don't reduce Xss aggressively without understanding deep ngăn xếp (stack / 스택)/StackOverflow risks.

---

# 64. Direct bộ nhớ (memory / 메모리)

DirectByteBuffer allocates bản địa (native / 네이티브)/off-heap bộ nhớ (memory / 메모리).

Mạng (network / 네트워크) frameworks may use direct buffers heavily.

Vùng nhớ vùng nhớ động (heap / 힙) đồ thị (graph / 그래프) may show small wrapper objects while RSS grows due to bản địa (native / 네이티브) buffers.

Observe direct bộ nhớ (memory / 메모리) metrics/NMT/khung phần mềm (framework / 프레임워크) allocator.

---

# 65. bản địa (native / 네이티브) bộ nhớ (memory / 메모리) Tracking

Enable NMT at JVM startup, e.g. appropriate `-XX:NativeMemoryTracking=summary/detail`.

Then:

```bash
jcmd <pid> VM.native_memory summary
```

Breaks down categories like Java vùng nhớ động (heap / 힙), lớp (class / 클래스), luồng thực thi (thread / 스레드), mã (code / 코드), GC, trình biên dịch (compiler / 컴파일러), nội bộ (internal / 내부).

NMT has overhead, especially detail. Use according sự cố (incident / 인시던트) chính sách (policy / 정책).

---

# 66. `jcmd` là Swiss Army Knife

Danh sách (list / 목록) processes:

```bash
jcmd
```

Luồng thực thi (thread / 스레드) dump:

```bash
jcmd <pid> Thread.print
```

Vùng nhớ vùng nhớ động (heap / 힙) info:

```bash
jcmd <pid> GC.heap_info
```

JFR:

```bash
jcmd <pid> JFR.start ...
jcmd <pid> JFR.dump ...
```

VM flags/classloader/bản địa (native / 네이티브) bộ nhớ (memory / 메모리) commands vary phiên bản (version / 버전).

Learn `jcmd <pid> help`.

---

# 67. Đọc luồng thực thi (thread / 스레드) Dump

Luồng thực thi (thread / 스레드) states:

```text
RUNNABLE
BLOCKED
WAITING
TIMED_WAITING
```

RUNNABLE không always CPU-running; bản địa (native / 네이티브) socket I/O may appear differently depending JVM/OS.

Look for many identical stacks, khóa (lock / 잠금) owners, pool waits, DB máy khách (client / 클라이언트) waits.

One dump is snapshot. Take repeated dumps several seconds apart to see persistence/progress.

---

# 68. Deadlock in luồng thực thi (thread / 스레드) Dump

JVM can identify Java-level monitor/ownable synchronizer deadlocks.

If found, inspect khóa (lock / 잠금) acquisition paths and define consistent thứ tự (ordering / 순서).

Don't just increase luồng thực thi (thread / 스레드) pool.

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

Run continuous low-overhead recording where chính sách (policy / 정책) allows so sự cố (incident / 인시던트) lịch sử (history / 이력) exists before bài toán (problem / 문제).

---

> **Chuyển mạch:** Ở chặng này của **Java cốt lõi (core / 핵심) — Part 3: cấp cao (senior / 시니어) — Rewritten Detailed**, cơ chế trong **Vị trí của Part 3 trong mạch học (learning flow / 학습 흐름)** cần được kiểm chứng bằng dấu vết cụ thể; **Profiling môi trường vận hành (production / 운영 환경): chọn bằng chứng theo loại bottleneck** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **Java 8 → 11 → 17 → 21 dưới góc nhìn môi trường vận hành (production / 운영 환경) engineer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Profiling môi trường vận hành (production / 운영 환경): chọn bằng chứng theo loại bottleneck

Profiling không phải mở một profiler rồi nhìn flame đồ thị (graph / 그래프) cho mọi vấn đề. Trước hết hãy phân loại symptom. Nếu CPU cao, CPU sampling/JFR là điểm bắt đầu tốt. Nếu CPU thấp nhưng độ trễ (latency / 지연 시간) cao, hãy nhìn luồng thực thi (thread / 스레드) states, socket/DB waits, connection-pool acquisition, tranh chấp khóa (lock contention / 잠금 경합) và phân tán (distributed / 분산) dấu vết (trace / 추적). Nếu GC CPU/pause cao, cần allocation profile, live-set/vùng nhớ động (heap / 힙) occupancy và GC events. Nếu RSS tăng nhưng vùng nhớ động (heap / 힙) ổn, vùng nhớ động (heap / 힙) profiler một mình không đủ; phải xét direct buffers, luồng thực thi (thread / 스레드) stacks, metaspace và bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

Một workflow môi trường vận hành (production / 운영 환경) có thể bắt đầu bằng metrics để xác nhận khi nào và phạm vi sự cố, sau đó JFR để xem JVM-level events, luồng thực thi (thread / 스레드) dump để xem thực thi (execution / 실행) đang chờ ở đâu, vùng nhớ động (heap / 힙) dump nếu cần retained-object phân tích (analysis / 분석), và cơ sở dữ liệu (database / 데이터베이스)/mạng (network / 네트워크) tooling cho downstream. Không có công cụ (tool / 도구) duy nhất nhìn thấy toàn hệ thống.

CPU sampling trả lời “ngăn xếp (stack / 스택) nào đang tiêu CPU theo thời gian”. Allocation profiling trả lời “mã (code / 코드) nào đang tạo nhiều đối tượng (object / 객체)/bytes”. khóa (lock / 잠금) profiling trả lời “luồng thực thi (thread / 스레드) nào đang chờ monitor/khóa (lock / 잠금)”. Khi nhìn flame đồ thị (graph / 그래프), width biểu thị mẫu (sample / 표본) frequency/chi phí (cost / 비용) tương đối chứ không phải lời gọi (call / 호출) count chính xác; hãy đọc từ ngăn xếp (stack / 스택) gốc (root / 루트) tới hot leaf và kiểm tra nguồn (source / 소스)/tải công việc (workload / 워크로드) trước khi tối ưu.

Quan trọng nhất là luôn có **before/after đo lường (measurement / 측정)**. Nếu đổi cấu trúc dữ liệu (data structure / 자료구조) nhưng p99, CPU và allocation không cải thiện, đó không phải tối ưu hóa (optimization / 최적화) có giá trị. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) là vòng lặp hypothesis → đo lường (measurement / 측정) → thay đổi (change / 변경) → xác minh (verification / 확인).

---

# 70. hiệu năng (performance / 성능): độ trễ (latency / 지연 시간) vs thông lượng (throughput / 처리량)

Độ trễ (latency / 지연 시간) = thời gian (time / 시간) one thao tác (operation / 연산) takes.

Thông lượng (throughput / 처리량) = operations per thời gian (time / 시간).

Tối ưu hóa (optimization / 최적화) can trade them.

Batching increases thông lượng (throughput / 처리량) but may delay individual item.

Large hàng đợi (queue / 큐) can temporarily maximize thông lượng (throughput / 처리량) but destroys tail độ trễ (latency / 지연 시간).

Define SLO before tuning.

---

# 71. Tail độ trễ (latency / 지연 시간)

Average 100 ms with p99 3 s means 1% requests terrible.

Users often feel tail.

Nhánh học (track / 트랙) p50/p95/p99.

GC, DB locks, remote dịch vụ (service / 서비스) jitter, queueing and contention show strongest in tails.

---

# 72. Little's Law Awareness

Concept:

```text
concurrency ≈ throughput × latency
```

If 1000 req/s and average 0.5s, roughly 500 concurrent in-flight operations.

This helps reason luồng thực thi (thread / 스레드)/liên kết (connection / 연결)/hàng đợi (queue / 큐) sức chứa (capacity / 용량).

Not a magic sizing formula but useful hệ thống (system / 시스템) intuition.

---

# 73. Allocation tỷ lệ (rate / 비율)

High allocation can increase GC CPU and bộ nhớ (memory / 메모리) bandwidth even if vùng nhớ động (heap / 힙) never OOMs.

JFR can show allocation hotspots.

Fix unnecessary materialization/large intermediate objects only if profile shows chi phí (cost / 비용).

Don't make mã (code / 코드) unreadable to avoid tiny short-lived objects JIT/GC handle well.

---

# 74. Boxing chi phí (cost / 비용)

Hot vòng lặp (loop / 루프):

```java
Stream<Integer>
```

creates/uses wrappers vs `IntStream`.

Metrics/data-processing hot paths may benefit thành phần nguyên thủy (primitive / 기본 요소) APIs.

Nghiệp vụ (business / 비즈니스) CRUD rarely needs premature boxing tối ưu hóa (optimization / 최적화).

Measure allocation profiles.

---

# 75. String Concatenation

Hiện đại (modern / 현대적) trình biên dịch (compiler / 컴파일러)/JDK uses optimized concat strategies.

Simple:

```java
String s =
    a + ":" + b;
```

fine.

Vòng lặp (loop / 루프) building huge văn bản (text / 텍스트) still benefits builder/streaming.

Hiệu năng (performance / 성능) advice must consider hiện đại (modern / 현대적) JDK, not Java 6 folklore.

---

# 76. False Sharing Awareness

Two threads cập nhật (update / 업데이트) unrelated counters located same bộ nhớ đệm (cache / 캐시) line, causing bộ nhớ đệm (cache / 캐시) coherence traffic.

This is hardware-level hiệu năng (performance / 성능) issue.

Do not pad random fields. Only investigate if low-level benchmark/profile shows bộ nhớ đệm (cache / 캐시) contention.

JVM/JDK internals may use padding techniques unavailable/stable for normal app APIs.

---

# 77. JMH Mindset

Microbenchmark pitfalls include JIT warm-up, dead-code elimination, constant folding, GC, branch prediction.

JMH provides forks, warmup, đo lường (measurement / 측정), Blackhole patterns.

Example “nanoTime around one lời gọi (call / 호출)” is not enough for library-level hiệu năng (performance / 성능) claims.

Benchmark representative dữ liệu (data / 데이터) and triển khai (deployment / 배포) JDK.

---

# 78. Buffered I/O

Hệ thống (system / 시스템) calls are expensive relative bộ nhớ (memory / 메모리) operations.

Buffering aggregates reads/writes.

But double buffering large payloads can waste bộ nhớ (memory / 메모리).

Know underlying API: `Files.newBufferedReader` already buffered ngữ nghĩa (semantics / 의미론); adding redundant layers may not help.

---

# 79. Direct ByteBuffer

Direct buffers can reduce copies in bản địa (native / 네이티브) I/O paths but allocate/free differently and use bản địa (native / 네이티브) bộ nhớ (memory / 메모리).

Good for high-performance networking/tệp (file / 파일) I/O; unnecessary for ordinary small tệp (file / 파일) parsing.

Cleaner/bản địa (native / 네이티브) thời gian tồn tại (lifetime / 수명) historically less deterministic than vùng nhớ động (heap / 힙).

Use frameworks/JDK APIs carefully and observe direct bộ nhớ (memory / 메모리).

---

# 80. FileChannel Transfer

`transferTo`/`transferFrom` may use efficient OS-assisted transfer depending nền tảng (platform / 플랫폼)/JDK.

Useful large tệp (file / 파일) transfer/máy chủ (server / 서버) paths.

Do not assume zero-copy guarantee across all environments; benchmark.

---

# 81. Memory-Mapped Files

`FileChannel.map` maps tệp (file / 파일) region into virtual bộ nhớ (memory / 메모리).

Useful random/large truy cập tệp (file access / 파일 접근) patterns.

But unmapping/vòng đời (lifecycle / 생명주기), page faults, tệp (file / 파일) truncation and address-space hành vi (behavior / 동작) create độ phức tạp (complexity / 복잡도).

Specialist technique, not default tệp (file / 파일) read API.

---

# 82. Java HTTP máy khách (client / 클라이언트) môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)

Reuse máy khách (client / 클라이언트) with liên kết (connection / 연결) management.

Set connect hết thời gian chờ (timeout / 타임아웃).

Set yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃).

Handle status separately from vận chuyển (transport / 전송) thất bại (failure / 실패).

Read body bounded; large body may require streaming handler.

TLS/DNS/proxy settings matter.

Remote-call mã (code / 코드) is a thất bại (failure / 실패) ranh giới (boundary / 경계) and should translate exceptions.

---

# 83. Deadline Propagation

Incoming yêu cầu (request / 요청) has deadline D.

Each child lời gọi (call / 호출) hết thời gian chờ (timeout / 타임아웃) should be <= remaining D minus cục bộ (local / 로컬) margin.

If thử lại (retry / 재시도), each attempt consumes ngân sách (budget / 예산).

This prevents downstream công việc (work / 작업) continuing after caller has already timed out.

Java cốt lõi (core / 핵심) does not provide one universal deadline propagation khung phần mềm (framework / 프레임워크); thiết kế (design / 설계) ngữ cảnh (context / 맥락) explicitly or use khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원) later.

---

# 84. thử lại (retry / 재시도)

Thử lại (retry / 재시도) only transient and safely repeatable operations.

Exponential backoff:

```text
100ms
200ms
400ms
```

add jitter to avoid synchronized thử lại (retry / 재시도) storms.

Limit attempts and total thời gian (time / 시간).

HTTP 400 kiểm tra hợp lệ (validation / 검증) should not thử lại (retry / 재시도). liên kết (connection / 연결) reset maybe thử lại (retry / 재시도) if idempotent.

Payment POST requires idempotency protection.

---

# 85. Circuit Breaker

Nhánh học (track / 트랙) recent failures; open circuit and thất bại (fail / 실패) fast while downstream unhealthy; allow probes later.

Circuit breaker protects hệ thống (system / 시스템), not tính đúng đắn (correctness / 정확성) of one lời gọi (call / 호출).

It belongs resilience thư viện (library / 라이브러리)/khung phần mềm (framework / 프레임워크) mức (level / 수준), but cấp cao (senior / 시니어) Java should understand mẫu (pattern / 패턴) independent of Spring.

---

# 86. Bulkhead

Separate sức chứa (capacity / 용량) per phụ thuộc (dependency / 의존성)/tải công việc (workload / 워크로드).

Payment 20 concurrent, report 5, email 50.

Can be semaphore, executor, liên kết (connection / 연결) pool.

If one subsystem stalls, it doesn't consume all threads/requests.

---

# 87. Reflection chi phí (cost / 비용) không chỉ nanoseconds

Reflection adds thời gian chạy (runtime / 런타임) kiểu (type / 타입)/truy cập (access / 접근) failures, encapsulation break, harder refactor/AOT tính tương thích (compatibility / 호환성) and siêu dữ liệu (metadata / 메타데이터) lookup.

Frameworks use it legitimately.

Ứng dụng (application / 애플리케이션) đường xử lý nóng (hot path / 핫 패스) should not scan methods repeatedly; bộ nhớ đệm (cache / 캐시) siêu dữ liệu (metadata / 메타데이터) if hạ tầng (infrastructure / 인프라) requires.

Main chi phí (cost / 비용) often độ phức tạp (complexity / 복잡도), not raw invoke ns.

---

# 88. MethodHandle Awareness

MethodHandle is typed low-level động (dynamic / 동적) invocation thành phần nguyên thủy (primitive / 기본 요소).

It supports lookup, `MethodType`, adaptation/composition and underpins features like động (dynamic / 동적) languages/lambdas.

Libraries may prefer it over raw reflection for advanced động (dynamic / 동적) dispatch.

Ứng dụng (application / 애플리케이션) nghiệp vụ (business / 비즈니스) mã (code / 코드) rarely needs.

Master Supplement goes deeper.

---

# 89. động (dynamic / 동적) Proxy

JDK Proxy intercepts giao diện (interface / 인터페이스) calls and is cốt lõi (core / 핵심) thiết kế (design / 설계) concept behind khung phần mềm (framework / 프레임워크) clients/AOP.

Invocation handler must correctly handle `equals/hashCode/toString` ngữ nghĩa (semantics / 의미론), exception unwrapping and classloader/giao diện (interface / 인터페이스) visibility.

Naive proxy mã (code / 코드) can wrap mục tiêu (target / 대상) exceptions in `InvocationTargetException`.

Frameworks handle many details.

---

# 90. Annotation Processing vs thời gian chạy (runtime / 런타임) Reflection

Thời gian chạy (runtime / 런타임) annotation:

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

Compile-time generation moves công việc (work / 작업)/errors earlier and avoids thời gian chạy (runtime / 런타임) reflection, but bản dựng (build / 빌드) độ phức tạp (complexity / 복잡도) increases.

MapStruct-like tools show this mô hình (model / 모델).

Master Supplement covers processor APIs.

---

# 91. Annotation không tạo hành vi (behavior / 동작)

`@Retry`
`@Transactional`
`@Inject`

are siêu dữ liệu (metadata / 메타데이터).

Some engine must read it via trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) processing and act.

When annotation “doesn't công việc (work / 작업)”, ask who processes it and whether đối tượng (object / 객체)/lời gọi (call / 호출) đường dẫn (path / 경로) is under that engine.

This mô hình tư duy (mental model / 사고 모델) is essential before Spring.

---

# 92. JDBC giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) là nghiệp vụ (business / 비즈니스) ranh giới (boundary / 경계)

Repository phương thức (method / 메서드):

```java
saveOrder()
```

không necessarily whole giao dịch (transaction / 트랜잭션).

Nghiệp vụ (business / 비즈니스):

```text
create order
reserve local stock rows
write ledger
```

may need one giao dịch (transaction / 트랜잭션).

Giao dịch (transaction / 트랜잭션) should be at use-case/ứng dụng (application / 애플리케이션) ranh giới (boundary / 경계) where atomic yêu cầu (requirement / 요구사항) is known.

Spring later makes declarative chính sách (policy / 정책) easier, but concept belongs Java/cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계).

---

# 93. Keep DB giao dịch (transaction / 트랜잭션) Short

Don't:

```text
open transaction
query/update
call remote HTTP 5s
send email
commit
```

Liên kết (connection / 연결)/locks held during remote wait.

Remote effects aren't rolled back by DB.

Short cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) + outbox/máy trạng thái (state machine / 상태 머신) is often better.

---

# 94. JDBC Isolation và Locking

Giao dịch (transaction / 트랜잭션) isolation must be matched to DB hiện thực (implementation / 구현) and nghiệp vụ (business / 비즈니스) anomaly tolerance.

READ COMMITTED may allow different reads across statements.

SERIALIZABLE stronger but may abort/khối (block / 블록) more.

Use optimistic versioning or tường minh (explicit / 명시적) locks where nghiệp vụ (business / 비즈니스) needs.

Don't set SERIALIZABLE globally “for an toàn (safety / 안전)”.

---

# 95. truy vấn (query / 쿼리) hết thời gian chờ (timeout / 타임아웃)

Statement:

```java
statement.setQueryTimeout(seconds);
```

driver/cơ sở dữ liệu (database / 데이터베이스) hỗ trợ (support / 지원) ngữ nghĩa (semantics / 의미론) vary.

Also liên kết (connection / 연결) acquire hết thời gian chờ (timeout / 타임아웃), mạng (network / 네트워크)/socket hết thời gian chờ (timeout / 타임아웃) and giao dịch (transaction / 트랜잭션) hết thời gian chờ (timeout / 타임아웃) exist.

One tầng (layer / 계층) hết thời gian chờ (timeout / 타임아웃) doesn't guarantee all.

---

# 96. liên kết (connection / 연결) Pool Awareness

Raw DataSource in môi trường vận hành (production / 운영 환경) often backed by pool.

Pool kích thước (size / 크기) controls concurrent DB công việc (work / 작업).

If app has 20 connections and 1000 virtual threads, 980 wait.

That's intentional backpressure if DB only supports 20 effectively.

Observe acquisition wait/active/idle and DB metrics.

---

# 97. bản địa (native / 네이티브) Serialization bảo mật (security / 보안)

Deserializing untrusted Java serialization has historical gadget-chain/code-execution risks.

Do not expose `ObjectInputStream` to arbitrary mạng (network / 네트워크)/tệp (file / 파일) dữ liệu (data / 데이터).

`ObjectInputFilter` can restrict classes/graphs in legacy cases, but di chuyển (migration / 마이그레이션) away from unsafe serialization is often preferable.

Serialization format is trust ranh giới (boundary / 경계).

---

# 98. `SecureRandom`

Use for tokens/cryptographic nonces/keys.

```java
SecureRandom secure =
    new SecureRandom();
```

`Random`, `ThreadLocalRandom` are predictable enough that they should not protect secrets.

UUID random may be fine as identifier but not automatically secret đơn vị từ (token / 토큰) with required entropy/chính sách (policy / 정책).

---

# 99. Password Hashing

Do not:

```java
SHA-256(password)
```

as password lưu trữ (storage / 저장소).

Password hashing requires adaptive, salted algorithms/policies such as Argon2/bcrypt/scrypt/PBKDF2 depending approved ecosystem.

Use maintained bảo mật (security / 보안) thư viện (library / 라이브러리)/khung phần mềm (framework / 프레임워크).

Cryptographic thiết kế (design / 설계) is a specialist lĩnh vực (domain / 도메인).

---

# 100. Secrets

Passwords/API keys/private keys should not be nguồn (source / 소스) constants or logs.

Read from môi trường (environment / 환경)/secret manager/secure tệp (file / 파일) ranh giới (boundary / 경계).

Avoid keeping secrets in String longer than necessary in special high-security contexts, though general Java ecosystem APIs may require strings.

Most importantly: never log them.

---

# 101. Exception kiến trúc (architecture / 아키텍처)

Classify:

```text
domain/business rejection
validation
transient infrastructure
permanent infrastructure/config
programming bug
cancellation/interruption
```

Caller chính sách (policy / 정책) differs.

A `UserNotFoundException` is not same as `DatabaseUnavailableException`.

Thử lại (retry / 재시도)/HTTP ánh xạ (mapping / 매핑)/log mức (level / 수준) should reflect category.

---

# 102. Preserve Cause

Wrap:

```java
throw new PaymentUnavailableException(
    "Payment provider failed",
    e);
```

Cause chuỗi (chain / 사슬) is bằng chứng vận hành (production evidence / 운영 증거).

Do not replace detailed low-level lỗi (error / 오류) with `"something failed"` without cause.

But don't leak cause văn bản (text / 텍스트) directly to bên ngoài (external / 외부) máy khách (client / 클라이언트).

---

# 103. `InterruptedException`

Interruption is cancellation/điều khiển (control / 제어) tín hiệu (signal / 신호).

If phương thức (method / 메서드) can propagate, do so.

If converting:

```java
Thread.currentThread()
      .interrupt();
```

before throwing unchecked if chính sách (policy / 정책) requires.

Swallowing interruption can prevent executor/ứng dụng (application / 애플리케이션) shutdown.

---

# 104. Log Once at quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계)

If repository logs lỗi (error / 오류) + rethrows, dịch vụ (service / 서비스) logs lỗi (error / 오류) + rethrows, controller logs lỗi (error / 오류), same thất bại (failure / 실패) appears three times.

Low layers add ngữ cảnh (context / 맥락) in exception; quyền sở hữu (ownership / 소유권)/yêu cầu (request / 요청) ranh giới (boundary / 경계) logs once with dấu vết (trace / 추적)/yêu cầu (request / 요청) ngữ cảnh (context / 맥락).

Expected nghiệp vụ (business / 비즈니스) errors may be INFO/WARN/no ngăn xếp (stack / 스택), not lỗi (error / 오류).

---

# 105. Java thư viện (library / 라이브러리) API thiết kế (design / 설계)

API công khai (public API / 공개 API) is expensive to thay đổi (change / 변경).

Keep visibility narrow.

Accept abstractions:

```java
Collection<T>
```

when you don't need danh sách (list / 목록) indexing.

Return giao diện (interface / 인터페이스):

```java
List<T>
```

not concrete `ArrayList`.

But don't over-generalize parameter if phương thức (method / 메서드) requires thứ tự (order / 순서)/random truy cập (access / 접근) ngữ nghĩa (semantics / 의미론).

Đặc tả API (API contract / API 계약) should match actual requirements.

---

# 106. Defensive bản sao (copy / 복사) in API công khai (public API / 공개 API)

Constructor receiving collection:

```java
this.items =
    List.copyOf(items);
```

Getter can return immutable danh sách (list / 목록).

This protects nội bộ (internal / 내부) bất biến (invariant / 불변식).

If elements mutable, document/clone/map immutable views according quyền sở hữu (ownership / 소유권).

API công khai (public API / 공개 API) needs tường minh (explicit / 명시적) null/thread-safety/mutation contracts.

---

# 107. nhị phân (binary / 이진), nguồn (source / 소스) và Behavioral tính tương thích (compatibility / 호환성)

Changing phương thức (method / 메서드) signature breaks nguồn (source / 소스)/nhị phân (binary / 이진).

Adding abstract giao diện (interface / 인터페이스) phương thức (method / 메서드) can break implementors unless default.

Changing `equals`/thứ tự (ordering / 순서) hành vi (behavior / 동작) may break behavioral tính tương thích (compatibility / 호환성) even if compile succeeds.

Libraries must think versioning beyond trình biên dịch (compiler / 컴파일러) errors.

SemVer only works if you understand công khai (public / 공개) contracts.

---

# 108. Overload Ambiguity

Overloads with null:

```java
send(String x)
send(byte[] x)
```

Lời gọi (call / 호출):

```java
send(null);
```

ambiguous.

Boxing/varargs/generics make worse.

Thiết kế (design / 설계) API so dùng chung (common / 공통) calls obvious. Use distinct names when ngữ nghĩa (semantic / 의미적) operations differ.

---

# 109. Functional cốt lõi (core / 핵심), Imperative Shell

Pure-ish cốt lõi (core / 핵심):

```java
OrderResult calculate(
    Order order,
    PricingPolicy policy)
```

no DB/mạng (network / 네트워크)/clock hidden.

Imperative shell loads dữ liệu (data / 데이터), calls cốt lõi (core / 핵심), saves kết quả (result / 결과).

This mẫu (pattern / 패턴) improves testability and separates deterministic lô-gic (logic / 논리) from effects.

Java does not need be “functional ngôn ngữ (language / 언어)” to benefit.

---

# 110. Streams không nên giấu điều khiển (control / 제어) luồng (flow / 흐름)

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

Side effects inside lazy chuỗi xử lý (pipeline / 파이프라인) make timing/lỗi (error / 오류)/thứ tự (order / 순서) obscure.

Imperative vòng lặp (loop / 루프) may be clearer.

---

# 111. chiến lược (strategy / 전략), Factory, Decorator, Adapter, Proxy, Command, trạng thái (state / 상태)

Hiện đại (modern / 현대적) Java often implements classic patterns with fewer classes.

Chiến lược (strategy / 전략) can be lambda.

Factory can be static factory.

Decorator wraps giao diện (interface / 인터페이스).

Adapter isolates vendor.

Proxy intercepts calls.

Command can be `Runnable`/bản ghi (record / 레코드) command.

Trạng thái (state / 상태) can be sealed trạng thái (state / 상태) types + chuyển tiếp (transition / 전이) methods.

Do not create mẫu (pattern / 패턴) bureaucracy; understand intent/sự đánh đổi (trade-off / 트레이드오프).

---

# 112. phụ thuộc (dependency / 의존성) Inversion

Cốt lõi (core / 핵심) defines:

```java
interface OrderRepository
interface PaymentGateway
```

Hạ tầng (infrastructure / 인프라) depends inward by implementing.

Use trường hợp (case / 사례) doesn't import JDBC/HTTP SDK.

Spring later wires adapters.

This is the strongest cầu nối (bridge / 브리지) from Java cốt lõi (core / 핵심) to Spring kiến trúc (architecture / 아키텍처).

---

# 113. Ports and Adapters

Ứng dụng (application / 애플리케이션) cốt lõi (core / 핵심) ports represent capabilities it needs.

Inbound adapter: REST/CLI/message invokes use trường hợp (case / 사례).

Outbound adapters: DB/payment/email implement ports.

Khung phần mềm (framework / 프레임워크) is at edge.

This kiến trúc (architecture / 아키텍처) is useful when boundaries/độ phức tạp (complexity / 복잡도) justify, not mandatory for simple CRUD.

---

# 114. Repository and đơn vị (unit / 단위) of công việc (work / 작업)

Repository abstracts aggregate persistence operations.

Đơn vị (unit / 단위) of công việc (work / 작업) groups changes in giao dịch (transaction / 트랜잭션).

JPA persistence ngữ cảnh (context / 맥락) is one hiện thực (implementation / 구현) style; JDBC dịch vụ (service / 서비스) giao dịch (transaction / 트랜잭션) another.

Don't make repository lớp trừu tượng (abstraction / 추상화) hide arbitrary remote/nghiệp vụ (business / 비즈니스) operations.

---

# 115. lĩnh vực (domain / 도메인) Events

Lĩnh vực (domain / 도메인) sự kiện (event / 이벤트) says meaningful fact:

```text
OrderPlaced
PaymentApproved
```

In-process lĩnh vực (domain / 도메인) sự kiện (event / 이벤트) can decouple cục bộ (local / 로컬) handlers.

But publication độ tin cậy (reliability / 신뢰성) differs from phân tán (distributed / 분산) broker sự kiện (event / 이벤트).

Don't confuse đối tượng (object / 객체) sự kiện (event / 이벤트) with durable message.

---

# 116. Idempotency

Thao tác (operation / 연산) executed twice should not duplicate nghiệp vụ (business / 비즈니스) tác động (effect / 효과) when thiết kế (design / 설계) requires.

Payment:

```text
Idempotency-Key
```

Message bên tiêu thụ (consumer / 소비자) stores processed sự kiện (event / 이벤트) ID or uses unique nghiệp vụ (business / 비즈니스) ràng buộc (constraint / 제약조건).

Thử lại (retry / 재시도) without idempotency can duplicate side effects.

This is phân tán (distributed / 분산) tính đúng đắn (correctness / 정확성) foundation.

---

# 117. At-Least-Once Delivery

Many brokers deliver at least once, meaning duplicate is normal.

Bên tiêu thụ (consumer / 소비자) must assume message may repeat.

Exactly-once marketing claims often have scoped ngữ nghĩa (semantics / 의미론); end-to-end nghiệp vụ (business / 비즈니스) side effects still need idempotency/transactions.

---

# 118. Outbox mẫu (pattern / 패턴)

Within cục bộ (local / 로컬) DB giao dịch (transaction / 트랜잭션):

```text
business row changes
+
outbox row
```

Lần ghi nhận (commit / 커밋) together.

Publisher later sends outbox to broker.

Crash/thử lại (retry / 재시도) may duplicate publish, so bên tiêu thụ (consumer / 소비자) idempotent.

Outbox solves dual-write durability gap, not all phân tán (distributed / 분산) problems.

---

# 119. Saga / Compensation

Multiple services can't share simple cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션).

Saga sequences cục bộ (local / 로컬) transactions + compensations.

Compensation is nghiệp vụ (business / 비즈니스) hành động (action / 동작), not chính xác (exact / 정확한) quay lui (rollback / 롤백).

Refund may itself thất bại (fail / 실패) and need thử lại (retry / 재시도)/manual intervention.

Mô hình (model / 모델) tiến trình (process / 프로세스) trạng thái (state / 상태) explicitly.

---

# 120. Testing hành vi (behavior / 동작), not hiện thực (implementation / 구현)

A đơn vị (unit / 단위) kiểm thử (test / 테스트) should assert observable đặc tả hợp đồng (contract / 계약).

If kiểm thử (test / 테스트) asserts private helper called exactly 3 times, harmless refactor breaks kiểm thử (test / 테스트).

Mocks are useful at tác động (effect / 효과) boundaries but over-mocking couples tests to hiện thực (implementation / 구현).

Fake repository can kiểm thử (test / 테스트) trạng thái (state / 상태) transitions naturally.

---

# 121. Deterministic Tests

Điều khiển (control / 제어):

```text
Clock
random
UUID
environment
external services
threads
```

Inject dependencies/fakes.

Never use `Thread.sleep(500)` as primary tính đồng thời (concurrency / 동시성) synchronization if latch/future can express completion.

Flaky kiểm thử (test / 테스트) is production-quality tín hiệu (signal / 신호): timing các giả định (assumptions / 가정들) may be wrong.

---

# 122. đặc tả hợp đồng (contract / 계약) Tests

If multiple repository implementations must share ngữ nghĩa (semantics / 의미론), run same đặc tả hợp đồng (contract / 계약) suite.

If HTTP vendor adapter must honor lược đồ (schema / 스키마), kiểm thử (test / 테스트) stub máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약).

Đặc tả hợp đồng (contract / 계약) testing protects ranh giới (boundary / 경계), not nội bộ (internal / 내부) phương thức (method / 메서드) calls.

---

# 123. tính đồng thời (concurrency / 동시성) Tests

Tính đồng thời (concurrency / 동시성) bugs probabilistic.

Use latches/barriers to orchestrate interleavings, repeated stress, and specialized tools like jcstress for JMM-level mã (code / 코드).

A kiểm thử (test / 테스트) passing 100 times does not mathematically prove lock-free thuật toán (algorithm / 알고리즘) correct.

Avoid custom tính đồng thời (concurrency / 동시성) primitives unless necessary.

---

# 124. Property-Based Testing Awareness

Instead of fixed examples only, generate many inputs and assert bất biến (invariant / 불변식).

Example money addition:

```text
a + zero == a
```

Parser round-trip.

Sorting đầu ra (output / 출력) is ordered + permutation of đầu vào (input / 입력).

Libraries exist; concept useful even with manual generated tests.

---

# 125. Logging, Metrics, Traces

Logs = detailed events.

Metrics = aggregated numeric signals.

Traces = yêu cầu (request / 요청)/thao tác (operation / 연산) causality across components.

JFR = JVM thời gian chạy (runtime / 런타임) events/profile.

Môi trường vận hành (production / 운영 환경) khả năng quan sát (observability / 관측 가능성) combines them.

Logging every yêu cầu (request / 요청) body is not khả năng quan sát (observability / 관측 가능성) chiến lược (strategy / 전략).

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

over free văn bản (text / 텍스트) impossible to truy vấn (query / 쿼리).

Use logging khung phần mềm (framework / 프레임워크) later, but Java cốt lõi (core / 핵심) mã (code / 코드) should pass contextual info through boundaries rather than toàn cục (global / 전역) static mutable ngữ cảnh (context / 맥락).

---

# 127. Correlation ID

Unique yêu cầu (request / 요청)/thao tác (operation / 연산) ID helps link logs.

In hệ thống phân tán (distributed system / 분산 시스템), dấu vết (trace / 추적) IDs often serve technical correlation.

Do not use dấu vết (trace / 추적) ID as nghiệp vụ (business / 비즈니스) idempotency key unless ngữ nghĩa (semantics / 의미론) align.

Ngữ cảnh (context / 맥락) propagation must cross executor/HTTP boundaries intentionally.

---

# 128. chỉ số (metric / 지표) Cardinality

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

explodes thời gian (time / 시간) series.

Metrics thiết kế (design / 설계) is bộ nhớ (memory / 메모리)/chi phí (cost / 비용)/hiệu năng (performance / 성능) concern.

Keep high-cardinality IDs in logs/traces.

---

# 129. tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권)

Hàm (function / 함수) that creates tài nguyên (resource / 자원) should clearly transfer/retain quyền sở hữu (ownership / 소유권).

```java
InputStream open()
```

caller owns close if đặc tả hợp đồng (contract / 계약) says so.

Phương thức (method / 메서드) receiving stream should not close unless documented.

Ambiguous quyền sở hữu (ownership / 소유권) causes leaks or premature close.

Use `AutoCloseable`/try-with-resources.

---

# 130. Shutdown Hook

Mục này biến kiến thức backend thành tiêu chí kiểm tra và quyết định triển khai. Hãy xác định contract, failure mode, evidence và cách rollback trước khi áp dụng.

```java
Runtime.getRuntime()
       .addShutdownHook(
           new Thread(
             this::shutdown));
```

can cleanup on normal JVM shutdown signals.

But not guaranteed on `kill -9`, crash or machine mất mát (loss / 손실).

Durability cannot depend solely on shutdown hooks.

Frameworks like Spring provide vòng đời (lifecycle / 생명주기) lớp trừu tượng (abstraction / 추상화); concept remains.

---

# 131. Immutable Snapshot

Dùng chung (shared / 공유) cấu hình (configuration / 구성)/trạng thái (state / 상태) can be represented immutable đối tượng (object / 객체) and replaced atomically:

```java
volatile Config config;
```

Readers take snapshot tham chiếu (reference / 참조); writer builds new cấu hình (config / 설정) then publish.

This reduces fine-grained locking compared mutating many fields.

Snapshot mẫu (pattern / 패턴) useful for routing/cấu hình (config / 설정)/bộ nhớ đệm (cache / 캐시) siêu dữ liệu (metadata / 메타데이터).

---

# 132. bộ nhớ đệm (cache / 캐시) is dữ liệu (data / 데이터) Consistency hệ thống (system / 시스템)

Bộ nhớ đệm (cache / 캐시) decisions:

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

Unbounded `ConcurrentHashMap` is not môi trường vận hành (production / 운영 환경) bộ nhớ đệm (cache / 캐시).

Libraries like Caffeine offer eviction/metrics; phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시) adds mạng (network / 네트워크)/serialization.

But mẫu (pattern / 패턴) ngữ nghĩa (semantics / 의미론) come first.

---

# 133. bộ nhớ đệm (cache / 캐시) Stampede

Popular entry expires; thousands requests tải (load / 로드) same DB giá trị (value / 값).

Mitigation single-flight/per-key synchronization, refresh-ahead, stale serving, TTL jitter.

If loader is under khóa (lock / 잠금), ensure slow loader doesn't khối (block / 블록) unrelated keys.

---

# 134. Negative Caching

Repeated non-existent key can hammer DB.

Bộ nhớ đệm (cache / 캐시) “not found” briefly if ngữ nghĩa (semantics / 의미론) allow.

But newly created dữ liệu (data / 데이터) may remain invisible until negative TTL expires.

Trade consistency for tải (load / 로드).

---

# 135. thời gian (time / 시간) tính đúng đắn (correctness / 정확성)

Use `Instant` for chính xác (exact / 정확한) timeline events.

Use `LocalDate` for birthday/nghiệp vụ (business / 비즈니스) date.

Use `ZonedDateTime` when zone rules matter.

Store zone ID separately if future cục bộ (local / 로컬) scheduling matters.

Don't use máy chủ (server / 서버) default timezone implicitly.

Inject `Clock` for lô-gic (logic / 논리)/testing.

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

`currentTimeMillis` wall-clock can jump due thời gian (time / 시간) corrections.

Don't store `nanoTime` as timestamp.

---

# 137. Money tính đúng đắn (correctness / 정확성)

Use BigDecimal from String/valueOf.

Define quy mô (scale / 규모)/rounding.

Compare numeric giá trị (value / 값) via `compareTo` when lĩnh vực (domain / 도메인) ignores quy mô (scale / 규모).

Better create `Money` kiểu (type / 타입) carrying Currency and chính sách (policy / 정책).

Avoid double.

These aren't “financial best practices” only; they prevent deterministic dữ liệu (data / 데이터) bugs.

---

# 138. Collections at cấp cao (senior / 시니어) mức (level / 수준)

Độ phức tạp (complexity / 복잡도) bảng (table / 테이블) isn't enough.

`ArrayList` often beats LinkedList due bộ nhớ đệm (cache / 캐시) locality.

Pre-size when large known sức chứa (capacity / 용량):

```java
new ArrayList<>(expected);
```

but don't over-allocate huge lists blindly.

EnumSet/EnumMap excellent for enum domains.

Java 21 Sequenced Collections improve first/last/reversed ngữ nghĩa (semantics / 의미론).

---

# 139. Streams at cấp cao (senior / 시니어) mức (level / 수준)

Laziness + single-use + side-effect các ràng buộc (constraints / 제약조건들) matter.

Parallel stream shares dùng chung (common / 공통) pool by default and may amplify blocking.

Custom Collector must satisfy định danh (identity / 식별자)/associativity/combiner contracts for parallel tính đúng đắn (correctness / 정확성).

Use stream for transformation, vòng lặp (loop / 루프) for stateful điều khiển (control / 제어) when clearer.

---

# 140. gói (package / 패키지) by tính năng (feature / 기능) vs Technical Layers

Tính năng (feature / 기능) gói (package / 패키지):

```text
order/
payment/
customer/
```

supports cohesive boundaries.

Package-private types prevent leakage.

Technical gói (package / 패키지) toàn cục (global / 전역) can encourage every dịch vụ (service / 서비스) importing every repository.

No universal cấu trúc (structure / 구조); enforce phụ thuộc (dependency / 의존성) direction.

JPMS optional stronger ranh giới mô-đun (module boundary / 모듈 경계).

---

# 141. JDK Upgrade is kỹ thuật (engineering / 엔지니어링) dự án (project / 프로젝트)

8→11 includes removed modules/APIs, new HTTP, GC/default changes.

11→17 includes strong encapsulation, ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) changes.

17→21 includes virtual threads, mẫu (pattern / 패턴) matching, GC/thời gian chạy (runtime / 런타임) improvements.

21→25 includes another LTS and major thời gian chạy (runtime / 런타임)/ngôn ngữ (language / 언어)/thư viện (library / 라이브러리) evolution.

Don't only thay đổi (change / 변경) `<java.version>`.

Run tests, phụ thuộc (dependency / 의존성) tính tương thích (compatibility / 호환성), hiệu năng (performance / 성능) baseline, GC/JFR, startup, bộ chứa (container / 컨테이너) bộ nhớ (memory / 메모리) and deprecated/nội bộ (internal / 내부) API scans.

---

> **Chuyển mạch:** Profiling chỉ có ý nghĩa khi chọn evidence theo bottleneck; phần phiên bản Java đặt kết quả đó vào các thay đổi runtime từ 8 đến 21. Hai khối này cùng dẫn tới quyết định vận hành có thể kiểm chứng, không phải danh sách release note.

## Java 8 → 11 → 17 → 21 dưới góc nhìn môi trường vận hành (production / 운영 환경) engineer

Ở mức (level / 수준) cấp cao (senior / 시니어), phiên bản (version / 버전) evolution không còn là câu chuyện cú pháp (syntax / 문법) đẹp hơn. Mỗi mốc thay đổi các giả định (assumptions / 가정들) của bản dựng (build / 빌드), thời gian chạy (runtime / 런타임) hoặc tính đồng thời (concurrency / 동시성) mô hình (model / 모델).

Java 8 đưa lambdas/streams/`java.time` vào mainstream, nhưng cũng là generation nơi rất nhiều enterprise frameworks dựa classpath, deep reflection và JDK-bundled Java EE APIs. “Java 8 ứng dụng (application / 애플리케이션)” thường mang các giả định (assumptions / 가정들) mà mã nguồn (source code / 소스 코드) không thể hiện rõ.

Java 11 buộc bản dựng (build / 빌드) trở nên tường minh (explicit / 명시적) hơn. JAXB/JAX-WS và Java EE/CORBA modules không còn bundled trong JDK, tiêu chuẩn (standard / 표준) HTTP máy khách (client / 클라이언트) xuất hiện và một số triển khai (deployment / 배포) các giả định (assumptions / 가정들) cũ biến mất. Khi di chuyển (migration / 마이그레이션), phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và packaging quan trọng ngang nguồn (source / 소스) tính tương thích (compatibility / 호환성). `ClassNotFoundException` sau upgrade có thể là nền tảng (platform / 플랫폼) thành phần (component / 컴포넌트) đã bị removed chứ không phải bug mới trong nghiệp vụ (business / 비즈니스) mã (code / 코드).

Java 17 làm encapsulation ranh giới (boundary / 경계) cứng hơn. Strong encapsulation làm nhiều illegal reflective accesses trở thành lỗi thay vì warning. Đồng thời records, sealed classes và mẫu (pattern / 패턴) matching giúp mô hình ứng dụng (application model / 애플리케이션 모델) closed/value-centric concepts bằng hệ kiểu (type system / 타입 시스템) thay vì conventions.

Java 21 thay đổi tính đồng thời (concurrency / 동시성) economics với Virtual Threads. High-concurrency blocking servers có thể giữ imperative style với rất nhiều lightweight threads, nhưng cấp cao (senior / 시니어) vẫn phải đặt bulkhead tại cơ sở dữ liệu (database / 데이터베이스), HTTP máy khách (client / 클라이언트), tỷ lệ (rate / 비율) limit và CPU. luồng thực thi (thread / 스레드) không còn là scarce tài nguyên (resource / 자원) theo cùng cách; **downstream sức chứa (capacity / 용량) vẫn scarce**. mẫu (pattern / 패턴) matching for `switch` và bản ghi (record / 레코드) patterns cũng làm sealed hierarchies hữu ích hơn vì trình biên dịch (compiler / 컴파일러) có thể check exhaustiveness.

Khi nâng phiên bản (version / 버전) môi trường vận hành (production / 운영 환경), tách nền tảng (platform / 플랫폼) upgrade, phụ thuộc (dependency / 의존성) upgrade và nguồn (source / 소스) modernization khi có thể. Chạy tests trên mục tiêu (target / 대상) JDK, dùng `jdeps`/`jdeprscan`, kiểm tra removed/deprecated APIs, đo startup/vùng nhớ động (heap / 힙)/GC/JFR baseline, rồi mới quyết định dùng tính năng (feature / 기능) mới. phiên bản (version / 버전) upgrade thành công không chỉ là “compile được”; nó phải giữ tính đúng đắn (correctness / 정확성) và SLO.

---

# 142. `--release`

Bản dựng (build / 빌드) mục tiêu (target / 대상) must match thời gian chạy (runtime / 런타임) nền tảng (platform / 플랫폼).

Maven/Gradle configure trình biên dịch (compiler / 컴파일러) bản phát hành (release / 릴리스).

Third-party dependencies may require newer thời gian chạy (runtime / 런타임) even if your nguồn (source / 소스) uses old cú pháp (syntax / 문법).

Inspect packaged sản phẩm tạo ra (artifact / 산출물) and CI thời gian chạy (runtime / 런타임).

---

# 143. Java 25 and Java 26 ngữ cảnh (context / 맥락)

As of the cập nhật (update / 업데이트) date of this document, Java 25 is the hiện tại (current / 현재) LTS family and Java 26 is the hiện tại (current / 현재) non-LTS family. Java 21, 17, 11 and 8 remain important enterprise baselines.

Học tập (learning / 학습) chiến lược (strategy / 전략): understand Java 8 fundamentals, ghi (write / 쓰기) hiện đại (modern / 현대적) mã (code / 코드) with 17/21 baseline awareness, and know 25/26 evolution. Don't force môi trường vận hành (production / 운영 환경) upgrade before khung phần mềm (framework / 프레임워크)/vendor tính tương thích (compatibility / 호환성).

Master Supplement covers Scoped Values, FFM, Stream Gatherers, Class-File API and newer bản phát hành (release / 릴리스) deltas.

---

# 144. rà soát mã (code review / 코드 리뷰): phương thức (method / 메서드)

Ask whether name reflects intent, inputs/outputs have ngữ nghĩa (semantic / 의미적) types, null chính sách (policy / 정책) clear, side effects obvious, exceptions meaningful, blocking/hết thời gian chờ (timeout / 타임아웃) visible, giao dịch (transaction / 트랜잭션)/tính đồng thời (concurrency / 동시성) ngữ cảnh (context / 맥락) assumed.

A short phương thức (method / 메서드) can still be bad if hidden remote lời gọi (call / 호출). A long phương thức (method / 메서드) can be okay if tuyến tính (linear / 선형) thuật toán (algorithm / 알고리즘) is clearer than artificial fragmentation.

Rà soát (review / 검토) contracts, not line count.

---

# 145. rà soát mã (code review / 코드 리뷰): lớp (class / 클래스)

Ask responsibility/cohesion, mutable trạng thái (state / 상태), luồng thực thi (thread / 스레드) an toàn (safety / 안전), vòng đời (lifecycle / 생명주기), phụ thuộc (dependency / 의존성) count, visibility, invariants, equality.

If lớp (class / 클래스) needs 15 collaborators, maybe God dịch vụ (service / 서비스)/use-case boundaries wrong.

If lớp (class / 클래스) has mutable dùng chung (shared / 공유) fields but no synchronization/thread-confinement đặc tả hợp đồng (contract / 계약), rủi ro (risk / 위험).

---

# 146. rà soát mã (code review / 코드 리뷰): tính đồng thời (concurrency / 동시성)

Identify dùng chung (shared / 공유) mutable trạng thái (state / 상태).

What establishes happens-before?

What thao tác (operation / 연산) must be atomic?

Locks thứ tự (order / 순서)?

Hàng đợi (queue / 큐) bounded?

Cancellation/interrupt?

Executor quyền sở hữu (ownership / 소유권)?

Downstream sức chứa (capacity / 용량)?

Without answers, concurrent mã (code / 코드) isn't “probably okay”.

---

# 147. rà soát mã (code review / 코드 리뷰): I/O

Who closes tài nguyên (resource / 자원)?

Charset?

Large dữ liệu (data / 데이터) loaded whole bộ nhớ (memory / 메모리)?

Hết thời gian chờ (timeout / 타임아웃)?

Đường dẫn (path / 경로) traversal?

Partial read/ghi (write / 쓰기)?

Thử lại (retry / 재시도)/idempotency?

Lỗi (error / 오류) translation?

These questions catch môi trường vận hành (production / 운영 환경) issues earlier than cú pháp (syntax / 문법) rà soát (review / 검토).

---

# 148. rà soát mã (code review / 코드 리뷰): Persistence

Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계)?

Liên kết (connection / 연결) quyền sở hữu (ownership / 소유권)?

PreparedStatement?

Truy vấn (query / 쿼리) hết thời gian chờ (timeout / 타임아웃)?

Isolation?

Batch kích thước (size / 크기)?

Remote calls inside giao dịch (transaction / 트랜잭션)?

Pool sức chứa (capacity / 용량)?

These principles carry into Spring/JPA.

---

# 149. Boolean Parameter Explosion

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
send(
    message,
    true,
    false,
    true);
```

impossible to read.

Use enum/options/command đối tượng (object / 객체)/named methods.

But don't create builder for two clear booleans if names at lời gọi (call / 호출) site already available through phương thức (method / 메서드) split.

---

# 150. thành phần nguyên thủy (primitive / 기본 요소) Obsession

IDs/currency/status/email as raw thành phần nguyên thủy (primitive / 기본 요소)/string everywhere cause argument mixing and repeated kiểm tra hợp lệ (validation / 검증).

Introduce ngữ nghĩa (semantic / 의미적) types where concept matters.

Don't wrap every integer into lớp (class / 클래스) in trivial nội bộ (internal / 내부) vòng lặp (loop / 루프).

---

# 151. God dịch vụ (service / 서비스)

One dịch vụ (service / 서비스) handles thứ tự (order / 순서), payment, inventory, email, reports, filesystem.

Changes unrelated collide.

Split by năng lực (capability / 역량)/use trường hợp (case / 사례) and define ports.

Don't just create `Utils` and move methods; responsibility still needs đơn vị sở hữu (owner / 오너).

---

# 152. Catch-Log-Rethrow Everywhere

Creates duplicate logs.

Either handle, translate/add ngữ cảnh (context / 맥락), or let propagate.

Log once where thao tác (operation / 연산) quyền sở hữu (ownership / 소유권)/ngữ cảnh (context / 맥락) complete.

Preserve cause.

---

# 153. Hidden Blocking

Phương thức (method / 메서드) name:

```java
User getUser()
```

may lời gọi (call / 호출) remote DB/HTTP and khối (block / 블록) seconds.

API/mô-đun (module / 모듈) docs/naming/ngữ cảnh (context / 맥락) should make expensive boundaries visible.

Reactive/event-loop mã (code / 코드) especially sensitive to hidden blocking.

---

# 154. Unbounded Everything

Unbounded hàng đợi (queue / 큐), bộ nhớ đệm (cache / 캐시), luồng thực thi (thread / 스레드) creation, thử lại (retry / 재시도), payload, tập kết quả (result set / 결과 집합) all share one dạng thất bại (failure mode / 실패 모드): overload converts into bộ nhớ (memory / 메모리)/độ trễ (latency / 지연 시간) collapse.

Bound resources.

Sức chứa (capacity / 용량) is part of tính đúng đắn (correctness / 정확성).

---

# 155. sự cố (incident / 인시던트): CPU 100%

Collect JFR/profile before restart if possible.

Find hot stacks.

Check GC CPU, busy loops, regex, serialization, crypto, khóa (lock / 잠금) spin, compilation.

Luồng thực thi (thread / 스레드) count isn't enough.

Fix hottest bằng chứng (evidence / 증거), not suspected khung phần mềm (framework / 프레임워크).

---

# 156. sự cố (incident / 인시던트): Slow, CPU Low

Likely waiting.

Luồng thực thi (thread / 스레드) dumps/traces reveal:

```text
socket read
DB pool
DB lock
future.get
monitor
queue
disk
```

Check downstream độ trễ (latency / 지연 시간)/pool saturation.

Adding CPUs won't fix wait.

---

# 157. sự cố (incident / 인시던트): RSS grows but vùng nhớ động (heap / 힙) looks fine

Possible:

```text
direct memory
thread stacks
metaspace
native library
JIT code cache
GC structures
```

Use NMT, luồng thực thi (thread / 스레드) count, direct buffer metrics, classloader stats.

Do not increase Xmx blindly; it may worsen bộ chứa (container / 컨테이너) OOM.

---

# 158. sự cố (incident / 인시던트): Frequent Full GC

Ask why old/live set high.

Vùng nhớ vùng nhớ động (heap / 힙) too small?

Leak/retention?

Allocation burst?

Humongous objects?

Tường minh (explicit / 명시적) hệ thống (system / 시스템).gc?

Siêu dữ liệu (metadata / 메타데이터) pressure?

GC logs/JFR/vùng nhớ động (heap / 힙) dump provide bằng chứng (evidence / 증거).

Changing collector without understanding live set may only thay đổi (change / 변경) symptom.

---

# 159. sự cố (incident / 인시던트): luồng thực thi (thread / 스레드) Count grows

Could be executor/luồng thực thi (thread / 스레드) leak, one-thread-per-request nền tảng (platform / 플랫폼) mô hình (model / 모델) under overload, scheduler creation, máy khách (client / 클라이언트) thư viện (library / 라이브러리) leak.

With virtual threads, high virtual-thread count may be expected; distinguish nền tảng (platform / 플랫폼) vs virtual and what they're waiting on.

Quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기) rà soát (review / 검토).

---

# 160. Java 21 tích hợp (integration / 통합)

Mẫu (pattern / 패턴) switch and bản ghi (record / 레코드) patterns encourage data-oriented modeling for closed structures.

Sequenced collections simplify thứ tự (order / 순서) APIs.

Virtual threads simplify blocking tính đồng thời (concurrency / 동시성).

Don't force all features into mã (code / 코드). Use when they reduce accidental độ phức tạp (complexity / 복잡도).

---

# 161. Preview Features

Preview means API/ngôn ngữ (language / 언어) may thay đổi (change / 변경) and compile/run requires flags tied to phiên bản (version / 버전).

Structured tính đồng thời (concurrency / 동시성)/Scoped Values had preview/incubator evolution across 21–24 before Scoped Values final in 25.

Môi trường vận hành (production / 운영 환경) baseline should explicitly decide whether preview allowed.

Never describe preview as stable final API.

---

# 162. “Always use giao diện (interface / 인터페이스)” is wrong

Giao diện (interface / 인터페이스) useful for lớp trừu tượng (abstraction / 추상화)/extension/ranh giới (boundary / 경계).

Private helper lớp (class / 클래스) with one hiện thực (implementation / 구현) and no meaningful đặc tả hợp đồng (contract / 계약) may not need.

Too many interfaces create điều hướng (navigation / 내비게이션) noise.

Choose based on substitution/ranh giới (boundary / 경계).

---

# 163. “Never use static” is wrong

Pure utility/static factory/constants are good.

Static mutable toàn cục (global / 전역) dependencies/trạng thái (state / 상태) are risky.

Judge hidden trạng thái (state / 상태)/vòng đời (lifecycle / 생명주기), not từ khóa (keyword / 키워드).

---

# 164. “Composition always better than inheritance” is too absolute

Composition often more flexible.

Inheritance works for true stable is-a hierarchy/khung phần mềm (framework / 프레임워크) template.

Use Liskov substitutability and thay đổi (change / 변경) pressure.

---

# 165. “Exceptions are slow”

Constructing/throwing exceptions with ngăn xếp (stack / 스택) traces can be expensive, so don't use exceptions for hot normal điều khiển (control / 제어) luồng (flow / 흐름).

But don't return magic lỗi (error / 오류) codes everywhere to avoid hypothetical chi phí (cost / 비용).

Correct lỗi (error / 오류) ngữ nghĩa (semantics / 의미론) first; profile.

---

# 166. “Streams are slow”

Streams can have overhead and boxing, but often JIT optimize well enough.

If chuỗi xử lý (pipeline / 파이프라인) clearer and not hot bottleneck, use it.

For tight performance-critical loops, benchmark vòng lặp (loop / 루프) vs stream.

No slogan.

---

# 167. “Virtual threads replace async”

Virtual threads make blocking style quy mô (scale / 규모).

Async/reactive remains useful for streaming/backpressure/composition APIs and certain architectures.

They solve different độ phức tạp (complexity / 복잡도) dimensions.

---

# 168. cấp cao (senior / 시니어) Practice dự án (project / 프로젝트)

Bản dựng (build / 빌드) plain Java production-style cốt lõi (core / 핵심) before Spring.

Lĩnh vực (domain / 도메인): orders/payments/inventory.

Use giá trị (value / 값) objects, sealed kết quả (result / 결과) types, repository/payment ports.

Implement JDBC repository with transactions/truy vấn (query / 쿼리) timeouts and liên kết (connection / 연결) pool thư viện (library / 라이브러리) if allowed.

Implement Java HTTP máy khách (client / 클라이언트) payment adapter with deadline/thử lại (retry / 재시도)/idempotency.

Use virtual threads for blocking yêu cầu (request / 요청) simulation plus semaphore bulkhead.

Implement transactional outbox bảng (table / 테이블) + publisher simulation.

Add JFR profiling and GC logging under tải (load / 로드).

Ghi (write / 쓰기) đơn vị (unit / 단위)/đặc tả hợp đồng (contract / 계약)/tính đồng thời (concurrency / 동시성) tests.

The dự án (project / 프로젝트) should make every tài nguyên (resource / 자원) đơn vị sở hữu (owner / 오너) tường minh (explicit / 명시적).

---

# 169. Spring Readiness Gate

Before Spring, you should understand DI/ports without bộ chứa (container / 컨테이너), proxy concept via động (dynamic / 동적) Proxy, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) with JDBC, annotations as siêu dữ liệu (metadata / 메타데이터), reflection/nạp lớp (class loading / 클래스 로딩), luồng thực thi (thread / 스레드) an toàn (safety / 안전)/JMM and executor vòng đời (lifecycle / 생명주기).

Then Spring annotations become convenient declarations over concepts you already understand.

`@Transactional` maps to giao dịch (transaction / 트랜잭션) interceptor/manager.

`@Async` maps to executor/proxy.

`@Repository` maps persistence adapter.

`@ConfigurationProperties` maps typed cấu hình (configuration / 구성).

Without Java cốt lõi (core / 핵심) mô hình tư duy (mental model / 사고 모델), Spring becomes memorization.

---

# 170. Kết luận Part 3

A cấp cao (senior / 시니어) Java engineer nhìn ứng dụng (application / 애플리케이션) như hệ thống resources và contracts:

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

Môi trường vận hành (production / 운영 환경) view:

```text
load
→ queue/pool
→ latency
→ downstream capacity
→ failures/retries
→ observability
```

Nếu bạn có thể dấu vết (trace / 추적) cả ba lớp cùng lúc, bạn đã vượt khỏi “biết Java cú pháp (syntax / 문법)” và bắt đầu kỹ thuật (engineering / 엔지니어링) bằng Java.

Master Supplement tiếp theo không nhằm thêm nhiều best practices. Nó sẽ bổ sung các vùng low-level/library-author hiện chưa cover đủ như VarHandle bộ nhớ (memory / 메모리) thứ tự (ordering / 순서), LockSupport/AQS, Spliterator/Gatherers/luồng (flow / 흐름), tham chiếu (reference / 참조) queues/Cleaner, NIO Selector, FFM/JNI, Java Agents/Instrumentation, Class-File API, MethodHandle sâu, đối tượng (object / 객체) bố cục (layout / 레이아웃), advanced GC/JFR/JMX và Java 22–26 evolution.

---

# References for version-sensitive topics

Oracle Java SE hỗ trợ (support / 지원) Roadmap:
https://www.oracle.com/java/technologies/java-se-support-roadmap.html

Oracle JDK 25 bản phát hành (release / 릴리스) notes:
https://www.oracle.com/java/technologies/javase/25all-relnotes.html

Oracle JDK 26 bản phát hành (release / 릴리스) notes:
https://www.oracle.com/java/technologies/javase/26all-relnotes.html

OpenJDK JEP chỉ mục (index / 인덱스):
https://openjdk.org/jeps/0

Java ngôn ngữ (language / 언어) Specification:
https://docs.oracle.com/javase/specs/

Java API Documentation:
https://docs.oracle.com/en/java/javase/

> **Bàn giao:** Sau **Java 8 → 11 → 17 → 21 dưới góc nhìn môi trường vận hành (production / 운영 환경) engineer**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

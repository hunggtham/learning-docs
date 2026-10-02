# Java Spring — Part 3: cấp cao (senior / 시니어)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Java Spring — Part 3: cấp cao (senior / 시니어)**. Route đi từ architecture boundary và runtime → failure modes, proxy/transactions và context → performance bottlenecks → production incidents, observability và recovery → version map, để senior reasoning dựa trên evidence.

## Spring khung phần mềm (framework / 프레임워크) 7 / Spring Boot 4 dưới góc nhìn kiến trúc, thời gian chạy (runtime / 런타임), thất bại (failure / 실패) và môi trường vận hành (production / 운영 환경)

> Part 3 không nhằm biến bạn thành người nhớ nhiều annotation hơn. Một cấp cao (senior / 시니어) Spring engineer phải có khả năng thiết kế ranh giới (boundary / 경계), dự đoán dạng thất bại (failure mode / 실패 모드), giải thích proxy/giao dịch (transaction / 트랜잭션)/ngữ cảnh (context / 맥락), tìm bottleneck bằng bằng chứng (evidence / 증거) và xử lý môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) mà không đổ mọi thứ cho “Spring magic”.

---

<!-- VERSION_UPDATE_2026-09-12_START -->

> **Chuyển mạch:** Bản đồ phiên bản đặt Spring 7/Boot 4 trong các câu hỏi kiến trúc, runtime và failure. Phần dependency resolution ở production tiếp tục bằng type contract, lifecycle và exposed object để kiểm tra một ứng dụng thật.

## Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21

Tài liệu dùng **Spring Boot 4.1.1 + Spring khung phần mềm (framework / 프레임워크) 7.0.9** làm baseline stable hiện đại. Spring Boot 4.1.1 yêu cầu tối thiểu Java 17, tương thích đến Java 26 và yêu cầu Spring khung phần mềm (framework / 프레임워크) 7.0.9 trở lên. Với Servlet ngăn xếp (stack / 스택), generation này dùng Servlet 6.1, điển hình với Tomcat 11 hoặc Jetty 12.1. GraalVM bản địa (native / 네이티브) ảnh (image / 이미지) hỗ trợ (support / 지원) của Boot 4.1 yêu cầu GraalVM 25 trở lên.

Khi học để làm việc enterprise, bạn vẫn phải nhận biết **Spring Boot 3.5.16 + Spring khung phần mềm (framework / 프레임워크) 6.2.19+**. Đây là maintenance line quan trọng của generation 3.x, vẫn yêu cầu Java 17+, tương thích đến Java 25 và thuộc Servlet 6.0 generation. Đây cũng là cầu nối (bridge / 브리지) tốt nhất trước khi migrate một hệ thống Boot 3 sang Boot 4.

Generation legacy **Spring Boot 2.7 + Spring khung phần mềm (framework / 프레임워크) 5.3** cần được nhận biết để maintain mã (code / 코드) cũ. Dấu hiệu rõ nhất là Java 8/11-era mã (code / 코드) và không gian tên (namespace / 네임스페이스) `javax.*`. Từ Boot 3 / khung phần mềm (framework / 프레임워크) 6, Spring chuyển sang Java 17+ và `jakarta.*`. Từ Boot 4 / khung phần mềm (framework / 프레임워크) 7, Spring tiếp tục nâng Jakarta EE 11, modularize Boot mạnh hơn và dùng Jackson 3 làm JSON generation ưu tiên.

Ở phía preview, **Spring Boot 4.2.0-M1 + Spring khung phần mềm (framework / 프레임워크) 7.1.0-M1** đã có tài liệu nhưng vẫn là milestone. Tài liệu này chỉ ghi chú (note / 노트) direction, không dùng preview API làm baseline.

```text
Boot 2.7 + Framework 5.3
→ Java 8+ generation
→ javax.*
→ legacy enterprise

Boot 3.5 + Framework 6.2
→ Java 17+
→ jakarta.*
→ Servlet 6.0
→ migration bridge quan trọng

Boot 4.1 + Framework 7.0
→ Java 17–26
→ Jakarta EE 11 / Servlet 6.1
→ Jackson 3 preferred
→ modular Boot
→ baseline hiện đại

Boot 4.2 M1 + Framework 7.1 M1
→ preview
→ theo dõi direction, không dùng làm production baseline
```

Phiên bản (version / 버전) chỉ được nhắc ở nơi nó thật sự thay đổi gói (package / 패키지), phụ thuộc (dependency / 의존성), API, hành vi thời gian chạy (runtime behavior / 런타임 동작) hoặc di chuyển (migration / 마이그레이션); không biến tài liệu thành changelog.
<!-- VERSION_UPDATE_2026-09-12_END -->

---
# 1. cấp cao (senior / 시니어) Spring là gì?

Ở Intermediate, bạn đã biết bộ chứa (container / 컨테이너) tạo bean qua definitions và post-processors, AOP dùng proxy, MVC có dispatch chuỗi xử lý (pipeline / 파이프라인), giao dịch (transaction / 트랜잭션) có propagation và JPA có persistence ngữ cảnh (context / 맥락).

Ở cấp cao (senior / 시니어), câu hỏi thay đổi. Khi phương thức (method / 메서드) có `@Transactional`, bạn phải đánh giá giao dịch (transaction / 트랜잭션) có giữ liên kết (connection / 연결) quá lâu không, có remote lời gọi (call / 호출) bên trong không, có `REQUIRES_NEW` khiến pool cạn không. Khi bật virtual threads, bạn phải hỏi DB liên kết (connection / 연결) pool, downstream tính đồng thời (concurrency / 동시성) và pinning chứ không chỉ nhìn luồng thực thi (thread / 스레드) count. Khi thêm bộ nhớ đệm (cache / 캐시), bạn phải hỏi stale tolerance và stampede. Khi publish sự kiện (event / 이벤트), bạn phải hỏi tiến trình (process / 프로세스) crash giữa lần ghi nhận (commit / 커밋) và publish. Khi độ trễ (latency / 지연 시간) p99 tăng, bạn phải biết lấy dấu vết (trace / 추적), JFR, DB metrics và luồng thực thi (thread / 스레드) dump để xây hypothesis.

Khung phần mềm (framework / 프레임워크) skill ở mức (level / 수준) cấp cao (senior / 시니어) là **lập luận (reasoning / 추론) about boundaries and thời gian chạy (runtime / 런타임) consequences**.

---

# 2. Spring không thay kiến trúc của bạn

Spring có thể inject phụ thuộc (dependency / 의존성) nhưng không quyết định phụ thuộc (dependency / 의존성) direction có đúng không. Nó có thể mở giao dịch (transaction / 트랜잭션) nhưng không biết nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) nào phải atomic. Nó có thể tạo REST controller nhưng không biết API công khai (public API / 공개 API) nên phiên bản (version / 버전) thế nào. Nó có thể bộ nhớ đệm (cache / 캐시) phương thức (method / 메서드) nhưng không biết dữ liệu stale 30 giây có chấp nhận được không.

Vì vậy hãy phân biệt:

```text
Framework capability
≠
Architecture decision
```

Một hệ thống đầy `@Service`, `@Repository`, `@Transactional` vẫn có thể có coupling tệ, giao dịch (transaction / 트랜잭션) sai và ranh giới (boundary / 경계) mơ hồ.

**lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구) — khung phần mềm (framework / 프레임워크) at the edges.** lĩnh vực (domain / 도메인)/giá trị (value / 값) objects và phần lớn nghiệp vụ (business / 비즈니스) decisions nên có thể hiểu bằng Java bình thường. Spring annotations tập trung ở composition/hạ tầng (infrastructure / 인프라) boundaries khi có thể.

---

# 3. bộ chứa (container / 컨테이너) startup dưới góc cấp cao (senior / 시니어)

Startup không phải “scan rồi new beans”. Một ứng dụng (application / 애플리케이션) lớn có nhiều stages: môi trường (environment / 환경)/cấu hình (config / 설정) dữ liệu (data / 데이터) được chuẩn bị, cấu hình (configuration / 구성) classes được parse, definitions được register, factory post-processors sửa siêu dữ liệu (metadata / 메타데이터), bean post-processors được tạo, eager singletons được instantiate, dependencies resolved, initialization callbacks chạy, auto-proxy creators có thể wrap mục tiêu (target / 대상), rồi vòng đời (lifecycle / 생명주기) hạ tầng (infrastructure / 인프라) mới start.

Khi startup chậm, bạn phải phân loại chi phí (cost / 비용):

```text
classpath/config scanning
bean creation
JPA metamodel
database connection
Flyway migration
remote discovery/JWK
custom @PostConstruct
AOT/native constraints
```

Đừng bật toàn cục (global / 전역) lazy initialization như phản xạ. Nó giảm startup bằng cách chuyển lỗi sang first yêu cầu (request / 요청).

---

<!-- SPRING_BATCH1_IOC_SENIOR -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 3: cấp cao (senior / 시니어)**, **Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21** xác định đầu vào; **Phụ thuộc (dependency / 의존성) resolution ở môi trường vận hành (production / 운영 환경): kiểu (type / 타입) đặc tả hợp đồng (contract / 계약), vòng đời (lifecycle / 생명주기) và exposed đối tượng (object / 객체) phải được xem cùng nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Vòng đời yêu cầu (request lifecycle / 요청 생명주기) dưới góc môi trường vận hành (production / 운영 환경): queueing, ngữ cảnh (context / 맥락) và thất bại (failure / 실패) quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) resolution ở môi trường vận hành (production / 운영 환경): kiểu (type / 타입) đặc tả hợp đồng (contract / 계약), vòng đời (lifecycle / 생명주기) và exposed đối tượng (object / 객체) phải được xem cùng nhau

Ở môi trường vận hành (production / 운영 환경), “bean tồn tại” chưa đủ. Bạn cần phân biệt **definition kiểu (type / 타입)**, **mục tiêu (target / 대상) kiểu (type / 타입)** và **exposed kiểu (type / 타입)**. Một `@Bean` factory phương thức (method / 메서드) có thể khai báo giao diện (interface / 인터페이스) return kiểu (type / 타입) trong khi đối tượng (object / 객체) thật là hiện thực (implementation / 구현) cụ thể; sau đó auto-proxying có thể expose JDK proxy chỉ implement interfaces hoặc lớp (class / 클래스) proxy subclass mục tiêu (target / 대상). mã (code / 코드) dùng `getBean(SomeConcreteClass.class)` có thể vì vậy phụ thuộc proxy chiến lược (strategy / 전략) một cách vô tình, trong khi constructor injection theo stable giao diện (interface / 인터페이스) ít nhạy hơn.

Phụ thuộc (dependency / 의존성) resolution cũng có vòng đời (lifecycle / 생명주기) chi phí (cost / 비용). Injecting một heavy singleton trực tiếp vào hạ tầng (infrastructure / 인프라) bean có thể kéo cả ứng dụng (application / 애플리케이션) đồ thị (graph / 그래프) vào startup sớm. Injecting `ObjectProvider<T>` hoặc thiết kế lại ranh giới (boundary / 경계) đôi khi không phải “lazy trick” mà là cách giữ phase separation đúng. Tuy nhiên provider bị dùng khắp nghiệp vụ (business / 비즈니스) mã (code / 코드) lại làm dependencies khó nhìn, nên deferred lookup chỉ nên xuất hiện khi vòng đời (lifecycle / 생명주기)/optionality thực sự cần.

Khi custom khung phần mềm (framework / 프레임워크) mã (code / 코드) can thiệp vào bean creation, hãy giữ một bất biến (invariant / 불변식): siêu dữ liệu (metadata / 메타데이터) processors không nên vô tình instantiate ứng dụng (application / 애플리케이션) beans, instance processors không nên phụ thuộc sâu vào nghiệp vụ (business / 비즈니스) đồ thị (graph / 그래프), và caller không nên phụ thuộc hiện thực (implementation / 구현) detail của proxy. Ba nguyên tắc này giảm phần lớn các lỗi startup/proxy khó đoán.
<!-- SPRING_BATCH1_IOC_SENIOR_END -->

---

# 4. Early Bean Creation và “not eligible for all BeanPostProcessors”

Một advanced startup bug xảy ra khi hạ tầng (infrastructure / 인프라) bean trong lúc tạo post-processor lại yêu cầu ứng dụng (application / 애플리케이션) bean quá sớm. Bean đó được instantiate trước khi toàn bộ post-processors được register. Kết quả nó có thể không nhận proxy/advice mà bạn kỳ vọng.

Nếu log nói bean “not eligible for getting processed by all BeanPostProcessors” và giao dịch (transaction / 트랜잭션)/AOP không chạy, hãy dấu vết (trace / 추적) **ai kéo bean vào creation sớm**.

Đây là khung phần mềm (framework / 프레임워크) vòng đời (lifecycle / 생명주기) bài toán (problem / 문제), không sửa bằng thêm `@Transactional`.

---

# 5. BeanPostProcessor thứ tự (ordering / 순서) và hạ tầng (infrastructure / 인프라) coupling

Spring hạ tầng (infrastructure / 인프라) dùng thứ tự (ordering / 순서) contracts như `PriorityOrdered`, `Ordered` và `@Order`. Khi bạn tự viết nhiều custom post-processors phụ thuộc thứ tự (order / 순서), bạn đang xây mini-framework.

Ứng dụng (application / 애플리케이션) mã (code / 코드) bình thường không nên dùng post-processor để implement nghiệp vụ (business / 비즈니스) tính năng (feature / 기능). Vì post-processor chạy ở vòng đời (lifecycle / 생명주기) tầng (layer / 계층), lỗi dễ ảnh hưởng toàn ngữ cảnh (context / 맥락) và khó gỡ lỗi (debug / 디버그).

Nếu một yêu cầu (requirement / 요구사항) có thể giải bằng tường minh (explicit / 명시적) composition/bean cấu hình (configuration / 구성), ưu tiên nó trước metaprogramming.

---

# 6. Proxy chuỗi (chain / 사슬) là thời gian chạy (runtime / 런타임) kiến trúc (architecture / 아키텍처)

Một bean có thể được bao bởi nhiều interceptors.

Concept:

```text
caller
→ security
→ observation
→ retry
→ transaction
→ cache
→ target
```

Thứ tự này không chỉ hiệu năng (performance / 성능); nó thay ngữ nghĩa (semantics / 의미론).

Ví dụ thử lại (retry / 재시도) **ngoài** giao dịch (transaction / 트랜잭션) có thể tạo giao dịch (transaction / 트랜잭션) mới cho từng attempt. thử lại (retry / 재시도) **trong** giao dịch (transaction / 트랜잭션) có thể thử lại (retry / 재시도) trong giao dịch (transaction / 트랜잭션) đã rollback-only, vô nghĩa hoặc sai.

Bộ nhớ đệm (cache / 캐시) ngoài bảo mật (security / 보안) có thể bộ nhớ đệm (cache / 캐시) phản hồi (response / 응답) không phân biệt permission nếu key sai.

Khi một phương thức (method / 메서드) có nhiều cross-cutting annotations, hãy vẽ interceptor ngăn xếp (stack / 스택).

---

# 7. Advisor, Pointcut, MethodInterceptor

Ở Spring AOP, một Advisor gắn advice với pointcut. phương thức (method / 메서드) interceptor có thể gọi `proceed()` để chuyển điều khiển (control / 제어) tới interceptor tiếp theo hoặc mục tiêu (target / 대상).

Pseudo:

```java
Object invoke(MethodInvocation invocation)
        throws Throwable {

    before();

    try {
        return invocation.proceed();
    } catch (Throwable t) {
        onError(t);
        throw t;
    } finally {
        after();
    }
}
```

Transactions, observations và custom aspects có thể conceptually nằm trong chuỗi (chain / 사슬) kiểu này.

Đây là Proxy + chuỗi (chain / 사슬) of Responsibility/Interceptor.

---

# 8. JDK Proxy và CGLIB dưới góc API thiết kế (design / 설계)

JDK proxy expose interfaces. Class-based proxy subclass mục tiêu (target / 대상).

Nếu nghiệp vụ (business / 비즈니스) API đã có giao diện (interface / 인터페이스) ổn định, JDK proxy thường tự nhiên. Nếu codebase inject concrete types và cần advise concrete methods, lớp (class / 클래스) proxy có thể cần.

Lớp (class / 클래스) proxy có limitation với final/private methods vì subclass không override được.

Spring khung phần mềm (framework / 프레임워크) 7 tiếp tục proxy-based Spring AOP và có thêm điều khiển (control / 제어) finer-grained như `@Proxyable` cho per-bean proxy choice trong hiện tại (current / 현재) generation.

Cấp cao (senior / 시니어) không nên ép toàn dự án (project / 프로젝트) sang một proxy kiểu (type / 타입) vì benchmark blog. Hãy thiết kế công khai (public / 공개) lớp trừu tượng (abstraction / 추상화) trước.

---

# 9. Self-invocation là dấu hiệu ranh giới (boundary / 경계), không chỉ technical caveat

Nếu bạn có:

```java
@Service
class AccountingService {

    @Transactional
    public void process() {
        saveAudit();
    }

    @Transactional(
        propagation = REQUIRES_NEW
    )
    public void saveAudit() {
    }
}
```

và `process()` gọi `this.saveAudit()`, advice thứ hai bị bypass.

Technical fix có thể dùng self proxy, nhưng kiến trúc (architecture / 아키텍처) fix thường tốt hơn: `AuditService` là collaborator có giao dịch (transaction / 트랜잭션) chính sách (policy / 정책) riêng.

Khi hai methods cần proxy policies khác nhau, đó thường là dấu hiệu chúng đại diện hai thực thi (execution / 실행) boundaries khác nhau.

---

<!-- SPRING_BATCH2_REQUEST_SENIOR -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Java Spring — Part 3: cấp cao (senior / 시니어)**, **Phụ thuộc (dependency / 의존성) resolution ở môi trường vận hành (production / 운영 환경): kiểu (type / 타입) đặc tả hợp đồng (contract / 계약), vòng đời (lifecycle / 생명주기) và exposed đối tượng (object / 객체) phải được xem cùng nhau** xác định đầu vào; **Vòng đời yêu cầu (request lifecycle / 요청 생명주기) dưới góc môi trường vận hành (production / 운영 환경): queueing, ngữ cảnh (context / 맥락) và thất bại (failure / 실패) quyền sở hữu (ownership / 소유권)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Suspend, resume, hết thời gian chờ (timeout / 타임아웃) và rollback-only là tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론) chứ không phải annotation trivia** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vòng đời yêu cầu (request lifecycle / 요청 생명주기) dưới góc môi trường vận hành (production / 운영 환경): queueing, ngữ cảnh (context / 맥락) và thất bại (failure / 실패) quyền sở hữu (ownership / 소유권)

Cấp cao (senior / 시니어) debugging cần nối HTTP vòng đời (lifecycle / 생명주기) với sức chứa (capacity / 용량). Một yêu cầu (request / 요청) có thể chờ ở connector accept hàng đợi (queue / 큐), máy chủ (server / 서버) executor, bảo mật (security / 보안) filter, tỷ lệ (rate / 비율) limiter, DB liên kết (connection / 연결) pool, remote HTTP máy khách (client / 클라이언트) hoặc khóa (lock / 잠금). Tất cả đều biểu hiện cuối cùng là “endpoint chậm”, nhưng cách xử lý hoàn toàn khác. Metrics và traces phải cho phép tách **máy chủ (server / 서버) hàng đợi (queue / 큐) thời gian (time / 시간), ứng dụng (application / 애플리케이션) thực thi (execution / 실행) thời gian (time / 시간) và downstream wait thời gian (time / 시간)** thay vì chỉ có một timer tổng.

Filter thứ tự (order / 순서) là bảo mật (security / 보안)/tính đúng đắn (correctness / 정확성) concern. CORS preflight phải được xử lý đúng trước authentication các giả định (assumptions / 가정들); correlation/tracing ngữ cảnh (context / 맥락) phải có sớm để bảo mật (security / 보안)/controller logs cùng một yêu cầu (request / 요청) ID; body-caching/logging filter có thể phá streaming hoặc tăng bộ nhớ (memory / 메모리) nếu wrap toàn payload. Interceptor phù hợp cho handler-aware chính sách (policy / 정책), nhưng không nhìn thấy yêu cầu (request / 요청) bị bảo mật (security / 보안) chuỗi (chain / 사슬) reject trước controller.

Một quy tắc (rule / 규칙) vận hành quan trọng là tầng (layer / 계층) nào tạo side tác động (effect / 효과) thì tầng (layer / 계층) đó phải chịu vòng đời (lifecycle / 생명주기) của side tác động (effect / 효과). Filter mở MDC/ngữ cảnh (context / 맥락) phải đóng trong `finally`. Controller không nên manually close transaction-managed EntityManager. dịch vụ (service / 서비스) không nên giữ servlet yêu cầu (request / 요청) để dùng trong async background tác vụ (task / 작업) sau khi yêu cầu (request / 요청) đã kết thúc. Tách quyền sở hữu (ownership / 소유권) đúng làm shutdown, hết thời gian chờ (timeout / 타임아웃) và lỗi (error / 오류) handling dễ lập luận (reasoning / 추론) hơn.
<!-- SPRING_BATCH2_REQUEST_SENIOR_END -->

---

# 10. giao dịch (transaction / 트랜잭션) Internals: từ annotation tới tài nguyên (resource / 자원)

Declarative giao dịch (transaction / 트랜잭션) luồng (flow / 흐름):

```text
caller
→ proxy
→ TransactionInterceptor
→ resolve transaction attributes
→ choose manager
→ get/create TransactionStatus
→ bind resource
→ target
→ commit/rollback
→ unbind/release
```

Với JDBC, vật lý (physical / 물리적) liên kết (connection / 연결) thường được lấy từ DataSource và gắn với thực thi (execution / 실행) ngữ cảnh (context / 맥락) để repositories trong cùng giao dịch (transaction / 트랜잭션) dùng cùng transactional liên kết (connection / 연결).

Hiểu điều này giải thích vì sao giao dịch (transaction / 트랜잭션) historically thread-bound và vì sao async thực thi (execution / 실행) không tự động “mang giao dịch (transaction / 트랜잭션) theo”.

---

<!-- SPRING_BATCH3_TX_SENIOR -->

> **Chuyển mạch:** Trong **Java Spring — Part 3: cấp cao (senior / 시니어)**, cơ chế trong **Vòng đời yêu cầu (request lifecycle / 요청 생명주기) dưới góc môi trường vận hành (production / 운영 환경): queueing, ngữ cảnh (context / 맥락) và thất bại (failure / 실패) quyền sở hữu (ownership / 소유권)** cần được kiểm chứng bằng dấu vết cụ thể; **Suspend, resume, hết thời gian chờ (timeout / 타임아웃) và rollback-only là tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론) chứ không phải annotation trivia** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **Từ Spring dữ liệu (data / 데이터) repository tới EntityManager: persistence thời gian chạy (runtime / 런타임) thật sự nằm ở đâu?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suspend, resume, hết thời gian chờ (timeout / 타임아웃) và rollback-only là tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론) chứ không phải annotation trivia

Khi propagation yêu cầu giao dịch (transaction / 트랜잭션) mới, manager có thể phải suspend resources/ngữ cảnh (context / 맥락) của giao dịch (transaction / 트랜잭션) hiện tại, bind resources mới, chạy inner phạm vi (scope / 범위) rồi resume outer resources. `REQUIRES_NEW` vì vậy vừa tạo isolation ranh giới (boundary / 경계) vừa tăng concurrent tài nguyên (resource / 자원) demand. Với cục bộ (local / 로컬) JDBC/JPA, “suspend” không biến outer giao dịch (transaction / 트랜잭션) thành free; liên kết (connection / 연결)/locks của outer có thể vẫn tồn tại trong lúc inner giao dịch (transaction / 트랜잭션) cần thêm sức chứa (capacity / 용량).

Hết thời gian chờ (timeout / 타임아웃) cũng phải được nhìn từ tài nguyên (resource / 자원) tầng (layer / 계층). Spring giao dịch (transaction / 트랜잭션) hết thời gian chờ (timeout / 타임아웃) có thể được truyền tới tài nguyên (resource / 자원) operations tùy manager/driver, nhưng nó không thay thế HTTP deadline, cơ sở dữ liệu (database / 데이터베이스) statement hết thời gian chờ (timeout / 타임아웃) hay khóa (lock / 잠금) hết thời gian chờ (timeout / 타임아웃) ở mọi tầng (layer / 계층). Một use trường hợp (case / 사례) có 2 giây ngân sách (budget / 예산) nhưng remote máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) 30 giây và DB khóa (lock / 잠금) wait 60 giây vẫn có thể phá độ trễ (latency / 지연 시간) SLO dù `@Transactional(timeout=5)` tồn tại.

Rollback-only là trạng thái của logical/vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션), không phải exception decoration. Một inner participant có thể đánh dấu giao dịch (transaction / 트랜잭션) không còn committable; outer phương thức (method / 메서드) catch exception chỉ thay Java điều khiển (control / 제어) luồng (flow / 흐름), không xóa trạng thái tài nguyên (resource / 자원). Đây là lý do cấp cao (senior / 시니어) rà soát mã (code review / 코드 리뷰) phải xem exception taxonomy cùng propagation đồ thị (graph / 그래프).
<!-- SPRING_BATCH3_TX_SENIOR_END -->

---

# 11. vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션) và logical scopes

Outer REQUIRED và inner REQUIRED có hai logical annotation scopes nhưng thường chia sẻ một vật lý (physical / 물리적) DB giao dịch (transaction / 트랜잭션).

Nếu inner làm giao dịch (transaction / 트랜잭션) rollback-only, outer catch exception không thể biến vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션) thành committable. lần ghi nhận (commit / 커밋) outer sẽ thất bại (fail / 실패)/quay lui (rollback / 롤백).

`UnexpectedRollbackException` tồn tại để ứng dụng (application / 애플리케이션) không nhận false success.

Cấp cao (senior / 시니어) phải xem logical lời gọi (call / 호출) đồ thị (graph / 그래프) và vật lý (physical / 물리적) tài nguyên (resource / 자원) cùng lúc.

---

# 12. `REQUIRES_NEW` và liên kết (connection / 연결) starvation

Giả sử liên kết (connection / 연결) pool 20. Có 20 concurrent requests, mỗi outer giao dịch (transaction / 트랜잭션) giữ một liên kết (connection / 연결). Mỗi yêu cầu (request / 요청) gọi inner `REQUIRES_NEW`, cần liên kết (connection / 연결) khác.

Tất cả 20 inner calls chờ liên kết (connection / 연결), nhưng 20 connections đang bị chính outer transactions của chúng giữ.

Đây có thể tạo starvation/deadlock-like điều kiện (condition / 조건).

Do đó `REQUIRES_NEW` không phải “save independent cho chắc”. Nó có tài nguyên (resource / 자원) topology.

---

# 13. TransactionSynchronization và after-commit hành vi (behavior / 동작)

Spring giao dịch (transaction / 트랜잭션) hạ tầng (infrastructure / 인프라) hỗ trợ callbacks quanh lần ghi nhận (commit / 커밋)/completion. `@TransactionalEventListener` tận dụng giao dịch (transaction / 트랜잭션) phase ngữ nghĩa (semantics / 의미론) ở high mức (level / 수준).

Nhưng after-commit callback vẫn trong tiến trình (process / 프로세스). Nếu DB lần ghi nhận (commit / 커밋) thành công và tiến trình (process / 프로세스) chết trước khi durable message được publish, callback không cứu được.

Đây là ranh giới (boundary / 경계) giữa **cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) synchronization** và **phân tán (distributed / 분산) độ tin cậy (reliability / 신뢰성)**.

---

# 14. giao dịch (transaction / 트랜잭션) với nhiều DataSources

Nếu ứng dụng (application / 애플리케이션) có `primaryDataSource` và `auditDataSource`, mỗi cái có cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) manager riêng.

```java
@Transactional("primaryTxManager")
```

không làm kiểm tra (audit / 감사) DB phép nối (join / 조인) atomic giao dịch (transaction / 트랜잭션) một cách thần kỳ.

Hai cục bộ (local / 로컬) transactions:

```text
DB A commit
DB B fail
```

vẫn có partial kết quả (result / 결과).

Muốn atomic phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) cần JTA/XA hoặc thường trong hiện đại (modern / 현대적) services dùng eventual consistency/nghiệp vụ (business / 비즈니스) patterns như outbox/saga tùy yêu cầu (requirement / 요구사항).

---

# 15. Keep DB Transactions Short

Một giao dịch (transaction / 트랜잭션) nên giữ locks/connections chỉ cho phần cần atomic.

Bad:

```java
@Transactional
public void placeOrder() {
    saveOrder();
    paymentHttpClient.charge();
    shippingClient.reserve();
    sendEmail();
}
```

Nếu payment mất 5 giây, liên kết (connection / 연결) bị giữ 5 giây. Nếu shipping thất bại (fail / 실패) sau payment success, DB quay lui (rollback / 롤백) không undo payment bên ngoài (external / 외부).

Cấp cao (senior / 시니어) thiết kế cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) + durable chuyển tiếp trạng thái (state transition / 상태 전이)/outbox, rồi bên ngoài (external / 외부) effects có thử lại (retry / 재시도)/idempotency.

---

# 16. Isolation không thể hiểu chỉ bằng enum Spring

`Isolation.READ_COMMITTED` là intent ánh xạ (mapping / 매핑). Actual phenomena phụ thuộc cơ sở dữ liệu (database / 데이터베이스) MVCC/locking hiện thực (implementation / 구현).

Bạn phải biết cơ sở dữ liệu (database / 데이터베이스) đang dùng. PostgreSQL READ COMMITTED, MySQL InnoDB ngữ nghĩa (semantics / 의미론) và Oracle có khác biệt.

Spring chỉ truyền isolation chính sách (policy / 정책) xuống giao dịch (transaction / 트랜잭션) tài nguyên (resource / 자원); nó không định nghĩa cơ sở dữ liệu (database / 데이터베이스) physics.

---

# 17. cơ sở dữ liệu (database / 데이터베이스) deadlock và Spring

Deadlock xảy ra khi transactions giữ khóa (lock / 잠금) theo cycle.

Ví dụ giao dịch (transaction / 트랜잭션) A cập nhật (update / 업데이트) thứ tự (order / 순서) rồi Payment; giao dịch (transaction / 트랜잭션) B cập nhật (update / 업데이트) Payment rồi thứ tự (order / 순서).

DB phát hiện cycle và abort một giao dịch (transaction / 트랜잭션).

Ứng dụng (application / 애플리케이션) mitigation gồm consistent khóa (lock / 잠금) thứ tự (ordering / 순서), giao dịch (transaction / 트랜잭션) ngắn, chỉ mục (index / 인덱스) đúng để tránh khóa (lock / 잠금) nhiều rows, thử lại (retry / 재시도) carefully với idempotency.

Đừng chỉ tăng hết thời gian chờ (timeout / 타임아웃).

---

<!-- SPRING_BATCH3_JPA_SENIOR -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 3: cấp cao (senior / 시니어)**, **Suspend, resume, hết thời gian chờ (timeout / 타임아웃) và rollback-only là tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론) chứ không phải annotation trivia** nêu điều cần giải thích; **Từ Spring dữ liệu (data / 데이터) repository tới EntityManager: persistence thời gian chạy (runtime / 런타임) thật sự nằm ở đâu?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bảo mật (security / 보안) môi trường vận hành (production / 운영 환경) mô hình (model / 모델): credential vận chuyển (transport / 전송), key vòng đời (lifecycle / 생명주기) và object-level authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ Spring dữ liệu (data / 데이터) repository tới EntityManager: persistence thời gian chạy (runtime / 런타임) thật sự nằm ở đâu?

Spring dữ liệu (data / 데이터) repository giao diện (interface / 인터페이스) thường được triển khai bằng proxy, nhưng proxy không phải cơ sở dữ liệu (database / 데이터베이스) engine. Nó dịch repository invocation thành hiện thực (implementation / 구현)/truy vấn (query / 쿼리) thực thi (execution / 실행) dùng JPA `EntityManager`. `EntityManager` mà ứng dụng (application / 애플리케이션) inject thường là một dùng chung (shared / 공유) proxy: mỗi lời gọi (call / 호출) được tuyến (route / 경로) tới transaction-bound persistence ngữ cảnh (context / 맥락) phù hợp. Vì vậy repository có thể trông stateless trong Java trong khi persistence ngữ cảnh (context / 맥락) giữ managed entities và pending changes theo giao dịch (transaction / 트랜잭션).

`save(entity)` cũng không đồng nghĩa “chạy INSERT ngay”. `SimpleJpaRepository` quyết định thực thể (entity / 엔터티) có mới hay không; thực thể (entity / 엔터티) mới thường đi `persist`, thực thể (entity / 엔터티) được xem là existing thường đi `merge`. `merge` trả về managed bản sao (copy / 복사) và đối tượng (object / 객체) truyền vào không nhất thiết trở thành chính instance managed. SQL INSERT/cập nhật (update / 업데이트) có thể chỉ xuất hiện ở flush/lần ghi nhận (commit / 커밋), do JPA write-behind. Vì vậy debugger nhìn thấy `save()` return chưa có nghĩa cơ sở dữ liệu (database / 데이터베이스) đã lần ghi nhận (commit / 커밋).

Flush là synchronization giữa persistence ngữ cảnh (context / 맥락) và cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션), còn lần ghi nhận (commit / 커밋) là durable giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계). truy vấn (query / 쿼리) có thể trigger flush tùy flush chế độ (mode / 모드) để bảo đảm truy vấn (query / 쿼리) thấy changes. `saveAndFlush` ép synchronization sớm hơn nhưng vẫn không biến cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) thành committed giao dịch (transaction / 트랜잭션). Dùng nó để “chắc chắn đã save” thường che việc chưa hiểu flush/lần ghi nhận (commit / 커밋) ngữ nghĩa (semantics / 의미론).

Open Session/EntityManager in View giữ persistence ngữ cảnh (context / 맥락) qua web yêu cầu (request / 요청) để lazy quan hệ (relation / 관계) còn có thể tải (load / 로드) trong serialization/view. Nó giảm `LazyInitializationException` nhưng làm SQL có thể phát sinh rất muộn, khó thấy giao dịch (transaction / 트랜잭션)/truy vấn (query / 쿼리) quyền sở hữu (ownership / 소유권) và dễ tạo N+1. cấp cao (senior / 시니어) thiết kế (design / 설계) nên chủ động fetch/projection ở ứng dụng (application / 애플리케이션) ranh giới (boundary / 경계) thay vì dựa lazy loading trong serializer.
<!-- SPRING_BATCH3_JPA_SENIOR_END -->

---

# 18. JPA Persistence ngữ cảnh (context / 맥락) như đơn vị (unit / 단위) of công việc (work / 작업)

Persistence ngữ cảnh (context / 맥락) giữ managed entities, định danh (identity / 식별자) map và pending changes.

Cấp cao (senior / 시니어) phải quan tâm **kích thước** ngữ cảnh (context / 맥락).

Nếu tải (load / 로드) 100.000 entities rồi cập nhật (update / 업데이트) trong một giao dịch (transaction / 트랜잭션), ngữ cảnh (context / 맥락) giữ tham chiếu (reference / 참조) và dirty-check siêu dữ liệu (metadata / 메타데이터) cho toàn bộ. bộ nhớ (memory / 메모리) tăng, flush chậm.

Batch processing thường cần chunk:

```text
load/persist batch
→ flush
→ clear
→ repeat
```

hoặc dùng bulk SQL nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) cho phép.

---

# 19. Dirty Checking chi phí (cost / 비용) và side effects

Dirty checking tiện vì bạn chỉ mutate managed thực thể (entity / 엔터티). Nhưng sự tiện này có hidden SQL.

Mapper hoặc helper vô tình lời gọi (call / 호출) setter trên managed thực thể (entity / 엔터티) có thể tạo cập nhật (update / 업데이트) khi giao dịch (transaction / 트랜잭션) flush.

Do đó thực thể (entity / 엔터티) mutation API nên có ngữ nghĩa (semantic / 의미적) rõ:

```java
order.cancel(reason);
```

thay vì công khai (public / 공개) setters mọi trường dữ liệu (field / 필드).

---

# 20. Flush Timing và truy vấn (query / 쿼리) tương tác (interaction / 상호작용)

JPA provider có thể flush trước truy vấn (query / 쿼리) nếu cần đảm bảo truy vấn (query / 쿼리) thấy pending changes.

Bạn có thể thấy SQL cập nhật (update / 업데이트) xảy ra giữa phương thức (method / 메서드) trước lần ghi nhận (commit / 커밋) và tưởng khung phần mềm (framework / 프레임워크) “lần ghi nhận (commit / 커밋) sớm”. Thực ra đó có thể là flush.

Gỡ lỗi (debug / 디버그) JPA phải phân biệt:

```text
SQL execution
transaction commit
```

---

# 21. N+1 ở môi trường vận hành (production / 운영 환경)

N+1 không chỉ làm “nhiều truy vấn (query / 쿼리)”. Nó tăng DB round trips, liên kết (connection / 연결) occupation, CPU parsing/thực thi (execution / 실행) và p99 độ trễ (latency / 지연 시간).

Một endpoint cục bộ (local / 로컬) kiểm thử (test / 테스트) với 5 orders có vẻ nhanh. môi trường vận hành (production / 운영 환경) người dùng (user / 사용자) có 500 orders sẽ tạo 501 queries.

Bạn phải instrument truy vấn (query / 쿼리) counts/tracing/SQL metrics thay vì chờ người dùng (user / 사용자) complain.

---

# 22. Fetch phép nối (join / 조인) và Cartesian Explosion

Thứ tự (order / 순서) có 10 items và 5 payments. phép nối (join / 조인) fetch cả hai collections có thể tạo 50 kết quả (result / 결과) rows cho một thứ tự (order / 순서).

ORM de-duplicate đối tượng (object / 객체) đồ thị (graph / 그래프) nhưng DB/mạng (network / 네트워크) đã xử lý 50 rows.

Nếu thêm third collection, multiplication tăng mạnh.

Cấp cao (senior / 시니어) không “fetch phép nối (join / 조인) everything”. Có thể dùng multiple queries, projections hoặc batch fetching.

---

# 23. Pagination và Fetch Collection

Cơ sở dữ liệu (database / 데이터베이스) pagination áp lên rows, nhưng collection fetch phép nối (join / 조인) nhân rows. ORM có thể không thể paginate thực thể (entity / 엔터티) roots đúng bằng SQL offset/limit hoặc phải xử lý bộ nhớ (memory / 메모리).

Dùng chung (common / 공통) chiến lược (strategy / 전략):

```text
page root IDs
→ fetch details by IDs
```

hoặc projection/keyset pagination.

---

# 24. DTO Projection và CQRS-lite

Một thứ tự (order / 순서) detail command luồng (flow / 흐름) cần rich thực thể (entity / 엔터티)/lĩnh vực (domain / 도메인) mô hình (model / 모델). Một dashboard chỉ cần thứ tự (order / 순서) ID, customer name, total, status.

Không cần hydrate toàn đồ thị (graph / 그래프) rồi serialize.

Projection truy vấn (query / 쿼리):

```java
record OrderSummary(
    Long id,
    String customer,
    BigDecimal total,
    OrderStatus status) {
}
```

Read mô hình (model / 모델) tối ưu riêng là pragmatic CQRS-lite, không cần dựng sự kiện (event / 이벤트) sourcing.

---

# 25. JPA Batch Inserts

Batching phụ thuộc Hibernate/JDBC settings, ID generation và flush mẫu (pattern / 패턴).

`IDENTITY` có thể hạn chế insert batching vì ID cần DB round trip sớm tùy provider.

Nếu hiệu năng (performance / 성능) matters, đo SQL/batch hành vi (behavior / 동작) trên actual DB.

Không bản sao (copy / 복사) `hibernate.jdbc.batch_size=1000` mà chưa measure giao dịch (transaction / 트랜잭션)/bộ nhớ (memory / 메모리)/DB packet effects.

---

# 26. Bulk cập nhật (update / 업데이트) và stale Persistence ngữ cảnh (context / 맥락)

JPQL bulk cập nhật (update / 업데이트):

```jpql
update User u
set u.active = false
where u.lastLogin < :cutoff
```

bypass normal thực thể (entity / 엔터티) dirty checking.

Nếu ngữ cảnh (context / 맥락) đã có `User` managed, đối tượng (object / 객체) bộ nhớ (memory / 메모리) có thể vẫn `active=true` dù DB changed.

Sau bulk thao tác (operation / 연산) cần clear/refresh chiến lược (strategy / 전략) phù hợp.

---

# 27. Optimistic Locking là nghiệp vụ (business / 비즈니스) xung đột (conflict / 충돌)

`@Version` thất bại (failure / 실패) không nhất thiết 500.

Hai users cùng sửa same tài nguyên (resource / 자원) là expected concurrent xung đột (conflict / 충돌).

API có thể map thành `409 Conflict`, prompt máy khách (client / 클라이언트) reload hoặc thử lại (retry / 재시도) if thao tác (operation / 연산) safely retryable.

Thử lại (retry / 재시도) tự động mọi optimistic khóa (lock / 잠금) thất bại (failure / 실패) có thể ghi đè người dùng (user / 사용자) intent nếu merge ngữ nghĩa (semantics / 의미론) không rõ.

---

# 28. liên kết (connection / 연결) Pool là Bulkhead

Liên kết (connection / 연결) pool không chỉ tối ưu hóa (optimization / 최적화) để reuse connections. Nó giới hạn số concurrent DB operations.

App có 10 instances × pool 100 = up to 1000 DB connections. cơ sở dữ liệu (database / 데이터베이스) có thể chỉ handle tốt 200.

Virtual threads không thay đổi DB sức chứa (capacity / 용량).

**mẫu lập trình (programming pattern / 프로그래밍 패턴) — Bulkhead.** Pool bảo vệ scarce downstream tài nguyên (resource / 자원).

---

# 29. Pool hết thời gian chờ (timeout / 타임아웃) không đồng nghĩa Pool quá nhỏ

Khi threads chờ liên kết (connection / 연결) quá lâu, nguyên nhân có thể là slow queries, giao dịch (transaction / 트랜잭션) giữ liên kết (connection / 연결) trong HTTP calls, tranh chấp khóa (lock contention / 잠금 경합) hoặc liên kết (connection / 연결) leak.

Tăng pool có thể làm DB overloaded hơn.

Cấp cao (senior / 시니어) workflow: nhìn active/pending liên kết (connection / 연결), acquisition độ trễ (latency / 지연 시간), truy vấn (query / 쿼리) độ trễ (latency / 지연 시간), giao dịch (transaction / 트랜잭션) duration và DB CPU/locks.

---

# 30. MVC với nền tảng (platform / 플랫폼) Threads

Classic servlet ứng dụng (application / 애플리케이션) có yêu cầu (request / 요청) mapped lên nền tảng (platform / 플랫폼) luồng thực thi (thread / 스레드) từ bộ chứa (container / 컨테이너) pool. Blocking JDBC/HTTP làm luồng thực thi (thread / 스레드) chờ.

Sức chứa (capacity / 용량) roughly bound bởi luồng thực thi (thread / 스레드) pool và downstream resources.

Đây là mô hình rất dễ hiểu và đã chạy enterprise hàng chục năm.

---

# 31. MVC với Virtual Threads

Với Java 21+ và Boot:

```yaml
spring:
  threads:
    virtual:
      enabled: true
```

blocking-style yêu cầu (request / 요청) có thể chạy trên lightweight virtual threads.

Điều này làm high concurrent I/O dễ quy mô (scale / 규모) mà vẫn giữ imperative mã (code / 코드).

Nhưng CPU-bound thao tác (operation / 연산) không nhanh hơn. DB pool, remote API tính đồng thời (concurrency / 동시성) và tệp (file / 파일) descriptors vẫn hữu hạn.

Boot 4.1 docs hiện khuyến nghị hiện đại (modern / 현대적) JDK versions cho trải nghiệm virtual luồng thực thi (thread / 스레드) tốt hơn; pinned virtual luồng thực thi (thread / 스레드) có thể được quan sát qua JFR/jcmd.

---

# 32. Pinning

Một virtual luồng thực thi (thread / 스레드) có thể bị pinned vào carrier trong một số blocking/monitor/bản địa (native / 네이티브) scenarios tùy JDK phiên bản (version / 버전).

Không sửa bằng “remove synchronized everywhere”. Hãy đo.

JFR virtual-thread events và tooling giúp xem tải công việc (workload / 워크로드) có pinning đáng kể không.

Hiện đại (modern / 현대적) JDK đã cải tiến virtual luồng thực thi (thread / 스레드)/synchronized tương tác (interaction / 상호작용) qua releases, vì vậy đừng dùng advice Java 21 ban đầu như chân lý mãi mãi.

---

# 33. yêu cầu (request / 요청) Deadline thay vì nhiều hết thời gian chờ (timeout / 타임아웃) rời rạc

Máy khách (client / 클라이언트) cho bạn SLA 2 giây.

Nếu dịch vụ (service / 서비스) A đặt DB hết thời gian chờ (timeout / 타임아웃) 5s, payment 5s, inventory 5s và thử lại (retry / 재시도) 3 lần, yêu cầu (request / 요청) không thể tôn trọng 2s.

Cấp cao (senior / 시니어) thiết kế (design / 설계) dùng ngân sách (budget / 예산):

```text
incoming deadline
→ local processing budget
→ downstream remaining budget
```

Một downstream lời gọi (call / 호출) bắt đầu ở 1.8s không nên có 5s hết thời gian chờ (timeout / 타임아웃).

---

# 34. Streaming phản hồi (response / 응답)

Nếu export 5GB tệp (file / 파일), không đọc toàn bộ thành byte array rồi trả.

Streaming giữ bộ nhớ (memory / 메모리) bounded nhưng tài nguyên (resource / 자원) vòng đời (lifecycle / 생명주기) khó hơn: máy khách (client / 클라이언트) disconnect, tệp (file / 파일) close, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và backpressure.

Không giữ JPA giao dịch (transaction / 트랜잭션) mở hàng phút để stream lazy thực thể (entity / 엔터티) rows nếu có lựa chọn tốt hơn.

---

# 35. yêu cầu (request / 요청) Payload Limits

Công khai (public / 공개) endpoint cần limit JSON/multipart/header sizes ở máy chủ (server / 서버)/khung phần mềm (framework / 프레임워크)/gateway layers.

Unbounded upload có thể gây bộ nhớ (memory / 메모리)/disk exhaustion.

Tệp (file / 파일) upload còn cần sanitize filename/đường dẫn (path / 경로), validate content và lưu trữ (storage / 저장소) isolation.

---

# 36. WebFlux là mô hình thực thi (execution model / 실행 모델) khác

WebFlux dựa trên Reactive Streams và non-blocking/event-loop-friendly kiến trúc (architecture / 아키텍처).

Bạn không học WebFlux bằng cách đổi:

```java
User
```

thành:

```java
Mono<User>
```

rồi giữ mọi blocking JPA lời gọi (call / 호출).

Nếu vòng lặp sự kiện (event loop / 이벤트 루프) luồng thực thi (thread / 스레드) gọi JDBC blocking, nó chặn nhiều requests cùng share vòng lặp (loop / 루프).

---

# 37. Mono và Flux

`Mono<T>` biểu diễn 0 hoặc 1 item async stream. `Flux<T>` biểu diễn 0..N.

Chuỗi xử lý (pipeline / 파이프라인) được bản dựng (build / 빌드) trước rồi công việc (work / 작업) thường xảy ra khi subscribe.

```java
webClient.get()
    .retrieve()
    .bodyToMono(User.class)
    .map(this::toDomain);
```

Nếu subscribe nhiều lần vào cold publisher, công việc (work / 작업) có thể chạy nhiều lần.

---

# 38. `map` vs `flatMap` trong Reactor

`map` biến giá trị (value / 값) synchronously:

```text
User → UserResponse
```

`flatMap` dùng khi hàm (function / 함수) trả publisher:

```text
UserId → Mono<User>
```

Unconstrained `flatMap` có thể tăng tính đồng thời (concurrency / 동시성) và reorder results. `concatMap` giữ chuỗi (sequence / 시퀀스) hơn nhưng giảm tính đồng thời (concurrency / 동시성).

Tính đồng thời (concurrency / 동시성) operator cũng là sức chứa (capacity / 용량) quyết định (decision / 결정).

---

# 39. Backpressure

Reactive Streams subscriber báo demand. Producer không nên phát vô hạn khi bên tiêu thụ (consumer / 소비자) chậm.

Backpressure là giao thức (protocol / 프로토콜) first-class, khác việc tạo million futures rồi để bộ nhớ (memory / 메모리) hàng đợi (queue / 큐).

Nếu bài toán (problem / 문제) cần streaming dữ liệu (data / 데이터) và end-to-end reactive hỗ trợ (support / 지원), WebFlux có lợi thế thật. Nếu CRUD blocking/JPA, MVC + virtual threads có thể đơn giản hơn.

---

# 40. Reactor ngữ cảnh (context / 맥락)

Reactive thực thi (execution / 실행) có thể hop threads nên ThreadLocal không đủ reliable cho yêu cầu (request / 요청) siêu dữ liệu (metadata / 메타데이터).

Reactor ngữ cảnh (context / 맥락) đi cùng subscriber/chuỗi xử lý (pipeline / 파이프라인).

Tracing/bảo mật (security / 보안) reactive integrations phải propagate ngữ cảnh (context / 맥락) theo reactive mô hình (model / 모델).

Đây là lý do bản sao (copy / 복사) blocking/thread-local patterns vào WebFlux gây bugs.

---

# 41. R2DBC không phải Reactive JPA

R2DBC cung cấp reactive relational truy cập (access / 접근).

Nó không có traditional JPA persistence ngữ cảnh (context / 맥락)/dirty checking/lazy loading mô hình (model / 모델).

Nếu chuyển từ JPA sang R2DBC, bạn đang đổi programming mô hình (model / 모델), không chỉ driver.

---

# 42. Chọn MVC, MVC+Virtual Threads hay WebFlux

MVC nền tảng (platform / 플랫폼) threads tốt khi hệ thống đơn giản, tính đồng thời (concurrency / 동시성) vừa và ecosystem blocking.

MVC + virtual threads rất hấp dẫn cho imperative, blocking I/O tải công việc (workload / 워크로드) với tính đồng thời (concurrency / 동시성) cao.

WebFlux phù hợp khi end-to-end reactive, streaming/backpressure, reactive DB/máy khách (client / 클라이언트) và event-loop mô hình (model / 모델) mang lợi ích rõ.

Không có “WebFlux luôn nhanh hơn”.

---

# 43. HTTP máy khách (client / 클라이언트) như hạ tầng (infrastructure / 인프라) Adapter

Bên ngoài (external / 외부) Payment API không nên leak `RestClient` phản hồi (response / 응답) types vào lĩnh vực (domain / 도메인).

Lĩnh vực (domain / 도메인) cổng (port / 포트):

```java
interface PaymentGateway {
    PaymentResult charge(
        OrderId orderId,
        Money amount);
}
```

Adapter:

```java
@Component
class HttpPaymentGateway
        implements PaymentGateway {

    private final PaymentHttpApi api;

    ...
}
```

Vendor DTO/HTTP exceptions được translate thành lĩnh vực (domain / 도메인)/ứng dụng (application / 애플리케이션) concepts.

**mẫu thiết kế (design pattern / 디자인 패턴) — Anti-Corruption tầng (layer / 계층).** Vendor mô hình (model / 모델) dừng ở ranh giới (boundary / 경계).

---

# 44. Remote thất bại (failure / 실패) Taxonomy

HTTP phụ thuộc (dependency / 의존성) có thể thất bại (fail / 실패) ở DNS, liên kết (connection / 연결), TLS handshake, pool acquisition, ghi (write / 쓰기), phản hồi (response / 응답) hết thời gian chờ (timeout / 타임아웃), 4xx, 5xx hoặc serialization.

Không map mọi thứ thành `PaymentException`.

Nghiệp vụ (business / 비즈니스) rejection như card declined khác transient mạng (network / 네트워크) thất bại (failure / 실패). thử lại (retry / 재시도) chính sách (policy / 정책) phụ thuộc classification.

---

# 45. thử lại (retry / 재시도) đúng cách

Thử lại (retry / 재시도) cần bốn điều: thất bại (failure / 실패) transient, thao tác (operation / 연산) idempotent hoặc được bảo vệ bằng idempotency key, attempts bounded, và delay/backoff/jitter nằm trong deadline.

Payment POST không có idempotency key mà thử lại (retry / 재시도) sau hết thời gian chờ (timeout / 타임아웃) có thể charge hai lần vì máy khách (client / 클라이언트) không biết máy chủ (server / 서버) đã xử lý yêu cầu (request / 요청) trước khi phản hồi (response / 응답) mất.

---

# 46. Circuit Breaker

Circuit breaker ngừng gửi yêu cầu (request / 요청) vào phụ thuộc (dependency / 의존성) đang thất bại (fail / 실패) liên tục.

States concept:

```text
CLOSED
→ failures threshold
OPEN
→ cooldown
HALF_OPEN
→ probe
```

Nó không thay thử lại (retry / 재시도). thử lại (retry / 재시도) cố lại thao tác (operation / 연산); circuit breaker bảo vệ hệ thống khỏi hammering phụ thuộc (dependency / 의존성) thất bại (fail / 실패).

Spring cốt lõi (core / 핵심) không ép một circuit-breaker hiện thực (implementation / 구현) duy nhất; thường dùng resilience ecosystem libraries.

---

# 47. Bulkhead

Payment, report và notification nên có sức chứa (capacity / 용량) riêng nếu một phụ thuộc (dependency / 의존성) có thể làm nghẽn tất cả workers/connections.

Hiện thực (implementation / 구현) có thể là Semaphore, pool hoặc liên kết (connection / 연결) limit.

Virtual threads càng làm bulkhead quan trọng vì luồng thực thi (thread / 스레드) creation không còn là natural limiter.

---

# 48. tải (load / 로드) Shedding

Khi hệ thống (system / 시스템) saturated, trả 429/503 sớm có thể tốt hơn hàng đợi (queue / 큐) 60 giây rồi hết thời gian chờ (timeout / 타임아웃).

Tải (load / 로드) shedding là nghiệp vụ (business / 비즈니스)/operational chính sách (policy / 정책): yêu cầu (request / 요청) nào drop được, yêu cầu (request / 요청) nào phải persist, máy khách (client / 클라이언트) thử lại (retry / 재시도) ra sao.

---

# 49. cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) không solve phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션)

Dịch vụ (service / 서비스) A:

```text
DB transaction
→ call Service B
```

Dịch vụ (service / 서비스) B không tự phép nối (join / 조인) giao dịch (transaction / 트랜잭션) A qua HTTP.

Nếu cần cross-service consistency, dùng saga, outbox, idempotency hoặc phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) technology tùy kiến trúc (architecture / 아키텍처).

Microservices đổi consistency mô hình (model / 모델); Spring annotation không xóa mạng (network / 네트워크) ranh giới (boundary / 경계).

---

# 50. Dual ghi (write / 쓰기) bài toán (problem / 문제)

Mã (code / 코드):

```text
save Order DB
commit
publish Kafka
```

Tiến trình (process / 프로세스) crash giữa lần ghi nhận (commit / 커밋) và publish tạo missing sự kiện (event / 이벤트).

Nếu publish trước rồi DB quay lui (rollback / 롤백), bên tiêu thụ (consumer / 소비자) thấy sự kiện (event / 이벤트) cho dữ liệu (data / 데이터) không tồn tại.

Đây là dual-write bài toán (problem / 문제).

---

# 51. Transactional Outbox

Trong **cùng cục bộ (local / 로컬) DB giao dịch (transaction / 트랜잭션)**:

```text
insert/update Order
+
insert OutboxEvent
```

Lần ghi nhận (commit / 커밋) đồng thời.

Separate publisher đọc outbox và publish broker.

Nếu publisher crash sau publish nhưng trước mark sent, sự kiện (event / 이벤트) có thể publish lại. bên tiêu thụ (consumer / 소비자) cần idempotency.

Outbox giải quyết durable intent, không tạo exactly-once end-to-end magic.

---

# 52. Idempotent bên tiêu thụ (consumer / 소비자)

Message có `eventId`/nghiệp vụ (business / 비즈니스) key.

Bên tiêu thụ (consumer / 소비자) lưu processed ID hoặc thực hiện chuyển tiếp trạng thái (state transition / 상태 전이) có uniqueness ràng buộc (constraint / 제약조건) để duplicate delivery không tạo duplicate tác động (effect / 효과).

At-least-once delivery + idempotent bên tiêu thụ (consumer / 소비자) là mẫu (pattern / 패턴) phổ biến.

---

# 53. Saga

Cross-service luồng (flow / 흐름):

```text
reserve inventory
→ authorize payment
→ create shipment
```

Nếu shipment thất bại (fail / 실패), saga có thể trigger compensation:

```text
refund/release payment
release inventory
```

Compensation là nghiệp vụ (business / 비즈니스) thao tác (operation / 연산), không phải quay lui (rollback / 롤백) cơ sở dữ liệu (database / 데이터베이스) thời gian (time / 시간) machine.

---

# 54. Spring ứng dụng (application / 애플리케이션) sự kiện (event / 이벤트) vs tích hợp (integration / 통합) sự kiện (event / 이벤트)

`ApplicationEvent` là in-process.

Tích hợp (integration / 통합) sự kiện (event / 이벤트) là cross-system đặc tả hợp đồng (contract / 계약).

Đừng serialize nội bộ (internal / 내부) JPA thực thể (entity / 엔터티) rồi gọi đó là sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약).

Tích hợp (integration / 통합) sự kiện (event / 이벤트) cần stable lược đồ (schema / 스키마)/phiên bản (version / 버전) evolution và payload chỉ chứa dữ liệu bên tiêu thụ (consumer / 소비자) cần.

---

# 55. bộ nhớ đệm (cache / 캐시) là Consistency hệ thống (system / 시스템)

Trước `@Cacheable`, hỏi nguồn chuẩn (source of truth / 정본), stale tolerance, TTL, max kích thước (size / 크기), eviction, multi-node hành vi (behavior / 동작) và cập nhật (update / 업데이트) thứ tự (ordering / 순서).

Nếu DB cập nhật (update / 업데이트) lần ghi nhận (commit / 커밋) nhưng bộ nhớ đệm (cache / 캐시) eviction thất bại (fail / 실패), bộ nhớ đệm (cache / 캐시) stale.

Nếu bộ nhớ đệm (cache / 캐시) updated trước DB lần ghi nhận (commit / 커밋) rồi giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백), bộ nhớ đệm (cache / 캐시) chứa future trạng thái (state / 상태) không tồn tại.

Giao dịch (transaction / 트랜잭션)/bộ nhớ đệm (cache / 캐시) tương tác (interaction / 상호작용) cần thiết kế (design / 설계).

---

# 56. bộ nhớ đệm (cache / 캐시) Stampede

Popular key hết hạn cùng lúc, 10.000 requests miss rồi cùng hit DB.

Mitigations: per-key single-flight, refresh-ahead, stale-while-revalidate, TTL jitter.

Bộ nhớ đệm (cache / 캐시) provider có thể hỗ trợ một số cơ chế (mechanism / 메커니즘), nhưng annotation Spring không tự giải quyết hết.

---

# 57. cục bộ (local / 로컬) vs phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시)

Cục bộ (local / 로컬) Caffeine-like bộ nhớ đệm (cache / 캐시) rất nhanh nhưng mỗi instance có trạng thái (state / 상태) riêng.

Phân tán (distributed / 분산) Redis-like bộ nhớ đệm (cache / 캐시) nhất quán chia sẻ hơn nhưng thêm mạng (network / 네트워크) độ trễ (latency / 지연 시간), serialization, availability và cluster độ phức tạp (complexity / 복잡도).

Nếu stale 5 giây chấp nhận được, cục bộ (local / 로컬) TTL có thể đủ. Đừng dùng phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시) chỉ vì app có nhiều instances nếu ngữ nghĩa (semantics / 의미론) không cần.

---

# 58. Spring bảo mật (security / 보안) Filter kiến trúc (architecture / 아키텍처)

Servlet yêu cầu (request / 요청) thường đi:

```text
Servlet container
→ DelegatingFilterProxy
→ FilterChainProxy
→ matching SecurityFilterChain
→ security filters
→ DispatcherServlet
```

`DelegatingFilterProxy` cầu nối (bridge / 브리지) servlet filter registration với Spring-managed bảo mật (security / 보안) hạ tầng (infrastructure / 인프라).

`FilterChainProxy` chọn bảo mật (security / 보안) chuỗi (chain / 사슬) phù hợp yêu cầu (request / 요청).

Hiểu luồng (flow / 흐름) này quan trọng khi có multiple chains cho `/api/**`, `/admin/**`.

---

<!-- SPRING_BATCH4_SECURITY_SENIOR -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Java Spring — Part 3: cấp cao (senior / 시니어)**, **Từ Spring dữ liệu (data / 데이터) repository tới EntityManager: persistence thời gian chạy (runtime / 런타임) thật sự nằm ở đâu?** nêu điều cần giải thích; **Bảo mật (security / 보안) môi trường vận hành (production / 운영 환경) mô hình (model / 모델): credential vận chuyển (transport / 전송), key vòng đời (lifecycle / 생명주기) và object-level authorization** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Khả năng quan sát (observability / 관측 가능성) phải phản ánh hàng đợi (queue / 큐)/tài nguyên (resource / 자원) boundaries của Spring ứng dụng (application / 애플리케이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안) môi trường vận hành (production / 운영 환경) mô hình (model / 모델): credential vận chuyển (transport / 전송), key vòng đời (lifecycle / 생명주기) và object-level authorization

Bảo mật (security / 보안) cấu hình (configuration / 구성) phải bắt đầu từ credential vận chuyển (transport / 전송). Session cookie nghĩa trình duyệt (browser / 브라우저) tự gửi credential và CSRF threat quan trọng. Bearer đơn vị từ (token / 토큰) trong `Authorization` header có threat khác nhưng vẫn cần XSS/lưu trữ (storage / 저장소)/leak controls ở máy khách (client / 클라이언트). CORS chỉ là trình duyệt (browser / 브라우저) origin chính sách (policy / 정책); nó không authenticate yêu cầu (request / 요청) và không thay authorization.

Với JWT tài nguyên (resource / 자원) máy chủ (server / 서버), signature kiểm tra hợp lệ (validation / 검증) mới chỉ chứng minh đơn vị từ (token / 토큰) phù hợp key/thuật toán (algorithm / 알고리즘). môi trường vận hành (production / 운영 환경) chính sách (policy / 정책) còn phải kiểm issuer, audience, thời gian (time / 시간) claims/clock skew, key rotation/JWK refresh và ánh xạ (mapping / 매핑) claims thành authorities đúng lĩnh vực (domain / 도메인). Log không được ghi raw truy cập (access / 접근) đơn vị từ (token / 토큰). Nếu định danh (identity / 식별자) provider outage xảy ra, hành vi (behavior / 동작) phụ thuộc key bộ nhớ đệm (cache / 캐시)/discovery chiến lược (strategy / 전략); đây là availability phụ thuộc (dependency / 의존성) cần được khả năng quan sát (observability / 관측 가능성) hóa.

Authorization theo role thường chưa đủ cho nghiệp vụ (business / 비즈니스) tài nguyên (resource / 자원). “người dùng (user / 사용자) có thể cancel thứ tự (order / 순서)” còn cần xác minh thứ tự (order / 순서) thuộc người dùng (user / 사용자) nào, trạng thái thứ tự (order / 순서) và tenant. chính sách (policy / 정책) này nên nằm ở use-case/lĩnh vực (domain / 도메인) authorization collaborator hoặc phương thức (method / 메서드) authorization có truy cập (access / 접근) tới lĩnh vực (domain / 도메인) facts, không chỉ ở URL matcher. Nếu chính sách (policy / 정책) chỉ nằm controller, nội bộ (internal / 내부)/batch/message entry điểm (point / 지점) có thể bypass.
<!-- SPRING_BATCH4_SECURITY_SENIOR_END -->

---

# 59. AuthenticationManager và AuthenticationProvider

Authentication filter tạo authentication yêu cầu (request / 요청)/đơn vị từ (token / 토큰) rồi gọi `AuthenticationManager`.

`ProviderManager` là dùng chung (common / 공통) hiện thực (implementation / 구현) phối hợp nhiều `AuthenticationProvider`.

Provider có thể authenticate password, JWT hoặc custom credential kiểu (type / 타입).

Sau success, authenticated `Authentication` đi vào SecurityContext.

---

# 60. Multiple SecurityFilterChains

Bạn có thể có chuỗi (chain / 사슬) riêng:

```text
/api/**
→ OAuth2 Resource Server

/admin/**
→ stricter admin config
```

Matcher/thứ tự (order / 순서) quyết định chuỗi (chain / 사슬) nào xử lý yêu cầu (request / 요청).

Mis-order có thể khiến yêu cầu (request / 요청) rơi vào default chuỗi (chain / 사슬).

Bảo mật (security / 보안) gỡ lỗi (debug / 디버그) nên dấu vết (trace / 추적) matcher + filter chuỗi (chain / 사슬), không chỉ controller.

---

# 61. JWT tài nguyên (resource / 자원) máy chủ (server / 서버)

Spring bảo mật (security / 보안) có OAuth2 tài nguyên (resource / 자원) máy chủ (server / 서버) hỗ trợ (support / 지원) để validate JWT từ authorization máy chủ (server / 서버).

Cấu hình (config / 설정) issuer:

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://idp.example.com
```

Khung phần mềm (framework / 프레임워크) có thể discover keys/siêu dữ liệu (metadata / 메타데이터) và verify signature/issuer/timestamps theo cấu hình (configuration / 구성).

Môi trường vận hành (production / 운영 환경) authorization còn phải quan tâm audience và ánh xạ (mapping / 매핑) claims/scopes đúng ứng dụng (application / 애플리케이션).

---

# 62. JWT không phải Encryption

Signed JWT payload thường đọc được.

Không đặt password/secret vì nghĩ “đơn vị từ (token / 토큰) encoded nên private”.

Signature bảo integrity/authenticity theo key/thuật toán (algorithm / 알고리즘), không tự mã hóa confidentiality.

---

# 63. phạm vi (scope / 범위), Authority và Role

OAuth phạm vi (scope / 범위) đại diện permission delegated cho đơn vị từ (token / 토큰)/máy khách (client / 클라이언트). ứng dụng (application / 애플리케이션) authorities/roles là mô hình (model / 모델) authorization của app.

Có thể map phạm vi (scope / 범위) thành authority, nhưng đừng coi role và phạm vi (scope / 범위) là universal same concept.

Complex quyền sở hữu (ownership / 소유권) permission có thể cần lĩnh vực (domain / 도메인) authorization dịch vụ (service / 서비스).

---

# 64. CSRF và Cookie Authentication

Trình duyệt (browser / 브라우저) tự attach cookies vào cross-site requests, vì vậy state-changing cookie-authenticated applications cần CSRF protection.

Bearer đơn vị từ (token / 토큰) trong `Authorization` header không tự được trình duyệt (browser / 브라우저) attach theo same way, nên threat mô hình (model / 모델) khác.

Bảo mật (security / 보안) chính sách (policy / 정책) phải xuất phát từ credential vận chuyển (transport / 전송), không từ câu “đây là REST”.

---

# 65. bảo mật (security / 보안) ngữ cảnh (context / 맥락) và Async

Bảo mật (security / 보안) ngữ cảnh (context / 맥락) có execution-context propagation concerns. Nếu submit tác vụ (task / 작업) sang arbitrary executor, principal không nhất thiết tự xuất hiện.

Spring bảo mật (security / 보안) có ngữ cảnh (context / 맥락) propagation integrations, nhưng bạn phải biết thực thi (execution / 실행) ranh giới (boundary / 경계).

Reactive bảo mật (security / 보안) lại dùng Reactor ngữ cảnh (context / 맥락) mô hình (model / 모델).

---

<!-- SPRING_BATCH5_OBS_SENIOR -->

> **Chuyển mạch:** Trong **Java Spring — Part 3: cấp cao (senior / 시니어)**, cơ chế trong **Bảo mật (security / 보안) môi trường vận hành (production / 운영 환경) mô hình (model / 모델): credential vận chuyển (transport / 전송), key vòng đời (lifecycle / 생명주기) và object-level authorization** cần được kiểm chứng bằng dấu vết cụ thể; **Khả năng quan sát (observability / 관측 가능성) phải phản ánh hàng đợi (queue / 큐)/tài nguyên (resource / 자원) boundaries của Spring ứng dụng (application / 애플리케이션)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **Môi trường vận hành (production / 운영 환경) troubleshooting theo symptom → tầng (layer / 계층) → bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng quan sát (observability / 관측 가능성) phải phản ánh hàng đợi (queue / 큐)/tài nguyên (resource / 자원) boundaries của Spring ứng dụng (application / 애플리케이션)

Một yêu cầu (request / 요청) timer duy nhất không đủ để biết yêu cầu (request / 요청) chậm ở đâu. môi trường vận hành (production / 운영 환경) dashboard nên cho thấy máy chủ (server / 서버) yêu cầu (request / 요청) độ trễ (latency / 지연 시간), active/in-flight requests, executor/virtual-thread hành vi (behavior / 동작) phù hợp thời gian chạy (runtime / 런타임), DB pool active/pending/acquisition thời gian (time / 시간), truy vấn (query / 쿼리) độ trễ (latency / 지연 시간), HTTP-client độ trễ (latency / 지연 시간), bộ nhớ đệm (cache / 캐시) hit/miss và JVM CPU/GC. Khi mỗi scarce tài nguyên (resource / 자원) có saturation tín hiệu (signal / 신호), bạn có thể phân biệt CPU-bound với queue-bound hoặc downstream-bound.

Dấu vết (trace / 추적) là nhân quả (causal / 인과적) đường dẫn (path / 경로), nhưng dấu vết (trace / 추적) không thay chỉ số (metric / 지표). Sampling có thể bỏ mất yêu cầu (request / 요청) hiếm; metrics cho phân phối (distribution / 분포)/p95/p99 và saturation liên tục. JFR lại trả lời JVM-level CPU/allocation/khóa (lock / 잠금)/GC mà tracing không thấy. Troubleshooting tốt chuyển giữa bốn lớp: metrics xác định thời điểm/phạm vi, dấu vết (trace / 추적) tìm phụ thuộc (dependency / 의존성)/span, logs lấy lĩnh vực (domain / 도메인)/lỗi (error / 오류) ngữ cảnh (context / 맥락), profile/JFR/DB plan xác minh thực thi (execution / 실행) chi phí (cost / 비용).
<!-- SPRING_BATCH5_OBS_SENIOR_END -->

---

# 66. khả năng quan sát (observability / 관측 가능성): Metrics, Traces, Logs

Metrics trả lời “hệ thống đang xảy ra bao nhiêu/lâu bao nhiêu”. Traces trả lời “yêu cầu (request / 요청) cụ thể đi qua đâu”. Logs cho detailed events/ngữ cảnh (context / 맥락). JFR/profile cho thời gian chạy (runtime / 런타임).

Không một nguồn nào đủ.

Khi p99 tăng, dấu vết (trace / 추적) có thể chỉ downstream span chậm; DB metrics cho khóa (lock / 잠금); JFR cho CPU/GC; logs cho lỗi (error / 오류) detail.

---

# 67. Micrometer Observation

Observation là lớp trừu tượng (abstraction / 추상화) cho thao tác (operation / 연산) instrumentation.

Concept:

```text
Observation
→ context
→ handlers
→ metrics/tracing
```

Một custom nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) `order.checkout` có low-cardinality tags như channel/payment kiểu (type / 타입) và high-cardinality dấu vết (trace / 추적) fields như orderId.

---

# 68. chỉ số (metric / 지표) Cardinality

Đừng tag chỉ số (metric / 지표):

```text
userId
orderId
raw URL with IDs
traceId
```

Mỗi unique giá trị (value / 값) tạo thời gian (time / 시간) series.

Metrics backend có thể chết vì cardinality explosion dù app vẫn chạy.

High-cardinality identifiers thuộc logs/traces.

---

# 69. phân tán (distributed / 분산) Tracing và ngữ cảnh (context / 맥락) Propagation

Yêu cầu (request / 요청) vào dịch vụ (service / 서비스) A có dấu vết (trace / 추적)/span ngữ cảnh (context / 맥락), HTTP máy khách (client / 클라이언트) phải propagate headers sang B. Async tác vụ (task / 작업) cũng cần ngữ cảnh (context / 맥락) propagation.

ThreadLocal-only mô hình (model / 모델) không đủ cho reactive luồng thực thi (thread / 스레드) hops. Virtual threads thay đổi luồng thực thi (thread / 스레드) quantity nhưng mỗi yêu cầu (request / 요청) có thể vẫn thread-confined khá tự nhiên tùy thiết kế (design / 설계).

Cấp cao (senior / 시니어) phải hiểu thư viện (library / 라이브러리)/khung phần mềm (framework / 프레임워크) đang dùng ngữ cảnh (context / 맥락) cơ chế (mechanism / 메커니즘) nào.

---

# 70. Actuator Management Surface

Endpoints như `env`, `configprops`, `mappings`, `heapdump`, `threaddump` có diagnostic giá trị (value / 값) nhưng có thể lộ secrets/nội bộ (internal / 내부) topology.

Management mạng (network / 네트워크)/bảo mật (security / 보안) phải được thiết kế riêng.

Không expose `/actuator/**` công khai (public / 공개) vì “chỉ dev biết URL”.

---

# 71. Health Check ngữ nghĩa (semantics / 의미론)

Readiness nên phản ánh khả năng phục vụ traffic. Liveness chỉ thất bại (fail / 실패) nếu tiến trình (process / 프로세스) trạng thái (state / 상태) hỏng và restart có ích.

Nếu DB down, readiness false hợp lý. Liveness false có thể khiến tất cả pods restart đồng loạt, làm sự cố (incident / 인시던트) tệ hơn.

Health indicator phải bounded; không probe phụ thuộc (dependency / 의존성) với unbounded mạng (network / 네트워크) lời gọi (call / 호출).

---

# 72. `@Async` trong môi trường vận hành (production / 운영 환경)

Fire-and-forget `@Async void` cho email marketing có thể chấp nhận nếu mất một tác vụ (task / 작업) không trọng yếu (critical / 중요).

Nhưng payment, legal kiểm tra (audit / 감사) hoặc shipment creation cần durability. In-memory tác vụ (task / 작업) mất khi pod crash/redeploy.

Nếu thao tác (operation / 연산) business-critical, message/job hàng đợi (queue / 큐) durable thường phù hợp hơn.

---

# 73. Executor sức chứa (capacity / 용량)

Nền tảng (platform / 플랫폼) ThreadPoolTaskExecutor có cốt lõi (core / 핵심)/max/hàng đợi (queue / 큐). hàng đợi (queue / 큐) unbounded hide overload.

CallerRuns/rejection hoặc bounded queues làm overload visible.

Virtual luồng thực thi (thread / 스레드) per tác vụ (task / 작업) bỏ scarce-thread pool, nhưng bạn vẫn phải add Semaphore/bulkhead cho downstream limit.

---

# 74. Scheduled Jobs trong Cluster

`@Scheduled` chạy trên mỗi JVM.

Nếu có 5 replicas, 5 executions.

Nếu job là cleanup idempotent và parallel-safe có thể okay. Nếu monthly billing phải exactly one logical run, cần leader/phân tán (distributed / 분산) khóa (lock / 잠금)/job nền tảng (platform / 플랫폼).

---

# 75. Graceful Shutdown

Triển khai (deployment / 배포) không chỉ “Spring ngữ cảnh (context / 맥락) close”.

Ideal:

```text
readiness off
→ LB stops new traffic
→ finish in-flight
→ stop scheduled/background producers
→ drain workers
→ close client pools
→ context close
```

Configure shutdown hết thời gian chờ (timeout / 타임아웃) phù hợp max yêu cầu (request / 요청)/tác vụ (task / 작업) duration và Kubernetes termination grace period.

---

# 76. Startup hiệu năng (performance / 성능)

Startup thời gian (time / 시간) matters trong autoscaling/serverless/bộ chứa (container / 컨테이너) rollout.

Measure sources:

```text
component/config processing
JPA boot
Flyway
network discovery
bean init
classloading
```

Spring provides startup instrumentation facilities and Boot điều kiện (condition / 조건) info.

Fix actual bottleneck, không blindly turn everything lazy.

---

# 77. AOT Processing

Spring AOT analyzes ứng dụng (application / 애플리케이션) ahead of thời gian chạy (runtime / 런타임) và generate mã (code / 코드)/siêu dữ liệu (metadata / 메타데이터)/hints.

AOT không đồng nghĩa bản địa (native / 네이티브) ảnh (image / 이미지). Nó có thể phục vụ optimized startup modes và GraalVM bản địa (native / 네이티브) workflow.

Động (dynamic / 동적) reflection/proxy/tài nguyên (resource / 자원) hành vi (behavior / 동작) phải được known/inferred ahead of thời gian (time / 시간) hơn.

---

# 78. GraalVM bản địa (native / 네이티브) ảnh (image / 이미지)

Bản địa (native / 네이티브) ảnh (image / 이미지) compile ứng dụng (application / 애플리케이션) thành bản địa (native / 네이티브) executable.

Lợi ích thường là startup nhanh và bộ nhớ (memory / 메모리) footprint thấp hơn. sự đánh đổi (trade-off / 트레이드오프) là bản dựng (build / 빌드) thời gian (time / 시간)/độ phức tạp (complexity / 복잡도), closed-world các ràng buộc (constraints / 제약조건들) và khác biệt thời gian chạy (runtime / 런타임) hiệu năng (performance / 성능) so JVM JIT.

Đừng benchmark 1 yêu cầu (request / 요청) rồi kết luận bản địa (native / 네이티브) tốt hơn toàn diện.

---

# 79. RuntimeHints

Custom động (dynamic / 동적) tính năng (feature / 기능) có thể cần hints:

```text
reflection
resources
serialization
JDK proxies
```

Spring AOT tự infer nhiều tiêu chuẩn (standard / 표준) Spring cases. Custom reflection/metaprogramming có thể cần `RuntimeHintsRegistrar`.

Bản địa (native / 네이티브) triển khai (deployment / 배포) phải kiểm thử (test / 테스트) actual executable.

---

# 80. Boot 4 và Jackson 3

Spring Boot 4 ưu tiên Jackson 3. Jackson 3 thay group/gói (package / 패키지) cho nhiều modules (`tools.jackson` generation), trong khi annotations có tính tương thích (compatibility / 호환성) specifics.

Nếu mã (code / 코드) chỉ dùng normal DTO + Boot auto-config, di chuyển (migration / 마이그레이션) dễ hơn.

Nếu bạn inject/customize Jackson nội bộ (internal / 내부) types everywhere, di chuyển (migration / 마이그레이션) lớn hơn.

Depend on stable khung phần mềm (framework / 프레임워크)/ứng dụng (application / 애플리케이션) abstractions, không leak third-party hiện thực (implementation / 구현) sâu khắp lĩnh vực (domain / 도메인).

---

# 81. Boot 3 → Boot 4 di chuyển (migration / 마이그레이션)

Không nhảy blind.

Nên đưa dự án (project / 프로젝트) lên latest 3.5 first, xử lý deprecations, dependencies và tests, rồi Boot 4.

Boot 4 yêu cầu Spring khung phần mềm (framework / 프레임워크) 7, Jakarta EE 11/Servlet 6.1 baseline và có phụ thuộc (dependency / 의존성)/mô-đun (module / 모듈) changes. Jackson 3 là thay đổi (change / 변경) lớn.

Di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) phải cover startup, web serialization, bảo mật (security / 보안), JPA/dữ liệu (data / 데이터), custom auto-config và khả năng quan sát (observability / 관측 가능성) agents.

---

# 82. Linkage Errors khi Upgrade

`NoSuchMethodError`, `NoClassDefFoundError`, `AbstractMethodError` thường chỉ compile/thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) mismatch.

Ví dụ app compile với thư viện (library / 라이브러리) v2 nhưng thời gian chạy (runtime / 런타임) tải (load / 로드) v1.

Use:

```bash
./mvnw dependency:tree
```

và inspect actual packaged sản phẩm tạo ra (artifact / 산출물)/classloader.

Đừng chữa bằng random `clean` mãi.

---

# 83. Modular Monolith

Microservices không phải default “cấp cao (senior / 시니어) kiến trúc (architecture / 아키텍처)”.

Một Spring Boot triển khai (deployment / 배포) có modules `order`, `payment`, `inventory`, `customer` với ranh giới (boundary / 경계) rõ có nhiều lợi ích: cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) dễ, operations đơn giản, refactor nhanh.

Mô-đun (module / 모듈) communication nên qua công khai (public / 공개) ứng dụng (application / 애플리케이션) APIs/events, không import repository/thực thể (entity / 엔터티) internals tùy tiện.

---

# 84. gói (package / 패키지) ranh giới (boundary / 경계)

Tính năng (feature / 기능) mô-đun (module / 모듈) có thể expose:

```java
public interface OrderApplication {
    OrderResult place(
        PlaceOrderCommand command);
}
```

Nội bộ (internal / 내부) adapters/repositories package-private hoặc nội bộ (internal / 내부) gói (package / 패키지).

Phụ thuộc (dependency / 의존성) direction phải enforce bằng kiến trúc (architecture / 아키텍처) tests/modulith tooling khi dự án (project / 프로젝트) lớn.

Folder names không đủ.

---

# 85. Spring Modulith Awareness

Spring Modulith cung cấp hỗ trợ (support / 지원) để mô hình (model / 모델) ứng dụng (application / 애플리케이션) modules, verify dependencies, kiểm thử (test / 테스트) mô-đun (module / 모듈) và document kiến trúc (architecture / 아키텍처)/sự kiện (event / 이벤트) interactions.

Nó hữu ích cho modular monolith, nhưng không thay việc thiết kế bounded responsibilities.

Master Supplement sẽ đi sâu hơn nếu cần.

---

# 86. Hexagonal kiến trúc (architecture / 아키텍처) với Spring

Cốt lõi (core / 핵심) defines ports:

```java
interface OrderRepository {
}

interface PaymentGateway {
}
```

Adapters:

```text
Spring MVC controller
JPA repository adapter
RestClient payment adapter
Kafka event publisher
```

Spring DI assemble.

Lợi ích là lĩnh vực (domain / 도메인)/ứng dụng (application / 애플리케이션) không phụ thuộc trực tiếp HTTP/JPA/vendor.

Đừng tạo 5 layers interfaces cho CRUD trivial chỉ để “clean kiến trúc (architecture / 아키텍처)”. kiến trúc (architecture / 아키텍처) độ phức tạp (complexity / 복잡도) phải proportional bài toán (problem / 문제) độ phức tạp (complexity / 복잡도).

---

# 87. Anti-Corruption tầng (layer / 계층)

Bên ngoài (external / 외부) vendor payment có mô hình (model / 모델):

```text
VendorPaymentStatus
VendorMoney
VendorErrorCode
```

Không để chúng đi xuyên ứng dụng (application / 애플리케이션).

Adapter map:

```text
VendorResponse
→ PaymentResult
```

Khi đổi vendor, lĩnh vực (domain / 도메인) ít đổi.

---

# 88. giao dịch (transaction / 트랜잭션) Script vs Rich lĩnh vực (domain / 도메인)

Simple admin CRUD có thể dùng dịch vụ (service / 서비스) methods + repository, gọi là transaction-script style.

Complex thứ tự (order / 순서)/pricing/rủi ro (risk / 위험) lĩnh vực (domain / 도메인) có thể cần giá trị (value / 값) objects, entities và invariants.

Cấp cao (senior / 시니어) không force DDD cho todo app và cũng không để complex banking rules thành 2.000-line dịch vụ (service / 서비스).

---

# 89. Annotation Soup

Phương thức (method / 메서드):

```java
@Transactional
@Async
@Cacheable
@PreAuthorize
@Observed
@Retryable
public Result execute() { ... }
```

là tín hiệu (signal / 신호) cần rà soát (review / 검토).

Bạn phải giải thích chính xác (exact / 정확한) thứ tự (ordering / 순서), luồng thực thi (thread / 스레드), giao dịch (transaction / 트랜잭션), thử lại (retry / 재시도), bộ nhớ đệm (cache / 캐시) và bảo mật (security / 보안) ngữ cảnh (context / 맥락). Nếu không, split responsibilities/policies.

Spring annotations giảm boilerplate nhưng có thể tăng hidden điều khiển (control / 제어) luồng (flow / 흐름).

---

# 90. God dịch vụ (service / 서비스)

`OrderService` 3.000 lines có nghiệp vụ (business / 비즈니스), email, SQL, tệp (file / 파일), HTTP, bộ nhớ đệm (cache / 캐시) và reporting là low cohesion.

Tách theo use trường hợp (case / 사례)/năng lực (capability / 역량), không chỉ tách thành `OrderServiceHelper`.

Phụ thuộc (dependency / 의존성) count, thay đổi (change / 변경) reasons và kiểm thử (test / 테스트) setup cho thấy boundaries.

---

# 91. Static ApplicationContext Holder

Mẫu (pattern / 패턴):

```java
SpringContext.getBean(Foo.class)
```

cho phép bất kỳ mã (code / 코드) nào kéo phụ thuộc (dependency / 의존성) toàn cục (global / 전역).

Nó biến DI thành dịch vụ (service / 서비스) Locator và phá phụ thuộc (dependency / 의존성) visibility.

Chỉ dùng trong tích hợp (integration / 통합) các ràng buộc (constraints / 제약조건들) rất đặc biệt, không làm default kiến trúc (architecture / 아키텍처).

---

# 92. thực thể (entity / 엔터티) Everywhere

Nếu `UserEntity` dùng làm API DTO, Kafka message, bộ nhớ đệm (cache / 캐시) giá trị (value / 값), lĩnh vực (domain / 도메인) đối tượng (object / 객체) và batch format, mọi lược đồ (schema / 스키마)/persistence thay đổi (change / 변경) có blast radius lớn.

Tách biểu diễn (representation / 표현) ở boundaries có vòng đời (lifecycle / 생명주기)/tính tương thích (compatibility / 호환성) khác nhau.

---

<!-- SPRING_BATCH5_TROUBLESHOOTING_SENIOR -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 3: cấp cao (senior / 시니어)**, **Khả năng quan sát (observability / 관측 가능성) phải phản ánh hàng đợi (queue / 큐)/tài nguyên (resource / 자원) boundaries của Spring ứng dụng (application / 애플리케이션)** nêu điều cần giải thích; **Môi trường vận hành (production / 운영 환경) troubleshooting theo symptom → tầng (layer / 계층) → bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Testing kiến trúc (architecture / 아키텍처) phải mô phỏng đúng thất bại (failure / 실패) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường vận hành (production / 운영 환경) troubleshooting theo symptom → tầng (layer / 계층) → bằng chứng (evidence / 증거)

Nếu ứng dụng (application / 애플리케이션) **không start**, bắt đầu từ first meaningful cause trong exception chuỗi (chain / 사슬) rồi phân loại: cấu hình (configuration / 구성) binding, missing/ambiguous bean, điều kiện (condition / 조건) mismatch, lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션), cơ sở dữ liệu (database / 데이터베이스) connectivity, classpath/linkage hay custom initialization. điều kiện (condition / 조건) report và phụ thuộc (dependency / 의존성) cây (tree / 트리) hữu ích hơn thêm annotation thử nghiệm.

Nếu yêu cầu (request / 요청) trả **404**, trước tiên kiểm ánh xạ (mapping / 매핑)/servlet ngữ cảnh (context / 맥락)/đường dẫn (path / 경로). Nếu **400**, nhìn conversion, JSON deserialize và Bean kiểm tra hợp lệ (validation / 검증). Nếu **401**, dấu vết (trace / 추적) authentication chuỗi (chain / 사슬)/credential. Nếu **403**, xác định principal đã authenticated chưa và authorization quy tắc (rule / 규칙) nào deny. Nếu controller breakpoint không bao giờ hit, đừng gỡ lỗi (debug / 디버그) dịch vụ (service / 서비스) trước filter/ánh xạ (mapping / 매핑) tầng (layer / 계층).

Nếu endpoint **chậm nhưng CPU thấp**, tìm wait: DB liên kết (connection / 연결) acquisition, slow SQL/locks, remote HTTP, executor hàng đợi (queue / 큐), synchronized khóa (lock / 잠금). Nếu **CPU cao**, dùng JFR/profile trước; JSON serialization, crypto, regex, mapper loops, GC hoặc busy vòng lặp (loop / 루프) đều có thể là nguyên nhân. Nếu **RSS tăng nhưng vùng nhớ động (heap / 힙) ổn**, nhìn luồng thực thi (thread / 스레드) count/stacks, direct buffer/bản địa (native / 네이티브) bộ nhớ (memory / 메모리), metaspace và agents chứ không chỉ vùng nhớ động (heap / 힙) dump.

Nếu bật virtual threads mà thông lượng (throughput / 처리량) không tăng, kiểm downstream scarce tài nguyên (resource / 자원). 50 DB connections vẫn chỉ cho khoảng 50 concurrent DB operations bất kể có 500 hay 50.000 virtual threads. Nếu độ trễ (latency / 지연 시간) tăng, queueing ở pool/semaphore/downstream vẫn là bottleneck thật.
<!-- SPRING_BATCH5_TROUBLESHOOTING_SENIOR_END -->

---

# 93. môi trường vận hành (production / 운영 환경) Debugging: `@Transactional` không chạy

Checklist lập luận (reasoning / 추론):

Bean có do Spring quản lý không? lời gọi (call / 호출) có đi qua proxy không? phương thức (method / 메서드) có proxyable không? giao dịch (transaction / 트랜잭션) manager đúng không? Annotation đặt ở phương thức (method / 메서드)/lớp (class / 클래스) mà proxy siêu dữ liệu (metadata / 메타데이터) resolve được không? Exception bị catch/swallow không? quay lui (rollback / 롤백) quy tắc (rule / 규칙) có phù hợp không?

Enable targeted giao dịch (transaction / 트랜잭션) logs nếu cần và observe DB liên kết (connection / 연결)/lần ghi nhận (commit / 커밋) hành vi (behavior / 동작). Đừng thêm annotation thứ hai.

---

# 94. môi trường vận hành (production / 운영 환경) Debugging: N+1

Dấu vết (trace / 추적) endpoint. Count SQL per yêu cầu (request / 요청). Xem serialization có truy cập (access / 접근) lazy quan hệ (relation / 관계). Check OSIV. Check mapper loops. Xem fetch đồ thị (graph / 그래프)/truy vấn (query / 쿼리).

Fix bằng fetch plan/projection, rồi measure truy vấn (query / 쿼리) count/p99 lại.

Không chỉ nhìn “endpoint chậm” và tăng CPU.

---

# 95. môi trường vận hành (production / 운영 환경) Debugging: DB Pool Exhausted

Check pool pending/acquisition thời gian (time / 시간), active count, giao dịch (transaction / 트랜잭션) duration, slow queries, locks và remote calls trong giao dịch (transaction / 트랜잭션).

Luồng thực thi (thread / 스레드) dump có thể cho thấy nhiều requests đang wait liên kết (connection / 연결).

Tăng max pool chỉ sau khi biết DB còn sức chứa (capacity / 용량).

---

# 96. môi trường vận hành (production / 운영 환경) Debugging: CPU 100%

Use JFR/profile. Check hot Java stacks, JSON serialization, crypto, regex, GC CPU, busy vòng lặp (loop / 루프), ORM ánh xạ (mapping / 매핑).

Spring Actuator metrics cho symptom; JFR cho thực thi (execution / 실행) detail.

---

# 97. CPU thấp nhưng độ trễ (latency / 지연 시간) cao

Đây thường là waiting bài toán (problem / 문제):

```text
DB lock/query
connection pool
remote HTTP
DNS
filesystem
thread lock
queue
```

Phân tán (distributed / 분산) dấu vết (trace / 추적) và luồng thực thi (thread / 스레드) dump rất hữu ích.

---

# 98. bộ nhớ (memory / 메모리) Growth

Possible ứng dụng (application / 애플리케이션) causes:

```text
unbounded cache
unbounded executor queue
HTTP session
large JPA persistence context
ThreadLocal
classloader leak
metrics cardinality
large buffers
```

Vùng nhớ vùng nhớ động (heap / 힙) dump/JFR/JVM tools cần phối hợp. RSS cao nhưng vùng nhớ động (heap / 힙) bình thường có thể là bản địa (native / 네이티브)/direct/luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) issue từ Java cốt lõi (core / 핵심).

Spring không thay JVM bộ nhớ (memory / 메모리) mô hình (model / 모델).

---

# 99. bảo mật (security / 보안) sự cố (incident / 인시던트) lập luận (reasoning / 추론)

401/403 cần dấu vết (trace / 추적) bảo mật (security / 보안) chuỗi (chain / 사슬), authentication cơ chế (mechanism / 메커니즘) và authorization quyết định (decision / 결정).

CORS trình duyệt (browser / 브라우저) lỗi (error / 오류) có thể che backend 401/403.

JWT issue cần check signature keys, issuer, audience, clock skew/expiry và claim ánh xạ (mapping / 매핑).

Không disable bảo mật (security / 보안) để “xác nhận endpoint”.

---

# 100. Logging và Sensitive yêu cầu dữ liệu (data request / 데이터 요청)/phản hồi (response / 응답) body logging có thể leak password/đơn vị từ (token / 토큰)/PII, tăng bộ nhớ (memory / 메모리) vì buffering và phá streaming.

Môi trường vận hành (production / 운영 환경) logging nên structured, redact fields và mẫu (sample / 표본) large/high-frequency dữ liệu (data / 데이터) khi cần.

Expected 404 không nhất thiết lỗi (error / 오류) dấu vết ngăn xếp (stack trace / 스택 트레이스).

---

# 101. SSRF trong RestClient/WebClient

Nếu endpoint cho người dùng (user / 사용자) nhập URL và máy chủ (server / 서버) fetch:

```text
https://...
```

attacker có thể mục tiêu (target / 대상) nội bộ (internal / 내부) siêu dữ liệu (metadata / 메타데이터) dịch vụ (service / 서비스)/localhost/private mạng (network / 네트워크).

Restrict allowed schemes/hosts/ports, DNS/IP ranges và redirects theo threat mô hình (model / 모델).

Spring máy khách (client / 클라이언트) API không tự làm nghiệp vụ (business / 비즈니스) allow-list.

---

# 102. Deserialization bảo mật (security / 보안)

Công khai (public / 공개) JSON không nên cho uncontrolled polymorphic kiểu (type / 타입) instantiation.

Bound yêu cầu (request / 요청) kích thước (size / 크기)/độ sâu (depth / 깊이) và điều khiển (control / 제어) allowed types.

DTO boundaries giảm mass assignment và deserialization attack surface.

---

# 103. Supply chuỗi (chain / 사슬)

Spring app kéo nhiều transitive dependencies. Theo dõi Boot maintenance line, CVEs, SBOM/phụ thuộc (dependency / 의존성) scanning.

Đừng override managed versions tùy tiện rồi vô tình kéo incompatible/security-old transitive đồ thị (graph / 그래프).

---

# 104. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링)

Cấp cao (senior / 시니어) tối ưu hóa (optimization / 최적화) vòng lặp (loop / 루프):

```text
define SLO
→ load/measure
→ identify bottleneck
→ hypothesis
→ change
→ measure again
```

“WebFlux nhanh”, “bản địa (native / 네이티브) nhanh”, “virtual luồng thực thi (thread / 스레드) nhanh”, “JPA chậm” đều là slogans nếu không gắn tải công việc (workload / 워크로드).

---

# 105. Tail độ trễ (latency / 지연 시간)

Average 100ms có thể che p99 3s.

Bên ngoài (external / 외부) dịch vụ (service / 서비스), GC, DB khóa (lock / 잠금) và queueing thường làm tail.

Nhánh học (track / 트랙) p50/p95/p99 và correlate với phụ thuộc (dependency / 의존성) spans.

---

# 106. Pagination và kết quả (result / 결과) Limits

Unbounded `/users` endpoint có thể trả millions rows, exhaust vùng nhớ động (heap / 힙)/DB.

Bound kích thước (size / 크기).

Deep offset:

```sql
offset 1000000 limit 20
```

có thể đắt.

Keyset/cursor pagination dùng stable ordered key để seek tiếp, thường quy mô (scale / 규모) tốt hơn.

---

# 107. Compression

HTTP compression giảm bandwidth cho JSON/văn bản (text / 텍스트) lớn nhưng dùng CPU.

Không nén tệp (file / 파일) đã compressed hoặc tiny payload vô ích.

Measure mạng (network / 네트워크) vs CPU sự đánh đổi (trade-off / 트레이드오프).

---

# 108. bản địa (native / 네이티브) ảnh (image / 이미지) vs JVM

Bản địa (native / 네이티브) ảnh (image / 이미지) tốt cho cold start/autoscaling footprint. JVM JIT thường rất mạnh cho long-running thông lượng (throughput / 처리량).

Một nền tảng (platform / 플랫폼) có dịch vụ (service / 서비스) chạy 24/7 và bộ nhớ (memory / 메모리) dư có thể không cần bản địa (native / 네이티브). Serverless/CLI có thể benefit lớn.

Cấp cao (senior / 시니어) chọn theo triển khai (deployment / 배포) economics, không hype.

---

# 109. Testing kiến trúc (architecture / 아키텍처)

Một healthy suite có nhiều plain đơn vị (unit / 단위) tests cho nghiệp vụ (business / 비즈니스), slice tests cho khung phần mềm (framework / 프레임워크) boundaries, tích hợp (integration / 통합) tests với real DB/bên ngoài (external / 외부) fakes và ít full end-to-end tests.

Không cần ratio cố định. Mỗi kiểm thử (test / 테스트) phải trả lời câu hỏi cụ thể.

---

<!-- SPRING_BATCH4_TEST_SENIOR -->

> **Chuyển mạch:** Troubleshooting theo symptom → layer → evidence cho biết cần quan sát ở đâu; architecture testing tiếp tục bằng cách mô phỏng đúng failure tại boundary. Hai phần cùng kiểm tra khả năng vận hành, không chỉ happy path.

## Testing kiến trúc (architecture / 아키텍처) phải mô phỏng đúng thất bại (failure / 실패) ranh giới (boundary / 경계)

Một bộ kiểm thử (test suite / 테스트 스위트) production-grade không được dùng một kiểu kiểm thử (test / 테스트) cho mọi thứ. nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) nên được ép qua plain đơn vị (unit / 단위)/thuộc tính (property / 속성) tests; persistence tính đồng thời (concurrency / 동시성) cần real cơ sở dữ liệu (database / 데이터베이스) vì locking/isolation khác H2; HTTP adapter cần đặc tả hợp đồng (contract / 계약)/stub máy chủ (server / 서버) để kiểm headers, hết thời gian chờ (timeout / 타임아웃) và lỗi (error / 오류) ánh xạ (mapping / 매핑); bảo mật (security / 보안) cần kiểm thử (test / 테스트) cả unauthenticated, authenticated-but-forbidden và đối tượng (object / 객체) quyền sở hữu (ownership / 소유권); giao dịch (transaction / 트랜잭션)/outbox cần kiểm thử (test / 테스트) lần ghi nhận (commit / 커밋) thật.

Ngữ cảnh (context / 맥락) caching là một phần hiệu năng kiểm thử (test / 테스트). Profiles, động (dynamic / 동적) properties, bean overrides và cấu hình (configuration / 구성) classes tham gia bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자). `@DirtiesContext` làm ngữ cảnh (context / 맥락) bị loại khỏi bộ nhớ đệm (cache / 캐시) và nên được coi là expensive thao tác (operation / 연산). Nếu một kiểm thử (test / 테스트) cần mutate toàn cục (global / 전역) singleton trạng thái (state / 상태) rồi dirties ngữ cảnh (context / 맥락) để cleanup, đó có thể là phản hồi (feedback / 피드백) rằng môi trường vận hành (production / 운영 환경) thiết kế (design / 설계) có toàn cục (global / 전역) mutable trạng thái (state / 상태) khó cô lập.

Testcontainers tăng fidelity nhưng không phải lý do đưa mọi đơn vị (unit / 단위) kiểm thử (test / 테스트) vào Docker. Hãy dùng bộ chứa (container / 컨테이너) ở ranh giới (boundary / 경계) nơi engine ngữ nghĩa (semantics / 의미론) quan trọng: PostgreSQL JSON/locking/chỉ mục (index / 인덱스) hành vi (behavior / 동작), Kafka broker giao thức (protocol / 프로토콜), Redis TTL/serialization. kiểm thử (test / 테스트) nhanh ở inner vòng lặp (loop / 루프) và realistic ở tích hợp (integration / 통합) ranh giới (boundary / 경계) là hai mục tiêu bổ sung nhau.
<!-- SPRING_BATCH4_TEST_SENIOR_END -->

---

# 110. Transactional Tests Pitfall

`@Transactional` kiểm thử (test / 테스트) quay lui (rollback / 롤백) sau kiểm thử (test / 테스트) tiện cleanup, nhưng có thể che commit-time các ràng buộc (constraints / 제약조건들), after-commit listeners và lazy-loading hành vi (behavior / 동작).

Mã (code / 코드) môi trường vận hành (production / 운영 환경) giao dịch (transaction / 트랜잭션) closed trước serialization nhưng kiểm thử (test / 테스트) giao dịch (transaction / 트랜잭션) vẫn open có thể làm kiểm thử (test / 테스트) pass và môi trường vận hành (production / 운영 환경) thất bại (fail / 실패).

Use transactional tests intentionally.

---

# 111. Testcontainers và môi trường vận hành (production / 운영 환경) Engine

Repository kiểm thử (test / 테스트) với real PostgreSQL bắt được JSONB cú pháp (syntax / 문법), locking, sequences và dialect differences H2 bỏ sót.

Migrations cũng được kiểm thử (test / 테스트).

Kiểm thử tích hợp (integration test / 통합 테스트) chậm hơn đơn vị (unit / 단위), nhưng confidence đúng tầng (layer / 계층).

---

# 112. đặc tả hợp đồng (contract / 계약) Testing

HTTP máy khách (client / 클라이언트) adapter có đặc tả hợp đồng (contract / 계약) với bên ngoài (external / 외부) API. kiểm thử (test / 테스트) đường đi của yêu cầu (request path / 요청 경로), headers, serialization, lỗi (error / 오류) ánh xạ (mapping / 매핑) và hết thời gian chờ (timeout / 타임아웃) hành vi (behavior / 동작) against stub/mock máy chủ (server / 서버).

Repository cổng (port / 포트) có ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약); fake/JPA implementations nên giữ hành vi (behavior / 동작) expected.

---

# 113. bản địa (native / 네이티브) Executable Testing

AOT/bản địa (native / 네이티브) ảnh (image / 이미지) có closed-world differences. Reflection/tài nguyên (resource / 자원) paths chỉ chạy trong môi trường vận hành (production / 운영 환경) cần được kiểm thử (test / 테스트) actual bản địa (native / 네이티브) sản phẩm tạo ra (artifact / 산출물).

Tracing tác nhân (agent / 에이전트)/hints không thay coverage.

---

# 114. ngôn ngữ (language / 언어) Idioms cấp cao (senior / 시니어)

**khung phần mềm (framework / 프레임워크) at the edge.** nghiệp vụ (business / 비즈니스) objects không cần Spring phụ thuộc (dependency / 의존성) vô lý.

**giao dịch (transaction / 트랜잭션) at use-case ranh giới (boundary / 경계).** Atomic DB chính sách (policy / 정책) gần nghiệp vụ (business / 비즈니스) thao tác (operation / 연산).

**Bounded everything.** hết thời gian chờ (timeout / 타임아웃), hàng đợi (queue / 큐), pool, bộ nhớ đệm (cache / 캐시), payload, thử lại (retry / 재시도) đều có giới hạn.

**tường minh (explicit / 명시적) side effects.** DB/HTTP/message boundaries dễ nhìn.

**Measure before optimize.** JFR/dấu vết (trace / 추적)/metrics/DB plan trước tuning.

**Stable bên ngoài (external / 외부) contracts.** DTO/sự kiện (event / 이벤트)/lỗi (error / 오류) codes không phụ thuộc thực thể (entity / 엔터티)/vendor lớp (class / 클래스).

---

# 115. Programming Patterns cấp cao (senior / 시니어)

**Transactional Outbox** cho DB + message intent. **Idempotency** cho thử lại (retry / 재시도)/message/payment. **Bulkhead** cho scarce resources. **thử lại (retry / 재시도) + Backoff + Jitter** cho transient thất bại (failure / 실패). **Deadline Propagation** cho độ trễ (latency / 지연 시간) ngân sách (budget / 예산). **bộ nhớ đệm (cache / 캐시) Aside/Single Flight** cho bộ nhớ đệm (cache / 캐시). **Anti-Corruption tầng (layer / 계층)** cho vendor ranh giới (boundary / 경계). **CQRS-lite** cho optimized read các mô hình (models / 모델들). **Graceful Shutdown** cho triển khai (deployment / 배포). **Optimistic tính đồng thời (concurrency / 동시성)** cho concurrent edits.

---

# 116. thiết kế (design / 설계) Patterns trong Spring cấp cao (senior / 시니어)

Proxy là nền của AOP/giao dịch (transaction / 트랜잭션)/bảo mật (security / 보안)/bộ nhớ đệm (cache / 캐시)/async/declarative clients. chuỗi (chain / 사슬) of Responsibility thể hiện qua servlet/bảo mật (security / 보안)/interceptor chains. Adapter nằm ở MVC HandlerAdapter, persistence và bên ngoài (external / 외부) gateways. Observer liên hệ ứng dụng (application / 애플리케이션) events. Factory xuất hiện trong BeanFactory/FactoryBean. chiến lược (strategy / 전략) xuất hiện ở providers/handlers/policies. Front Controller là DispatcherServlet.

Ở cấp cao (senior / 시니어), mẫu (pattern / 패턴) quan trọng không phải tên mà là sự đánh đổi (trade-off / 트레이드오프): hidden điều khiển (control / 제어) luồng (flow / 흐름), testability, thứ tự (ordering / 순서) và vòng đời (lifecycle / 생명주기).

---

# 117. cấp cao (senior / 시니어) Mini dự án (project / 프로젝트): môi trường vận hành (production / 운영 환경) thứ tự (order / 순서) nền tảng (platform / 플랫폼)

Xây modular monolith gồm `order`, `payment`, `inventory`, `customer`, `notification`.

Thứ tự (order / 순서) creation dùng cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) để lưu thứ tự (order / 순서) + outbox. Một publisher background gửi tích hợp (integration / 통합) sự kiện (event / 이벤트). bên tiêu thụ (consumer / 소비자) simulation phải idempotent.

Payment adapter dùng RestClient/HTTP giao diện (interface / 인터페이스), hết thời gian chờ (timeout / 타임아웃), lỗi (error / 오류) taxonomy, idempotency key, bounded thử lại (retry / 재시도) và bulkhead.

JPA phải có optimistic locking, một read projection, một N+1 kiểm thử (test / 테스트)/fix và batch processing experiment.

Bảo mật (security / 보안) dùng OAuth2 tài nguyên (resource / 자원) máy chủ (server / 서버) JWT. Authorization cancel thứ tự (order / 순서) phải ở use-case ranh giới (boundary / 경계).

Khả năng quan sát (observability / 관측 가능성) gồm Actuator, Micrometer, tracing và custom checkout observation với low-cardinality tags.

Chạy kiểm thử tải (load test / 부하 테스트) nền tảng (platform / 플랫폼) threads vs virtual threads. Đo thông lượng (throughput / 처리량), p95/p99, DB pool waiting, CPU, bộ nhớ (memory / 메모리) và luồng thực thi (thread / 스레드) counts.

Bản dựng (build / 빌드) bản địa (native / 네이티브) ảnh (image / 이미지) experiment và so startup/RSS/steady-state thay vì tuyên bố winner.

---

# 118. cấp cao (senior / 시니어) → Master Supplement Gate

Bạn sẵn sàng sang Master Supplement khi có thể giải thích bằng nhân quả (causal / 인과적) luồng (flow / 흐름), không dùng câu “Spring tự làm”.

Với bộ chứa (container / 컨테이너), bạn phải hiểu definitions, post-processors, early bean creation và proxy chuỗi (chain / 사슬). Với AOP, bạn phải giải thích Advisor/MethodInterceptor, proxy types, self-invocation và thứ tự (ordering / 순서).

Với giao dịch (transaction / 트랜잭션), bạn phải phân biệt logical/vật lý (physical / 물리적) transactions, tài nguyên (resource / 자원) binding, rollback-only, REQUIRES_NEW tài nguyên (resource / 자원) impact và local-vs-distributed ranh giới (boundary / 경계).

Với JPA, bạn phải diagnose N+1/cartesian fetch, dirty checking chi phí (cost / 비용), batching, locking, pool sizing và OSIV sự đánh đổi (trade-off / 트레이드오프).

Với web, bạn phải chọn MVC nền tảng (platform / 플랫폼) threads, MVC virtual threads hay WebFlux dựa tải công việc (workload / 워크로드). Với reactive, hiểu vòng lặp sự kiện (event loop / 이벤트 루프)/backpressure/ngữ cảnh (context / 맥락).

Với bảo mật (security / 보안), phải dấu vết (trace / 추적) Servlet filter kiến trúc (architecture / 아키텍처), authentication manager/providers, JWT kiểm tra hợp lệ (validation / 검증), phương thức (method / 메서드) authorization, CSRF/CORS contexts.

Với môi trường vận hành (production / 운영 환경), phải giải thích outbox, idempotency, saga, bộ nhớ đệm (cache / 캐시) stampede, graceful shutdown, khả năng quan sát (observability / 관측 가능성) cardinality, AOT/bản địa (native / 네이티브) các ràng buộc (constraints / 제약조건들) và sự cố (incident / 인시던트) debugging.

---

# 119. Những gì cố ý để sang Master Supplement

Master Supplement sẽ không lặp ứng dụng (application / 애플리케이션) patterns. Nó sẽ đi vào **Spring nguồn (source / 소스)/framework-author mức (level / 수준)**: `DefaultListableBeanFactory`, configuration-class processing, `AutowiredAnnotationBeanPostProcessor`, auto-proxy creation internals, `AdvisedSupport/ProxyFactory`, `TransactionInterceptor` nguồn (source / 소스) luồng (flow / 흐름), `TransactionSynchronizationManager`, DispatcherServlet initialization, handler mappings/adapters registry, Boot auto-configuration import siêu dữ liệu (metadata / 메타데이터), custom starter authoring, Spring TestContext internals, AOT processors/thời gian chạy (runtime / 런타임) hints deeper, Spring 7 null-safety/JSpecify, Boot 4 modularization và Spring 7.1 preview/hiện tại (current / 현재) evolution.

Đó là tầng (layer / 계층) cần thiết nếu mục tiêu là “master Spring itself”, không chỉ cấp cao (senior / 시니어) Spring ứng dụng (application / 애플리케이션) engineer.

---

<!-- VERSION_DETAIL_PART3_2026-09-21_START -->
# Phiên bản (version / 버전) Deep Dive cho cấp cao (senior / 시니어): di chuyển (migration / 마이그레이션) và môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) theo generation

Đường di chuyển (migration / 마이그레이션) an toàn từ Boot 3 sang Boot 4 là đưa ứng dụng (application / 애플리케이션) lên **latest Boot 3.5.x trước**, xử lý deprecations/phụ thuộc (dependency / 의존성) conflicts rồi mới chuyển 4.x. Boot 4 loại bỏ nhiều API deprecated và đồng thời nâng major versions của portfolio projects.

Boot 4 có modular thiết kế (design / 설계) rõ hơn. Main modules và kiểm thử (test / 테스트) hạ tầng (infrastructure / 인프라) được tách theo technology, nhiều integrations có `spring-boot-starter-<technology>` và `spring-boot-starter-<technology>-test`. di chuyển (migration / 마이그레이션) phải rà soát (review / 검토) cả môi trường vận hành (production / 운영 환경) phụ thuộc (dependency / 의존성) cây (tree / 트리) lẫn kiểm thử (test / 테스트) phụ thuộc (dependency / 의존성) cây (tree / 트리).

Jackson 3 là breaking điểm (point / 지점) lớn. Boot 4 còn `spring-boot-jackson2` như stop-gap tính tương thích (compatibility / 호환성) mô-đun (module / 모듈) nhưng mô-đun (module / 모듈) này deprecated theo hướng loại bỏ trong tương lai. Custom serializers, mapper modules, polymorphic typing, persisted JSON và bảo mật (security / 보안) serialization cần kiểm thử (test / 테스트) riêng khi migrate.

Khung phần mềm (framework / 프레임워크) 7 dùng JSpecify và deprecated Spring null-safety annotations cũ trong `org.springframework.lang`. Với Java static phân tích (analysis / 분석) hoặc Kotlin, upgrade có thể tạo compile-time warnings/errors mới dù phương thức (method / 메서드) names gần như không đổi.

Khung phần mềm (framework / 프레임워크) 7 có bản địa (native / 네이티브) API-versioning hỗ trợ (support / 지원) cho MVC/WebFlux và `@Proxyable` từ 7.0. `@Proxyable` chỉ gợi ý proxy kiểu (type / 타입) nếu bean thật sự được auto-proxy; nó không tự tạo proxy.

Boot 4.1 bổ sung notable features gồm Spring gRPC hỗ trợ (support / 지원), Jackson cấu hình (configuration / 구성)/customization improvements, HTTP máy khách (client / 클라이언트) SSRF mitigation với `InetAddressFilter`, OpenTelemetry/khả năng quan sát (observability / 관측 가능성) enhancements và Log4j tệp (file / 파일) rotation hỗ trợ (support / 지원).

Spring bảo mật (security / 보안) cũng đã sang major generation 7. bảo mật (security / 보안) 6.5 là preparation line cho di chuyển (migration / 마이그레이션); hiện tại (current / 현재) docs tại thời điểm cập nhật liệt kê stable 7.1.1, 7.0.7 và 6.5.11. Khi dùng Boot, ưu tiên phiên bản (version / 버전) management của Boot trừ khi có lý do bảo mật (security / 보안)/tính tương thích (compatibility / 호환성) rõ và đã kiểm thử (test / 테스트) ma trận (matrix / 행렬).

Preview hiện tại là Boot 4.2.0-M1 + khung phần mềm (framework / 프레임워크) 7.1.0-M1. cấp cao (senior / 시니어)/Master nên đọc để biết direction nhưng không nên dạy milestone API như stable môi trường vận hành (production / 운영 환경) API.
<!-- VERSION_DETAIL_PART3_2026-09-21_END -->

---

# 120. phiên bản (version / 버전) References

Hiện tại (current / 현재) stable Boot hệ thống (system / 시스템) requirements: https://docs.spring.io/spring-boot/system-requirements.html

Spring AOP proxying: https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/cốt lõi (core / 핵심)/aop/proxying.html

Spring Transactions: https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/data-access/giao dịch (transaction / 트랜잭션).html

Spring MVC: https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/web/webmvc.html

Spring WebFlux: https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/web/webflux.html

Spring bảo mật (security / 보안): https://docs.spring.io/spring-security/tham chiếu (reference / 참조)/

Spring Boot Actuator: https://docs.spring.io/spring-boot/tham chiếu (reference / 참조)/actuator/

Spring bản địa (native / 네이티브) Images: https://docs.spring.io/spring-boot/tham chiếu (reference / 참조)/packaging/native-image/

Boot 4 di chuyển (migration / 마이그레이션): https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

> **Bàn giao:** Sau **Testing kiến trúc (architecture / 아키텍처) phải mô phỏng đúng thất bại (failure / 실패) ranh giới (boundary / 경계)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

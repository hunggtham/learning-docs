# Java Spring — Part 3: Senior
## Spring Framework 7 / Spring Boot 4 dưới góc nhìn kiến trúc, runtime, failure và production

> Part 3 không nhằm biến bạn thành người nhớ nhiều annotation hơn. Một Senior Spring engineer phải có khả năng thiết kế boundary, dự đoán failure mode, giải thích proxy/transaction/context, tìm bottleneck bằng evidence và xử lý production incident mà không đổ mọi thứ cho “Spring magic”.

---

# 1. Senior Spring là gì?

Ở Intermediate, bạn đã biết container tạo bean qua definitions và post-processors, AOP dùng proxy, MVC có dispatch pipeline, transaction có propagation và JPA có persistence context.

Ở Senior, câu hỏi thay đổi. Khi method có `@Transactional`, bạn phải đánh giá transaction có giữ connection quá lâu không, có remote call bên trong không, có `REQUIRES_NEW` khiến pool cạn không. Khi bật virtual threads, bạn phải hỏi DB connection pool, downstream concurrency và pinning chứ không chỉ nhìn thread count. Khi thêm cache, bạn phải hỏi stale tolerance và stampede. Khi publish event, bạn phải hỏi process crash giữa commit và publish. Khi latency p99 tăng, bạn phải biết lấy trace, JFR, DB metrics và thread dump để xây hypothesis.

Framework skill ở level Senior là **reasoning about boundaries and runtime consequences**.

---

# 2. Spring không thay kiến trúc của bạn

Spring có thể inject dependency nhưng không quyết định dependency direction có đúng không. Nó có thể mở transaction nhưng không biết business operation nào phải atomic. Nó có thể tạo REST controller nhưng không biết public API nên version thế nào. Nó có thể cache method nhưng không biết dữ liệu stale 30 giây có chấp nhận được không.

Vì vậy hãy phân biệt:

```text
Framework capability
≠
Architecture decision
```

Một hệ thống đầy `@Service`, `@Repository`, `@Transactional` vẫn có thể có coupling tệ, transaction sai và boundary mơ hồ.

**Language Idiom — Framework at the edges.** Domain/value objects và phần lớn business decisions nên có thể hiểu bằng Java bình thường. Spring annotations tập trung ở composition/infrastructure boundaries khi có thể.

---

# 3. Container startup dưới góc Senior

Startup không phải “scan rồi new beans”. Một application lớn có nhiều stages: environment/config data được chuẩn bị, configuration classes được parse, definitions được register, factory post-processors sửa metadata, bean post-processors được tạo, eager singletons được instantiate, dependencies resolved, initialization callbacks chạy, auto-proxy creators có thể wrap target, rồi lifecycle infrastructure mới start.

Khi startup chậm, bạn phải phân loại cost:

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

Đừng bật global lazy initialization như phản xạ. Nó giảm startup bằng cách chuyển lỗi sang first request.

---

# 4. Early Bean Creation và “not eligible for all BeanPostProcessors”

Một advanced startup bug xảy ra khi infrastructure bean trong lúc tạo post-processor lại yêu cầu application bean quá sớm. Bean đó được instantiate trước khi toàn bộ post-processors được register. Kết quả nó có thể không nhận proxy/advice mà bạn kỳ vọng.

Nếu log nói bean “not eligible for getting processed by all BeanPostProcessors” và transaction/AOP không chạy, hãy trace **ai kéo bean vào creation sớm**.

Đây là framework lifecycle problem, không sửa bằng thêm `@Transactional`.

---

# 5. BeanPostProcessor ordering và infrastructure coupling

Spring infrastructure dùng ordering contracts như `PriorityOrdered`, `Ordered` và `@Order`. Khi bạn tự viết nhiều custom post-processors phụ thuộc order, bạn đang xây mini-framework.

Application code bình thường không nên dùng post-processor để implement business feature. Vì post-processor chạy ở lifecycle layer, lỗi dễ ảnh hưởng toàn context và khó debug.

**Senior Rule.** Nếu một requirement có thể giải bằng explicit composition/bean configuration, ưu tiên nó trước metaprogramming.

---

# 6. Proxy chain là runtime architecture

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

Thứ tự này không chỉ performance; nó thay semantics.

Ví dụ retry **ngoài** transaction có thể tạo transaction mới cho từng attempt. Retry **trong** transaction có thể retry trong transaction đã rollback-only, vô nghĩa hoặc sai.

Cache ngoài security có thể cache response không phân biệt permission nếu key sai.

Khi một method có nhiều cross-cutting annotations, hãy vẽ interceptor stack.

---

# 7. Advisor, Pointcut, MethodInterceptor

Ở Spring AOP, một Advisor gắn advice với pointcut. Method interceptor có thể gọi `proceed()` để chuyển control tới interceptor tiếp theo hoặc target.

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

Transactions, observations và custom aspects có thể conceptually nằm trong chain kiểu này.

**Design Pattern.** Đây là Proxy + Chain of Responsibility/Interceptor.

---

# 8. JDK Proxy và CGLIB dưới góc API design

JDK proxy expose interfaces. Class-based proxy subclass target.

Nếu business API đã có interface ổn định, JDK proxy thường tự nhiên. Nếu codebase inject concrete types và cần advise concrete methods, class proxy có thể cần.

Class proxy có limitation với final/private methods vì subclass không override được.

Spring Framework 7 tiếp tục proxy-based Spring AOP và có thêm control finer-grained như `@Proxyable` cho per-bean proxy choice trong current generation.

Senior không nên ép toàn project sang một proxy type vì benchmark blog. Hãy thiết kế public abstraction trước.

---

# 9. Self-invocation là dấu hiệu boundary, không chỉ technical caveat

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

Technical fix có thể dùng self proxy, nhưng architecture fix thường tốt hơn: `AuditService` là collaborator có transaction policy riêng.

**Programming Pattern — Policy boundary as collaborator.** Khi hai methods cần proxy policies khác nhau, đó thường là dấu hiệu chúng đại diện hai execution boundaries khác nhau.

---

# 10. Transaction Internals: từ annotation tới resource

Declarative transaction flow:

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

Với JDBC, physical connection thường được lấy từ DataSource và gắn với execution context để repositories trong cùng transaction dùng cùng transactional connection.

Hiểu điều này giải thích vì sao transaction historically thread-bound và vì sao async execution không tự động “mang transaction theo”.

---

# 11. Physical transaction và logical scopes

Outer REQUIRED và inner REQUIRED có hai logical annotation scopes nhưng thường chia sẻ một physical DB transaction.

Nếu inner làm transaction rollback-only, outer catch exception không thể biến physical transaction thành committable. Commit outer sẽ fail/rollback.

`UnexpectedRollbackException` tồn tại để application không nhận false success.

Senior phải xem logical call graph và physical resource cùng lúc.

---

# 12. `REQUIRES_NEW` và connection starvation

Giả sử connection pool 20. Có 20 concurrent requests, mỗi outer transaction giữ một connection. Mỗi request gọi inner `REQUIRES_NEW`, cần connection khác.

Tất cả 20 inner calls chờ connection, nhưng 20 connections đang bị chính outer transactions của chúng giữ.

Đây có thể tạo starvation/deadlock-like condition.

Do đó `REQUIRES_NEW` không phải “save independent cho chắc”. Nó có resource topology.

---

# 13. TransactionSynchronization và after-commit behavior

Spring transaction infrastructure hỗ trợ callbacks quanh commit/completion. `@TransactionalEventListener` tận dụng transaction phase semantics ở high level.

Nhưng after-commit callback vẫn trong process. Nếu DB commit thành công và process chết trước khi durable message được publish, callback không cứu được.

Đây là boundary giữa **local transaction synchronization** và **distributed reliability**.

---

# 14. Transaction với nhiều DataSources

Nếu application có `primaryDataSource` và `auditDataSource`, mỗi cái có local transaction manager riêng.

```java
@Transactional("primaryTxManager")
```

không làm audit DB join atomic transaction một cách thần kỳ.

Hai local transactions:

```text
DB A commit
DB B fail
```

vẫn có partial result.

Muốn atomic distributed transaction cần JTA/XA hoặc thường trong modern services dùng eventual consistency/business patterns như outbox/saga tùy requirement.

---

# 15. Keep DB Transactions Short

Một transaction nên giữ locks/connections chỉ cho phần cần atomic.

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

Nếu payment mất 5 giây, connection bị giữ 5 giây. Nếu shipping fail sau payment success, DB rollback không undo payment external.

Senior thiết kế local transaction + durable state transition/outbox, rồi external effects có retry/idempotency.

---

# 16. Isolation không thể hiểu chỉ bằng enum Spring

`Isolation.READ_COMMITTED` là intent mapping. Actual phenomena phụ thuộc database MVCC/locking implementation.

Bạn phải biết database đang dùng. PostgreSQL READ COMMITTED, MySQL InnoDB semantics và Oracle có khác biệt.

Spring chỉ truyền isolation policy xuống transaction resource; nó không định nghĩa database physics.

---

# 17. Database deadlock và Spring

Deadlock xảy ra khi transactions giữ lock theo cycle.

Ví dụ transaction A update Order rồi Payment; transaction B update Payment rồi Order.

DB phát hiện cycle và abort một transaction.

Application mitigation gồm consistent lock ordering, transaction ngắn, index đúng để tránh lock nhiều rows, retry carefully với idempotency.

Đừng chỉ tăng timeout.

---

# 18. JPA Persistence Context như Unit of Work

Persistence context giữ managed entities, identity map và pending changes.

Senior phải quan tâm **kích thước** context.

Nếu load 100.000 entities rồi update trong một transaction, context giữ reference và dirty-check metadata cho toàn bộ. Memory tăng, flush chậm.

Batch processing thường cần chunk:

```text
load/persist batch
→ flush
→ clear
→ repeat
```

hoặc dùng bulk SQL nếu business logic cho phép.

---

# 19. Dirty Checking cost và side effects

Dirty checking tiện vì bạn chỉ mutate managed entity. Nhưng sự tiện này có hidden SQL.

Mapper hoặc helper vô tình call setter trên managed entity có thể tạo update khi transaction flush.

Do đó entity mutation API nên có semantic rõ:

```java
order.cancel(reason);
```

thay vì public setters mọi field.

---

# 20. Flush Timing và Query interaction

JPA provider có thể flush trước query nếu cần đảm bảo query thấy pending changes.

Bạn có thể thấy SQL UPDATE xảy ra giữa method trước commit và tưởng framework “commit sớm”. Thực ra đó có thể là flush.

Debug JPA phải phân biệt:

```text
SQL execution
transaction commit
```

---

# 21. N+1 ở production

N+1 không chỉ làm “nhiều query”. Nó tăng DB round trips, connection occupation, CPU parsing/execution và p99 latency.

Một endpoint local test với 5 orders có vẻ nhanh. Production user có 500 orders sẽ tạo 501 queries.

Bạn phải instrument query counts/tracing/SQL metrics thay vì chờ user complain.

---

# 22. Fetch Join và Cartesian Explosion

Order có 10 items và 5 payments. Join fetch cả hai collections có thể tạo 50 result rows cho một order.

ORM de-duplicate object graph nhưng DB/network đã xử lý 50 rows.

Nếu thêm third collection, multiplication tăng mạnh.

Senior không “fetch join everything”. Có thể dùng multiple queries, projections hoặc batch fetching.

---

# 23. Pagination và Fetch Collection

Database pagination áp lên rows, nhưng collection fetch join nhân rows. ORM có thể không thể paginate entity roots đúng bằng SQL offset/limit hoặc phải xử lý memory.

Common strategy:

```text
page root IDs
→ fetch details by IDs
```

hoặc projection/keyset pagination.

---

# 24. DTO Projection và CQRS-lite

Một order detail command flow cần rich entity/domain model. Một dashboard chỉ cần order ID, customer name, total, status.

Không cần hydrate toàn graph rồi serialize.

Projection query:

```java
record OrderSummary(
    Long id,
    String customer,
    BigDecimal total,
    OrderStatus status) {
}
```

Read model tối ưu riêng là pragmatic CQRS-lite, không cần dựng event sourcing.

---

# 25. JPA Batch Inserts

Batching phụ thuộc Hibernate/JDBC settings, ID generation và flush pattern.

`IDENTITY` có thể hạn chế insert batching vì ID cần DB round trip sớm tùy provider.

Nếu performance matters, đo SQL/batch behavior trên actual DB.

Không copy `hibernate.jdbc.batch_size=1000` mà chưa measure transaction/memory/DB packet effects.

---

# 26. Bulk Update và stale Persistence Context

JPQL bulk update:

```jpql
update User u
set u.active = false
where u.lastLogin < :cutoff
```

bypass normal entity dirty checking.

Nếu context đã có `User` managed, object memory có thể vẫn `active=true` dù DB changed.

Sau bulk operation cần clear/refresh strategy phù hợp.

---

# 27. Optimistic Locking là business conflict

`@Version` failure không nhất thiết 500.

Hai users cùng sửa same resource là expected concurrent conflict.

API có thể map thành `409 Conflict`, prompt client reload hoặc retry if operation safely retryable.

Retry tự động mọi optimistic lock failure có thể ghi đè user intent nếu merge semantics không rõ.

---

# 28. Connection Pool là Bulkhead

Connection pool không chỉ optimization để reuse connections. Nó giới hạn số concurrent DB operations.

App có 10 instances × pool 100 = up to 1000 DB connections. Database có thể chỉ handle tốt 200.

Virtual threads không thay đổi DB capacity.

**Programming Pattern — Bulkhead.** Pool bảo vệ scarce downstream resource.

---

# 29. Pool Timeout không đồng nghĩa Pool quá nhỏ

Khi threads chờ connection quá lâu, nguyên nhân có thể là slow queries, transaction giữ connection trong HTTP calls, lock contention hoặc connection leak.

Tăng pool có thể làm DB overloaded hơn.

Senior workflow: nhìn active/pending connection, acquisition latency, query latency, transaction duration và DB CPU/locks.

---

# 30. MVC với Platform Threads

Classic servlet application có request mapped lên platform thread từ container pool. Blocking JDBC/HTTP làm thread chờ.

Capacity roughly bound bởi thread pool và downstream resources.

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

blocking-style request có thể chạy trên lightweight virtual threads.

Điều này làm high concurrent I/O dễ scale mà vẫn giữ imperative code.

Nhưng CPU-bound operation không nhanh hơn. DB pool, remote API concurrency và file descriptors vẫn hữu hạn.

Boot 4.1 docs hiện khuyến nghị modern JDK versions cho trải nghiệm virtual thread tốt hơn; pinned virtual thread có thể được quan sát qua JFR/jcmd.

---

# 32. Pinning

Một virtual thread có thể bị pinned vào carrier trong một số blocking/monitor/native scenarios tùy JDK version.

Không sửa bằng “remove synchronized everywhere”. Hãy đo.

JFR virtual-thread events và tooling giúp xem workload có pinning đáng kể không.

Modern JDK đã cải tiến virtual thread/synchronized interaction qua releases, vì vậy đừng dùng advice Java 21 ban đầu như chân lý mãi mãi.

---

# 33. Request Deadline thay vì nhiều Timeout rời rạc

Client cho bạn SLA 2 giây.

Nếu service A đặt DB timeout 5s, payment 5s, inventory 5s và retry 3 lần, request không thể tôn trọng 2s.

Senior design dùng budget:

```text
incoming deadline
→ local processing budget
→ downstream remaining budget
```

Một downstream call bắt đầu ở 1.8s không nên có 5s timeout.

---

# 34. Streaming Response

Nếu export 5GB file, không đọc toàn bộ thành byte array rồi trả.

Streaming giữ memory bounded nhưng resource lifecycle khó hơn: client disconnect, file close, transaction boundary và backpressure.

Không giữ JPA transaction mở hàng phút để stream lazy entity rows nếu có lựa chọn tốt hơn.

---

# 35. Request Payload Limits

Public endpoint cần limit JSON/multipart/header sizes ở server/framework/gateway layers.

Unbounded upload có thể gây memory/disk exhaustion.

File upload còn cần sanitize filename/path, validate content và storage isolation.

---

# 36. WebFlux là execution model khác

WebFlux dựa trên Reactive Streams và non-blocking/event-loop-friendly architecture.

Bạn không học WebFlux bằng cách đổi:

```java
User
```

thành:

```java
Mono<User>
```

rồi giữ mọi blocking JPA call.

Nếu event loop thread gọi JDBC blocking, nó chặn nhiều requests cùng share loop.

---

# 37. Mono và Flux

`Mono<T>` biểu diễn 0 hoặc 1 item async stream. `Flux<T>` biểu diễn 0..N.

Pipeline được build trước rồi work thường xảy ra khi subscribe.

```java
webClient.get()
    .retrieve()
    .bodyToMono(User.class)
    .map(this::toDomain);
```

Nếu subscribe nhiều lần vào cold publisher, work có thể chạy nhiều lần.

---

# 38. `map` vs `flatMap` trong Reactor

`map` biến value synchronously:

```text
User → UserResponse
```

`flatMap` dùng khi function trả publisher:

```text
UserId → Mono<User>
```

Unconstrained `flatMap` có thể tăng concurrency và reorder results. `concatMap` giữ sequence hơn nhưng giảm concurrency.

Concurrency operator cũng là capacity decision.

---

# 39. Backpressure

Reactive Streams subscriber báo demand. Producer không nên phát vô hạn khi consumer chậm.

Backpressure là protocol first-class, khác việc tạo million futures rồi để memory queue.

Nếu problem cần streaming data và end-to-end reactive support, WebFlux có lợi thế thật. Nếu CRUD blocking/JPA, MVC + virtual threads có thể đơn giản hơn.

---

# 40. Reactor Context

Reactive execution có thể hop threads nên ThreadLocal không đủ reliable cho request metadata.

Reactor Context đi cùng subscriber/pipeline.

Tracing/security reactive integrations phải propagate context theo reactive model.

Đây là lý do copy blocking/thread-local patterns vào WebFlux gây bugs.

---

# 41. R2DBC không phải Reactive JPA

R2DBC cung cấp reactive relational access.

Nó không có traditional JPA persistence context/dirty checking/lazy loading model.

Nếu chuyển từ JPA sang R2DBC, bạn đang đổi programming model, không chỉ driver.

---

# 42. Chọn MVC, MVC+Virtual Threads hay WebFlux

MVC platform threads tốt khi hệ thống đơn giản, concurrency vừa và ecosystem blocking.

MVC + virtual threads rất hấp dẫn cho imperative, blocking I/O workload với concurrency cao.

WebFlux phù hợp khi end-to-end reactive, streaming/backpressure, reactive DB/client và event-loop model mang lợi ích rõ.

Không có “WebFlux luôn nhanh hơn”.

---

# 43. HTTP Client như Infrastructure Adapter

External Payment API không nên leak `RestClient` response types vào domain.

Domain port:

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

Vendor DTO/HTTP exceptions được translate thành domain/application concepts.

**Design Pattern — Anti-Corruption Layer.** Vendor model dừng ở boundary.

---

# 44. Remote Failure Taxonomy

HTTP dependency có thể fail ở DNS, connection, TLS handshake, pool acquisition, write, response timeout, 4xx, 5xx hoặc serialization.

Không map mọi thứ thành `PaymentException`.

Business rejection như card declined khác transient network failure. Retry policy phụ thuộc classification.

---

# 45. Retry đúng cách

Retry cần bốn điều: failure transient, operation idempotent hoặc được bảo vệ bằng idempotency key, attempts bounded, và delay/backoff/jitter nằm trong deadline.

Payment POST không có idempotency key mà retry sau timeout có thể charge hai lần vì client không biết server đã xử lý request trước khi response mất.

---

# 46. Circuit Breaker

Circuit breaker ngừng gửi request vào dependency đang fail liên tục.

States concept:

```text
CLOSED
→ failures threshold
OPEN
→ cooldown
HALF_OPEN
→ probe
```

Nó không thay retry. Retry cố lại operation; circuit breaker bảo vệ hệ thống khỏi hammering dependency fail.

Spring Core không ép một circuit-breaker implementation duy nhất; thường dùng resilience ecosystem libraries.

---

# 47. Bulkhead

Payment, report và notification nên có capacity riêng nếu một dependency có thể làm nghẽn tất cả workers/connections.

Implementation có thể là Semaphore, pool hoặc connection limit.

Virtual threads càng làm bulkhead quan trọng vì thread creation không còn là natural limiter.

---

# 48. Load Shedding

Khi system saturated, trả 429/503 sớm có thể tốt hơn queue 60 giây rồi timeout.

Load shedding là business/operational policy: request nào drop được, request nào phải persist, client retry ra sao.

---

# 49. Local Transaction không solve Distributed Transaction

Service A:

```text
DB transaction
→ call Service B
```

Service B không tự join transaction A qua HTTP.

Nếu cần cross-service consistency, dùng saga, outbox, idempotency hoặc distributed transaction technology tùy architecture.

Microservices đổi consistency model; Spring annotation không xóa network boundary.

---

# 50. Dual Write Problem

Code:

```text
save Order DB
commit
publish Kafka
```

process crash giữa commit và publish tạo missing event.

Nếu publish trước rồi DB rollback, consumer thấy event cho data không tồn tại.

Đây là dual-write problem.

---

# 51. Transactional Outbox

Trong **cùng local DB transaction**:

```text
insert/update Order
+
insert OutboxEvent
```

Commit đồng thời.

Separate publisher đọc outbox và publish broker.

Nếu publisher crash sau publish nhưng trước mark sent, event có thể publish lại. Consumer cần idempotency.

Outbox giải quyết durable intent, không tạo exactly-once end-to-end magic.

---

# 52. Idempotent Consumer

Message có `eventId`/business key.

Consumer lưu processed ID hoặc thực hiện state transition có uniqueness constraint để duplicate delivery không tạo duplicate effect.

At-least-once delivery + idempotent consumer là pattern phổ biến.

---

# 53. Saga

Cross-service flow:

```text
reserve inventory
→ authorize payment
→ create shipment
```

Nếu shipment fail, saga có thể trigger compensation:

```text
refund/release payment
release inventory
```

Compensation là business operation, không phải rollback database time machine.

---

# 54. Spring Application Event vs Integration Event

`ApplicationEvent` là in-process.

Integration event là cross-system contract.

Đừng serialize internal JPA entity rồi gọi đó là event contract.

Integration event cần stable schema/version evolution và payload chỉ chứa dữ liệu consumer cần.

---

# 55. Cache là Consistency System

Trước `@Cacheable`, hỏi source of truth, stale tolerance, TTL, max size, eviction, multi-node behavior và update ordering.

Nếu DB update commit nhưng cache eviction fail, cache stale.

Nếu cache updated trước DB commit rồi transaction rollback, cache chứa future state không tồn tại.

Transaction/cache interaction cần design.

---

# 56. Cache Stampede

Popular key hết hạn cùng lúc, 10.000 requests miss rồi cùng hit DB.

Mitigations: per-key single-flight, refresh-ahead, stale-while-revalidate, TTL jitter.

Cache provider có thể hỗ trợ một số mechanism, nhưng annotation Spring không tự giải quyết hết.

---

# 57. Local vs Distributed Cache

Local Caffeine-like cache rất nhanh nhưng mỗi instance có state riêng.

Distributed Redis-like cache nhất quán chia sẻ hơn nhưng thêm network latency, serialization, availability và cluster complexity.

Nếu stale 5 giây chấp nhận được, local TTL có thể đủ. Đừng dùng distributed cache chỉ vì app có nhiều instances nếu semantics không cần.

---

# 58. Spring Security Filter Architecture

Servlet request thường đi:

```text
Servlet container
→ DelegatingFilterProxy
→ FilterChainProxy
→ matching SecurityFilterChain
→ security filters
→ DispatcherServlet
```

`DelegatingFilterProxy` bridge servlet filter registration với Spring-managed security infrastructure.

`FilterChainProxy` chọn security chain phù hợp request.

Hiểu flow này quan trọng khi có multiple chains cho `/api/**`, `/admin/**`.

---

# 59. AuthenticationManager và AuthenticationProvider

Authentication filter tạo authentication request/token rồi gọi `AuthenticationManager`.

`ProviderManager` là common implementation phối hợp nhiều `AuthenticationProvider`.

Provider có thể authenticate password, JWT hoặc custom credential type.

Sau success, authenticated `Authentication` đi vào SecurityContext.

---

# 60. Multiple SecurityFilterChains

Bạn có thể có chain riêng:

```text
/api/**
→ OAuth2 Resource Server

/admin/**
→ stricter admin config
```

Matcher/order quyết định chain nào xử lý request.

Mis-order có thể khiến request rơi vào default chain.

Security debug nên trace matcher + filter chain, không chỉ controller.

---

# 61. JWT Resource Server

Spring Security có OAuth2 Resource Server support để validate JWT từ authorization server.

Config issuer:

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://idp.example.com
```

Framework có thể discover keys/metadata và verify signature/issuer/timestamps theo configuration.

Production authorization còn phải quan tâm audience và mapping claims/scopes đúng application.

---

# 62. JWT không phải Encryption

Signed JWT payload thường đọc được.

Không đặt password/secret vì nghĩ “token encoded nên private”.

Signature bảo integrity/authenticity theo key/algorithm, không tự mã hóa confidentiality.

---

# 63. Scope, Authority và Role

OAuth scope đại diện permission delegated cho token/client. Application authorities/roles là model authorization của app.

Có thể map scope thành authority, nhưng đừng coi role và scope là universal same concept.

Complex ownership permission có thể cần domain authorization service.

---

# 64. CSRF và Cookie Authentication

Browser tự attach cookies vào cross-site requests, vì vậy state-changing cookie-authenticated applications cần CSRF protection.

Bearer token trong `Authorization` header không tự được browser attach theo same way, nên threat model khác.

Security policy phải xuất phát từ credential transport, không từ câu “đây là REST”.

---

# 65. Security Context và Async

Security context có execution-context propagation concerns. Nếu submit task sang arbitrary executor, principal không nhất thiết tự xuất hiện.

Spring Security có context propagation integrations, nhưng bạn phải biết execution boundary.

Reactive security lại dùng Reactor context model.

---

# 66. Observability: Metrics, Traces, Logs

Metrics trả lời “hệ thống đang xảy ra bao nhiêu/lâu bao nhiêu”. Traces trả lời “request cụ thể đi qua đâu”. Logs cho detailed events/context. JFR/profile cho runtime.

Không một nguồn nào đủ.

Khi p99 tăng, trace có thể chỉ downstream span chậm; DB metrics cho lock; JFR cho CPU/GC; logs cho error detail.

---

# 67. Micrometer Observation

Observation là abstraction cho operation instrumentation.

Concept:

```text
Observation
→ context
→ handlers
→ metrics/tracing
```

Một custom business operation `order.checkout` có low-cardinality tags như channel/payment type và high-cardinality trace fields như orderId.

---

# 68. Metric Cardinality

Đừng tag metric:

```text
userId
orderId
raw URL with IDs
traceId
```

Mỗi unique value tạo time series.

Metrics backend có thể chết vì cardinality explosion dù app vẫn chạy.

High-cardinality identifiers thuộc logs/traces.

---

# 69. Distributed Tracing và Context Propagation

Request vào service A có trace/span context, HTTP client phải propagate headers sang B. Async task cũng cần context propagation.

ThreadLocal-only model không đủ cho reactive thread hops. Virtual threads thay đổi thread quantity nhưng mỗi request có thể vẫn thread-confined khá tự nhiên tùy design.

Senior phải hiểu library/framework đang dùng context mechanism nào.

---

# 70. Actuator Management Surface

Endpoints như `env`, `configprops`, `mappings`, `heapdump`, `threaddump` có diagnostic value nhưng có thể lộ secrets/internal topology.

Management network/security phải được thiết kế riêng.

Không expose `/actuator/**` public vì “chỉ dev biết URL”.

---

# 71. Health Check Semantics

Readiness nên phản ánh khả năng phục vụ traffic. Liveness chỉ fail nếu process state hỏng và restart có ích.

Nếu DB down, readiness false hợp lý. Liveness false có thể khiến tất cả pods restart đồng loạt, làm incident tệ hơn.

Health indicator phải bounded; không probe dependency với unbounded network call.

---

# 72. `@Async` trong Production

Fire-and-forget `@Async void` cho email marketing có thể chấp nhận nếu mất một task không critical.

Nhưng payment, legal audit hoặc shipment creation cần durability. In-memory task mất khi pod crash/redeploy.

Nếu operation business-critical, message/job queue durable thường phù hợp hơn.

---

# 73. Executor Capacity

Platform ThreadPoolTaskExecutor có core/max/queue. Queue unbounded hide overload.

CallerRuns/rejection hoặc bounded queues làm overload visible.

Virtual thread per task bỏ scarce-thread pool, nhưng bạn vẫn phải add Semaphore/bulkhead cho downstream limit.

---

# 74. Scheduled Jobs trong Cluster

`@Scheduled` chạy trên mỗi JVM.

Nếu có 5 replicas, 5 executions.

Nếu job là cleanup idempotent và parallel-safe có thể okay. Nếu monthly billing phải exactly one logical run, cần leader/distributed lock/job platform.

---

# 75. Graceful Shutdown

Deployment không chỉ “Spring context close”.

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

Configure shutdown timeout phù hợp max request/task duration và Kubernetes termination grace period.

---

# 76. Startup Performance

Startup time matters trong autoscaling/serverless/container rollout.

Measure sources:

```text
component/config processing
JPA boot
Flyway
network discovery
bean init
classloading
```

Spring provides startup instrumentation facilities and Boot condition info.

Fix actual bottleneck, không blindly turn everything lazy.

---

# 77. AOT Processing

Spring AOT analyzes application ahead of runtime và generate code/metadata/hints.

AOT không đồng nghĩa native image. Nó có thể phục vụ optimized startup modes và GraalVM native workflow.

Dynamic reflection/proxy/resource behavior phải được known/inferred ahead of time hơn.

---

# 78. GraalVM Native Image

Native image compile application thành native executable.

Lợi ích thường là startup nhanh và memory footprint thấp hơn. Trade-off là build time/complexity, closed-world constraints và khác biệt runtime performance so JVM JIT.

Đừng benchmark 1 request rồi kết luận native tốt hơn toàn diện.

---

# 79. RuntimeHints

Custom dynamic feature có thể cần hints:

```text
reflection
resources
serialization
JDK proxies
```

Spring AOT tự infer nhiều standard Spring cases. Custom reflection/metaprogramming có thể cần `RuntimeHintsRegistrar`.

Native deployment phải test actual executable.

---

# 80. Boot 4 và Jackson 3

Spring Boot 4 ưu tiên Jackson 3. Jackson 3 thay group/package cho nhiều modules (`tools.jackson` generation), trong khi annotations có compatibility specifics.

Nếu code chỉ dùng normal DTO + Boot auto-config, migration dễ hơn.

Nếu bạn inject/customize Jackson internal types everywhere, migration lớn hơn.

**Senior Pattern.** Depend on stable framework/application abstractions, không leak third-party implementation sâu khắp domain.

---

# 81. Boot 3 → Boot 4 Migration

Không nhảy blind.

Nên đưa project lên latest 3.5 first, xử lý deprecations, dependencies và tests, rồi Boot 4.

Boot 4 yêu cầu Spring Framework 7, Jakarta EE 11/Servlet 6.1 baseline và có dependency/module changes. Jackson 3 là change lớn.

Migration test phải cover startup, web serialization, security, JPA/data, custom auto-config và observability agents.

---

# 82. Linkage Errors khi Upgrade

`NoSuchMethodError`, `NoClassDefFoundError`, `AbstractMethodError` thường chỉ compile/runtime dependency mismatch.

Ví dụ app compile với library v2 nhưng runtime load v1.

Use:

```bash
./mvnw dependency:tree
```

và inspect actual packaged artifact/classloader.

Đừng chữa bằng random `clean` mãi.

---

# 83. Modular Monolith

Microservices không phải default “Senior architecture”.

Một Spring Boot deployment có modules `order`, `payment`, `inventory`, `customer` với boundary rõ có nhiều lợi ích: local transaction dễ, operations đơn giản, refactor nhanh.

Module communication nên qua public application APIs/events, không import repository/entity internals tùy tiện.

---

# 84. Package Boundary

Feature module có thể expose:

```java
public interface OrderApplication {
    OrderResult place(
        PlaceOrderCommand command);
}
```

Internal adapters/repositories package-private hoặc internal package.

Dependency direction phải enforce bằng architecture tests/modulith tooling khi project lớn.

Folder names không đủ.

---

# 85. Spring Modulith Awareness

Spring Modulith cung cấp support để model application modules, verify dependencies, test module và document architecture/event interactions.

Nó hữu ích cho modular monolith, nhưng không thay việc thiết kế bounded responsibilities.

Master Supplement sẽ đi sâu hơn nếu cần.

---

# 86. Hexagonal Architecture với Spring

Core defines ports:

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

Lợi ích là domain/application không phụ thuộc trực tiếp HTTP/JPA/vendor.

Đừng tạo 5 layers interfaces cho CRUD trivial chỉ để “clean architecture”. Architecture complexity phải proportional problem complexity.

---

# 87. Anti-Corruption Layer

External vendor payment có model:

```text
VendorPaymentStatus
VendorMoney
VendorErrorCode
```

Không để chúng đi xuyên application.

Adapter map:

```text
VendorResponse
→ PaymentResult
```

Khi đổi vendor, domain ít đổi.

---

# 88. Transaction Script vs Rich Domain

Simple admin CRUD có thể dùng service methods + repository, gọi là transaction-script style.

Complex order/pricing/risk domain có thể cần value objects, entities và invariants.

Senior không force DDD cho todo app và cũng không để complex banking rules thành 2.000-line service.

---

# 89. Annotation Soup

Method:

```java
@Transactional
@Async
@Cacheable
@PreAuthorize
@Observed
@Retryable
public Result execute() { ... }
```

là signal cần review.

Bạn phải giải thích exact ordering, thread, transaction, retry, cache và security context. Nếu không, split responsibilities/policies.

Spring annotations giảm boilerplate nhưng có thể tăng hidden control flow.

---

# 90. God Service

`OrderService` 3.000 lines có business, email, SQL, file, HTTP, cache và reporting là low cohesion.

Tách theo use case/capability, không chỉ tách thành `OrderServiceHelper`.

Dependency count, change reasons và test setup cho thấy boundaries.

---

# 91. Static ApplicationContext Holder

Pattern:

```java
SpringContext.getBean(Foo.class)
```

cho phép bất kỳ code nào kéo dependency global.

Nó biến DI thành Service Locator và phá dependency visibility.

Chỉ dùng trong integration constraints rất đặc biệt, không làm default architecture.

---

# 92. Entity Everywhere

Nếu `UserEntity` dùng làm API DTO, Kafka message, cache value, domain object và batch format, mọi schema/persistence change có blast radius lớn.

Tách representation ở boundaries có lifecycle/compatibility khác nhau.

---

# 93. Production Debugging: `@Transactional` không chạy

Checklist reasoning:

Bean có do Spring quản lý không? Call có đi qua proxy không? Method có proxyable không? Transaction manager đúng không? Annotation đặt ở method/class mà proxy metadata resolve được không? Exception bị catch/swallow không? Rollback rule có phù hợp không?

Enable targeted transaction logs nếu cần và observe DB connection/commit behavior. Đừng thêm annotation thứ hai.

---

# 94. Production Debugging: N+1

Trace endpoint. Count SQL per request. Xem serialization có access lazy relation. Check OSIV. Check mapper loops. Xem fetch graph/query.

Fix bằng fetch plan/projection, rồi measure query count/p99 lại.

Không chỉ nhìn “endpoint chậm” và tăng CPU.

---

# 95. Production Debugging: DB Pool Exhausted

Check pool pending/acquisition time, active count, transaction duration, slow queries, locks và remote calls trong transaction.

Thread dump có thể cho thấy nhiều requests đang wait connection.

Tăng max pool chỉ sau khi biết DB còn capacity.

---

# 96. Production Debugging: CPU 100%

Use JFR/profile. Check hot Java stacks, JSON serialization, crypto, regex, GC CPU, busy loop, ORM mapping.

Spring Actuator metrics cho symptom; JFR cho execution detail.

---

# 97. CPU thấp nhưng Latency cao

Đây thường là waiting problem:

```text
DB lock/query
connection pool
remote HTTP
DNS
filesystem
thread lock
queue
```

Distributed trace và thread dump rất hữu ích.

---

# 98. Memory Growth

Possible application causes:

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

Heap dump/JFR/JVM tools cần phối hợp. RSS cao nhưng heap bình thường có thể là native/direct/thread stack issue từ Java Core.

Spring không thay JVM memory model.

---

# 99. Security Incident Reasoning

401/403 cần trace security chain, authentication mechanism và authorization decision.

CORS browser error có thể che backend 401/403.

JWT issue cần check signature keys, issuer, audience, clock skew/expiry và claim mapping.

Không disable security để “xác nhận endpoint”.

---

# 100. Logging và Sensitive Data

Request/response body logging có thể leak password/token/PII, tăng memory vì buffering và phá streaming.

Production logging nên structured, redact fields và sample large/high-frequency data khi cần.

Expected 404 không nhất thiết ERROR stack trace.

---

# 101. SSRF trong RestClient/WebClient

Nếu endpoint cho user nhập URL và server fetch:

```text
https://...
```

attacker có thể target internal metadata service/localhost/private network.

Restrict allowed schemes/hosts/ports, DNS/IP ranges và redirects theo threat model.

Spring client API không tự làm business allow-list.

---

# 102. Deserialization Security

Public JSON không nên cho uncontrolled polymorphic type instantiation.

Bound request size/depth và control allowed types.

DTO boundaries giảm mass assignment và deserialization attack surface.

---

# 103. Supply Chain

Spring app kéo nhiều transitive dependencies. Theo dõi Boot maintenance line, CVEs, SBOM/dependency scanning.

Đừng override managed versions tùy tiện rồi vô tình kéo incompatible/security-old transitive graph.

---

# 104. Performance Engineering

Senior optimization loop:

```text
define SLO
→ load/measure
→ identify bottleneck
→ hypothesis
→ change
→ measure again
```

“WebFlux nhanh”, “native nhanh”, “virtual thread nhanh”, “JPA chậm” đều là slogans nếu không gắn workload.

---

# 105. Tail Latency

Average 100ms có thể che p99 3s.

External service, GC, DB lock và queueing thường làm tail.

Track p50/p95/p99 và correlate với dependency spans.

---

# 106. Pagination và Result Limits

Unbounded `/users` endpoint có thể trả millions rows, exhaust heap/DB.

Bound size.

Deep offset:

```sql
offset 1000000 limit 20
```

có thể đắt.

Keyset/cursor pagination dùng stable ordered key để seek tiếp, thường scale tốt hơn.

---

# 107. Compression

HTTP compression giảm bandwidth cho JSON/text lớn nhưng dùng CPU.

Không nén file đã compressed hoặc tiny payload vô ích.

Measure network vs CPU trade-off.

---

# 108. Native Image vs JVM

Native image tốt cho cold start/autoscaling footprint. JVM JIT thường rất mạnh cho long-running throughput.

Một platform có service chạy 24/7 và memory dư có thể không cần native. Serverless/CLI có thể benefit lớn.

Senior chọn theo deployment economics, không hype.

---

# 109. Testing Architecture

Một healthy suite có nhiều plain unit tests cho business, slice tests cho framework boundaries, integration tests với real DB/external fakes và ít full end-to-end tests.

Không cần ratio cố định. Mỗi test phải trả lời câu hỏi cụ thể.

---

# 110. Transactional Tests Pitfall

`@Transactional` test rollback sau test tiện cleanup, nhưng có thể che commit-time constraints, after-commit listeners và lazy-loading behavior.

Code production transaction closed trước serialization nhưng test transaction vẫn open có thể làm test pass và production fail.

Use transactional tests intentionally.

---

# 111. Testcontainers và Production Engine

Repository test với real PostgreSQL bắt được JSONB syntax, locking, sequences và dialect differences H2 bỏ sót.

Migrations cũng được test.

Integration test chậm hơn unit, nhưng confidence đúng layer.

---

# 112. Contract Testing

HTTP client adapter có contract với external API. Test request path, headers, serialization, error mapping và timeout behavior against stub/mock server.

Repository port có semantic contract; fake/JPA implementations nên giữ behavior expected.

---

# 113. Native Executable Testing

AOT/native image có closed-world differences. Reflection/resource paths chỉ chạy trong production cần được test actual native artifact.

Tracing agent/hints không thay coverage.

---

# 114. Language Idioms Senior

**Framework at the edge.** Business objects không cần Spring dependency vô lý.

**Transaction at use-case boundary.** Atomic DB policy gần business operation.

**Bounded everything.** Timeout, queue, pool, cache, payload, retry đều có giới hạn.

**Explicit side effects.** DB/HTTP/message boundaries dễ nhìn.

**Measure before optimize.** JFR/trace/metrics/DB plan trước tuning.

**Stable external contracts.** DTO/event/error codes không phụ thuộc entity/vendor class.

---

# 115. Programming Patterns Senior

**Transactional Outbox** cho DB + message intent. **Idempotency** cho retry/message/payment. **Bulkhead** cho scarce resources. **Retry + Backoff + Jitter** cho transient failure. **Deadline Propagation** cho latency budget. **Cache Aside/Single Flight** cho cache. **Anti-Corruption Layer** cho vendor boundary. **CQRS-lite** cho optimized read models. **Graceful Shutdown** cho deployment. **Optimistic Concurrency** cho concurrent edits.

---

# 116. Design Patterns trong Spring Senior

Proxy là nền của AOP/transaction/security/cache/async/declarative clients. Chain of Responsibility thể hiện qua servlet/security/interceptor chains. Adapter nằm ở MVC HandlerAdapter, persistence và external gateways. Observer liên hệ application events. Factory xuất hiện trong BeanFactory/FactoryBean. Strategy xuất hiện ở providers/handlers/policies. Front Controller là DispatcherServlet.

Ở Senior, pattern quan trọng không phải tên mà là trade-off: hidden control flow, testability, ordering và lifecycle.

---

# 117. Senior Mini Project: Production Order Platform

Xây modular monolith gồm `order`, `payment`, `inventory`, `customer`, `notification`.

Order creation dùng local transaction để lưu order + outbox. Một publisher background gửi integration event. Consumer simulation phải idempotent.

Payment adapter dùng RestClient/HTTP interface, timeout, error taxonomy, idempotency key, bounded retry và bulkhead.

JPA phải có optimistic locking, một read projection, một N+1 test/fix và batch processing experiment.

Security dùng OAuth2 Resource Server JWT. Authorization cancel order phải ở use-case boundary.

Observability gồm Actuator, Micrometer, tracing và custom checkout observation với low-cardinality tags.

Chạy load test platform threads vs virtual threads. Đo throughput, p95/p99, DB pool waiting, CPU, memory và thread counts.

Build native image experiment và so startup/RSS/steady-state thay vì tuyên bố winner.

---

# 118. Senior → Master Supplement Gate

Bạn sẵn sàng sang Master Supplement khi có thể giải thích bằng causal flow, không dùng câu “Spring tự làm”.

Với container, bạn phải hiểu definitions, post-processors, early bean creation và proxy chain. Với AOP, bạn phải giải thích Advisor/MethodInterceptor, proxy types, self-invocation và ordering.

Với transaction, bạn phải phân biệt logical/physical transactions, resource binding, rollback-only, REQUIRES_NEW resource impact và local-vs-distributed boundary.

Với JPA, bạn phải diagnose N+1/cartesian fetch, dirty checking cost, batching, locking, pool sizing và OSIV trade-off.

Với web, bạn phải chọn MVC platform threads, MVC virtual threads hay WebFlux dựa workload. Với reactive, hiểu event loop/backpressure/context.

Với Security, phải trace Servlet filter architecture, authentication manager/providers, JWT validation, method authorization, CSRF/CORS contexts.

Với production, phải giải thích outbox, idempotency, saga, cache stampede, graceful shutdown, observability cardinality, AOT/native constraints và incident debugging.

---

# 119. Những gì cố ý để sang Master Supplement

Master Supplement sẽ không lặp application patterns. Nó sẽ đi vào **Spring source/framework-author level**: `DefaultListableBeanFactory`, configuration-class processing, `AutowiredAnnotationBeanPostProcessor`, auto-proxy creation internals, `AdvisedSupport/ProxyFactory`, `TransactionInterceptor` source flow, `TransactionSynchronizationManager`, DispatcherServlet initialization, handler mappings/adapters registry, Boot auto-configuration import metadata, custom starter authoring, Spring TestContext internals, AOT processors/runtime hints deeper, Spring 7 null-safety/JSpecify, Boot 4 modularization và Spring 7.1 preview/current evolution.

Đó là layer cần thiết nếu mục tiêu là “master Spring itself”, không chỉ Senior Spring application engineer.

---

# 120. Version References

Current stable Boot system requirements: https://docs.spring.io/spring-boot/system-requirements.html

Spring AOP proxying: https://docs.spring.io/spring-framework/reference/core/aop/proxying.html

Spring Transactions: https://docs.spring.io/spring-framework/reference/data-access/transaction.html

Spring MVC: https://docs.spring.io/spring-framework/reference/web/webmvc.html

Spring WebFlux: https://docs.spring.io/spring-framework/reference/web/webflux.html

Spring Security: https://docs.spring.io/spring-security/reference/

Spring Boot Actuator: https://docs.spring.io/spring-boot/reference/actuator/

Spring Native Images: https://docs.spring.io/spring-boot/reference/packaging/native-image/

Boot 4 Migration: https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

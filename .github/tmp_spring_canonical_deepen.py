from pathlib import Path
import re
import subprocess

BASE = Path('10_backend/spring_java')
P1 = BASE / 'spring_part1_beginner_rewritten_detailed.md'
P2 = BASE / 'spring_part2_intermediate_rewritten_detailed.md'
P3 = BASE / 'spring_part3_senior_rewritten_detailed.md'
P4 = BASE / 'spring_part4_master_supplement_rewritten_detailed.md'
FILES = [P1, P2, P3, P4]


def read(p):
    return p.read_text(encoding='utf-8')


def write(p, text):
    p.write_text(text.rstrip() + '\n', encoding='utf-8')


def insert_before(text, marker, block, sentinel):
    if sentinel in text:
        return text
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError(f'marker not found: {marker}')
    return text[:idx] + block.strip() + '\n\n---\n\n' + text[idx:]


def strip_repetitive_labels(text):
    replacements = [
        '**Senior Note.** ',
        '**Language Idiom.** ',
        '**Programming Pattern.** ',
        '**Design Pattern.** ',
        '**Senior Rule.** ',
        '**Senior Pattern — Evidence over guessing.** ',
        '**Programming Pattern — Bounded Queue / Backpressure.** ',
        '**Language Idiom — Strong boundary types.** ',
        '**Programming Pattern — Policy boundary as collaborator.** ',
        '**Senior Pattern.** ',
    ]
    for r in replacements:
        text = text.replace(r, '')
    return text


def git(*args):
    subprocess.run(['git', *args], check=True)


def commit(message):
    git('add', *[str(p) for p in FILES])
    if subprocess.run(['git', 'diff', '--cached', '--quiet']).returncode != 0:
        git('commit', '-m', message)


# ---------------------------------------------------------------------------
# Batch 1 — IoC / DI internals
# ---------------------------------------------------------------------------

p1 = read(P1)
p1 = insert_before(
    p1,
    '# 3. Spring Framework và Spring Boot khác nhau như thế nào?',
    r'''
<!-- SPRING_BATCH1_IOC_BEGINNER -->
## Từ metadata tới bean instance: container thực sự làm gì khi “inject dependency”? 

Khi mới học, câu “Spring scan `@Service` rồi inject bean” đủ để bắt đầu, nhưng mental model đó quá ngắn để debug hệ thống thật. Container thực tế phải đi qua ba lớp khác nhau: **metadata cấu hình**, **BeanDefinition**, rồi mới tới **object instance**. `@Component`, `@Service`, `@Repository`, `@Configuration` và `@Bean` cung cấp metadata. Spring đọc metadata đó để đăng ký BeanDefinition, tức bản mô tả cách tạo object: class nào, scope nào, factory method nào, dependency nào, có lazy hay không, có qualifier gì và callback lifecycle nào. Chỉ sau khi context bước vào giai đoạn tạo bean, BeanDefinition mới được dùng để instantiate object.

Vì vậy một bean có thể “được Spring biết tới” nhưng object thật chưa hề tồn tại. Lazy bean là ví dụ rõ nhất. Request-scoped bean còn cho thấy một BeanDefinition có thể đại diện nhiều instance theo từng request thay vì một singleton duy nhất. Khi bạn hiểu definition và instance là hai khái niệm khác nhau, nhiều lỗi startup bắt đầu dễ đọc hơn.

Khi tạo một singleton service, container conceptually làm việc như sau:

```text
BeanDefinition của OrderService
→ chọn constructor
→ resolve từng constructor parameter
→ lấy hoặc tạo dependency bean tương ứng
→ gọi constructor Java bình thường
→ chạy injection/lifecycle processors
→ có thể wrap object bằng proxy
→ đặt final reference vào singleton registry
```

Điểm cuối rất quan trọng: reference mà controller nhận đôi khi không phải object do constructor vừa tạo mà là **proxy** bao quanh object đó. Transaction, method security, cache, async và AOP dựa trên khả năng này. Spring không thay đổi quy tắc Java; nó thay object mà caller đang giữ reference tới.

Dependency Injection vì vậy nên được hiểu là **xây object graph có kiểm soát**, không phải “tìm bean toàn cục”. Nếu business class tự giữ `ApplicationContext` rồi gọi `getBean()` ở mọi nơi, dependency lại trở thành hidden global lookup và bạn đã biến DI thành Service Locator. Constructor injection giữ graph hiển thị trong type signature, làm test dễ hơn và giúp container fail sớm nếu graph không thể xây.
<!-- SPRING_BATCH1_IOC_BEGINNER_END -->''',
    'SPRING_BATCH1_IOC_BEGINNER_END'
)
write(P1, strip_repetitive_labels(p1))

p2 = read(P2)
p2 = insert_before(
    p2,
    '# 6. BeanFactoryPostProcessor',
    r'''
<!-- SPRING_BATCH1_IOC_INTERMEDIATE -->
## `ApplicationContext.refresh()` dưới dạng một pipeline metadata → object graph

Một `ApplicationContext` đi vào trạng thái usable không phải bằng một lệnh “scan rồi new tất cả”. Với `AbstractApplicationContext`, mental model hữu ích là method `refresh()` điều phối nhiều phase. Environment và configuration sources được chuẩn bị; BeanDefinitions được load; factory-level processors có cơ hội thay metadata; BeanPostProcessors được đăng ký; sau đó eager singletons mới được instantiate; cuối cùng lifecycle/event infrastructure được hoàn tất.

`ConfigurationClassPostProcessor` là một component quan trọng ở nửa **metadata**. Nó parse `@Configuration`, `@ComponentScan`, `@Import`, `@Bean` và mở rộng configuration graph thành thêm BeanDefinitions. `AutowiredAnnotationBeanPostProcessor` lại làm việc ở nửa **instance/lifecycle**, đọc injection metadata và hỗ trợ resolve dependency cho constructor/field/method injection. Hai class đều có chữ “processor” nhưng tham gia ở hai thời điểm rất khác nhau; đây là lý do phải tách metadata processing và instance processing trong đầu.

`DefaultListableBeanFactory` là nơi dependency resolution trở nên cụ thể. Khi constructor yêu cầu `PaymentGateway`, container không chỉ tìm string bean name. Nó xem type assignability, generic type metadata khi có thể, qualifier, primary/fallback semantics, bean-name fallback và trạng thái candidate. Nếu dependency là `List<PaymentGateway>`, container resolve nhiều beans rồi order chúng theo ordering contract. Nếu dependency là `ObjectProvider<PaymentGateway>`, việc resolve object có thể bị trì hoãn tới lúc provider được gọi.

Một dependency graph tốt phải có thể giải từ ngoài vào trong. Constructor cycle như `A(B)` và `B(A)` không thể tạo theo Java semantics vì để construct A cần B hoàn chỉnh, còn construct B lại cần A. Historical Spring machinery có thể xử lý một số setter/field cycles bằng early singleton references, nhưng constructor cycle cho thấy graph không có điểm bắt đầu rõ. Thay vì bật circular-reference option như một fix mặc định, hãy tìm responsibility đang bị trộn hoặc introduce một abstraction/event boundary phù hợp.

Một quy tắc debug rất hiệu quả là phân loại lỗi theo phase. `NoSuchBeanDefinitionException` và `NoUniqueBeanDefinitionException` thường thuộc dependency resolution. Bean tạo được nhưng `@Transactional` không chạy thường thuộc proxy/post-processing hoặc call path. Bean không xuất hiện vì condition không match thuộc metadata/auto-configuration. Khi xác định đúng phase, số lượng hypothesis giảm mạnh.
<!-- SPRING_BATCH1_IOC_INTERMEDIATE_END -->''',
    'SPRING_BATCH1_IOC_INTERMEDIATE_END'
)
write(P2, strip_repetitive_labels(p2))

p3 = read(P3)
p3 = insert_before(
    p3,
    '# 4. Early Bean Creation và “not eligible for all BeanPostProcessors”',
    r'''
<!-- SPRING_BATCH1_IOC_SENIOR -->
## Dependency resolution ở production: type contract, lifecycle và exposed object phải được xem cùng nhau

Ở production, “bean tồn tại” chưa đủ. Bạn cần phân biệt **definition type**, **target type** và **exposed type**. Một `@Bean` factory method có thể khai báo interface return type trong khi object thật là implementation cụ thể; sau đó auto-proxying có thể expose JDK proxy chỉ implement interfaces hoặc class proxy subclass target. Code dùng `getBean(SomeConcreteClass.class)` có thể vì vậy phụ thuộc proxy strategy một cách vô tình, trong khi constructor injection theo stable interface ít nhạy hơn.

Dependency resolution cũng có lifecycle cost. Injecting một heavy singleton trực tiếp vào infrastructure bean có thể kéo cả application graph vào startup sớm. Injecting `ObjectProvider<T>` hoặc thiết kế lại boundary đôi khi không phải “lazy trick” mà là cách giữ phase separation đúng. Tuy nhiên provider bị dùng khắp business code lại làm dependencies khó nhìn, nên deferred lookup chỉ nên xuất hiện khi lifecycle/optionality thực sự cần.

Khi custom framework code can thiệp vào bean creation, hãy giữ một invariant: metadata processors không nên vô tình instantiate application beans, instance processors không nên phụ thuộc sâu vào business graph, và caller không nên phụ thuộc implementation detail của proxy. Ba nguyên tắc này giảm phần lớn các lỗi startup/proxy khó đoán.
<!-- SPRING_BATCH1_IOC_SENIOR_END -->''',
    'SPRING_BATCH1_IOC_SENIOR_END'
)
write(P3, strip_repetitive_labels(p3))

p4 = read(P4)
p4 = insert_before(
    p4,
    '# 5. `ConfigurationClassPostProcessor`',
    r'''
<!-- SPRING_BATCH1_IOC_MASTER -->
## Source trace: từ `getBean()` tới `doCreateBean()` và final exposed reference

Khi muốn đọc Spring source thay vì chỉ dùng API, một trace có giá trị là bắt đầu từ `AbstractBeanFactory#doGetBean`. Lookup trước hết kiểm tra singleton cache; nếu chưa có instance, framework lấy merged BeanDefinition, bảo đảm dependencies cần tạo trước, rồi đi vào creation path phù hợp scope. Với singleton, singleton registry kiểm soát “create once” semantics và trạng thái currently-in-creation để phát hiện cycle.

`AbstractAutowireCapableBeanFactory#createBean` và `doCreateBean` là nơi object creation pipeline trở nên rõ. Framework có cơ hội resolve class, cho `InstantiationAwareBeanPostProcessor` can thiệp trước instantiation, chọn constructor/factory method, instantiate bean, populate properties/injection points, chạy initialization callbacks rồi apply post-processors. Auto-proxy creator thường thay final exposed reference ở cuối lifecycle bằng proxy.

Circular-reference support làm pipeline phức tạp vì framework có thể đăng ký một **singleton factory cho early reference** trước khi bean hoàn tất initialization. `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference` cho phép auto-proxy infrastructure bảo đảm early reference tương thích với object sẽ được expose cuối. Đây là mechanism để hiểu source, không phải invitation xây graph dựa vào circular references.

Khi đọc source, đừng biến tên method nội bộ thành public contract. Contract mà application có thể dựa vào nằm ở documented container semantics, lifecycle interfaces và API reference. Tên helper hoặc ordering implementation có thể đổi giữa Framework versions. Mastery là dùng internals để giải thích behavior, rồi quay lại public contract để thiết kế code ổn định.
<!-- SPRING_BATCH1_IOC_MASTER_END -->''',
    'SPRING_BATCH1_IOC_MASTER_END'
)
write(P4, strip_repetitive_labels(p4))

commit('Deepen Spring IoC and dependency injection internals')


# ---------------------------------------------------------------------------
# Batch 2 — request lifecycle
# ---------------------------------------------------------------------------

p2 = read(P2)
p2 = insert_before(
    p2,
    '# 26. HandlerMapping',
    r'''
<!-- SPRING_BATCH2_REQUEST_INTERMEDIATE -->
## Request lifecycle end-to-end: từ servlet container tới response commit

Một request MVC bắt đầu trước Spring MVC. Tomcat hoặc Jetty nhận network data, parse HTTP và tạo `HttpServletRequest`/`HttpServletResponse`. Container chọn execution thread; với cấu hình virtual-thread hiện đại, execution model có thể khác platform-thread pool nhưng Servlet contract vẫn là request đi qua filter chain trước khi tới servlet đích.

Spring Security nếu được dùng nằm trong filter chain này, vì vậy authentication/authorization thường hoàn tất **trước** `DispatcherServlet`. Sau đó `DispatcherServlet#doDispatch` hỏi `HandlerMapping` để lấy `HandlerExecutionChain`, gọi `preHandle` của interceptors, chọn `HandlerAdapter`, rồi `RequestMappingHandlerAdapter` chuẩn bị invoke controller method. Argument resolvers lấy path variable, query parameter, request body, principal hoặc custom context; data binding/conversion tạo Java values; validation có thể reject request trước khi business service được gọi.

Nếu controller gọi application service transactional, lúc đó control mới đi qua service proxy và transaction interceptor. Repository/JPA chạy bên trong transaction; controller nhận result; return-value handler quyết định xử lý `ResponseEntity`, DTO, async type hoặc view; `HttpMessageConverter` serialize body. Chỉ khi servlet response được commit thì status/headers/body bắt đầu trở thành output không thể tự do thay đổi nữa.

Exception cũng có lifecycle. Exception từ controller không nhất thiết nhảy thẳng ra container; `HandlerExceptionResolver` chain, trong đó có resolver cho `@ExceptionHandler`/`@ControllerAdvice`, có cơ hội map exception thành response. Exception ở filter trước DispatcherServlet lại nằm ngoài MVC exception-resolver path và thường cần security/filter-level handling riêng. Đây là lý do cùng một exception type có thể được xử lý khác tùy nó phát sinh ở layer nào.

Async MVC thêm một boundary khác. Khi controller trả `Callable`, `DeferredResult` hoặc supported async type, servlet request có thể được đưa vào async mode và processing tiếp tục ở execution khác trước khi có một async dispatch quay lại hoàn tất response. ThreadLocal context tự chế có thể mất ở boundary này; security, tracing và request context phải dùng cơ chế propagation đúng. Vì vậy request lifecycle phải được hiểu theo **dispatches và execution context**, không chỉ “một request = một thread từ đầu tới cuối”.
<!-- SPRING_BATCH2_REQUEST_INTERMEDIATE_END -->''',
    'SPRING_BATCH2_REQUEST_INTERMEDIATE_END'
)
write(P2, p2)

p3 = read(P3)
p3 = insert_before(
    p3,
    '# 10. Transaction Internals: từ annotation tới resource',
    r'''
<!-- SPRING_BATCH2_REQUEST_SENIOR -->
## Request lifecycle dưới góc production: queueing, context và failure ownership

Senior debugging cần nối HTTP lifecycle với capacity. Một request có thể chờ ở connector accept queue, server executor, Security filter, rate limiter, DB connection pool, remote HTTP client hoặc lock. Tất cả đều biểu hiện cuối cùng là “endpoint chậm”, nhưng cách xử lý hoàn toàn khác. Metrics và traces phải cho phép tách **server queue time, application execution time và downstream wait time** thay vì chỉ có một timer tổng.

Filter order là security/correctness concern. CORS preflight phải được xử lý đúng trước authentication assumptions; correlation/tracing context phải có sớm để security/controller logs cùng một request ID; body-caching/logging filter có thể phá streaming hoặc tăng memory nếu wrap toàn payload. Interceptor phù hợp cho handler-aware policy, nhưng không nhìn thấy request bị security chain reject trước controller.

Một rule vận hành quan trọng là layer nào tạo side effect thì layer đó phải chịu lifecycle của side effect. Filter mở MDC/context phải đóng trong `finally`. Controller không nên manually close transaction-managed EntityManager. Service không nên giữ servlet request để dùng trong async background task sau khi request đã kết thúc. Tách ownership đúng làm shutdown, timeout và error handling dễ reasoning hơn.
<!-- SPRING_BATCH2_REQUEST_SENIOR_END -->''',
    'SPRING_BATCH2_REQUEST_SENIOR_END'
)
write(P3, p3)

p4 = read(P4)
p4 = insert_before(
    p4,
    '# 16. `RequestMappingHandlerMapping`',
    r'''
<!-- SPRING_BATCH2_REQUEST_MASTER -->
## Source trace: `DispatcherServlet#doDispatch` thực sự phối hợp những strategy nào?

Trong `doDispatch`, DispatcherServlet không trực tiếp gọi controller bằng reflection tùy ý. Nó lấy handler qua `getHandler`, chọn adapter qua `getHandlerAdapter`, rồi delegate việc invoke. Với annotated controller, `RequestMappingHandlerAdapter` tạo `ServletInvocableHandlerMethod`; argument resolution đi qua các composite resolver đã được đăng ký theo order. Một resolver chỉ tham gia khi `supportsParameter` trả true, sau đó mới resolve value. Return values đi qua một composite tương tự để chọn handler phù hợp.

`RequestResponseBodyMethodProcessor` là một mắt xích quan trọng cho `@RequestBody` và response body: nó phối hợp message converters, content negotiation, validation/binding hooks và body advice. Vì vậy lỗi JSON deserialize, validation và media type xảy ra trước controller body execution trong nhiều case. Khi custom converter/resolver được thêm sai order, bạn đang thay dispatch algorithm của framework chứ không chỉ “thêm annotation hỗ trợ”.

Exception resolution cũng là strategy chain. `ExceptionHandlerExceptionResolver` tìm `@ExceptionHandler`; `ResponseStatusExceptionResolver` xử lý status-oriented exceptions; default resolver map một số framework exceptions. Master-level extension nên chọn đúng strategy interface thay vì override DispatcherServlet hoặc viết filter bắt mọi Throwable làm mất semantics MVC.
<!-- SPRING_BATCH2_REQUEST_MASTER_END -->''',
    'SPRING_BATCH2_REQUEST_MASTER_END'
)
write(P4, p4)

commit('Trace Spring MVC request lifecycle end to end')


# ---------------------------------------------------------------------------
# Batch 3 — transactions and persistence
# ---------------------------------------------------------------------------

p2 = read(P2)
p2 = insert_before(
    p2,
    '# 39. PlatformTransactionManager',
    r'''
<!-- SPRING_BATCH3_TX_INTERMEDIATE -->
## `@Transactional` đi từ metadata tới Connection như thế nào?

`@Transactional` được đọc thành `TransactionAttribute`. Khi call đi qua transactional proxy, `TransactionInterceptor` đi vào common transaction logic của `TransactionAspectSupport`: resolve transaction attribute, chọn `TransactionManager`, hỏi manager xem có transaction hiện tại không rồi tạo `TransactionStatus`. Với JDBC, `DataSourceTransactionManager` lấy Connection từ DataSource, configure auto-commit/isolation/read-only theo policy và bind resource holder với current execution context. Repository code dùng Spring-aware connection access có thể vì vậy nhận đúng connection đang thuộc transaction hiện tại thay vì tạo connection độc lập.

`TransactionSynchronizationManager` giữ resource bindings và synchronization callbacks cho imperative transaction. Nó giải thích tại sao hai repository methods trên cùng thread có thể cùng dùng một transaction mà không truyền Connection qua mọi method signature. Nó cũng giải thích tại sao `new Thread(...)` hoặc arbitrary executor không tự mang transaction đi theo: thread mới không có resource binding cũ.

Khi target method return, interceptor không tự “commit database” trực tiếp. Transaction manager quyết định commit hay rollback dựa `TransactionStatus`, rollback-only flag và exception rule. Cleanup sau đó unbind resource, restore state và release Connection về pool. Nếu code giữ transaction quá lâu, bạn đang giữ scarce connection/locks quá lâu; annotation không làm resource cost biến mất.
<!-- SPRING_BATCH3_TX_INTERMEDIATE_END -->''',
    'SPRING_BATCH3_TX_INTERMEDIATE_END'
)
write(P2, p2)

p3 = read(P3)
p3 = insert_before(
    p3,
    '# 11. Physical transaction và logical scopes',
    r'''
<!-- SPRING_BATCH3_TX_SENIOR -->
## Suspend, resume, timeout và rollback-only là resource semantics chứ không phải annotation trivia

Khi propagation yêu cầu transaction mới, manager có thể phải suspend resources/context của transaction hiện tại, bind resources mới, chạy inner scope rồi resume outer resources. `REQUIRES_NEW` vì vậy vừa tạo isolation boundary vừa tăng concurrent resource demand. Với local JDBC/JPA, “suspend” không biến outer transaction thành free; connection/locks của outer có thể vẫn tồn tại trong lúc inner transaction cần thêm capacity.

Timeout cũng phải được nhìn từ resource layer. Spring transaction timeout có thể được truyền tới resource operations tùy manager/driver, nhưng nó không thay thế HTTP deadline, database statement timeout hay lock timeout ở mọi layer. Một use case có 2 giây budget nhưng remote client timeout 30 giây và DB lock wait 60 giây vẫn có thể phá latency SLO dù `@Transactional(timeout=5)` tồn tại.

Rollback-only là trạng thái của logical/physical transaction, không phải exception decoration. Một inner participant có thể đánh dấu transaction không còn committable; outer method catch exception chỉ thay Java control flow, không xóa trạng thái resource. Đây là lý do senior code review phải xem exception taxonomy cùng propagation graph.
<!-- SPRING_BATCH3_TX_SENIOR_END -->''',
    'SPRING_BATCH3_TX_SENIOR_END'
)
p3 = insert_before(
    p3,
    '# 18. JPA Persistence Context như Unit of Work',
    r'''
<!-- SPRING_BATCH3_JPA_SENIOR -->
## Từ Spring Data repository tới EntityManager: persistence runtime thật sự nằm ở đâu?

Spring Data repository interface thường được triển khai bằng proxy, nhưng proxy không phải database engine. Nó dịch repository invocation thành implementation/query execution dùng JPA `EntityManager`. `EntityManager` mà application inject thường là một shared proxy: mỗi call được route tới transaction-bound persistence context phù hợp. Vì vậy repository có thể trông stateless trong Java trong khi persistence context giữ managed entities và pending changes theo transaction.

`save(entity)` cũng không đồng nghĩa “chạy INSERT ngay”. `SimpleJpaRepository` quyết định entity có mới hay không; entity mới thường đi `persist`, entity được xem là existing thường đi `merge`. `merge` trả về managed copy và object truyền vào không nhất thiết trở thành chính instance managed. SQL INSERT/UPDATE có thể chỉ xuất hiện ở flush/commit, do JPA write-behind. Vì vậy debugger nhìn thấy `save()` return chưa có nghĩa database đã commit.

Flush là synchronization giữa persistence context và database transaction, còn commit là durable transaction boundary. Query có thể trigger flush tùy flush mode để bảo đảm query thấy changes. `saveAndFlush` ép synchronization sớm hơn nhưng vẫn không biến local transaction thành committed transaction. Dùng nó để “chắc chắn đã save” thường che việc chưa hiểu flush/commit semantics.

Open Session/EntityManager in View giữ persistence context qua web request để lazy relation còn có thể load trong serialization/view. Nó giảm `LazyInitializationException` nhưng làm SQL có thể phát sinh rất muộn, khó thấy transaction/query ownership và dễ tạo N+1. Senior design nên chủ động fetch/projection ở application boundary thay vì dựa lazy loading trong serializer.
<!-- SPRING_BATCH3_JPA_SENIOR_END -->''',
    'SPRING_BATCH3_JPA_SENIOR_END'
)
write(P3, p3)

p4 = read(P4)
p4 = insert_before(
    p4,
    '# 13. `TransactionSynchronizationManager`',
    r'''
<!-- SPRING_BATCH3_TX_MASTER -->
## Source trace: `TransactionInterceptor` → `TransactionAspectSupport` → transaction manager

`TransactionInterceptor` là MethodInterceptor mỏng; phần orchestration chính nằm trong `TransactionAspectSupport#invokeWithinTransaction`. Framework lấy `TransactionAttributeSource`, xác định manager, tạo/join transaction rồi invoke callback tới target. Sau target, logic complete-after-throwing hoặc commit-after-returning chuyển control cho transaction manager. Đọc source theo flow này giúp bạn phân biệt AOP interception với actual resource implementation.

Ở JDBC, `DataSourceTransactionManager` phối hợp `DataSourceUtils` và resource holder để cùng DataSource lookup nhận transaction-bound Connection. Ở JPA, `JpaTransactionManager` quản lý EntityManager/persistence context và có thể expose JDBC connection integration tùy setup. `TransactionSynchronizationManager` chỉ là context registry; business transaction semantics vẫn nằm trong manager + underlying resource.
<!-- SPRING_BATCH3_TX_MASTER_END -->''',
    'SPRING_BATCH3_TX_MASTER_END'
)
p4 = insert_before(
    p4,
    '# 15. `DispatcherServlet` source flow',
    r'''
<!-- SPRING_BATCH3_PERSISTENCE_MASTER -->
## Spring Data JPA proxy, query execution và entity state

Spring Data tạo repository proxy từ repository metadata, repository fragments và store-specific base implementation. Query method có thể được resolve thành derived query, declared query hoặc custom implementation. Proxy vì vậy là dispatch layer; query parser/JPA provider/database mới quyết định SQL cuối cùng.

Ở JPA, bốn trạng thái useful là transient, managed, detached và removed. Dirty checking chỉ áp dụng có ý nghĩa với managed entity trong persistence context. Khi transaction kết thúc và context đóng, entity trở detached; sửa field trên detached object không tự tạo SQL. `merge` không “reattach same object” theo cách đơn giản mà copy state vào managed instance và trả managed instance đó.

Performance phải được reason bằng fetch plan và SQL count, không bằng số repository methods. Một repository call có thể tạo một SQL projection nhỏ hoặc hàng trăm lazy queries. Ngược lại, một fetch join quá lớn có thể tạo Cartesian multiplication. Spring Data abstraction không loại nhu cầu đọc generated SQL, execution plan và persistence-context behavior.
<!-- SPRING_BATCH3_PERSISTENCE_MASTER_END -->''',
    'SPRING_BATCH3_PERSISTENCE_MASTER_END'
)
write(P4, p4)

commit('Deepen Spring transaction and persistence runtime')


# ---------------------------------------------------------------------------
# Batch 4 — Security and testing
# ---------------------------------------------------------------------------

p2 = read(P2)
p2 = insert_before(
    p2,
    '# 77. Authentication và SecurityContext',
    r'''
<!-- SPRING_BATCH4_SECURITY_INTERMEDIATE -->
## Spring Security request flow: từ filter matching tới `Authentication`

Servlet container nhìn Spring Security như một filter. `DelegatingFilterProxy` bridge container lifecycle với bean `FilterChainProxy`. `FilterChainProxy` giữ nhiều `SecurityFilterChain`; mỗi chain có request matcher và ordered filters. Với một request, chain phù hợp được chọn, vì vậy multiple-chain configuration thực chất là **routing security policy trước MVC routing**.

Một authentication filter đọc credential phù hợp protocol, tạo một `Authentication` chưa authenticated rồi giao cho `AuthenticationManager`. Common `ProviderManager` thử các `AuthenticationProvider` hỗ trợ loại token đó. Password provider có thể dùng `UserDetailsService` + `PasswordEncoder`; resource server JWT dùng provider/decoder khác. Khi thành công, authenticated `Authentication` được đặt vào SecurityContext theo configured strategy/repository để phần còn lại của request thấy principal/authorities.

Authorization xảy ra sau khi authentication context tồn tại. Request authorization dùng authorization manager/filter infrastructure; method security lại là method-interceptor/proxy layer, nghĩa là cùng một request có thể vượt HTTP rule nhưng bị chặn ở use-case method vì object-level policy. Đó là defense in depth khi boundary được chọn có chủ đích, không phải lý do copy cùng role expression ở mọi layer.

Authentication failure và access denied cũng có hai semantics khác nhau. Unauthenticated caller cần `AuthenticationEntryPoint`; authenticated caller thiếu quyền đi `AccessDeniedHandler`. Trộn cả hai thành HTTP 401 hoặc 403 tùy tiện làm client behavior và incident diagnosis sai.
<!-- SPRING_BATCH4_SECURITY_INTERMEDIATE_END -->''',
    'SPRING_BATCH4_SECURITY_INTERMEDIATE_END'
)
p2 = insert_before(
    p2,
    '# 81. `@MockitoBean`',
    r'''
<!-- SPRING_BATCH4_TEST_INTERMEDIATE -->
## Chọn test theo boundary thay vì chọn annotation theo thói quen

Plain unit test tạo object bằng constructor và test business rule nhanh nhất vì không cần Spring context. MVC slice test hỏi mapping, validation, serialization và controller advice có đúng không. Data slice test hỏi mapping/query/transaction với persistence infrastructure. Full `@SpringBootTest` hỏi object graph và integration giữa nhiều subsystem có khởi động/hoạt động cùng nhau không. End-to-end với real port chỉ cần ở những flow mà network/server behavior thật mang thêm confidence.

`@SpringBootTest` mặc định không đồng nghĩa “browser gọi server thật”; web environment quyết định mock servlet context hay embedded server với port. `MockMvc` chạy MVC infrastructure không cần network socket, rất phù hợp controller/filter integration. `RANDOM_PORT` phù hợp khi bạn cần HTTP client/server stack thật hơn.

`@MockitoBean` thay một Spring bean trong test context, khác với Mockito `@Mock` chỉ tạo object mock trong test class. Bean override thay cấu hình context và có thể ảnh hưởng TestContext cache key; hàng trăm test classes mỗi class override beans/properties khác nhau có thể tạo hàng trăm contexts. Khi suite chậm, đo context reuse trước khi chỉ tăng parallelism.

Transactional test auto-rollback rất tiện nhưng có blind spot: commit-time constraint, `afterCommit` callback, outbox publisher và lazy-loading sau transaction có thể không được exercise giống production. Hãy có tests explicit commit hoặc non-transactional request boundary cho những behavior này.
<!-- SPRING_BATCH4_TEST_INTERMEDIATE_END -->''',
    'SPRING_BATCH4_TEST_INTERMEDIATE_END'
)
write(P2, p2)

p3 = read(P3)
p3 = insert_before(
    p3,
    '# 59. AuthenticationManager và AuthenticationProvider',
    r'''
<!-- SPRING_BATCH4_SECURITY_SENIOR -->
## Security production model: credential transport, key lifecycle và object-level authorization

Security configuration phải bắt đầu từ credential transport. Session cookie nghĩa browser tự gửi credential và CSRF threat quan trọng. Bearer token trong `Authorization` header có threat khác nhưng vẫn cần XSS/storage/leak controls ở client. CORS chỉ là browser origin policy; nó không authenticate request và không thay authorization.

Với JWT resource server, signature validation mới chỉ chứng minh token phù hợp key/algorithm. Production policy còn phải kiểm issuer, audience, time claims/clock skew, key rotation/JWK refresh và mapping claims thành authorities đúng domain. Log không được ghi raw access token. Nếu identity provider outage xảy ra, behavior phụ thuộc key cache/discovery strategy; đây là availability dependency cần được observability hóa.

Authorization theo role thường chưa đủ cho business resource. “USER có thể cancel order” còn cần xác minh order thuộc user nào, trạng thái order và tenant. Policy này nên nằm ở use-case/domain authorization collaborator hoặc method authorization có access tới domain facts, không chỉ ở URL matcher. Nếu policy chỉ nằm controller, internal/batch/message entry point có thể bypass.
<!-- SPRING_BATCH4_SECURITY_SENIOR_END -->''',
    'SPRING_BATCH4_SECURITY_SENIOR_END'
)
p3 = insert_before(
    p3,
    '# 110. Transactional Tests Pitfall',
    r'''
<!-- SPRING_BATCH4_TEST_SENIOR -->
## Testing architecture phải mô phỏng đúng failure boundary

Một test suite production-grade không được dùng một kiểu test cho mọi thứ. Business invariant nên được ép qua plain unit/property tests; persistence concurrency cần real database vì locking/isolation khác H2; HTTP adapter cần contract/stub server để kiểm headers, timeout và error mapping; Security cần test cả unauthenticated, authenticated-but-forbidden và object ownership; transaction/outbox cần test commit thật.

Context caching là một phần hiệu năng test. Profiles, dynamic properties, bean overrides và configuration classes tham gia cache identity. `@DirtiesContext` làm context bị loại khỏi cache và nên được coi là expensive operation. Nếu một test cần mutate global singleton state rồi dirties context để cleanup, đó có thể là feedback rằng production design có global mutable state khó cô lập.

Testcontainers tăng fidelity nhưng không phải lý do đưa mọi unit test vào Docker. Hãy dùng container ở boundary nơi engine semantics quan trọng: PostgreSQL JSON/locking/index behavior, Kafka broker protocol, Redis TTL/serialization. Test nhanh ở inner loop và realistic ở integration boundary là hai mục tiêu bổ sung nhau.
<!-- SPRING_BATCH4_TEST_SENIOR_END -->''',
    'SPRING_BATCH4_TEST_SENIOR_END'
)
write(P3, p3)

p4 = read(P4)
p4 = insert_before(
    p4,
    '# 20. Spring TestContext Framework',
    r'''
<!-- SPRING_BATCH4_SECURITY_TEST_MASTER -->
## Source trace Spring Security và TestContext

`DelegatingFilterProxy` resolve filter bean từ ApplicationContext nhưng delegate security execution cho `FilterChainProxy`. `FilterChainProxy` chọn first matching `SecurityFilterChain` theo order rồi chạy list security filters. Authentication filters delegate tới `AuthenticationManager`; `ProviderManager` chọn `AuthenticationProvider`; authorization filter/interceptors dùng `AuthorizationManager`. `ExceptionTranslationFilter` chuyển security exceptions thành entry-point/access-denied responses ở servlet security layer. Trace theo các object này giúp debug 401/403 mà không cần bật debug log toàn hệ thống.

Method security lại đi qua Spring AOP infrastructure. Advisor/interceptor được gắn vào bean method; call phải qua proxy. Điều này nối trực tiếp knowledge của container/AOP với Security: self-invocation có thể bypass method-security advice giống transaction/cache nếu call path không đi qua proxy.

Ở testing, Spring TestContext tạo `MergedContextConfiguration` từ annotations/configuration/profiles/properties/context customizers rồi dùng nó như nền của cache key. Bean override annotations như `@MockitoBean` tham gia context customization, nên thay mock set có thể làm context không reuse. Hiểu cache key giúp tối ưu suite bằng architecture thay vì chỉ tăng CPU runner.
<!-- SPRING_BATCH4_SECURITY_TEST_MASTER_END -->''',
    'SPRING_BATCH4_SECURITY_TEST_MASTER_END'
)
write(P4, p4)

commit('Deepen Spring Security and testing architecture')


# ---------------------------------------------------------------------------
# Batch 5 — observability, troubleshooting, versions/migration
# ---------------------------------------------------------------------------

p1 = read(P1)
p1 = p1.replace('cập nhật 2026-09-12', 'cập nhật 2026-09-21')
p1 = p1.replace('<artifactId>spring-boot-starter-web</artifactId>', '<artifactId>spring-boot-starter-webmvc</artifactId>')
p1 = insert_before(
    p1,
    '# 5. Tạo một Spring Boot project và hiểu những file đang xuất hiện',
    r'''
<!-- SPRING_BATCH5_VERSION_BEGINNER -->
## Học version theo “cách viết application thay đổi”, không theo release-note list

Boot 2.7 / Framework 5.3 đại diện thế hệ Java 8-era, `javax.*` và nhiều security/config examples cũ. Khi nhìn `javax.servlet`, `javax.persistence`, `WebSecurityConfigurerAdapter`, `RestTemplate`-centric tutorials hoặc XML nhiều, đừng vội kết luận code sai; hãy xác định generation trước rồi map sang cách hiện đại.

Boot 3 / Framework 6 là bước chuyển platform lớn hơn một bản nâng version: Java 17 trở thành baseline, Java EE namespace đổi sang `jakarta.*`, Spring Security 6 chuyển mạnh sang bean/lambda configuration, observability/AOT trở thành first-class hơn. Migration thường thất bại ở third-party library chưa hỗ trợ Jakarta chứ không chỉ ở source import.

Boot 4 / Framework 7 tiếp tục platform hóa: Jakarta EE 11 / Servlet 6.1, Jackson 3 là hướng mặc định, Boot modularize starters/test support mạnh hơn, Framework dùng JSpecify nullness và có API-versioning support ở web stack. Vì vậy code mới nên học theo Boot 4.1, nhưng người làm enterprise vẫn cần đọc được 2.7/3.x và biết migration path thay vì rewrite toàn bộ.
<!-- SPRING_BATCH5_VERSION_BEGINNER_END -->''',
    'SPRING_BATCH5_VERSION_BEGINNER_END'
)
write(P1, p1)

p2 = read(P2)
p2 = p2.replace('cập nhật 2026-09-12', 'cập nhật 2026-09-21')
p2 = insert_before(
    p2,
    '# 86. Micrometer',
    r'''
<!-- SPRING_BATCH5_OBS_INTERMEDIATE -->
## Observability pipeline: operation → Observation → metrics/traces, còn log là evidence khác

Micrometer Observation model bắt đầu từ một operation có lifecycle start/stop/error và context. `ObservationRegistry` phối hợp các `ObservationHandler`; handler có thể tạo meter, tracing span hoặc context propagation tùy stack được cấu hình. Vì framework có thể instrument HTTP server/client, datasource và nhiều integrations sẵn, custom instrumentation nên bổ sung business boundary thay vì tạo duplicate span quanh mọi method.

Metric dimensions phải low-cardinality vì mỗi combination tạo time series. `method`, normalized route, status group hoặc payment type thường bounded; `userId`, `orderId`, raw exception message và full URL thường không bounded. High-cardinality identity phù hợp trace/log hơn. Một hệ thống quan sát tốt dùng cùng semantic operation names/correlation để đi từ metric spike → exemplar/trace → logs → JFR/DB evidence.

Actuator chỉ là management surface. Endpoint `health`, `metrics`, `mappings`, `conditions`, `threaddump`, `heapdump`, `env` có risk khác nhau. Exposure và authorization phải được thiết kế như admin API; production không nên public toàn bộ `/actuator/**`. Health cũng phải có semantics: liveness trả lời restart có giúp không; readiness trả lời instance có nên nhận traffic không.
<!-- SPRING_BATCH5_OBS_INTERMEDIATE_END -->''',
    'SPRING_BATCH5_OBS_INTERMEDIATE_END'
)
write(P2, p2)

p3 = read(P3)
p3 = p3.replace('cập nhật 2026-09-12', 'cập nhật 2026-09-21')
p3 = p3.replace('VERSION_DETAIL_PART3_2026-09-12', 'VERSION_DETAIL_PART3_2026-09-21')
p3 = insert_before(
    p3,
    '# 66. Observability: Metrics, Traces, Logs',
    r'''
<!-- SPRING_BATCH5_OBS_SENIOR -->
## Observability phải phản ánh queue/resource boundaries của Spring application

Một request timer duy nhất không đủ để biết request chậm ở đâu. Production dashboard nên cho thấy server request latency, active/in-flight requests, executor/virtual-thread behavior phù hợp runtime, DB pool active/pending/acquisition time, query latency, HTTP-client latency, cache hit/miss và JVM CPU/GC. Khi mỗi scarce resource có saturation signal, bạn có thể phân biệt CPU-bound với queue-bound hoặc downstream-bound.

Trace là causal path, nhưng trace không thay metric. Sampling có thể bỏ mất request hiếm; metrics cho distribution/p95/p99 và saturation liên tục. JFR lại trả lời JVM-level CPU/allocation/lock/GC mà tracing không thấy. Troubleshooting tốt chuyển giữa bốn lớp: metrics xác định thời điểm/phạm vi, trace tìm dependency/span, logs lấy domain/error context, profile/JFR/DB plan xác minh execution cost.
<!-- SPRING_BATCH5_OBS_SENIOR_END -->''',
    'SPRING_BATCH5_OBS_SENIOR_END'
)
p3 = insert_before(
    p3,
    '# 93. Production Debugging: `@Transactional` không chạy',
    r'''
<!-- SPRING_BATCH5_TROUBLESHOOTING_SENIOR -->
## Production troubleshooting theo symptom → layer → evidence

Nếu application **không start**, bắt đầu từ first meaningful cause trong exception chain rồi phân loại: configuration binding, missing/ambiguous bean, condition mismatch, schema migration, database connectivity, classpath/linkage hay custom initialization. Condition report và dependency tree hữu ích hơn thêm annotation thử nghiệm.

Nếu request trả **404**, trước tiên kiểm mapping/servlet context/path. Nếu **400**, nhìn conversion, JSON deserialize và Bean Validation. Nếu **401**, trace authentication chain/credential. Nếu **403**, xác định principal đã authenticated chưa và authorization rule nào deny. Nếu controller breakpoint không bao giờ hit, đừng debug service trước filter/mapping layer.

Nếu endpoint **chậm nhưng CPU thấp**, tìm wait: DB connection acquisition, slow SQL/locks, remote HTTP, executor queue, synchronized lock. Nếu **CPU cao**, dùng JFR/profile trước; JSON serialization, crypto, regex, mapper loops, GC hoặc busy loop đều có thể là nguyên nhân. Nếu **RSS tăng nhưng heap ổn**, nhìn thread count/stacks, direct buffer/native memory, metaspace và agents chứ không chỉ heap dump.

Nếu bật virtual threads mà throughput không tăng, kiểm downstream scarce resource. 50 DB connections vẫn chỉ cho khoảng 50 concurrent DB operations bất kể có 500 hay 50.000 virtual threads. Nếu latency tăng, queueing ở pool/semaphore/downstream vẫn là bottleneck thật.
<!-- SPRING_BATCH5_TROUBLESHOOTING_SENIOR_END -->''',
    'SPRING_BATCH5_TROUBLESHOOTING_SENIOR_END'
)
write(P3, p3)

p4 = read(P4)
p4 = p4.replace('Version snapshot — 2026-09-12', 'Version snapshot — 2026-09-21')
p4 = insert_before(
    p4,
    '# 45. Source-reading roadmap',
    r'''
<!-- SPRING_BATCH5_VERSION_MASTER -->
## Migration graph: 2.7/5.3 → 3.5/6.2 → 4.1/7.0

Migration nên được xem như chuỗi compatibility boundaries. Từ Boot 2.7 lên generation 3, boundary lớn là Java 17 + Jakarta namespace + portfolio major versions; hãy loại deprecated APIs ở latest 2.7 trước, update libraries tới bản Jakarta-compatible rồi mới đổi major. Từ Boot 3 lên 4, official strategy vẫn nên đưa application lên latest 3.5 trước để warnings/deprecations hiện rõ, sau đó mới xử lý Boot 4 modular starter graph, Framework 7, Jackson 3, Security 7 và test-module changes.

Đừng migrate bằng cách chỉnh version rồi sửa compile errors cho tới khi xanh. Một upgrade matrix phải test startup/auto-config, HTTP serialization, Security authentication/authorization, database migrations/JPA queries, transaction rollback behavior, scheduled/async work, observability agents/exporters và packaging/native path nếu có. Binary linkage errors sau deploy thường là dấu hiệu runtime dependency graph khác graph compile, vì vậy inspect packaged artifact/BOM resolution.

Tại thời điểm cập nhật này, baseline stable của bộ note là Boot 4.1.1 + Framework 7.0.9. Boot docs vẫn liệt kê 3.5.16 như maintenance line quan trọng. Framework 7.1.0-M1 và Boot 4.2.0-M1 vẫn preview. Spring Security docs liệt kê 7.1.1 là latest stable, cùng maintenance 7.0.7 và 6.5.11; Security 7.2.0-M1 là preview. Preview chỉ dùng để theo dõi direction, không được viết thành production baseline.
<!-- SPRING_BATCH5_VERSION_MASTER_END -->''',
    'SPRING_BATCH5_VERSION_MASTER_END'
)
write(P4, p4)

commit('Expand Spring observability troubleshooting and migrations')


# Final validation and cleanup
for p in FILES:
    text = read(p)
    if '_version_updated' in p.name or '_updated' in p.name:
        raise RuntimeError('canonical filename violation')

required = {
    P1: ['SPRING_BATCH1_IOC_BEGINNER_END', 'SPRING_BATCH5_VERSION_BEGINNER_END'],
    P2: ['SPRING_BATCH1_IOC_INTERMEDIATE_END', 'SPRING_BATCH2_REQUEST_INTERMEDIATE_END', 'SPRING_BATCH3_TX_INTERMEDIATE_END', 'SPRING_BATCH4_SECURITY_INTERMEDIATE_END', 'SPRING_BATCH4_TEST_INTERMEDIATE_END', 'SPRING_BATCH5_OBS_INTERMEDIATE_END'],
    P3: ['SPRING_BATCH1_IOC_SENIOR_END', 'SPRING_BATCH2_REQUEST_SENIOR_END', 'SPRING_BATCH3_TX_SENIOR_END', 'SPRING_BATCH3_JPA_SENIOR_END', 'SPRING_BATCH4_SECURITY_SENIOR_END', 'SPRING_BATCH4_TEST_SENIOR_END', 'SPRING_BATCH5_OBS_SENIOR_END', 'SPRING_BATCH5_TROUBLESHOOTING_SENIOR_END'],
    P4: ['SPRING_BATCH1_IOC_MASTER_END', 'SPRING_BATCH2_REQUEST_MASTER_END', 'SPRING_BATCH3_TX_MASTER_END', 'SPRING_BATCH3_PERSISTENCE_MASTER_END', 'SPRING_BATCH4_SECURITY_TEST_MASTER_END', 'SPRING_BATCH5_VERSION_MASTER_END'],
}
for p, markers in required.items():
    t = read(p)
    missing = [m for m in markers if m not in t]
    if missing:
        raise RuntimeError(f'{p}: missing {missing}')

# Ensure only four Spring markdown canonical notes remain.
mds = sorted(BASE.glob('*.md'))
if len(mds) != 4:
    raise RuntimeError(f'expected 4 canonical Spring notes, found {[p.name for p in mds]}')
if any('_updated' in p.name or '_version_updated' in p.name for p in mds):
    raise RuntimeError('duplicate updated file remains')

print('Spring canonical deepening audit passed:')
for p in mds:
    text = read(p)
    print(f'{p}: {len(text.splitlines())} lines, {len(text.split())} words')

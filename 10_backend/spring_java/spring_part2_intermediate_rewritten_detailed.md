# Java Spring — Part 2: Intermediate
## Từ “biết dùng Spring” đến “hiểu container, proxy, transaction và persistence runtime”

> Part 2 giả định bạn đã hoàn thành Part 1 và có thể tự xây một REST API nhỏ. Ở đây mục tiêu không còn là nhớ thêm annotation. Mục tiêu là hiểu Spring đang làm gì **trước khi bean tồn tại, trong lúc bean được tạo, khi method đi qua proxy, khi request đi qua MVC pipeline, khi transaction giữ connection và khi JPA giữ entity trong persistence context**.

---

# 1. Cách tư duy ở level Intermediate

Ở Beginner, bạn nhìn:

```java
@Service
class UserService {
}
```

và hiểu “Spring tạo bean này”.

Ở Intermediate, bạn cần hỏi thêm: Spring biết class này bằng metadata nào? Metadata được đăng ký khi nào? Container dùng definition nào để tạo object? Dependency được resolve trước hay sau constructor? Bean có bị một `BeanPostProcessor` wrap thành proxy không? Reference mà controller nhận là target object hay proxy?

Tương tự, khi nhìn:

```java
@Transactional
public void transfer() {
}
```

bạn không được dừng ở “method có transaction”. Bạn phải hỏi method call có đi qua Spring proxy không, transaction manager nào được chọn, đang join transaction cũ hay tạo transaction mới, DB connection được giữ trong bao lâu, exception nào làm rollback và side effect ngoài DB có nằm trong cùng atomic boundary không.

Đó là thay đổi tư duy chính của Part 2.

---

# 2. BeanFactory và ApplicationContext

`BeanFactory` là abstraction lõi của IoC container. Nó biết bean definitions, tạo object, resolve dependencies và cung cấp bean lookup. `ApplicationContext` xây trên BeanFactory và bổ sung các application-level capability như events, resource loading, environment, message resolution và tự động nhận các post-processors.

Trong Spring Boot, bạn gần như luôn làm việc với `ApplicationContext`. Nhưng biết `BeanFactory` là quan trọng vì rất nhiều error message và internal type xoay quanh bean factory.

Mental model:

```text
ApplicationContext
    └── BeanFactory
          ├── BeanDefinitions
          ├── singleton registry
          ├── dependency resolution
          └── creation/lifecycle machinery
```

Một `ApplicationContext` không phải chỉ là `Map<String,Object>`. Nó giữ metadata và infrastructure để tạo object đúng lúc, đúng scope và đúng lifecycle.

---

# 3. BeanDefinition là gì?

Trước khi singleton `UserService` instance tồn tại, container cần biết **cách** tạo nó. `BeanDefinition` là metadata kiểu blueprint.

Nó có thể mô tả bean class, scope, lazy flag, factory method, constructor metadata, init/destroy method, qualifiers, dependency metadata và các flags khác.

Khi component scanning tìm:

```java
@Service
public class UserService {
}
```

Spring không nhất thiết `new UserService()` ngay. Nó trước hết register metadata. Sau đó ở context refresh/bean creation phase, metadata này được dùng để tạo instance.

Đây là lý do hai khái niệm phải tách rõ:

```text
BeanDefinition exists
≠
Bean instance already exists
```

Một lazy bean có definition nhưng chưa có instance. Một request-scoped bean có definition toàn thời gian nhưng instance thay đổi theo request.

---

# 4. BeanDefinitionRegistry

Bean definitions phải được lưu ở đâu đó. `BeanDefinitionRegistry` là abstraction cho việc register/remove/query bean definitions.

Application code bình thường không dùng trực tiếp. Nhưng framework authors và advanced infrastructure có thể register dynamic beans programmatically.

Việc hiểu registry giúp bạn thấy component scanning chỉ là **một nguồn tạo definitions**. `@Bean`, auto-configuration, imports, XML cũ, programmatic registry và framework extensions đều có thể đưa bean definitions vào container.

---

# 5. Container startup lifecycle chi tiết hơn

Một flow đơn giản hóa nhưng hữu ích:

```text
Load configuration sources
→ register BeanDefinitions
→ invoke BeanFactoryPostProcessors
→ register BeanPostProcessors
→ create eager singleton beans
→ inject dependencies
→ run initialization callbacks
→ post-process / proxy beans
→ application ready
```

Điểm quan trọng là **metadata processing** xảy ra trước phần lớn object creation, còn **bean instance processing** xảy ra sau khi object đã được instantiate.

Nếu bạn hiểu hai giai đoạn này, `BeanFactoryPostProcessor` và `BeanPostProcessor` sẽ không còn dễ nhầm.

---

# 6. BeanFactoryPostProcessor

`BeanFactoryPostProcessor` làm việc với bean factory/definitions trước khi normal beans được tạo.

Hãy nghĩ nó như giai đoạn:

```text
“sửa bản thiết kế trước khi xây nhà”
```

Nó có thể sửa properties/metadata hoặc register thêm definitions.

Application code ít khi cần implement. Nếu một project có custom `BeanFactoryPostProcessor`, đó là infrastructure-level code và cần đọc cẩn thận vì nó ảnh hưởng container startup.

Một lỗi nguy hiểm là gọi `getBean()` quá sớm trong phase này, làm bean bị instantiate trước khi toàn bộ processing infrastructure sẵn sàng.

---

# 7. BeanPostProcessor

`BeanPostProcessor` làm việc với **bean instance**. Nó có callbacks trước/sau initialization.

Concept:

```text
raw bean
→ pre-init processors
→ initialization
→ post-init processors
→ final bean reference
```

Một post-processor có thể trả về cùng object hoặc object khác, ví dụ proxy.

Đây là cửa ngõ để hiểu rất nhiều Spring features. Injection annotations, lifecycle annotations, AOP proxy creation và nhiều framework behaviors được triển khai qua post-processing hoặc các infrastructure tương tự.

**Senior Note.** Nếu một bean “đáng lẽ phải transactional” nhưng không được proxy, một hypothesis là bean được tạo quá sớm trước khi auto-proxy creator có cơ hội xử lý.

---

# 8. Lifecycle callbacks sâu hơn

Một bean có thể trải qua constructor, dependency injection, Aware callbacks, pre-initialization post-processors, `@PostConstruct`, `InitializingBean.afterPropertiesSet`, custom init method, post-initialization processors và cuối cùng mới trở thành reference được sử dụng.

Có nhiều cơ chế để làm cùng loại việc. Điều đó không có nghĩa bạn nên dùng tất cả. Application code hiện đại thường dùng constructor + `@PostConstruct` rất ít và explicit lifecycle bean khi resource phức tạp.

Nếu startup logic có external I/O, hãy đặt timeout và failure semantics rõ. Một `@PostConstruct` gọi network 20 phút không phải initialization tốt.

---

# 9. Aware interfaces

Spring cung cấp các callback kiểu `BeanNameAware`, `ApplicationContextAware`, `EnvironmentAware`, `ResourceLoaderAware`.

Ví dụ:

```java
class MyInfrastructureBean
        implements ApplicationContextAware {

    @Override
    public void setApplicationContext(
            ApplicationContext applicationContext) {
        ...
    }
}
```

Application service bình thường không nên dùng `ApplicationContextAware` để fetch dependencies. Constructor injection rõ hơn.

Aware interfaces phù hợp khi component cần tương tác với container infrastructure như một framework integration.

---

# 10. FactoryBean khác `@Bean` như thế nào?

`@Bean` là annotation đặt trên factory method trong configuration.

`FactoryBean<T>` là interface đặc biệt của Spring. Bean được đăng ký là factory nhưng normal lookup thường nhận **product** của factory.

Ví dụ concept:

```text
FactoryBean<RemoteClient>
    ↓
getObject()
    ↓
RemoteClient
```

Nếu cần chính factory, bean name có semantics đặc biệt với `&`.

Frameworks dùng `FactoryBean` cho object phức tạp như proxies/clients. Application code bình thường rất ít khi cần tự viết một `FactoryBean`.

---

# 11. ObjectProvider và controlled lazy lookup

Có tình huống dependency không nên resolve ngay hoặc thật sự optional. Spring cung cấp `ObjectProvider<T>`.

```java
@Service
class ReportService {
    private final ObjectProvider<HeavyExporter> provider;

    ReportService(
            ObjectProvider<HeavyExporter> provider) {
        this.provider = provider;
    }

    void export() {
        HeavyExporter exporter =
                provider.getObject();
        ...
    }
}
```

Điều này tốt hơn tiêm `ApplicationContext` rồi `getBean` trong business code vì dependency type vẫn explicit.

`ObjectProvider` cũng hữu ích cho optional bean, multiple beans và prototype resolution.

---

# 12. Dependency resolution khi có nhiều candidates

Khi constructor cần:

```java
PaymentGateway gateway
```

Spring phải tìm candidate assignable với type. Nếu một candidate, dễ. Nếu nhiều, container xem qualifiers, primary và metadata khác để resolve.

Đây là lý do `NoUniqueBeanDefinitionException` không phải lỗi ngẫu nhiên; nó nói object graph mơ hồ.

Bạn có thể dùng semantic custom qualifier:

```java
@Target({
    ElementType.TYPE,
    ElementType.PARAMETER
})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface InternalPayment {
}
```

Implementation:

```java
@InternalPayment
@Component
class InternalPaymentGateway
        implements PaymentGateway {
}
```

Injection:

```java
PaymentService(
    @InternalPayment PaymentGateway gateway) {
}
```

Semantic qualifier bền hơn string bean name khi architecture thật sự có category rõ.

---

# 13. Inject `List<T>` để tạo pipeline

Nếu có nhiều validators:

```java
interface OrderValidator {
    void validate(Order order);
}
```

Spring có thể inject:

```java
OrderService(
        List<OrderValidator> validators) {
    this.validators = validators;
}
```

Các beans có thể được order bằng `@Order`/`Ordered`.

Đây là cách Spring rất tự nhiên để assemble **Chain of Responsibility**.

```text
Order
→ StockValidator
→ PriceValidator
→ PolicyValidator
→ proceed
```

**Programming Pattern.** Inject collection của strategies thay vì viết một God Validator với `if` khổng lồ.

---

# 14. Inject `Map<String,T>` và Strategy Registry

Spring có thể inject:

```java
Map<String, PaymentGateway> gateways
```

key thường liên quan bean name.

Bạn có thể build registry:

```java
@Component
class PaymentGatewayRegistry {
    private final Map<PaymentType, PaymentGateway> gateways;

    PaymentGatewayRegistry(
            List<PaymentGateway> gateways) {
        this.gateways = gateways.stream()
                .collect(toMap(
                    PaymentGateway::type,
                    identity()
                ));
    }
}
```

Business code:

```java
registry.get(type).charge(...);
```

Điều này scale tốt hơn rải `if (type == CARD)` hoặc `@Qualifier` ở mọi nơi.

---

# 15. Scope interaction: singleton inject prototype

Giả sử:

```java
@Scope("prototype")
@Component
class ReportContext {
}
```

và singleton service:

```java
@Service
class ReportService {
    private final ReportContext context;

    ReportService(ReportContext context) {
        this.context = context;
    }
}
```

Prototype được resolve lúc singleton tạo, nên service giữ một instance đó. Prototype scope không tự khiến field “refresh mỗi method call”.

Nếu cần instance mới mỗi lần, dùng provider:

```java
ReportContext context =
        provider.getObject();
```

Đây là ví dụ điển hình cho việc scope là lifecycle contract, không phải annotation decoration.

---

# 16. Scoped Proxy

Một singleton cần request-scoped dependency. Physical request object chỉ tồn tại trong từng request, nhưng singleton sống suốt app.

Spring giải quyết bằng proxy:

```text
Singleton Service
     ↓ holds
RequestContext proxy
     ↓ delegates at runtime
Current request-scoped instance
```

Vì vậy injected reference không nhất thiết là target object thật. Đây là cầu nối quan trọng sang AOP/proxy mindset.

---

# 17. Proxy là concept trung tâm của Spring

Rất nhiều tính năng Spring can thiệp vào method call bằng proxy:

```text
caller
  ↓
proxy
  ↓
interceptor/advice
  ↓
target
```

Transactions, method security, caching, async và AOP thường dựa vào kiểu flow này.

Nếu bạn giữ target raw hoặc call method nội bộ qua `this`, interceptor có thể không chạy.

---

# 18. JDK Dynamic Proxy và Class-based Proxy

JDK dynamic proxy chủ yếu proxy interfaces. Nếu target implement interface, proxy có thể expose interfaces.

Class-based proxy dùng subclass generation, truyền thống qua CGLIB. Vì nó subclass target nên final class/final method/private method có limitation tương ứng.

Ví dụ:

```java
public interface PaymentService {
    void pay();
}
```

JDK proxy có thể implement `PaymentService`.

Nếu code inject concrete `PaymentServiceImpl` thay vì interface, proxy strategy có thể ảnh hưởng type compatibility.

**Language Idiom.** “Program to intended public abstraction” giúp giảm coupling với proxy mechanics.

---

# 19. Self-invocation problem

Đây là một trong những bug Spring kinh điển.

```java
@Service
class OrderService {

    public void place() {
        saveAudit();
    }

    @Transactional
    public void saveAudit() {
        ...
    }
}
```

Call:

```java
this.saveAudit();
```

là Java call trực tiếp trong cùng object. Nó không đi ra proxy rồi quay lại.

Flow thực tế:

```text
external caller
→ proxy
→ OrderService.place()
→ this.saveAudit()
```

Không có:

```text
→ proxy transaction interceptor
```

ở call thứ hai.

Giải pháp tốt thường là tách policy boundary thành collaborator khác, không dùng hack self-proxy.

---

# 20. Spring AOP terminology

Một **Aspect** gom cross-cutting concern. **Pointcut** chọn nơi áp dụng. **Advice** là logic chạy. **Join point** trong Spring AOP thường là method execution có thể intercept. **Target** là object thật. **Proxy** là object caller thường tương tác.

Ví dụ logging aspect:

```java
@Aspect
@Component
class TimingAspect {

    @Around(
        "execution(* com.example..service..*(..))"
    )
    Object time(
        ProceedingJoinPoint pjp
    ) throws Throwable {

        long start = System.nanoTime();

        try {
            return pjp.proceed();
        } finally {
            long elapsed =
                System.nanoTime() - start;
            ...
        }
    }
}
```

AOP hợp với cross-cutting infrastructure. Business rule quan trọng không nên bị giấu trong pointcut khó nhìn.

---

# 21. Auto-configuration internals ở mức Intermediate

Boot auto-configuration là tập configuration classes được import có điều kiện.

Các condition phổ biến:

```java
@ConditionalOnClass(...)
@ConditionalOnMissingBean(...)
@ConditionalOnBean(...)
@ConditionalOnProperty(...)
```

`@ConditionalOnClass` nghĩa feature chỉ khả dụng nếu dependency/class cần thiết có mặt. `@ConditionalOnMissingBean` implement “default but back off”. `@ConditionalOnProperty` cho feature bật/tắt theo config.

Ví dụ conceptual:

```java
@AutoConfiguration
@ConditionalOnClass(PaymentSdk.class)
@EnableConfigurationProperties(
    PaymentProperties.class
)
class PaymentAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    PaymentClient paymentClient(
            PaymentProperties properties) {
        return new PaymentClient(properties);
    }
}
```

Đây là pattern nền cho starter/autoconfiguration ecosystem.

---

# 22. Condition Evaluation Report

Khi Boot không tạo bean bạn mong đợi, thay vì đoán hãy xem condition report/debug.

Nó trả lời:

```text
Auto-configuration nào matched?
Cái nào không matched?
Condition nào fail?
```

Ví dụ DataSource auto-config không chạy có thể vì JDBC class thiếu, không có URL hoặc một condition khác.

**Senior Pattern — Evidence over guessing.** Không thêm annotation ngẫu nhiên khi có condition report giải thích nguyên nhân.

---

# 23. Configuration Properties sâu hơn

Một subsystem nên có properties object:

```java
@Validated
@ConfigurationProperties(
    "payment.client"
)
public record PaymentClientProperties(
        @NotNull URI baseUrl,
        @NotNull Duration connectTimeout,
        @NotNull Duration readTimeout,
        @Min(0) int maxRetries) {
}
```

Spring bind external text thành type rồi validate.

Nếu `connect-timeout: abc`, application có thể fail startup thay vì chạy với giá trị sai.

---

# 24. Property source precedence

Một property có thể đến từ nhiều nguồn: packaged `application.yml`, profile-specific config, environment variables, JVM system properties, command-line arguments và test overrides.

Điều quan trọng không phải thuộc bảng precedence ngay lập tức mà là hiểu **cùng một key có thể bị override**.

Khi local chạy đúng nhưng container chạy khác, hãy kiểm tra effective config source.

Actuator/config reports có thể hỗ trợ nhưng phải bảo vệ secrets.

---

# 25. Spring MVC pipeline chi tiết

Beginner mental model:

```text
DispatcherServlet → Controller
```

Intermediate:

```text
HTTP request
→ Servlet Filter chain
→ DispatcherServlet
→ HandlerMapping
→ HandlerInterceptor.preHandle
→ HandlerAdapter
→ Argument Resolvers
→ Controller method
→ Return Value Handler
→ HttpMessageConverter
→ HTTP response
```

Mỗi stage giải quyết một loại abstraction khác.

---

# 26. HandlerMapping

`HandlerMapping` trả lời:

```text
Request này map tới handler nào?
```

Annotated controllers thường dùng `RequestMappingHandlerMapping`, nó đọc `@RequestMapping`, `@GetMapping` và mapping metadata.

Nếu hai methods match mơ hồ, error xảy ra ở mapping layer.

---

# 27. HandlerAdapter

DispatcherServlet không hard-code cách gọi mọi loại handler. `HandlerAdapter` biết cách thực thi handler kiểu cụ thể.

Annotated controller methods được xử lý qua `RequestMappingHandlerAdapter`.

Đây là **Adapter Pattern** trong framework architecture: DispatcherServlet tương tác uniform dù handler mechanisms khác.

---

# 28. HandlerMethodArgumentResolver

Controller:

```java
UserResponse me(
        @CurrentUser UserId userId)
```

Spring cần biết lấy `UserId` từ đâu. Custom argument resolver có thể đọc authenticated principal/security context rồi tạo domain `UserId`.

Resolver rất hợp với transport/context concern. Nó không nên gọi 5 databases và implement business workflow vì controller signature sẽ che hidden I/O.

---

# 29. ReturnValueHandler

Return type có thể là DTO, `ResponseEntity`, view model, async type hoặc các supported abstractions khác. Return-value handling quyết định semantics sau controller.

Đây là lý do controller method return “Java object” nhưng response lại có status/body JSON đúng.

---

# 30. HttpMessageConverter

Message converter chuyển:

```text
HTTP body
↔
Java object
```

JSON converter dùng Jackson integration. String/body resource/form-data có converter khác.

`@RequestBody` chỉ nói rằng argument đến từ body. Converter mới thực hiện format conversion.

---

# 31. `Content-Type` và `Accept`

`Content-Type` nói body hiện tại là format gì.

```http
Content-Type: application/json
```

`Accept` nói client muốn response format gì.

```http
Accept: application/json
```

Nếu request gửi format unsupported, server có thể trả `415 Unsupported Media Type`. Nếu client yêu cầu response representation server không tạo được, có thể `406 Not Acceptable`.

Đây là HTTP semantics được Spring MVC implement.

---

# 32. Servlet Filter và HandlerInterceptor

Filter ở Servlet level và chạy trước DispatcherServlet. Nó có thể wrap request/response, làm security infrastructure, request correlation và low-level web concerns.

Interceptor ở Spring MVC level và biết handler mapping/controller.

Ví dụ request ID tạo ở filter là hợp lý vì mọi request cần ID kể cả trước khi biết controller. Controller-specific audit có thể dùng interceptor.

Không chọn theo “filter cũ, interceptor mới”; chúng ở hai abstraction layer khác nhau.

---

# 33. OncePerRequestFilter

Spring có `OncePerRequestFilter` làm base class cho nhiều filter custom.

Ví dụ:

```java
@Component
class RequestIdFilter
        extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(
            HttpServletRequest request,
            HttpServletResponse response,
            FilterChain chain)
            throws ServletException, IOException {

        String requestId =
            UUID.randomUUID().toString();

        try {
            ...
            chain.doFilter(
                request,
                response);
        } finally {
            ...
        }
    }
}
```

Bạn vẫn phải hiểu async/error dispatch semantics nếu filter phức tạp.

---

# 34. ConversionService và custom Converter

Path variable là string ở HTTP nhưng có thể map thành domain ID.

```java
public record UserId(long value) {
}
```

Converter:

```java
@Component
class UserIdConverter
        implements Converter<
            String,
            UserId> {

    @Override
    public UserId convert(
            String source) {
        return new UserId(
            Long.parseLong(source));
    }
}
```

Controller:

```java
@GetMapping("/{id}")
UserResponse get(
        @PathVariable UserId id) {
}
```

**Language Idiom — Strong boundary types.** Conversion ở web boundary cho phép core dùng `UserId` thay vì raw `long`.

---

# 35. Method Validation

Bean Validation không chỉ áp vào DTO. Service method có thể được validation thông qua method-validation infrastructure.

```java
@Validated
@Service
class TransferService {

    public void transfer(
            @Positive
            BigDecimal amount) {
    }
}
```

Vì đây thường là interceptor/proxy feature, self-invocation/proxy boundary lại có ý nghĩa.

Tuy nhiên domain invariants phức tạp vẫn nên nằm trong domain/application logic, không biến validation annotations thành business engine.

---

# 36. Custom Validation Constraint

Khi một reusable syntactic/domain-adjacent constraint hợp lý, bạn có thể tạo annotation + `ConstraintValidator`.

Ví dụ currency code:

```java
@ValidCurrency
String currency
```

Validator nên pure/cheap nếu có thể. Validator gọi remote API hoặc DB cho mỗi field có thể tạo hidden I/O và performance khó đoán.

Cross-field rule như `start <= end` thường là class-level validation hoặc domain invariant.

---

# 37. ProblemDetail và error architecture

Ở Intermediate, error handling cần phân biệt representation error, validation error, domain rejection và infrastructure failure.

Ví dụ:

```text
"abc" không convert được sang long
→ malformed input

email="" 
→ Bean Validation

cancel order đã SHIPPED
→ domain conflict

database unreachable
→ infrastructure failure
```

`ProblemDetail` hoặc error envelope nên mang stable machine code, human message và correlation ID khi cần.

Controller advice là web boundary; domain exception không nhất thiết mang HTTP annotation.

---

# 38. Transaction infrastructure

`@Transactional` được transaction interceptor đọc khi method call đi qua proxy.

Flow concept:

```text
caller
→ transactional proxy
→ read transaction attributes
→ choose transaction manager
→ create/join transaction
→ invoke target
→ commit/rollback
→ cleanup
```

Nếu call không đi qua proxy, declarative transaction advice không chạy.

---

# 39. PlatformTransactionManager

Spring cung cấp transaction abstraction. Với JDBC có manager kiểu DataSource-based. Với JPA có JPA transaction manager. Application dùng common `@Transactional`, còn manager implementation biết cách điều khiển resource.

Điều này cho phép transaction semantics tương đối thống nhất ở Spring layer, nhưng database behavior vẫn phụ thuộc DB/JPA provider.

---

# 40. Propagation.REQUIRED

Default `REQUIRED` nghĩa:

```text
Có transaction hiện tại
→ join

Không có
→ tạo mới
```

Outer:

```java
@Transactional
public void checkout() {
    paymentService.record();
}
```

Inner:

```java
@Transactional
public void record() {
}
```

nếu proxy call đúng, thường cùng physical transaction.

---

# 41. Logical và Physical Transaction

Mỗi `@Transactional` method có logical transaction scope, nhưng nhiều REQUIRED scopes có thể dùng cùng physical DB transaction.

Điều này giải thích rollback-only.

Inner method fail và transaction bị đánh dấu rollback-only. Outer catch exception rồi cố return success. Khi commit, framework phát hiện physical transaction phải rollback và có thể ném `UnexpectedRollbackException`.

Đây là behavior bảo vệ caller khỏi tưởng rằng commit thành công.

---

# 42. REQUIRES_NEW

`REQUIRES_NEW` suspend outer transaction và tạo physical transaction riêng.

```java
@Transactional(
    propagation =
        Propagation.REQUIRES_NEW
)
```

Use case có thể là audit độc lập, nhưng phải cẩn thận resource.

Nếu outer giữ connection và inner cần thêm connection, mỗi thread có thể giữ 2 connections. Pool nhỏ có thể cạn.

Không dùng `REQUIRES_NEW` như “force save”.

---

# 43. NESTED

`NESTED` thường dựa trên savepoint semantics khi transaction manager/resource hỗ trợ.

Nó không giống REQUIRES_NEW. Nested có thể rollback phần trong về savepoint mà outer transaction tiếp tục, nhưng vẫn thuộc physical transaction lớn.

Support thực tế cần kiểm tra transaction manager/database.

---

# 44. Các propagation còn lại

`SUPPORTS` tham gia transaction nếu có, không có thì chạy non-transactional. `MANDATORY` yêu cầu transaction phải tồn tại. `NOT_SUPPORTED` suspend transaction hiện tại rồi chạy non-transactional. `NEVER` yêu cầu không được có transaction.

Bạn không cần dùng thường xuyên, nhưng phải biết chúng biểu diễn **policy về context hiện tại**, không chỉ “level” transaction.

---

# 45. Isolation

Spring expose isolation options tương ứng relational transaction concepts như READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE.

Nhưng tên giống nhau không có nghĩa mọi database implement chi tiết giống nhau. PostgreSQL, MySQL/InnoDB, Oracle có MVCC/locking semantics khác.

**Senior Note.** Học Spring isolation mà không học database isolation là thiếu một nửa.

---

# 46. `readOnly=true`

```java
@Transactional(readOnly = true)
```

là hint/policy được transaction manager/provider dùng. Với JPA nó có thể ảnh hưởng flush behavior; với DB/driver có thể set read-only hints.

Nó không phải universal “write blocker” và không nên được xem như security mechanism.

---

# 47. Rollback Rules

Spring declarative transaction mặc định rollback trên unchecked `RuntimeException`/`Error`; checked exceptions không tự động rollback theo default rule trừ khi cấu hình.

```java
@Transactional(
    rollbackFor = IOException.class
)
```

có thể override.

Đừng cấu hình `rollbackFor = Exception.class` khắp nơi nếu chưa thiết kế exception taxonomy.

---

# 48. TransactionTemplate

Nếu chỉ một phần method cần transaction hoặc bạn muốn sequence rõ:

```java
Order order =
    transactionTemplate.execute(
        status -> {
            Order saved =
                repository.save(...);
            outbox.save(...);
            return saved;
        });

paymentClient.notify(order.id());
```

Programmatic transaction làm boundary explicit và tránh một số proxy/self-invocation problem.

---

# 49. JDBC Exception Translation

Spring JDBC chuyển nhiều `SQLException` vendor-specific thành `DataAccessException` hierarchy.

Lợi ích là service không phụ thuộc trực tiếp error code từng DB.

Tuy nhiên production debugging vẫn cần root cause SQL state/vendor exception.

Exception translation không có nghĩa database differences biến mất.

---

# 50. JdbcClient, JdbcTemplate và NamedParameterJdbcTemplate

`JdbcTemplate` là API lâu đời, rõ và mạnh. `NamedParameterJdbcTemplate` thêm named params. `JdbcClient` cung cấp fluent façade hiện đại cho common JDBC operations.

Không có một winner tuyệt đối. Chọn theo codebase/version/use case. Điều cốt lõi vẫn là SQL, mapping, transaction và connection management.

---

# 51. JPA Entity Lifecycle

Một entity có thể ở trạng thái transient, managed, detached hoặc removed.

Transient:

```java
new UserEntity(...)
```

chưa thuộc persistence context.

Managed là entity được persistence context track. Khi managed state đổi trong transaction, dirty checking có thể generate update.

Detached là entity từng managed nhưng context không còn quản lý. Thay đổi detached object không tự động persist.

Removed là entity được schedule xóa.

---

# 52. Persistence Context

Persistence context không chỉ “cache”.

Nó là unit quản lý identity và state của entities.

Nếu load cùng entity ID trong một context, provider thường duy trì cùng object identity.

```text
find User#1
→ managed instance A

find User#1 again
→ same managed identity
```

Điều này hỗ trợ dirty checking và relationship consistency.

---

# 53. Dirty Checking

```java
@Transactional
public void changeName(
        long id,
        String newName) {

    UserEntity user =
        repository.findById(id)
            .orElseThrow();

    user.changeName(newName);
}
```

Nếu entity managed, provider so sánh/tracking state và phát SQL update khi flush.

Bạn có thể không cần gọi `save()` cho managed entity.

Việc hiểu này rất quan trọng vì nhiều tutorial gọi `save()` vô điều kiện làm bạn không thấy unit-of-work model của JPA.

---

# 54. Flush khác Commit

Flush đẩy pending ORM changes thành SQL/DB interaction để đồng bộ persistence context với database state cần thiết.

Commit hoàn tất transaction.

Có thể:

```text
flush
→ SQL chạy
→ transaction vẫn chưa commit
→ later rollback
```

Do đó “thấy INSERT được execute” không đồng nghĩa dữ liệu chắc chắn committed.

---

# 55. Lazy Loading

Relationship lazy không load ngay.

```java
order.getItems()
```

có thể trigger SQL khi access nếu persistence context còn hoạt động.

Nếu context đóng:

```text
entity detached
→ access lazy relation
→ LazyInitializationException
```

Đừng fix bằng `EAGER` toàn bộ. EAGER có thể over-fetch và tạo query explosion theo hướng khác.

---

# 56. N+1 Problem

Query 100 orders:

```sql
select ... from orders
```

Sau đó từng order load items:

```sql
select ... from order_items where order_id=?
```

Result:

```text
1 query orders
+
100 queries items
```

N+1 là performance problem do access pattern và fetch plan.

Fix có thể là fetch join, entity graph, projection, batch fetching hoặc query redesign tùy case.

---

# 57. Fetch Join

JPQL:

```jpql
select distinct o
from Order o
join fetch o.items
where o.id = :id
```

có thể load association trong query.

Nhưng fetch join collection + pagination hoặc nhiều collections có thể tạo Cartesian multiplication. Senior sẽ đi sâu.

---

# 58. EntityGraph

Entity graph mô tả fetch plan tách khỏi static entity mapping.

Ý tưởng tốt là relation mapping nói default semantics, còn use case quyết định cần graph nào.

Không phải mọi API call cần cùng graph.

---

# 59. Projection

Read-only API không nhất thiết load full entity.

```java
public record UserSummary(
    Long id,
    String name) {
}
```

query projection có thể chỉ lấy cột cần thiết.

Đây là bước đầu của CQRS-lite: write side dùng entity/domain model, read side có optimized query DTO.

---

# 60. Page, Slice và Sort

`Page` thường cung cấp total elements/total pages, nên có thể cần count query.

`Slice` chủ yếu biết có trang tiếp theo không, có thể tránh full total count.

Nếu UI không cần total, `Slice` có thể rẻ hơn.

Pagination cũng phải có ordering ổn định. Deep offset có performance issues; Senior sẽ học keyset/cursor pagination.

---

# 61. Optimistic Locking

Entity:

```java
@Version
private long version;
```

Hai transactions đọc version 1. A update thành version 2. B update với expected version 1 và fail optimistic locking.

Điều này tránh silent lost update mà không giữ row lock suốt thời gian user/business processing.

Conflict phải được xử lý theo business semantics: retry, reject hoặc yêu cầu user refresh.

---

# 62. Pessimistic Locking

Pessimistic lock yêu cầu DB lock row/resource.

Hợp khi conflict cost cao và contention pattern justify.

Nhưng lock làm transactions chờ nhau và có thể deadlock. Transaction phải ngắn và lock ordering nhất quán.

Không dùng pessimistic lock như default “cho chắc”.

---

# 63. Flyway và Liquibase trong flow delivery

Migration phải chạy theo sequence được version-control.

Nếu `V5` đã chạy production, không sửa file đó để “clean history”. Tạo `V6`.

Migration review phải xem lock/time impact. `ALTER TABLE` lớn có thể gây downtime tùy DB/version.

Schema evolution là production concern, không chỉ local startup concern.

---

# 64. RestClient cấu hình đúng

Client nên là bean:

```java
@Configuration
class PaymentClientConfiguration {

    @Bean
    RestClient paymentRestClient(
            RestClient.Builder builder,
            PaymentProperties properties) {

        return builder
            .baseUrl(
                properties.baseUrl()
                    .toString())
            .build();
    }
}
```

Business service không nên tự build client mỗi method.

Central configuration giúp headers, timeout, serialization, observability và base URL thống nhất.

---

# 65. HTTP Service Client

Spring cho phép declarative interface:

```java
public interface UserApi {

    @GetExchange("/users/{id}")
    UserResponse get(
        @PathVariable long id);
}
```

Framework tạo proxy triển khai interface và gửi HTTP.

Mental model rất giống Spring Data repository:

```text
interface contract
→ framework proxy
→ transport implementation
```

Domain vẫn nên phụ thuộc gateway abstraction nếu external API shape không phải domain contract.

---

# 66. RestTemplate và WebClient

`RestTemplate` xuất hiện rất nhiều trong legacy Spring. Bạn phải đọc được.

`RestClient` là synchronous fluent API hiện đại.

`WebClient` là reactive client với `Mono/Flux` và non-blocking execution model.

Đừng chọn WebClient chỉ vì “nhanh hơn”. Nếu application blocking/JPA và bạn call `.block()` mọi nơi, bạn đang trộn models mà không nhận lợi ích rõ.

---

# 67. Spring Events

Publisher:

```java
publisher.publishEvent(
    new UserRegistered(userId));
```

Listener:

```java
@EventListener
void on(UserRegistered event) {
}
```

Default application event không phải durable distributed message. Nó sống trong process.

Nếu listener throw, behavior phụ thuộc synchronous/asynchronous event infrastructure.

---

# 68. TransactionalEventListener

Bạn có thể bind listener vào transaction phase như after commit.

Ví dụ gửi follow-up only after DB commit.

Nhưng crash:

```text
DB committed
→ process crashes
→ in-memory after-commit listener not completed
```

event có thể mất.

Nếu business requires durable delivery, cần Outbox/broker pattern ở Senior.

---

# 69. `@Async`

`@Async` dùng proxy/interceptor để submit method execution vào executor.

Điều này thay:

```text
thread
transaction context
exception flow
security context
trace context
```

`void` async method có exception không thể return cho original caller theo normal call stack.

Nếu caller cần result/failure, `CompletableFuture` hoặc durable workflow phù hợp hơn tùy requirement.

---

# 70. Async Executor

Bạn phải biết executor nào thực thi task. Với platform-thread pool, quan tâm core/max/queue/rejection/shutdown.

Một unbounded queue có thể giữ hàng triệu tasks khi producer nhanh hơn consumer.

**Programming Pattern — Bounded Queue / Backpressure.** Async không loại overload; nó chỉ chuyển overload sang queue nếu không có capacity policy.

---

# 71. Virtual Threads trong Spring Boot

Với Java 21+, Boot có thể bật virtual-thread support:

```yaml
spring:
  threads:
    virtual:
      enabled: true
```

Virtual threads làm imperative blocking style scale concurrency tốt hơn ở nhiều I/O workloads.

Nhưng DB connection pool vẫn giới hạn database concurrency. Nếu 100.000 virtual threads cùng cần DB và pool có 30 connections, 99.970 threads có thể chờ. Điều đó có thể đúng vì DB không chịu 100k concurrent queries.

Virtual thread không thay capacity management.

---

# 72. `@Scheduled`

`fixedDelay` tính delay sau lần execution trước hoàn tất. `fixedRate` target cadence dựa trên schedule intervals.

Cron expressions cho scheduling linh hoạt.

Trong cluster 3 replicas, mỗi instance có scheduler riêng. Nếu job phải chạy đúng một lần toàn cluster, cần distributed lock hoặc external job scheduler.

---

# 73. Spring Cache

`@Cacheable`:

```java
@Cacheable(
    cacheNames = "users",
    key = "#id"
)
public User get(long id) {
}
```

cache hit có thể skip method.

`@CachePut` execute method rồi update cache. `@CacheEvict` xoá entry.

Nhưng annotation không trả lời TTL, max size, distributed consistency, serialization, stampede hoặc eviction policy.

---

# 74. Cache Self-invocation

Caching cũng thường proxy-based.

```java
this.getUser(id);
```

có thể bypass cache advice giống transaction.

Đây là lý do hiểu proxy một lần giúp hiểu nhiều Spring annotations.

---

# 75. Cache key semantics

Cache key phải chứa các input quyết định output.

Nếu result phụ thuộc:

```text
userId
tenant
locale
permission level
```

nhưng key chỉ là `userId`, cache có thể trả sai dữ liệu.

Caching là correctness system, không chỉ performance tool.

---

# 76. Spring Security architecture ở Intermediate

Servlet security thường có flow:

```text
Servlet Filter Chain
→ DelegatingFilterProxy
→ FilterChainProxy
→ SecurityFilterChain
→ authentication filters
→ authorization
→ DispatcherServlet
```

Spring Security nằm trước controller phần lớn thời gian.

Nếu request không vào controller, lỗi có thể nằm trong security chain chứ không phải mapping.

---

# 77. Authentication và SecurityContext

Sau authentication thành công, Spring Security có `Authentication` chứa principal/authorities và được đặt trong security context theo configured strategy.

Controller/service có thể đọc authenticated principal qua higher-level APIs.

Bạn không nên tự parse Authorization header trong mọi controller.

---

# 78. Authorization

Authorization quyết định caller có quyền gì.

Simple:

```text
role/authority
```

Complex:

```text
user có sở hữu order này không?
```

Có thể cần domain authorization service, không chỉ string expressions.

Method security đưa policy gần use-case boundary nhưng cũng là proxy feature.

---

# 79. CSRF và CORS ở level đúng

CORS là browser cross-origin policy. Nó không xác minh user.

CSRF là attack liên quan browser tự gửi credentials như cookies/session sang target site. Stateless bearer-token API có threat model khác.

Đừng copy:

```java
csrf.disable();
cors.allowAll();
```

chỉ để Postman/browser chạy.

---

# 80. Testing Slices

Spring Boot test slices load phần context cần thiết.

`@WebMvcTest` tập trung MVC.

`@DataJpaTest` tập trung JPA.

`@JdbcTest` tập trung JDBC.

`@JsonTest` tập trung JSON.

`@RestClientTest` hỗ trợ client layer tùy generation/module.

Chọn slice giúp test nhanh và failure localized.

---

# 81. `@MockitoBean`

Spring Test hiện đại có bean override support như `@MockitoBean`.

```java
@WebMvcTest(UserController.class)
class UserControllerTest {

    @MockitoBean
    UserService userService;
}
```

Nhiều tutorial cũ dùng `@MockBean`. Khi học Boot 4/Framework 7, ưu tiên current Spring Test API và chỉ nhận biết legacy syntax.

---

# 82. Test Context Caching

Spring Test cache ApplicationContext tương thích giữa tests.

Nếu mỗi test class có profile/properties/mock setup khác, contexts khác nhau và startup lặp lại.

`@DirtiesContext` ép context không reuse và rất đắt nếu lạm dụng.

Test suite performance cũng là architecture feedback.

---

# 83. Testcontainers

H2 không phải PostgreSQL/Oracle/MySQL.

Nếu query dùng DB-specific feature, locking, JSON operators hoặc dialect, in-memory fake DB có thể cho confidence sai.

Testcontainers cho phép chạy actual DB engine trong test.

```text
real PostgreSQL
→ Flyway migrations
→ repository test
```

Điều này rất giá trị cho data layer.

---

# 84. `@DynamicPropertySource`

Container có dynamic port/URL. Test cần inject property:

```java
@DynamicPropertySource
static void configure(
        DynamicPropertyRegistry registry) {

    registry.add(
        "spring.datasource.url",
        postgres::getJdbcUrl);
}
```

Boot còn có integration tiện hơn tùy current modules/version, nhưng mental model là runtime resource tạo config động.

---

# 85. Actuator sâu hơn

Actuator có thể expose health, metrics, mappings, conditions, config properties, environment, thread dump, heap dump và nhiều runtime info.

Các endpoint nhạy cảm không được public mặc định tùy config, và bạn không nên mở tất cả.

Trong incident, `/actuator/conditions`/mappings/metrics có thể rất hữu ích.

---

# 86. Micrometer

Micrometer là metrics/observation abstraction trong Spring ecosystem.

Counter đo event count tăng dần. Gauge đo current value. Timer đo count + duration distribution.

Ví dụ:

```text
orders.created
http.client.duration
queue.depth
```

Tag phải low-cardinality.

Sai:

```text
userId=123456
```

vì mỗi user tạo time series.

Đúng hơn:

```text
status=SUCCESS
paymentType=CARD
```

---

# 87. Observation

Modern Spring/Micrometer Observation model cho phép một operation tạo metrics/tracing instrumentation thống nhất.

Bạn chưa cần custom Observation phức tạp ở Intermediate, nhưng nên hiểu framework observability không chỉ là `log.info`.

Senior sẽ học trace context propagation và custom observations.

---

# 88. Liveness và Readiness ở deployment

Liveness không nên fail vì một external dependency temporary unavailable nếu restart process không giúp.

Readiness có thể fail để load balancer stop sending traffic.

Probe phải nhanh và bounded. Health endpoint gọi 10 slow APIs mỗi 2 giây có thể trở thành load generator.

---

# 89. Graceful Shutdown awareness

Application shutdown tốt không phải `kill -9`.

Flow lý tưởng:

```text
stop accepting traffic
→ drain in-flight requests
→ stop producers
→ finish/stop background tasks
→ close clients/pools
→ close context
```

Boot hỗ trợ graceful shutdown ở web infrastructure, nhưng custom executor/client/resource phải có lifecycle đúng.

---

# 90. Coding Patterns ở Intermediate

**Bean collection as Strategy/Chain.** Inject `List<T>` thay vì giant conditional.

**Typed configuration + validation.** Invalid config fail startup.

**Proxy boundary awareness.** Nếu feature dựa method interception, external call path phải đi qua proxy.

**Transactional use-case boundary.** Transaction bao business atomic operation, không tùy tiện ở controller/repository mọi nơi.

**DTO projection for reads.** Không load entity graph chỉ để trả 3 fields.

**Bounded async.** Executor queue/capacity/failure semantics phải explicit.

**Transport adapter translation.** HTTP/JPA vendor exceptions không leak vô hạn vào core.

---

# 91. Design Patterns ở Intermediate

Spring AOP thể hiện Proxy/Interceptor. HandlerAdapter thể hiện Adapter. MVC filters/interceptors tạo Chain of Responsibility. `BeanFactory` và `FactoryBean` thể hiện factory abstractions. Spring Events liên hệ Observer. `JdbcTemplate`/`TransactionTemplate` là template-style patterns. Strategy injection qua multiple beans giúp business extension mà không mở `switch` khổng lồ.

Pattern chỉ có giá trị khi bạn hiểu runtime cost và hidden control flow.

---

# 92. Common Intermediate mistakes

Một lỗi rất phổ biến là “annotation stacking”: `@Transactional @Async @Cacheable` trên cùng method mà không trace execution order. Transaction có chạy ở caller thread hay async thread? Cache key được check trước hay sau security? Exception retry ở ngoài hay trong transaction? Nếu không trả lời được, code chưa đủ rõ.

Lỗi khác là fix N+1 bằng EAGER toàn bộ. Điều đó chuyển từ “query nhiều” sang “fetch quá nhiều”.

Lỗi khác là tăng DB pool khi pool timeout. Nguyên nhân có thể là long transaction hoặc slow query; pool lớn hơn chỉ đưa thêm load xuống DB.

Lỗi khác là `@SpringBootTest` cho mọi test. Dùng unit/slice/integration đúng level.

Lỗi khác là xem application events như durable message queue.

---

# 93. Mini Project Intermediate: Order Service

Hãy xây `Order Service` dùng PostgreSQL + Flyway + Spring Data JPA. `Order` có items, status và optimistic `@Version`. Endpoint tạo order, đọc detail, list pagination, cancel và mark paid.

Bạn phải cố ý tạo N+1 rồi đo số SQL, sau đó fix bằng fetch plan/projection. Bạn phải viết một transaction tạo order + outbox row cùng local transaction, dù chưa publish broker thật.

Tạo `PaymentClient` bằng RestClient hoặc HTTP interface, có typed config và timeout. Viết một fake HTTP server/test để verify request/response mapping.

Thêm cache cho read path rồi mô tả key/TTL/invalidation semantics. Thêm async notification và ghi rõ executor/failure behavior. Nếu Java 21+, chạy một experiment virtual threads.

Test phải gồm plain unit test, `@WebMvcTest`, `@DataJpaTest`, Testcontainers PostgreSQL và một `@SpringBootTest`.

---

# 94. Intermediate → Senior Gate

Bạn sẵn sàng sang Senior khi có thể trace một bean từ BeanDefinition đến final proxy reference; giải thích BeanFactoryPostProcessor khác BeanPostProcessor; nói được vì sao self-invocation bypass transaction/cache/async; và giải thích dependency candidate resolution khi có multiple beans.

Bạn phải trace request qua Filter → DispatcherServlet → HandlerMapping → HandlerAdapter → ArgumentResolver → Controller → ReturnValueHandler → MessageConverter.

Với transaction, bạn phải giải thích REQUIRED, REQUIRES_NEW, NESTED, rollback-only, UnexpectedRollbackException, isolation và checked-exception rollback defaults. Bạn phải biết `readOnly` không phải security write blocker.

Với JPA, bạn phải giải thích persistence context, managed/detached, dirty checking, flush vs commit, lazy loading, N+1, fetch join, projection, pagination và optimistic locking.

Với infrastructure, bạn phải hiểu `@Async` cần executor, `@Scheduled` chạy trên mỗi instance, Spring event không durable, cache annotation không định nghĩa cache policy, virtual thread không thay DB pool, và Security chạy ở filter chain trước MVC.

Nếu bạn chỉ nhớ API names mà không giải thích được failure modes, chưa nên gọi là Senior.

---

# 95. Version Notes

Spring Boot 4.1.1 hiện yêu cầu Java 17+, Spring Framework 7.0.9+ và hỗ trợ Java đến 26 theo official system requirements. Boot 4 dùng Jakarta EE 11/Servlet 6.1 baseline và ưu tiên Jackson 3.

Boot 3.x vẫn cực kỳ quan trọng trong enterprise. Khi đọc code Boot 3, bạn có thể gặp Jackson 2 và testing annotations/conventions cũ hơn. Boot 2.7 còn `javax.*`.

Current references:

Spring Boot: https://docs.spring.io/spring-boot/reference/

Spring Framework: https://docs.spring.io/spring-framework/reference/

Transaction: https://docs.spring.io/spring-framework/reference/data-access/transaction.html

Spring MVC: https://docs.spring.io/spring-framework/reference/web/webmvc.html

Spring Data JPA: https://docs.spring.io/spring-data/jpa/reference/

Spring Security: https://docs.spring.io/spring-security/reference/

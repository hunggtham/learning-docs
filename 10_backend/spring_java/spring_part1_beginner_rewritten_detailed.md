# Java Spring — Part 1: Beginner
## Học Spring Framework và Spring Boot từ số 0, theo hướng hiểu bản chất trước khi dùng annotation

> Lộ trình của bộ tài liệu này là **Beginner → Intermediate → Senior → Master Supplement**.  
> Part 1 được viết cho người đã biết Java Core ở mức cơ bản nhưng **chưa cần biết Spring, Servlet, HTTP backend, IoC, DI, JDBC, ORM hay transaction**. Mục tiêu không phải học thuộc annotation, mà là hiểu vì sao Spring tồn tại, Spring đang làm công việc gì thay cho bạn, và mỗi dòng code của một ứng dụng Spring Boot liên hệ thế nào với Java thuần.

---

# 1. Spring giải quyết vấn đề gì?

Nếu mới học backend Java, bạn rất dễ nhìn Spring như một bộ sưu tập annotation. Bạn thấy `@RestController`, `@Service`, `@Repository`, `@Autowired`, `@Transactional` và tưởng rằng chỉ cần nhớ “annotation này dùng để làm gì” là đã học Spring. Cách học đó giúp tạo demo nhanh nhưng rất dễ gãy khi gặp project thật, bởi vì annotation chỉ là **metadata**. Annotation tự nó không tạo object, không mở transaction, không nhận HTTP request và cũng không truy cập database. Có một runtime của Spring đọc metadata đó rồi thực hiện công việc tương ứng.

Hãy bắt đầu bằng Java thuần. Giả sử hệ thống đặt hàng cần một `OrderService`, và `OrderService` cần một `PaymentGateway`.

```java
public final class OrderService {
    private final PaymentGateway paymentGateway;

    public OrderService() {
        this.paymentGateway = new KoreanCardPaymentGateway();
    }

    public void placeOrder(Order order) {
        paymentGateway.charge(order.total());
    }
}
```

Đoạn code này chạy được, nhưng `OrderService` đang vừa làm business logic vừa tự quyết định dependency cụ thể. Nếu ngày mai bạn muốn dùng `MockPaymentGateway` cho test hoặc đổi sang `BankTransferPaymentGateway`, bạn phải sửa `OrderService`. Class này đang phụ thuộc trực tiếp vào cách dependency được khởi tạo.

Ta có thể cải thiện bằng constructor:

```java
public final class OrderService {
    private final PaymentGateway paymentGateway;

    public OrderService(PaymentGateway paymentGateway) {
        this.paymentGateway = paymentGateway;
    }
}
```

Ở đây `OrderService` chỉ nói rằng “tôi cần một `PaymentGateway`”. Nó không quyết định ai tạo gateway và gateway cụ thể là class nào. Một nơi khác sẽ assemble object graph:

```java
PaymentGateway gateway = new KoreanCardPaymentGateway();
OrderService orderService = new OrderService(gateway);
```

Đây chính là điểm xuất phát để hiểu **Dependency Injection**. Dependency được đưa từ bên ngoài vào object, thay vì object tự tạo dependency bên trong.

Khi application lớn lên, việc tự tay viết hàng trăm dòng `new A(new B(new C(...)))` trở nên khó quản lý. Bạn còn phải giải quyết lifecycle, configuration, environment, test replacement, proxy, transaction, web infrastructure và nhiều dependency có quan hệ với nhau. Spring cung cấp một **container** làm công việc tạo và liên kết các object đó.

**Language Idiom.** Trong Java/Spring hiện đại, dependency bắt buộc nên được biểu diễn bằng constructor parameter. Điều này làm object graph rõ ràng, field có thể `final`, và object không tồn tại ở trạng thái “chưa được inject xong”.

**Programming Pattern.** Pattern quan trọng ở đây là **Constructor Injection** và **Explicit Dependencies**. Một class có constructor gồm `OrderRepository`, `PaymentGateway` và `Clock` nói rất rõ nó cần gì để hoạt động.

**Design Pattern.** Ở tầng design, Spring hỗ trợ **Dependency Injection**, đồng thời giúp thực hiện **Dependency Inversion Principle** khi business code phụ thuộc vào abstraction thay vì vendor implementation.

**Senior Note.** Nếu constructor của một service có mười hai dependency, đừng chữa bằng field injection để constructor trông ngắn hơn. Đó thường là tín hiệu class đang có quá nhiều trách nhiệm hoặc use case boundary chưa rõ.

---

# 2. IoC là gì và tại sao Dependency Injection chỉ là một phần của IoC?

**IoC — Inversion of Control** có nghĩa rộng hơn Dependency Injection. Trong code Java thuần nhỏ, application code thường trực tiếp kiểm soát việc tạo object, gọi lifecycle và wiring. Với Spring, quyền kiểm soát nhiều việc được đảo ngược sang framework. Bạn khai báo các component và contract; framework quyết định lúc nào tạo bean, inject dependency, gọi lifecycle callback, tạo proxy hoặc đăng ký controller.

Không có Spring:

```java
public static void main(String[] args) {
    DataSource dataSource = createDataSource();
    UserRepository repository = new JdbcUserRepository(dataSource);
    UserService service = new UserService(repository);
    UserController controller = new UserController(service);

    HttpServer server = createServer(controller);
    server.start();
}
```

Với Spring Boot, bạn thường chỉ viết:

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

Phần wiring lớn được chuyển sang Spring container.

Điều quan trọng là Spring không “đoán business logic”. Nó chỉ quản lý object và infrastructure dựa trên metadata/configuration bạn cung cấp.

**Senior Note.** Một cách rất hiệu quả để debug Spring là luôn dịch câu hỏi về Java thuần: “Object này do ai tạo?”, “Reference này được truyền vào khi nào?”, “Method này có đang được gọi qua proxy không?”, “Ai mở resource?”, “Ai chịu trách nhiệm close?”. Khi trả lời được các câu đó, phần lớn “Spring magic” biến thành một flow Java bình thường.

---

# 3. Spring Framework và Spring Boot khác nhau như thế nào?

Spring Framework là nền tảng. Nó cung cấp IoC container, DI, Spring MVC, transaction abstraction, data-access abstraction, AOP, event system, resource abstraction và testing support. Spring Boot sử dụng Spring Framework và thêm một lớp convention để giúp application bắt đầu nhanh hơn.

Nếu dùng Spring Framework thuần, bạn phải chủ động cấu hình nhiều thành phần. Với web application, bạn phải quan tâm servlet container, `DispatcherServlet`, message converters, JSON mapper, data source, transaction manager và rất nhiều wiring khác. Spring Boot nhìn vào classpath, configuration và các bean hiện có để tạo ra những default hợp lý.

Có thể hình dung như sau:

```text
Java
  ↓
Spring Framework
  ↓
Spring Boot
  ↓
Application của bạn
```

Spring Boot không thay thế Spring Framework. Boot là một cách **bootstrap, configure và vận hành Spring application** dễ hơn.

---

# 4. Version Spring cần học vào năm 2026

Khi học Spring, version quan trọng hơn nhiều người nghĩ vì cùng một bài tutorial có thể dùng package hoặc API đã lỗi thời. Có ba generation bạn cần nhận biết.

Spring Boot 2.7 đi cùng Spring Framework 5.3 là generation legacy nhưng vẫn tồn tại trong enterprise. Nó chạy được từ Java 8 và còn thuộc thế giới `javax.*`.

Spring Boot 3.x đi với Spring Framework 6.x, yêu cầu Java 17 trở lên và chuyển sang namespace `jakarta.*`. Đây là bước migration rất lớn.

Spring Boot 4.x đi với Spring Framework 7.x. Ở thời điểm tài liệu này, Spring Boot stable hiện tại là **4.1.1** và yêu cầu Java 17 trở lên, Spring Framework 7.0.9 trở lên; Boot 4 dựa trên Jakarta EE 11 và Servlet 6.1. Boot 4 cũng ưu tiên Jackson 3. Với project mới, đây là generation nên hiểu, nhưng bạn vẫn phải biết Boot 3 vì code enterprise hiện nay vẫn rất nhiều.

Ví dụ Boot 2 có thể dùng:

```java
import javax.validation.Valid;
import javax.persistence.Entity;
```

Boot 3/4 dùng:

```java
import jakarta.validation.Valid;
import jakarta.persistence.Entity;
```

Sự đổi tên này không chỉ là style. Library cũ phụ thuộc `javax.*` có thể không tương thích với application Jakarta mới.

**Senior Note.** Khi đọc Stack Overflow hoặc blog, trước tiên hãy nhìn năm bài viết, Java version và Spring Boot version. Một lời khuyên đúng cho Boot 2.1 có thể sai hoặc không còn cần thiết ở Boot 4.

---

# 5. Tạo một Spring Boot project và hiểu những file đang xuất hiện

Cách phổ biến nhất để tạo project là Spring Initializr tại `start.spring.io`. Bạn chọn build tool, Java version, Boot version và dependencies. Với backend cơ bản, Maven + Java 21 hoặc 25 + Spring Web + Validation là lựa chọn dễ học.

Một project Maven có thể có cấu trúc:

```text
demo/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/demo/
│   │   │       └── DemoApplication.java
│   │   └── resources/
│   │       └── application.yml
│   └── test/
│       └── java/
└── mvnw
```

`pom.xml` mô tả dependencies và build. `src/main/java` chứa source code. `src/main/resources` chứa configuration và resource. `src/test/java` chứa test. `mvnw` là Maven Wrapper để project có thể dùng version Maven phù hợp mà developer không cần tự quản lý Maven global quá chặt.

Main class:

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

Main class nên nằm gần root package `com.example.demo` để component scan mặc định nhìn thấy các subpackage như `com.example.demo.user`, `com.example.demo.order`.

---

# 6. Starter dependency là gì?

Spring Boot dùng “starter” để gom dependency theo use case. Nếu bạn muốn làm web application, thay vì tự thêm Spring MVC, Jackson, servlet container, logging integration và các transitive dependency tương thích, bạn thêm starter phù hợp.

Ví dụ:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

Validation:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

JPA:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

Starter không phải “một framework khác”. Nó chủ yếu là dependency bundle + sự phối hợp với Boot auto-configuration.

Một lợi ích lớn của Boot là **dependency management**. Boot phát hành một tập hợp version đã được kiểm thử cùng nhau. Vì vậy nếu dependency đã được Boot quản lý, bạn thường không tự ghi version. Tự ép Jackson, Hibernate hoặc Spring Framework sang một version khác chỉ vì “mới hơn” có thể gây lỗi linkage/runtime.

**Senior Pattern.** Hãy để platform/BOM quản lý dependency versions và chỉ override khi có lý do cụ thể, ví dụ security patch hoặc library compatibility đã được xác minh.

---

# 7. `@SpringBootApplication` thực sự có ý nghĩa gì?

`@SpringBootApplication` là annotation tổng hợp mang ba ý tưởng lớn: đây là một configuration class, application muốn dùng auto-configuration, và component scanning sẽ bắt đầu từ package hiện tại.

Bạn không nên học thuộc “nó bằng ba annotation” rồi dừng lại. Điều cần hiểu là annotation này nói với Boot: “hãy xây ApplicationContext cho application này, tìm các component của tôi, rồi dựa vào classpath/configuration để tạo những infrastructure bean cần thiết”.

Khi `SpringApplication.run(...)` chạy, một flow đơn giản có thể hình dung là: Boot chuẩn bị `Environment`, xác định loại application, tạo `ApplicationContext`, load bean definitions, chạy các processor, tạo singleton beans, cấu hình web server nếu đây là web application, rồi chuyển application sang trạng thái ready.

Các chi tiết sâu của flow này sẽ nằm ở Intermediate và Senior.

---

# 8. Bean là gì?

Bean là **object do Spring container quản lý**. Một object Java bình thường:

```java
User user = new User();
```

không tự nhiên trở thành Spring bean. Khi Spring biết cách tạo và quản lý `UserService`, instance `UserService` trong container là bean.

Ví dụ:

```java
@Service
public class UserService {
}
```

Spring component scan phát hiện class và đăng ký metadata để sau đó tạo bean.

Bean có thể được tạo từ component scanning hoặc từ `@Bean` method:

```java
@Configuration
public class TimeConfiguration {
    @Bean
    Clock clock() {
        return Clock.systemUTC();
    }
}
```

`Clock` là class của JDK nên bạn không thể thêm `@Component` vào source của nó. `@Bean` cho phép bạn nói rõ Spring phải tạo object bằng factory method nào.

**Programming Pattern.** Application components mà bạn sở hữu source thường dùng stereotype annotation. Infrastructure object hoặc third-party object thường được tạo rõ ràng trong `@Configuration`.

---

# 9. `ApplicationContext` là gì?

`ApplicationContext` là container cấp cao của Spring. Nó quản lý bean definitions và bean instances, dependency resolution, lifecycle, events, `Environment`, resources, messages và nhiều extension point.

Bạn có thể lấy bean thủ công:

```java
ApplicationContext context =
        SpringApplication.run(Application.class, args);

UserService service =
        context.getBean(UserService.class);
```

Nhưng business code bình thường không nên tự cầm `ApplicationContext` rồi `getBean()` ở khắp nơi. Làm vậy biến Spring thành Service Locator và che giấu dependencies.

Đúng hơn:

```java
@Service
public class OrderService {
    private final PaymentGateway gateway;

    public OrderService(PaymentGateway gateway) {
        this.gateway = gateway;
    }
}
```

Spring container chịu trách nhiệm tìm bean phù hợp và inject vào constructor.

---

# 10. `@Component`, `@Service`, `@Repository`, `@Controller`, `@RestController`

`@Component` là stereotype tổng quát. `@Service`, `@Repository` và `@Controller` truyền tải intent cụ thể hơn và cũng tham gia component scanning.

`@Service` nên dùng cho application/business service:

```java
@Service
public class UserService {
}
```

`@Repository` biểu thị data-access component:

```java
@Repository
public class JdbcUserRepository {
}
```

`@Controller` thuộc web MVC truyền thống có thể trả view. `@RestController` thường dùng cho REST API và response body được viết trực tiếp ra HTTP response thông qua message conversion.

```java
@RestController
@RequestMapping("/users")
public class UserController {
}
```

**Language Idiom.** Dùng stereotype thể hiện role thật. `@Component` không sai, nhưng `@Repository` nói nhiều hơn về kiến trúc so với một annotation generic.

**Senior Note.** Annotation không tạo “layer” một cách thần kỳ. Nếu `@Service` chứa SQL, HTTP parsing, file handling và security logic hỗn hợp, nó vẫn là God Service dù có annotation đúng tên.

---

# 11. Component Scan và lỗi “Spring không tìm thấy Bean”

Main class:

```text
com.example.demo.DemoApplication
```

mặc định scan các package phía dưới:

```text
com.example.demo.user
com.example.demo.order
com.example.demo.payment
```

Nếu `PaymentService` nằm ở:

```text
com.company.payment
```

nằm ngoài root scan, Spring có thể không tìm thấy.

Bạn có thể cấu hình scan:

```java
@ComponentScan({
    "com.example.demo",
    "com.company.payment"
})
```

nhưng không nên xử lý mọi lỗi bằng cách scan quá rộng như `"com"`. Điều đó làm container nhìn thấy component không chủ đích và làm object graph khó hiểu hơn.

**Senior Pattern.** Package structure là một architectural boundary. Main application class ở root package và package-by-feature thường giúp scanning tự nhiên.

---

# 12. Constructor Injection chi tiết

Giả sử:

```java
public interface UserRepository {
    Optional<User> findById(long id);
}
```

Implementation:

```java
@Repository
public class InMemoryUserRepository implements UserRepository {
}
```

Service:

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

Khi container tạo `UserService`, nó thấy constructor cần `UserRepository`, tìm bean compatible, thấy `InMemoryUserRepository`, tạo/resolve bean đó rồi truyền reference vào constructor.

Nếu class chỉ có một constructor, Spring hiện đại không cần `@Autowired` trên constructor.

Điều này tạo object giống Java thuần:

```java
UserRepository repository = new InMemoryUserRepository();
UserService service = new UserService(repository);
```

khác ở chỗ Spring làm wiring.

**Language Idiom.** Required dependency → constructor. Optional dependency chỉ nên optional nếu business/lifecycle thực sự cho phép thiếu.

---

# 13. Field Injection và vì sao không nên chọn làm default

Field injection:

```java
@Service
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

rất ngắn, nhưng dependency bị ẩn. Bạn có thể viết:

```java
new UserService();
```

và object tồn tại trong trạng thái chưa hợp lệ. Field không thể `final` theo cách bình thường. Unit test muốn tạo service phải dùng reflection/framework hoặc chạy Spring.

Constructor injection cho phép:

```java
UserService service =
        new UserService(fakeRepository);
```

không cần Spring.

Field injection vẫn xuất hiện rất nhiều trong code legacy, nên bạn phải đọc được. Nhưng khi viết mới, constructor injection là default tốt hơn.

---

# 14. Setter Injection dùng khi nào?

Setter injection:

```java
@Service
public class ReportService {
    private Exporter exporter;

    @Autowired
    public void setExporter(Exporter exporter) {
        this.exporter = exporter;
    }
}
```

có thể phù hợp nếu dependency thật sự thay đổi được hoặc optional theo lifecycle. Tuy nhiên phần lớn application service có required dependency nên constructor dễ reason hơn.

Đừng chọn setter chỉ vì “Spring hỗ trợ ba loại injection”. API tồn tại không có nghĩa mọi kiểu đều tốt như nhau.

---

# 15. Nhiều Bean cùng interface: `@Primary` và `@Qualifier`

Giả sử:

```java
public interface PaymentGateway {
    PaymentResult pay(Money money);
}
```

Có hai implementations:

```java
@Component
public class CardPaymentGateway implements PaymentGateway {
}
```

```java
@Component
public class BankPaymentGateway implements PaymentGateway {
}
```

Nếu `PaymentService` chỉ yêu cầu:

```java
PaymentService(PaymentGateway gateway)
```

container có hai candidates và không biết chọn cái nào.

`@Primary` nói rằng một bean là default:

```java
@Primary
@Component
public class CardPaymentGateway implements PaymentGateway {
}
```

`@Qualifier` chọn rõ candidate:

```java
public PaymentService(
        @Qualifier("bankPaymentGateway")
        PaymentGateway gateway) {
}
```

**Senior Note.** Nếu application phải chọn gateway động dựa trên `PaymentType`, rải `@Qualifier` vào business methods không phải thiết kế tốt. Ở Intermediate ta sẽ học inject `List`/`Map` strategy và tạo registry.

---

# 16. Bean Scope và ý nghĩa của Singleton

Default Spring bean scope là singleton, nghĩa là **một bean instance trên một ApplicationContext**, không phải một object duy nhất cho toàn JVM theo GoF Singleton.

```java
@Service
public class UserService {
}
```

nhiều HTTP request sẽ dùng cùng `UserService` instance.

Vì vậy đây là code nguy hiểm:

```java
@Service
public class UserService {
    private Long currentUserId;

    public User load(Long id) {
        this.currentUserId = id;
        ...
    }
}
```

Hai requests có thể ghi đè `currentUserId`.

Service singleton nên thường stateless:

```java
public User load(Long id) {
    return repository.findById(id)
            .orElseThrow();
}
```

State của request nằm trong local variables hoặc request-scoped/context object có chủ đích.

Spring còn có prototype, request, session và các web scopes khác. Beginner chỉ cần nhớ rằng “scope quyết định lifecycle và phạm vi chia sẻ object”. Không dùng prototype để thay cho `new` của mọi domain object.

---

# 17. Bean lifecycle: object được tạo và huỷ lúc nào?

Một bean singleton đơn giản trải qua flow gần như:

```text
Spring biết BeanDefinition
→ tạo instance
→ inject dependencies
→ thực hiện post-processing/lifecycle callback
→ bean sẵn sàng sử dụng
→ ApplicationContext đóng
→ destruction callback
```

Bạn có thể dùng:

```java
@PostConstruct
void initialize() {
    ...
}
```

và:

```java
@PreDestroy
void shutdown() {
    ...
}
```

với package Jakarta:

```java
jakarta.annotation.PostConstruct
jakarta.annotation.PreDestroy
```

`@PostConstruct` không nên biến thành nơi chạy network call vô hạn hoặc migration lớn. Nếu startup dependency không bounded, deployment có thể treo.

`@PreDestroy` phù hợp để close resource do bean sở hữu.

**Programming Pattern — Resource Ownership.** Component tạo resource thì component đó nên có trách nhiệm quản lý lifecycle của resource. Nếu bean tạo client/executor, cần biết khi context đóng resource được đóng bằng cách nào.

---

# 18. `@Configuration` và `@Bean` như Java-based configuration

Ví dụ:

```java
@Configuration
public class PaymentConfiguration {

    @Bean
    PaymentClient paymentClient(
            PaymentProperties properties) {

        return new PaymentClient(
                properties.baseUrl(),
                properties.timeout()
        );
    }
}
```

`@Configuration` nói rằng class này chứa bean definitions/configuration. `@Bean` nói rằng return value của method sẽ được container quản lý.

Điều hay của method parameter là dependency explicit:

```java
@Bean
OrderService orderService(
        OrderRepository repository,
        Clock clock) {
    return new OrderService(repository, clock);
}
```

Đọc method là thấy ngay dependencies.

**Design Pattern.** `@Bean` giống Factory Method ở mức khái niệm; container trở thành object factory lớn quản lý lifecycle và dependency graph.

---

# 19. Spring Boot Auto-Configuration: “magic” đầu tiên cần hiểu

Bạn thêm `spring-boot-starter-web` rồi application tự có web server, JSON, MVC. Đây là auto-configuration.

Boot xem các điều kiện như class nào đang có trên classpath, application có phải servlet web application không, property nào bật/tắt, và bạn đã tự tạo bean nào chưa. Nếu điều kiện phù hợp, Boot đăng ký default infrastructure bean.

Mental model quan trọng nhất là **default + back-off**. Boot cố gắng cho bạn default hợp lý, nhưng khi bạn cung cấp bean/config riêng, auto-configuration thường lùi lại.

Ví dụ concept:

```java
@Bean
@ConditionalOnMissingBean
SomeClient someClient() {
    return defaultClient();
}
```

Nếu application đã có `SomeClient`, default không được tạo.

**Senior Idiom.** Spring Boot không phải “convention over configuration” theo nghĩa không cấu hình được. Nó là “sensible defaults, explicit override”.

---

# 20. Configuration bên ngoài application

Hard-code:

```java
String apiUrl = "https://prod.example.com";
```

là vấn đề vì local, test và production cần giá trị khác nhau. Spring Boot có externalized configuration.

`application.yml`:

```yaml
spring:
  application:
    name: user-service

server:
  port: 8080

payment:
  base-url: https://pay.example.com
  timeout: 2s
```

Bạn có thể override bằng environment variable hoặc command-line property tùy deployment.

Configuration không phải business code. Nó là input của application.

---

# 21. `@Value` và khi nào nên dùng

Simple value:

```java
@Service
public class PaymentClient {
    private final Duration timeout;

    public PaymentClient(
            @Value("${payment.timeout:2s}")
            Duration timeout) {
        this.timeout = timeout;
    }
}
```

`:2s` là default trong placeholder syntax.

`@Value` tiện cho một vài giá trị nhỏ, nhưng khi có nhiều property cùng nhóm, typed configuration tốt hơn.

---

# 22. `@ConfigurationProperties`: cách cấu hình nên học sớm

```java
@ConfigurationProperties("payment")
public record PaymentProperties(
        URI baseUrl,
        Duration timeout
) {
}
```

YAML:

```yaml
payment:
  base-url: https://pay.example.com
  timeout: 2s
```

Spring bind text configuration vào type thật. `timeout` trở thành `Duration`, URL trở thành `URI`. Điều này tốt hơn `String` vì invalid format có thể fail sớm.

Bạn có thể đăng ký qua `@ConfigurationPropertiesScan` hoặc `@EnableConfigurationProperties`.

**Programming Pattern — Typed Configuration.** Parse và validate external configuration một lần ở boundary, sau đó core application sử dụng type có nghĩa.

**Senior Note.** `int timeout = 3` rất tệ nếu không biết đơn vị là giây hay millisecond. `Duration` làm unit explicit.

---

# 23. Profiles dùng để làm gì?

Profiles giúp chọn configuration/bean theo environment hoặc deployment context. Ví dụ `application-local.yml` có local DB, còn production lấy secrets từ runtime environment.

Bean-specific profile:

```java
@Bean
@Profile("local")
PaymentGateway fakePaymentGateway() {
    return new FakePaymentGateway();
}
```

Profiles không nên trở thành business feature engine. Nếu bạn có `@Profile("customerA")`, `@Profile("customerB")`, `@Profile("customerC")` rải khắp application, có thể business variation đang bị biến thành deployment variation.

---

# 24. HTTP là gì trước khi học Spring MVC?

Backend REST là chương trình nhận HTTP request và trả HTTP response. Request gồm method, URL/path, headers và có thể có body. Response gồm status code, headers và body.

Ví dụ:

```http
GET /users/42
Accept: application/json
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":42,"name":"Kim"}
```

Các HTTP methods thường gặp là GET để đọc, POST để tạo/trigger operation, PUT để thay thế/cập nhật resource theo contract, PATCH cho partial change và DELETE để xoá. Đây là HTTP semantics chứ không phải Spring invention.

Status code cũng là HTTP. `200` là thành công phổ biến, `201` thường dùng khi tạo resource, `204` là thành công không có body, `400` là request invalid, `401` liên quan authentication, `403` liên quan authorization, `404` không tìm thấy, `409` conflict và `500` là server error.

Spring MVC chỉ giúp map HTTP world vào Java methods.

---

# 25. Servlet và DispatcherServlet ở mức Beginner

Trong Servlet-based Spring MVC, embedded server như Tomcat nhận TCP/HTTP request rồi đưa request vào Servlet stack. Spring MVC có `DispatcherServlet` đóng vai trò **Front Controller**. Nó nhận request đã vào Spring MVC, tìm controller method phù hợp, resolve arguments, gọi method, xử lý return value và viết response.

Mental model:

```text
Browser / Mobile / Client
          ↓
      Web Server
          ↓
     Servlet stack
          ↓
  DispatcherServlet
          ↓
      Controller
          ↓
       Service
          ↓
      Repository
```

Ở Beginner bạn chưa cần biết `HandlerMapping` hay `HandlerAdapter`; Intermediate sẽ mở flow đó.

**Design Pattern — Front Controller.** Thay vì mỗi endpoint tự làm toàn bộ infrastructure, một entry point trung tâm dispatch request đến handler phù hợp.

---

# 26. Viết REST Controller đầu tiên

```java
@RestController
@RequestMapping("/users")
public class UserController {

    @GetMapping("/{id}")
    public UserResponse get(
            @PathVariable long id) {

        return new UserResponse(id, "Kim");
    }
}
```

`@RequestMapping("/users")` tạo base path. `@GetMapping("/{id}")` match GET request như `/users/10`. `@PathVariable` lấy phần `{id}` rồi conversion thành `long`.

Response record:

```java
public record UserResponse(
        long id,
        String name) {
}
```

Spring MVC dùng message converter, thông thường với Jackson JSON integration, để biến object thành JSON.

---

# 27. `@RequestParam`

Request:

```text
GET /users?page=0&size=20&keyword=kim
```

Controller:

```java
@GetMapping
public List<UserResponse> find(
        @RequestParam(defaultValue = "0")
        int page,

        @RequestParam(defaultValue = "20")
        int size,

        @RequestParam(required = false)
        String keyword) {
    ...
}
```

`@RequestParam` dùng query parameter. `@PathVariable` thường dùng identity/path segment. Đừng cố nhét mọi thứ vào path.

---

# 28. `@RequestHeader`

```java
@GetMapping("/me")
public UserResponse me(
        @RequestHeader("X-Request-Id")
        String requestId) {
    ...
}
```

Headers thường chứa metadata như authorization, content negotiation, tracing/correlation, conditional request và caching directives.

Không nên dùng custom header để nhét toàn bộ business payload.

---

# 29. `@RequestBody` và JSON → Java

Request:

```http
POST /users
Content-Type: application/json

{
  "name": "Kim",
  "email": "kim@example.com"
}
```

DTO:

```java
public record CreateUserRequest(
        String name,
        String email) {
}
```

Controller:

```java
@PostMapping
public UserResponse create(
        @RequestBody
        CreateUserRequest request) {
    ...
}
```

Spring chọn JSON message converter và Jackson đọc body thành Java object.

Điều quan trọng là `@RequestBody` không phải “API đọc JSON” độc lập. Nó là chỉ dẫn cho MVC argument-resolution/message-conversion infrastructure.

---

# 30. DTO là gì và tại sao không nên dùng Entity làm request/response?

DTO là object dùng để vận chuyển dữ liệu qua boundary. HTTP request DTO đại diện contract client được phép gửi. HTTP response DTO đại diện contract server công khai.

Nếu bạn dùng JPA entity trực tiếp:

```java
@PostMapping
public UserEntity create(
        @RequestBody UserEntity entity) {
    ...
}
```

client có thể gửi field không nên được phép thay đổi, entity lifecycle bị leak ra web layer, lazy relationships có thể trigger SQL trong serialization và database refactor có thể vô tình phá public API.

Tốt hơn:

```java
public record CreateUserRequest(
        String name,
        String email) {
}
```

và:

```java
public record UserResponse(
        long id,
        String name,
        String email) {
}
```

**Programming Pattern — Boundary DTO.** Transport contract được tách khỏi persistence/domain representation.

**Senior Note.** Tách boundary không có nghĩa phải tạo DTO cho từng private method. Mapping ceremony chỉ có giá trị ở boundary có ý nghĩa.

---

# 31. `ResponseEntity` và khi nào cần

Bạn có thể return DTO trực tiếp:

```java
@GetMapping("/{id}")
public UserResponse get(
        @PathVariable long id) {
    return service.get(id);
}
```

Spring trả 200 theo default.

Nếu cần control status/header:

```java
@PostMapping
public ResponseEntity<UserResponse> create(
        @RequestBody CreateUserRequest request) {

    UserResponse response = service.create(request);

    return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(response);
}
```

Không cần bọc mọi response trong `ResponseEntity` nếu bạn không cần control thêm.

---

# 32. Validation là gì?

JSON syntactically hợp lệ chưa chắc input hợp lệ. Ví dụ:

```json
{
  "name": "",
  "email": "abc"
}
```

có JSON đúng nhưng dữ liệu sai.

Bean Validation cho phép mô tả constraints:

```java
public record CreateUserRequest(
        @NotBlank
        @Size(max = 100)
        String name,

        @NotBlank
        @Email
        String email) {
}
```

Controller:

```java
@PostMapping
public UserResponse create(
        @Valid
        @RequestBody
        CreateUserRequest request) {
    ...
}
```

`@Valid` yêu cầu validation cascade vào request object.

---

# 33. `@NotNull`, `@NotEmpty`, `@NotBlank`

`@NotNull` chỉ nói value không được `null`. Chuỗi `""` vẫn pass.

`@NotEmpty` nói collection/string không null và không rỗng, nhưng string `"   "` vẫn có độ dài và có thể pass.

`@NotBlank` dành cho text; nó reject null, empty và chỉ-whitespace. Vì vậy required user name thường hợp với `@NotBlank`.

Ví dụ:

```java
@NotNull
private LocalDate birthday;

@NotBlank
private String displayName;

@NotEmpty
private List<String> roles;
```

---

# 34. Validation không thay business rules

`@Email` có thể kiểm tra email format. Nó không biết email đã được đăng ký hay chưa.

`@Positive` có thể kiểm tra amount > 0. Nó không biết account có đủ balance.

Nên phân biệt:

```text
Boundary validation
→ shape / format / required / range

Business invariant
→ rule của domain/use case
```

Ví dụ duplicate email nên được kiểm tra ở application/domain/persistence rule, không cố viết một validator annotation gọi DB cho mọi case.

---

# 35. Centralized Exception Handling

Nếu mỗi controller viết:

```java
try {
    ...
} catch (UserNotFoundException e) {
    ...
}
```

thì error handling bị lặp.

Spring có `@RestControllerAdvice`:

```java
@RestControllerAdvice
public class ApiExceptionHandler {

    @ExceptionHandler(UserNotFoundException.class)
    ResponseEntity<ApiError> handleUserNotFound(
            UserNotFoundException e) {

        return ResponseEntity
                .status(HttpStatus.NOT_FOUND)
                .body(new ApiError(
                        "USER_NOT_FOUND",
                        e.getMessage()
                ));
    }
}
```

DTO:

```java
public record ApiError(
        String code,
        String message) {
}
```

Error code như `USER_NOT_FOUND` ổn định hơn việc client phụ thuộc raw Java class name hoặc raw English message.

---

# 36. `ProblemDetail`

Spring hiện đại hỗ trợ `ProblemDetail` để biểu diễn lỗi HTTP theo model chuẩn hóa.

```java
ProblemDetail problem =
        ProblemDetail.forStatus(
                HttpStatus.NOT_FOUND);

problem.setTitle("User not found");
problem.setProperty(
        "code",
        "USER_NOT_FOUND");
```

Bạn không bắt buộc phải dùng ngay ở Beginner, nhưng nên biết nó tồn tại vì error response trong Spring mới không chỉ có custom DTO.

**Senior Note.** Public error response không nên lộ stack trace, SQL, table name, filesystem path hoặc internal host.

---

# 37. Controller, Service, Repository: vì sao cần tách?

Controller hiểu HTTP. Service hiểu use case. Repository hiểu persistence.

Controller:

```java
@RestController
class UserController {
    private final UserService service;
}
```

Service:

```java
@Service
class UserService {
    private final UserRepository repository;
}
```

Repository:

```java
public interface UserRepository {
    Optional<User> findById(UserId id);
}
```

Đây là layered architecture đơn giản, tốt cho Beginner vì responsibility rõ.

Nếu controller viết SQL trực tiếp, business logic gắn với HTTP và database cùng lúc. Test khó hơn và thay transport/persistence khó hơn.

**Programming Pattern — Thin Controller.** Controller chỉ nhận/validate/map HTTP, gọi use case rồi map response.

**Design Pattern — Repository.** Repository che persistence mechanics khỏi application/domain code.

---

# 38. Domain Object và Spring Bean khác nhau

Không phải mọi object đều nên là bean.

Spring beans thường là long-lived services/infrastructure:

```text
Controller
Service
Repository
HTTP client
Configuration
Scheduler
```

Domain/value objects:

```text
Order
Money
Address
UserId
Email
```

thường được tạo bằng `new`, factory hoặc load từ persistence.

Ví dụ `Money` không cần:

```java
@Component
public class Money {
}
```

Nó không phải shared service.

**Senior Note.** “Spring-managed everything” tạo domain model phụ thuộc framework vô ích.

---

# 39. Repository interface trước database

Để học DI mà không bị database làm rối, hãy bắt đầu bằng in-memory repository.

```java
public interface UserRepository {
    User save(User user);
    Optional<User> findById(long id);
}
```

Implementation:

```java
@Repository
public class InMemoryUserRepository
        implements UserRepository {

    private final Map<Long, User> users =
            new ConcurrentHashMap<>();

    private final AtomicLong sequence =
            new AtomicLong();

    @Override
    public User save(User user) {
        long id = sequence.incrementAndGet();
        User saved = user.withId(id);
        users.put(id, saved);
        return saved;
    }

    @Override
    public Optional<User> findById(long id) {
        return Optional.ofNullable(
                users.get(id));
    }
}
```

Khi chuyển sang JDBC, `UserService` không cần thay đổi nếu contract repository giữ nguyên. Đây là lợi ích Dependency Inversion nhìn thấy rất rõ.

---

# 40. JDBC là gì trước khi học Spring JDBC?

JDBC là Java standard API để làm việc với relational database.

Plain JDBC flow:

```text
get Connection
prepare SQL
bind parameters
execute
read ResultSet
close ResultSet
close Statement
close Connection
translate SQLException
```

Code rất nhiều boilerplate.

Spring JDBC không thay SQL. Nó giảm boilerplate quanh JDBC.

---

# 41. DataSource là gì?

`DataSource` là abstraction cung cấp database connections. Trong production, nó thường đại diện connection pool thay vì mở physical connection mới cho mọi query.

Boot có thể auto-configure `DataSource` khi driver và configuration phù hợp tồn tại.

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/demo
    username: demo
    password: ${DB_PASSWORD}
```

Không commit secret thật vào Git.

---

# 42. `JdbcTemplate`

Repository:

```java
@Repository
public class JdbcUserRepository
        implements UserRepository {

    private final JdbcTemplate jdbcTemplate;

    public JdbcUserRepository(
            JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public Optional<User> findById(long id) {
        List<User> rows =
                jdbcTemplate.query(
                    """
                    select id, name, email
                    from users
                    where id = ?
                    """,
                    (rs, rowNum) ->
                        new User(
                            rs.getLong("id"),
                            rs.getString("name"),
                            rs.getString("email")
                        ),
                    id
                );

        return rows.stream().findFirst();
    }
}
```

Spring handles resource cleanup and exception translation around common JDBC flow, nhưng SQL vẫn do bạn kiểm soát.

**Senior Note.** Framework abstraction không thay kiến thức index, join, transaction, query plan và locking.

---

# 43. `JdbcClient`

Spring Framework hiện đại có `JdbcClient`, một fluent facade cho common JDBC operations.

Concept:

```java
jdbcClient
    .sql("""
        select id, name
        from users
        where id = :id
    """)
    .param("id", id)
    .query(...)
```

Bạn không cần chọn `JdbcClient` ngay để học. Điều quan trọng là hiểu cả `JdbcTemplate` và `JdbcClient` đều nằm trên JDBC; chúng không phải ORM.

---

# 44. ORM, JPA, Hibernate và Spring Data JPA

Đây là bốn khái niệm thường bị trộn.

**ORM** là kỹ thuật map object với relational database.

**JPA/Jakarta Persistence** là specification/API tiêu chuẩn cho persistence trong Java ecosystem.

**Hibernate** là một implementation ORM/JPA rất phổ biến.

**Spring Data JPA** là layer của Spring giúp tạo repository abstraction và query support trên JPA.

Dependency:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

Entity:

```java
@Entity
@Table(name = "users")
public class UserEntity {

    @Id
    @GeneratedValue(
        strategy = GenerationType.IDENTITY
    )
    private Long id;

    private String name;
    private String email;
}
```

Repository:

```java
public interface UserJpaRepository
        extends JpaRepository<UserEntity, Long> {
}
```

Spring Data tạo implementation proxy cho interface.

---

# 45. `@Entity`, `@Table`, `@Id`, `@GeneratedValue`

`@Entity` nói class là persistence entity. `@Table` map table name khi cần. `@Id` đánh dấu primary identity trong JPA. `@GeneratedValue` mô tả strategy sinh ID.

Các generation strategies như `IDENTITY`, `SEQUENCE`, `AUTO` không chỉ là syntax. Chúng ảnh hưởng cách ORM insert và batch. Chi tiết sẽ sang Intermediate/Senior.

---

# 46. Transaction là gì trước khi học `@Transactional`?

Transaction là một nhóm database operations được coi như một unit. Ví dụ chuyển tiền:

```text
trừ account A
+
cộng account B
```

Nếu operation thứ hai fail mà operation thứ nhất đã commit, dữ liệu sai. Transaction giúp hai thay đổi commit cùng hoặc rollback cùng trong cùng transactional resource.

Plain JDBC:

```java
connection.setAutoCommit(false);

try {
    debit(connection);
    credit(connection);
    connection.commit();
} catch (Exception e) {
    connection.rollback();
    throw e;
}
```

Spring cho phép declarative transaction:

```java
@Transactional
public void transfer(...) {
    debit(...);
    credit(...);
}
```

Nhưng annotation hoạt động nhờ transaction infrastructure/proxy. Đây là lý do hiểu proxy ở Intermediate rất quan trọng.

---

# 47. `@Transactional` ở Beginner nên hiểu đến đâu?

Ở Beginner, hãy hiểu ba điều. Thứ nhất, transaction boundary nên gần business use case. Thứ hai, method chạy trong transaction có thể commit hoặc rollback dựa trên kết quả/exception. Thứ ba, `@Transactional` không biến HTTP call sang service khác thành cùng database transaction.

Một anti-pattern:

```java
@Transactional
public void checkout() {
    orderRepository.save(...);
    externalPaymentApi.call();
    emailApi.send();
}
```

Method có thể giữ DB connection/locks trong khi chờ network, và transaction local không thể rollback payment đã hoàn thành ở external service.

Chi tiết propagation, isolation và rollback rules sẽ ở Intermediate.

---

# 48. Database Migration: tại sao không để ORM tự sửa schema production?

Demo có thể dùng JPA DDL auto. Production cần schema evolution được version-control.

Hai tools phổ biến:

```text
Flyway
Liquibase
```

Flyway thường dùng SQL migration:

```text
V1__create_users.sql
V2__add_user_email_index.sql
```

Application version và database schema version phải evolve có kiểm soát.

Bạn chưa cần học sâu ở Beginner, nhưng hãy hình thành nguyên tắc: **schema migration là artifact của software delivery**, không phải thao tác thủ công ngẫu nhiên trên production DB.

---

# 49. Spring HTTP Client: gọi API bên ngoài

Backend không chỉ nhận HTTP; nó còn gọi service khác.

Spring hiện đại có `RestClient` cho synchronous imperative client:

```java
RestClient restClient =
        RestClient.builder()
                .baseUrl(
                    "https://api.example.com")
                .build();

UserResponse user =
        restClient.get()
                .uri("/users/{id}", id)
                .retrieve()
                .body(UserResponse.class);
```

Code thật nên cấu hình client thành bean, externalize base URL/timeout và translate lỗi.

Legacy project có `RestTemplate`. Reactive stack có `WebClient`.

Beginner chỉ cần hiểu sự khác nhau: `RestClient` phù hợp synchronous imperative style; `WebClient` thuộc reactive/non-blocking style và cần học Reactor để dùng đúng.

---

# 50. Timeout là requirement, không phải option phụ

External call có thể treo/chậm. Nếu không có timeout, request thread hoặc virtual thread có thể chờ rất lâu, connection bị chiếm và system có thể cascade failure.

Do đó client config cần nghĩ đến:

```text
connect timeout
response/read timeout
overall deadline
```

Exact API phụ thuộc underlying client.

**Senior Pattern — Bounded Waiting.** Mọi remote/blocking dependency cần giới hạn thời gian. “Không giới hạn” là một failure policy, thường là policy tệ.

---

# 51. Logging trong Spring Boot

Không dùng `System.out.println` làm logging production.

SLF4J style:

```java
private static final Logger log =
        LoggerFactory.getLogger(
                UserService.class);

log.info(
        "Created user id={}",
        user.id()
);
```

Parameterized logging tránh xây chuỗi không cần thiết khi log level không bật và tạo format thống nhất.

Không log password, access token, refresh token, private keys hoặc raw sensitive data.

---

# 52. Actuator là gì?

`spring-boot-starter-actuator` cung cấp production-oriented management features.

Health:

```text
/actuator/health
```

Các endpoint/capability khác có thể liên quan metrics, config, mappings, thread dump và runtime insight, tùy exposure.

Health endpoint thường được load balancer hoặc Kubernetes dùng để biết application có sẵn sàng không.

**Senior Note.** Management endpoints có thể lộ thông tin nhạy cảm. Không expose tất cả ra public Internet.

---

# 53. Liveness và Readiness

Liveness trả lời: “process có bị hỏng đến mức restart có thể giúp không?”

Readiness trả lời: “instance có nên nhận traffic mới không?”

Database tạm thời down thường làm application không ready, nhưng kill/restart liên tục application chưa chắc giúp DB sống lại.

Đây là semantics vận hành, không chỉ endpoint naming.

---

# 54. Unit Test không cần Spring

Service:

```java
public final class PriceService {
    private final DiscountPolicy policy;

    public PriceService(
            DiscountPolicy policy) {
        this.policy = policy;
    }

    public Money calculate(Money price) {
        return policy.apply(price);
    }
}
```

Unit test:

```java
@Test
void appliesDiscount() {
    DiscountPolicy policy =
            price -> price.multiply(
                    new BigDecimal("0.9"));

    PriceService service =
            new PriceService(policy);

    ...
}
```

Không có lý do load Spring context nếu test chỉ cần plain Java behavior.

**Language Idiom.** “Don’t start Spring if you don’t need Spring.”

---

# 55. `@SpringBootTest`

```java
@SpringBootTest
class ApplicationIntegrationTest {
}
```

annotation này load Boot application context lớn hơn, phù hợp test wiring/auto-configuration/integration.

Nếu mọi test đều `@SpringBootTest`, suite chậm và lỗi khó localize.

---

# 56. MVC test

`@WebMvcTest` tập trung vào web layer.

Concept:

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
}
```

Bạn có thể replace service dependency bằng test mock theo Spring Test version hiện đại.

Mục tiêu là test:

```text
routing
JSON
validation
status
exception advice
```

không cần real DB.

Intermediate sẽ đi sâu test slices và Boot 4 testing APIs.

---

# 57. Security: Beginner cần hiểu gì?

Spring Security là một subsystem lớn. Đừng học nó bằng cách copy một `SecurityFilterChain` rồi disable tất cả để request chạy.

Bạn chỉ cần nắm mental model:

```text
Request
↓
Security filter chain
↓
Authentication
↓
Authorization
↓
Controller
```

Authentication trả lời “ai đang gọi”. Authorization trả lời “người này có được phép làm operation không”.

`401` thường liên quan authentication chưa thành công. `403` thường liên quan caller đã được nhận diện nhưng không có quyền.

CORS và CSRF là security/browser topics khác nhau. CORS không phải authentication. CSRF không nên bị disable chỉ vì “API đang trả 403”.

---

# 58. `@Async`, `@Scheduled`, cache và event: chỉ awareness ở Beginner

Spring có `@Async`, `@Scheduled`, cache annotations và application events. Bạn sẽ gặp chúng rất sớm nên cần biết chúng tồn tại, nhưng không nên dùng trước khi hiểu semantics.

`@Async` đưa execution sang executor/thread khác. Điều đó làm transaction context, exception handling và context propagation phức tạp.

`@Scheduled` chạy task theo scheduler của mỗi application instance. Nếu deploy 3 replicas, job có thể chạy 3 lần.

`@Cacheable` có thể bỏ qua method khi cache hit, nhưng annotation không tự quyết định TTL, size, eviction hoặc distributed consistency.

`@EventListener` là in-process event listener và mặc định không phải durable messaging giống Kafka.

Intermediate sẽ mở tất cả các phần này.

---

# 59. Package structure nên dùng khi bắt đầu

Thay vì:

```text
controller/
service/
repository/
entity/
```

cho toàn project, package by feature giúp code liên quan nằm gần nhau:

```text
user/
  UserController
  UserService
  UserRepository
  User
  UserResponse

order/
  OrderController
  OrderService
  OrderRepository
```

Project nhỏ dùng layered packages vẫn được. Nhưng khi lớn, package-by-feature thường giúp cohesion tốt hơn.

**Senior Note.** Folder structure không chữa được coupling nếu các module gọi nhau tùy tiện. Boundary là dependency rules, không chỉ thư mục.

---

# 60. Một REST flow hoàn chỉnh

Request:

```http
POST /users
Content-Type: application/json

{
  "name": "Kim",
  "email": "kim@example.com"
}
```

Request DTO:

```java
public record CreateUserRequest(
        @NotBlank String name,
        @NotBlank @Email String email) {
}
```

Controller:

```java
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService service;

    public UserController(
            UserService service) {
        this.service = service;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public UserResponse create(
            @Valid
            @RequestBody
            CreateUserRequest request) {

        User user = service.create(
                request.name(),
                request.email());

        return new UserResponse(
                user.id(),
                user.name(),
                user.email());
    }
}
```

Service:

```java
@Service
public class UserService {

    private final UserRepository repository;

    public UserService(
            UserRepository repository) {
        this.repository = repository;
    }

    public User create(
            String name,
            String email) {

        User user =
                User.create(name, email);

        return repository.save(user);
    }
}
```

Flow:

```text
HTTP JSON
→ Jackson/MessageConverter
→ CreateUserRequest
→ Bean Validation
→ UserController
→ UserService
→ UserRepository
→ DB/in-memory
→ User
→ UserResponse
→ JSON
```

Đây là mental model nền tảng bạn phải nhìn thấy trước khi học internals.

---

# 61. Language Idioms cần hình thành ở Beginner

**Constructor Injection.** Required dependencies đi vào constructor và field nên `final` khi có thể. Điều này làm object luôn hợp lệ sau construction.

**Thin Controller.** Controller chỉ chịu transport concerns: nhận request, validation, mapping, status/headers và gọi use case.

**Stateless Singleton Service.** Không lưu state của từng request vào field của singleton bean.

**Typed Configuration.** Dùng `Duration`, `URI`, enum và configuration property object thay vì rải `String`/`int` magic values.

**Boundary DTO.** Public HTTP contract không phải persistence entity.

**Fail Fast.** Required config sai hoặc dependency thiếu nên fail lúc startup nếu có thể, thay vì chờ production request đầu tiên mới phát hiện.

---

# 62. Coding / Programming Patterns cần nhận ra

**Repository Pattern** đặt abstraction giữa business logic và persistence. **Dependency Injection** externalize object wiring. **Configuration Object** gom typed settings. **Exception Translation** chuyển lỗi infrastructure thành lỗi có nghĩa ở application boundary. **Guard Clause** giảm nesting trong service/domain. **Resource Ownership** xác định rõ ai tạo và ai close. **Layered Architecture** giúp Beginner hiểu separation of concerns. Sau này các pattern này sẽ được nâng lên Ports & Adapters, Outbox, Idempotency và Resilience.

---

# 63. Design Patterns liên hệ trực tiếp với Spring

Spring Container có vai trò gần **Factory** vì nó tạo object. `DispatcherServlet` là **Front Controller**. `JdbcTemplate` là ví dụ nổi tiếng của **Template Method/Template-style abstraction**: framework quản lý flow lặp lại, caller cung cấp phần biến đổi. Spring AOP và nhiều annotation infrastructure dựa trên **Proxy**. Dependency selection có thể implement **Strategy**. HTTP/database/vendor integrations thường đóng vai trò **Adapter**.

Không cần học thuộc tên pattern trước khi hiểu problem. Pattern chỉ hữu ích khi bạn hiểu lực kéo thiết kế mà nó giải quyết.

---

# 64. Các lỗi Beginner thường gặp và cách suy nghĩ đúng

Lỗi đầu tiên là dùng `new` để tạo một service vốn được Spring quản lý, rồi thắc mắc vì sao dependency không được inject. Nếu class là bean, hãy để container tạo nó hoặc chỉ `new` nó trong unit test với dependency explicit.

Lỗi thứ hai là field injection vì ngắn. Hãy ưu tiên constructor.

Lỗi thứ ba là đưa business logic vào controller. Controller là HTTP adapter, không phải domain.

Lỗi thứ tư là dùng entity làm request/response. Hãy tách boundary DTO.

Lỗi thứ năm là hard-code URL/password/timeout. Hãy externalize typed configuration.

Lỗi thứ sáu là thêm `@Transactional`, `@Async`, `@Cacheable` như “fix annotation” mà không hiểu proxy/execution context. Nếu behavior phụ thuộc proxy, self-call hoặc lifecycle có thể làm annotation không hoạt động như bạn tưởng.

Lỗi thứ bảy là đọc tutorial Boot 2 rồi copy `javax.*` vào Boot 4. Luôn check generation.

---

# 65. Mini Project Beginner: User Management API

Hãy xây một application có các endpoint `POST /users`, `GET /users/{id}`, `GET /users`, `PUT /users/{id}` và `DELETE /users/{id}`. Bắt đầu bằng `InMemoryUserRepository` để tập trung vào Spring Core, DI, MVC, validation và exception handling. Khi flow chạy ổn, thay repository bằng Spring JDBC mà không đổi contract của service. Sau đó thêm JPA implementation để cảm nhận sự khác biệt giữa JDBC và ORM.

Project phải có typed `@ConfigurationProperties`, một `Clock` bean để test time-dependent logic, global error handling, Actuator health, unit test service không load Spring, MVC test và ít nhất một full integration test.

Khi bạn thay repository implementation mà controller/service gần như không phải đổi, bạn đã thực sự hiểu giá trị của DI thay vì chỉ thuộc `@Autowired`.

---

# 66. Beginner → Intermediate Gate

Bạn sẵn sàng sang Intermediate khi có thể tự giải thích, bằng lời của mình, một request từ browser đi qua embedded server và Spring MVC đến controller/service/repository rồi quay về JSON. Bạn phải giải thích được Spring bean khác object Java bình thường ở đâu, ApplicationContext làm gì, constructor injection hoạt động thế nào, `@Component` khác `@Bean` về cách registration, singleton scope có ý nghĩa gì, vì sao singleton service không tự thread-safe, bean lifecycle cơ bản ra sao và auto-configuration dựa trên classpath/configuration/defaults như thế nào.

Ở web layer, bạn phải hiểu `@PathVariable`, `@RequestParam`, `@RequestBody`, DTO, validation, HTTP status và global exception handling. Ở persistence, bạn phải phân biệt JDBC, Spring JDBC, JPA, Hibernate và Spring Data JPA. Với transaction, bạn chưa cần thuộc propagation nhưng phải hiểu atomic local database unit và biết `@Transactional` không tạo distributed transaction. Với testing, bạn phải hiểu vì sao plain unit test không cần Spring context.

Nếu bạn chỉ nhớ “annotation X dùng để Y” nhưng không trace được flow, chưa nên sang Intermediate.

---

# 67. Bạn sẽ học gì ở Part 2?

Part 2 sẽ mở chiếc hộp mà Part 1 mới chỉ nhìn từ bên ngoài. Bạn sẽ học `BeanDefinition`, `BeanFactory`, `ApplicationContext`, bean creation phases, post-processors, `FactoryBean`, `ObjectProvider`, scoped proxy và dependency candidate resolution. Spring MVC sẽ được mở thành `DispatcherServlet → HandlerMapping → HandlerAdapter → ArgumentResolver → HttpMessageConverter`. `@Transactional` sẽ được giải bằng proxy, transaction manager, physical/logical transaction, propagation, isolation, rollback-only và resource binding.

Persistence sẽ đi vào entity lifecycle, persistence context, dirty checking, lazy loading, N+1, fetch strategy, pagination và locking. Sau đó mới đến RestClient/HTTP interface, WebClient, events, async, scheduling, caching, Security, test slices, Testcontainers, Actuator, Micrometer và Virtual Threads.

Đó là lúc Spring chuyển từ “framework tôi đang dùng” thành “runtime model tôi hiểu”.

---

# 68. Version references

Các phần phụ thuộc version trong file này dựa trên documentation chính thức hiện tại. Spring Boot system requirements: https://docs.spring.io/spring-boot/system-requirements.html

Spring Framework reference: https://docs.spring.io/spring-framework/reference/

Spring Boot reference: https://docs.spring.io/spring-boot/reference/

Boot 4 migration guide: https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Khi đọc tài liệu cũ, luôn xác định nó thuộc Boot 2, Boot 3 hay Boot 4 trước khi copy code.

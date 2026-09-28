# Java Spring — Part 1: Beginner

> **Mạch đọc:** Đọc **Java Spring — Part 1: Beginner** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Học Spring khung phần mềm (framework / 프레임워크) và Spring Boot từ số 0, theo hướng hiểu bản chất trước khi dùng annotation** sang **Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

## Học Spring khung phần mềm (framework / 프레임워크) và Spring Boot từ số 0, theo hướng hiểu bản chất trước khi dùng annotation

> Lộ trình của bộ tài liệu này là **Beginner → Intermediate → cấp cao (senior / 시니어) → Master Supplement**.
> Part 1 được viết cho người đã biết Java cốt lõi (core / 핵심) ở mức cơ bản nhưng **chưa cần biết Spring, Servlet, HTTP backend, IoC, DI, JDBC, ORM hay giao dịch (transaction / 트랜잭션)**. Mục tiêu không phải học thuộc annotation, mà là hiểu vì sao Spring tồn tại, Spring đang làm công việc gì thay cho bạn, và mỗi dòng mã (code / 코드) của một ứng dụng Spring Boot liên hệ thế nào với Java thuần.

---


<!-- VERSION_UPDATE_2026-09-12_START -->

> **Chuyển mạch:** Từ **Học Spring khung phần mềm (framework / 프레임워크) và Spring Boot từ số 0, theo hướng hiểu bản chất trước khi dùng annotation**, ta sang **Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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
# 1. Spring giải quyết vấn đề gì?

Nếu mới học backend Java, bạn rất dễ nhìn Spring như một bộ sưu tập annotation. Bạn thấy `@RestController`, `@Service`, `@Repository`, `@Autowired`, `@Transactional` và tưởng rằng chỉ cần nhớ “annotation này dùng để làm gì” là đã học Spring. Cách học đó giúp tạo demo nhanh nhưng rất dễ gãy khi gặp dự án (project / 프로젝트) thật, bởi vì annotation chỉ là **siêu dữ liệu (metadata / 메타데이터)**. Annotation tự nó không tạo đối tượng (object / 객체), không mở giao dịch (transaction / 트랜잭션), không nhận HTTP yêu cầu (request / 요청) và cũng không truy cập cơ sở dữ liệu (database / 데이터베이스). Có một thời gian chạy (runtime / 런타임) của Spring đọc siêu dữ liệu (metadata / 메타데이터) đó rồi thực hiện công việc tương ứng.

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

Đoạn mã (code / 코드) này chạy được, nhưng `OrderService` đang vừa làm lô-gic nghiệp vụ (business logic / 비즈니스 로직) vừa tự quyết định phụ thuộc (dependency / 의존성) cụ thể. Nếu ngày mai bạn muốn dùng `MockPaymentGateway` cho kiểm thử (test / 테스트) hoặc đổi sang `BankTransferPaymentGateway`, bạn phải sửa `OrderService`. lớp (class / 클래스) này đang phụ thuộc trực tiếp vào cách phụ thuộc (dependency / 의존성) được khởi tạo.

Ta có thể cải thiện bằng constructor:

```java
public final class OrderService {
    private final PaymentGateway paymentGateway;

    public OrderService(PaymentGateway paymentGateway) {
        this.paymentGateway = paymentGateway;
    }
}
```

Ở đây `OrderService` chỉ nói rằng “tôi cần một `PaymentGateway`”. Nó không quyết định ai tạo gateway và gateway cụ thể là lớp (class / 클래스) nào. Một nơi khác sẽ assemble đối tượng (object / 객체) đồ thị (graph / 그래프):

```java
PaymentGateway gateway = new KoreanCardPaymentGateway();
OrderService orderService = new OrderService(gateway);
```

Đây chính là điểm xuất phát để hiểu **phụ thuộc (dependency / 의존성) Injection**. phụ thuộc (dependency / 의존성) được đưa từ bên ngoài vào đối tượng (object / 객체), thay vì đối tượng (object / 객체) tự tạo phụ thuộc (dependency / 의존성) bên trong.

Khi ứng dụng (application / 애플리케이션) lớn lên, việc tự tay viết hàng trăm dòng `new A(new B(new C(...)))` trở nên khó quản lý. Bạn còn phải giải quyết vòng đời (lifecycle / 생명주기), cấu hình (configuration / 구성), môi trường (environment / 환경), kiểm thử (test / 테스트) replacement, proxy, giao dịch (transaction / 트랜잭션), web hạ tầng (infrastructure / 인프라) và nhiều phụ thuộc (dependency / 의존성) có quan hệ với nhau. Spring cung cấp một **bộ chứa (container / 컨테이너)** làm công việc tạo và liên kết các đối tượng (object / 객체) đó.

Trong Java/Spring hiện đại, phụ thuộc (dependency / 의존성) bắt buộc nên được biểu diễn bằng constructor parameter. Điều này làm đối tượng (object / 객체) đồ thị (graph / 그래프) rõ ràng, trường dữ liệu (field / 필드) có thể `final`, và đối tượng (object / 객체) không tồn tại ở trạng thái “chưa được inject xong”.

Mẫu (pattern / 패턴) quan trọng ở đây là **Constructor Injection** và **tường minh (explicit / 명시적) Dependencies**. Một lớp (class / 클래스) có constructor gồm `OrderRepository`, `PaymentGateway` và `Clock` nói rất rõ nó cần gì để hoạt động.

Ở tầng thiết kế (design / 설계), Spring hỗ trợ **phụ thuộc (dependency / 의존성) Injection**, đồng thời giúp thực hiện **phụ thuộc (dependency / 의존성) Inversion Principle** khi nghiệp vụ (business / 비즈니스) mã (code / 코드) phụ thuộc vào lớp trừu tượng (abstraction / 추상화) thay vì vendor hiện thực (implementation / 구현).

Nếu constructor của một dịch vụ (service / 서비스) có mười hai phụ thuộc (dependency / 의존성), đừng chữa bằng trường dữ liệu (field / 필드) injection để constructor trông ngắn hơn. Đó thường là tín hiệu lớp (class / 클래스) đang có quá nhiều trách nhiệm hoặc use trường hợp (case / 사례) ranh giới (boundary / 경계) chưa rõ.

---

# 2. IoC là gì và tại sao phụ thuộc (dependency / 의존성) Injection chỉ là một phần của IoC?

**IoC — Inversion of điều khiển (control / 제어)** có nghĩa rộng hơn phụ thuộc (dependency / 의존성) Injection. Trong mã (code / 코드) Java thuần nhỏ, ứng dụng (application / 애플리케이션) mã (code / 코드) thường trực tiếp kiểm soát việc tạo đối tượng (object / 객체), gọi vòng đời (lifecycle / 생명주기) và wiring. Với Spring, quyền kiểm soát nhiều việc được đảo ngược sang khung phần mềm (framework / 프레임워크). Bạn khai báo các thành phần (component / 컴포넌트) và đặc tả hợp đồng (contract / 계약); khung phần mềm (framework / 프레임워크) quyết định lúc nào tạo bean, inject phụ thuộc (dependency / 의존성), gọi vòng đời (lifecycle / 생명주기) callback, tạo proxy hoặc đăng ký controller.

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

Phần wiring lớn được chuyển sang Spring bộ chứa (container / 컨테이너).

Điều quan trọng là Spring không “đoán lô-gic nghiệp vụ (business logic / 비즈니스 로직)”. Nó chỉ quản lý đối tượng (object / 객체) và hạ tầng (infrastructure / 인프라) dựa trên siêu dữ liệu (metadata / 메타데이터)/cấu hình (configuration / 구성) bạn cung cấp.

Một cách rất hiệu quả để gỡ lỗi (debug / 디버그) Spring là luôn dịch câu hỏi về Java thuần: “đối tượng (object / 객체) này do ai tạo?”, “tham chiếu (reference / 참조) này được truyền vào khi nào?”, “phương thức (method / 메서드) này có đang được gọi qua proxy không?”, “Ai mở tài nguyên (resource / 자원)?”, “Ai chịu trách nhiệm close?”. Khi trả lời được các câu đó, phần lớn “Spring magic” biến thành một luồng (flow / 흐름) Java bình thường.

---

<!-- SPRING_BATCH1_IOC_BEGINNER -->

> **Chuyển mạch:** Từ **Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21**, ta sang **Từ siêu dữ liệu (metadata / 메타데이터) tới bean instance: bộ chứa (container / 컨테이너) thực sự làm gì khi “inject phụ thuộc (dependency / 의존성)”?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Từ siêu dữ liệu (metadata / 메타데이터) tới bean instance: bộ chứa (container / 컨테이너) thực sự làm gì khi “inject phụ thuộc (dependency / 의존성)”?

Khi mới học, câu “Spring scan `@Service` rồi inject bean” đủ để bắt đầu, nhưng mô hình tư duy (mental model / 사고 모델) đó quá ngắn để gỡ lỗi (debug / 디버그) hệ thống thật. bộ chứa (container / 컨테이너) thực tế phải đi qua ba lớp khác nhau: **siêu dữ liệu (metadata / 메타데이터) cấu hình**, **BeanDefinition**, rồi mới tới **đối tượng (object / 객체) instance**. `@Component`, `@Service`, `@Repository`, `@Configuration` và `@Bean` cung cấp siêu dữ liệu (metadata / 메타데이터). Spring đọc siêu dữ liệu (metadata / 메타데이터) đó để đăng ký BeanDefinition, tức bản mô tả cách tạo đối tượng (object / 객체): lớp (class / 클래스) nào, phạm vi (scope / 범위) nào, factory phương thức (method / 메서드) nào, phụ thuộc (dependency / 의존성) nào, có lazy hay không, có qualifier gì và callback vòng đời (lifecycle / 생명주기) nào. Chỉ sau khi ngữ cảnh (context / 맥락) bước vào giai đoạn tạo bean, BeanDefinition mới được dùng để instantiate đối tượng (object / 객체).

Vì vậy một bean có thể “được Spring biết tới” nhưng đối tượng (object / 객체) thật chưa hề tồn tại. Lazy bean là ví dụ rõ nhất. Request-scoped bean còn cho thấy một BeanDefinition có thể đại diện nhiều instance theo từng yêu cầu (request / 요청) thay vì một singleton duy nhất. Khi bạn hiểu definition và instance là hai khái niệm khác nhau, nhiều lỗi startup bắt đầu dễ đọc hơn.

Khi tạo một singleton dịch vụ (service / 서비스), bộ chứa (container / 컨테이너) conceptually làm việc như sau:

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

Điểm cuối rất quan trọng: tham chiếu (reference / 참조) mà controller nhận đôi khi không phải đối tượng (object / 객체) do constructor vừa tạo mà là **proxy** bao quanh đối tượng (object / 객체) đó. giao dịch (transaction / 트랜잭션), phương thức (method / 메서드) bảo mật (security / 보안), bộ nhớ đệm (cache / 캐시), async và AOP dựa trên khả năng này. Spring không thay đổi quy tắc Java; nó thay đối tượng (object / 객체) mà caller đang giữ tham chiếu (reference / 참조) tới.

Phụ thuộc (dependency / 의존성) Injection vì vậy nên được hiểu là **xây đối tượng (object / 객체) đồ thị (graph / 그래프) có kiểm soát**, không phải “tìm bean toàn cục”. Nếu nghiệp vụ (business / 비즈니스) lớp (class / 클래스) tự giữ `ApplicationContext` rồi gọi `getBean()` ở mọi nơi, phụ thuộc (dependency / 의존성) lại trở thành hidden toàn cục (global / 전역) lookup và bạn đã biến DI thành dịch vụ (service / 서비스) Locator. Constructor injection giữ đồ thị (graph / 그래프) hiển thị trong kiểu (type / 타입) signature, làm kiểm thử (test / 테스트) dễ hơn và giúp bộ chứa (container / 컨테이너) thất bại (fail / 실패) sớm nếu đồ thị (graph / 그래프) không thể xây.
<!-- SPRING_BATCH1_IOC_BEGINNER_END -->

---

# 3. Spring khung phần mềm (framework / 프레임워크) và Spring Boot khác nhau như thế nào?

Spring khung phần mềm (framework / 프레임워크) là nền tảng. Nó cung cấp IoC bộ chứa (container / 컨테이너), DI, Spring MVC, giao dịch (transaction / 트랜잭션) lớp trừu tượng (abstraction / 추상화), data-access lớp trừu tượng (abstraction / 추상화), AOP, sự kiện (event / 이벤트) hệ thống (system / 시스템), tài nguyên (resource / 자원) lớp trừu tượng (abstraction / 추상화) và testing hỗ trợ (support / 지원). Spring Boot sử dụng Spring khung phần mềm (framework / 프레임워크) và thêm một lớp convention để giúp ứng dụng (application / 애플리케이션) bắt đầu nhanh hơn.

Nếu dùng Spring khung phần mềm (framework / 프레임워크) thuần, bạn phải chủ động cấu hình nhiều thành phần. Với web ứng dụng (application / 애플리케이션), bạn phải quan tâm servlet bộ chứa (container / 컨테이너), `DispatcherServlet`, message converters, JSON mapper, dữ liệu (data / 데이터) nguồn (source / 소스), giao dịch (transaction / 트랜잭션) manager và rất nhiều wiring khác. Spring Boot nhìn vào classpath, cấu hình (configuration / 구성) và các bean hiện có để tạo ra những default hợp lý.

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

Spring Boot không thay thế Spring khung phần mềm (framework / 프레임워크). Boot là một cách **bootstrap, configure và vận hành Spring ứng dụng (application / 애플리케이션)** dễ hơn.

---

# 4. phiên bản (version / 버전) Spring cần học vào năm 2026

Khi học Spring, phiên bản (version / 버전) quan trọng hơn nhiều người nghĩ vì cùng một bài tutorial có thể dùng gói (package / 패키지) hoặc API đã lỗi thời. Có ba generation bạn cần nhận biết.

Spring Boot 2.7 đi cùng Spring khung phần mềm (framework / 프레임워크) 5.3 là generation legacy nhưng vẫn tồn tại trong enterprise. Nó chạy được từ Java 8 và còn thuộc thế giới `javax.*`.

Spring Boot 3.x đi với Spring khung phần mềm (framework / 프레임워크) 6.x, yêu cầu Java 17 trở lên và chuyển sang không gian tên (namespace / 네임스페이스) `jakarta.*`. Đây là bước di chuyển (migration / 마이그레이션) rất lớn.

Spring Boot 4.x đi với Spring khung phần mềm (framework / 프레임워크) 7.x. Ở thời điểm tài liệu này, Spring Boot stable hiện tại là **4.1.1** và yêu cầu Java 17 trở lên, Spring khung phần mềm (framework / 프레임워크) 7.0.9 trở lên; Boot 4 dựa trên Jakarta EE 11 và Servlet 6.1. Boot 4 cũng ưu tiên Jackson 3. Với dự án (project / 프로젝트) mới, đây là generation nên hiểu, nhưng bạn vẫn phải biết Boot 3 vì mã (code / 코드) enterprise hiện nay vẫn rất nhiều.

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

Sự đổi tên này không chỉ là style. thư viện (library / 라이브러리) cũ phụ thuộc `javax.*` có thể không tương thích với ứng dụng (application / 애플리케이션) Jakarta mới.

Khi đọc ngăn xếp (stack / 스택) Overflow hoặc blog, trước tiên hãy nhìn năm bài viết, Java phiên bản (version / 버전) và Spring Boot phiên bản (version / 버전). Một lời khuyên đúng cho Boot 2.1 có thể sai hoặc không còn cần thiết ở Boot 4.

---

<!-- SPRING_BATCH5_VERSION_BEGINNER -->

> **Chuyển mạch:** Từ **Từ siêu dữ liệu (metadata / 메타데이터) tới bean instance: bộ chứa (container / 컨테이너) thực sự làm gì khi “inject phụ thuộc (dependency / 의존성)”?**, ta sang **Học phiên bản (version / 버전) theo “cách viết ứng dụng (application / 애플리케이션) thay đổi”, không theo release-note danh sách (list / 목록)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Học phiên bản (version / 버전) theo “cách viết ứng dụng (application / 애플리케이션) thay đổi”, không theo release-note danh sách (list / 목록)

Boot 2.7 / khung phần mềm (framework / 프레임워크) 5.3 đại diện thế hệ Java 8-era, `javax.*` và nhiều bảo mật (security / 보안)/cấu hình (config / 설정) examples cũ. Khi nhìn `javax.servlet`, `javax.persistence`, `WebSecurityConfigurerAdapter`, `RestTemplate`-centric tutorials hoặc XML nhiều, đừng vội kết luận mã (code / 코드) sai; hãy xác định generation trước rồi map sang cách hiện đại.

Boot 3 / khung phần mềm (framework / 프레임워크) 6 là bước chuyển nền tảng (platform / 플랫폼) lớn hơn một bản nâng phiên bản (version / 버전): Java 17 trở thành baseline, Java EE không gian tên (namespace / 네임스페이스) đổi sang `jakarta.*`, Spring bảo mật (security / 보안) 6 chuyển mạnh sang bean/lambda cấu hình (configuration / 구성), khả năng quan sát (observability / 관측 가능성)/AOT trở thành first-class hơn. di chuyển (migration / 마이그레이션) thường thất bại ở third-party thư viện (library / 라이브러리) chưa hỗ trợ Jakarta chứ không chỉ ở nguồn (source / 소스) import.

Boot 4 / khung phần mềm (framework / 프레임워크) 7 tiếp tục nền tảng (platform / 플랫폼) hóa: Jakarta EE 11 / Servlet 6.1, Jackson 3 là hướng mặc định, Boot modularize starters/kiểm thử (test / 테스트) hỗ trợ (support / 지원) mạnh hơn, khung phần mềm (framework / 프레임워크) dùng JSpecify nullness và có API-versioning hỗ trợ (support / 지원) ở web ngăn xếp (stack / 스택). Vì vậy mã (code / 코드) mới nên học theo Boot 4.1, nhưng người làm enterprise vẫn cần đọc được 2.7/3.x và biết di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) thay vì rewrite toàn bộ.
<!-- SPRING_BATCH5_VERSION_BEGINNER_END -->

---

# 5. Tạo một Spring Boot dự án (project / 프로젝트) và hiểu những tệp (file / 파일) đang xuất hiện

Cách phổ biến nhất để tạo dự án (project / 프로젝트) là Spring Initializr tại `start.spring.io`. Bạn chọn bản dựng (build / 빌드) công cụ (tool / 도구), Java phiên bản (version / 버전), Boot phiên bản (version / 버전) và dependencies. Với backend cơ bản, Maven + Java 21 hoặc 25 + Spring Web + kiểm tra hợp lệ (validation / 검증) là lựa chọn dễ học.

Một dự án (project / 프로젝트) Maven có thể có cấu trúc:

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

`pom.xml` mô tả dependencies và bản dựng (build / 빌드). `src/main/java` chứa mã nguồn (source code / 소스 코드). `src/main/resources` chứa cấu hình (configuration / 구성) và tài nguyên (resource / 자원). `src/test/java` chứa kiểm thử (test / 테스트). `mvnw` là Maven Wrapper để dự án (project / 프로젝트) có thể dùng phiên bản (version / 버전) Maven phù hợp mà nhà phát triển (developer / 개발자) không cần tự quản lý Maven toàn cục (global / 전역) quá chặt.

Main lớp (class / 클래스):

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

Main lớp (class / 클래스) nên nằm gần gốc (root / 루트) gói (package / 패키지) `com.example.demo` để thành phần (component / 컴포넌트) scan mặc định nhìn thấy các subpackage như `com.example.demo.user`, `com.example.demo.order`.

---

# 6. Starter phụ thuộc (dependency / 의존성) là gì?

Spring Boot dùng “starter” để gom phụ thuộc (dependency / 의존성) theo use trường hợp (case / 사례). Nếu bạn muốn làm web ứng dụng (application / 애플리케이션), thay vì tự thêm Spring MVC, Jackson, servlet bộ chứa (container / 컨테이너), logging tích hợp (integration / 통합) và các transitive phụ thuộc (dependency / 의존성) tương thích, bạn thêm starter phù hợp.

Ví dụ:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webmvc</artifactId>
</dependency>
```

Kiểm tra hợp lệ (validation / 검증):

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

Starter không phải “một khung phần mềm (framework / 프레임워크) khác”. Nó chủ yếu là phụ thuộc (dependency / 의존성) bundle + sự phối hợp với Boot auto-configuration.

Một lợi ích lớn của Boot là **phụ thuộc (dependency / 의존성) management**. Boot phát hành một tập hợp phiên bản (version / 버전) đã được kiểm thử cùng nhau. Vì vậy nếu phụ thuộc (dependency / 의존성) đã được Boot quản lý, bạn thường không tự ghi phiên bản (version / 버전). Tự ép Jackson, Hibernate hoặc Spring khung phần mềm (framework / 프레임워크) sang một phiên bản (version / 버전) khác chỉ vì “mới hơn” có thể gây lỗi linkage/thời gian chạy (runtime / 런타임).

Hãy để nền tảng (platform / 플랫폼)/BOM quản lý phụ thuộc (dependency / 의존성) versions và chỉ override khi có lý do cụ thể, ví dụ bảo mật (security / 보안) patch hoặc thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성) đã được xác minh.

---

# 7. `@SpringBootApplication` thực sự có ý nghĩa gì?

`@SpringBootApplication` là annotation tổng hợp mang ba ý tưởng lớn: đây là một cấu hình (configuration / 구성) lớp (class / 클래스), ứng dụng (application / 애플리케이션) muốn dùng auto-configuration, và thành phần (component / 컴포넌트) scanning sẽ bắt đầu từ gói (package / 패키지) hiện tại.

Bạn không nên học thuộc “nó bằng ba annotation” rồi dừng lại. Điều cần hiểu là annotation này nói với Boot: “hãy xây ApplicationContext cho ứng dụng (application / 애플리케이션) này, tìm các thành phần (component / 컴포넌트) của tôi, rồi dựa vào classpath/cấu hình (configuration / 구성) để tạo những hạ tầng (infrastructure / 인프라) bean cần thiết”.

Khi `SpringApplication.run(...)` chạy, một luồng (flow / 흐름) đơn giản có thể hình dung là: Boot chuẩn bị `Environment`, xác định loại ứng dụng (application / 애플리케이션), tạo `ApplicationContext`, tải (load / 로드) bean definitions, chạy các processor, tạo singleton beans, cấu hình web máy chủ (server / 서버) nếu đây là web ứng dụng (application / 애플리케이션), rồi chuyển ứng dụng (application / 애플리케이션) sang trạng thái ready.

Các chi tiết sâu của luồng (flow / 흐름) này sẽ nằm ở Intermediate và cấp cao (senior / 시니어).

---

# 8. Bean là gì?

Bean là **đối tượng (object / 객체) do Spring bộ chứa (container / 컨테이너) quản lý**. Một đối tượng (object / 객체) Java bình thường:

```java
User user = new User();
```

không tự nhiên trở thành Spring bean. Khi Spring biết cách tạo và quản lý `UserService`, instance `UserService` trong bộ chứa (container / 컨테이너) là bean.

Ví dụ:

```java
@Service
public class UserService {
}
```

Spring thành phần (component / 컴포넌트) scan phát hiện lớp (class / 클래스) và đăng ký siêu dữ liệu (metadata / 메타데이터) để sau đó tạo bean.

Bean có thể được tạo từ thành phần (component / 컴포넌트) scanning hoặc từ `@Bean` phương thức (method / 메서드):

```java
@Configuration
public class TimeConfiguration {
    @Bean
    Clock clock() {
        return Clock.systemUTC();
    }
}
```

`Clock` là lớp (class / 클래스) của JDK nên bạn không thể thêm `@Component` vào nguồn (source / 소스) của nó. `@Bean` cho phép bạn nói rõ Spring phải tạo đối tượng (object / 객체) bằng factory phương thức (method / 메서드) nào.

Ứng dụng (application / 애플리케이션) components mà bạn sở hữu nguồn (source / 소스) thường dùng stereotype annotation. hạ tầng (infrastructure / 인프라) đối tượng (object / 객체) hoặc third-party đối tượng (object / 객체) thường được tạo rõ ràng trong `@Configuration`.

---

# 9. `ApplicationContext` là gì?

`ApplicationContext` là bộ chứa (container / 컨테이너) cấp cao của Spring. Nó quản lý bean definitions và bean instances, phụ thuộc (dependency / 의존성) resolution, vòng đời (lifecycle / 생명주기), events, `Environment`, resources, messages và nhiều extension điểm (point / 지점).

Bạn có thể lấy bean thủ công:

```java
ApplicationContext context =
        SpringApplication.run(Application.class, args);

UserService service =
        context.getBean(UserService.class);
```

Nhưng nghiệp vụ (business / 비즈니스) mã (code / 코드) bình thường không nên tự cầm `ApplicationContext` rồi `getBean()` ở khắp nơi. Làm vậy biến Spring thành dịch vụ (service / 서비스) Locator và che giấu dependencies.

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

Spring bộ chứa (container / 컨테이너) chịu trách nhiệm tìm bean phù hợp và inject vào constructor.

---

# 10. `@Component`, `@Service`, `@Repository`, `@Controller`, `@RestController`

`@Component` là stereotype tổng quát. `@Service`, `@Repository` và `@Controller` truyền tải intent cụ thể hơn và cũng tham gia thành phần (component / 컴포넌트) scanning.

`@Service` nên dùng cho ứng dụng (application / 애플리케이션)/nghiệp vụ (business / 비즈니스) dịch vụ (service / 서비스):

```java
@Service
public class UserService {
}
```

`@Repository` biểu thị data-access thành phần (component / 컴포넌트):

```java
@Repository
public class JdbcUserRepository {
}
```

`@Controller` thuộc web MVC truyền thống có thể trả view. `@RestController` thường dùng cho REST API và phản hồi (response / 응답) body được viết trực tiếp ra HTTP phản hồi (response / 응답) thông qua message conversion.

```java
@RestController
@RequestMapping("/users")
public class UserController {
}
```

Dùng stereotype thể hiện role thật. `@Component` không sai, nhưng `@Repository` nói nhiều hơn về kiến trúc so với một annotation generic.

Annotation không tạo “tầng (layer / 계층)” một cách thần kỳ. Nếu `@Service` chứa SQL, HTTP parsing, tệp (file / 파일) handling và bảo mật (security / 보안) lô-gic (logic / 논리) hỗn hợp, nó vẫn là God dịch vụ (service / 서비스) dù có annotation đúng tên.

---

# 11. thành phần (component / 컴포넌트) Scan và lỗi “Spring không tìm thấy Bean”

Main lớp (class / 클래스):

```text
com.example.demo.DemoApplication
```

mặc định scan các gói (package / 패키지) phía dưới:

```text
com.example.demo.user
com.example.demo.order
com.example.demo.payment
```

Nếu `PaymentService` nằm ở:

```text
com.company.payment
```

nằm ngoài gốc (root / 루트) scan, Spring có thể không tìm thấy.

Bạn có thể cấu hình scan:

```java
@ComponentScan({
    "com.example.demo",
    "com.company.payment"
})
```

nhưng không nên xử lý mọi lỗi bằng cách scan quá rộng như `"com"`. Điều đó làm bộ chứa (container / 컨테이너) nhìn thấy thành phần (component / 컴포넌트) không chủ đích và làm đối tượng (object / 객체) đồ thị (graph / 그래프) khó hiểu hơn.

Gói (package / 패키지) cấu trúc (structure / 구조) là một architectural ranh giới (boundary / 경계). Main ứng dụng (application / 애플리케이션) lớp (class / 클래스) ở gốc (root / 루트) gói (package / 패키지) và package-by-feature thường giúp scanning tự nhiên.

---

# 12. Constructor Injection chi tiết

Giả sử:

```java
public interface UserRepository {
    Optional<User> findById(long id);
}
```

Hiện thực (implementation / 구현):

```java
@Repository
public class InMemoryUserRepository implements UserRepository {
}
```

Dịch vụ (service / 서비스):

```java
@Service
public class UserService {
    private final UserRepository repository;

    public UserService(UserRepository repository) {
        this.repository = repository;
    }
}
```

Khi bộ chứa (container / 컨테이너) tạo `UserService`, nó thấy constructor cần `UserRepository`, tìm bean compatible, thấy `InMemoryUserRepository`, tạo/resolve bean đó rồi truyền tham chiếu (reference / 참조) vào constructor.

Nếu lớp (class / 클래스) chỉ có một constructor, Spring hiện đại không cần `@Autowired` trên constructor.

Điều này tạo đối tượng (object / 객체) giống Java thuần:

```java
UserRepository repository = new InMemoryUserRepository();
UserService service = new UserService(repository);
```

khác ở chỗ Spring làm wiring.

Required phụ thuộc (dependency / 의존성) → constructor. Optional phụ thuộc (dependency / 의존성) chỉ nên optional nếu nghiệp vụ (business / 비즈니스)/vòng đời (lifecycle / 생명주기) thực sự cho phép thiếu.

---

# 13. trường dữ liệu (field / 필드) Injection và vì sao không nên chọn làm default

Trường dữ liệu (field / 필드) injection:

```java
@Service
public class UserService {
    @Autowired
    private UserRepository repository;
}
```

rất ngắn, nhưng phụ thuộc (dependency / 의존성) bị ẩn. Bạn có thể viết:

```java
new UserService();
```

và đối tượng (object / 객체) tồn tại trong trạng thái chưa hợp lệ. trường dữ liệu (field / 필드) không thể `final` theo cách bình thường. đơn vị (unit / 단위) kiểm thử (test / 테스트) muốn tạo dịch vụ (service / 서비스) phải dùng reflection/khung phần mềm (framework / 프레임워크) hoặc chạy Spring.

Constructor injection cho phép:

```java
UserService service =
        new UserService(fakeRepository);
```

không cần Spring.

Trường dữ liệu (field / 필드) injection vẫn xuất hiện rất nhiều trong mã (code / 코드) legacy, nên bạn phải đọc được. Nhưng khi viết mới, constructor injection là default tốt hơn.

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

có thể phù hợp nếu phụ thuộc (dependency / 의존성) thật sự thay đổi được hoặc optional theo vòng đời (lifecycle / 생명주기). Tuy nhiên phần lớn ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스) có required phụ thuộc (dependency / 의존성) nên constructor dễ reason hơn.

Đừng chọn setter chỉ vì “Spring hỗ trợ ba loại injection”. API tồn tại không có nghĩa mọi kiểu đều tốt như nhau.

---

# 15. Nhiều Bean cùng giao diện (interface / 인터페이스): `@Primary` và `@Qualifier`

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

Bộ chứa (container / 컨테이너) có hai candidates và không biết chọn cái nào.

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

Nếu ứng dụng (application / 애플리케이션) phải chọn gateway động dựa trên `PaymentType`, rải `@Qualifier` vào nghiệp vụ (business / 비즈니스) methods không phải thiết kế tốt. Ở Intermediate ta sẽ học inject `List`/`Map` chiến lược (strategy / 전략) và tạo registry.

---

# 16. Bean phạm vi (scope / 범위) và ý nghĩa của Singleton

Default Spring bean phạm vi (scope / 범위) là singleton, nghĩa là **một bean instance trên một ApplicationContext**, không phải một đối tượng (object / 객체) duy nhất cho toàn JVM theo GoF Singleton.

```java
@Service
public class UserService {
}
```

nhiều HTTP yêu cầu (request / 요청) sẽ dùng cùng `UserService` instance.

Vì vậy đây là mã (code / 코드) nguy hiểm:

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

Dịch vụ (service / 서비스) singleton nên thường stateless:

```java
public User load(Long id) {
    return repository.findById(id)
            .orElseThrow();
}
```

Trạng thái (state / 상태) của yêu cầu (request / 요청) nằm trong cục bộ (local / 로컬) variables hoặc request-scoped/ngữ cảnh (context / 맥락) đối tượng (object / 객체) có chủ đích.

Spring còn có prototype, yêu cầu (request / 요청), session và các web scopes khác. Beginner chỉ cần nhớ rằng “phạm vi (scope / 범위) quyết định vòng đời (lifecycle / 생명주기) và phạm vi chia sẻ đối tượng (object / 객체)”. Không dùng prototype để thay cho `new` của mọi lĩnh vực (domain / 도메인) đối tượng (object / 객체).

---

# 17. Bean vòng đời (lifecycle / 생명주기): đối tượng (object / 객체) được tạo và huỷ lúc nào?

Một bean singleton đơn giản trải qua luồng (flow / 흐름) gần như:

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

với gói (package / 패키지) Jakarta:

```java
jakarta.annotation.PostConstruct
jakarta.annotation.PreDestroy
```

`@PostConstruct` không nên biến thành nơi chạy mạng (network / 네트워크) lời gọi (call / 호출) vô hạn hoặc di chuyển (migration / 마이그레이션) lớn. Nếu startup phụ thuộc (dependency / 의존성) không bounded, triển khai (deployment / 배포) có thể treo.

`@PreDestroy` phù hợp để close tài nguyên (resource / 자원) do bean sở hữu.

**mẫu lập trình (programming pattern / 프로그래밍 패턴) — tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권).** thành phần (component / 컴포넌트) tạo tài nguyên (resource / 자원) thì thành phần (component / 컴포넌트) đó nên có trách nhiệm quản lý vòng đời (lifecycle / 생명주기) của tài nguyên (resource / 자원). Nếu bean tạo máy khách (client / 클라이언트)/executor, cần biết khi ngữ cảnh (context / 맥락) đóng tài nguyên (resource / 자원) được đóng bằng cách nào.

---

# 18. `@Configuration` và `@Bean` như Java-based cấu hình (configuration / 구성)

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

`@Configuration` nói rằng lớp (class / 클래스) này chứa bean definitions/cấu hình (configuration / 구성). `@Bean` nói rằng return giá trị (value / 값) của phương thức (method / 메서드) sẽ được bộ chứa (container / 컨테이너) quản lý.

Điều hay của phương thức (method / 메서드) parameter là phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적):

```java
@Bean
OrderService orderService(
        OrderRepository repository,
        Clock clock) {
    return new OrderService(repository, clock);
}
```

Đọc phương thức (method / 메서드) là thấy ngay dependencies.

`@Bean` giống Factory phương thức (method / 메서드) ở mức khái niệm; bộ chứa (container / 컨테이너) trở thành đối tượng (object / 객체) factory lớn quản lý vòng đời (lifecycle / 생명주기) và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프).

---

# 19. Spring Boot Auto-Configuration: “magic” đầu tiên cần hiểu

Bạn thêm `spring-boot-starter-web` rồi ứng dụng (application / 애플리케이션) tự có web máy chủ (server / 서버), JSON, MVC. Đây là auto-configuration.

Boot xem các điều kiện như lớp (class / 클래스) nào đang có trên classpath, ứng dụng (application / 애플리케이션) có phải servlet web ứng dụng (application / 애플리케이션) không, thuộc tính (property / 속성) nào bật/tắt, và bạn đã tự tạo bean nào chưa. Nếu điều kiện phù hợp, Boot đăng ký default hạ tầng (infrastructure / 인프라) bean.

Mô hình tư duy (mental model / 사고 모델) quan trọng nhất là **default + back-off**. Boot cố gắng cho bạn default hợp lý, nhưng khi bạn cung cấp bean/cấu hình (config / 설정) riêng, auto-configuration thường lùi lại.

Ví dụ concept:

```java
@Bean
@ConditionalOnMissingBean
SomeClient someClient() {
    return defaultClient();
}
```

Nếu ứng dụng (application / 애플리케이션) đã có `SomeClient`, default không được tạo.

**cấp cao (senior / 시니어) Idiom.** Spring Boot không phải “convention over cấu hình (configuration / 구성)” theo nghĩa không cấu hình được. Nó là “sensible defaults, tường minh (explicit / 명시적) override”.

---

# 20. cấu hình (configuration / 구성) bên ngoài ứng dụng (application / 애플리케이션)

Hard-code:

```java
String apiUrl = "https://prod.example.com";
```

là vấn đề vì cục bộ (local / 로컬), kiểm thử (test / 테스트) và môi trường vận hành (production / 운영 환경) cần giá trị khác nhau. Spring Boot có externalized cấu hình (configuration / 구성).

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

Bạn có thể override bằng môi trường (environment / 환경) variable hoặc command-line thuộc tính (property / 속성) tùy triển khai (deployment / 배포).

Cấu hình (configuration / 구성) không phải nghiệp vụ (business / 비즈니스) mã (code / 코드). Nó là đầu vào (input / 입력) của ứng dụng (application / 애플리케이션).

---

# 21. `@Value` và khi nào nên dùng

Simple giá trị (value / 값):

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

`:2s` là default trong placeholder cú pháp (syntax / 문법).

`@Value` tiện cho một vài giá trị nhỏ, nhưng khi có nhiều thuộc tính (property / 속성) cùng nhóm, typed cấu hình (configuration / 구성) tốt hơn.

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

Spring bind văn bản (text / 텍스트) cấu hình (configuration / 구성) vào kiểu (type / 타입) thật. `timeout` trở thành `Duration`, URL trở thành `URI`. Điều này tốt hơn `String` vì invalid format có thể thất bại (fail / 실패) sớm.

Bạn có thể đăng ký qua `@ConfigurationPropertiesScan` hoặc `@EnableConfigurationProperties`.

**mẫu lập trình (programming pattern / 프로그래밍 패턴) — Typed cấu hình (configuration / 구성).** Parse và validate bên ngoài (external / 외부) cấu hình (configuration / 구성) một lần ở ranh giới (boundary / 경계), sau đó cốt lõi (core / 핵심) ứng dụng (application / 애플리케이션) sử dụng kiểu (type / 타입) có nghĩa.

`int timeout = 3` rất tệ nếu không biết đơn vị là giây hay millisecond. `Duration` làm đơn vị (unit / 단위) tường minh (explicit / 명시적).

---

# 23. Profiles dùng để làm gì?

Profiles giúp chọn cấu hình (configuration / 구성)/bean theo môi trường (environment / 환경) hoặc triển khai (deployment / 배포) ngữ cảnh (context / 맥락). Ví dụ `application-local.yml` có cục bộ (local / 로컬) DB, còn môi trường vận hành (production / 운영 환경) lấy secrets từ thời gian chạy (runtime / 런타임) môi trường (environment / 환경).

Bean-specific profile:

```java
@Bean
@Profile("local")
PaymentGateway fakePaymentGateway() {
    return new FakePaymentGateway();
}
```

Profiles không nên trở thành nghiệp vụ (business / 비즈니스) tính năng (feature / 기능) engine. Nếu bạn có `@Profile("customerA")`, `@Profile("customerB")`, `@Profile("customerC")` rải khắp ứng dụng (application / 애플리케이션), có thể nghiệp vụ (business / 비즈니스) variation đang bị biến thành triển khai (deployment / 배포) variation.

---

# 24. HTTP là gì trước khi học Spring MVC?

Backend REST là chương trình nhận HTTP yêu cầu (request / 요청) và trả HTTP phản hồi (response / 응답). yêu cầu (request / 요청) gồm phương thức (method / 메서드), URL/đường dẫn (path / 경로), headers và có thể có body. phản hồi (response / 응답) gồm status mã (code / 코드), headers và body.

Ví dụ:

```http
GET /users/42
Accept: application/json
```

Phản hồi (response / 응답):

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":42,"name":"Kim"}
```

Các HTTP methods thường gặp là GET để đọc, POST để tạo/trigger thao tác (operation / 연산), PUT để thay thế/cập nhật tài nguyên (resource / 자원) theo đặc tả hợp đồng (contract / 계약), PATCH cho partial thay đổi (change / 변경) và DELETE để xoá. Đây là HTTP ngữ nghĩa (semantics / 의미론) chứ không phải Spring invention.

Status mã (code / 코드) cũng là HTTP. `200` là thành công phổ biến, `201` thường dùng khi tạo tài nguyên (resource / 자원), `204` là thành công không có body, `400` là yêu cầu (request / 요청) invalid, `401` liên quan authentication, `403` liên quan authorization, `404` không tìm thấy, `409` xung đột (conflict / 충돌) và `500` là máy chủ (server / 서버) lỗi (error / 오류).

Spring MVC chỉ giúp map HTTP world vào Java methods.

---

# 25. Servlet và DispatcherServlet ở mức Beginner

Trong Servlet-based Spring MVC, embedded máy chủ (server / 서버) như Tomcat nhận TCP/HTTP yêu cầu (request / 요청) rồi đưa yêu cầu (request / 요청) vào Servlet ngăn xếp (stack / 스택). Spring MVC có `DispatcherServlet` đóng vai trò **Front Controller**. Nó nhận yêu cầu (request / 요청) đã vào Spring MVC, tìm controller phương thức (method / 메서드) phù hợp, resolve arguments, gọi phương thức (method / 메서드), xử lý return giá trị (value / 값) và viết phản hồi (response / 응답).

Mô hình tư duy (mental model / 사고 모델):

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

Ở Beginner bạn chưa cần biết `HandlerMapping` hay `HandlerAdapter`; Intermediate sẽ mở luồng (flow / 흐름) đó.

**mẫu thiết kế (design pattern / 디자인 패턴) — Front Controller.** Thay vì mỗi endpoint tự làm toàn bộ hạ tầng (infrastructure / 인프라), một entry điểm (point / 지점) trung tâm dispatch yêu cầu (request / 요청) đến handler phù hợp.

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

`@RequestMapping("/users")` tạo cơ sở (base / 기반) đường dẫn (path / 경로). `@GetMapping("/{id}")` match GET yêu cầu (request / 요청) như `/users/10`. `@PathVariable` lấy phần `{id}` rồi conversion thành `long`.

Phản hồi (response / 응답) bản ghi (record / 레코드):

```java
public record UserResponse(
        long id,
        String name) {
}
```

Spring MVC dùng message converter, thông thường với Jackson JSON tích hợp (integration / 통합), để biến đối tượng (object / 객체) thành JSON.

---

# 27. `@RequestParam`

Yêu cầu (request / 요청):

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

`@RequestParam` dùng truy vấn (query / 쿼리) parameter. `@PathVariable` thường dùng định danh (identity / 식별자)/đường dẫn (path / 경로) segment. Đừng cố nhét mọi thứ vào đường dẫn (path / 경로).

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

Headers thường chứa siêu dữ liệu (metadata / 메타데이터) như authorization, content negotiation, tracing/correlation, conditional yêu cầu (request / 요청) và caching directives.

Không nên dùng custom header để nhét toàn bộ nghiệp vụ (business / 비즈니스) payload.

---

# 29. `@RequestBody` và JSON → Java

Yêu cầu (request / 요청):

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

Spring chọn JSON message converter và Jackson đọc body thành Java đối tượng (object / 객체).

Điều quan trọng là `@RequestBody` không phải “API đọc JSON” độc lập. Nó là chỉ dẫn cho MVC argument-resolution/message-conversion hạ tầng (infrastructure / 인프라).

---

# 30. DTO là gì và tại sao không nên dùng thực thể (entity / 엔터티) làm yêu cầu (request / 요청)/phản hồi (response / 응답)?

DTO là đối tượng (object / 객체) dùng để vận chuyển dữ liệu qua ranh giới (boundary / 경계). HTTP yêu cầu (request / 요청) DTO đại diện đặc tả hợp đồng (contract / 계약) máy khách (client / 클라이언트) được phép gửi. HTTP phản hồi (response / 응답) DTO đại diện đặc tả hợp đồng (contract / 계약) máy chủ (server / 서버) công khai.

Nếu bạn dùng JPA thực thể (entity / 엔터티) trực tiếp:

```java
@PostMapping
public UserEntity create(
        @RequestBody UserEntity entity) {
    ...
}
```

Máy khách (client / 클라이언트) có thể gửi trường dữ liệu (field / 필드) không nên được phép thay đổi, thực thể (entity / 엔터티) vòng đời (lifecycle / 생명주기) bị leak ra web tầng (layer / 계층), lazy relationships có thể trigger SQL trong serialization và cơ sở dữ liệu (database / 데이터베이스) refactor có thể vô tình phá API công khai (public API / 공개 API).

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

**mẫu lập trình (programming pattern / 프로그래밍 패턴) — ranh giới (boundary / 경계) DTO.** vận chuyển (transport / 전송) đặc tả hợp đồng (contract / 계약) được tách khỏi persistence/lĩnh vực (domain / 도메인) biểu diễn (representation / 표현).

Tách ranh giới (boundary / 경계) không có nghĩa phải tạo DTO cho từng private phương thức (method / 메서드). ánh xạ (mapping / 매핑) ceremony chỉ có giá trị ở ranh giới (boundary / 경계) có ý nghĩa.

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

Nếu cần điều khiển (control / 제어) status/header:

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

Không cần bọc mọi phản hồi (response / 응답) trong `ResponseEntity` nếu bạn không cần điều khiển (control / 제어) thêm.

---

# 32. kiểm tra hợp lệ (validation / 검증) là gì?

JSON syntactically hợp lệ chưa chắc đầu vào (input / 입력) hợp lệ. Ví dụ:

```json
{
  "name": "",
  "email": "abc"
}
```

có JSON đúng nhưng dữ liệu sai.

Bean kiểm tra hợp lệ (validation / 검증) cho phép mô tả các ràng buộc (constraints / 제약조건들):

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

`@Valid` yêu cầu kiểm tra hợp lệ (validation / 검증) cascade vào yêu cầu (request / 요청) đối tượng (object / 객체).

---

# 33. `@NotNull`, `@NotEmpty`, `@NotBlank`

`@NotNull` chỉ nói giá trị (value / 값) không được `null`. Chuỗi `""` vẫn pass.

`@NotEmpty` nói collection/string không null và không rỗng, nhưng string `"   "` vẫn có độ dài và có thể pass.

`@NotBlank` dành cho văn bản (text / 텍스트); nó reject null, empty và chỉ-whitespace. Vì vậy required người dùng (user / 사용자) name thường hợp với `@NotBlank`.

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

# 34. kiểm tra hợp lệ (validation / 검증) không thay nghiệp vụ (business / 비즈니스) rules

`@Email` có thể kiểm tra email format. Nó không biết email đã được đăng ký hay chưa.

`@Positive` có thể kiểm tra amount > 0. Nó không biết account có đủ balance.

Nên phân biệt:

```text
Boundary validation
→ shape / format / required / range

Business invariant
→ rule của domain/use case
```

Ví dụ duplicate email nên được kiểm tra ở ứng dụng (application / 애플리케이션)/lĩnh vực (domain / 도메인)/persistence quy tắc (rule / 규칙), không cố viết một validator annotation gọi DB cho mọi trường hợp (case / 사례).

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

thì lỗi (error / 오류) handling bị lặp.

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

Lỗi (error / 오류) mã (code / 코드) như `USER_NOT_FOUND` ổn định hơn việc máy khách (client / 클라이언트) phụ thuộc raw Java lớp (class / 클래스) name hoặc raw English message.

---

# 36. `ProblemDetail`

Spring hiện đại hỗ trợ `ProblemDetail` để biểu diễn lỗi HTTP theo mô hình (model / 모델) chuẩn hóa.

```java
ProblemDetail problem =
        ProblemDetail.forStatus(
                HttpStatus.NOT_FOUND);

problem.setTitle("User not found");
problem.setProperty(
        "code",
        "USER_NOT_FOUND");
```

Bạn không bắt buộc phải dùng ngay ở Beginner, nhưng nên biết nó tồn tại vì lỗi (error / 오류) phản hồi (response / 응답) trong Spring mới không chỉ có custom DTO.

Công khai (public / 공개) lỗi (error / 오류) phản hồi (response / 응답) không nên lộ dấu vết ngăn xếp (stack trace / 스택 트레이스), SQL, bảng (table / 테이블) name, filesystem đường dẫn (path / 경로) hoặc nội bộ (internal / 내부) host.

---

# 37. Controller, dịch vụ (service / 서비스), Repository: vì sao cần tách?

Controller hiểu HTTP. dịch vụ (service / 서비스) hiểu use trường hợp (case / 사례). Repository hiểu persistence.

Controller:

```java
@RestController
class UserController {
    private final UserService service;
}
```

Dịch vụ (service / 서비스):

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

Đây là layered kiến trúc (architecture / 아키텍처) đơn giản, tốt cho Beginner vì responsibility rõ.

Nếu controller viết SQL trực tiếp, lô-gic nghiệp vụ (business logic / 비즈니스 로직) gắn với HTTP và cơ sở dữ liệu (database / 데이터베이스) cùng lúc. kiểm thử (test / 테스트) khó hơn và thay vận chuyển (transport / 전송)/persistence khó hơn.

**mẫu lập trình (programming pattern / 프로그래밍 패턴) — Thin Controller.** Controller chỉ nhận/validate/map HTTP, gọi use trường hợp (case / 사례) rồi map phản hồi (response / 응답).

**mẫu thiết kế (design pattern / 디자인 패턴) — Repository.** Repository che persistence mechanics khỏi ứng dụng (application / 애플리케이션)/lĩnh vực (domain / 도메인) mã (code / 코드).

---

# 38. lĩnh vực (domain / 도메인) đối tượng (object / 객체) và Spring Bean khác nhau

Không phải mọi đối tượng (object / 객체) đều nên là bean.

Spring beans thường là long-lived services/hạ tầng (infrastructure / 인프라):

```text
Controller
Service
Repository
HTTP client
Configuration
Scheduler
```

Lĩnh vực (domain / 도메인)/giá trị (value / 값) objects:

```text
Order
Money
Address
UserId
Email
```

thường được tạo bằng `new`, factory hoặc tải (load / 로드) từ persistence.

Ví dụ `Money` không cần:

```java
@Component
public class Money {
}
```

Nó không phải dùng chung (shared / 공유) dịch vụ (service / 서비스).

“Spring-managed everything” tạo lĩnh vực (domain / 도메인) mô hình (model / 모델) phụ thuộc khung phần mềm (framework / 프레임워크) vô ích.

---

# 39. Repository giao diện (interface / 인터페이스) trước cơ sở dữ liệu (database / 데이터베이스)

Để học DI mà không bị cơ sở dữ liệu (database / 데이터베이스) làm rối, hãy bắt đầu bằng in-memory repository.

```java
public interface UserRepository {
    User save(User user);
    Optional<User> findById(long id);
}
```

Hiện thực (implementation / 구현):

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

Khi chuyển sang JDBC, `UserService` không cần thay đổi nếu đặc tả hợp đồng (contract / 계약) repository giữ nguyên. Đây là lợi ích phụ thuộc (dependency / 의존성) Inversion nhìn thấy rất rõ.

---

# 40. JDBC là gì trước khi học Spring JDBC?

JDBC là Java tiêu chuẩn (standard / 표준) API để làm việc với relational cơ sở dữ liệu (database / 데이터베이스).

Plain JDBC luồng (flow / 흐름):

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

Mã (code / 코드) rất nhiều boilerplate.

Spring JDBC không thay SQL. Nó giảm boilerplate quanh JDBC.

---

# 41. DataSource là gì?

`DataSource` là lớp trừu tượng (abstraction / 추상화) cung cấp cơ sở dữ liệu (database / 데이터베이스) connections. Trong môi trường vận hành (production / 운영 환경), nó thường đại diện liên kết (connection / 연결) pool thay vì mở vật lý (physical / 물리적) liên kết (connection / 연결) mới cho mọi truy vấn (query / 쿼리).

Boot có thể auto-configure `DataSource` khi driver và cấu hình (configuration / 구성) phù hợp tồn tại.

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/demo
    username: demo
    password: ${DB_PASSWORD}
```

Không lần ghi nhận (commit / 커밋) secret thật vào Git.

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

Spring handles tài nguyên (resource / 자원) cleanup and exception translation around dùng chung (common / 공통) JDBC luồng (flow / 흐름), nhưng SQL vẫn do bạn kiểm soát.

Khung phần mềm (framework / 프레임워크) lớp trừu tượng (abstraction / 추상화) không thay kiến thức chỉ mục (index / 인덱스), phép nối (join / 조인), giao dịch (transaction / 트랜잭션), kế hoạch truy vấn (query plan / 쿼리 계획) và locking.

---

# 43. `JdbcClient`

Spring khung phần mềm (framework / 프레임워크) hiện đại có `JdbcClient`, một fluent facade cho dùng chung (common / 공통) JDBC operations.

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

# 44. ORM, JPA, Hibernate và Spring dữ liệu (data / 데이터) JPA

Đây là bốn khái niệm thường bị trộn.

**ORM** là kỹ thuật map đối tượng (object / 객체) với relational cơ sở dữ liệu (database / 데이터베이스).

**JPA/Jakarta Persistence** là specification/API tiêu chuẩn cho persistence trong Java ecosystem.

**Hibernate** là một hiện thực (implementation / 구현) ORM/JPA rất phổ biến.

**Spring dữ liệu (data / 데이터) JPA** là tầng (layer / 계층) của Spring giúp tạo repository lớp trừu tượng (abstraction / 추상화) và truy vấn (query / 쿼리) hỗ trợ (support / 지원) trên JPA.

Phụ thuộc (dependency / 의존성):

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

Thực thể (entity / 엔터티):

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

Spring dữ liệu (data / 데이터) tạo hiện thực (implementation / 구현) proxy cho giao diện (interface / 인터페이스).

---

# 45. `@Entity`, `@Table`, `@Id`, `@GeneratedValue`

`@Entity` nói lớp (class / 클래스) là persistence thực thể (entity / 엔터티). `@Table` map bảng (table / 테이블) name khi cần. `@Id` đánh dấu primary định danh (identity / 식별자) trong JPA. `@GeneratedValue` mô tả chiến lược (strategy / 전략) sinh ID.

Các generation strategies như `IDENTITY`, `SEQUENCE`, `AUTO` không chỉ là cú pháp (syntax / 문법). Chúng ảnh hưởng cách ORM insert và batch. Chi tiết sẽ sang Intermediate/cấp cao (senior / 시니어).

---

# 46. giao dịch (transaction / 트랜잭션) là gì trước khi học `@Transactional`?

Giao dịch (transaction / 트랜잭션) là một nhóm cơ sở dữ liệu (database / 데이터베이스) operations được coi như một đơn vị (unit / 단위). Ví dụ chuyển tiền:

```text
trừ account A
+
cộng account B
```

Nếu thao tác (operation / 연산) thứ hai thất bại (fail / 실패) mà thao tác (operation / 연산) thứ nhất đã lần ghi nhận (commit / 커밋), dữ liệu sai. giao dịch (transaction / 트랜잭션) giúp hai thay đổi lần ghi nhận (commit / 커밋) cùng hoặc quay lui (rollback / 롤백) cùng trong cùng transactional tài nguyên (resource / 자원).

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

Spring cho phép declarative giao dịch (transaction / 트랜잭션):

```java
@Transactional
public void transfer(...) {
    debit(...);
    credit(...);
}
```

Nhưng annotation hoạt động nhờ giao dịch (transaction / 트랜잭션) hạ tầng (infrastructure / 인프라)/proxy. Đây là lý do hiểu proxy ở Intermediate rất quan trọng.

---

# 47. `@Transactional` ở Beginner nên hiểu đến đâu?

Ở Beginner, hãy hiểu ba điều. Thứ nhất, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) nên gần nghiệp vụ (business / 비즈니스) use trường hợp (case / 사례). Thứ hai, phương thức (method / 메서드) chạy trong giao dịch (transaction / 트랜잭션) có thể lần ghi nhận (commit / 커밋) hoặc quay lui (rollback / 롤백) dựa trên kết quả/exception. Thứ ba, `@Transactional` không biến HTTP lời gọi (call / 호출) sang dịch vụ (service / 서비스) khác thành cùng cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션).

Một anti-pattern:

```java
@Transactional
public void checkout() {
    orderRepository.save(...);
    externalPaymentApi.call();
    emailApi.send();
}
```

Phương thức (method / 메서드) có thể giữ DB liên kết (connection / 연결)/locks trong khi chờ mạng (network / 네트워크), và giao dịch (transaction / 트랜잭션) cục bộ (local / 로컬) không thể quay lui (rollback / 롤백) payment đã hoàn thành ở bên ngoài (external / 외부) dịch vụ (service / 서비스).

Chi tiết propagation, isolation và quay lui (rollback / 롤백) rules sẽ ở Intermediate.

---

# 48. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션): tại sao không để ORM tự sửa lược đồ (schema / 스키마) môi trường vận hành (production / 운영 환경)?

Demo có thể dùng JPA DDL auto. môi trường vận hành (production / 운영 환경) cần lược đồ (schema / 스키마) evolution được version-control.

Hai tools phổ biến:

```text
Flyway
Liquibase
```

Flyway thường dùng SQL di chuyển (migration / 마이그레이션):

```text
V1__create_users.sql
V2__add_user_email_index.sql
```

Ứng dụng (application / 애플리케이션) phiên bản (version / 버전) và cơ sở dữ liệu (database / 데이터베이스) lược đồ (schema / 스키마) phiên bản (version / 버전) phải evolve có kiểm soát.

Bạn chưa cần học sâu ở Beginner, nhưng hãy hình thành nguyên tắc: **lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) là sản phẩm tạo ra (artifact / 산출물) của software delivery**, không phải thao tác thủ công ngẫu nhiên trên môi trường vận hành (production / 운영 환경) DB.

---

# 49. Spring HTTP máy khách (client / 클라이언트): gọi API bên ngoài

Backend không chỉ nhận HTTP; nó còn gọi dịch vụ (service / 서비스) khác.

Spring hiện đại có `RestClient` cho synchronous imperative máy khách (client / 클라이언트):

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

Mã (code / 코드) thật nên cấu hình máy khách (client / 클라이언트) thành bean, externalize cơ sở (base / 기반) URL/hết thời gian chờ (timeout / 타임아웃) và translate lỗi.

Legacy dự án (project / 프로젝트) có `RestTemplate`. Reactive ngăn xếp (stack / 스택) có `WebClient`.

Beginner chỉ cần hiểu sự khác nhau: `RestClient` phù hợp synchronous imperative style; `WebClient` thuộc reactive/non-blocking style và cần học Reactor để dùng đúng.

---

# 50. hết thời gian chờ (timeout / 타임아웃) là yêu cầu (requirement / 요구사항), không phải option phụ

Bên ngoài (external / 외부) lời gọi (call / 호출) có thể treo/chậm. Nếu không có hết thời gian chờ (timeout / 타임아웃), yêu cầu (request / 요청) luồng thực thi (thread / 스레드) hoặc virtual luồng thực thi (thread / 스레드) có thể chờ rất lâu, liên kết (connection / 연결) bị chiếm và hệ thống (system / 시스템) có thể cascade thất bại (failure / 실패).

Do đó máy khách (client / 클라이언트) cấu hình (config / 설정) cần nghĩ đến:

```text
connect timeout
response/read timeout
overall deadline
```

Chính xác (exact / 정확한) API phụ thuộc underlying máy khách (client / 클라이언트).

**cấp cao (senior / 시니어) mẫu (pattern / 패턴) — Bounded Waiting.** Mọi remote/blocking phụ thuộc (dependency / 의존성) cần giới hạn thời gian. “Không giới hạn” là một thất bại (failure / 실패) chính sách (policy / 정책), thường là chính sách (policy / 정책) tệ.

---

# 51. Logging trong Spring Boot

Không dùng `System.out.println` làm logging môi trường vận hành (production / 운영 환경).

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

Parameterized logging tránh xây chuỗi không cần thiết khi log mức (level / 수준) không bật và tạo format thống nhất.

Không log password, truy cập (access / 접근) đơn vị từ (token / 토큰), refresh đơn vị từ (token / 토큰), private keys hoặc raw sensitive dữ liệu (data / 데이터).

---

# 52. Actuator là gì?

`spring-boot-starter-actuator` cung cấp production-oriented management features.

Health:

```text
/actuator/health
```

Các endpoint/năng lực (capability / 역량) khác có thể liên quan metrics, cấu hình (config / 설정), mappings, luồng thực thi (thread / 스레드) dump và thời gian chạy (runtime / 런타임) insight, tùy exposure.

Health endpoint thường được bộ cân bằng tải (load balancer / 로드 밸런서) hoặc Kubernetes dùng để biết ứng dụng (application / 애플리케이션) có sẵn sàng không.

Management endpoints có thể lộ thông tin nhạy cảm. Không expose tất cả ra công khai (public / 공개) Internet.

---

# 53. Liveness và Readiness

Liveness trả lời: “tiến trình (process / 프로세스) có bị hỏng đến mức restart có thể giúp không?”

Readiness trả lời: “instance có nên nhận traffic mới không?”

Cơ sở dữ liệu (database / 데이터베이스) tạm thời down thường làm ứng dụng (application / 애플리케이션) không ready, nhưng kill/restart liên tục ứng dụng (application / 애플리케이션) chưa chắc giúp DB sống lại.

Đây là ngữ nghĩa (semantics / 의미론) vận hành, không chỉ endpoint naming.

---

# 54. đơn vị (unit / 단위) kiểm thử (test / 테스트) không cần Spring

Dịch vụ (service / 서비스):

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

Đơn vị (unit / 단위) kiểm thử (test / 테스트):

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

Không có lý do tải (load / 로드) Spring ngữ cảnh (context / 맥락) nếu kiểm thử (test / 테스트) chỉ cần plain Java hành vi (behavior / 동작).

“Don’t start Spring if you don’t need Spring.”

---

# 55. `@SpringBootTest`

```java
@SpringBootTest
class ApplicationIntegrationTest {
}
```

annotation này tải (load / 로드) Boot ứng dụng (application / 애플리케이션) ngữ cảnh (context / 맥락) lớn hơn, phù hợp kiểm thử (test / 테스트) wiring/auto-configuration/tích hợp (integration / 통합).

Nếu mọi kiểm thử (test / 테스트) đều `@SpringBootTest`, suite chậm và lỗi khó localize.

---

# 56. MVC kiểm thử (test / 테스트)

`@WebMvcTest` tập trung vào web tầng (layer / 계층).

Concept:

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
}
```

Bạn có thể replace dịch vụ (service / 서비스) phụ thuộc (dependency / 의존성) bằng kiểm thử (test / 테스트) mock theo Spring kiểm thử (test / 테스트) phiên bản (version / 버전) hiện đại.

Mục tiêu là kiểm thử (test / 테스트):

```text
routing
JSON
validation
status
exception advice
```

không cần real DB.

Intermediate sẽ đi sâu kiểm thử (test / 테스트) slices và Boot 4 testing APIs.

---

# 57. bảo mật (security / 보안): Beginner cần hiểu gì?

Spring bảo mật (security / 보안) là một subsystem lớn. Đừng học nó bằng cách bản sao (copy / 복사) một `SecurityFilterChain` rồi disable tất cả để yêu cầu (request / 요청) chạy.

Bạn chỉ cần nắm mô hình tư duy (mental model / 사고 모델):

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

Authentication trả lời “ai đang gọi”. Authorization trả lời “người này có được phép làm thao tác (operation / 연산) không”.

`401` thường liên quan authentication chưa thành công. `403` thường liên quan caller đã được nhận diện nhưng không có quyền.

CORS và CSRF là bảo mật (security / 보안)/trình duyệt (browser / 브라우저) topics khác nhau. CORS không phải authentication. CSRF không nên bị disable chỉ vì “API đang trả 403”.

---

# 58. `@Async`, `@Scheduled`, bộ nhớ đệm (cache / 캐시) và sự kiện (event / 이벤트): chỉ awareness ở Beginner

Spring có `@Async`, `@Scheduled`, bộ nhớ đệm (cache / 캐시) annotations và ứng dụng (application / 애플리케이션) events. Bạn sẽ gặp chúng rất sớm nên cần biết chúng tồn tại, nhưng không nên dùng trước khi hiểu ngữ nghĩa (semantics / 의미론).

`@Async` đưa thực thi (execution / 실행) sang executor/luồng thực thi (thread / 스레드) khác. Điều đó làm giao dịch (transaction / 트랜잭션) ngữ cảnh (context / 맥락), exception handling và ngữ cảnh (context / 맥락) propagation phức tạp.

`@Scheduled` chạy tác vụ (task / 작업) theo scheduler của mỗi ứng dụng (application / 애플리케이션) instance. Nếu deploy 3 replicas, job có thể chạy 3 lần.

`@Cacheable` có thể bỏ qua phương thức (method / 메서드) khi bộ nhớ đệm (cache / 캐시) hit, nhưng annotation không tự quyết định TTL, kích thước (size / 크기), eviction hoặc phân tán (distributed / 분산) consistency.

`@EventListener` là in-process sự kiện (event / 이벤트) listener và mặc định không phải durable messaging giống Kafka.

Intermediate sẽ mở tất cả các phần này.

---

# 59. gói (package / 패키지) cấu trúc (structure / 구조) nên dùng khi bắt đầu

Thay vì:

```text
controller/
service/
repository/
entity/
```

cho toàn dự án (project / 프로젝트), gói (package / 패키지) by tính năng (feature / 기능) giúp mã (code / 코드) liên quan nằm gần nhau:

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

Dự án (project / 프로젝트) nhỏ dùng layered packages vẫn được. Nhưng khi lớn, package-by-feature thường giúp cohesion tốt hơn.

Folder cấu trúc (structure / 구조) không chữa được coupling nếu các mô-đun (module / 모듈) gọi nhau tùy tiện. ranh giới (boundary / 경계) là phụ thuộc (dependency / 의존성) rules, không chỉ thư mục.

---

# 60. Một REST luồng (flow / 흐름) hoàn chỉnh

Yêu cầu (request / 요청):

```http
POST /users
Content-Type: application/json

{
  "name": "Kim",
  "email": "kim@example.com"
}
```

Yêu cầu (request / 요청) DTO:

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

Dịch vụ (service / 서비스):

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

Luồng (flow / 흐름):

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

Đây là mô hình tư duy (mental model / 사고 모델) nền tảng bạn phải nhìn thấy trước khi học internals.

---

# 61. ngôn ngữ (language / 언어) Idioms cần hình thành ở Beginner

**Constructor Injection.** Required dependencies đi vào constructor và trường dữ liệu (field / 필드) nên `final` khi có thể. Điều này làm đối tượng (object / 객체) luôn hợp lệ sau construction.

**Thin Controller.** Controller chỉ chịu vận chuyển (transport / 전송) concerns: nhận yêu cầu (request / 요청), kiểm tra hợp lệ (validation / 검증), ánh xạ (mapping / 매핑), status/headers và gọi use trường hợp (case / 사례).

**Stateless Singleton dịch vụ (service / 서비스).** Không lưu trạng thái (state / 상태) của từng yêu cầu (request / 요청) vào trường dữ liệu (field / 필드) của singleton bean.

**Typed cấu hình (configuration / 구성).** Dùng `Duration`, `URI`, enum và cấu hình (configuration / 구성) thuộc tính (property / 속성) đối tượng (object / 객체) thay vì rải `String`/`int` magic values.

**ranh giới (boundary / 경계) DTO.** công khai (public / 공개) HTTP đặc tả hợp đồng (contract / 계약) không phải persistence thực thể (entity / 엔터티).

**thất bại (fail / 실패) Fast.** Required cấu hình (config / 설정) sai hoặc phụ thuộc (dependency / 의존성) thiếu nên thất bại (fail / 실패) lúc startup nếu có thể, thay vì chờ môi trường vận hành (production / 운영 환경) yêu cầu (request / 요청) đầu tiên mới phát hiện.

---

# 62. Coding / Programming Patterns cần nhận ra

**Repository mẫu (pattern / 패턴)** đặt lớp trừu tượng (abstraction / 추상화) giữa lô-gic nghiệp vụ (business logic / 비즈니스 로직) và persistence. **phụ thuộc (dependency / 의존성) Injection** externalize đối tượng (object / 객체) wiring. **cấu hình (configuration / 구성) đối tượng (object / 객체)** gom typed settings. **Exception Translation** chuyển lỗi hạ tầng (infrastructure / 인프라) thành lỗi có nghĩa ở ứng dụng (application / 애플리케이션) ranh giới (boundary / 경계). **Guard Clause** giảm nesting trong dịch vụ (service / 서비스)/lĩnh vực (domain / 도메인). **tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권)** xác định rõ ai tạo và ai close. **Layered kiến trúc (architecture / 아키텍처)** giúp Beginner hiểu separation of concerns. Sau này các mẫu (pattern / 패턴) này sẽ được nâng lên Ports & Adapters, Outbox, Idempotency và Resilience.

---

# 63. thiết kế (design / 설계) Patterns liên hệ trực tiếp với Spring

Spring bộ chứa (container / 컨테이너) có vai trò gần **Factory** vì nó tạo đối tượng (object / 객체). `DispatcherServlet` là **Front Controller**. `JdbcTemplate` là ví dụ nổi tiếng của **Template phương thức (method / 메서드)/Template-style lớp trừu tượng (abstraction / 추상화)**: khung phần mềm (framework / 프레임워크) quản lý luồng (flow / 흐름) lặp lại, caller cung cấp phần biến đổi. Spring AOP và nhiều annotation hạ tầng (infrastructure / 인프라) dựa trên **Proxy**. phụ thuộc (dependency / 의존성) selection có thể implement **chiến lược (strategy / 전략)**. HTTP/cơ sở dữ liệu (database / 데이터베이스)/vendor integrations thường đóng vai trò **Adapter**.

Không cần học thuộc tên mẫu (pattern / 패턴) trước khi hiểu bài toán (problem / 문제). mẫu (pattern / 패턴) chỉ hữu ích khi bạn hiểu lực kéo thiết kế mà nó giải quyết.

---

# 64. Các lỗi Beginner thường gặp và cách suy nghĩ đúng

Lỗi đầu tiên là dùng `new` để tạo một dịch vụ (service / 서비스) vốn được Spring quản lý, rồi thắc mắc vì sao phụ thuộc (dependency / 의존성) không được inject. Nếu lớp (class / 클래스) là bean, hãy để bộ chứa (container / 컨테이너) tạo nó hoặc chỉ `new` nó trong đơn vị (unit / 단위) kiểm thử (test / 테스트) với phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적).

Lỗi thứ hai là trường dữ liệu (field / 필드) injection vì ngắn. Hãy ưu tiên constructor.

Lỗi thứ ba là đưa lô-gic nghiệp vụ (business logic / 비즈니스 로직) vào controller. Controller là HTTP adapter, không phải lĩnh vực (domain / 도메인).

Lỗi thứ tư là dùng thực thể (entity / 엔터티) làm yêu cầu (request / 요청)/phản hồi (response / 응답). Hãy tách ranh giới (boundary / 경계) DTO.

Lỗi thứ năm là hard-code URL/password/hết thời gian chờ (timeout / 타임아웃). Hãy externalize typed cấu hình (configuration / 구성).

Lỗi thứ sáu là thêm `@Transactional`, `@Async`, `@Cacheable` như “fix annotation” mà không hiểu proxy/thực thi (execution / 실행) ngữ cảnh (context / 맥락). Nếu hành vi (behavior / 동작) phụ thuộc proxy, self-call hoặc vòng đời (lifecycle / 생명주기) có thể làm annotation không hoạt động như bạn tưởng.

Lỗi thứ bảy là đọc tutorial Boot 2 rồi bản sao (copy / 복사) `javax.*` vào Boot 4. Luôn check generation.

---

# 65. Mini dự án (project / 프로젝트) Beginner: người dùng (user / 사용자) Management API

Hãy xây một ứng dụng (application / 애플리케이션) có các endpoint `POST /users`, `GET /users/{id}`, `GET /users`, `PUT /users/{id}` và `DELETE /users/{id}`. Bắt đầu bằng `InMemoryUserRepository` để tập trung vào Spring cốt lõi (core / 핵심), DI, MVC, kiểm tra hợp lệ (validation / 검증) và exception handling. Khi luồng (flow / 흐름) chạy ổn, thay repository bằng Spring JDBC mà không đổi đặc tả hợp đồng (contract / 계약) của dịch vụ (service / 서비스). Sau đó thêm JPA hiện thực (implementation / 구현) để cảm nhận sự khác biệt giữa JDBC và ORM.

Dự án (project / 프로젝트) phải có typed `@ConfigurationProperties`, một `Clock` bean để kiểm thử (test / 테스트) time-dependent lô-gic (logic / 논리), toàn cục (global / 전역) lỗi (error / 오류) handling, Actuator health, đơn vị (unit / 단위) kiểm thử (test / 테스트) dịch vụ (service / 서비스) không tải (load / 로드) Spring, MVC kiểm thử (test / 테스트) và ít nhất một full kiểm thử tích hợp (integration test / 통합 테스트).

Khi bạn thay repository hiện thực (implementation / 구현) mà controller/dịch vụ (service / 서비스) gần như không phải đổi, bạn đã thực sự hiểu giá trị của DI thay vì chỉ thuộc `@Autowired`.

---

# 66. Beginner → Intermediate Gate

Bạn sẵn sàng sang Intermediate khi có thể tự giải thích, bằng lời của mình, một yêu cầu (request / 요청) từ trình duyệt (browser / 브라우저) đi qua embedded máy chủ (server / 서버) và Spring MVC đến controller/dịch vụ (service / 서비스)/repository rồi quay về JSON. Bạn phải giải thích được Spring bean khác đối tượng (object / 객체) Java bình thường ở đâu, ApplicationContext làm gì, constructor injection hoạt động thế nào, `@Component` khác `@Bean` về cách registration, singleton phạm vi (scope / 범위) có ý nghĩa gì, vì sao singleton dịch vụ (service / 서비스) không tự thread-safe, bean vòng đời (lifecycle / 생명주기) cơ bản ra sao và auto-configuration dựa trên classpath/cấu hình (configuration / 구성)/defaults như thế nào.

Ở web tầng (layer / 계층), bạn phải hiểu `@PathVariable`, `@RequestParam`, `@RequestBody`, DTO, kiểm tra hợp lệ (validation / 검증), HTTP status và toàn cục (global / 전역) exception handling. Ở persistence, bạn phải phân biệt JDBC, Spring JDBC, JPA, Hibernate và Spring dữ liệu (data / 데이터) JPA. Với giao dịch (transaction / 트랜잭션), bạn chưa cần thuộc propagation nhưng phải hiểu atomic cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) đơn vị (unit / 단위) và biết `@Transactional` không tạo phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션). Với testing, bạn phải hiểu vì sao plain đơn vị (unit / 단위) kiểm thử (test / 테스트) không cần Spring ngữ cảnh (context / 맥락).

Nếu bạn chỉ nhớ “annotation X dùng để Y” nhưng không dấu vết (trace / 추적) được luồng (flow / 흐름), chưa nên sang Intermediate.

---

# 67. Bạn sẽ học gì ở Part 2?

Part 2 sẽ mở chiếc hộp mà Part 1 mới chỉ nhìn từ bên ngoài. Bạn sẽ học `BeanDefinition`, `BeanFactory`, `ApplicationContext`, bean creation phases, post-processors, `FactoryBean`, `ObjectProvider`, scoped proxy và phụ thuộc (dependency / 의존성) candidate resolution. Spring MVC sẽ được mở thành `DispatcherServlet → HandlerMapping → HandlerAdapter → ArgumentResolver → HttpMessageConverter`. `@Transactional` sẽ được giải bằng proxy, giao dịch (transaction / 트랜잭션) manager, vật lý (physical / 물리적)/logical giao dịch (transaction / 트랜잭션), propagation, isolation, rollback-only và tài nguyên (resource / 자원) binding.

Persistence sẽ đi vào thực thể (entity / 엔터티) vòng đời (lifecycle / 생명주기), persistence ngữ cảnh (context / 맥락), dirty checking, lazy loading, N+1, fetch chiến lược (strategy / 전략), pagination và locking. Sau đó mới đến RestClient/HTTP giao diện (interface / 인터페이스), WebClient, events, async, scheduling, caching, bảo mật (security / 보안), kiểm thử (test / 테스트) slices, Testcontainers, Actuator, Micrometer và Virtual Threads.

Đó là lúc Spring chuyển từ “khung phần mềm (framework / 프레임워크) tôi đang dùng” thành “thời gian chạy (runtime / 런타임) mô hình (model / 모델) tôi hiểu”.

---

<!-- VERSION_DETAIL_PART1_2026-09-12_START -->
# Phiên bản (version / 버전) Deep Dive cho Beginner: nhìn dự án (project / 프로젝트) và nhận ra Spring generation

Ở Beginner, mục tiêu của phiên bản (version / 버전) kiến thức (knowledge / 지식) không phải học lịch sử bản phát hành (release / 릴리스). Mục tiêu là mở một dự án (project / 프로젝트) và nhận ra ngay generation để không bản sao (copy / 복사) nhầm tutorial.

Nếu thấy `javax.persistence.*` hoặc `javax.validation.*`, dự án (project / 프로젝트) gần như chắc chắn thuộc generation trước Boot 3. Boot 3+ chuyển sang `jakarta.persistence.*`, `jakarta.validation.*` và Jakarta ecosystem. Đây là breaking di chuyển (migration / 마이그레이션) lớn chứ không chỉ rename gói (package / 패키지).

Nếu dự án (project / 프로젝트) dùng Boot 3.5.x, hãy nghĩ khung phần mềm (framework / 프레임워크) 6.2 generation: Java 17 minimum, Jakarta không gian tên (namespace / 네임스페이스) và Servlet 6.0-era ngăn xếp (stack / 스택). Đây là line rất quan trọng khi đọc mã (code / 코드) enterprise hiện tại.

Nếu dự án (project / 프로젝트) dùng Boot 4, hãy chú ý Boot 4 modularize phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) mạnh hơn. di chuyển (migration / 마이그레이션) guide chuẩn hóa nhiều starter names; web MVC starter hiện là `spring-boot-starter-webmvc`, bảo mật (security / 보안) OAuth2 starters đi theo nhóm `spring-boot-starter-security-*`, và nhiều technology/kiểm thử (test / 테스트) integrations có dedicated starters riêng. Flyway/Liquibase cũng có Boot starter riêng trong Boot 4 di chuyển (migration / 마이그레이션) mô hình (model / 모델).

Boot 4 ưu tiên Jackson 3. Jackson 3 đổi nhiều group/gói (package / 패키지) names từ `com.fasterxml.jackson` sang `tools.jackson`, trong khi annotations giữ tính tương thích (compatibility / 호환성) riêng. Nếu bạn chỉ dùng DTO + `@RestController`, Boot che phần lớn thay đổi; nếu tự custom mapper/modules thì phiên bản (version / 버전) trở nên rất quan trọng.

Spring khung phần mềm (framework / 프레임워크) 7 chuyển null-safety sang JSpecify. Beginner chưa cần cấu hình NullAway, nhưng nên biết tại sao IDE/Kotlin có thể báo nullability khác tutorial khung phần mềm (framework / 프레임워크) 5/6.

Khi tạo dự án (project / 프로젝트) mới ở thời điểm hiện tại, một baseline học hợp lý là Java 21 hoặc 25 với Boot 4.1.x. Java 17 vẫn là minimum, còn phiên bản (version / 버전) môi trường vận hành (production / 운영 환경) thật phải theo nền tảng (platform / 플랫폼)/vendor/khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원) của công ty.
<!-- VERSION_DETAIL_PART1_2026-09-12_END -->

---

# 68. phiên bản (version / 버전) references

Các phần phụ thuộc phiên bản (version / 버전) trong tệp (file / 파일) này dựa trên documentation chính thức hiện tại. Spring Boot hệ thống (system / 시스템) requirements: https://docs.spring.io/spring-boot/system-requirements.html

Spring khung phần mềm (framework / 프레임워크) tham chiếu (reference / 참조): https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/

Spring Boot tham chiếu (reference / 참조): https://docs.spring.io/spring-boot/tham chiếu (reference / 참조)/

Boot 4 di chuyển (migration / 마이그레이션) guide: https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Khi đọc tài liệu cũ, luôn xác định nó thuộc Boot 2, Boot 3 hay Boot 4 trước khi bản sao (copy / 복사) mã (code / 코드).

> **Bàn giao:** Sau **Học phiên bản (version / 버전) theo “cách viết ứng dụng (application / 애플리케이션) thay đổi”, không theo release-note danh sách (list / 목록)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [spring part2 intermediate rewritten detailed](./spring_part2_intermediate_rewritten_detailed.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.

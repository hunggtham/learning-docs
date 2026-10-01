# Java Spring — Part 2: Intermediate

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Java Spring — Part 2: Intermediate**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ “biết dùng Spring” đến “hiểu bộ chứa (container / 컨테이너), proxy, giao dịch (transaction / 트랜잭션) và persistence thời gian chạy (runtime / 런타임)”** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## Từ “biết dùng Spring” đến “hiểu bộ chứa (container / 컨테이너), proxy, giao dịch (transaction / 트랜잭션) và persistence thời gian chạy (runtime / 런타임)”

> Part 2 giả định bạn đã hoàn thành Part 1 và có thể tự xây một REST API nhỏ. Ở đây mục tiêu không còn là nhớ thêm annotation. Mục tiêu là hiểu Spring đang làm gì **trước khi bean tồn tại, trong lúc bean được tạo, khi phương thức (method / 메서드) đi qua proxy, khi yêu cầu (request / 요청) đi qua MVC chuỗi xử lý (pipeline / 파이프라인), khi giao dịch (transaction / 트랜잭션) giữ liên kết (connection / 연결) và khi JPA giữ thực thể (entity / 엔터티) trong persistence ngữ cảnh (context / 맥락)**.

---

<!-- VERSION_UPDATE_2026-09-12_START -->

> **Chuyển mạch:** Bản đồ phiên bản nối câu hỏi “biết dùng Spring” với container, proxy, transaction và persistence runtime. Tiếp theo, `ApplicationContext.refresh()` được đọc như pipeline metadata → object graph để thấy cơ chế thay vì ghi nhớ annotation.

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
# 1. Cách tư duy ở mức (level / 수준) Intermediate

Ở Beginner, bạn nhìn:

```java
@Service
class UserService {
}
```

và hiểu “Spring tạo bean này”.

Ở Intermediate, bạn cần hỏi thêm: Spring biết lớp (class / 클래스) này bằng siêu dữ liệu (metadata / 메타데이터) nào? siêu dữ liệu (metadata / 메타데이터) được đăng ký khi nào? bộ chứa (container / 컨테이너) dùng definition nào để tạo đối tượng (object / 객체)? phụ thuộc (dependency / 의존성) được resolve trước hay sau constructor? Bean có bị một `BeanPostProcessor` wrap thành proxy không? tham chiếu (reference / 참조) mà controller nhận là mục tiêu (target / 대상) đối tượng (object / 객체) hay proxy?

Tương tự, khi nhìn:

```java
@Transactional
public void transfer() {
}
```

bạn không được dừng ở “phương thức (method / 메서드) có giao dịch (transaction / 트랜잭션)”. Bạn phải hỏi phương thức (method / 메서드) lời gọi (call / 호출) có đi qua Spring proxy không, giao dịch (transaction / 트랜잭션) manager nào được chọn, đang phép nối (join / 조인) giao dịch (transaction / 트랜잭션) cũ hay tạo giao dịch (transaction / 트랜잭션) mới, DB liên kết (connection / 연결) được giữ trong bao lâu, exception nào làm quay lui (rollback / 롤백) và side tác động (effect / 효과) ngoài DB có nằm trong cùng atomic ranh giới (boundary / 경계) không.

Đó là thay đổi tư duy chính của Part 2.

---

# 2. BeanFactory và ApplicationContext

`BeanFactory` là lớp trừu tượng (abstraction / 추상화) lõi của IoC bộ chứa (container / 컨테이너). Nó biết bean definitions, tạo đối tượng (object / 객체), resolve dependencies và cung cấp bean lookup. `ApplicationContext` xây trên BeanFactory và bổ sung các application-level năng lực (capability / 역량) như events, tài nguyên (resource / 자원) loading, môi trường (environment / 환경), message resolution và tự động nhận các post-processors.

Trong Spring Boot, bạn gần như luôn làm việc với `ApplicationContext`. Nhưng biết `BeanFactory` là quan trọng vì rất nhiều lỗi (error / 오류) message và nội bộ (internal / 내부) kiểu (type / 타입) xoay quanh bean factory.

Mô hình tư duy (mental model / 사고 모델):

```text
ApplicationContext
    └── BeanFactory
          ├── BeanDefinitions
          ├── singleton registry
          ├── dependency resolution
          └── creation/lifecycle machinery
```

Một `ApplicationContext` không phải chỉ là `Map<String,Object>`. Nó giữ siêu dữ liệu (metadata / 메타데이터) và hạ tầng (infrastructure / 인프라) để tạo đối tượng (object / 객체) đúng lúc, đúng phạm vi (scope / 범위) và đúng vòng đời (lifecycle / 생명주기).

---

# 3. BeanDefinition là gì?

Trước khi singleton `UserService` instance tồn tại, bộ chứa (container / 컨테이너) cần biết **cách** tạo nó. `BeanDefinition` là siêu dữ liệu (metadata / 메타데이터) kiểu blueprint.

Nó có thể mô tả bean lớp (class / 클래스), phạm vi (scope / 범위), lazy flag, factory phương thức (method / 메서드), constructor siêu dữ liệu (metadata / 메타데이터), init/destroy phương thức (method / 메서드), qualifiers, phụ thuộc (dependency / 의존성) siêu dữ liệu (metadata / 메타데이터) và các flags khác.

Khi thành phần (component / 컴포넌트) scanning tìm:

```java
@Service
public class UserService {
}
```

Spring không nhất thiết `new UserService()` ngay. Nó trước hết register siêu dữ liệu (metadata / 메타데이터). Sau đó ở ngữ cảnh (context / 맥락) refresh/bean creation phase, siêu dữ liệu (metadata / 메타데이터) này được dùng để tạo instance.

Đây là lý do hai khái niệm phải tách rõ:

```text
BeanDefinition exists
≠
Bean instance already exists
```

Một lazy bean có definition nhưng chưa có instance. Một request-scoped bean có definition toàn thời gian nhưng instance thay đổi theo yêu cầu (request / 요청).

---

# 4. BeanDefinitionRegistry

Bean definitions phải được lưu ở đâu đó. `BeanDefinitionRegistry` là lớp trừu tượng (abstraction / 추상화) cho việc register/remove/truy vấn (query / 쿼리) bean definitions.

Ứng dụng (application / 애플리케이션) mã (code / 코드) bình thường không dùng trực tiếp. Nhưng khung phần mềm (framework / 프레임워크) authors và advanced hạ tầng (infrastructure / 인프라) có thể register động (dynamic / 동적) beans programmatically.

Việc hiểu registry giúp bạn thấy thành phần (component / 컴포넌트) scanning chỉ là **một nguồn tạo definitions**. `@Bean`, auto-configuration, imports, XML cũ, programmatic registry và khung phần mềm (framework / 프레임워크) extensions đều có thể đưa bean definitions vào bộ chứa (container / 컨테이너).

---

# 5. bộ chứa (container / 컨테이너) startup vòng đời (lifecycle / 생명주기) chi tiết hơn

Một luồng (flow / 흐름) đơn giản hóa nhưng hữu ích:

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

Điểm quan trọng là **siêu dữ liệu (metadata / 메타데이터) processing** xảy ra trước phần lớn đối tượng (object / 객체) creation, còn **bean instance processing** xảy ra sau khi đối tượng (object / 객체) đã được instantiate.

Nếu bạn hiểu hai giai đoạn này, `BeanFactoryPostProcessor` và `BeanPostProcessor` sẽ không còn dễ nhầm.

---

<!-- SPRING_BATCH1_IOC_INTERMEDIATE -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 2: Intermediate**, **Bản đồ phiên bản (version / 버전) dùng xuyên suốt tài liệu — cập nhật 2026-09-21** nêu điều cần giải thích; **ApplicationContext.refresh() dưới dạng một chuỗi xử lý (pipeline / 파이프라인) siêu dữ liệu (metadata / 메타데이터) → đối tượng (object / 객체) đồ thị (graph / 그래프)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Vòng đời yêu cầu (request lifecycle / 요청 생명주기) end-to-end: từ servlet bộ chứa (container / 컨테이너) tới phản hồi (response / 응답) lần ghi nhận (commit / 커밋)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `ApplicationContext.refresh()` dưới dạng một chuỗi xử lý (pipeline / 파이프라인) siêu dữ liệu (metadata / 메타데이터) → đối tượng (object / 객체) đồ thị (graph / 그래프)

Một `ApplicationContext` đi vào trạng thái usable không phải bằng một lệnh “scan rồi new tất cả”. Với `AbstractApplicationContext`, mô hình tư duy (mental model / 사고 모델) hữu ích là phương thức (method / 메서드) `refresh()` điều phối nhiều phase. môi trường (environment / 환경) và cấu hình (configuration / 구성) sources được chuẩn bị; BeanDefinitions được tải (load / 로드); factory-level processors có cơ hội thay siêu dữ liệu (metadata / 메타데이터); BeanPostProcessors được đăng ký; sau đó eager singletons mới được instantiate; cuối cùng vòng đời (lifecycle / 생명주기)/sự kiện (event / 이벤트) hạ tầng (infrastructure / 인프라) được hoàn tất.

`ConfigurationClassPostProcessor` là một thành phần (component / 컴포넌트) quan trọng ở nửa **siêu dữ liệu (metadata / 메타데이터)**. Nó parse `@Configuration`, `@ComponentScan`, `@Import`, `@Bean` và mở rộng cấu hình (configuration / 구성) đồ thị (graph / 그래프) thành thêm BeanDefinitions. `AutowiredAnnotationBeanPostProcessor` lại làm việc ở nửa **instance/vòng đời (lifecycle / 생명주기)**, đọc injection siêu dữ liệu (metadata / 메타데이터) và hỗ trợ resolve phụ thuộc (dependency / 의존성) cho constructor/trường dữ liệu (field / 필드)/phương thức (method / 메서드) injection. Hai lớp (class / 클래스) đều có chữ “processor” nhưng tham gia ở hai thời điểm rất khác nhau; đây là lý do phải tách siêu dữ liệu (metadata / 메타데이터) processing và instance processing trong đầu.

`DefaultListableBeanFactory` là nơi phụ thuộc (dependency / 의존성) resolution trở nên cụ thể. Khi constructor yêu cầu `PaymentGateway`, bộ chứa (container / 컨테이너) không chỉ tìm string bean name. Nó xem kiểu (type / 타입) assignability, generic kiểu (type / 타입) siêu dữ liệu (metadata / 메타데이터) khi có thể, qualifier, primary/fallback ngữ nghĩa (semantics / 의미론), bean-name fallback và trạng thái candidate. Nếu phụ thuộc (dependency / 의존성) là `List<PaymentGateway>`, bộ chứa (container / 컨테이너) resolve nhiều beans rồi thứ tự (order / 순서) chúng theo thứ tự (ordering / 순서) đặc tả hợp đồng (contract / 계약). Nếu phụ thuộc (dependency / 의존성) là `ObjectProvider<PaymentGateway>`, việc resolve đối tượng (object / 객체) có thể bị trì hoãn tới lúc provider được gọi.

Một phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) tốt phải có thể giải từ ngoài vào trong. Constructor cycle như `A(B)` và `B(A)` không thể tạo theo Java ngữ nghĩa (semantics / 의미론) vì để construct A cần B hoàn chỉnh, còn construct B lại cần A. Historical Spring machinery có thể xử lý một số setter/trường dữ liệu (field / 필드) cycles bằng early singleton references, nhưng constructor cycle cho thấy đồ thị (graph / 그래프) không có điểm bắt đầu rõ. Thay vì bật circular-reference option như một fix mặc định, hãy tìm responsibility đang bị trộn hoặc introduce một lớp trừu tượng (abstraction / 추상화)/sự kiện (event / 이벤트) ranh giới (boundary / 경계) phù hợp.

Một quy tắc gỡ lỗi (debug / 디버그) rất hiệu quả là phân loại lỗi theo phase. `NoSuchBeanDefinitionException` và `NoUniqueBeanDefinitionException` thường thuộc phụ thuộc (dependency / 의존성) resolution. Bean tạo được nhưng `@Transactional` không chạy thường thuộc proxy/post-processing hoặc lời gọi (call / 호출) đường dẫn (path / 경로). Bean không xuất hiện vì điều kiện (condition / 조건) không match thuộc siêu dữ liệu (metadata / 메타데이터)/auto-configuration. Khi xác định đúng phase, số lượng hypothesis giảm mạnh.
<!-- SPRING_BATCH1_IOC_INTERMEDIATE_END -->

---

# 6. BeanFactoryPostProcessor

`BeanFactoryPostProcessor` làm việc với bean factory/definitions trước khi normal beans được tạo.

Hãy nghĩ nó như giai đoạn:

```text
“sửa bản thiết kế trước khi xây nhà”
```

Nó có thể sửa properties/siêu dữ liệu (metadata / 메타데이터) hoặc register thêm definitions.

Ứng dụng (application / 애플리케이션) mã (code / 코드) ít khi cần implement. Nếu một dự án (project / 프로젝트) có custom `BeanFactoryPostProcessor`, đó là infrastructure-level mã (code / 코드) và cần đọc cẩn thận vì nó ảnh hưởng bộ chứa (container / 컨테이너) startup.

Một lỗi nguy hiểm là gọi `getBean()` quá sớm trong phase này, làm bean bị instantiate trước khi toàn bộ processing hạ tầng (infrastructure / 인프라) sẵn sàng.

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

Một post-processor có thể trả về cùng đối tượng (object / 객체) hoặc đối tượng (object / 객체) khác, ví dụ proxy.

Đây là cửa ngõ để hiểu rất nhiều Spring features. Injection annotations, vòng đời (lifecycle / 생명주기) annotations, AOP proxy creation và nhiều khung phần mềm (framework / 프레임워크) behaviors được triển khai qua post-processing hoặc các hạ tầng (infrastructure / 인프라) tương tự.

Nếu một bean “đáng lẽ phải transactional” nhưng không được proxy, một hypothesis là bean được tạo quá sớm trước khi auto-proxy creator có cơ hội xử lý.

---

# 8. vòng đời (lifecycle / 생명주기) callbacks sâu hơn

Một bean có thể trải qua constructor, phụ thuộc (dependency / 의존성) injection, Aware callbacks, pre-initialization post-processors, `@PostConstruct`, `InitializingBean.afterPropertiesSet`, custom init phương thức (method / 메서드), post-initialization processors và cuối cùng mới trở thành tham chiếu (reference / 참조) được sử dụng.

Có nhiều cơ chế để làm cùng loại việc. Điều đó không có nghĩa bạn nên dùng tất cả. ứng dụng (application / 애플리케이션) mã (code / 코드) hiện đại thường dùng constructor + `@PostConstruct` rất ít và tường minh (explicit / 명시적) vòng đời (lifecycle / 생명주기) bean khi tài nguyên (resource / 자원) phức tạp.

Nếu startup lô-gic (logic / 논리) có bên ngoài (external / 외부) I/O, hãy đặt hết thời gian chờ (timeout / 타임아웃) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) rõ. Một `@PostConstruct` gọi mạng (network / 네트워크) 20 phút không phải initialization tốt.

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

Ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스) bình thường không nên dùng `ApplicationContextAware` để fetch dependencies. Constructor injection rõ hơn.

Aware interfaces phù hợp khi thành phần (component / 컴포넌트) cần tương tác với bộ chứa (container / 컨테이너) hạ tầng (infrastructure / 인프라) như một khung phần mềm (framework / 프레임워크) tích hợp (integration / 통합).

---

# 10. FactoryBean khác `@Bean` như thế nào?

`@Bean` là annotation đặt trên factory phương thức (method / 메서드) trong cấu hình (configuration / 구성).

`FactoryBean<T>` là giao diện (interface / 인터페이스) đặc biệt của Spring. Bean được đăng ký là factory nhưng normal lookup thường nhận **sản phẩm (product / 제품)** của factory.

Ví dụ concept:

```text
FactoryBean<RemoteClient>
    ↓
getObject()
    ↓
RemoteClient
```

Nếu cần chính factory, bean name có ngữ nghĩa (semantics / 의미론) đặc biệt với `&`.

Frameworks dùng `FactoryBean` cho đối tượng (object / 객체) phức tạp như proxies/clients. ứng dụng (application / 애플리케이션) mã (code / 코드) bình thường rất ít khi cần tự viết một `FactoryBean`.

---

# 11. ObjectProvider và controlled lazy lookup

Có tình huống phụ thuộc (dependency / 의존성) không nên resolve ngay hoặc thật sự optional. Spring cung cấp `ObjectProvider<T>`.

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

Điều này tốt hơn tiêm `ApplicationContext` rồi `getBean` trong nghiệp vụ (business / 비즈니스) mã (code / 코드) vì phụ thuộc (dependency / 의존성) kiểu (type / 타입) vẫn tường minh (explicit / 명시적).

`ObjectProvider` cũng hữu ích cho optional bean, multiple beans và prototype resolution.

---

# 12. phụ thuộc (dependency / 의존성) resolution khi có nhiều candidates

Khi constructor cần:

```java
PaymentGateway gateway
```

Spring phải tìm candidate assignable với kiểu (type / 타입). Nếu một candidate, dễ. Nếu nhiều, bộ chứa (container / 컨테이너) xem qualifiers, primary và siêu dữ liệu (metadata / 메타데이터) khác để resolve.

Đây là lý do `NoUniqueBeanDefinitionException` không phải lỗi ngẫu nhiên; nó nói đối tượng (object / 객체) đồ thị (graph / 그래프) mơ hồ.

Bạn có thể dùng ngữ nghĩa (semantic / 의미적) custom qualifier:

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

Hiện thực (implementation / 구현):

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

Ngữ nghĩa (semantic / 의미적) qualifier bền hơn string bean name khi kiến trúc (architecture / 아키텍처) thật sự có category rõ.

---

# 13. Inject `List<T>` để tạo chuỗi xử lý (pipeline / 파이프라인)

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

Các beans có thể được thứ tự (order / 순서) bằng `@Order`/`Ordered`.

Đây là cách Spring rất tự nhiên để assemble **chuỗi (chain / 사슬) of Responsibility**.

```text
Order
→ StockValidator
→ PriceValidator
→ PolicyValidator
→ proceed
```

Inject collection của strategies thay vì viết một God Validator với `if` khổng lồ.

---

# 14. Inject `Map<String,T>` và chiến lược (strategy / 전략) Registry

Spring có thể inject:

```java
Map<String, PaymentGateway> gateways
```

key thường liên quan bean name.

Bạn có thể bản dựng (build / 빌드) registry:

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

Nghiệp vụ (business / 비즈니스) mã (code / 코드):

```java
registry.get(type).charge(...);
```

Điều này quy mô (scale / 규모) tốt hơn rải `if (type == CARD)` hoặc `@Qualifier` ở mọi nơi.

---

# 15. phạm vi (scope / 범위) tương tác (interaction / 상호작용): singleton inject prototype

Giả sử:

```java
@Scope("prototype")
@Component
class ReportContext {
}
```

và singleton dịch vụ (service / 서비스):

```java
@Service
class ReportService {
    private final ReportContext context;

    ReportService(ReportContext context) {
        this.context = context;
    }
}
```

Prototype được resolve lúc singleton tạo, nên dịch vụ (service / 서비스) giữ một instance đó. Prototype phạm vi (scope / 범위) không tự khiến trường dữ liệu (field / 필드) “refresh mỗi phương thức (method / 메서드) lời gọi (call / 호출)”.

Nếu cần instance mới mỗi lần, dùng provider:

```java
ReportContext context =
        provider.getObject();
```

Đây là ví dụ điển hình cho việc phạm vi (scope / 범위) là vòng đời (lifecycle / 생명주기) đặc tả hợp đồng (contract / 계약), không phải annotation decoration.

---

# 16. Scoped Proxy

Một singleton cần request-scoped phụ thuộc (dependency / 의존성). vật lý (physical / 물리적) yêu cầu (request / 요청) đối tượng (object / 객체) chỉ tồn tại trong từng yêu cầu (request / 요청), nhưng singleton sống suốt app.

Spring giải quyết bằng proxy:

```text
Singleton Service
     ↓ holds
RequestContext proxy
     ↓ delegates at runtime
Current request-scoped instance
```

Vì vậy injected tham chiếu (reference / 참조) không nhất thiết là mục tiêu (target / 대상) đối tượng (object / 객체) thật. Đây là cầu nối quan trọng sang AOP/proxy mindset.

---

# 17. Proxy là concept trung tâm của Spring

Rất nhiều tính năng Spring can thiệp vào phương thức (method / 메서드) lời gọi (call / 호출) bằng proxy:

```text
caller
  ↓
proxy
  ↓
interceptor/advice
  ↓
target
```

Transactions, phương thức (method / 메서드) bảo mật (security / 보안), caching, async và AOP thường dựa vào kiểu luồng (flow / 흐름) này.

Nếu bạn giữ mục tiêu (target / 대상) raw hoặc lời gọi (call / 호출) phương thức (method / 메서드) nội bộ qua `this`, interceptor có thể không chạy.

---

# 18. JDK động (dynamic / 동적) Proxy và Class-based Proxy

JDK động (dynamic / 동적) proxy chủ yếu proxy interfaces. Nếu mục tiêu (target / 대상) implement giao diện (interface / 인터페이스), proxy có thể expose interfaces.

Class-based proxy dùng subclass generation, truyền thống qua CGLIB. Vì nó subclass mục tiêu (target / 대상) nên final lớp (class / 클래스)/final phương thức (method / 메서드)/private phương thức (method / 메서드) có limitation tương ứng.

Ví dụ:

```java
public interface PaymentService {
    void pay();
}
```

JDK proxy có thể implement `PaymentService`.

Nếu mã (code / 코드) inject concrete `PaymentServiceImpl` thay vì giao diện (interface / 인터페이스), proxy chiến lược (strategy / 전략) có thể ảnh hưởng kiểu (type / 타입) tính tương thích (compatibility / 호환성).

“Program to intended công khai (public / 공개) lớp trừu tượng (abstraction / 추상화)” giúp giảm coupling với proxy mechanics.

---

# 19. Self-invocation bài toán (problem / 문제)

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

Lời gọi (call / 호출):

```java
this.saveAudit();
```

là Java lời gọi (call / 호출) trực tiếp trong cùng đối tượng (object / 객체). Nó không đi ra proxy rồi quay lại.

Luồng (flow / 흐름) thực tế:

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

ở lời gọi (call / 호출) thứ hai.

Giải pháp tốt thường là tách chính sách (policy / 정책) ranh giới (boundary / 경계) thành collaborator khác, không dùng hack self-proxy.

---

# 20. Spring AOP terminology

Một **Aspect** gom cross-cutting concern. **Pointcut** chọn nơi áp dụng. **Advice** là lô-gic (logic / 논리) chạy. **phép nối (join / 조인) điểm (point / 지점)** trong Spring AOP thường là phương thức (method / 메서드) thực thi (execution / 실행) có thể intercept. **mục tiêu (target / 대상)** là đối tượng (object / 객체) thật. **Proxy** là đối tượng (object / 객체) caller thường tương tác.

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

AOP hợp với cross-cutting hạ tầng (infrastructure / 인프라). nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) quan trọng không nên bị giấu trong pointcut khó nhìn.

---

# 21. Auto-configuration internals ở mức Intermediate

Boot auto-configuration là tập cấu hình (configuration / 구성) classes được import có điều kiện.

Các điều kiện (condition / 조건) phổ biến:

```java
@ConditionalOnClass(...)
@ConditionalOnMissingBean(...)
@ConditionalOnBean(...)
@ConditionalOnProperty(...)
```

`@ConditionalOnClass` nghĩa tính năng (feature / 기능) chỉ khả dụng nếu phụ thuộc (dependency / 의존성)/lớp (class / 클래스) cần thiết có mặt. `@ConditionalOnMissingBean` implement “default but back off”. `@ConditionalOnProperty` cho tính năng (feature / 기능) bật/tắt theo cấu hình (config / 설정).

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

Đây là mẫu (pattern / 패턴) nền cho starter/autoconfiguration ecosystem.

---

# 22. điều kiện (condition / 조건) Evaluation Report

Khi Boot không tạo bean bạn mong đợi, thay vì đoán hãy xem điều kiện (condition / 조건) report/gỡ lỗi (debug / 디버그).

Nó trả lời:

```text
Auto-configuration nào matched?
Cái nào không matched?
Condition nào fail?
```

Ví dụ DataSource auto-config không chạy có thể vì JDBC lớp (class / 클래스) thiếu, không có URL hoặc một điều kiện (condition / 조건) khác.

Không thêm annotation ngẫu nhiên khi có điều kiện (condition / 조건) report giải thích nguyên nhân.

---

# 23. cấu hình (configuration / 구성) Properties sâu hơn

Một subsystem nên có properties đối tượng (object / 객체):

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

Spring bind bên ngoài (external / 외부) văn bản (text / 텍스트) thành kiểu (type / 타입) rồi validate.

Nếu `connect-timeout: abc`, ứng dụng (application / 애플리케이션) có thể thất bại (fail / 실패) startup thay vì chạy với giá trị sai.

---

# 24. thuộc tính (property / 속성) nguồn (source / 소스) precedence

Một thuộc tính (property / 속성) có thể đến từ nhiều nguồn: packaged `application.yml`, profile-specific cấu hình (config / 설정), môi trường (environment / 환경) variables, JVM hệ thống (system / 시스템) properties, command-line arguments và kiểm thử (test / 테스트) overrides.

Điều quan trọng không phải thuộc bảng precedence ngay lập tức mà là hiểu **cùng một key có thể bị override**.

Khi cục bộ (local / 로컬) chạy đúng nhưng bộ chứa (container / 컨테이너) chạy khác, hãy kiểm tra effective cấu hình (config / 설정) nguồn (source / 소스).

Actuator/cấu hình (config / 설정) reports có thể hỗ trợ nhưng phải bảo vệ secrets.

---

# 25. Spring MVC chuỗi xử lý (pipeline / 파이프라인) chi tiết

Beginner mô hình tư duy (mental model / 사고 모델):

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

Mỗi stage giải quyết một loại lớp trừu tượng (abstraction / 추상화) khác.

---

<!-- SPRING_BATCH2_REQUEST_INTERMEDIATE -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Java Spring — Part 2: Intermediate**, **ApplicationContext.refresh() dưới dạng một chuỗi xử lý (pipeline / 파이프라인) siêu dữ liệu (metadata / 메타데이터) → đối tượng (object / 객체) đồ thị (graph / 그래프)** nêu điều cần giải thích; **Vòng đời yêu cầu (request lifecycle / 요청 생명주기) end-to-end: từ servlet bộ chứa (container / 컨테이너) tới phản hồi (response / 응답) lần ghi nhận (commit / 커밋)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **@Transactional đi từ siêu dữ liệu (metadata / 메타데이터) tới liên kết (connection / 연결) như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vòng đời yêu cầu (request lifecycle / 요청 생명주기) end-to-end: từ servlet bộ chứa (container / 컨테이너) tới phản hồi (response / 응답) lần ghi nhận (commit / 커밋)

Một yêu cầu (request / 요청) MVC bắt đầu trước Spring MVC. Tomcat hoặc Jetty nhận mạng (network / 네트워크) dữ liệu (data / 데이터), parse HTTP và tạo `HttpServletRequest`/`HttpServletResponse`. bộ chứa (container / 컨테이너) chọn thực thi (execution / 실행) luồng thực thi (thread / 스레드); với cấu hình virtual-thread hiện đại, mô hình thực thi (execution model / 실행 모델) có thể khác platform-thread pool nhưng Servlet đặc tả hợp đồng (contract / 계약) vẫn là yêu cầu (request / 요청) đi qua filter chuỗi (chain / 사슬) trước khi tới servlet đích.

Spring bảo mật (security / 보안) nếu được dùng nằm trong filter chuỗi (chain / 사슬) này, vì vậy authentication/authorization thường hoàn tất **trước** `DispatcherServlet`. Sau đó `DispatcherServlet#doDispatch` hỏi `HandlerMapping` để lấy `HandlerExecutionChain`, gọi `preHandle` của interceptors, chọn `HandlerAdapter`, rồi `RequestMappingHandlerAdapter` chuẩn bị invoke controller phương thức (method / 메서드). Argument resolvers lấy đường dẫn (path / 경로) variable, truy vấn (query / 쿼리) parameter, yêu cầu (request / 요청) body, principal hoặc custom ngữ cảnh (context / 맥락); dữ liệu (data / 데이터) binding/conversion tạo Java values; kiểm tra hợp lệ (validation / 검증) có thể reject yêu cầu (request / 요청) trước khi nghiệp vụ (business / 비즈니스) dịch vụ (service / 서비스) được gọi.

Nếu controller gọi ứng dụng (application / 애플리케이션) dịch vụ (service / 서비스) transactional, lúc đó điều khiển (control / 제어) mới đi qua dịch vụ (service / 서비스) proxy và giao dịch (transaction / 트랜잭션) interceptor. Repository/JPA chạy bên trong giao dịch (transaction / 트랜잭션); controller nhận kết quả (result / 결과); return-value handler quyết định xử lý `ResponseEntity`, DTO, async kiểu (type / 타입) hoặc view; `HttpMessageConverter` serialize body. Chỉ khi servlet phản hồi (response / 응답) được lần ghi nhận (commit / 커밋) thì status/headers/body bắt đầu trở thành đầu ra (output / 출력) không thể tự do thay đổi nữa.

Exception cũng có vòng đời (lifecycle / 생명주기). Exception từ controller không nhất thiết nhảy thẳng ra bộ chứa (container / 컨테이너); `HandlerExceptionResolver` chuỗi (chain / 사슬), trong đó có resolver cho `@ExceptionHandler`/`@ControllerAdvice`, có cơ hội map exception thành phản hồi (response / 응답). Exception ở filter trước DispatcherServlet lại nằm ngoài MVC exception-resolver đường dẫn (path / 경로) và thường cần bảo mật (security / 보안)/filter-level handling riêng. Đây là lý do cùng một exception kiểu (type / 타입) có thể được xử lý khác tùy nó phát sinh ở tầng (layer / 계층) nào.

Async MVC thêm một ranh giới (boundary / 경계) khác. Khi controller trả `Callable`, `DeferredResult` hoặc supported async kiểu (type / 타입), servlet yêu cầu (request / 요청) có thể được đưa vào async chế độ (mode / 모드) và processing tiếp tục ở thực thi (execution / 실행) khác trước khi có một async dispatch quay lại hoàn tất phản hồi (response / 응답). ThreadLocal ngữ cảnh (context / 맥락) tự chế có thể mất ở ranh giới (boundary / 경계) này; bảo mật (security / 보안), tracing và yêu cầu (request / 요청) ngữ cảnh (context / 맥락) phải dùng cơ chế propagation đúng. Vì vậy vòng đời yêu cầu (request lifecycle / 요청 생명주기) phải được hiểu theo **dispatches và thực thi (execution / 실행) ngữ cảnh (context / 맥락)**, không chỉ “một yêu cầu (request / 요청) = một luồng thực thi (thread / 스레드) từ đầu tới cuối”.
<!-- SPRING_BATCH2_REQUEST_INTERMEDIATE_END -->

---

# 26. HandlerMapping

`HandlerMapping` trả lời:

```text
Request này map tới handler nào?
```

Annotated controllers thường dùng `RequestMappingHandlerMapping`, nó đọc `@RequestMapping`, `@GetMapping` và ánh xạ (mapping / 매핑) siêu dữ liệu (metadata / 메타데이터).

Nếu hai methods match mơ hồ, lỗi (error / 오류) xảy ra ở ánh xạ (mapping / 매핑) tầng (layer / 계층).

---

# 27. HandlerAdapter

DispatcherServlet không hard-code cách gọi mọi loại handler. `HandlerAdapter` biết cách thực thi handler kiểu cụ thể.

Annotated controller methods được xử lý qua `RequestMappingHandlerAdapter`.

Đây là **Adapter mẫu (pattern / 패턴)** trong khung phần mềm (framework / 프레임워크) kiến trúc (architecture / 아키텍처): DispatcherServlet tương tác uniform dù handler mechanisms khác.

---

# 28. HandlerMethodArgumentResolver

Controller:

```java
UserResponse me(
        @CurrentUser UserId userId)
```

Spring cần biết lấy `UserId` từ đâu. Custom argument resolver có thể đọc authenticated principal/bảo mật (security / 보안) ngữ cảnh (context / 맥락) rồi tạo lĩnh vực (domain / 도메인) `UserId`.

Resolver rất hợp với vận chuyển (transport / 전송)/ngữ cảnh (context / 맥락) concern. Nó không nên gọi 5 databases và implement nghiệp vụ (business / 비즈니스) workflow vì controller signature sẽ che hidden I/O.

---

# 29. ReturnValueHandler

Return kiểu (type / 타입) có thể là DTO, `ResponseEntity`, view mô hình (model / 모델), async kiểu (type / 타입) hoặc các supported abstractions khác. Return-value handling quyết định ngữ nghĩa (semantics / 의미론) sau controller.

Đây là lý do controller phương thức (method / 메서드) return “Java đối tượng (object / 객체)” nhưng phản hồi (response / 응답) lại có status/body JSON đúng.

---

# 30. HttpMessageConverter

Message converter chuyển:

```text
HTTP body
↔
Java object
```

JSON converter dùng Jackson tích hợp (integration / 통합). String/body tài nguyên (resource / 자원)/form-data có converter khác.

`@RequestBody` chỉ nói rằng argument đến từ body. Converter mới thực hiện format conversion.

---

# 31. `Content-Type` và `Accept`

`Content-Type` nói body hiện tại là format gì.

```http
Content-Type: application/json
```

`Accept` nói máy khách (client / 클라이언트) muốn phản hồi (response / 응답) format gì.

```http
Accept: application/json
```

Nếu yêu cầu (request / 요청) gửi format unsupported, máy chủ (server / 서버) có thể trả `415 Unsupported Media Type`. Nếu máy khách (client / 클라이언트) yêu cầu phản hồi (response / 응답) biểu diễn (representation / 표현) máy chủ (server / 서버) không tạo được, có thể `406 Not Acceptable`.

Đây là HTTP ngữ nghĩa (semantics / 의미론) được Spring MVC implement.

---

# 32. Servlet Filter và HandlerInterceptor

Filter ở Servlet mức (level / 수준) và chạy trước DispatcherServlet. Nó có thể wrap yêu cầu (request / 요청)/phản hồi (response / 응답), làm bảo mật (security / 보안) hạ tầng (infrastructure / 인프라), yêu cầu (request / 요청) correlation và low-level web concerns.

Interceptor ở Spring MVC mức (level / 수준) và biết handler ánh xạ (mapping / 매핑)/controller.

Ví dụ yêu cầu (request / 요청) ID tạo ở filter là hợp lý vì mọi yêu cầu (request / 요청) cần ID kể cả trước khi biết controller. Controller-specific kiểm tra (audit / 감사) có thể dùng interceptor.

Không chọn theo “filter cũ, interceptor mới”; chúng ở hai lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층) khác nhau.

---

# 33. OncePerRequestFilter

Spring có `OncePerRequestFilter` làm cơ sở (base / 기반) lớp (class / 클래스) cho nhiều filter custom.

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

Bạn vẫn phải hiểu async/lỗi (error / 오류) dispatch ngữ nghĩa (semantics / 의미론) nếu filter phức tạp.

---

# 34. ConversionService và custom Converter

Đường dẫn (path / 경로) variable là string ở HTTP nhưng có thể map thành lĩnh vực (domain / 도메인) ID.

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

Conversion ở web ranh giới (boundary / 경계) cho phép cốt lõi (core / 핵심) dùng `UserId` thay vì raw `long`.

---

# 35. phương thức (method / 메서드) kiểm tra hợp lệ (validation / 검증)

Bean kiểm tra hợp lệ (validation / 검증) không chỉ áp vào DTO. dịch vụ (service / 서비스) phương thức (method / 메서드) có thể được kiểm tra hợp lệ (validation / 검증) thông qua method-validation hạ tầng (infrastructure / 인프라).

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

Vì đây thường là interceptor/proxy tính năng (feature / 기능), self-invocation/proxy ranh giới (boundary / 경계) lại có ý nghĩa.

Tuy nhiên lĩnh vực (domain / 도메인) invariants phức tạp vẫn nên nằm trong lĩnh vực (domain / 도메인)/ứng dụng (application / 애플리케이션) lô-gic (logic / 논리), không biến kiểm tra hợp lệ (validation / 검증) annotations thành nghiệp vụ (business / 비즈니스) engine.

---

# 36. Custom kiểm tra hợp lệ (validation / 검증) ràng buộc (constraint / 제약조건)

Khi một reusable syntactic/domain-adjacent ràng buộc (constraint / 제약조건) hợp lý, bạn có thể tạo annotation + `ConstraintValidator`.

Ví dụ currency mã (code / 코드):

```java
@ValidCurrency
String currency
```

Validator nên pure/cheap nếu có thể. Validator gọi remote API hoặc DB cho mỗi trường dữ liệu (field / 필드) có thể tạo hidden I/O và hiệu năng (performance / 성능) khó đoán.

Cross-field quy tắc (rule / 규칙) như `start <= end` thường là class-level kiểm tra hợp lệ (validation / 검증) hoặc lĩnh vực (domain / 도메인) bất biến (invariant / 불변식).

---

# 37. ProblemDetail và lỗi (error / 오류) kiến trúc (architecture / 아키텍처)

Ở Intermediate, lỗi (error / 오류) handling cần phân biệt biểu diễn (representation / 표현) lỗi (error / 오류), kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류), lĩnh vực (domain / 도메인) rejection và hạ tầng (infrastructure / 인프라) thất bại (failure / 실패).

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

`ProblemDetail` hoặc lỗi (error / 오류) envelope nên mang stable mã máy (machine code / 기계어), human message và correlation ID khi cần.

Controller advice là web ranh giới (boundary / 경계); lĩnh vực (domain / 도메인) exception không nhất thiết mang HTTP annotation.

---

# 38. giao dịch (transaction / 트랜잭션) hạ tầng (infrastructure / 인프라)

`@Transactional` được giao dịch (transaction / 트랜잭션) interceptor đọc khi phương thức (method / 메서드) lời gọi (call / 호출) đi qua proxy.

Luồng (flow / 흐름) concept:

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

Nếu lời gọi (call / 호출) không đi qua proxy, declarative giao dịch (transaction / 트랜잭션) advice không chạy.

---

<!-- SPRING_BATCH3_TX_INTERMEDIATE -->

> **Chuyển mạch:** Trong **Java Spring — Part 2: Intermediate**, cơ chế trong **Vòng đời yêu cầu (request lifecycle / 요청 생명주기) end-to-end: từ servlet bộ chứa (container / 컨테이너) tới phản hồi (response / 응답) lần ghi nhận (commit / 커밋)** cần được kiểm chứng bằng dấu vết cụ thể; **@Transactional đi từ siêu dữ liệu (metadata / 메타데이터) tới liên kết (connection / 연결) như thế nào?** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **Spring bảo mật (security / 보안) yêu cầu (request / 요청) luồng (flow / 흐름): từ filter matching tới Authentication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `@Transactional` đi từ siêu dữ liệu (metadata / 메타데이터) tới liên kết (connection / 연결) như thế nào?

`@Transactional` được đọc thành `TransactionAttribute`. Khi lời gọi (call / 호출) đi qua transactional proxy, `TransactionInterceptor` đi vào dùng chung (common / 공통) giao dịch (transaction / 트랜잭션) lô-gic (logic / 논리) của `TransactionAspectSupport`: resolve giao dịch (transaction / 트랜잭션) attribute, chọn `TransactionManager`, hỏi manager xem có giao dịch (transaction / 트랜잭션) hiện tại không rồi tạo `TransactionStatus`. Với JDBC, `DataSourceTransactionManager` lấy liên kết (connection / 연결) từ DataSource, configure auto-commit/isolation/read-only theo chính sách (policy / 정책) và bind tài nguyên (resource / 자원) holder với hiện tại (current / 현재) thực thi (execution / 실행) ngữ cảnh (context / 맥락). Repository mã (code / 코드) dùng Spring-aware liên kết (connection / 연결) truy cập (access / 접근) có thể vì vậy nhận đúng liên kết (connection / 연결) đang thuộc giao dịch (transaction / 트랜잭션) hiện tại thay vì tạo liên kết (connection / 연결) độc lập.

`TransactionSynchronizationManager` giữ tài nguyên (resource / 자원) bindings và synchronization callbacks cho imperative giao dịch (transaction / 트랜잭션). Nó giải thích tại sao hai repository methods trên cùng luồng thực thi (thread / 스레드) có thể cùng dùng một giao dịch (transaction / 트랜잭션) mà không truyền liên kết (connection / 연결) qua mọi phương thức (method / 메서드) signature. Nó cũng giải thích tại sao `new Thread(...)` hoặc arbitrary executor không tự mang giao dịch (transaction / 트랜잭션) đi theo: luồng thực thi (thread / 스레드) mới không có tài nguyên (resource / 자원) binding cũ.

Khi mục tiêu (target / 대상) phương thức (method / 메서드) return, interceptor không tự “lần ghi nhận (commit / 커밋) cơ sở dữ liệu (database / 데이터베이스)” trực tiếp. giao dịch (transaction / 트랜잭션) manager quyết định lần ghi nhận (commit / 커밋) hay quay lui (rollback / 롤백) dựa `TransactionStatus`, rollback-only flag và exception quy tắc (rule / 규칙). Cleanup sau đó unbind tài nguyên (resource / 자원), restore trạng thái (state / 상태) và bản phát hành (release / 릴리스) liên kết (connection / 연결) về pool. Nếu mã (code / 코드) giữ giao dịch (transaction / 트랜잭션) quá lâu, bạn đang giữ scarce liên kết (connection / 연결)/locks quá lâu; annotation không làm tài nguyên (resource / 자원) chi phí (cost / 비용) biến mất.
<!-- SPRING_BATCH3_TX_INTERMEDIATE_END -->

---

# 39. PlatformTransactionManager

Spring cung cấp giao dịch (transaction / 트랜잭션) lớp trừu tượng (abstraction / 추상화). Với JDBC có manager kiểu DataSource-based. Với JPA có JPA giao dịch (transaction / 트랜잭션) manager. ứng dụng (application / 애플리케이션) dùng dùng chung (common / 공통) `@Transactional`, còn manager hiện thực (implementation / 구현) biết cách điều khiển tài nguyên (resource / 자원).

Điều này cho phép giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) tương đối thống nhất ở Spring tầng (layer / 계층), nhưng cơ sở dữ liệu (database / 데이터베이스) hành vi (behavior / 동작) vẫn phụ thuộc DB/JPA provider.

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

nếu proxy lời gọi (call / 호출) đúng, thường cùng vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션).

---

# 41. Logical và vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션)

Mỗi `@Transactional` phương thức (method / 메서드) có logical giao dịch (transaction / 트랜잭션) phạm vi (scope / 범위), nhưng nhiều REQUIRED scopes có thể dùng cùng vật lý (physical / 물리적) DB giao dịch (transaction / 트랜잭션).

Điều này giải thích rollback-only.

Inner phương thức (method / 메서드) thất bại (fail / 실패) và giao dịch (transaction / 트랜잭션) bị đánh dấu rollback-only. Outer catch exception rồi cố return success. Khi lần ghi nhận (commit / 커밋), khung phần mềm (framework / 프레임워크) phát hiện vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션) phải quay lui (rollback / 롤백) và có thể ném `UnexpectedRollbackException`.

Đây là hành vi (behavior / 동작) bảo vệ caller khỏi tưởng rằng lần ghi nhận (commit / 커밋) thành công.

---

# 42. REQUIRES_NEW

`REQUIRES_NEW` suspend outer giao dịch (transaction / 트랜잭션) và tạo vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션) riêng.

```java
@Transactional(
    propagation =
        Propagation.REQUIRES_NEW
)
```

Use trường hợp (case / 사례) có thể là kiểm tra (audit / 감사) độc lập, nhưng phải cẩn thận tài nguyên (resource / 자원).

Nếu outer giữ liên kết (connection / 연결) và inner cần thêm liên kết (connection / 연결), mỗi luồng thực thi (thread / 스레드) có thể giữ 2 connections. Pool nhỏ có thể cạn.

Không dùng `REQUIRES_NEW` như “force save”.

---

# 43. NESTED

`NESTED` thường dựa trên savepoint ngữ nghĩa (semantics / 의미론) khi giao dịch (transaction / 트랜잭션) manager/tài nguyên (resource / 자원) hỗ trợ.

Nó không giống REQUIRES_NEW. Nested có thể quay lui (rollback / 롤백) phần trong về savepoint mà outer giao dịch (transaction / 트랜잭션) tiếp tục, nhưng vẫn thuộc vật lý (physical / 물리적) giao dịch (transaction / 트랜잭션) lớn.

Hỗ trợ (support / 지원) thực tế cần kiểm tra giao dịch (transaction / 트랜잭션) manager/cơ sở dữ liệu (database / 데이터베이스).

---

# 44. Các propagation còn lại

`SUPPORTS` tham gia giao dịch (transaction / 트랜잭션) nếu có, không có thì chạy non-transactional. `MANDATORY` yêu cầu giao dịch (transaction / 트랜잭션) phải tồn tại. `NOT_SUPPORTED` suspend giao dịch (transaction / 트랜잭션) hiện tại rồi chạy non-transactional. `NEVER` yêu cầu không được có giao dịch (transaction / 트랜잭션).

Bạn không cần dùng thường xuyên, nhưng phải biết chúng biểu diễn **chính sách (policy / 정책) về ngữ cảnh (context / 맥락) hiện tại**, không chỉ “mức (level / 수준)” giao dịch (transaction / 트랜잭션).

---

# 45. Isolation

Spring expose isolation options tương ứng relational giao dịch (transaction / 트랜잭션) concepts như READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE.

Nhưng tên giống nhau không có nghĩa mọi cơ sở dữ liệu (database / 데이터베이스) implement chi tiết giống nhau. PostgreSQL, MySQL/InnoDB, Oracle có MVCC/locking ngữ nghĩa (semantics / 의미론) khác.

Học Spring isolation mà không học cơ sở dữ liệu (database / 데이터베이스) isolation là thiếu một nửa.

---

# 46. `readOnly=true`

Phần này nối khái niệm backend với một ví dụ hoặc quy trình có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu code với contract và failure mode của hệ thống.

```java
@Transactional(readOnly = true)
```

là hint/chính sách (policy / 정책) được giao dịch (transaction / 트랜잭션) manager/provider dùng. Với JPA nó có thể ảnh hưởng flush hành vi (behavior / 동작); với DB/driver có thể set read-only hints.

Nó không phải universal “ghi (write / 쓰기) blocker” và không nên được xem như bảo mật (security / 보안) cơ chế (mechanism / 메커니즘).

---

# 47. quay lui (rollback / 롤백) Rules

Spring declarative giao dịch (transaction / 트랜잭션) mặc định quay lui (rollback / 롤백) trên unchecked `RuntimeException`/`Error`; checked exceptions không tự động quay lui (rollback / 롤백) theo default quy tắc (rule / 규칙) trừ khi cấu hình.

```java
@Transactional(
    rollbackFor = IOException.class
)
```

có thể override.

Đừng cấu hình `rollbackFor = Exception.class` khắp nơi nếu chưa thiết kế exception taxonomy.

---

# 48. TransactionTemplate

Nếu chỉ một phần phương thức (method / 메서드) cần giao dịch (transaction / 트랜잭션) hoặc bạn muốn chuỗi (sequence / 시퀀스) rõ:

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

Programmatic giao dịch (transaction / 트랜잭션) làm ranh giới (boundary / 경계) tường minh (explicit / 명시적) và tránh một số proxy/self-invocation bài toán (problem / 문제).

---

# 49. JDBC Exception Translation

Spring JDBC chuyển nhiều `SQLException` vendor-specific thành `DataAccessException` hierarchy.

Lợi ích là dịch vụ (service / 서비스) không phụ thuộc trực tiếp lỗi (error / 오류) mã (code / 코드) từng DB.

Tuy nhiên môi trường vận hành (production / 운영 환경) debugging vẫn cần nguyên nhân gốc (root cause / 근본 원인) SQL trạng thái (state / 상태)/vendor exception.

Exception translation không có nghĩa cơ sở dữ liệu (database / 데이터베이스) differences biến mất.

---

# 50. JdbcClient, JdbcTemplate và NamedParameterJdbcTemplate

`JdbcTemplate` là API lâu đời, rõ và mạnh. `NamedParameterJdbcTemplate` thêm named params. `JdbcClient` cung cấp fluent façade hiện đại cho dùng chung (common / 공통) JDBC operations.

Không có một winner tuyệt đối. Chọn theo codebase/phiên bản (version / 버전)/use trường hợp (case / 사례). Điều cốt lõi vẫn là SQL, ánh xạ (mapping / 매핑), giao dịch (transaction / 트랜잭션) và liên kết (connection / 연결) management.

---

# 51. JPA thực thể (entity / 엔터티) vòng đời (lifecycle / 생명주기)

Một thực thể (entity / 엔터티) có thể ở trạng thái transient, managed, detached hoặc removed.

Transient:

```java
new UserEntity(...)
```

chưa thuộc persistence ngữ cảnh (context / 맥락).

Managed là thực thể (entity / 엔터티) được persistence ngữ cảnh (context / 맥락) nhánh học (track / 트랙). Khi managed trạng thái (state / 상태) đổi trong giao dịch (transaction / 트랜잭션), dirty checking có thể generate cập nhật (update / 업데이트).

Detached là thực thể (entity / 엔터티) từng managed nhưng ngữ cảnh (context / 맥락) không còn quản lý. Thay đổi detached đối tượng (object / 객체) không tự động persist.

Removed là thực thể (entity / 엔터티) được schedule xóa.

---

# 52. Persistence ngữ cảnh (context / 맥락)

Persistence ngữ cảnh (context / 맥락) không chỉ “bộ nhớ đệm (cache / 캐시)”.

Nó là đơn vị (unit / 단위) quản lý định danh (identity / 식별자) và trạng thái (state / 상태) của entities.

Nếu tải (load / 로드) cùng thực thể (entity / 엔터티) ID trong một ngữ cảnh (context / 맥락), provider thường duy trì cùng đối tượng (object / 객체) định danh (identity / 식별자).

```text
find User#1
→ managed instance A

find User#1 again
→ same managed identity
```

Điều này hỗ trợ dirty checking và relationship consistency.

---

# 53. Dirty Checking

Mục này biến kiến thức backend thành tiêu chí kiểm tra và quyết định triển khai. Hãy xác định contract, failure mode, evidence và cách rollback trước khi áp dụng.

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

Nếu thực thể (entity / 엔터티) managed, provider so sánh/tracking trạng thái (state / 상태) và phát SQL cập nhật (update / 업데이트) khi flush.

Bạn có thể không cần gọi `save()` cho managed thực thể (entity / 엔터티).

Việc hiểu này rất quan trọng vì nhiều tutorial gọi `save()` vô điều kiện làm bạn không thấy unit-of-work mô hình (model / 모델) của JPA.

---

# 54. Flush khác lần ghi nhận (commit / 커밋)

Flush đẩy pending ORM changes thành SQL/DB tương tác (interaction / 상호작용) để đồng bộ persistence ngữ cảnh (context / 맥락) với cơ sở dữ liệu (database / 데이터베이스) trạng thái (state / 상태) cần thiết.

Lần ghi nhận (commit / 커밋) hoàn tất giao dịch (transaction / 트랜잭션).

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

Relationship lazy không tải (load / 로드) ngay.

```java
order.getItems()
```

có thể trigger SQL khi truy cập (access / 접근) nếu persistence ngữ cảnh (context / 맥락) còn hoạt động.

Nếu ngữ cảnh (context / 맥락) đóng:

```text
entity detached
→ access lazy relation
→ LazyInitializationException
```

Đừng fix bằng `EAGER` toàn bộ. EAGER có thể over-fetch và tạo truy vấn (query / 쿼리) explosion theo hướng khác.

---

# 56. N+1 bài toán (problem / 문제)

Truy vấn (query / 쿼리) 100 orders:

```sql
select ... from orders
```

Sau đó từng thứ tự (order / 순서) tải (load / 로드) items:

```sql
select ... from order_items where order_id=?
```

Kết quả (result / 결과):

```text
1 query orders
+
100 queries items
```

N+1 là hiệu năng (performance / 성능) bài toán (problem / 문제) do truy cập (access / 접근) mẫu (pattern / 패턴) và fetch plan.

Fix có thể là fetch phép nối (join / 조인), thực thể (entity / 엔터티) đồ thị (graph / 그래프), projection, batch fetching hoặc truy vấn (query / 쿼리) redesign tùy trường hợp (case / 사례).

---

# 57. Fetch phép nối (join / 조인)

JPQL:

```jpql
select distinct o
from Order o
join fetch o.items
where o.id = :id
```

có thể tải (load / 로드) association trong truy vấn (query / 쿼리).

Nhưng fetch phép nối (join / 조인) collection + pagination hoặc nhiều collections có thể tạo Cartesian multiplication. cấp cao (senior / 시니어) sẽ đi sâu.

---

# 58. EntityGraph

Thực thể (entity / 엔터티) đồ thị (graph / 그래프) mô tả fetch plan tách khỏi static thực thể (entity / 엔터티) ánh xạ (mapping / 매핑).

Ý tưởng tốt là quan hệ (relation / 관계) ánh xạ (mapping / 매핑) nói default ngữ nghĩa (semantics / 의미론), còn use trường hợp (case / 사례) quyết định cần đồ thị (graph / 그래프) nào.

Không phải mọi API lời gọi (call / 호출) cần cùng đồ thị (graph / 그래프).

---

# 59. Projection

Read-only API không nhất thiết tải (load / 로드) full thực thể (entity / 엔터티).

```java
public record UserSummary(
    Long id,
    String name) {
}
```

Truy vấn (query / 쿼리) projection có thể chỉ lấy cột cần thiết.

Đây là bước đầu của CQRS-lite: ghi (write / 쓰기) side dùng thực thể (entity / 엔터티)/lĩnh vực (domain / 도메인) mô hình (model / 모델), read side có optimized truy vấn (query / 쿼리) DTO.

---

# 60. Page, Slice và Sort

`Page` thường cung cấp total elements/total pages, nên có thể cần count truy vấn (query / 쿼리).

`Slice` chủ yếu biết có trang tiếp theo không, có thể tránh full total count.

Nếu UI không cần total, `Slice` có thể rẻ hơn.

Pagination cũng phải có thứ tự (ordering / 순서) ổn định. Deep offset có hiệu năng (performance / 성능) issues; cấp cao (senior / 시니어) sẽ học keyset/cursor pagination.

---

# 61. Optimistic Locking

Thực thể (entity / 엔터티):

```java
@Version
private long version;
```

Hai transactions đọc phiên bản (version / 버전) 1. A cập nhật (update / 업데이트) thành phiên bản (version / 버전) 2. B cập nhật (update / 업데이트) với expected phiên bản (version / 버전) 1 và thất bại (fail / 실패) optimistic locking.

Điều này tránh silent lost cập nhật (update / 업데이트) mà không giữ row khóa (lock / 잠금) suốt thời gian người dùng (user / 사용자)/nghiệp vụ (business / 비즈니스) processing.

Xung đột (conflict / 충돌) phải được xử lý theo nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론): thử lại (retry / 재시도), reject hoặc yêu cầu người dùng (user / 사용자) refresh.

---

# 62. Pessimistic Locking

Pessimistic khóa (lock / 잠금) yêu cầu DB khóa (lock / 잠금) row/tài nguyên (resource / 자원).

Hợp khi xung đột (conflict / 충돌) chi phí (cost / 비용) cao và contention mẫu (pattern / 패턴) justify.

Nhưng khóa (lock / 잠금) làm transactions chờ nhau và có thể deadlock. giao dịch (transaction / 트랜잭션) phải ngắn và khóa (lock / 잠금) thứ tự (ordering / 순서) nhất quán.

Không dùng pessimistic khóa (lock / 잠금) như default “cho chắc”.

---

# 63. Flyway và Liquibase trong luồng (flow / 흐름) delivery

Di chuyển (migration / 마이그레이션) phải chạy theo chuỗi (sequence / 시퀀스) được version-control.

Nếu `V5` đã chạy môi trường vận hành (production / 운영 환경), không sửa tệp (file / 파일) đó để “clean lịch sử (history / 이력)”. Tạo `V6`.

Di chuyển (migration / 마이그레이션) rà soát (review / 검토) phải xem khóa (lock / 잠금)/thời gian (time / 시간) impact. `ALTER TABLE` lớn có thể gây downtime tùy DB/phiên bản (version / 버전).

Lược đồ (schema / 스키마) evolution là môi trường vận hành (production / 운영 환경) concern, không chỉ cục bộ (local / 로컬) startup concern.

---

# 64. RestClient cấu hình đúng

Máy khách (client / 클라이언트) nên là bean:

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

Nghiệp vụ (business / 비즈니스) dịch vụ (service / 서비스) không nên tự bản dựng (build / 빌드) máy khách (client / 클라이언트) mỗi phương thức (method / 메서드).

Central cấu hình (configuration / 구성) giúp headers, hết thời gian chờ (timeout / 타임아웃), serialization, khả năng quan sát (observability / 관측 가능성) và cơ sở (base / 기반) URL thống nhất.

---

# 65. HTTP dịch vụ (service / 서비스) máy khách (client / 클라이언트)

Spring cho phép declarative giao diện (interface / 인터페이스):

```java
public interface UserApi {

    @GetExchange("/users/{id}")
    UserResponse get(
        @PathVariable long id);
}
```

Khung phần mềm (framework / 프레임워크) tạo proxy triển khai giao diện (interface / 인터페이스) và gửi HTTP.

Mô hình tư duy (mental model / 사고 모델) rất giống Spring dữ liệu (data / 데이터) repository:

```text
interface contract
→ framework proxy
→ transport implementation
```

Lĩnh vực (domain / 도메인) vẫn nên phụ thuộc gateway lớp trừu tượng (abstraction / 추상화) nếu bên ngoài (external / 외부) API shape không phải lĩnh vực (domain / 도메인) đặc tả hợp đồng (contract / 계약).

---

# 66. RestTemplate và WebClient

`RestTemplate` xuất hiện rất nhiều trong legacy Spring. Bạn phải đọc được.

`RestClient` là synchronous fluent API hiện đại.

`WebClient` là reactive máy khách (client / 클라이언트) với `Mono/Flux` và non-blocking mô hình thực thi (execution model / 실행 모델).

Đừng chọn WebClient chỉ vì “nhanh hơn”. Nếu ứng dụng (application / 애플리케이션) blocking/JPA và bạn lời gọi (call / 호출) `.block()` mọi nơi, bạn đang trộn các mô hình (models / 모델들) mà không nhận lợi ích rõ.

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

Default ứng dụng (application / 애플리케이션) sự kiện (event / 이벤트) không phải durable phân tán (distributed / 분산) message. Nó sống trong tiến trình (process / 프로세스).

Nếu listener throw, hành vi (behavior / 동작) phụ thuộc synchronous/asynchronous sự kiện (event / 이벤트) hạ tầng (infrastructure / 인프라).

---

# 68. TransactionalEventListener

Bạn có thể bind listener vào giao dịch (transaction / 트랜잭션) phase như after lần ghi nhận (commit / 커밋).

Ví dụ gửi follow-up only after DB lần ghi nhận (commit / 커밋).

Nhưng crash:

```text
DB committed
→ process crashes
→ in-memory after-commit listener not completed
```

Sự kiện (event / 이벤트) có thể mất.

Nếu nghiệp vụ (business / 비즈니스) requires durable delivery, cần Outbox/broker mẫu (pattern / 패턴) ở cấp cao (senior / 시니어).

---

# 69. `@Async`

`@Async` dùng proxy/interceptor để submit phương thức (method / 메서드) thực thi (execution / 실행) vào executor.

Điều này thay:

```text
thread
transaction context
exception flow
security context
trace context
```

`void` async phương thức (method / 메서드) có exception không thể return cho original caller theo normal ngăn xếp lời gọi (call stack / 호출 스택).

Nếu caller cần kết quả (result / 결과)/thất bại (failure / 실패), `CompletableFuture` hoặc durable workflow phù hợp hơn tùy yêu cầu (requirement / 요구사항).

---

# 70. Async Executor

Bạn phải biết executor nào thực thi tác vụ (task / 작업). Với platform-thread pool, quan tâm cốt lõi (core / 핵심)/max/hàng đợi (queue / 큐)/rejection/shutdown.

Một unbounded hàng đợi (queue / 큐) có thể giữ hàng triệu tasks khi producer nhanh hơn bên tiêu thụ (consumer / 소비자).

Async không loại overload; nó chỉ chuyển overload sang hàng đợi (queue / 큐) nếu không có sức chứa (capacity / 용량) chính sách (policy / 정책).

---

# 71. Virtual Threads trong Spring Boot

Với Java 21+, Boot có thể bật virtual-thread hỗ trợ (support / 지원):

```yaml
spring:
  threads:
    virtual:
      enabled: true
```

Virtual threads làm imperative blocking style quy mô (scale / 규모) tính đồng thời (concurrency / 동시성) tốt hơn ở nhiều I/O workloads.

Nhưng DB liên kết (connection / 연결) pool vẫn giới hạn cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성). Nếu 100.000 virtual threads cùng cần DB và pool có 30 connections, 99.970 threads có thể chờ. Điều đó có thể đúng vì DB không chịu 100k concurrent queries.

Virtual luồng thực thi (thread / 스레드) không thay sức chứa (capacity / 용량) management.

---

# 72. `@Scheduled`

`fixedDelay` tính delay sau lần thực thi (execution / 실행) trước hoàn tất. `fixedRate` mục tiêu (target / 대상) cadence dựa trên schedule intervals.

Cron expressions cho scheduling linh hoạt.

Trong cluster 3 replicas, mỗi instance có scheduler riêng. Nếu job phải chạy đúng một lần toàn cluster, cần phân tán (distributed / 분산) khóa (lock / 잠금) hoặc bên ngoài (external / 외부) job scheduler.

---

# 73. Spring bộ nhớ đệm (cache / 캐시)

`@Cacheable`:

```java
@Cacheable(
    cacheNames = "users",
    key = "#id"
)
public User get(long id) {
}
```

Bộ nhớ đệm (cache / 캐시) hit có thể skip phương thức (method / 메서드).

`@CachePut` execute phương thức (method / 메서드) rồi cập nhật (update / 업데이트) bộ nhớ đệm (cache / 캐시). `@CacheEvict` xoá entry.

Nhưng annotation không trả lời TTL, max kích thước (size / 크기), phân tán (distributed / 분산) consistency, serialization, stampede hoặc eviction chính sách (policy / 정책).

---

# 74. bộ nhớ đệm (cache / 캐시) Self-invocation

Caching cũng thường proxy-based.

```java
this.getUser(id);
```

có thể bypass bộ nhớ đệm (cache / 캐시) advice giống giao dịch (transaction / 트랜잭션).

Đây là lý do hiểu proxy một lần giúp hiểu nhiều Spring annotations.

---

# 75. bộ nhớ đệm (cache / 캐시) key ngữ nghĩa (semantics / 의미론)

Bộ nhớ đệm (cache / 캐시) key phải chứa các đầu vào (input / 입력) quyết định đầu ra (output / 출력).

Nếu kết quả (result / 결과) phụ thuộc:

```text
userId
tenant
locale
permission level
```

nhưng key chỉ là `userId`, bộ nhớ đệm (cache / 캐시) có thể trả sai dữ liệu.

Caching là tính đúng đắn (correctness / 정확성) hệ thống (system / 시스템), không chỉ hiệu năng (performance / 성능) công cụ (tool / 도구).

---

# 76. Spring bảo mật (security / 보안) kiến trúc (architecture / 아키텍처) ở Intermediate

Servlet bảo mật (security / 보안) thường có luồng (flow / 흐름):

```text
Servlet Filter Chain
→ DelegatingFilterProxy
→ FilterChainProxy
→ SecurityFilterChain
→ authentication filters
→ authorization
→ DispatcherServlet
```

Spring bảo mật (security / 보안) nằm trước controller phần lớn thời gian.

Nếu yêu cầu (request / 요청) không vào controller, lỗi có thể nằm trong bảo mật (security / 보안) chuỗi (chain / 사슬) chứ không phải ánh xạ (mapping / 매핑).

---

<!-- SPRING_BATCH4_SECURITY_INTERMEDIATE -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 2: Intermediate**, **@Transactional đi từ siêu dữ liệu (metadata / 메타데이터) tới liên kết (connection / 연결) như thế nào?** nêu điều cần giải thích; **Spring bảo mật (security / 보안) yêu cầu (request / 요청) luồng (flow / 흐름): từ filter matching tới Authentication** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Chọn kiểm thử (test / 테스트) theo ranh giới (boundary / 경계) thay vì chọn annotation theo thói quen** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spring bảo mật (security / 보안) yêu cầu (request / 요청) luồng (flow / 흐름): từ filter matching tới `Authentication`

Servlet bộ chứa (container / 컨테이너) nhìn Spring bảo mật (security / 보안) như một filter. `DelegatingFilterProxy` cầu nối (bridge / 브리지) bộ chứa (container / 컨테이너) vòng đời (lifecycle / 생명주기) với bean `FilterChainProxy`. `FilterChainProxy` giữ nhiều `SecurityFilterChain`; mỗi chuỗi (chain / 사슬) có yêu cầu (request / 요청) matcher và ordered filters. Với một yêu cầu (request / 요청), chuỗi (chain / 사슬) phù hợp được chọn, vì vậy multiple-chain cấu hình (configuration / 구성) thực chất là **routing bảo mật (security / 보안) chính sách (policy / 정책) trước MVC routing**.

Một authentication filter đọc credential phù hợp giao thức (protocol / 프로토콜), tạo một `Authentication` chưa authenticated rồi giao cho `AuthenticationManager`. dùng chung (common / 공통) `ProviderManager` thử các `AuthenticationProvider` hỗ trợ loại đơn vị từ (token / 토큰) đó. Password provider có thể dùng `UserDetailsService` + `PasswordEncoder`; tài nguyên (resource / 자원) máy chủ (server / 서버) JWT dùng provider/decoder khác. Khi thành công, authenticated `Authentication` được đặt vào SecurityContext theo configured chiến lược (strategy / 전략)/repository để phần còn lại của yêu cầu (request / 요청) thấy principal/authorities.

Authorization xảy ra sau khi authentication ngữ cảnh (context / 맥락) tồn tại. yêu cầu (request / 요청) authorization dùng authorization manager/filter hạ tầng (infrastructure / 인프라); phương thức (method / 메서드) bảo mật (security / 보안) lại là method-interceptor/proxy tầng (layer / 계층), nghĩa là cùng một yêu cầu (request / 요청) có thể vượt HTTP quy tắc (rule / 규칙) nhưng bị chặn ở use-case phương thức (method / 메서드) vì object-level chính sách (policy / 정책). Đó là defense in độ sâu (depth / 깊이) khi ranh giới (boundary / 경계) được chọn có chủ đích, không phải lý do bản sao (copy / 복사) cùng role expression ở mọi tầng (layer / 계층).

Authentication thất bại (failure / 실패) và truy cập (access / 접근) denied cũng có hai ngữ nghĩa (semantics / 의미론) khác nhau. Unauthenticated caller cần `AuthenticationEntryPoint`; authenticated caller thiếu quyền đi `AccessDeniedHandler`. Trộn cả hai thành HTTP 401 hoặc 403 tùy tiện làm máy khách (client / 클라이언트) hành vi (behavior / 동작) và sự cố (incident / 인시던트) diagnosis sai.
<!-- SPRING_BATCH4_SECURITY_INTERMEDIATE_END -->

---

# 77. Authentication và SecurityContext

Sau authentication thành công, Spring bảo mật (security / 보안) có `Authentication` chứa principal/authorities và được đặt trong bảo mật (security / 보안) ngữ cảnh (context / 맥락) theo configured chiến lược (strategy / 전략).

Controller/dịch vụ (service / 서비스) có thể đọc authenticated principal qua higher-level APIs.

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

Có thể cần lĩnh vực (domain / 도메인) authorization dịch vụ (service / 서비스), không chỉ string expressions.

Phương thức (method / 메서드) bảo mật (security / 보안) đưa chính sách (policy / 정책) gần use-case ranh giới (boundary / 경계) nhưng cũng là proxy tính năng (feature / 기능).

---

# 79. CSRF và CORS ở mức (level / 수준) đúng

CORS là trình duyệt (browser / 브라우저) cross-origin chính sách (policy / 정책). Nó không xác minh người dùng (user / 사용자).

CSRF là attack liên quan trình duyệt (browser / 브라우저) tự gửi credentials như cookies/session sang mục tiêu (target / 대상) site. Stateless bearer-token API có threat mô hình (model / 모델) khác.

Đừng bản sao (copy / 복사):

```java
csrf.disable();
cors.allowAll();
```

chỉ để Postman/trình duyệt (browser / 브라우저) chạy.

---

# 80. Testing Slices

Spring Boot kiểm thử (test / 테스트) slices tải (load / 로드) phần ngữ cảnh (context / 맥락) cần thiết.

`@WebMvcTest` tập trung MVC.

`@DataJpaTest` tập trung JPA.

`@JdbcTest` tập trung JDBC.

`@JsonTest` tập trung JSON.

`@RestClientTest` hỗ trợ máy khách (client / 클라이언트) tầng (layer / 계층) tùy generation/mô-đun (module / 모듈).

Chọn slice giúp kiểm thử (test / 테스트) nhanh và thất bại (failure / 실패) localized.

---

<!-- SPRING_BATCH4_TEST_INTERMEDIATE -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Java Spring — Part 2: Intermediate**, **Spring bảo mật (security / 보안) yêu cầu (request / 요청) luồng (flow / 흐름): từ filter matching tới Authentication** đã nêu tiêu chí phân biệt, còn **Chọn kiểm thử (test / 테스트) theo ranh giới (boundary / 경계) thay vì chọn annotation theo thói quen** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인): thao tác (operation / 연산) → Observation → metrics/traces, còn log là bằng chứng (evidence / 증거) khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chọn kiểm thử (test / 테스트) theo ranh giới (boundary / 경계) thay vì chọn annotation theo thói quen

Plain đơn vị (unit / 단위) kiểm thử (test / 테스트) tạo đối tượng (object / 객체) bằng constructor và kiểm thử (test / 테스트) nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) nhanh nhất vì không cần Spring ngữ cảnh (context / 맥락). MVC slice kiểm thử (test / 테스트) hỏi ánh xạ (mapping / 매핑), kiểm tra hợp lệ (validation / 검증), serialization và controller advice có đúng không. dữ liệu (data / 데이터) slice kiểm thử (test / 테스트) hỏi ánh xạ (mapping / 매핑)/truy vấn (query / 쿼리)/giao dịch (transaction / 트랜잭션) với persistence hạ tầng (infrastructure / 인프라). Full `@SpringBootTest` hỏi đối tượng (object / 객체) đồ thị (graph / 그래프) và tích hợp (integration / 통합) giữa nhiều subsystem có khởi động/hoạt động cùng nhau không. End-to-end với real cổng (port / 포트) chỉ cần ở những luồng (flow / 흐름) mà mạng (network / 네트워크)/máy chủ (server / 서버) hành vi (behavior / 동작) thật mang thêm confidence.

`@SpringBootTest` mặc định không đồng nghĩa “trình duyệt (browser / 브라우저) gọi máy chủ (server / 서버) thật”; web môi trường (environment / 환경) quyết định mock servlet ngữ cảnh (context / 맥락) hay embedded máy chủ (server / 서버) với cổng (port / 포트). `MockMvc` chạy MVC hạ tầng (infrastructure / 인프라) không cần mạng (network / 네트워크) socket, rất phù hợp controller/filter tích hợp (integration / 통합). `RANDOM_PORT` phù hợp khi bạn cần HTTP máy khách (client / 클라이언트)/máy chủ (server / 서버) ngăn xếp (stack / 스택) thật hơn.

`@MockitoBean` thay một Spring bean trong kiểm thử (test / 테스트) ngữ cảnh (context / 맥락), khác với Mockito `@Mock` chỉ tạo đối tượng (object / 객체) mock trong kiểm thử (test / 테스트) lớp (class / 클래스). Bean override thay cấu hình ngữ cảnh (context / 맥락) và có thể ảnh hưởng TestContext bộ nhớ đệm (cache / 캐시) key; hàng trăm kiểm thử (test / 테스트) classes mỗi lớp (class / 클래스) override beans/properties khác nhau có thể tạo hàng trăm contexts. Khi suite chậm, đo ngữ cảnh (context / 맥락) reuse trước khi chỉ tăng parallelism.

Transactional kiểm thử (test / 테스트) auto-rollback rất tiện nhưng có blind spot: commit-time ràng buộc (constraint / 제약조건), `afterCommit` callback, outbox publisher và lazy-loading sau giao dịch (transaction / 트랜잭션) có thể không được exercise giống môi trường vận hành (production / 운영 환경). Hãy có tests tường minh (explicit / 명시적) lần ghi nhận (commit / 커밋) hoặc non-transactional yêu cầu (request / 요청) ranh giới (boundary / 경계) cho những hành vi (behavior / 동작) này.
<!-- SPRING_BATCH4_TEST_INTERMEDIATE_END -->

---

# 81. `@MockitoBean`

Spring kiểm thử (test / 테스트) hiện đại có bean override hỗ trợ (support / 지원) như `@MockitoBean`.

```java
@WebMvcTest(UserController.class)
class UserControllerTest {

    @MockitoBean
    UserService userService;
}
```

Nhiều tutorial cũ dùng `@MockBean`. Khi học Boot 4/khung phần mềm (framework / 프레임워크) 7, ưu tiên hiện tại (current / 현재) Spring kiểm thử (test / 테스트) API và chỉ nhận biết legacy cú pháp (syntax / 문법).

---

# 82. kiểm thử (test / 테스트) ngữ cảnh (context / 맥락) Caching

Spring kiểm thử (test / 테스트) bộ nhớ đệm (cache / 캐시) ApplicationContext tương thích giữa tests.

Nếu mỗi kiểm thử (test / 테스트) lớp (class / 클래스) có profile/properties/mock setup khác, contexts khác nhau và startup lặp lại.

`@DirtiesContext` ép ngữ cảnh (context / 맥락) không reuse và rất đắt nếu lạm dụng.

Bộ kiểm thử (test suite / 테스트 스위트) hiệu năng (performance / 성능) cũng là kiến trúc (architecture / 아키텍처) phản hồi (feedback / 피드백).

---

# 83. Testcontainers

H2 không phải PostgreSQL/Oracle/MySQL.

Nếu truy vấn (query / 쿼리) dùng DB-specific tính năng (feature / 기능), locking, JSON operators hoặc dialect, in-memory fake DB có thể cho confidence sai.

Testcontainers cho phép chạy actual DB engine trong kiểm thử (test / 테스트).

```text
real PostgreSQL
→ Flyway migrations
→ repository test
```

Điều này rất giá trị cho dữ liệu (data / 데이터) tầng (layer / 계층).

---

# 84. `@DynamicPropertySource`

Bộ chứa (container / 컨테이너) có động (dynamic / 동적) cổng (port / 포트)/URL. kiểm thử (test / 테스트) cần inject thuộc tính (property / 속성):

```java
@DynamicPropertySource
static void configure(
        DynamicPropertyRegistry registry) {

    registry.add(
        "spring.datasource.url",
        postgres::getJdbcUrl);
}
```

Boot còn có tích hợp (integration / 통합) tiện hơn tùy hiện tại (current / 현재) modules/phiên bản (version / 버전), nhưng mô hình tư duy (mental model / 사고 모델) là thời gian chạy (runtime / 런타임) tài nguyên (resource / 자원) tạo cấu hình (config / 설정) động.

---

# 85. Actuator sâu hơn

Actuator có thể expose health, metrics, mappings, conditions, cấu hình (config / 설정) properties, môi trường (environment / 환경), luồng thực thi (thread / 스레드) dump, vùng nhớ động (heap / 힙) dump và nhiều thời gian chạy (runtime / 런타임) info.

Các endpoint nhạy cảm không được công khai (public / 공개) mặc định tùy cấu hình (config / 설정), và bạn không nên mở tất cả.

Trong sự cố (incident / 인시던트), `/actuator/conditions`/mappings/metrics có thể rất hữu ích.

---

<!-- SPRING_BATCH5_OBS_INTERMEDIATE -->

> **Chuyển mạch:** Khi boundary test đã xác định phần nào cần container thật, observability pipeline cho biết cùng thao tác đó được chứng minh bằng Observation, metrics, traces hay log. Handoff này nối test evidence với chẩn đoán runtime.

## Khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인): thao tác (operation / 연산) → Observation → metrics/traces, còn log là bằng chứng (evidence / 증거) khác

Micrometer Observation mô hình (model / 모델) bắt đầu từ một thao tác (operation / 연산) có vòng đời (lifecycle / 생명주기) start/stop/lỗi (error / 오류) và ngữ cảnh (context / 맥락). `ObservationRegistry` phối hợp các `ObservationHandler`; handler có thể tạo meter, tracing span hoặc ngữ cảnh (context / 맥락) propagation tùy ngăn xếp (stack / 스택) được cấu hình. Vì khung phần mềm (framework / 프레임워크) có thể instrument HTTP máy chủ (server / 서버)/máy khách (client / 클라이언트), datasource và nhiều integrations sẵn, custom instrumentation nên bổ sung nghiệp vụ (business / 비즈니스) ranh giới (boundary / 경계) thay vì tạo duplicate span quanh mọi phương thức (method / 메서드).

Chỉ số (metric / 지표) dimensions phải low-cardinality vì mỗi combination tạo thời gian (time / 시간) series. `method`, normalized tuyến (route / 경로), status group hoặc payment kiểu (type / 타입) thường bounded; `userId`, `orderId`, raw exception message và full URL thường không bounded. High-cardinality định danh (identity / 식별자) phù hợp dấu vết (trace / 추적)/log hơn. Một hệ thống quan sát tốt dùng cùng ngữ nghĩa (semantic / 의미적) thao tác (operation / 연산) names/correlation để đi từ chỉ số (metric / 지표) spike → exemplar/dấu vết (trace / 추적) → logs → JFR/DB bằng chứng (evidence / 증거).

Actuator chỉ là management surface. Endpoint `health`, `metrics`, `mappings`, `conditions`, `threaddump`, `heapdump`, `env` có rủi ro (risk / 위험) khác nhau. Exposure và authorization phải được thiết kế như admin API; môi trường vận hành (production / 운영 환경) không nên công khai (public / 공개) toàn bộ `/actuator/**`. Health cũng phải có ngữ nghĩa (semantics / 의미론): liveness trả lời restart có giúp không; readiness trả lời instance có nên nhận traffic không.
<!-- SPRING_BATCH5_OBS_INTERMEDIATE_END -->

---

# 86. Micrometer

Micrometer là metrics/observation lớp trừu tượng (abstraction / 추상화) trong Spring ecosystem.

Counter đo sự kiện (event / 이벤트) count tăng dần. Gauge đo hiện tại (current / 현재) giá trị (value / 값). Timer đo count + duration phân phối (distribution / 분포).

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

vì mỗi người dùng (user / 사용자) tạo thời gian (time / 시간) series.

Đúng hơn:

```text
status=SUCCESS
paymentType=CARD
```

---

# 87. Observation

Hiện đại (modern / 현대적) Spring/Micrometer Observation mô hình (model / 모델) cho phép một thao tác (operation / 연산) tạo metrics/tracing instrumentation thống nhất.

Bạn chưa cần custom Observation phức tạp ở Intermediate, nhưng nên hiểu khung phần mềm (framework / 프레임워크) khả năng quan sát (observability / 관측 가능성) không chỉ là `log.info`.

Cấp cao (senior / 시니어) sẽ học ngữ cảnh dấu vết (trace context / 추적 컨텍스트) propagation và custom observations.

---

# 88. Liveness và Readiness ở triển khai (deployment / 배포)

Liveness không nên thất bại (fail / 실패) vì một bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) temporary unavailable nếu restart tiến trình (process / 프로세스) không giúp.

Readiness có thể thất bại (fail / 실패) để bộ cân bằng tải (load balancer / 로드 밸런서) stop sending traffic.

Probe phải nhanh và bounded. Health endpoint gọi 10 slow APIs mỗi 2 giây có thể trở thành tải (load / 로드) generator.

---

# 89. Graceful Shutdown awareness

Ứng dụng (application / 애플리케이션) shutdown tốt không phải `kill -9`.

Luồng (flow / 흐름) lý tưởng:

```text
stop accepting traffic
→ drain in-flight requests
→ stop producers
→ finish/stop background tasks
→ close clients/pools
→ close context
```

Boot hỗ trợ graceful shutdown ở web hạ tầng (infrastructure / 인프라), nhưng custom executor/máy khách (client / 클라이언트)/tài nguyên (resource / 자원) phải có vòng đời (lifecycle / 생명주기) đúng.

---

# 90. Coding Patterns ở Intermediate

**Bean collection as chiến lược (strategy / 전략)/chuỗi (chain / 사슬).** Inject `List<T>` thay vì giant conditional.

**Typed cấu hình (configuration / 구성) + kiểm tra hợp lệ (validation / 검증).** Invalid cấu hình (config / 설정) thất bại (fail / 실패) startup.

**Proxy ranh giới (boundary / 경계) awareness.** Nếu tính năng (feature / 기능) dựa phương thức (method / 메서드) interception, bên ngoài (external / 외부) lời gọi (call / 호출) đường dẫn (path / 경로) phải đi qua proxy.

**Transactional use-case ranh giới (boundary / 경계).** giao dịch (transaction / 트랜잭션) bao nghiệp vụ (business / 비즈니스) atomic thao tác (operation / 연산), không tùy tiện ở controller/repository mọi nơi.

**DTO projection for reads.** Không tải (load / 로드) thực thể (entity / 엔터티) đồ thị (graph / 그래프) chỉ để trả 3 fields.

**Bounded async.** Executor hàng đợi (queue / 큐)/sức chứa (capacity / 용량)/thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) phải tường minh (explicit / 명시적).

**vận chuyển (transport / 전송) adapter translation.** HTTP/JPA vendor exceptions không leak vô hạn vào cốt lõi (core / 핵심).

---

# 91. thiết kế (design / 설계) Patterns ở Intermediate

Spring AOP thể hiện Proxy/Interceptor. HandlerAdapter thể hiện Adapter. MVC filters/interceptors tạo chuỗi (chain / 사슬) of Responsibility. `BeanFactory` và `FactoryBean` thể hiện factory abstractions. Spring Events liên hệ Observer. `JdbcTemplate`/`TransactionTemplate` là template-style patterns. chiến lược (strategy / 전략) injection qua multiple beans giúp nghiệp vụ (business / 비즈니스) extension mà không mở `switch` khổng lồ.

Mẫu (pattern / 패턴) chỉ có giá trị khi bạn hiểu thời gian chạy (runtime / 런타임) chi phí (cost / 비용) và hidden điều khiển (control / 제어) luồng (flow / 흐름).

---

# 92. dùng chung (common / 공통) Intermediate mistakes

Một lỗi rất phổ biến là “annotation stacking”: `@Transactional @Async @Cacheable` trên cùng phương thức (method / 메서드) mà không dấu vết (trace / 추적) thực thi (execution / 실행) thứ tự (order / 순서). giao dịch (transaction / 트랜잭션) có chạy ở caller luồng thực thi (thread / 스레드) hay async luồng thực thi (thread / 스레드)? bộ nhớ đệm (cache / 캐시) key được check trước hay sau bảo mật (security / 보안)? Exception thử lại (retry / 재시도) ở ngoài hay trong giao dịch (transaction / 트랜잭션)? Nếu không trả lời được, mã (code / 코드) chưa đủ rõ.

Lỗi khác là fix N+1 bằng EAGER toàn bộ. Điều đó chuyển từ “truy vấn (query / 쿼리) nhiều” sang “fetch quá nhiều”.

Lỗi khác là tăng DB pool khi pool hết thời gian chờ (timeout / 타임아웃). Nguyên nhân có thể là long giao dịch (transaction / 트랜잭션) hoặc slow truy vấn (query / 쿼리); pool lớn hơn chỉ đưa thêm tải (load / 로드) xuống DB.

Lỗi khác là `@SpringBootTest` cho mọi kiểm thử (test / 테스트). Dùng đơn vị (unit / 단위)/slice/tích hợp (integration / 통합) đúng mức (level / 수준).

Lỗi khác là xem ứng dụng (application / 애플리케이션) events như durable message hàng đợi (queue / 큐).

---

# 93. Mini dự án (project / 프로젝트) Intermediate: thứ tự (order / 순서) dịch vụ (service / 서비스)

Hãy xây `Order Service` dùng PostgreSQL + Flyway + Spring dữ liệu (data / 데이터) JPA. `Order` có items, status và optimistic `@Version`. Endpoint tạo thứ tự (order / 순서), đọc detail, danh sách (list / 목록) pagination, cancel và mark paid.

Bạn phải cố ý tạo N+1 rồi đo số SQL, sau đó fix bằng fetch plan/projection. Bạn phải viết một giao dịch (transaction / 트랜잭션) tạo thứ tự (order / 순서) + outbox row cùng cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션), dù chưa publish broker thật.

Tạo `PaymentClient` bằng RestClient hoặc HTTP giao diện (interface / 인터페이스), có typed cấu hình (config / 설정) và hết thời gian chờ (timeout / 타임아웃). Viết một fake HTTP máy chủ (server / 서버)/kiểm thử (test / 테스트) để verify yêu cầu (request / 요청)/phản hồi (response / 응답) ánh xạ (mapping / 매핑).

Thêm bộ nhớ đệm (cache / 캐시) cho read đường dẫn (path / 경로) rồi mô tả key/TTL/vô hiệu hóa (invalidation / 무효화) ngữ nghĩa (semantics / 의미론). Thêm async notification và ghi rõ executor/hành vi khi thất bại (failure behavior / 실패 동작). Nếu Java 21+, chạy một experiment virtual threads.

Kiểm thử (test / 테스트) phải gồm plain đơn vị (unit / 단위) kiểm thử (test / 테스트), `@WebMvcTest`, `@DataJpaTest`, Testcontainers PostgreSQL và một `@SpringBootTest`.

---

# 94. Intermediate → cấp cao (senior / 시니어) Gate

Bạn sẵn sàng sang cấp cao (senior / 시니어) khi có thể dấu vết (trace / 추적) một bean từ BeanDefinition đến final proxy tham chiếu (reference / 참조); giải thích BeanFactoryPostProcessor khác BeanPostProcessor; nói được vì sao self-invocation bypass giao dịch (transaction / 트랜잭션)/bộ nhớ đệm (cache / 캐시)/async; và giải thích phụ thuộc (dependency / 의존성) candidate resolution khi có multiple beans.

Bạn phải dấu vết (trace / 추적) yêu cầu (request / 요청) qua Filter → DispatcherServlet → HandlerMapping → HandlerAdapter → ArgumentResolver → Controller → ReturnValueHandler → MessageConverter.

Với giao dịch (transaction / 트랜잭션), bạn phải giải thích REQUIRED, REQUIRES_NEW, NESTED, rollback-only, UnexpectedRollbackException, isolation và checked-exception quay lui (rollback / 롤백) defaults. Bạn phải biết `readOnly` không phải bảo mật (security / 보안) ghi (write / 쓰기) blocker.

Với JPA, bạn phải giải thích persistence ngữ cảnh (context / 맥락), managed/detached, dirty checking, flush vs lần ghi nhận (commit / 커밋), lazy loading, N+1, fetch phép nối (join / 조인), projection, pagination và optimistic locking.

Với hạ tầng (infrastructure / 인프라), bạn phải hiểu `@Async` cần executor, `@Scheduled` chạy trên mỗi instance, Spring sự kiện (event / 이벤트) không durable, bộ nhớ đệm (cache / 캐시) annotation không định nghĩa bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책), virtual luồng thực thi (thread / 스레드) không thay DB pool, và bảo mật (security / 보안) chạy ở filter chuỗi (chain / 사슬) trước MVC.

Nếu bạn chỉ nhớ API names mà không giải thích được thất bại (failure / 실패) modes, chưa nên gọi là cấp cao (senior / 시니어).

---

<!-- VERSION_DETAIL_PART2_2026-09-12_START -->
# Phiên bản (version / 버전) Deep Dive cho Intermediate: API nào xuất hiện ở generation nào?

`RestClient` được Spring khung phần mềm (framework / 프레임워크) giới thiệu từ **6.1**. Vì vậy Boot 2 / khung phần mềm (framework / 프레임워크) 5 không có API này; dự án (project / 프로젝트) cũ thường dùng `RestTemplate` cho synchronous HTTP hoặc `WebClient` cho reactive ngăn xếp (stack / 스택). Với khung phần mềm (framework / 프레임워크) 6.1+ và 7.x, `RestClient` là synchronous fluent API quan trọng cho mã (code / 코드) mới.

`JdbcClient` cũng có từ **khung phần mềm (framework / 프레임워크) 6.1**. Nó là fluent façade trên `JdbcTemplate` và `NamedParameterJdbcTemplate`, nên template APIs vẫn rất quan trọng cho batch, stored procedures và operations phức tạp.

Virtual-thread tích hợp (integration / 통합) của Spring Boot bắt đầu từ **Boot 3.2** trên Java 21+ với `spring.threads.virtual.enabled=true`. tính năng (feature / 기능) tiếp tục ở Boot 3.5 và Boot 4.x. Khi bật, pool-size properties truyền thống có thể không còn tác dụng theo cùng cách; `spring.main.keep-alive=true` vẫn cần nhớ ở các ứng dụng (application / 애플리케이션) mà daemon virtual threads có thể làm JVM kết thúc khi không còn non-daemon luồng thực thi (thread / 스레드).

Spring kiểm thử (test / 테스트) có bean override hạ tầng (infrastructure / 인프라) mới từ **khung phần mềm (framework / 프레임워크) 6.2**, gồm `@TestBean`, `@MockitoBean` và `@MockitoSpyBean`. Vì vậy tutorial cũ dùng `@MockBean` là bình thường; với khung phần mềm (framework / 프레임워크) 6.2/7.x, hãy hiểu hiện tại (current / 현재) TestContext bean-override mô hình (model / 모델).

Spring khung phần mềm (framework / 프레임워크) 7 thêm **API versioning hỗ trợ (support / 지원)** cho MVC/WebFlux và máy khách (client / 클라이언트) side, thêm `@Proxyable` để gợi ý proxy kiểu (type / 타입) per bean khi auto-proxying xảy ra, và chuyển null-safety contracts sang JSpecify. Những thay đổi này có ý nghĩa thời gian chạy (runtime / 런타임)/tooling thực tế, không chỉ là số major phiên bản (version / 버전).

Khi đọc một API Intermediate, luôn hỏi: nó thuộc khung phần mềm (framework / 프레임워크) hay Boot, xuất hiện từ phiên bản (version / 버전) nào, và lớp trừu tượng (abstraction / 추상화) tương đương trong generation cũ là gì. Cách này giúp bạn vừa maintain Boot 2/3 vừa viết Boot 4 mã (code / 코드) hiện đại.
<!-- VERSION_DETAIL_PART2_2026-09-12_END -->

---

# 95. phiên bản (version / 버전) Notes

Spring Boot 4.1.1 hiện yêu cầu Java 17+, Spring khung phần mềm (framework / 프레임워크) 7.0.9+ và hỗ trợ Java đến 26 theo official hệ thống (system / 시스템) requirements. Boot 4 dùng Jakarta EE 11/Servlet 6.1 baseline và ưu tiên Jackson 3.

Boot 3.x vẫn cực kỳ quan trọng trong enterprise. Khi đọc mã (code / 코드) Boot 3, bạn có thể gặp Jackson 2 và testing annotations/conventions cũ hơn. Boot 2.7 còn `javax.*`.

Hiện tại (current / 현재) references:

Spring Boot: https://docs.spring.io/spring-boot/tham chiếu (reference / 참조)/

Spring khung phần mềm (framework / 프레임워크): https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/

Giao dịch (transaction / 트랜잭션): https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/data-access/giao dịch (transaction / 트랜잭션).html

Spring MVC: https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/web/webmvc.html

Spring dữ liệu (data / 데이터) JPA: https://docs.spring.io/spring-data/jpa/tham chiếu (reference / 참조)/

Spring bảo mật (security / 보안): https://docs.spring.io/spring-security/tham chiếu (reference / 참조)/

> **Bàn giao:** Sau **Khả năng quan sát (observability / 관측 가능성) chuỗi xử lý (pipeline / 파이프라인): thao tác (operation / 연산) → Observation → metrics/traces, còn log là bằng chứng (evidence / 증거) khác**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

# Java Spring — Part 4: Master Supplement — Rewritten Detailed

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Java Spring — Part 4: Master Supplement — Rewritten Detailed**. Route đi từ framework/container internals → proxy, transactions và MVC dispatch → Boot auto-configuration/TestContext → custom starters, AOT/runtime hints và null-safety → version evolution, để source trace giải thích hành vi thay vì gọi đó là “magic”.

## Spring khung phần mềm (framework / 프레임워크) 7 / Spring Boot 4 internals, khung phần mềm (framework / 프레임워크) authoring, AOT và phiên bản (version / 버전) evolution

> Đây là phần thứ tư của lộ trình **Beginner → Intermediate → cấp cao (senior / 시니어) → Master Supplement**. Ba phần đầu tập trung vào xây ứng dụng (application / 애플리케이션) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링). Master Supplement tập trung vào Spring như một khung phần mềm (framework / 프레임워크): bộ chứa (container / 컨테이너) nguồn (source / 소스) luồng (flow / 흐름), auto-proxy creation, giao dịch (transaction / 트랜잭션) interception, MVC dispatch internals, Boot auto-configuration, TestContext, custom starters, AOT/thời gian chạy (runtime / 런타임) hints, null-safety và major-version di chuyển (migration / 마이그레이션). Baseline stable là **Spring Boot 4.1.1 + Spring khung phần mềm (framework / 프레임워크) 7.0.9**; Boot 4.2.0-M1 / khung phần mềm (framework / 프레임워크) 7.1.0-M1 chỉ là preview.

---

# 1. phiên bản (version / 버전) ma trận (matrix / 행렬) dành cho Master

Mục này biến kiến thức backend thành tiêu chí kiểm tra và quyết định triển khai. Hãy xác định contract, failure mode, evidence và cách rollback trước khi áp dụng.

| Generation | Spring Boot | Spring Framework | Java baseline | Web/Jakarta generation | Vai trò |
|---|---|---|---|---|---|
| Legacy | 2.7.x | 5.3.x | Java 8+ | `javax.*` | maintain mã (code / 코드) cũ |
| hiện đại (modern / 현대적) 3.x | 3.5.16 | 6.2.19+ | Java 17+ | Jakarta / Servlet 6.0 | di chuyển (migration / 마이그레이션) cầu nối (bridge / 브리지) |
| hiện tại (current / 현재) stable | 4.1.1 | 7.0.9+ | Java 17–26 | Jakarta EE 11 / Servlet 6.1 | baseline tài liệu |
| hiện tại (current / 현재) preview | 4.2.0-M1 | 7.1.0-M1+ | Java 17–26 | preview | theo dõi direction |

Một Master Spring engineer cần nghĩ phiên bản (version / 버전) như một **phụ thuộc (dependency / 의존성) nền tảng (platform / 플랫폼)**. Boot quản lý một tested phụ thuộc (dependency / 의존성) set gồm khung phần mềm (framework / 프레임워크), bảo mật (security / 보안), dữ liệu (data / 데이터) và nhiều third-party libraries. Vì vậy “override một sản phẩm tạo ra (artifact / 산출물) lên phiên bản (version / 버전) mới hơn” không tự động là upgrade tốt hơn; nền tảng (platform / 플랫폼) coherence thường quan trọng hơn newest-number-per-library.

# 2. Đọc Spring nguồn (source / 소스) theo chuỗi xử lý (pipeline / 파이프라인)

Spring nguồn (source / 소스) quá lớn để đọc ngẫu nhiên. Hãy dấu vết (trace / 추적) một câu hỏi cụ thể, ví dụ “một `@Service` transactional trở thành proxy bằng cách nào?” rồi đi theo luồng (flow / 흐름):

```text
configuration/component metadata
→ BeanDefinition registration
→ BeanFactory
→ instantiation
→ dependency population
→ initialization
→ BeanPostProcessors
→ auto-proxy decision
→ proxy creation
→ interceptor chain
→ final bean reference
```

Cách đọc này giúp mỗi lớp (class / 클래스) có vị trí rõ thay vì trở thành hàng nghìn dòng nguồn (source / 소스) rời rạc.

# 3. `DefaultListableBeanFactory`

`DefaultListableBeanFactory` là hiện thực (implementation / 구현) trung tâm quản lý BeanDefinitions, singleton registry và phụ thuộc (dependency / 의존성) resolution trong dùng chung (common / 공통) ApplicationContext. Nó xử lý aliases, factory methods, scopes, generic types, qualifiers, primary/fallback candidates, FactoryBeans và kiểu (type / 타입) queries. Khi gỡ lỗi (debug / 디버그) missing/wrong bean, hãy tách hai câu hỏi: siêu dữ liệu (metadata / 메타데이터) candidate nào tồn tại, và final thời gian chạy (runtime / 런타임) đối tượng (object / 객체) nào được expose sau vòng đời (lifecycle / 생명주기)/proxying.

# 4. Singleton registry và early references

Spring có machinery cho singleton creation trạng thái (state / 상태) và một số early references để xử lý historical setter/trường dữ liệu (field / 필드) circular dependencies. Điều này trở nên khó hơn khi auto-proxying tham gia vì tham chiếu (reference / 참조) sớm và final proxy không được mâu thuẫn. Dù khung phần mềm (framework / 프레임워크) có thể giải một số cycle, ứng dụng (application / 애플리케이션) không nên dựa vào circular phụ thuộc (dependency / 의존성) như thiết kế (design / 설계) tính năng (feature / 기능); cycle thường là tín hiệu ranh giới (boundary / 경계) sai.

<!-- SPRING_BATCH1_IOC_MASTER -->

> **Chuyển mạch:** Trong **Java Spring — Part 4: Master Supplement — Rewritten Detailed**, **Spring khung phần mềm (framework / 프레임워크) 7 / Spring Boot 4 internals, khung phần mềm (framework / 프레임워크) authoring, AOT và phiên bản (version / 버전) evolution** nêu điều cần giải thích; **Nguồn (source / 소스) dấu vết (trace / 추적): từ getBean() tới doCreateBean() và final exposed tham chiếu (reference / 참조)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Nguồn (source / 소스) dấu vết (trace / 추적): TransactionInterceptor → TransactionAspectSupport → giao dịch (transaction / 트랜잭션) manager** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguồn (source / 소스) dấu vết (trace / 추적): từ `getBean()` tới `doCreateBean()` và final exposed tham chiếu (reference / 참조)

Khi muốn đọc Spring nguồn (source / 소스) thay vì chỉ dùng API, một dấu vết (trace / 추적) có giá trị là bắt đầu từ `AbstractBeanFactory#doGetBean`. Lookup trước hết kiểm tra singleton bộ nhớ đệm (cache / 캐시); nếu chưa có instance, khung phần mềm (framework / 프레임워크) lấy merged BeanDefinition, bảo đảm dependencies cần tạo trước, rồi đi vào creation đường dẫn (path / 경로) phù hợp phạm vi (scope / 범위). Với singleton, singleton registry kiểm soát “create once” ngữ nghĩa (semantics / 의미론) và trạng thái currently-in-creation để phát hiện cycle.

`AbstractAutowireCapableBeanFactory#createBean` và `doCreateBean` là nơi đối tượng (object / 객체) creation chuỗi xử lý (pipeline / 파이프라인) trở nên rõ. khung phần mềm (framework / 프레임워크) có cơ hội resolve lớp (class / 클래스), cho `InstantiationAwareBeanPostProcessor` can thiệp trước instantiation, chọn constructor/factory phương thức (method / 메서드), instantiate bean, populate properties/injection points, chạy initialization callbacks rồi apply post-processors. Auto-proxy creator thường thay final exposed tham chiếu (reference / 참조) ở cuối vòng đời (lifecycle / 생명주기) bằng proxy.

Circular-reference hỗ trợ (support / 지원) làm chuỗi xử lý (pipeline / 파이프라인) phức tạp vì khung phần mềm (framework / 프레임워크) có thể đăng ký một **singleton factory cho early tham chiếu (reference / 참조)** trước khi bean hoàn tất initialization. `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference` cho phép auto-proxy hạ tầng (infrastructure / 인프라) bảo đảm early tham chiếu (reference / 참조) tương thích với đối tượng (object / 객체) sẽ được expose cuối. Đây là cơ chế (mechanism / 메커니즘) để hiểu nguồn (source / 소스), không phải invitation xây đồ thị (graph / 그래프) dựa vào circular references.

Khi đọc nguồn (source / 소스), đừng biến tên phương thức (method / 메서드) nội bộ thành công khai (public / 공개) đặc tả hợp đồng (contract / 계약). đặc tả hợp đồng (contract / 계약) mà ứng dụng (application / 애플리케이션) có thể dựa vào nằm ở documented bộ chứa (container / 컨테이너) ngữ nghĩa (semantics / 의미론), vòng đời (lifecycle / 생명주기) interfaces và API tham chiếu (reference / 참조). Tên helper hoặc thứ tự (ordering / 순서) hiện thực (implementation / 구현) có thể đổi giữa khung phần mềm (framework / 프레임워크) versions. Mastery là dùng internals để giải thích hành vi (behavior / 동작), rồi quay lại công khai (public / 공개) đặc tả hợp đồng (contract / 계약) để thiết kế mã (code / 코드) ổn định.
<!-- SPRING_BATCH1_IOC_MASTER_END -->

---

# 5. `ConfigurationClassPostProcessor`

`@Configuration`, `@ComponentScan`, `@Import` và `@Bean` chỉ là siêu dữ liệu (metadata / 메타데이터) cho tới khi Spring parse chúng. `ConfigurationClassPostProcessor` chạy ở BeanFactory post-processing phase và mở rộng gốc (root / 루트) cấu hình (configuration / 구성) thành một đồ thị (graph / 그래프) definitions/imports/components. Khi startup có missing/duplicate definitions, hãy dấu vết (trace / 추적) siêu dữ liệu (metadata / 메타데이터) expansion thay vì chỉ nhìn constructor injection.

# 6. `@Configuration` và tường minh (explicit / 명시적) bean parameters

Full cấu hình (configuration / 구성) classes historically có enhancement để direct calls giữa `@Bean` methods giữ bộ chứa (container / 컨테이너) ngữ nghĩa (semantics / 의미론). Tuy nhiên:

```java
@Bean
Client client(Auth auth) {
    return new Client(auth);
}
```

rõ hơn việc gọi `auth()` trực tiếp từ bean phương thức (method / 메서드). Mastery thường dẫn tới mã (code / 코드) ít phụ thuộc khung phần mềm (framework / 프레임워크) interception hơn, không phải nhiều magic hơn.

# 7. `AutowiredAnnotationBeanPostProcessor`

Constructor/trường dữ liệu (field / 필드)/phương thức (method / 메서드) injection annotations cần hạ tầng (infrastructure / 인프라) đọc siêu dữ liệu (metadata / 메타데이터) rồi resolve phụ thuộc (dependency / 의존성) qua BeanFactory. `AutowiredAnnotationBeanPostProcessor` là một thành phần (component / 컴포넌트) quan trọng của luồng (flow / 흐름) này. Constructor injection có lợi vì required dependencies được resolve trước construction và hệ kiểu (type system / 타입 시스템) nhìn thấy chúng; trường dữ liệu (field / 필드) injection phụ thuộc nhiều hơn vào post-construction mutation/reflection.

# 8. BeanPostProcessor thứ tự (ordering / 순서) và early-instantiation hazard

Nếu custom post-processor inject ordinary ứng dụng (application / 애플리케이션) beans quá sớm, ứng dụng (application / 애플리케이션) bean có thể được tạo trước khi toàn bộ processors/auto-proxy creators sẵn sàng. Log kiểu “not eligible for getting processed by all BeanPostProcessors” thường là tín hiệu này. hạ tầng (infrastructure / 인프라) nên giữ phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) tối thiểu và tránh kéo nghiệp vụ (business / 비즈니스) beans vào vòng đời (lifecycle / 생명주기) phase quá sớm.

# 9. `AbstractAutoProxyCreator`

Auto-proxy creator không proxy mọi bean. Nó tìm Advisors/interceptors phù hợp với bean/phương thức (method / 메서드). Nếu không có advisor, original bean được trả. Nếu có, khung phần mềm (framework / 프레임워크) bản dựng (build / 빌드) proxy và final bean tham chiếu (reference / 참조) trong ngữ cảnh (context / 맥락) là proxy. Vì vậy annotation advice không chạy có thể do advisor không match, bean không được proxy hoặc lời gọi (call / 호출) bypass proxy.

# 10. `ProxyFactory`, `AdvisedSupport` và interceptor chuỗi (chain / 사슬)

Proxy giữ mục tiêu (target / 대상) + advisors. thời gian chạy (runtime / 런타임) lời gọi (call / 호출) conceptually:

```text
proxy
→ security interceptor
→ observation interceptor
→ transaction interceptor
→ target
```

Around interceptor có thể không gọi mục tiêu (target / 대상), ví dụ bộ nhớ đệm (cache / 캐시) hit hoặc authorization thất bại (failure / 실패). thứ tự (ordering / 순서) do đó là ngữ nghĩa (semantics / 의미론), không phải style.

# 11. Spring 7 `@Proxyable`

Khung phần mềm (framework / 프레임워크) 7 thêm `@Proxyable` để gợi ý proxy kiểu (type / 타입) per bean, có thể chọn interface-based JDK proxy hoặc target-class CGLIB proxy. Annotation chỉ ảnh hưởng bean **khi auto-proxying thực sự xảy ra**; nó không tự tạo proxy. Đây là advanced di chuyển (migration / 마이그레이션)/hạ tầng (infrastructure / 인프라) công cụ (tool / 도구), không phải annotation cần đặt lên mọi dịch vụ (service / 서비스).

# 12. giao dịch (transaction / 트랜잭션) nguồn (source / 소스) luồng (flow / 흐름)

Simplified:

```text
@Transactional metadata
→ transaction advisor
→ TransactionInterceptor
→ TransactionAttributeSource
→ choose transaction manager
→ create/join transaction
→ invoke target
→ commit/rollback
→ cleanup resources
```

Giao dịch (transaction / 트랜잭션) interceptor không trực tiếp biết JDBC/JPA hiện thực (implementation / 구현); nó đi qua transaction-manager lớp trừu tượng (abstraction / 추상화).

<!-- SPRING_BATCH3_TX_MASTER -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 4: Master Supplement — Rewritten Detailed**, **Nguồn (source / 소스) dấu vết (trace / 추적): từ getBean() tới doCreateBean() và final exposed tham chiếu (reference / 참조)** nêu điều cần giải thích; **Nguồn (source / 소스) dấu vết (trace / 추적): TransactionInterceptor → TransactionAspectSupport → giao dịch (transaction / 트랜잭션) manager** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Spring dữ liệu (data / 데이터) JPA proxy, truy vấn (query / 쿼리) thực thi (execution / 실행) và thực thể (entity / 엔터티) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguồn (source / 소스) dấu vết (trace / 추적): `TransactionInterceptor` → `TransactionAspectSupport` → giao dịch (transaction / 트랜잭션) manager

`TransactionInterceptor` là MethodInterceptor mỏng; phần orchestration chính nằm trong `TransactionAspectSupport#invokeWithinTransaction`. khung phần mềm (framework / 프레임워크) lấy `TransactionAttributeSource`, xác định manager, tạo/phép nối (join / 조인) giao dịch (transaction / 트랜잭션) rồi invoke callback tới mục tiêu (target / 대상). Sau mục tiêu (target / 대상), lô-gic (logic / 논리) complete-after-throwing hoặc commit-after-returning chuyển điều khiển (control / 제어) cho giao dịch (transaction / 트랜잭션) manager. Đọc nguồn (source / 소스) theo luồng (flow / 흐름) này giúp bạn phân biệt AOP interception với actual tài nguyên (resource / 자원) hiện thực (implementation / 구현).

Ở JDBC, `DataSourceTransactionManager` phối hợp `DataSourceUtils` và tài nguyên (resource / 자원) holder để cùng DataSource lookup nhận transaction-bound liên kết (connection / 연결). Ở JPA, `JpaTransactionManager` quản lý EntityManager/persistence ngữ cảnh (context / 맥락) và có thể expose JDBC liên kết (connection / 연결) tích hợp (integration / 통합) tùy setup. `TransactionSynchronizationManager` chỉ là ngữ cảnh (context / 맥락) registry; nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론) vẫn nằm trong manager + underlying tài nguyên (resource / 자원).
<!-- SPRING_BATCH3_TX_MASTER_END -->

---

# 13. `TransactionSynchronizationManager`

Imperative giao dịch (transaction / 트랜잭션) hạ tầng (infrastructure / 인프라) cần bind resources/ngữ cảnh (context / 맥락) với hiện tại (current / 현재) thực thi (execution / 실행) luồng thực thi (thread / 스레드): liên kết (connection / 연결)/session, giao dịch (transaction / 트랜잭션) active/read-only/name/isolation và synchronization callbacks. `TransactionSynchronizationManager` là hạ tầng (infrastructure / 인프라) trung tâm cho kiểu binding này. nghiệp vụ (business / 비즈니스) mã (code / 코드) hiếm khi nên gọi trực tiếp, nhưng hiểu nó giải thích vì sao spawn luồng thực thi (thread / 스레드) mới không tự mang imperative giao dịch (transaction / 트랜잭션) theo.

# 14. Self-invocation nhìn từ proxy internals

Bên ngoài (external / 외부) lời gọi (call / 호출) đi `caller → proxy → interceptor → target`. nội bộ (internal / 내부) `this.otherMethod()` chỉ là Java lời gọi (call / 호출) trên mục tiêu (target / 대상) và không quay lại proxy. Vì vậy giao dịch (transaction / 트랜잭션)/bộ nhớ đệm (cache / 캐시)/bảo mật (security / 보안)/async advice có thể bị bypass. Đây là consequence của proxy-based AOP, không phải bug riêng `@Transactional`.

<!-- SPRING_BATCH3_PERSISTENCE_MASTER -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Java Spring — Part 4: Master Supplement — Rewritten Detailed**, **Nguồn (source / 소스) dấu vết (trace / 추적): TransactionInterceptor → TransactionAspectSupport → giao dịch (transaction / 트랜잭션) manager** nêu điều cần giải thích; **Spring dữ liệu (data / 데이터) JPA proxy, truy vấn (query / 쿼리) thực thi (execution / 실행) và thực thể (entity / 엔터티) trạng thái (state / 상태)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Nguồn (source / 소스) dấu vết (trace / 추적): DispatcherServlet#doDispatch thực sự phối hợp những chiến lược (strategy / 전략) nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spring dữ liệu (data / 데이터) JPA proxy, truy vấn (query / 쿼리) thực thi (execution / 실행) và thực thể (entity / 엔터티) trạng thái (state / 상태)

Spring dữ liệu (data / 데이터) tạo repository proxy từ repository siêu dữ liệu (metadata / 메타데이터), repository fragments và store-specific cơ sở (base / 기반) hiện thực (implementation / 구현). truy vấn (query / 쿼리) phương thức (method / 메서드) có thể được resolve thành derived truy vấn (query / 쿼리), declared truy vấn (query / 쿼리) hoặc custom hiện thực (implementation / 구현). Proxy vì vậy là dispatch tầng (layer / 계층); truy vấn (query / 쿼리) parser/JPA provider/cơ sở dữ liệu (database / 데이터베이스) mới quyết định SQL cuối cùng.

Ở JPA, bốn trạng thái useful là transient, managed, detached và removed. Dirty checking chỉ áp dụng có ý nghĩa với managed thực thể (entity / 엔터티) trong persistence ngữ cảnh (context / 맥락). Khi giao dịch (transaction / 트랜잭션) kết thúc và ngữ cảnh (context / 맥락) đóng, thực thể (entity / 엔터티) trở detached; sửa trường dữ liệu (field / 필드) trên detached đối tượng (object / 객체) không tự tạo SQL. `merge` không “reattach same đối tượng (object / 객체)” theo cách đơn giản mà bản sao (copy / 복사) trạng thái (state / 상태) vào managed instance và trả managed instance đó.

Hiệu năng (performance / 성능) phải được reason bằng fetch plan và SQL count, không bằng số repository methods. Một repository lời gọi (call / 호출) có thể tạo một SQL projection nhỏ hoặc hàng trăm lazy queries. Ngược lại, một fetch phép nối (join / 조인) quá lớn có thể tạo Cartesian multiplication. Spring dữ liệu (data / 데이터) lớp trừu tượng (abstraction / 추상화) không loại nhu cầu đọc generated SQL, thực thi (execution / 실행) plan và persistence-context hành vi (behavior / 동작).
<!-- SPRING_BATCH3_PERSISTENCE_MASTER_END -->

---

# 15. `DispatcherServlet` nguồn (source / 소스) luồng (flow / 흐름)

High mức (level / 수준):

```text
request
→ doDispatch
→ HandlerExecutionChain
→ HandlerAdapter
→ handler invocation
→ return-value handling / ModelAndView
→ exception resolution
→ render/complete
```

`DispatcherServlet` là Front Controller phối hợp chiến lược (strategy / 전략) interfaces thay vì hard-code mọi handler mô hình (model / 모델).

<!-- SPRING_BATCH2_REQUEST_MASTER -->

> **Chuyển mạch:** Trong **Java Spring — Part 4: Master Supplement — Rewritten Detailed**, **Spring dữ liệu (data / 데이터) JPA proxy, truy vấn (query / 쿼리) thực thi (execution / 실행) và thực thể (entity / 엔터티) trạng thái (state / 상태)** nêu điều cần giải thích; **Nguồn (source / 소스) dấu vết (trace / 추적): DispatcherServlet#doDispatch thực sự phối hợp những chiến lược (strategy / 전략) nào?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Nguồn (source / 소스) dấu vết (trace / 추적) Spring bảo mật (security / 보안) và TestContext** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguồn (source / 소스) dấu vết (trace / 추적): `DispatcherServlet#doDispatch` thực sự phối hợp những chiến lược (strategy / 전략) nào?

Trong `doDispatch`, DispatcherServlet không trực tiếp gọi controller bằng reflection tùy ý. Nó lấy handler qua `getHandler`, chọn adapter qua `getHandlerAdapter`, rồi delegate việc invoke. Với annotated controller, `RequestMappingHandlerAdapter` tạo `ServletInvocableHandlerMethod`; argument resolution đi qua các composite resolver đã được đăng ký theo thứ tự (order / 순서). Một resolver chỉ tham gia khi `supportsParameter` trả true, sau đó mới resolve giá trị (value / 값). Return values đi qua một composite tương tự để chọn handler phù hợp.

`RequestResponseBodyMethodProcessor` là một mắt xích quan trọng cho `@RequestBody` và phản hồi (response / 응답) body: nó phối hợp message converters, content negotiation, kiểm tra hợp lệ (validation / 검증)/binding hooks và body advice. Vì vậy lỗi JSON deserialize, kiểm tra hợp lệ (validation / 검증) và media kiểu (type / 타입) xảy ra trước controller body thực thi (execution / 실행) trong nhiều trường hợp (case / 사례). Khi custom converter/resolver được thêm sai thứ tự (order / 순서), bạn đang thay dispatch thuật toán (algorithm / 알고리즘) của khung phần mềm (framework / 프레임워크) chứ không chỉ “thêm annotation hỗ trợ”.

Exception resolution cũng là chiến lược (strategy / 전략) chuỗi (chain / 사슬). `ExceptionHandlerExceptionResolver` tìm `@ExceptionHandler`; `ResponseStatusExceptionResolver` xử lý status-oriented exceptions; default resolver map một số khung phần mềm (framework / 프레임워크) exceptions. Master-level extension nên chọn đúng chiến lược (strategy / 전략) giao diện (interface / 인터페이스) thay vì override DispatcherServlet hoặc viết filter bắt mọi Throwable làm mất ngữ nghĩa (semantics / 의미론) MVC.
<!-- SPRING_BATCH2_REQUEST_MASTER_END -->

---

# 16. `RequestMappingHandlerMapping`

Annotated mappings được đăng ký theo đường dẫn (path / 경로), HTTP phương thức (method / 메서드), params, headers, consumes/produces và ở khung phần mềm (framework / 프레임워크) 7 còn có API-version ngữ nghĩa (semantics / 의미론). Ambiguous tuyến (route / 경로) là xung đột (conflict / 충돌) trong ánh xạ (mapping / 매핑) registry, không phải DispatcherServlet ngẫu nhiên chọn sai.

# 17. `RequestMappingHandlerAdapter`

Adapter phối hợp argument resolvers, return-value handlers, conversion/binding, kiểm tra hợp lệ (validation / 검증), async hỗ trợ (support / 지원) và message converters để invoke annotated phương thức (method / 메서드). Custom extension nên giữ web-boundary concern; đừng giấu heavy nghiệp vụ (business / 비즈니스) I/O trong argument resolver.

# 18. khung phần mềm (framework / 프레임워크) 7 API Versioning

Khung phần mềm (framework / 프레임워크) 7 có `ApiVersionStrategy`, resolver/parser/kiểm tra hợp lệ (validation / 검증)/deprecation handler abstractions. MVC/WebFlux mappings có thể khai báo API phiên bản (version / 버전); RestClient/WebClient/HTTP dịch vụ (service / 서비스) clients cũng có phiên bản (version / 버전) insertion hỗ trợ (support / 지원). khung phần mềm (framework / 프레임워크) giải mechanics, còn sản phẩm (product / 제품) vẫn phải quyết định tính tương thích (compatibility / 호환성)/deprecation/sunset chính sách (policy / 정책).

# 19. Jackson 3 generation

Boot 4 ưu tiên Jackson 3. mã (code / 코드) chỉ dùng DTO + Boot auto-config thường migrate dễ. mã (code / 코드) custom mapper/modules/polymorphic serialization phải rà soát (review / 검토) gói (package / 패키지) changes và behavioral tính tương thích (compatibility / 호환성). `spring-boot-jackson2` tồn tại như deprecated stop-gap, không phải long-term mục tiêu (target / 대상).

<!-- SPRING_BATCH4_SECURITY_TEST_MASTER -->

> **Chuyển mạch:** Ở chặng này của **Java Spring — Part 4: Master Supplement — Rewritten Detailed**, **Nguồn (source / 소스) dấu vết (trace / 추적): DispatcherServlet#doDispatch thực sự phối hợp những chiến lược (strategy / 전략) nào?** nêu điều cần giải thích; **Nguồn (source / 소스) dấu vết (trace / 추적) Spring bảo mật (security / 보안) và TestContext** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Di chuyển (migration / 마이그레이션) đồ thị (graph / 그래프): 2.7/5.3 → 3.5/6.2 → 4.1/7.0** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguồn (source / 소스) dấu vết (trace / 추적) Spring bảo mật (security / 보안) và TestContext

`DelegatingFilterProxy` resolve filter bean từ ApplicationContext nhưng delegate bảo mật (security / 보안) thực thi (execution / 실행) cho `FilterChainProxy`. `FilterChainProxy` chọn first matching `SecurityFilterChain` theo thứ tự (order / 순서) rồi chạy danh sách (list / 목록) bảo mật (security / 보안) filters. Authentication filters delegate tới `AuthenticationManager`; `ProviderManager` chọn `AuthenticationProvider`; authorization filter/interceptors dùng `AuthorizationManager`. `ExceptionTranslationFilter` chuyển bảo mật (security / 보안) exceptions thành entry-point/access-denied responses ở servlet bảo mật (security / 보안) tầng (layer / 계층). dấu vết (trace / 추적) theo các đối tượng (object / 객체) này giúp gỡ lỗi (debug / 디버그) 401/403 mà không cần bật gỡ lỗi (debug / 디버그) log toàn hệ thống.

Phương thức (method / 메서드) bảo mật (security / 보안) lại đi qua Spring AOP hạ tầng (infrastructure / 인프라). Advisor/interceptor được gắn vào bean phương thức (method / 메서드); lời gọi (call / 호출) phải qua proxy. Điều này nối trực tiếp kiến thức (knowledge / 지식) của bộ chứa (container / 컨테이너)/AOP với bảo mật (security / 보안): self-invocation có thể bypass method-security advice giống giao dịch (transaction / 트랜잭션)/bộ nhớ đệm (cache / 캐시) nếu lời gọi (call / 호출) đường dẫn (path / 경로) không đi qua proxy.

Ở testing, Spring TestContext tạo `MergedContextConfiguration` từ annotations/cấu hình (configuration / 구성)/profiles/properties/ngữ cảnh (context / 맥락) customizers rồi dùng nó như nền của bộ nhớ đệm (cache / 캐시) key. Bean override annotations như `@MockitoBean` tham gia ngữ cảnh (context / 맥락) customization, nên thay mock set có thể làm ngữ cảnh (context / 맥락) không reuse. Hiểu bộ nhớ đệm (cache / 캐시) key giúp tối ưu suite bằng kiến trúc (architecture / 아키텍처) thay vì chỉ tăng CPU runner.
<!-- SPRING_BATCH4_SECURITY_TEST_MASTER_END -->

---

# 20. Spring TestContext khung phần mềm (framework / 프레임워크)

TestContext quản lý ngữ cảnh (context / 맥락) loading, caching, listeners, DI, kiểm thử (test / 테스트) transactions và bean overrides. Suite chậm thường do nhiều unique ngữ cảnh (context / 맥락) configurations/profiles/mock combinations làm bộ nhớ đệm (cache / 캐시) reuse kém. Master nên đo ngữ cảnh (context / 맥락) fragmentation trước khi kết luận “Spring kiểm thử (test / 테스트) chậm”.

# 21. Bean override hạ tầng (infrastructure / 인프라) từ khung phần mềm (framework / 프레임워크) 6.2

Khung phần mềm (framework / 프레임워크) 6.2 có `@TestBean`, `@MockitoBean`, `@MockitoSpyBean` trên tường minh (explicit / 명시적) bean-override hạ tầng (infrastructure / 인프라). Đây là hướng hiện đại hơn toàn cục (global / 전역) bean-definition overriding. Legacy tutorials vẫn dùng `@MockBean`; đọc được nhưng mã (code / 코드) mới trên 6.2/7.x nên hiểu hiện tại (current / 현재) cơ chế (mechanism / 메커니즘).

# 22. Boot 4 kiểm thử (test / 테스트) modularization

Boot 4 tách kiểm thử (test / 테스트) hạ tầng (infrastructure / 인프라) theo technology, với mẫu (pattern / 패턴) `spring-boot-starter-<technology>-test`. di chuyển (migration / 마이그레이션) phải rà soát (review / 검토) kiểm thử (test / 테스트) dependencies riêng. bảo mật (security / 보안)/GraphQL/JDBC/JPA tests có thể cần dedicated kiểm thử (test / 테스트) starter thay vì vô tình dựa vào transitive classpath của Boot 3.

# 23. Auto-configuration discovery

Hiện đại (modern / 현대적) Boot khai báo auto-configurations qua siêu dữ liệu (metadata / 메타데이터) `META-INF/spring/...AutoConfiguration.imports` thay vì broad thành phần (component / 컴포넌트) scanning. Boot tải (load / 로드) candidates, evaluate conditions rồi import. Custom starter nên tường minh (explicit / 명시적), back-off friendly và không scan bên tiêu thụ (consumer / 소비자) gói (package / 패키지) tùy tiện.

# 24. Conditions như executable cấu hình (configuration / 구성) đồ thị (graph / 그래프)

`@ConditionalOnClass`, `@ConditionalOnMissingBean`, `@ConditionalOnProperty`, `@ConditionalOnWebApplication` tạo boolean đồ thị (graph / 그래프). Timing quan trọng: missing-bean điều kiện (condition / 조건) chỉ thấy definitions đã biết ở phase đó. Auto-config thứ tự (ordering / 순서) chỉ nên dùng khi phụ thuộc (dependency / 의존성) thực sự tồn tại và phải có tests.

# 25. điều kiện (condition / 조건) Evaluation Report và `ApplicationContextRunner`

Khi auto-config không match, điều kiện (condition / 조건) report cho biết lý do. Custom starter nên kiểm thử (test / 테스트) phụ thuộc (dependency / 의존성) present/absent, thuộc tính (property / 속성) on/off và custom-bean back-off. `ApplicationContextRunner` rất hữu ích vì tạo ngữ cảnh (context / 맥락) nhỏ, nhanh và inspectable.

# 26. `@ConfigurationProperties` như API công khai (public API / 공개 API)

Starter properties có prefix, kiểu (type / 타입), defaults, kiểm tra hợp lệ (validation / 검증) và siêu dữ liệu (metadata / 메타데이터). Rename thuộc tính (property / 속성) là cấu hình (configuration / 구성) API thay đổi (change / 변경). thư viện (library / 라이브러리) author nên provide deprecation/di chuyển (migration / 마이그레이션) siêu dữ liệu (metadata / 메타데이터) khi có thể, không coi YAML key là hiện thực (implementation / 구현) detail.

# 27. Boot 4 modular starter mô hình (model / 모델)

Di chuyển (migration / 마이그레이션) guide ánh xạ (mapping / 매핑) điển hình:

```text
spring-boot-starter-web
→ spring-boot-starter-webmvc

spring-boot-starter-oauth2-client
→ spring-boot-starter-security-oauth2-client

spring-boot-starter-oauth2-resource-server
→ spring-boot-starter-security-oauth2-resource-server
```

Flyway/Liquibase cũng có dedicated Boot starters trong Boot 4 mô hình (model / 모델). Supporting Boot 3 và Boot 4 trong cùng custom starter sản phẩm tạo ra (artifact / 산출물) bị khuyến nghị thận trọng vì gói (package / 패키지)/mô-đun (module / 모듈) đồ thị (graph / 그래프) khác đáng kể.

# 28. `spring-boot-starter-classic` di chuyển (migration / 마이그레이션) cầu nối (bridge / 브리지)

Boot 4 cung cấp classic starter để tái tạo broader classpath tạm thời. di chuyển (migration / 마이그레이션) có thể đi `Boot 3.5 → Boot 4 + classic → fix imports/deps → remove classic → dedicated starters`. Classic là aid, không phải final kiến trúc (architecture / 아키텍처).

# 29. JSpecify trong khung phần mềm (framework / 프레임워크) 7

Khung phần mềm (framework / 프레임워크) 7 annotate APIs bằng JSpecify. `@NullMarked` cho non-null default; type-use `@Nullable` biểu diễn nullable chính xác trong generics/arrays/nested types. Các Spring null annotations cũ trong `org.springframework.lang` được deprecate theo hướng JSpecify. Java static phân tích (analysis / 분석) và Kotlin interoperability vì vậy thay đổi thực tế khi upgrade.

# 30. `Nullness` thời gian chạy (runtime / 런타임) API

Khung phần mềm (framework / 프레임워크) 7 có `org.springframework.core.Nullness` để khung phần mềm (framework / 프레임워크) mã (code / 코드) inspect nullness của trường dữ liệu (field / 필드)/phương thức (method / 메서드) parameter/kiểu (type / 타입) usage. Static checking vẫn là giá trị chính; thời gian chạy (runtime / 런타임) API dành cho động (dynamic / 동적) khung phần mềm (framework / 프레임워크)/binding lô-gic (logic / 논리).

# 31. `RestClient` phiên bản (version / 버전) evolution

`RestClient` xuất hiện từ khung phần mềm (framework / 프레임워크) 6.1. khung phần mềm (framework / 프레임워크) 7 mở rộng máy khách (client / 클라이언트) hạ tầng (infrastructure / 인프라) và API-version tích hợp (integration / 통합). lĩnh vực (domain / 도메인)/ứng dụng (application / 애플리케이션) API nên expose gateway đặc tả hợp đồng (contract / 계약), không expose RestClient như nghiệp vụ (business / 비즈니스) lớp trừu tượng (abstraction / 추상화).

# 32. `JdbcClient` phiên bản (version / 버전) evolution

`JdbcClient` cũng từ 6.1 và delegate xuống JdbcTemplate/NamedParameterJdbcTemplate. Simple truy vấn (query / 쿼리)/cập nhật (update / 업데이트) có thể dùng fluent máy khách (client / 클라이언트); batch/stored-procedure/complex callbacks vẫn phù hợp lower-level templates.

# 33. Virtual Threads từ Boot 3.2

`spring.threads.virtual.enabled=true` xuất hiện từ Boot 3.2 cho Java 21+. Boot 3.5 docs khuyến nghị Java 24+ để có trải nghiệm virtual-thread tốt hơn; Boot 4 tiếp tục hỗ trợ (support / 지원). Pool-size properties có thể bị ignore, vì vậy downstream sức chứa (capacity / 용량) phải giới hạn bằng DB pool, Semaphore, tỷ lệ (rate / 비율) limit hoặc máy khách (client / 클라이언트) liên kết (connection / 연결) limit.

# 34. Boot 4.1 gRPC

Boot 4.1 có Spring gRPC hỗ trợ (support / 지원) và modules máy khách (client / 클라이언트)/máy chủ (server / 서버)/kiểm thử (test / 테스트). Starter giúp wiring/cấu hình (config / 설정) nhưng giao thức (protocol / 프로토콜) deadline, thử lại (retry / 재시도), streaming, auth và khả năng quan sát (observability / 관측 가능성) vẫn là architectural responsibility.

# 35. Boot 4.1 SSRF mitigation

Boot 4.1 highlight HTTP máy khách (client / 클라이언트) SSRF mitigation qua `InetAddressFilter`. Đây là guardrail cho server-side fetch; complete defense vẫn cần scheme/host/redirect/DNS/private-range chính sách (policy / 정책) phù hợp threat mô hình (model / 모델).

# 36. Boot 4.1 khả năng quan sát (observability / 관측 가능성)

Boot 4.1 tiếp tục cải thiện OpenTelemetry và observation/chỉ số (metric / 지표) conventions. Khi upgrade, custom instrumentation viết theo tutorial cũ có thể duplicate spans/metrics. Ưu tiên Boot-managed tích hợp (integration / 통합) rồi customize qua documented extension points.

# 37. Spring bảo mật (security / 보안) 6.5 → 7.x

Bảo mật (security / 보안) 6.5 là preparation line cho bảo mật (security / 보안) 7. hiện tại (current / 현재) docs tại thời điểm cập nhật có stable 7.1.1, 7.0.7, 6.5.11. bảo mật (security / 보안) 7 remove deprecated APIs và di chuyển (migration / 마이그레이션) còn liên quan Jackson 3/bảo mật (security / 보안) serialization. Với Boot, dùng Boot-managed phiên bản (version / 버전) trừ khi override có lý do rõ.

# 38. AOT Processing

Spring AOT precomputes/generates siêu dữ liệu (metadata / 메타데이터)/mã (code / 코드)/hints mà thời gian chạy (runtime / 런타임) trước đây discover dynamically. động (dynamic / 동적) reflection/tài nguyên (resource / 자원)/proxy hành vi (behavior / 동작) khó infer cần tường minh (explicit / 명시적) hints. thư viện (library / 라이브러리) claim AOT/bản địa (native / 네이티브) hỗ trợ (support / 지원) phải kiểm thử (test / 테스트) both JVM normal chế độ (mode / 모드) và bản địa (native / 네이티브) đường dẫn (path / 경로).

# 39. RuntimeHints

`RuntimeHints` đăng ký reflection/resources/serialization/proxies. Chỉ register năng lực (capability / 역량) thật cần; blanket reflection registration làm bản địa (native / 네이티브) ảnh (image / 이미지) lớn và che thiết kế (design / 설계) issue. kiểm thử (test / 테스트) actual bản địa (native / 네이티브) executable cho trọng yếu (critical / 중요) paths.

# 40. bản địa (native / 네이티브) ảnh (image / 이미지)

Boot 4.1 supported bản địa (native / 네이티브) luồng (flow / 흐름) yêu cầu GraalVM 25+. bản địa (native / 네이티브) ảnh (image / 이미지) thường tốt startup/RSS; JVM JIT có thể tốt peak thông lượng (throughput / 처리량). khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) mã (code / 코드) cần tránh uncontrolled động (dynamic / 동적) nạp lớp (class loading / 클래스 로딩) và reflection không hinted.

# 41. CRaC / JVM checkpoint restore awareness

Spring khung phần mềm (framework / 프레임워크) tham chiếu (reference / 참조) có JVM Checkpoint Restore tích hợp (integration / 통합). Checkpoint/restore là startup mô hình (model / 모델) khác bản địa (native / 네이티브) ảnh (image / 이미지): warm JVM trạng thái (state / 상태) được checkpoint rồi restore. Sockets, threads, random/crypto trạng thái (state / 상태) và bên ngoài (external / 외부) connections cần vòng đời (lifecycle / 생명주기) around checkpoint. Đây là specialized năng lực (capability / 역량), không phải default.

# 42. ứng dụng (application / 애플리케이션) startup instrumentation

Spring `ApplicationStartup`/Boot startup tooling giúp phân rã startup chi phí (cost / 비용). Nếu di chuyển (migration / 마이그레이션) DB chiếm 70% startup, tối ưu thành phần (component / 컴포넌트) scan sẽ không giải quyết nhiều. Luôn instrument trước.

# 43. Preview: khung phần mềm (framework / 프레임워크) 7.1 / Boot 4.2

Official docs hiện liệt kê khung phần mềm (framework / 프레임워크) 7.1.0-M1 và Boot 4.2.0-M1 là preview. Đọc để biết direction nhưng không expose preview types trong stable công khai (public / 공개) APIs và không viết môi trường vận hành (production / 운영 환경) guidance như thể milestone đã final.

# 44. phụ thuộc (dependency / 의존성) override chính sách (policy / 정책)

Default: để Boot quản lý versions. Override khi có bảo mật (security / 보안) fix, vendor tính tương thích (compatibility / 호환성), required tính năng (feature / 기능) hoặc known bug fix, và phải kiểm thử (test / 테스트) ma trận (matrix / 행렬). nền tảng (platform / 플랫폼) coherence quan trọng hơn newest sản phẩm tạo ra (artifact / 산출물) number.

<!-- SPRING_BATCH5_VERSION_MASTER -->

> **Chuyển mạch:** Source trace của Spring Security và TestContext chỉ ra behavior cần giữ; migration graph 2.7/5.3 → 3.5/6.2 → 4.1/7.0 dùng các mốc đó để đối chiếu compatibility và failure khi nâng phiên bản.

## Di chuyển (migration / 마이그레이션) đồ thị (graph / 그래프): 2.7/5.3 → 3.5/6.2 → 4.1/7.0

Di chuyển (migration / 마이그레이션) nên được xem như chuỗi tính tương thích (compatibility / 호환성) boundaries. Từ Boot 2.7 lên generation 3, ranh giới (boundary / 경계) lớn là Java 17 + Jakarta không gian tên (namespace / 네임스페이스) + portfolio major versions; hãy loại deprecated APIs ở latest 2.7 trước, cập nhật (update / 업데이트) libraries tới bản Jakarta-compatible rồi mới đổi major. Từ Boot 3 lên 4, official chiến lược (strategy / 전략) vẫn nên đưa ứng dụng (application / 애플리케이션) lên latest 3.5 trước để warnings/deprecations hiện rõ, sau đó mới xử lý Boot 4 modular starter đồ thị (graph / 그래프), khung phần mềm (framework / 프레임워크) 7, Jackson 3, bảo mật (security / 보안) 7 và test-module changes.

Đừng migrate bằng cách chỉnh phiên bản (version / 버전) rồi sửa compile errors cho tới khi xanh. Một upgrade ma trận (matrix / 행렬) phải kiểm thử (test / 테스트) startup/auto-config, HTTP serialization, bảo mật (security / 보안) authentication/authorization, cơ sở dữ liệu (database / 데이터베이스) migrations/JPA queries, giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백) hành vi (behavior / 동작), scheduled/async công việc (work / 작업), khả năng quan sát (observability / 관측 가능성) agents/exporters và packaging/bản địa (native / 네이티브) đường dẫn (path / 경로) nếu có. nhị phân (binary / 이진) linkage errors sau deploy thường là dấu hiệu thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) khác đồ thị (graph / 그래프) compile, vì vậy inspect packaged sản phẩm tạo ra (artifact / 산출물)/BOM resolution.

Tại thời điểm cập nhật này, baseline stable của bộ ghi chú (note / 노트) là Boot 4.1.1 + khung phần mềm (framework / 프레임워크) 7.0.9. Boot docs vẫn liệt kê 3.5.16 như maintenance line quan trọng. khung phần mềm (framework / 프레임워크) 7.1.0-M1 và Boot 4.2.0-M1 vẫn preview. Spring bảo mật (security / 보안) docs liệt kê 7.1.1 là latest stable, cùng maintenance 7.0.7 và 6.5.11; bảo mật (security / 보안) 7.2.0-M1 là preview. Preview chỉ dùng để theo dõi direction, không được viết thành môi trường vận hành (production / 운영 환경) baseline.
<!-- SPRING_BATCH5_VERSION_MASTER_END -->

---

# 45. Source-reading roadmap

Mục này biến kiến thức backend thành tiêu chí kiểm tra và quyết định triển khai. Hãy xác định contract, failure mode, evidence và cách rollback trước khi áp dụng.

```text
1. DefaultListableBeanFactory / AbstractBeanFactory
2. AbstractAutowireCapableBeanFactory
3. ConfigurationClassPostProcessor
4. AutowiredAnnotationBeanPostProcessor
5. AbstractAutoProxyCreator
6. ProxyFactory / AdvisedSupport
7. TransactionInterceptor
8. TransactionSynchronizationManager
9. DispatcherServlet
10. RequestMappingHandlerMapping
11. RequestMappingHandlerAdapter
12. TestContext Framework
13. Boot auto-configuration conditions/imports
14. AOT RuntimeHints
```

Đọc từng luồng (flow / 흐름) với debugger/minimal mẫu (sample / 표본); không đọc nguồn (source / 소스) linearly như tiểu thuyết.

# 46. Lab: dấu vết (trace / 추적) transactional proxy

Tạo dịch vụ (service / 서비스) `@Transactional`, inspect thời gian chạy (runtime / 런타임) lớp (class / 클래스)/advisors, breakpoint TransactionInterceptor, so sánh bên ngoài (external / 외부) lời gọi (call / 호출) và self-invocation. Sau đó thử giao diện (interface / 인터페이스) vs target-class proxy và khung phần mềm (framework / 프레임워크) 7 `@Proxyable` trong lab.

# 47. Lab: custom Boot 4 starter

Tạo `@AutoConfiguration` + `@ConditionalOnClass` + `@EnableConfigurationProperties` + `@ConditionalOnMissingBean`. Register qua Boot auto-configuration imports. kiểm thử (test / 테스트) bằng ApplicationContextRunner cho positive/negative/back-off cases.

# 48. Lab: khung phần mềm (framework / 프레임워크) 7 API versioning

Configure header-based API phiên bản (version / 버전), mappings v1/v2, missing/unsupported phiên bản (version / 버전) và deprecation/sunset hành vi (behavior / 동작). Sau đó configure RestClient yêu cầu (request / 요청)/default API phiên bản (version / 버전) để hiểu máy chủ (server / 서버)/máy khách (client / 클라이언트) symmetry.

# 49. Lab: JSpecify

Dùng `@NullMarked` ở gói (package / 패키지), `@Nullable` cho generic element/return và static analyzer/IDE. Quan sát khác biệt so Spring null annotations legacy.

# 50. Lab: Boot 3.5 → 4.1

Mẫu (sample / 표본) phải có MVC, JPA, bảo mật (security / 보안), Flyway và tests. Upgrade, ghi lại starter names, Jackson custom mã (code / 코드), kiểm thử (test / 테스트) dependencies, bảo mật (security / 보안) changes, nullability warnings và third-party tính tương thích (compatibility / 호환성). Đây là bài tập versioning thực tế hơn việc học changelog.

# 51. phiên bản (version / 버전) snapshot — 2026-09-21

Mục này biến kiến thức backend thành tiêu chí kiểm tra và quyết định triển khai. Hãy xác định contract, failure mode, evidence và cách rollback trước khi áp dụng.

```text
Stable current:
Spring Boot 4.1.1
Spring Framework 7.0.9
Java 17 minimum, Java 26 compatible
Servlet 6.1
Tomcat 11.0.x / Jetty 12.1.x
GraalVM 25+

Important 3.x maintenance:
Spring Boot 3.5.16
Spring Framework 6.2.19+
Java 17 minimum, Java 25 compatible
Servlet 6.0 generation

Preview:
Spring Boot 4.2.0-M1
Spring Framework 7.1.0-M1

Spring Security current stable lines in docs:
7.1.1 / 7.0.7 / 6.5.11
```

Snapshot phải được re-check trước môi trường vận hành (production / 운영 환경) upgrade vì patch/minor versions thay đổi liên tục.

# 52. Khi nào có thể nói Master Spring?

Dấu hiệu không phải thuộc lớp (class / 클래스) names, mà là khi symptom xuất hiện bạn biết đúng tầng (layer / 계층): bean missing → definitions/conditions; annotation advice missing → proxy/advisor/lời gọi (call / 호출) đường dẫn (path / 경로); giao dịch (transaction / 트랜잭션) strange → tài nguyên (resource / 자원)/ngữ cảnh (context / 맥락); MVC binding strange → ánh xạ (mapping / 매핑)/resolver/converter; Boot phụ thuộc (dependency / 의존성) strange → mô-đun (module / 모듈)/starter/nền tảng (platform / 플랫폼); bản địa (native / 네이티브) thất bại (fail / 실패) → reflection/resources/proxy hints; upgrade thất bại (fail / 실패) → di chuyển (migration / 마이그레이션) guide/deprecated APIs/nhị phân (binary / 이진) đồ thị (graph / 그래프).

Khi bạn đi được từ symptom → subsystem → nguồn (source / 소스)/docs → minimal reproduction → fix, Spring không còn là magic.

# 53. Nguồn version-sensitive

Spring Boot hệ thống (system / 시스템) Requirements
https://docs.spring.io/spring-boot/system-requirements.html

Spring Boot phụ thuộc (dependency / 의존성) Versions
https://docs.spring.io/spring-boot/appendix/dependency-versions/

Spring Boot 4 di chuyển (migration / 마이그레이션) Guide
https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Spring khung phần mềm (framework / 프레임워크) tham chiếu (reference / 참조)
https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/

Spring khung phần mềm (framework / 프레임워크) Null an toàn (safety / 안전)
https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/cốt lõi (core / 핵심)/null-safety.html

Spring MVC API Versioning
https://docs.spring.io/spring-framework/tham chiếu (reference / 참조)/web/webmvc-versioning.html

Spring bảo mật (security / 보안) tham chiếu (reference / 참조)
https://docs.spring.io/spring-security/tham chiếu (reference / 참조)/

> **Bàn giao:** Sau **Di chuyển (migration / 마이그레이션) đồ thị (graph / 그래프): 2.7/5.3 → 3.5/6.2 → 4.1/7.0**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

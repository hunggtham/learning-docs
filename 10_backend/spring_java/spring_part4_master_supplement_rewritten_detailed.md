# Java Spring — Part 4: Master Supplement — Rewritten Detailed
## Spring Framework 7 / Spring Boot 4 internals, framework authoring, AOT và version evolution

> Đây là phần thứ tư của lộ trình **Beginner → Intermediate → Senior → Master Supplement**. Ba phần đầu tập trung vào xây application và production engineering. Master Supplement tập trung vào Spring như một framework: container source flow, auto-proxy creation, transaction interception, MVC dispatch internals, Boot auto-configuration, TestContext, custom starters, AOT/runtime hints, null-safety và major-version migration. Baseline stable là **Spring Boot 4.1.1 + Spring Framework 7.0.9**; Boot 4.2.0-M1 / Framework 7.1.0-M1 chỉ là preview.

---

# 1. Version matrix dành cho Master

| Generation | Spring Boot | Spring Framework | Java baseline | Web/Jakarta generation | Vai trò |
|---|---|---|---|---|---|
| Legacy | 2.7.x | 5.3.x | Java 8+ | `javax.*` | maintain code cũ |
| Modern 3.x | 3.5.16 | 6.2.19+ | Java 17+ | Jakarta / Servlet 6.0 | migration bridge |
| Current stable | 4.1.1 | 7.0.9+ | Java 17–26 | Jakarta EE 11 / Servlet 6.1 | baseline tài liệu |
| Current preview | 4.2.0-M1 | 7.1.0-M1+ | Java 17–26 | preview | theo dõi direction |

Một Master Spring engineer cần nghĩ version như một **dependency platform**. Boot quản lý một tested dependency set gồm Framework, Security, Data và nhiều third-party libraries. Vì vậy “override một artifact lên version mới hơn” không tự động là upgrade tốt hơn; platform coherence thường quan trọng hơn newest-number-per-library.

# 2. Đọc Spring source theo pipeline

Spring source quá lớn để đọc ngẫu nhiên. Hãy trace một câu hỏi cụ thể, ví dụ “một `@Service` transactional trở thành proxy bằng cách nào?” rồi đi theo flow:

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

Cách đọc này giúp mỗi class có vị trí rõ thay vì trở thành hàng nghìn dòng source rời rạc.

# 3. `DefaultListableBeanFactory`

`DefaultListableBeanFactory` là implementation trung tâm quản lý BeanDefinitions, singleton registry và dependency resolution trong common ApplicationContext. Nó xử lý aliases, factory methods, scopes, generic types, qualifiers, primary/fallback candidates, FactoryBeans và type queries. Khi debug missing/wrong bean, hãy tách hai câu hỏi: metadata candidate nào tồn tại, và final runtime object nào được expose sau lifecycle/proxying.

# 4. Singleton registry và early references

Spring có machinery cho singleton creation state và một số early references để xử lý historical setter/field circular dependencies. Điều này trở nên khó hơn khi auto-proxying tham gia vì reference sớm và final proxy không được mâu thuẫn. Dù framework có thể giải một số cycle, application không nên dựa vào circular dependency như design feature; cycle thường là tín hiệu boundary sai.

<!-- SPRING_BATCH1_IOC_MASTER -->
## Source trace: từ `getBean()` tới `doCreateBean()` và final exposed reference

Khi muốn đọc Spring source thay vì chỉ dùng API, một trace có giá trị là bắt đầu từ `AbstractBeanFactory#doGetBean`. Lookup trước hết kiểm tra singleton cache; nếu chưa có instance, framework lấy merged BeanDefinition, bảo đảm dependencies cần tạo trước, rồi đi vào creation path phù hợp scope. Với singleton, singleton registry kiểm soát “create once” semantics và trạng thái currently-in-creation để phát hiện cycle.

`AbstractAutowireCapableBeanFactory#createBean` và `doCreateBean` là nơi object creation pipeline trở nên rõ. Framework có cơ hội resolve class, cho `InstantiationAwareBeanPostProcessor` can thiệp trước instantiation, chọn constructor/factory method, instantiate bean, populate properties/injection points, chạy initialization callbacks rồi apply post-processors. Auto-proxy creator thường thay final exposed reference ở cuối lifecycle bằng proxy.

Circular-reference support làm pipeline phức tạp vì framework có thể đăng ký một **singleton factory cho early reference** trước khi bean hoàn tất initialization. `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference` cho phép auto-proxy infrastructure bảo đảm early reference tương thích với object sẽ được expose cuối. Đây là mechanism để hiểu source, không phải invitation xây graph dựa vào circular references.

Khi đọc source, đừng biến tên method nội bộ thành public contract. Contract mà application có thể dựa vào nằm ở documented container semantics, lifecycle interfaces và API reference. Tên helper hoặc ordering implementation có thể đổi giữa Framework versions. Mastery là dùng internals để giải thích behavior, rồi quay lại public contract để thiết kế code ổn định.
<!-- SPRING_BATCH1_IOC_MASTER_END -->

---

# 5. `ConfigurationClassPostProcessor`

`@Configuration`, `@ComponentScan`, `@Import` và `@Bean` chỉ là metadata cho tới khi Spring parse chúng. `ConfigurationClassPostProcessor` chạy ở BeanFactory post-processing phase và mở rộng root configuration thành một graph definitions/imports/components. Khi startup có missing/duplicate definitions, hãy trace metadata expansion thay vì chỉ nhìn constructor injection.

# 6. `@Configuration` và explicit bean parameters

Full configuration classes historically có enhancement để direct calls giữa `@Bean` methods giữ container semantics. Tuy nhiên:

```java
@Bean
Client client(Auth auth) {
    return new Client(auth);
}
```

rõ hơn việc gọi `auth()` trực tiếp từ bean method. Mastery thường dẫn tới code ít phụ thuộc framework interception hơn, không phải nhiều magic hơn.

# 7. `AutowiredAnnotationBeanPostProcessor`

Constructor/field/method injection annotations cần infrastructure đọc metadata rồi resolve dependency qua BeanFactory. `AutowiredAnnotationBeanPostProcessor` là một component quan trọng của flow này. Constructor injection có lợi vì required dependencies được resolve trước construction và type system nhìn thấy chúng; field injection phụ thuộc nhiều hơn vào post-construction mutation/reflection.

# 8. BeanPostProcessor ordering và early-instantiation hazard

Nếu custom post-processor inject ordinary application beans quá sớm, application bean có thể được tạo trước khi toàn bộ processors/auto-proxy creators sẵn sàng. Log kiểu “not eligible for getting processed by all BeanPostProcessors” thường là tín hiệu này. Infrastructure nên giữ dependency graph tối thiểu và tránh kéo business beans vào lifecycle phase quá sớm.

# 9. `AbstractAutoProxyCreator`

Auto-proxy creator không proxy mọi bean. Nó tìm Advisors/interceptors phù hợp với bean/method. Nếu không có advisor, original bean được trả. Nếu có, framework build proxy và final bean reference trong context là proxy. Vì vậy annotation advice không chạy có thể do advisor không match, bean không được proxy hoặc call bypass proxy.

# 10. `ProxyFactory`, `AdvisedSupport` và interceptor chain

Proxy giữ target + advisors. Runtime call conceptually:

```text
proxy
→ security interceptor
→ observation interceptor
→ transaction interceptor
→ target
```

Around interceptor có thể không gọi target, ví dụ cache hit hoặc authorization failure. Ordering do đó là semantics, không phải style.

# 11. Spring 7 `@Proxyable`

Framework 7 thêm `@Proxyable` để gợi ý proxy type per bean, có thể chọn interface-based JDK proxy hoặc target-class CGLIB proxy. Annotation chỉ ảnh hưởng bean **khi auto-proxying thực sự xảy ra**; nó không tự tạo proxy. Đây là advanced migration/infrastructure tool, không phải annotation cần đặt lên mọi service.

# 12. Transaction source flow

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

Transaction interceptor không trực tiếp biết JDBC/JPA implementation; nó đi qua transaction-manager abstraction.

# 13. `TransactionSynchronizationManager`

Imperative transaction infrastructure cần bind resources/context với current execution thread: connection/session, transaction active/read-only/name/isolation và synchronization callbacks. `TransactionSynchronizationManager` là infrastructure trung tâm cho kiểu binding này. Business code hiếm khi nên gọi trực tiếp, nhưng hiểu nó giải thích vì sao spawn thread mới không tự mang imperative transaction theo.

# 14. Self-invocation nhìn từ proxy internals

External call đi `caller → proxy → interceptor → target`. Internal `this.otherMethod()` chỉ là Java call trên target và không quay lại proxy. Vì vậy transaction/cache/security/async advice có thể bị bypass. Đây là consequence của proxy-based AOP, không phải bug riêng `@Transactional`.

# 15. `DispatcherServlet` source flow

High level:

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

`DispatcherServlet` là Front Controller phối hợp strategy interfaces thay vì hard-code mọi handler model.

# 16. `RequestMappingHandlerMapping`

Annotated mappings được đăng ký theo path, HTTP method, params, headers, consumes/produces và ở Framework 7 còn có API-version semantics. Ambiguous route là conflict trong mapping registry, không phải DispatcherServlet ngẫu nhiên chọn sai.

# 17. `RequestMappingHandlerAdapter`

Adapter phối hợp argument resolvers, return-value handlers, conversion/binding, validation, async support và message converters để invoke annotated method. Custom extension nên giữ web-boundary concern; đừng giấu heavy business I/O trong argument resolver.

# 18. Framework 7 API Versioning

Framework 7 có `ApiVersionStrategy`, resolver/parser/validation/deprecation handler abstractions. MVC/WebFlux mappings có thể khai báo API version; RestClient/WebClient/HTTP Service clients cũng có version insertion support. Framework giải mechanics, còn product vẫn phải quyết định compatibility/deprecation/sunset policy.

# 19. Jackson 3 generation

Boot 4 ưu tiên Jackson 3. Code chỉ dùng DTO + Boot auto-config thường migrate dễ. Code custom mapper/modules/polymorphic serialization phải review package changes và behavioral compatibility. `spring-boot-jackson2` tồn tại như deprecated stop-gap, không phải long-term target.

# 20. Spring TestContext Framework

TestContext quản lý context loading, caching, listeners, DI, test transactions và bean overrides. Suite chậm thường do nhiều unique context configurations/profiles/mock combinations làm cache reuse kém. Master nên đo context fragmentation trước khi kết luận “Spring test chậm”.

# 21. Bean override infrastructure từ Framework 6.2

Framework 6.2 có `@TestBean`, `@MockitoBean`, `@MockitoSpyBean` trên explicit bean-override infrastructure. Đây là hướng hiện đại hơn global bean-definition overriding. Legacy tutorials vẫn dùng `@MockBean`; đọc được nhưng code mới trên 6.2/7.x nên hiểu current mechanism.

# 22. Boot 4 test modularization

Boot 4 tách test infrastructure theo technology, với pattern `spring-boot-starter-<technology>-test`. Migration phải review test dependencies riêng. Security/GraphQL/JDBC/JPA tests có thể cần dedicated test starter thay vì vô tình dựa vào transitive classpath của Boot 3.

# 23. Auto-configuration discovery

Modern Boot khai báo auto-configurations qua metadata `META-INF/spring/...AutoConfiguration.imports` thay vì broad component scanning. Boot load candidates, evaluate conditions rồi import. Custom starter nên explicit, back-off friendly và không scan consumer package tùy tiện.

# 24. Conditions như executable configuration graph

`@ConditionalOnClass`, `@ConditionalOnMissingBean`, `@ConditionalOnProperty`, `@ConditionalOnWebApplication` tạo boolean graph. Timing quan trọng: missing-bean condition chỉ thấy definitions đã biết ở phase đó. Auto-config ordering chỉ nên dùng khi dependency thực sự tồn tại và phải có tests.

# 25. Condition Evaluation Report và `ApplicationContextRunner`

Khi auto-config không match, condition report cho biết lý do. Custom starter nên test dependency present/absent, property on/off và custom-bean back-off. `ApplicationContextRunner` rất hữu ích vì tạo context nhỏ, nhanh và inspectable.

# 26. `@ConfigurationProperties` như public API

Starter properties có prefix, type, defaults, validation và metadata. Rename property là configuration API change. Library author nên provide deprecation/migration metadata khi có thể, không coi YAML key là implementation detail.

# 27. Boot 4 modular starter model

Migration guide mapping điển hình:

```text
spring-boot-starter-web
→ spring-boot-starter-webmvc

spring-boot-starter-oauth2-client
→ spring-boot-starter-security-oauth2-client

spring-boot-starter-oauth2-resource-server
→ spring-boot-starter-security-oauth2-resource-server
```

Flyway/Liquibase cũng có dedicated Boot starters trong Boot 4 model. Supporting Boot 3 và Boot 4 trong cùng custom starter artifact bị khuyến nghị thận trọng vì package/module graph khác đáng kể.

# 28. `spring-boot-starter-classic` migration bridge

Boot 4 cung cấp classic starter để tái tạo broader classpath tạm thời. Migration có thể đi `Boot 3.5 → Boot 4 + classic → fix imports/deps → remove classic → dedicated starters`. Classic là aid, không phải final architecture.

# 29. JSpecify trong Framework 7

Framework 7 annotate APIs bằng JSpecify. `@NullMarked` cho non-null default; type-use `@Nullable` biểu diễn nullable chính xác trong generics/arrays/nested types. Các Spring null annotations cũ trong `org.springframework.lang` được deprecate theo hướng JSpecify. Java static analysis và Kotlin interoperability vì vậy thay đổi thực tế khi upgrade.

# 30. `Nullness` runtime API

Framework 7 có `org.springframework.core.Nullness` để framework code inspect nullness của field/method parameter/type usage. Static checking vẫn là giá trị chính; runtime API dành cho dynamic framework/binding logic.

# 31. `RestClient` version evolution

`RestClient` xuất hiện từ Framework 6.1. Framework 7 mở rộng client infrastructure và API-version integration. Domain/application API nên expose gateway contract, không expose RestClient như business abstraction.

# 32. `JdbcClient` version evolution

`JdbcClient` cũng từ 6.1 và delegate xuống JdbcTemplate/NamedParameterJdbcTemplate. Simple query/update có thể dùng fluent client; batch/stored-procedure/complex callbacks vẫn phù hợp lower-level templates.

# 33. Virtual Threads từ Boot 3.2

`spring.threads.virtual.enabled=true` xuất hiện từ Boot 3.2 cho Java 21+. Boot 3.5 docs khuyến nghị Java 24+ để có trải nghiệm virtual-thread tốt hơn; Boot 4 tiếp tục support. Pool-size properties có thể bị ignore, vì vậy downstream capacity phải giới hạn bằng DB pool, Semaphore, rate limit hoặc client connection limit.

# 34. Boot 4.1 gRPC

Boot 4.1 có Spring gRPC support và modules client/server/test. Starter giúp wiring/config nhưng protocol deadline, retry, streaming, auth và observability vẫn là architectural responsibility.

# 35. Boot 4.1 SSRF mitigation

Boot 4.1 highlight HTTP client SSRF mitigation qua `InetAddressFilter`. Đây là guardrail cho server-side fetch; complete defense vẫn cần scheme/host/redirect/DNS/private-range policy phù hợp threat model.

# 36. Boot 4.1 observability

Boot 4.1 tiếp tục cải thiện OpenTelemetry và observation/metric conventions. Khi upgrade, custom instrumentation viết theo tutorial cũ có thể duplicate spans/metrics. Ưu tiên Boot-managed integration rồi customize qua documented extension points.

# 37. Spring Security 6.5 → 7.x

Security 6.5 là preparation line cho Security 7. Current docs tại thời điểm cập nhật có stable 7.1.1, 7.0.7, 6.5.11. Security 7 remove deprecated APIs và migration còn liên quan Jackson 3/security serialization. Với Boot, dùng Boot-managed version trừ khi override có lý do rõ.

# 38. AOT Processing

Spring AOT precomputes/generates metadata/code/hints mà runtime trước đây discover dynamically. Dynamic reflection/resource/proxy behavior khó infer cần explicit hints. Library claim AOT/native support phải test both JVM normal mode và native path.

# 39. RuntimeHints

`RuntimeHints` đăng ký reflection/resources/serialization/proxies. Chỉ register capability thật cần; blanket reflection registration làm native image lớn và che design issue. Test actual native executable cho critical paths.

# 40. Native Image

Boot 4.1 supported native flow yêu cầu GraalVM 25+. Native image thường tốt startup/RSS; JVM JIT có thể tốt peak throughput. Framework/library code cần tránh uncontrolled dynamic class loading và reflection không hinted.

# 41. CRaC / JVM checkpoint restore awareness

Spring Framework reference có JVM Checkpoint Restore integration. Checkpoint/restore là startup model khác native image: warm JVM state được checkpoint rồi restore. Sockets, threads, random/crypto state và external connections cần lifecycle around checkpoint. Đây là specialized capability, không phải default.

# 42. Application startup instrumentation

Spring `ApplicationStartup`/Boot startup tooling giúp phân rã startup cost. Nếu migration DB chiếm 70% startup, tối ưu component scan sẽ không giải quyết nhiều. Luôn instrument trước.

# 43. Preview: Framework 7.1 / Boot 4.2

Official docs hiện liệt kê Framework 7.1.0-M1 và Boot 4.2.0-M1 là preview. Đọc để biết direction nhưng không expose preview types trong stable public APIs và không viết production guidance như thể milestone đã final.

# 44. Dependency override policy

Default: để Boot quản lý versions. Override khi có security fix, vendor compatibility, required feature hoặc known bug fix, và phải test matrix. Platform coherence quan trọng hơn newest artifact number.

# 45. Source-reading roadmap

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

Đọc từng flow với debugger/minimal sample; không đọc source linearly như tiểu thuyết.

# 46. Lab: trace transactional proxy

Tạo service `@Transactional`, inspect runtime class/advisors, breakpoint TransactionInterceptor, so sánh external call và self-invocation. Sau đó thử interface vs target-class proxy và Framework 7 `@Proxyable` trong lab.

# 47. Lab: custom Boot 4 starter

Tạo `@AutoConfiguration` + `@ConditionalOnClass` + `@EnableConfigurationProperties` + `@ConditionalOnMissingBean`. Register qua Boot auto-configuration imports. Test bằng ApplicationContextRunner cho positive/negative/back-off cases.

# 48. Lab: Framework 7 API versioning

Configure header-based API version, mappings v1/v2, missing/unsupported version và deprecation/sunset behavior. Sau đó configure RestClient request/default API version để hiểu server/client symmetry.

# 49. Lab: JSpecify

Dùng `@NullMarked` ở package, `@Nullable` cho generic element/return và static analyzer/IDE. Quan sát khác biệt so Spring null annotations legacy.

# 50. Lab: Boot 3.5 → 4.1

Sample phải có MVC, JPA, Security, Flyway và tests. Upgrade, ghi lại starter names, Jackson custom code, test dependencies, Security changes, nullability warnings và third-party compatibility. Đây là bài tập versioning thực tế hơn việc học changelog.

# 51. Version snapshot — 2026-09-12

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

Snapshot phải được re-check trước production upgrade vì patch/minor versions thay đổi liên tục.

# 52. Khi nào có thể nói Master Spring?

Dấu hiệu không phải thuộc class names, mà là khi symptom xuất hiện bạn biết đúng layer: bean missing → definitions/conditions; annotation advice missing → proxy/advisor/call path; transaction strange → resource/context; MVC binding strange → mapping/resolver/converter; Boot dependency strange → module/starter/platform; native fail → reflection/resources/proxy hints; upgrade fail → migration guide/deprecated APIs/binary graph.

Khi bạn đi được từ symptom → subsystem → source/docs → minimal reproduction → fix, Spring không còn là magic.

# 53. Nguồn version-sensitive

Spring Boot System Requirements  
https://docs.spring.io/spring-boot/system-requirements.html

Spring Boot Dependency Versions  
https://docs.spring.io/spring-boot/appendix/dependency-versions/

Spring Boot 4 Migration Guide  
https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide

Spring Framework Reference  
https://docs.spring.io/spring-framework/reference/

Spring Framework Null Safety  
https://docs.spring.io/spring-framework/reference/core/null-safety.html

Spring MVC API Versioning  
https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html

Spring Security Reference  
https://docs.spring.io/spring-security/reference/

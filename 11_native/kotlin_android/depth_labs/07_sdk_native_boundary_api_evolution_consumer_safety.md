# Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)

> **Mạch đọc:** Đặt **độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. API công khai (public API / 공개 API) là đặc tả hợp đồng (contract / 계약), không chỉ là công khai (public / 공개) từ khóa (keyword / 키워드)** sang **2. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) khác nhau**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi viết ứng dụng (application / 애플리케이션) mã (code / 코드), nhóm (team / 팀) kiểm soát hầu hết lời gọi (call / 호출) site. Khi viết Android thư viện (library / 라이브러리) hoặc SDK, mã (code / 코드) của bạn chạy bên trong tiến trình (process / 프로세스) của **người khác**, dưới hệ thống dựng (build system / 빌드 시스템), phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), vòng đời (lifecycle / 생명주기), shrinker và bản phát hành (release / 릴리스) cadence của **người khác**. Vì vậy SDK authoring đòi hỏi discipline cao hơn: API công khai (public API / 공개 API) phải ổn định, phụ thuộc (dependency / 의존성) không được gây xung đột, initialization không được làm chậm app host, bản địa (native / 네이티브) mã (code / 코드) không được phá ABI, và thất bại (failure / 실패) không được kéo cả tiến trình (process / 프로세스) bên tiêu thụ (consumer / 소비자) xuống theo.

Độ sâu (depth / 깊이) Lab này đào sâu cách thiết kế thư viện (library / 라이브러리)/SDK như một long-lived đặc tả hợp đồng (contract / 계약).

---

## 1. API công khai (public API / 공개 API) là đặc tả hợp đồng (contract / 계약), không chỉ là `public` từ khóa (keyword / 키워드)

Một kiểu (type / 타입) công khai (public / 공개) trong bytecode có thể trở thành phụ thuộc (dependency / 의존성) của hàng trăm bên tiêu thụ (consumer / 소비자).

Sau khi bản phát hành (release / 릴리스):

```kotlin
class Client(
    val config: Config
)
```

Bên tiêu thụ (consumer / 소비자) có thể compile trực tiếp against constructor và thuộc tính (property / 속성) đó.

Nếu phiên bản (version / 버전) sau đổi:

```kotlin
class Client internal constructor(...)
```

Nguồn (source / 소스)/nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) có thể vỡ.

Công khai (public / 공개) surface phải nhỏ và có chủ ý ngay từ đầu.

---

## 2. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) khác nhau

Nguồn (source / 소스) tính tương thích (compatibility / 호환성) hỏi:

```text
consumer source cũ compile lại với library mới được không?
```

Nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) hỏi:

```text
consumer APK/module đã compile trước đó có chạy với binary library mới không?
```

Một thay đổi có thể source-compatible nhưng binary-incompatible hoặc ngược lại.

SDK môi trường vận hành (production / 운영 환경) cần hiểu cả hai nếu bên tiêu thụ (consumer / 소비자) có động (dynamic / 동적)/plugin/multi-module phân phối (distribution / 분포) hoặc phụ thuộc (dependency / 의존성) resolution phức tạp.

---

## 3. Kotlin default argument có ABI implications

Ví dụ:

```kotlin
fun login(
    username: String,
    timeoutMs: Long = 5_000
)
```

Kotlin trình biên dịch (compiler / 컴파일러) sinh helper/default machinery.

Java bên tiêu thụ (consumer / 소비자) không tự thấy default parameter như Kotlin.

Nếu SDK cần Java-friendly API, cân nhắc overload tường minh (explicit / 명시적) hoặc `@JvmOverloads` có chủ ý.

Đừng assume Kotlin ergonomics tự động map tốt sang Java ABI.

---

## 4. `@JvmName`, `@JvmField`, `@JvmStatic` thay đổi Java surface

Kotlin nguồn (source / 소스) đẹp có thể tạo Java lời gọi (call / 호출) site khó dùng.

Thư viện (library / 라이브러리) API công khai (public API / 공개 API) nên rà soát (review / 검토) từ cả Kotlin và Java nếu hỗ trợ (support / 지원) Java bên tiêu thụ (consumer / 소비자).

Ví dụ companion factory:

```kotlin
class Client private constructor(...) {
    companion object {
        @JvmStatic
        fun create(config: Config): Client = ...
    }
}
```

Java bên tiêu thụ (consumer / 소비자):

```java
Client.create(config);
```

API ergonomics là part của tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약).

---

## 5. Nullability annotation là đặc tả hợp đồng (contract / 계약) với Java bên tiêu thụ (consumer / 소비자)

Kotlin kiểu (type / 타입):

```kotlin
fun token(): String?
```

rõ nullability.

Java ranh giới (boundary / 경계) có thể mất một phần type-safety nếu annotation siêu dữ liệu (metadata / 메타데이터) không được preserve/understood.

SDK nên tránh ambiguous nền tảng (platform / 플랫폼) kiểu (type / 타입) trong API công khai (public API / 공개 API).

---

## 6. Expose giao diện (interface / 인터페이스), hide hiện thực (implementation / 구현) khi hiện thực (implementation / 구현) có thay đổi (change / 변경) axis lớn

Ví dụ:

```kotlin
interface AnalyticsClient {
    fun track(event: Event)
}
```

Hiện thực (implementation / 구현) mạng (network / 네트워크)/lưu trữ (storage / 저장소) có thể thay đổi mà bên tiêu thụ (consumer / 소비자) không biết.

Nhưng đừng tạo giao diện (interface / 인터페이스) cho mọi dữ liệu (data / 데이터) lớp (class / 클래스) vô cớ. lớp trừu tượng (abstraction / 추상화) cần bảo vệ một thay đổi (change / 변경) axis cụ thể.

---

## 7. công khai (public / 공개) mô hình (model / 모델) nên độc lập nội bộ (internal / 내부) vận chuyển (transport / 전송) mô hình (model / 모델)

Không expose Retrofit/Moshi/Room-specific kiểu (type / 타입) trong API nếu không muốn bên tiêu thụ (consumer / 소비자) phụ thuộc hiện thực (implementation / 구현).

Bad:

```kotlin
fun events(): Flow<List<EventEntity>>
```

nếu `EventEntity` là Room thực thể (entity / 엔터티) nội bộ.

Better:

```kotlin
fun events(): Flow<List<Event>>
```

Nội bộ (internal / 내부) lược đồ (schema / 스키마) có thể migrate mà công khai (public / 공개) đặc tả hợp đồng (contract / 계약) ổn định.

---

## 8. phụ thuộc (dependency / 의존성) leakage mở rộng tính tương thích (compatibility / 호환성) surface

Nếu công khai (public / 공개) phương thức (method / 메서드) trả kiểu (type / 타입) từ third-party thư viện (library / 라이브러리):

```kotlin
fun client(): okhttp3.OkHttpClient
```

SDK đã biến OkHttp phiên bản (version / 버전)/API thành part của công khai (public / 공개) đặc tả hợp đồng (contract / 계약).

Bên tiêu thụ (consumer / 소비자) có thể buộc phụ thuộc (dependency / 의존성) phiên bản (version / 버전) theo SDK hoặc gặp xung đột (conflict / 충돌).

Expose third-party kiểu (type / 타입) chỉ khi đó là intentional tích hợp (integration / 통합) surface.

---

## 9. `api` phụ thuộc (dependency / 의존성) có thể leak transitive surface

Thư viện (library / 라이브러리) dùng Gradle `api(...)` khiến bên tiêu thụ (consumer / 소비자) compile thấy phụ thuộc (dependency / 의존성) đó.

`implementation(...)` giữ phụ thuộc (dependency / 의존성) private hơn.

Chọn `api` khi công khai (public / 공개) ABI thực sự cần, không vì bản dựng (build / 빌드) fix nhanh.

---

## 10. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) là bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전) bài toán (problem / 문제)

SDK A cần thư viện (library / 라이브러리) X v1, app cần X v2.

Nếu nhị phân (binary / 이진) incompatible, thời gian chạy (runtime / 런타임) có thể crash:

```text
NoSuchMethodError
ClassNotFoundException
VerifyError
```

SDK nên giảm phụ thuộc (dependency / 의존성) footprint, tránh pin phiên bản (version / 버전) cứng không cần thiết và kiểm thử (test / 테스트) với representative bên tiêu thụ (consumer / 소비자) đồ thị (graph / 그래프).

---

## 11. Shading/relocation đôi khi cần nhưng có chi phí (cost / 비용)

Nếu SDK buộc dùng phụ thuộc (dependency / 의존성) dễ xung đột (conflict / 충돌), có thể relocate gói (package / 패키지) bằng shading.

Nhưng shading:

- tăng sản phẩm tạo ra (artifact / 산출물) kích thước (size / 크기),
- complicate license/bảo mật (security / 보안) updates,
- có thể break reflection/tài nguyên (resource / 자원) loading.

Dùng khi xung đột (conflict / 충돌) rủi ro (risk / 위험) thật, không mặc định.

---

## 12. Android tài nguyên (resource / 자원) cũng là công khai (public / 공개) surface

AAR có thể đóng góp:

```text
layout
drawable
string
style
attr
```

Tài nguyên (resource / 자원) name collision với app/SDK khác có thể xảy ra.

Prefix tài nguyên (resource / 자원):

```text
my_sdk_*
```

là practice hữu ích cho thư viện (library / 라이브러리) lớn.

---

## 13. Manifest contribution phải tối thiểu

SDK auto-add:

```text
permission
service
receiver
provider
metadata
```

làm app host chịu hành vi (behavior / 동작) mà có thể không nhận ra.

Mỗi manifest entry nên trả lời:

```text
vì sao cần?
exported không?
permission guard?
startup cost?
consumer disable/override được không?
```

---

## 14. Auto-initialization là bên tiêu thụ (consumer / 소비자) startup debt

SDK dùng ContentProvider để auto-init rất tiện nhưng chạy trên startup đường dẫn (path / 경로) bên tiêu thụ (consumer / 소비자).

Nếu initialization nặng, mọi app tích hợp đều trả độ trễ (latency / 지연 시간) chi phí (cost / 비용).

Ưu tiên lazy/on-demand khi tính năng (feature / 기능) không cần trước first tương tác (interaction / 상호작용).

Nếu auto-init cần thiết, keep công việc (work / 작업) tối thiểu.

---

## 15. SDK không được assume Activity tồn tại

Thư viện (library / 라이브러리) có thể được gọi từ:

```text
Service
Receiver
Worker
Application
headless process
```

Nếu API cốt lõi (core / 핵심) yêu cầu Activity ngữ cảnh (context / 맥락) cho mọi thao tác (operation / 연산), coupling quá mạnh.

Phân biệt:

```text
application-scoped capability
vs
UI-scoped capability
```

UI luồng (flow / 흐름) mới nhận Activity/Fragment khi thật sự cần.

---

## 16. ngữ cảnh (context / 맥락) thời gian tồn tại (lifetime / 수명) phải rõ

Không giữ Activity ngữ cảnh (context / 맥락) trong singleton.

Nếu SDK máy khách (client / 클라이언트) sống ứng dụng (application / 애플리케이션) thời gian tồn tại (lifetime / 수명), giữ `applicationContext` khi phù hợp.

Nếu cần Activity cho permission/UI, nhận ephemeral tham chiếu (reference / 참조) ở phương thức (method / 메서드) ranh giới (boundary / 경계) và không bộ nhớ đệm (cache / 캐시) lâu dài.

---

## 17. Threading đặc tả hợp đồng (contract / 계약) phải document

Bên tiêu thụ (consumer / 소비자) cần biết callback chạy luồng thực thi (thread / 스레드) nào.

API mơ hồ:

```kotlin
client.fetch { result -> ... }
```

callback có thể background hoặc main tùy hiện thực (implementation / 구현).

Better đặc tả hợp đồng (contract / 계약):

```text
callbacks delivered on main thread
```

hoặc expose suspend API và để caller quyết định ngữ cảnh (context / 맥락) khi hợp lý.

---

## 18. Suspend API nên main-safe

SDK công khai (public / 공개) suspend hàm (function / 함수) không nên yêu cầu bên tiêu thụ (consumer / 소비자) nhớ chuyển IO nếu underlying công việc (work / 작업) blocking.

```kotlin
suspend fun loadConfig(): Config =
    withContext(ioDispatcher) {
        blockingStore.read()
    }
```

Threading detail nằm trong SDK.

---

## 19. Callback cancellation cần tường minh (explicit / 명시적) handle

Nếu SDK expose callback API:

```kotlin
fun fetch(callback: Callback): RequestHandle
```

Bên tiêu thụ (consumer / 소비자) cần cách cancel khi vòng đời (lifecycle / 생명주기) kết thúc.

Không có cancel đường dẫn (path / 경로) dễ tạo stale callback/leak.

---

## 20. luồng (flow / 흐름) API cần define hot/cold ngữ nghĩa (semantics / 의미론)

Công khai (public / 공개) SDK phương thức (method / 메서드):

```kotlin
fun events(): Flow<Event>
```

Bên tiêu thụ (consumer / 소비자) cần biết:

```text
mỗi collector tạo connection riêng?
replay không?
buffer policy?
start/stop resource khi nào?
```

Luồng (flow / 흐름) kiểu (type / 타입) không tự document tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론).

---

## 21. Exception kiểu (type / 타입) công khai (public / 공개) trở thành Đặc tả API (API contract / API 계약)

Nếu SDK throw nội bộ (internal / 내부) Retrofit exception trực tiếp, bên tiêu thụ (consumer / 소비자) có thể bắt `HttpException` và phụ thuộc hiện thực (implementation / 구현).

Tốt hơn map sang SDK-defined lỗi (error / 오류) mô hình (model / 모델) nếu cần stable đặc tả hợp đồng (contract / 계약).

```kotlin
sealed interface SdkError {
    data object NetworkUnavailable : SdkError
    data class Server(val code: Int) : SdkError
    data object Unauthorized : SdkError
}
```

---

## 22. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약) phải phân biệt retryable/permanent

Bên tiêu thụ (consumer / 소비자) cần biết có thử lại (retry / 재시도) được không.

SDK có thể expose siêu dữ liệu (metadata / 메타데이터):

```kotlin
data class Failure(
    val kind: FailureKind,
    val retryAfter: Duration? = null
)
```

Đừng bắt bên tiêu thụ (consumer / 소비자) reverse-engineer message string.

---

## 23. Logging trong SDK phải respect host privacy

Không log:

```text
token
full request body
PII
password
```

SDK gỡ lỗi (debug / 디버그) logging nên opt-in và redact.

Bên tiêu thụ (consumer / 소비자) có privacy/compliance yêu cầu (requirement / 요구사항) riêng; SDK không được âm thầm thu thập vượt đặc tả hợp đồng (contract / 계약).

---

## 24. Telemetry SDK phải có backpressure/lưu trữ (storage / 저장소) chính sách (policy / 정책)

Analytics sự kiện (event / 이벤트) hàng đợi (queue / 큐) có thể tăng khi offline.

SDK cần chính sách (policy / 정책):

```text
max queue size
retention
batch size
retry
sampling
disk limit
```

Không để analytics chiếm disk vô hạn hoặc thử lại (retry / 재시도) làm hao pin.

---

## 25. SDK phải degrade gracefully khi host misconfigure

Ví dụ API key thiếu.

Bad:

```text
crash Application startup
```

Better tùy criticality:

```text
return initialization error
log actionable diagnostic
disable feature safely
```

Thư viện (library / 라이브러리) không nên kéo cả app host crash nếu tính năng (feature / 기능) optional.

---

## 26. bản địa (native / 네이티브) mã (code / 코드) làm thất bại (failure / 실패) ranh giới (boundary / 경계) nguy hiểm hơn

Kotlin exception thường có thể catch.

Bản địa (native / 네이티브) SIGSEGV có thể kill toàn tiến trình (process / 프로세스).

JNI/NDK ranh giới (boundary / 경계) cần kiểm tra hợp lệ (validation / 검증) chặt hơn:

```text
null
array length
buffer capacity
pointer lifetime
thread attachment
exception pending
```

---

## 27. JNI cục bộ (local / 로컬)/toàn cục (global / 전역) tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명) khác nhau

Cục bộ (local / 로컬) tham chiếu (reference / 참조) thường chỉ valid trong bản địa (native / 네이티브) lời gọi (call / 호출)/frame.

Nếu giữ Java đối tượng (object / 객체) qua lời gọi (call / 호출), cần toàn cục (global / 전역) tham chiếu (reference / 참조) phù hợp và delete khi xong.

Giữ cục bộ (local / 로컬) ref lâu có thể use-after-lifetime; quên delete toàn cục (global / 전역) ref gây leak.

---

## 28. `JNIEnv*` gắn với luồng thực thi (thread / 스레드)

Không bộ nhớ đệm (cache / 캐시) `JNIEnv*` từ luồng thực thi (thread / 스레드) A rồi dùng trên luồng thực thi (thread / 스레드) B.

Bản địa (native / 네이티브) luồng thực thi (thread / 스레드) cần attach JVM để lấy môi trường (environment / 환경) hợp lệ, rồi detach khi vòng đời (lifecycle / 생명주기) yêu cầu.

Luồng thực thi (thread / 스레드) quyền sở hữu (ownership / 소유권) là cốt lõi (core / 핵심) JNI bất biến (invariant / 불변식).

---

## 29. Java exception từ JNI phải check

Nếu bản địa (native / 네이티브) gọi Java phương thức (method / 메서드) và Java throw, JNI có pending exception.

Tiếp tục gọi API khác khi exception pending có thể gây hành vi (behavior / 동작) khó đoán.

Bản địa (native / 네이티브) cầu nối (bridge / 브리지) nên check/propagate/clear theo đặc tả hợp đồng (contract / 계약) đúng.

---

## 30. bản địa (native / 네이티브) buffer quyền sở hữu (ownership / 소유권) phải tường minh (explicit / 명시적)

Nếu Kotlin truyền `ByteBuffer` direct sang bản địa (native / 네이티브), hỏi:

```text
ai giữ memory?
native có giữ pointer sau call không?
GC có move/free backing memory không?
write/read concurrency?
```

Ranh giới (boundary / 경계) docs phải nói rõ thời gian tồn tại (lifetime / 수명).

---

## 31. ABI split ảnh hưởng phân phối (distribution / 분포) và testing

Bản địa (native / 네이티브) `.so` bản dựng (build / 빌드) theo ABI:

```text
arm64-v8a
armeabi-v7a
x86_64
```

Nếu một ABI thiếu thư viện (library / 라이브러리) hoặc hành vi (behavior / 동작) khác, app có thể chỉ crash trên nhóm thiết bị (device / 장치) đó.

CI/bản phát hành (release / 릴리스) kiểm thử (test / 테스트) cần representative ABI.

---

## 32. bản địa (native / 네이티브) symbolication là môi trường vận hành (production / 운영 환경) yêu cầu (requirement / 요구사항)

Crash address:

```text
#00 pc 00000000001234 libfoo.so
```

không hữu ích nếu không có symbol ánh xạ (mapping / 매핑)/hiện vật bản dựng (build artifact / 빌드 산출물) tương ứng.

Bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인) phải archive/upload bản địa (native / 네이티브) symbols theo phiên bản (version / 버전)/bản dựng (build / 빌드) id.

---

## 33. Sanitizer hữu ích để bắt bộ nhớ (memory / 메모리) bug trước môi trường vận hành (production / 운영 환경)

Address/UndefinedBehavior sanitizer hoặc tooling tương ứng giúp bắt:

```text
use-after-free
buffer overflow
undefined behavior
```

Bản địa (native / 네이티브) bộ nhớ (memory / 메모리) bug hiếm nhưng blast radius lớn.

---

## 34. 16 KB page-size tính tương thích (compatibility / 호환성) là bản địa (native / 네이티브) packaging/thời gian chạy (runtime / 런타임) concern

Hiện đại (modern / 현대적) Android thiết bị (device / 장치) ecosystem có thể dùng page kích thước (size / 크기) khác 4 KB.

Bản địa (native / 네이티브) thư viện (library / 라이브러리) bản dựng (build / 빌드)/link alignment phải compatible.

Nếu SDK ship prebuilt `.so`, SDK author chịu trách nhiệm kiểm tra nhị phân (binary / 이진) của mình, không đẩy rủi ro (risk / 위험) cho bên tiêu thụ (consumer / 소비자) app.

---

## 35. bản địa (native / 네이티브) mã (code / 코드) nên được dùng khi lợi ích rõ

Lý do hợp lý:

```text
reuse C/C++ engine
media/codec
high-performance numerical/native library
platform low-level integration
```

Không dùng NDK chỉ để “nhanh hơn” mà chưa benchmark.

JNI crossing cũng có overhead và độ phức tạp (complexity / 복잡도).

---

## 36. JNI ranh giới (boundary / 경계) nên coarse-grained

Bad:

```text
Kotlin gọi native cho từng pixel/từng item nhỏ
```

Crossing hàng triệu lần tạo overhead.

Better:

```text
pass batch/buffer
native xử lý chunk lớn
return aggregated result
```

Optimize ranh giới (boundary / 경계) frequency trước micro-optimize hàm (function / 함수) body.

---

## 37. công khai (public / 공개) bản địa (native / 네이티브) ABI và nội bộ (internal / 내부) bản địa (native / 네이티브) ABI khác nhau

Nếu SDK expose C API cho third party, ABI stability trở thành đặc tả hợp đồng (contract / 계약) dài hạn.

Nếu bản địa (native / 네이티브) chỉ nội bộ (internal / 내부) sau JNI, có thể refactor tự do hơn miễn Java/Kotlin API ổn định.

Giữ bản địa (native / 네이티브) hiện thực (implementation / 구현) private nếu không cần bên ngoài (external / 외부) ABI.

---

## 38. Deprecation nên có di chuyển (migration / 마이그레이션) đường dẫn (path / 경로)

Bad:

```kotlin
@Deprecated("Old")
fun oldApi()
```

Better:

```kotlin
@Deprecated(
    message = "Use track(Event) instead",
    replaceWith = ReplaceWith("track(Event(name, properties))")
)
fun log(name: String, properties: Map<String, Any>)
```

Docs cần giải thích ngữ nghĩa (semantic / 의미적) difference nếu di chuyển (migration / 마이그레이션) không 1:1.

---

## 39. Removal cần bản phát hành (release / 릴리스) chính sách (policy / 정책)

API công khai (public API / 공개 API) không nên deprecated hôm nay, remove ngày mai nếu SDK có broad bên tiêu thụ (consumer / 소비자) cơ sở (base / 기반).

Chính sách (policy / 정책) ví dụ:

```text
deprecate in minor
keep ít nhất N release cycles
remove in major
publish migration guide
```

SemVer chỉ hữu ích khi nhóm (team / 팀) thực sự tôn trọng tính tương thích (compatibility / 호환성) chính sách (policy / 정책).

---

## 40. Behavioral tính tương thích (compatibility / 호환성) quan trọng không kém signature

Phương thức (method / 메서드) signature không đổi nhưng hành vi (behavior / 동작) thay:

```text
callback trước chạy main, giờ chạy background
retry count từ 1 thành 5
timeout từ 5s thành 60s
auto-init bắt đầu network call
```

Bên tiêu thụ (consumer / 소비자) có thể vỡ dù nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) pass.

Bản phát hành (release / 릴리스) ghi chú (note / 노트) phải cover hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약).

---

## 41. hiệu năng (performance / 성능) regression của SDK là externalized chi phí (cost / 비용)

SDK thêm 100ms startup nghĩa là mọi host app trả chi phí (cost / 비용) đó.

SDK nên benchmark:

```text
initialization time
memory overhead
thread count
network usage
artifact size
```

Consumer-centric hiệu năng (performance / 성능) là part của chất lượng (quality / 품질).

---

## 42. SDK kích thước (size / 크기) ngân sách (budget / 예산) cần nhánh học (track / 트랙) transitive chi phí (cost / 비용)

AAR 100 KB nhưng kéo phụ thuộc (dependency / 의존성) 5 MB vẫn làm bên tiêu thụ (consumer / 소비자) sản phẩm tạo ra (artifact / 산출물) lớn.

Measure final bên tiêu thụ (consumer / 소비자) impact, không chỉ tệp (file / 파일) AAR.

---

## 43. Custom Lint giúp encode tích hợp (integration / 통합) quy tắc (rule / 규칙)

Nếu SDK yêu cầu:

```text
API chỉ gọi từ main thread
manifest config bắt buộc
permission usage pattern
forbidden deprecated API
```

custom Lint có thể phát hiện sớm ở bên tiêu thụ (consumer / 소비자) bản dựng (build / 빌드).

Trình biên dịch (compiler / 컴파일러)/build-time phản hồi (feedback / 피드백) tốt hơn thời gian chạy (runtime / 런타임) crash.

---

## 44. SDK mẫu (sample / 표본) app phải là real bên tiêu thụ (consumer / 소비자)

Đừng để mẫu (sample / 표본) mô-đun (module / 모듈) truy cập (access / 접근) nội bộ (internal / 내부) dự án (project / 프로젝트) hiện thực (implementation / 구현) đặc biệt.

Mẫu (sample / 표본) nên consume published/cục bộ (local / 로컬) Maven sản phẩm tạo ra (artifact / 산출물) gần giống bên ngoài (external / 외부) bên tiêu thụ (consumer / 소비자).

Như vậy detect:

```text
missing consumer rules
missing transitive dependency
resource/manifest issue
Java/Kotlin API ergonomics
```

---

## 45. tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) nên compile old bên tiêu thụ (consumer / 소비자) against new SDK

Lưu mẫu (sample / 표본) bên tiêu thụ (consumer / 소비자)/API dump từ phiên bản (version / 버전) trước.

CI new SDK có thể chạy:

```text
binary API diff
source compile test
release minified app test
Java consumer test
Kotlin consumer test
```

Đây là đặc tả hợp đồng (contract / 계약) regression suite.

---

## 46. API dump giúp rà soát (review / 검토) accidental công khai (public / 공개) surface

Công cụ (tool / 도구)/API dump cho thấy công khai (public / 공개) declarations thay đổi trong PR.

Reviewer có thể hỏi:

```text
API mới này thật sự cần public?
nullable contract đúng chưa?
third-party type leak không?
```

API công khai (public API / 공개 API) rà soát (review / 검토) nên tường minh (explicit / 명시적) như cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) rà soát (review / 검토).

---

## 47. Consumer-driven tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

SDK kiểm thử (test / 테스트) ma trận (matrix / 행렬) nên gồm:

```text
min supported Android API
latest Android API
representative AGP/Kotlin ranges nếu support
R8 on/off
Java/Kotlin consumer
common dependency version combinations
major OEM/device nếu hardware feature
```

Không thể hỗ trợ (support / 지원) “mọi phiên bản (version / 버전)”; hỗ trợ (support / 지원) phạm vi (range / 범위) phải document.

---

## 48. bảo mật (security / 보안) cập nhật (update / 업데이트) có thể buộc tính tương thích (compatibility / 호환성) sự đánh đổi (trade-off / 트레이드오프)

Nếu phụ thuộc (dependency / 의존성) có vulnerability nghiêm trọng, SDK có thể cần upgrade breaking phụ thuộc (dependency / 의존성).

Chính sách (policy / 정책) cần cân bằng:

```text
consumer safety
compatibility
migration urgency
```

Bảo mật (security / 보안) patch không nên bị trì hoãn vô hạn chỉ để tránh major phiên bản (version / 버전).

---

## 49. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) provenance cho SDK

Mỗi published sản phẩm tạo ra (artifact / 산출물) nên map được về:

```text
git commit
CI run
source tag
toolchain
dependency lock
signing/provenance metadata
```

Nếu Maven sản phẩm tạo ra (artifact / 산출물) bị sự cố (incident / 인시던트), nhóm (team / 팀) phải reproduce và kiểm tra (audit / 감사) được.

---

## 50. SDK độ tin cậy (reliability / 신뢰성) checklist

| Câu hỏi | Ý nghĩa |
|---|---|
| công khai (public / 공개) surface tối thiểu chưa? | giảm tính tương thích (compatibility / 호환성) burden |
| Third-party kiểu (type / 타입) có leak không? | phụ thuộc (dependency / 의존성) coupling |
| Java bên tiêu thụ (consumer / 소비자) dùng dễ không? | interop đặc tả hợp đồng (contract / 계약) |
| Callback/luồng thực thi (thread / 스레드) ngữ nghĩa (semantics / 의미론) document chưa? | tính đồng thời (concurrency / 동시성) an toàn (safety / 안전) |
| Initialization có nằm startup đường dẫn (path / 경로) không? | host hiệu năng (performance / 성능) |
| bên tiêu thụ (consumer / 소비자) R8 rules đủ chưa? | bản phát hành (release / 릴리스) an toàn (safety / 안전) |
| Manifest entry/exported/bảo mật (security / 보안) đúng chưa? | host bảo mật (security / 보안) |
| bản địa (native / 네이티브) symbols archived chưa? | crash forensic |
| ABI/page-size kiểm thử (test / 테스트) chưa? | bản địa (native / 네이티브) tính tương thích (compatibility / 호환성) |
| Old bên tiêu thụ (consumer / 소비자) compile/run được không? | API evolution |
| Behavioral thay đổi (change / 변경) có bản phát hành (release / 릴리스) ghi chú (note / 노트) không? | ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성) |
| sản phẩm tạo ra (artifact / 산출물) reproducible/auditable không? | supply-chain/bản phát hành (release / 릴리스) |

---

## 51. Kết luận

Một SDK tốt không chỉ “có API dễ gọi”. Nó phải là một phụ thuộc (dependency / 의존성) tử tế trong ecosystem của bên tiêu thụ (consumer / 소비자).

Mô hình tư duy (mental model / 사고 모델):

```text
small public contract
-> stable source/binary behavior
-> minimal dependency leakage
-> explicit lifetime/thread/error semantics
-> release-safe R8/resources/manifest
-> safe native boundary
-> measurable host impact
-> controlled deprecation/migration
-> reproducible artifact
```

Ứng dụng (application / 애플리케이션) mã (code / 코드) có thể sửa theo cadence của chính nhóm (team / 팀). SDK mã (code / 코드) phải sống cùng cadence của nhiều bên tiêu thụ (consumer / 소비자), vì vậy mỗi công khai (public / 공개) quyết định (decision / 결정) đều có chi phí dài hạn.

> **Bàn giao:** Sau **51. Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture invariants boundary reasoning](./01_architecture_invariants_boundary_reasoning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.

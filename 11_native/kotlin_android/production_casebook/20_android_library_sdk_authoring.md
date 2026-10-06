# Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**. Route đi từ Android library/JVM distinction → public API surface → AAR/resources/manifest/ProGuard → binary compatibility, consumer behavior và publishing → tests/versioning, để SDK được thiết kế như contract không kiểm soát consumer.

Viết mã (code / 코드) bên trong một app và viết một Android thư viện (library / 라이브러리)/SDK cho app khác sử dụng là hai bài toán khác nhau. Trong app, nhóm (team / 팀) có thể refactor đồng thời mọi lời gọi (call / 호출) site. Trong thư viện (library / 라이브러리), công khai (public / 공개) lớp (class / 클래스), tài nguyên (resource / 자원), manifest thành phần (component / 컴포넌트), ProGuard quy tắc (rule / 규칙), initialization hành vi (behavior / 동작) và transitive phụ thuộc (dependency / 의존성) đều trở thành đặc tả hợp đồng (contract / 계약) với bên tiêu thụ (consumer / 소비자) mà bạn không kiểm soát.

Chapter này xây mô hình tư duy (mental model / 사고 모델) để thiết kế reusable Android thư viện (library / 라이브러리)/SDK ổn định, nhỏ, kiểm thử (test / 테스트) được và không ép bên tiêu thụ (consumer / 소비자) hiểu hiện thực (implementation / 구현) detail.

## 1. Android thư viện (library / 라이브러리) khác pure Kotlin/JVM thư viện (library / 라이브러리)

Pure Kotlin/JVM thư viện (library / 라이브러리) chủ yếu publish bytecode/JAR và siêu dữ liệu (metadata / 메타데이터). Android thư viện (library / 라이브러리) có thể cần Android resources, manifest, bản địa (native / 네이티브) thư viện (library / 라이브러리), bên tiêu thụ (consumer / 소비자) ProGuard rules, lint checks và Android-specific APIs, nên thường được bản dựng (build / 빌드) thành **AAR — Android Archive**.

AAR có thể chứa:

```text
classes.jar
AndroidManifest.xml
res/
assets/
jni/
consumer-rules
R.txt/public resources metadata
```

Không phải AAR nào cũng có mọi thành phần.

Nếu thư viện (library / 라이브러리) không cần Android khung phần mềm (framework / 프레임워크)/tài nguyên (resource / 자원), pure Kotlin/JVM mô-đun (module / 모듈) thường đơn giản và reusable hơn.

> **Nối mạch:** Android library mang resource/manifest/runtime concerns ngoài pure Kotlin/JVM; public API surface vì vậy là product, kéo theo source và binary compatibility obligations.

## 2. API công khai (public API / 공개 API) surface là sản phẩm

Mọi `public` declaration có thể trở thành tính tương thích (compatibility / 호환성) obligation. Đừng để hiện thực (implementation / 구현) lớp (class / 클래스) công khai (public / 공개) chỉ vì default visibility tiện.

Kotlin default là `public`, nên thư viện (library / 라이브러리) author phải chủ động dùng `internal`/`private`.

```kotlin
public interface PaymentClient {
    suspend fun pay(request: PaymentRequest): PaymentResult
}

internal class DefaultPaymentClient(...) : PaymentClient { ... }
```

API công khai (public API / 공개 API) nhỏ giúp evolve hiện thực (implementation / 구현) mà không phá bên tiêu thụ (consumer / 소비자).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **2. API công khai (public API / 공개 API) surface là sản phẩm** đặt vấn đề; **3. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)** đối chiếu bằng chứng, rồi **4. Kotlin default parameters và Java bên tiêu thụ (consumer / 소비자)** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)

**nguồn (source / 소스) tính tương thích (compatibility / 호환성)**: bên tiêu thụ (consumer / 소비자) nguồn (source / 소스) cũ recompile với thư viện (library / 라이브러리) mới vẫn compile.

**nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)**: app/thư viện (library / 라이브러리) bên tiêu thụ (consumer / 소비자) đã compile trước đó vẫn link/run với nhị phân (binary / 이진) mới mà không cần recompile.

Một thay đổi (change / 변경) có thể source-compatible nhưng binary-incompatible hoặc ngược lại.

Ví dụ đổi phương thức (method / 메서드) signature/default parameter/inline hiện thực (implementation / 구현)/giao diện (interface / 인터페이스) shape có thể có ABI implication khác trực giác mã nguồn (source code / 소스 코드).

Thư viện (library / 라이브러리) môi trường vận hành (production / 운영 환경) cần API/ABI kiểm tra hợp lệ (validation / 검증), không chỉ compile mẫu (sample / 표본) app.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **3. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)** đặt vấn đề; **4. Kotlin default parameters và Java bên tiêu thụ (consumer / 소비자)** đối chiếu bằng chứng, rồi **5. @JvmStatic, @JvmField, @JvmName là interoperability tools** mở rộng hệ quả hoặc giới hạn liên quan.

## 4. Kotlin default parameters và Java bên tiêu thụ (consumer / 소비자)

Kotlin:

```kotlin
fun connect(timeoutMs: Long = 5_000)
```

Kotlin caller dùng default parameter tự nhiên. Java caller không thấy overload giống Kotlin trừ khi dùng `@JvmOverloads` hoặc tường minh (explicit / 명시적) overload.

Thư viện (library / 라이브러리) cho mixed Java/Kotlin ecosystem phải rà soát (review / 검토) Java ergonomics:

```kotlin
@JvmOverloads
fun connect(timeoutMs: Long = 5_000, retry: Int = 1)
```

Không thêm `@JvmOverloads` máy móc; nó tăng công khai (public / 공개) methods/ABI surface.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **5. @JvmStatic, @JvmField, @JvmName là interoperability tools** nối từ **4. Kotlin default parameters và Java bên tiêu thụ (consumer / 소비자)** sang **6. Avoid exposing hiện thực (implementation / 구현) phụ thuộc (dependency / 의존성) types**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. `@JvmStatic`, `@JvmField`, `@JvmName` là interoperability tools

Companion/đối tượng (object / 객체) API có thể awkward từ Java. Annotation JVM giúp shape bytecode/API:

```kotlin
class Sdk private constructor() {
    companion object {
        @JvmStatic
        fun initialize(context: Context) { ... }
    }
}
```

`@JvmName` giúp tránh signature clash hoặc cung cấp Java-friendly name. Mọi annotation này nên được xem là ABI quyết định (decision / 결정).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **6. Avoid exposing hiện thực (implementation / 구현) phụ thuộc (dependency / 의존성) types** nối từ **5. @JvmStatic, @JvmField, @JvmName là interoperability tools** sang **7. api vs implementation trong thư viện (library / 라이브러리)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Avoid exposing hiện thực (implementation / 구현) phụ thuộc (dependency / 의존성) types

Nếu API công khai (public API / 공개 API) trả Retrofit `Response`, OkHttp kiểu (type / 타입), Room thực thể (entity / 엔터티) hay coroutine nội bộ (internal / 내부) kiểu (type / 타입) không cần thiết, bên tiêu thụ (consumer / 소비자) bị coupled vào phụ thuộc (dependency / 의존성)/phiên bản (version / 버전) của SDK.

Bad:

```kotlin
fun fetch(): retrofit2.Response<UserDto>
```

Better:

```kotlin
suspend fun fetchUser(): UserResult
```

Expose tiêu chuẩn (standard / 표준)/library-owned lĩnh vực (domain / 도메인) types. Điều này giảm transitive phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) và cho phép đổi hiện thực (implementation / 구현).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **7. api vs implementation trong thư viện (library / 라이브러리)** nối từ **6. Avoid exposing hiện thực (implementation / 구현) phụ thuộc (dependency / 의존성) types** sang **8. AAR tài nguyên (resource / 자원) là global-ish không gian tên (namespace / 네임스페이스) concern**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. `api` vs `implementation` trong thư viện (library / 라이브러리)

Nếu API công khai (public API / 공개 API) expose kiểu (type / 타입) từ phụ thuộc (dependency / 의존성), Gradle có thể cần `api`. Nếu phụ thuộc (dependency / 의존성) chỉ hiện thực (implementation / 구현) detail, dùng `implementation`.

Overuse `api` làm phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) bên tiêu thụ (consumer / 소비자) phình và tăng ABI coupling.

Goal không phải “không có transitive phụ thuộc (dependency / 의존성)”, mà là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) deliberate.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **7. api vs implementation trong thư viện (library / 라이브러리)** đặt vấn đề; **8. AAR tài nguyên (resource / 자원) là global-ish không gian tên (namespace / 네임스페이스) concern** đối chiếu bằng chứng, rồi **9. Theme/style đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. AAR tài nguyên (resource / 자원) là global-ish không gian tên (namespace / 네임스페이스) concern

Tài nguyên (resource / 자원) name trong dependencies được merge vào app tài nguyên (resource / 자원) đồ thị (graph / 그래프). thư viện (library / 라이브러리) nên prefix tài nguyên (resource / 자원) để giảm collision:

```text
sdk_payment_button
sdk_payment_error_title
sdk_payment_theme_overlay
```

Không đặt generic `button_primary` trong công khai (public / 공개) thư viện (library / 라이브러리).

Nếu tài nguyên (resource / 자원) không intended for bên tiêu thụ (consumer / 소비자) override/use, giảm công khai (public / 공개) exposure theo năng lực (capability / 역량) bản dựng (build / 빌드) tools/phiên bản (version / 버전) hỗ trợ.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **8. AAR tài nguyên (resource / 자원) là global-ish không gian tên (namespace / 네임스페이스) concern** đặt vấn đề; **9. Theme/style đặc tả hợp đồng (contract / 계약)** đối chiếu bằng chứng, rồi **10. Compose thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. Theme/style đặc tả hợp đồng (contract / 계약)

Custom View/Compose thành phần (component / 컴포넌트) thư viện (library / 라이브러리) cần document theme expectation. Không assume bên tiêu thụ (consumer / 소비자) dùng cùng Material theme/phiên bản (version / 버전).

Nếu SDK kết xuất (render / 렌더링) UI, cân nhắc:

- theme overlay;
- colors/typography configurable;
- dark chế độ (mode / 모드);
- động (dynamic / 동적) color hành vi (behavior / 동작);
- khả năng tiếp cận (accessibility / 접근성)/font quy mô (scale / 규모);
- localization;
- edge-to-edge/insets.

UI SDK là công khai (public / 공개) visual đặc tả hợp đồng (contract / 계약), không chỉ mã (code / 코드) API.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **10. Compose thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)** nối từ **9. Theme/style đặc tả hợp đồng (contract / 계약)** sang **11. Manifest của thư viện (library / 라이브러리) được merge vào bên tiêu thụ (consumer / 소비자) app**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Compose thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)

Compose thư viện (library / 라이브러리) API công khai (public API / 공개 API) có thêm concern trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리) phiên bản (version / 버전). Avoid exposing unstable/experimental API không có chính sách (policy / 정책) rõ.

Công khai (public / 공개) composable nên follow trạng thái (state / 상태) hoisting:

```kotlin
@Composable
fun PaymentButton(
    state: PaymentButtonState,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
)
```

`Modifier` thường để cuối/default giúp composition idiom. Không hardcode điều hướng (navigation / 내비게이션)/ViewModel/toàn cục (global / 전역) singleton bên trong reusable UI thành phần (component / 컴포넌트).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **11. Manifest của thư viện (library / 라이브러리) được merge vào bên tiêu thụ (consumer / 소비자) app** nối từ **10. Compose thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성)** sang **12. Auto-initialization là convenience có startup chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Manifest của thư viện (library / 라이브러리) được merge vào bên tiêu thụ (consumer / 소비자) app

Thư viện (library / 라이브러리) có thể khai báo provider/dịch vụ (service / 서비스)/receiver/permission. Đây là powerful side tác động (effect / 효과).

SDK author phải:

- minimal manifest footprint;
- `android:exported` tường minh (explicit / 명시적)/correct;
- unique authorities bằng `${applicationId}` placeholder khi phù hợp;
- avoid broad permission nếu tính năng (feature / 기능) optional;
- document thành phần (component / 컴포넌트) hành vi (behavior / 동작).

Bên tiêu thụ (consumer / 소비자) phải có khả năng override/remove thành phần (component / 컴포넌트) khi kiến trúc (architecture / 아키텍처) cho phép.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **12. Auto-initialization là convenience có startup chi phí (cost / 비용)** nối từ **11. Manifest của thư viện (library / 라이브러리) được merge vào bên tiêu thụ (consumer / 소비자) app** sang **13. Context quyền sở hữu (ownership / 소유권) trong SDK**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Auto-initialization là convenience có startup chi phí (cost / 비용)

SDK thường dùng ContentProvider/AndroidX Startup để auto-init. Điều này giảm setup nhưng thêm công việc (work / 작업) vào cold start của mọi app bên tiêu thụ (consumer / 소비자).

Chỉ auto-init phần thật sự cần và rất nhẹ. Heavy SDK nên tường minh (explicit / 명시적) initialize hoặc lazy tính năng (feature / 기능) init.

Cung cấp opt-out nếu auto-init có meaningful chi phí (cost / 비용).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, sau nội dung của **12. Auto-initialization là convenience có startup chi phí (cost / 비용)**, **13. Context quyền sở hữu (ownership / 소유권) trong SDK** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **14. Threading đặc tả hợp đồng (contract / 계약) phải được document** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. `Context` quyền sở hữu (ownership / 소유권) trong SDK

Long-lived SDK đối tượng (object / 객체) không giữ Activity ngữ cảnh (context / 맥락) nếu không cần. Dùng ứng dụng (application / 애플리케이션) ngữ cảnh (context / 맥락) cho process-lifetime dịch vụ (service / 서비스).

Nếu API cần Activity để launch UI/permission, chỉ giữ tham chiếu (reference / 참조) trong thao tác (operation / 연산) phạm vi (scope / 범위) hoặc weak/lifecycle-aware đặc tả hợp đồng (contract / 계약).

Bộ nhớ (memory / 메모리) leak trong SDK ảnh hưởng mọi app bên tiêu thụ (consumer / 소비자) và khó gỡ lỗi (debug / 디버그) vì ngăn xếp (stack / 스택) crossing thư viện (library / 라이브러리) ranh giới (boundary / 경계).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **14. Threading đặc tả hợp đồng (contract / 계약) phải được document** nối từ **13. Context quyền sở hữu (ownership / 소유권) trong SDK** sang **15. Coroutine API và phạm vi (scope / 범위) quyền sở hữu (ownership / 소유권)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Threading đặc tả hợp đồng (contract / 계약) phải được document

API callback có chạy main luồng thực thi (thread / 스레드) không? phương thức (method / 메서드) có thread-safe không? Có thể lời gọi (call / 호출) concurrent không?

Kotlin coroutine API thường rõ hơn callback, nhưng vẫn cần main-safety đặc tả hợp đồng (contract / 계약).

```kotlin
interface AnalyticsSdk {
    /** Main-safe; may be called from any thread. */
    fun track(event: Event)
}
```

Nếu bên tiêu thụ (consumer / 소비자) phải tự biết “phương thức (method / 메서드) này không được main luồng thực thi (thread / 스레드)” mà docs không nói, SDK đặc tả hợp đồng (contract / 계약) chưa đủ.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, sau nội dung của **14. Threading đặc tả hợp đồng (contract / 계약) phải được document**, **15. Coroutine API và phạm vi (scope / 범위) quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **16. luồng (flow / 흐름) API công khai (public API / 공개 API)** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. Coroutine API và phạm vi (scope / 범위) quyền sở hữu (ownership / 소유권)

Thư viện (library / 라이브러리) `suspend` hàm (function / 함수) nên caller-owned: công việc (work / 작업) bị cancel khi caller phạm vi (scope / 범위) cancel, trừ khi thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론) thật sự durable.

Không launch `GlobalScope` để thoát cancellation.

Nếu SDK cần process-long công việc (work / 작업), expose tường minh (explicit / 명시적) vòng đời (lifecycle / 생명주기) or use appropriate durable Android thành phần nguyên thủy (primitive / 기본 요소); document hành vi (behavior / 동작).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **15. Coroutine API và phạm vi (scope / 범위) quyền sở hữu (ownership / 소유권)** đặt đầu vào cho **16. luồng (flow / 흐름) API công khai (public API / 공개 API)**, rồi **17. lỗi (error / 오류) mô hình (model / 모델) API công khai (public API / 공개 API)** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. luồng (flow / 흐름) API công khai (public API / 공개 API)

`Flow<T>` hợp lý cho stream. Cần document hot/cold hành vi (behavior / 동작) và replay ngữ nghĩa (semantics / 의미론).

Expose mutable stream ra ngoài là nguy hiểm:

```kotlin
private val _state = MutableStateFlow(...)
val state: StateFlow<State> = _state.asStateFlow()
```

Bên tiêu thụ (consumer / 소비자) quan sát, SDK sở hữu mutation.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **16. luồng (flow / 흐름) API công khai (public API / 공개 API)** đặt đầu vào cho **17. lỗi (error / 오류) mô hình (model / 모델) API công khai (public API / 공개 API)**, rồi **18. Cancellation không phải lỗi (error / 오류) bình thường** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. lỗi (error / 오류) mô hình (model / 모델) API công khai (public API / 공개 API)

Không để mọi thất bại (failure / 실패) thành raw `Exception` implementation-specific.

Thư viện (library / 라이브러리) có thể dùng sealed kết quả (result / 결과)/lỗi (error / 오류):

```kotlin
sealed interface PaymentError {
    data object NetworkUnavailable : PaymentError
    data object Cancelled : PaymentError
    data class Declined(val code: String?) : PaymentError
    data class Internal(val cause: Throwable?) : PaymentError
}
```

Nhưng công khai (public / 공개) lỗi (error / 오류) taxonomy phải stable. Đừng expose nội bộ (internal / 내부) máy chủ (server / 서버) mã (code / 코드) như permanent enum nếu backend có thể thêm giá trị (value / 값).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **18. Cancellation không phải lỗi (error / 오류) bình thường** nối từ **17. lỗi (error / 오류) mô hình (model / 모델) API công khai (public API / 공개 API)** sang **19. bên tiêu thụ (consumer / 소비자) ProGuard/R8 rules**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Cancellation không phải lỗi (error / 오류) bình thường

Coroutine thư viện (library / 라이브러리) không nên catch `Throwable` rồi biến `CancellationException` thành SDK lỗi (error / 오류). Propagate cancellation đúng structured tính đồng thời (concurrency / 동시성).

```kotlin
catch (e: CancellationException) {
    throw e
}
```

Nếu API có tường minh (explicit / 명시적) người dùng (user / 사용자) cancellation kết quả (result / 결과) khác coroutine cancellation, document distinction.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **19. bên tiêu thụ (consumer / 소비자) ProGuard/R8 rules** nối từ **18. Cancellation không phải lỗi (error / 오류) bình thường** sang **20. kiểm thử (test / 테스트) minified bên tiêu thụ (consumer / 소비자) app**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. bên tiêu thụ (consumer / 소비자) ProGuard/R8 rules

Thư viện (library / 라이브러리) dùng reflection/JNI/serialization có thể cần keep rules khi bên tiêu thụ (consumer / 소비자) app minify.

Đưa quy tắc (rule / 규칙) bắt buộc vào `consumerProguardFiles`, không yêu cầu mọi bên tiêu thụ (consumer / 소비자) bản sao (copy / 복사) docs thủ công.

```kotlin
android {
    defaultConfig {
        consumerProguardFiles("consumer-rules.pro")
    }
}
```

Quy tắc (rule / 규칙) phải minimal. `-keep class com.sdk.** { *; }` có thể vô hiệu hóa tối ưu hóa (optimization / 최적화) lớn của bên tiêu thụ (consumer / 소비자).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **20. kiểm thử (test / 테스트) minified bên tiêu thụ (consumer / 소비자) app** nối từ **19. bên tiêu thụ (consumer / 소비자) ProGuard/R8 rules** sang **21. bản địa (native / 네이티브) thư viện (library / 라이브러리) trong AAR**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. kiểm thử (test / 테스트) minified bên tiêu thụ (consumer / 소비자) app

Thư viện (library / 라이브러리) gỡ lỗi (debug / 디버그) đơn vị (unit / 단위) tests không phát hiện R8 issue. Tạo mẫu (sample / 표본)/fixture app bản dựng (build / 빌드) `release` minified để kiểm thử (test / 테스트) SDK packaged như bên tiêu thụ (consumer / 소비자) thật.

CI nên ít nhất bản dựng (build / 빌드)/install smoke kiểm thử (test / 테스트) minified sản phẩm tạo ra (artifact / 산출물) cho thư viện (library / 라이브러리) có reflection/JNI.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **21. bản địa (native / 네이티브) thư viện (library / 라이브러리) trong AAR** nối từ **20. kiểm thử (test / 테스트) minified bên tiêu thụ (consumer / 소비자) app** sang **22. Lint checks như executable documentation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. bản địa (native / 네이티브) thư viện (library / 라이브러리) trong AAR

Nếu AAR chứa `.so`, SDK author chịu thêm ABI/page-size/symbol concern của trường hợp (case / 사례) 17.

Bên tiêu thụ (consumer / 소비자) không nên bất ngờ với 30 MB bản địa (native / 네이티브) binaries. Document kích thước (size / 크기) và ABI hỗ trợ (support / 지원).

Bản địa (native / 네이티브) symbols/gỡ lỗi (debug / 디버그) gói (package / 패키지) cần bản phát hành (release / 릴리스) management tương ứng nếu SDK hỗ trợ (support / 지원) crash phân tích (analysis / 분석).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **22. Lint checks như executable documentation** nối từ **21. bản địa (native / 네이티브) thư viện (library / 라이브러리) trong AAR** sang **23. Annotations và opt-in**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Lint checks như executable documentation

Nếu SDK có usage quy tắc (rule / 규칙) mà trình biên dịch (compiler / 컴파일러) không encode được, custom Android Lint có thể bắt sai usage ở bên tiêu thụ (consumer / 소비자) bản dựng (build / 빌드).

Ví dụ:

- API cần manifest declaration;
- phương thức (method / 메서드) không được gọi trong main luồng thực thi (thread / 스레드);
- annotation pair phải dùng cùng nhau;
- deprecated di chuyển (migration / 마이그레이션) đường dẫn (path / 경로).

Lint tốt giúp chuyển docs thành early phản hồi (feedback / 피드백). Nhưng custom lint cũng là sản phẩm tạo ra (artifact / 산출물)/versioned API phải kiểm thử (test / 테스트) với toolchain bên tiêu thụ (consumer / 소비자).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **23. Annotations và opt-in** nối từ **22. Lint checks như executable documentation** sang **24. SemVer chỉ hữu ích khi tính tương thích (compatibility / 호환성) chính sách (policy / 정책) rõ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Annotations và opt-in

`@RequiresApi`, `@IntDef` legacy Java interop, Kotlin `@RequiresOptIn`, nullability annotations và threading annotations có thể tăng đặc tả hợp đồng (contract / 계약) clarity.

Experimental API nên rõ:

```kotlin
@RequiresOptIn
annotation class ExperimentalSdkApi
```

Không gọi API “experimental” nhưng vẫn hứa nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) như stable API.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **24. SemVer chỉ hữu ích khi tính tương thích (compatibility / 호환성) chính sách (policy / 정책) rõ** nối từ **23. Annotations và opt-in** sang **25. Behavioral tính tương thích (compatibility / 호환성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. SemVer chỉ hữu ích khi tính tương thích (compatibility / 호환성) chính sách (policy / 정책) rõ

Ngữ nghĩa (semantic / 의미적) Versioning thường hiểu:

- major: breaking thay đổi (change / 변경);
- minor: backward-compatible tính năng (feature / 기능);
- patch: backward-compatible fix.

Nhưng “breaking” phải định nghĩa nguồn (source / 소스), nhị phân (binary / 이진), hành vi (behavior / 동작), tài nguyên (resource / 자원) và dữ liệu (data / 데이터) tính tương thích (compatibility / 호환성).

Android SDK có thể giữ nhị phân (binary / 이진) API nhưng đổi manifest hành vi (behavior / 동작) làm app bên tiêu thụ (consumer / 소비자) break. Đó vẫn là breaking thay đổi (change / 변경) về sản phẩm (product / 제품) đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **25. Behavioral tính tương thích (compatibility / 호환성)** nối từ **24. SemVer chỉ hữu ích khi tính tương thích (compatibility / 호환성) chính sách (policy / 정책) rõ** sang **26. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) kiểm tra hợp lệ (validation / 검증)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Behavioral tính tương thích (compatibility / 호환성)

Phương thức (method / 메서드) signature không đổi nhưng ngữ nghĩa (semantics / 의미론) đổi từ “thử lại (retry / 재시도) 1 lần” sang “thử lại (retry / 재시도) vô hạn” có thể phá app.

SDK bản phát hành (release / 릴리스) notes phải ghi hành vi (behavior / 동작) changes, luồng thực thi (thread / 스레드) changes, permission changes, startup changes và phụ thuộc (dependency / 의존성) changes—không chỉ API diff.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **26. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) kiểm tra hợp lệ (validation / 검증)** nối từ **25. Behavioral tính tương thích (compatibility / 호환성)** sang **27. Inline hàm (function / 함수) tính tương thích (compatibility / 호환성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) kiểm tra hợp lệ (validation / 검증)

Kotlin/Java ecosystem có tools để dump/check công khai (public / 공개) ABI. nhóm (team / 팀) nên integrate API dump/check vào CI cho published libraries.

Workflow:

```text
change library
→ generate API/ABI dump
→ diff against baseline
→ deliberate approve breaking/additive change
```

Không rà soát (review / 검토) công khai (public / 공개) ABI bằng mắt trong 500-file PR.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **27. Inline hàm (function / 함수) tính tương thích (compatibility / 호환성)** nối từ **26. nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) kiểm tra hợp lệ (validation / 검증)** sang **28. dữ liệu (data / 데이터) lớp (class / 클래스) trong API công khai (public API / 공개 API)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Inline hàm (function / 함수) tính tương thích (compatibility / 호환성)

Công khai (public / 공개) `inline` hàm (function / 함수) đưa hiện thực (implementation / 구현) vào caller bytecode khi compile. Thay hiện thực (implementation / 구현)/thư viện (library / 라이브러리) phiên bản (version / 버전) có ngữ nghĩa (semantics / 의미론) khác non-inline phương thức (method / 메서드).

Công khai (public / 공개) inline API cần đặc biệt cẩn thận với references tới nội bộ (internal / 내부) hiện thực (implementation / 구현); Kotlin có `@PublishedApi` cho specific use trường hợp (case / 사례) nhưng nó cũng mở tính tương thích (compatibility / 호환성) commitment.

Đừng inline API công khai (public API / 공개 API) chỉ vì micro hiệu năng (performance / 성능) nếu không cần.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **27. Inline hàm (function / 함수) tính tương thích (compatibility / 호환성)** đặt vấn đề; **28. dữ liệu (data / 데이터) lớp (class / 클래스) trong API công khai (public API / 공개 API)** đối chiếu bằng chứng, rồi **29. Enum evolution** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. dữ liệu (data / 데이터) lớp (class / 클래스) trong API công khai (public API / 공개 API)

Công khai (public / 공개) `data class` tiện nhưng auto-generated `copy/componentN` và constructor shape trở thành API. Thêm thuộc tính (property / 속성) vào primary constructor có thể nguồn (source / 소스)/nhị phân (binary / 이진) implications.

Đối với long-lived SDK mô hình (model / 모델) cần evolve, builder/giao diện (interface / 인터페이스)/regular lớp (class / 클래스) hoặc optional extension fields có thể linh hoạt hơn tùy use trường hợp (case / 사례).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **28. dữ liệu (data / 데이터) lớp (class / 클래스) trong API công khai (public API / 공개 API)** đặt vấn đề; **29. Enum evolution** đối chiếu bằng chứng, rồi **30. Parcelable/Serializable công khai (public / 공개) mô hình (model / 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. Enum evolution

Bên tiêu thụ (consumer / 소비자) `when` exhaustive trên enum có thể break các giả định (assumptions / 가정들) khi thư viện (library / 라이브러리) thêm enum constant. mạng (network / 네트워크)/server-open lĩnh vực (domain / 도메인) càng không nên expose closed enum nếu future values có thể xuất hiện.

Sealed hierarchy cũng là closed-world đặc tả hợp đồng (contract / 계약). Chọn closed/open mô hình (model / 모델) có chủ ý.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **29. Enum evolution** nêu quy tắc; **30. Parcelable/Serializable công khai (public / 공개) mô hình (model / 모델)** thử quy tắc trong tình huống, rồi **31. tài nguyên (resource / 자원) ID không phải stable bên ngoài (external / 외부) giao thức (protocol / 프로토콜)** mở rộng hệ quả.

## 30. Parcelable/Serializable công khai (public / 공개) mô hình (model / 모델)

Nếu SDK mô hình (model / 모델) đi qua Bundle/Intent/tiến trình (process / 프로세스) recreation, serialized shape trở thành tính tương thích (compatibility / 호환성) concern.

Không dùng Java Serializable mặc định cho durable lưu trữ (storage / 저장소)/versioned giao thức (protocol / 프로토콜). Parcelable phù hợp Android IPC/trạng thái (state / 상태) ngắn hạn nhưng không phải stable persistence format.

Durable dữ liệu (data / 데이터) cần tường minh (explicit / 명시적) lược đồ (schema / 스키마)/versioning.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **30. Parcelable/Serializable công khai (public / 공개) mô hình (model / 모델)** nêu quy tắc; **31. tài nguyên (resource / 자원) ID không phải stable bên ngoài (external / 외부) giao thức (protocol / 프로토콜)** thử quy tắc trong tình huống, rồi **32. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) và BOM** mở rộng hệ quả.

## 31. tài nguyên (resource / 자원) ID không phải stable bên ngoài (external / 외부) giao thức (protocol / 프로토콜)

Không persist raw `R.id`/tài nguyên (resource / 자원) integer qua app versions/máy chủ (server / 서버). IDs có thể thay khi rebuild/tài nguyên (resource / 자원) đồ thị (graph / 그래프) thay đổi.

Công khai (public / 공개) SDK API nên dùng ngữ nghĩa (semantic / 의미적) identifiers/string/lĩnh vực (domain / 도메인) kiểu (type / 타입).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **31. tài nguyên (resource / 자원) ID không phải stable bên ngoài (external / 외부) giao thức (protocol / 프로토콜)** đặt vấn đề; **32. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) và BOM** đối chiếu bằng chứng, rồi **33. Shading/relocation** mở rộng hệ quả hoặc giới hạn liên quan.

## 32. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) và BOM

SDK kéo nhiều libraries có thể xung đột (conflict / 충돌) bên tiêu thụ (consumer / 소비자) versions. Giảm phụ thuộc (dependency / 의존성) footprint và tránh pin các ràng buộc (constraints / 제약조건들) quá chặt nếu không cần.

Nếu publish family nhiều artifacts, BOM/nền tảng (platform / 플랫폼) có thể giúp align versions. Nhưng BOM không giải thời gian chạy (runtime / 런타임) incompatibility nếu modules thật sự không compatible.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **33. Shading/relocation** nối từ **32. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) và BOM** sang **34. Publishing repository**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Shading/relocation

Một số JVM libraries shade phụ thuộc (dependency / 의존성) để tránh xung đột (conflict / 충돌), nhưng Android/R8/tài nguyên (resource / 자원)/bản địa (native / 네이티브) môi trường (environment / 환경) làm technique phức tạp. Chỉ dùng khi hiểu license/kích thước (size / 크기)/reflection consequences.

Tốt hơn thường là giảm phụ thuộc (dependency / 의존성) hoặc expose tính tương thích (compatibility / 호환성) phạm vi (range / 범위) hợp lý.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **34. Publishing repository** nối từ **33. Shading/relocation** sang **35. Sources và documentation artifacts**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Publishing repository

Thư viện (library / 라이브러리) có thể publish Maven sản phẩm tạo ra (artifact / 산출물) gồm group/sản phẩm tạo ra (artifact / 산출물)/phiên bản (version / 버전), POM/mô-đun (module / 모듈) siêu dữ liệu (metadata / 메타데이터) và AAR/JAR.

Nội bộ (internal / 내부) SDK có thể dùng private Maven repository. công khai (public / 공개) SDK có thể publish central repository phù hợp.

Publishing chuỗi xử lý (pipeline / 파이프라인) phải immutable: không overwrite nhị phân (binary / 이진) của cùng phiên bản (version / 버전). Nếu `1.2.3` hôm nay khác `1.2.3` ngày mai, reproducibility bên tiêu thụ (consumer / 소비자) vỡ.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **34. Publishing repository** đặt vấn đề; **35. Sources và documentation artifacts** đối chiếu bằng chứng, rồi **36. mẫu (sample / 표본) app là kiểm thử tích hợp (integration test / 통합 테스트) và documentation** mở rộng hệ quả hoặc giới hạn liên quan.

## 35. Sources và documentation artifacts

Publish nguồn (source / 소스)/Javadoc/Dokka artifacts giúp debugging/IDE điều hướng (navigation / 내비게이션). API công khai (public API / 공개 API) docs phải đi cùng bản phát hành (release / 릴리스) phiên bản (version / 버전).

Docs website “latest” không đủ khi bên tiêu thụ (consumer / 소비자) đang pin old phiên bản (version / 버전). Giữ versioned di chuyển (migration / 마이그레이션)/bản phát hành (release / 릴리스) notes.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **35. Sources và documentation artifacts** đặt vấn đề; **36. mẫu (sample / 표본) app là kiểm thử tích hợp (integration test / 통합 테스트) và documentation** đối chiếu bằng chứng, rồi **37. kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho SDK** mở rộng hệ quả hoặc giới hạn liên quan.

## 36. mẫu (sample / 표본) app là kiểm thử tích hợp (integration test / 통합 테스트) và documentation

Một mẫu (sample / 표본) app tốt chứng minh:

- install SDK;
- manifest/cấu hình (config / 설정) setup;
- dùng chung (common / 공통) luồng (flow / 흐름);
- lỗi (error / 오류)/cancel;
- tiến trình (process / 프로세스) recreation;
- bản phát hành (release / 릴리스) minification;
- Java bên tiêu thụ (consumer / 소비자) nếu hỗ trợ (support / 지원).

Mẫu (sample / 표본) phải bản dựng (build / 빌드) trong CI để tránh docs drift.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **37. kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho SDK** nối từ **36. mẫu (sample / 표본) app là kiểm thử tích hợp (integration test / 통합 테스트) và documentation** sang **38. Backward tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) của SDK**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho SDK

SDK kiểm thử (test / 테스트) không chỉ đơn vị (unit / 단위) kiểm thử (test / 테스트) nội bộ (internal / 내부) mã (code / 코드). Cần:

1. pure đơn vị (unit / 단위) tests;
2. Android instrumentation nếu khung phần mềm (framework / 프레임워크) tương tác (interaction / 상호작용);
3. minSdk + latest representative;
4. Java/Kotlin bên tiêu thụ (consumer / 소비자) compile;
5. minified bản phát hành (release / 릴리스) bên tiêu thụ (consumer / 소비자);
6. tiến trình (process / 프로세스)/vòng đời (lifecycle / 생명주기) tests nếu SDK UI/hệ thống (system / 시스템) thành phần (component / 컴포넌트);
7. mạng (network / 네트워크) thất bại (failure / 실패)/cancellation;
8. upgrade from previous SDK phiên bản (version / 버전) in mẫu (sample / 표본) app khi trạng thái (state / 상태) durable;
9. ABI/bản địa (native / 네이티브) ma trận (matrix / 행렬) nếu `.so`;
10. compile against supported AGP/Kotlin phạm vi (range / 범위) nếu officially promised.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **38. Backward tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) của SDK** nối từ **37. kiểm thử (test / 테스트) ma trận (matrix / 행렬) cho SDK** sang **39. SDK initialization API thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Backward tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) của SDK

Không nên hứa hỗ trợ (support / 지원) “mọi Kotlin/AGP phiên bản (version / 버전)”. Define tested hỗ trợ (support / 지원) phạm vi (range / 범위).

Kotlin siêu dữ liệu (metadata / 메타데이터)/trình biên dịch (compiler / 컴파일러) plugin changes có thể ảnh hưởng bên tiêu thụ (consumer / 소비자) compile. Android thư viện (library / 라이브러리) tài nguyên (resource / 자원)/manifest hành vi (behavior / 동작) cũng phụ thuộc AGP.

Bản phát hành (release / 릴리스) notes phải nêu minimum compileSdk/minSdk/JDK/AGP nếu thay đổi.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **39. SDK initialization API thiết kế (design / 설계)** nối từ **38. Backward tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) của SDK** sang **40. Multi-process SDK**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. SDK initialization API thiết kế (design / 설계)

Nếu cần tường minh (explicit / 명시적) init:

```kotlin
Sdk.initialize(
    context = applicationContext,
    config = SdkConfig(...)
)
```

Define:

- gọi nhiều lần idempotent không;
- luồng thực thi (thread / 스레드) nào được gọi;
- init async hay sync;
- lỗi cấu hình (config / 설정) trả thế nào;
- tiến trình (process / 프로세스) nào init;
- init trước use API nếu quên thì hành vi (behavior / 동작) gì.

Không để `lateinit global` crash ngẫu nhiên mà không đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **39. SDK initialization API thiết kế (design / 설계)** đặt đầu vào cho **40. Multi-process SDK**, rồi **41. Privacy và dữ liệu (data / 데이터) collection đặc tả hợp đồng (contract / 계약)** mở rộng hệ quả hoặc giới hạn liên quan.

## 40. Multi-process SDK

Nếu SDK có provider/dịch vụ (service / 서비스) tiến trình (process / 프로세스) riêng, trạng thái (state / 상태) không dùng chung (shared / 공유) như singleton bộ nhớ (memory / 메모리). DataStore/Room/dùng chung (shared / 공유) truy cập tệp (file access / 파일 접근) cần multi-process tính đúng đắn (correctness / 정확성) riêng.

Tránh multi-process nếu không required. SDK bên tiêu thụ (consumer / 소비자) thường không muốn thêm tiến trình (process / 프로세스) chỉ để thư viện (library / 라이브러리) tiện.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, cơ chế trong **40. Multi-process SDK** cần được kiểm chứng bằng dấu vết cụ thể; **41. Privacy và dữ liệu (data / 데이터) collection đặc tả hợp đồng (contract / 계약)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **42. bảo mật (security / 보안) surface của SDK** mở rộng hệ quả hoặc giới hạn liên quan.

## 41. Privacy và dữ liệu (data / 데이터) collection đặc tả hợp đồng (contract / 계약)

SDK analytics/ads/auth có thể thu dữ liệu (data / 데이터) thay app. bên tiêu thụ (consumer / 소비자) cần biết để khai dữ liệu (data / 데이터) an toàn (safety / 안전)/privacy chính sách (policy / 정책).

SDK nên document:

- dữ liệu (data / 데이터) fields collected;
- purpose;
- retention/upload;
- opt-out/cấu hình (config / 설정);
- permissions;
- mạng (network / 네트워크) domains;
- identifiers.

Privacy side tác động (effect / 효과) là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) ngang API signature.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **41. Privacy và dữ liệu (data / 데이터) collection đặc tả hợp đồng (contract / 계약)** đặt vấn đề; **42. bảo mật (security / 보안) surface của SDK** đối chiếu bằng chứng, rồi **43. Deprecation và di chuyển (migration / 마이그레이션)** mở rộng hệ quả hoặc giới hạn liên quan.

## 42. bảo mật (security / 보안) surface của SDK

Rà soát (review / 검토) exported components, WebView cầu nối (bridge / 브리지), PendingIntent mutability, tệp (file / 파일) URI/provider, certificate/TLS, đơn vị từ (token / 토큰) lưu trữ (storage / 저장소) và bản địa (native / 네이티브) parser.

Bên tiêu thụ (consumer / 소비자) app inherit attack surface thư viện (library / 라이브러리). Vì vậy bảo mật (security / 보안) patch cadence và vulnerability disclosure tiến trình (process / 프로세스) quan trọng với SDK công khai (public / 공개).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **43. Deprecation và di chuyển (migration / 마이그레이션)** nối từ **42. bảo mật (security / 보안) surface của SDK** sang **44. cờ tính năng (feature flag / 기능 플래그) trong SDK**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Deprecation và di chuyển (migration / 마이그레이션)

Không xóa API công khai (public API / 공개 API) ngay. Deprecate với replacement/di chuyển (migration / 마이그레이션) message:

```kotlin
@Deprecated(
    message = "Use authenticate(request) instead",
    replaceWith = ReplaceWith("authenticate(request)")
)
fun login(...)
```

Nếu replacement không mechanical, link di chuyển (migration / 마이그레이션) guide.

Deprecation cửa sổ (window / 윈도우) tùy chính sách (policy / 정책); quan trọng là bên tiêu thụ (consumer / 소비자) có thời gian và clear đường dẫn (path / 경로).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **44. cờ tính năng (feature flag / 기능 플래그) trong SDK** nối từ **43. Deprecation và di chuyển (migration / 마이그레이션)** sang **45. cấp cao (senior / 시니어) rà soát (review / 검토) checklist cho thư viện (library / 라이브러리) bản phát hành (release / 릴리스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. cờ tính năng (feature flag / 기능 플래그) trong SDK

Remote flag nội bộ SDK có thể thay hành vi (behavior / 동작) bên tiêu thụ (consumer / 소비자) ngoài phiên bản (version / 버전) upgrade, gây khó reproduce. Nếu dùng, flag cần khả năng quan sát (observability / 관측 가능성)/versioning và không được silently break đặc tả hợp đồng (contract / 계약).

Trọng yếu (critical / 중요) hành vi (behavior / 동작) nên consumer-configurable hoặc release-versioned thay vì hidden máy chủ (server / 서버) switch không document.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, **45. cấp cao (senior / 시니어) rà soát (review / 검토) checklist cho thư viện (library / 라이브러리) bản phát hành (release / 릴리스)** nối từ **44. cờ tính năng (feature flag / 기능 플래그) trong SDK** sang **46. Official references**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. cấp cao (senior / 시니어) rà soát (review / 검토) checklist cho thư viện (library / 라이브러리) bản phát hành (release / 릴리스)

Trước publish:

- API công khai (public API / 공개 API) diff đã rà soát (review / 검토) chưa;
- nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) check pass;
- minSdk/compile/toolchain yêu cầu (requirement / 요구사항) đổi không;
- transitive dependencies đổi gì;
- manifest/tài nguyên (resource / 자원)/permission footprint đổi không;
- bên tiêu thụ (consumer / 소비자) R8 rules tested chưa;
- bản phát hành (release / 릴리스) minified mẫu (sample / 표본) chạy chưa;
- Java interoperability ổn chưa;
- privacy/bảo mật (security / 보안) hành vi (behavior / 동작) đổi không;
- di chuyển (migration / 마이그레이션)/bản phát hành (release / 릴리스) ghi chú (note / 노트) đủ chưa;
- sản phẩm tạo ra (artifact / 산출물) immutable/provenance dấu vết (trace / 추적) được không.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 20 — Android thư viện (library / 라이브러리) và SDK Authoring: AAR, API công khai (public API / 공개 API), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) và Publishing**, sau nội dung của **45. cấp cao (senior / 시니어) rà soát (review / 검토) checklist cho thư viện (library / 라이브러리) bản phát hành (release / 릴리스)**, **46. Official references** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 46. Official references
Phần này nối mạch Android vừa học với “46. Official references”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

- Android thư viện (library / 라이브러리) modules: https://nhà phát triển (developer / 개발자).android.com/studio/projects/android-library
- Publish your thư viện (library / 라이브러리): https://nhà phát triển (developer / 개발자).android.com/bản dựng (build / 빌드)/publish-library
- bản dựng (build / 빌드) variants: https://nhà phát triển (developer / 개발자).android.com/bản dựng (build / 빌드)/build-variants
- R8: https://nhà phát triển (developer / 개발자).android.com/topic/hiệu năng (performance / 성능)/app-optimization
- Android Lint: https://nhà phát triển (developer / 개발자).android.com/studio/ghi (write / 쓰기)/lint

Library authoring là compatibility engineering dài hạn. API đẹp ở version 1.0 nhưng không có evolution strategy sẽ trở thành technical debt cho cả SDK team và mọi consumer.

> **Bàn giao:** Sau **46. Official references**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

# Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. API công khai (public API / 공개 API) là đặc tả hợp đồng (contract / 계약), không chỉ là public từ khóa (keyword / 키워드)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) khác nhau** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **1. API công khai (public API / 공개 API) là đặc tả hợp đồng (contract / 계약), không chỉ là public từ khóa (keyword / 키워드)** nêu điều cần giải thích; **2. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) khác nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Kotlin default argument có ABI implications** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **2. nguồn (source / 소스) tính tương thích (compatibility / 호환성) và nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) khác nhau** nêu điều cần giải thích; **3. Kotlin default argument có ABI implications** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. @JvmName, @JvmField, @JvmStatic thay đổi Java surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Default arguments ảnh hưởng ABI; `@JvmName`/`@JvmField`/`@JvmStatic` tiếp theo định hình Java surface, rồi nullability annotations trở thành contract cho Java consumers.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **4. @JvmName, @JvmField, @JvmStatic thay đổi Java surface** cho ta quy tắc; **5. Nullability annotation là đặc tả hợp đồng (contract / 계약) với Java bên tiêu thụ (consumer / 소비자)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **6. Expose giao diện (interface / 인터페이스), hide hiện thực (implementation / 구현) khi hiện thực (implementation / 구현) có thay đổi (change / 변경) axis lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Nullability annotation là đặc tả hợp đồng (contract / 계약) với Java bên tiêu thụ (consumer / 소비자)

Kotlin kiểu (type / 타입):

```kotlin
fun token(): String?
```

rõ nullability.

Java ranh giới (boundary / 경계) có thể mất một phần type-safety nếu annotation siêu dữ liệu (metadata / 메타데이터) không được preserve/understood.

SDK nên tránh ambiguous nền tảng (platform / 플랫폼) kiểu (type / 타입) trong API công khai (public API / 공개 API).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **5. Nullability annotation là đặc tả hợp đồng (contract / 계약) với Java bên tiêu thụ (consumer / 소비자)** cho ta quy tắc; **6. Expose giao diện (interface / 인터페이스), hide hiện thực (implementation / 구현) khi hiện thực (implementation / 구현) có thay đổi (change / 변경) axis lớn** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. công khai (public / 공개) mô hình (model / 모델) nên độc lập nội bộ (internal / 내부) vận chuyển (transport / 전송) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **7. công khai (public / 공개) mô hình (model / 모델) nên độc lập nội bộ (internal / 내부) vận chuyển (transport / 전송) mô hình (model / 모델)** tiếp nhận điểm tựa từ **6. Expose giao diện (interface / 인터페이스), hide hiện thực (implementation / 구현) khi hiện thực (implementation / 구현) có thay đổi (change / 변경) axis lớn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. phụ thuộc (dependency / 의존성) leakage mở rộng tính tương thích (compatibility / 호환성) surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **8. phụ thuộc (dependency / 의존성) leakage mở rộng tính tương thích (compatibility / 호환성) surface** tiếp nhận điểm tựa từ **7. công khai (public / 공개) mô hình (model / 모델) nên độc lập nội bộ (internal / 내부) vận chuyển (transport / 전송) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. api phụ thuộc (dependency / 의존성) có thể leak transitive surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. phụ thuộc (dependency / 의존성) leakage mở rộng tính tương thích (compatibility / 호환성) surface

Nếu công khai (public / 공개) phương thức (method / 메서드) trả kiểu (type / 타입) từ third-party thư viện (library / 라이브러리):

```kotlin
fun client(): okhttp3.OkHttpClient
```

SDK đã biến OkHttp phiên bản (version / 버전)/API thành part của công khai (public / 공개) đặc tả hợp đồng (contract / 계약).

Bên tiêu thụ (consumer / 소비자) có thể buộc phụ thuộc (dependency / 의존성) phiên bản (version / 버전) theo SDK hoặc gặp xung đột (conflict / 충돌).

Expose third-party kiểu (type / 타입) chỉ khi đó là intentional tích hợp (integration / 통합) surface.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **9. api phụ thuộc (dependency / 의존성) có thể leak transitive surface** tiếp nhận điểm tựa từ **8. phụ thuộc (dependency / 의존성) leakage mở rộng tính tương thích (compatibility / 호환성) surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) là bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. `api` phụ thuộc (dependency / 의존성) có thể leak transitive surface

Thư viện (library / 라이브러리) dùng Gradle `api(...)` khiến bên tiêu thụ (consumer / 소비자) compile thấy phụ thuộc (dependency / 의존성) đó.

`implementation(...)` giữ phụ thuộc (dependency / 의존성) private hơn.

Chọn `api` khi công khai (public / 공개) ABI thực sự cần, không vì bản dựng (build / 빌드) fix nhanh.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **10. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) là bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **9. api phụ thuộc (dependency / 의존성) có thể leak transitive surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Shading/relocation đôi khi cần nhưng có chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **11. Shading/relocation đôi khi cần nhưng có chi phí (cost / 비용)** tiếp nhận điểm tựa từ **10. phụ thuộc (dependency / 의존성) xung đột (conflict / 충돌) là bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Android tài nguyên (resource / 자원) cũng là công khai (public / 공개) surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Shading/relocation đôi khi cần nhưng có chi phí (cost / 비용)

Nếu SDK buộc dùng phụ thuộc (dependency / 의존성) dễ xung đột (conflict / 충돌), có thể relocate gói (package / 패키지) bằng shading.

Nhưng shading:

- tăng sản phẩm tạo ra (artifact / 산출물) kích thước (size / 크기),
- complicate license/bảo mật (security / 보안) updates,
- có thể break reflection/tài nguyên (resource / 자원) loading.

Dùng khi xung đột (conflict / 충돌) rủi ro (risk / 위험) thật, không mặc định.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **11. Shading/relocation đôi khi cần nhưng có chi phí (cost / 비용)** nêu điều cần giải thích; **12. Android tài nguyên (resource / 자원) cũng là công khai (public / 공개) surface** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Manifest contribution phải tối thiểu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **12. Android tài nguyên (resource / 자원) cũng là công khai (public / 공개) surface** nêu điều cần giải thích; **13. Manifest contribution phải tối thiểu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Auto-initialization là bên tiêu thụ (consumer / 소비자) startup debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **14. Auto-initialization là bên tiêu thụ (consumer / 소비자) startup debt** tiếp nhận điểm tựa từ **13. Manifest contribution phải tối thiểu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. SDK không được assume Activity tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Auto-initialization là bên tiêu thụ (consumer / 소비자) startup debt

SDK dùng ContentProvider để auto-init rất tiện nhưng chạy trên startup đường dẫn (path / 경로) bên tiêu thụ (consumer / 소비자).

Nếu initialization nặng, mọi app tích hợp đều trả độ trễ (latency / 지연 시간) chi phí (cost / 비용).

Ưu tiên lazy/on-demand khi tính năng (feature / 기능) không cần trước first tương tác (interaction / 상호작용).

Nếu auto-init cần thiết, keep công việc (work / 작업) tối thiểu.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **15. SDK không được assume Activity tồn tại** tiếp nhận điểm tựa từ **14. Auto-initialization là bên tiêu thụ (consumer / 소비자) startup debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. ngữ cảnh (context / 맥락) thời gian tồn tại (lifetime / 수명) phải rõ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **16. ngữ cảnh (context / 맥락) thời gian tồn tại (lifetime / 수명) phải rõ** tiếp nhận điểm tựa từ **15. SDK không được assume Activity tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Threading đặc tả hợp đồng (contract / 계약) phải document** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. ngữ cảnh (context / 맥락) thời gian tồn tại (lifetime / 수명) phải rõ

Không giữ Activity ngữ cảnh (context / 맥락) trong singleton.

Nếu SDK máy khách (client / 클라이언트) sống ứng dụng (application / 애플리케이션) thời gian tồn tại (lifetime / 수명), giữ `applicationContext` khi phù hợp.

Nếu cần Activity cho permission/UI, nhận ephemeral tham chiếu (reference / 참조) ở phương thức (method / 메서드) ranh giới (boundary / 경계) và không bộ nhớ đệm (cache / 캐시) lâu dài.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **17. Threading đặc tả hợp đồng (contract / 계약) phải document** tiếp nhận điểm tựa từ **16. ngữ cảnh (context / 맥락) thời gian tồn tại (lifetime / 수명) phải rõ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Suspend API nên main-safe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **18. Suspend API nên main-safe** tiếp nhận điểm tựa từ **17. Threading đặc tả hợp đồng (contract / 계약) phải document** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Callback cancellation cần tường minh (explicit / 명시적) handle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **19. Callback cancellation cần tường minh (explicit / 명시적) handle** tiếp nhận điểm tựa từ **18. Suspend API nên main-safe** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. luồng (flow / 흐름) API cần define hot/cold ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Callback cancellation cần tường minh (explicit / 명시적) handle

Nếu SDK expose callback API:

```kotlin
fun fetch(callback: Callback): RequestHandle
```

Bên tiêu thụ (consumer / 소비자) cần cách cancel khi vòng đời (lifecycle / 생명주기) kết thúc.

Không có cancel đường dẫn (path / 경로) dễ tạo stale callback/leak.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **19. Callback cancellation cần tường minh (explicit / 명시적) handle** xác định đầu vào; **20. luồng (flow / 흐름) API cần define hot/cold ngữ nghĩa (semantics / 의미론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. Exception kiểu (type / 타입) công khai (public / 공개) trở thành Đặc tả API (API contract / API 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **20. luồng (flow / 흐름) API cần define hot/cold ngữ nghĩa (semantics / 의미론)** xác định đầu vào; **21. Exception kiểu (type / 타입) công khai (public / 공개) trở thành Đặc tả API (API contract / API 계약)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약) phải phân biệt retryable/permanent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **22. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약) phải phân biệt retryable/permanent** tiếp nhận điểm tựa từ **21. Exception kiểu (type / 타입) công khai (public / 공개) trở thành Đặc tả API (API contract / API 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Logging trong SDK phải respect host privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **23. Logging trong SDK phải respect host privacy** tiếp nhận điểm tựa từ **22. lỗi (error / 오류) đặc tả hợp đồng (contract / 계약) phải phân biệt retryable/permanent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Telemetry SDK phải có backpressure/lưu trữ (storage / 저장소) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **24. Telemetry SDK phải có backpressure/lưu trữ (storage / 저장소) chính sách (policy / 정책)** tiếp nhận điểm tựa từ **23. Logging trong SDK phải respect host privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. SDK phải degrade gracefully khi host misconfigure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **25. SDK phải degrade gracefully khi host misconfigure** tiếp nhận điểm tựa từ **24. Telemetry SDK phải có backpressure/lưu trữ (storage / 저장소) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. bản địa (native / 네이티브) mã (code / 코드) làm thất bại (failure / 실패) ranh giới (boundary / 경계) nguy hiểm hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **25. SDK phải degrade gracefully khi host misconfigure** đã nêu tiêu chí phân biệt, còn **26. bản địa (native / 네이티브) mã (code / 코드) làm thất bại (failure / 실패) ranh giới (boundary / 경계) nguy hiểm hơn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **27. JNI cục bộ (local / 로컬)/toàn cục (global / 전역) tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **26. bản địa (native / 네이티브) mã (code / 코드) làm thất bại (failure / 실패) ranh giới (boundary / 경계) nguy hiểm hơn** đã nêu tiêu chí phân biệt, còn **27. JNI cục bộ (local / 로컬)/toàn cục (global / 전역) tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명) khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. JNIEnv gắn với luồng thực thi (thread / 스레드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. JNI cục bộ (local / 로컬)/toàn cục (global / 전역) tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명) khác nhau

Cục bộ (local / 로컬) tham chiếu (reference / 참조) thường chỉ valid trong bản địa (native / 네이티브) lời gọi (call / 호출)/frame.

Nếu giữ Java đối tượng (object / 객체) qua lời gọi (call / 호출), cần toàn cục (global / 전역) tham chiếu (reference / 참조) phù hợp và delete khi xong.

Giữ cục bộ (local / 로컬) ref lâu có thể use-after-lifetime; quên delete toàn cục (global / 전역) ref gây leak.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **28. JNIEnv gắn với luồng thực thi (thread / 스레드)** tiếp nhận điểm tựa từ **27. JNI cục bộ (local / 로컬)/toàn cục (global / 전역) tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Java exception từ JNI phải check** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `JNIEnv*` gắn với luồng thực thi (thread / 스레드)

Không bộ nhớ đệm (cache / 캐시) `JNIEnv*` từ luồng thực thi (thread / 스레드) A rồi dùng trên luồng thực thi (thread / 스레드) B.

Bản địa (native / 네이티브) luồng thực thi (thread / 스레드) cần attach JVM để lấy môi trường (environment / 환경) hợp lệ, rồi detach khi vòng đời (lifecycle / 생명주기) yêu cầu.

Luồng thực thi (thread / 스레드) quyền sở hữu (ownership / 소유권) là cốt lõi (core / 핵심) JNI bất biến (invariant / 불변식).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **29. Java exception từ JNI phải check** tiếp nhận điểm tựa từ **28. JNIEnv gắn với luồng thực thi (thread / 스레드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. bản địa (native / 네이티브) buffer quyền sở hữu (ownership / 소유권) phải tường minh (explicit / 명시적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Java exception từ JNI phải check

Nếu bản địa (native / 네이티브) gọi Java phương thức (method / 메서드) và Java throw, JNI có pending exception.

Tiếp tục gọi API khác khi exception pending có thể gây hành vi (behavior / 동작) khó đoán.

Bản địa (native / 네이티브) cầu nối (bridge / 브리지) nên check/propagate/clear theo đặc tả hợp đồng (contract / 계약) đúng.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, sau nội dung của **29. Java exception từ JNI phải check**, **30. bản địa (native / 네이티브) buffer quyền sở hữu (ownership / 소유권) phải tường minh (explicit / 명시적)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **31. ABI split ảnh hưởng phân phối (distribution / 분포) và testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **31. ABI split ảnh hưởng phân phối (distribution / 분포) và testing** tiếp nhận điểm tựa từ **30. bản địa (native / 네이티브) buffer quyền sở hữu (ownership / 소유권) phải tường minh (explicit / 명시적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. bản địa (native / 네이티브) symbolication là môi trường vận hành (production / 운영 환경) yêu cầu (requirement / 요구사항)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **32. bản địa (native / 네이티브) symbolication là môi trường vận hành (production / 운영 환경) yêu cầu (requirement / 요구사항)** tiếp nhận điểm tựa từ **31. ABI split ảnh hưởng phân phối (distribution / 분포) và testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Sanitizer hữu ích để bắt bộ nhớ (memory / 메모리) bug trước môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. bản địa (native / 네이티브) symbolication là môi trường vận hành (production / 운영 환경) yêu cầu (requirement / 요구사항)

Crash address:

```text
#00 pc 00000000001234 libfoo.so
```

không hữu ích nếu không có symbol ánh xạ (mapping / 매핑)/hiện vật bản dựng (build artifact / 빌드 산출물) tương ứng.

Bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인) phải archive/upload bản địa (native / 네이티브) symbols theo phiên bản (version / 버전)/bản dựng (build / 빌드) id.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **33. Sanitizer hữu ích để bắt bộ nhớ (memory / 메모리) bug trước môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **32. bản địa (native / 네이티브) symbolication là môi trường vận hành (production / 운영 환경) yêu cầu (requirement / 요구사항)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. 16 KB page-size tính tương thích (compatibility / 호환성) là bản địa (native / 네이티브) packaging/thời gian chạy (runtime / 런타임) concern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Sanitizer hữu ích để bắt bộ nhớ (memory / 메모리) bug trước môi trường vận hành (production / 운영 환경)

Address/UndefinedBehavior sanitizer hoặc tooling tương ứng giúp bắt:

```text
use-after-free
buffer overflow
undefined behavior
```

Bản địa (native / 네이티브) bộ nhớ (memory / 메모리) bug hiếm nhưng blast radius lớn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **34. 16 KB page-size tính tương thích (compatibility / 호환성) là bản địa (native / 네이티브) packaging/thời gian chạy (runtime / 런타임) concern** tiếp nhận điểm tựa từ **33. Sanitizer hữu ích để bắt bộ nhớ (memory / 메모리) bug trước môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. bản địa (native / 네이티브) mã (code / 코드) nên được dùng khi lợi ích rõ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. 16 KB page-size tính tương thích (compatibility / 호환성) là bản địa (native / 네이티브) packaging/thời gian chạy (runtime / 런타임) concern

Hiện đại (modern / 현대적) Android thiết bị (device / 장치) ecosystem có thể dùng page kích thước (size / 크기) khác 4 KB.

Bản địa (native / 네이티브) thư viện (library / 라이브러리) bản dựng (build / 빌드)/link alignment phải compatible.

Nếu SDK ship prebuilt `.so`, SDK author chịu trách nhiệm kiểm tra nhị phân (binary / 이진) của mình, không đẩy rủi ro (risk / 위험) cho bên tiêu thụ (consumer / 소비자) app.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **35. bản địa (native / 네이티브) mã (code / 코드) nên được dùng khi lợi ích rõ** tiếp nhận điểm tựa từ **34. 16 KB page-size tính tương thích (compatibility / 호환성) là bản địa (native / 네이티브) packaging/thời gian chạy (runtime / 런타임) concern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. JNI ranh giới (boundary / 경계) nên coarse-grained** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **35. bản địa (native / 네이티브) mã (code / 코드) nên được dùng khi lợi ích rõ** đã nêu tiêu chí phân biệt, còn **36. JNI ranh giới (boundary / 경계) nên coarse-grained** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **37. công khai (public / 공개) bản địa (native / 네이티브) ABI và nội bộ (internal / 내부) bản địa (native / 네이티브) ABI khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **36. JNI ranh giới (boundary / 경계) nên coarse-grained** đã nêu tiêu chí phân biệt, còn **37. công khai (public / 공개) bản địa (native / 네이티브) ABI và nội bộ (internal / 내부) bản địa (native / 네이티브) ABI khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **38. Deprecation nên có di chuyển (migration / 마이그레이션) đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. công khai (public / 공개) bản địa (native / 네이티브) ABI và nội bộ (internal / 내부) bản địa (native / 네이티브) ABI khác nhau

Nếu SDK expose C API cho third party, ABI stability trở thành đặc tả hợp đồng (contract / 계약) dài hạn.

Nếu bản địa (native / 네이티브) chỉ nội bộ (internal / 내부) sau JNI, có thể refactor tự do hơn miễn Java/Kotlin API ổn định.

Giữ bản địa (native / 네이티브) hiện thực (implementation / 구현) private nếu không cần bên ngoài (external / 외부) ABI.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **37. công khai (public / 공개) bản địa (native / 네이티브) ABI và nội bộ (internal / 내부) bản địa (native / 네이티브) ABI khác nhau** xác định đầu vào; **38. Deprecation nên có di chuyển (migration / 마이그레이션) đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **39. Removal cần bản phát hành (release / 릴리스) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **38. Deprecation nên có di chuyển (migration / 마이그레이션) đường dẫn (path / 경로)** xác định đầu vào; **39. Removal cần bản phát hành (release / 릴리스) chính sách (policy / 정책)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **40. Behavioral tính tương thích (compatibility / 호환성) quan trọng không kém signature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **40. Behavioral tính tương thích (compatibility / 호환성) quan trọng không kém signature** tiếp nhận điểm tựa từ **39. Removal cần bản phát hành (release / 릴리스) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. hiệu năng (performance / 성능) regression của SDK là externalized chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **41. hiệu năng (performance / 성능) regression của SDK là externalized chi phí (cost / 비용)** tiếp nhận điểm tựa từ **40. Behavioral tính tương thích (compatibility / 호환성) quan trọng không kém signature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. SDK kích thước (size / 크기) ngân sách (budget / 예산) cần nhánh học (track / 트랙) transitive chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **42. SDK kích thước (size / 크기) ngân sách (budget / 예산) cần nhánh học (track / 트랙) transitive chi phí (cost / 비용)** tiếp nhận điểm tựa từ **41. hiệu năng (performance / 성능) regression của SDK là externalized chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Custom Lint giúp encode tích hợp (integration / 통합) quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. SDK kích thước (size / 크기) ngân sách (budget / 예산) cần nhánh học (track / 트랙) transitive chi phí (cost / 비용)

AAR 100 KB nhưng kéo phụ thuộc (dependency / 의존성) 5 MB vẫn làm bên tiêu thụ (consumer / 소비자) sản phẩm tạo ra (artifact / 산출물) lớn.

Measure final bên tiêu thụ (consumer / 소비자) impact, không chỉ tệp (file / 파일) AAR.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **43. Custom Lint giúp encode tích hợp (integration / 통합) quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **42. SDK kích thước (size / 크기) ngân sách (budget / 예산) cần nhánh học (track / 트랙) transitive chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. SDK mẫu (sample / 표본) app phải là real bên tiêu thụ (consumer / 소비자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **44. SDK mẫu (sample / 표본) app phải là real bên tiêu thụ (consumer / 소비자)** tiếp nhận điểm tựa từ **43. Custom Lint giúp encode tích hợp (integration / 통합) quy tắc (rule / 규칙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) nên compile old bên tiêu thụ (consumer / 소비자) against new SDK** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **45. tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) nên compile old bên tiêu thụ (consumer / 소비자) against new SDK** tiếp nhận điểm tựa từ **44. SDK mẫu (sample / 표본) app phải là real bên tiêu thụ (consumer / 소비자)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. API dump giúp rà soát (review / 검토) accidental công khai (public / 공개) surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **46. API dump giúp rà soát (review / 검토) accidental công khai (public / 공개) surface** tiếp nhận điểm tựa từ **45. tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) nên compile old bên tiêu thụ (consumer / 소비자) against new SDK** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Consumer-driven tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **47. Consumer-driven tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **46. API dump giúp rà soát (review / 검토) accidental công khai (public / 공개) surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. bảo mật (security / 보안) cập nhật (update / 업데이트) có thể buộc tính tương thích (compatibility / 호환성) sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **48. bảo mật (security / 보안) cập nhật (update / 업데이트) có thể buộc tính tương thích (compatibility / 호환성) sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **47. Consumer-driven tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) provenance cho SDK** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **49. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) provenance cho SDK** tiếp nhận điểm tựa từ **48. bảo mật (security / 보안) cập nhật (update / 업데이트) có thể buộc tính tương thích (compatibility / 호환성) sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. SDK reliability checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **50. SDK reliability checklist** tiếp nhận điểm tựa từ **49. bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) provenance cho SDK** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. SDK reliability checklist
Phần này nối mạch Android vừa học với “50. SDK reliability checklist”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

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

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 07 — SDK Authoring, bản địa (native / 네이티브) ranh giới (boundary / 경계), API Evolution và bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전)**, **51. Kết luận** gom các mảnh từ **50. SDK reliability checklist** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

Application code có thể sửa theo cadence của chính team. SDK code phải sống cùng cadence của nhiều consumer, vì vậy mỗi public decision đều có chi phí dài hạn.

> **Bàn giao:** Sau **51. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

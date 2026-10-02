# Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)

> **Mạch đọc:** [README](./README.md) là owner của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**; đặt case sau runtime/process và trước performance/release. Từ **1. Cold, warm và hot start là ba tình huống khác nhau** nối critical path, Application/ContentProvider/DI initialization, first useful frame, lazy work và startup measurement, rồi dùng dependency/lifetime evidence để tối ưu thay vì dồn mọi thứ vào `Application.onCreate()`.

Một app có thể có kiến trúc (architecture / 아키텍처) sạch nhưng vẫn tạo trải nghiệm tệ nếu cold start chậm, initialization chạy sai luồng thực thi (thread / 스레드), SDK tự động khởi tạo quá sớm hoặc splash screen che một main-thread stall dài. Startup là nơi nhiều subsystem cùng tranh thời gian: tiến trình (process / 프로세스) creation, nạp lớp (class loading / 클래스 로딩), `Application`, ContentProvider auto-init, DI đồ thị (graph / 그래프), cơ sở dữ liệu (database / 데이터베이스)/mạng (network / 네트워크) cấu hình (config / 설정), Compose first frame và analytics/crash SDK.

Chapter này xây mô hình tư duy (mental model / 사고 모델) startup từ OS tiến trình (process / 프로세스) tới first useful frame, sau đó thiết kế initialization theo phụ thuộc (dependency / 의존성)/thời gian tồn tại (lifetime / 수명) thay vì “nhét hết vào `Application.onCreate()`”.

## 1. Cold, warm và hot start là ba tình huống khác nhau

**Cold start**: tiến trình (process / 프로세스) chưa tồn tại. hệ thống (system / 시스템) phải tạo tiến trình (process / 프로세스), thời gian chạy (runtime / 런타임), ứng dụng (application / 애플리케이션) và Activity trước khi kết xuất (render / 렌더링) UI.

**Warm start**: tiến trình (process / 프로세스) còn nhưng Activity cần recreate hoặc app quay lại từ trạng thái (state / 상태) không còn UI fully resident.

**Hot start**: Activity/tác vụ (task / 작업) còn gần như sẵn, resume nhanh.

Khi nói “startup 800 ms”, phải nói scenario nào. Tối ưu hot start không giải cold-start regression.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **1. Cold, warm và hot start là ba tình huống khác nhau** cho ta quy tắc; **2. Startup đường găng (critical path / 임계 경로)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **3. thời gian (time / 시간) to Initial Display và thời gian (time / 시간) to Full Display** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Startup đường găng (critical path / 임계 경로)

Một mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
launcher tap/deep link/notification
→ process creation nếu cần
→ runtime/class loading
→ Application creation
→ auto-initializers/providers
→ Activity creation
→ theme/splash
→ Compose/View inflate
→ first frame
→ content/data ready
```

Không phải mọi bước đều chạy tuần tự tuyệt đối, nhưng mô hình (model / 모델) đủ để hỏi “công việc (work / 작업) này có nằm trên đường dẫn (path / 경로) đến first frame không?”.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **2. Startup đường găng (critical path / 임계 경로)** xác định đầu vào; **3. thời gian (time / 시간) to Initial Display và thời gian (time / 시간) to Full Display** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Application.onCreate() là toàn cục (global / 전역) startup hotspot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. thời gian (time / 시간) to Initial Display và thời gian (time / 시간) to Full Display

**TTID** phản ánh thời gian tới frame đầu tiên meaningful enough để hiển thị. **TTFD** phản ánh thời gian tới khi UI thực sự ready với content quan trọng.

Một app có thể TTID đẹp bằng cách kết xuất (render / 렌더링) skeleton sớm nhưng TTFD rất chậm. sản phẩm (product / 제품) hiệu năng (performance / 성능) nên theo cả perceived readiness, không chỉ launcher-to-first-pixel.

> **Chuyển mạch:** Tách TTID khỏi TTFD để biết startup bottleneck; `Application.onCreate()` là global hotspot, còn ContentProvider auto-init thêm work trước first frame.

## 4. `Application.onCreate()` là toàn cục (global / 전역) startup hotspot

`Application.onCreate()` chạy sớm trên main luồng thực thi (thread / 스레드) của tiến trình (process / 프로세스). mã (code / 코드) blocking ở đây trì hoãn mọi entry điểm (point / 지점).

Không nên:

- open/migrate cơ sở dữ liệu (database / 데이터베이스) nặng synchronous;
- đọc tệp (file / 파일) lớn;
- mạng (network / 네트워크) lời gọi (call / 호출);
- parse cấu hình (config / 설정) lớn;
- eagerly create mọi repository/dịch vụ (service / 서비스);
- initialize SDK không cần cho first screen.

Toàn cục (global / 전역) initialization phải nhỏ, deterministic và main-safe.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **5. ContentProvider auto-initialization** tiếp nhận điểm tựa từ **4. Application.onCreate() là toàn cục (global / 전역) startup hotspot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. AndroidX App Startup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. ContentProvider auto-initialization

Nhiều libraries dùng `ContentProvider` để auto-init trước/around ứng dụng (application / 애플리케이션) startup. Điều này tiện nhưng khiến công việc (work / 작업) xuất hiện ngoài `Application.onCreate()`.

Khi startup chậm, inspect merged manifest và dấu vết (trace / 추적) providers. Một SDK có thể add provider qua manifest phụ thuộc (dependency / 의존성).

Không kết luận `Application` nhẹ nghĩa startup nhẹ.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **6. AndroidX App Startup** tiếp nhận điểm tựa từ **5. ContentProvider auto-initialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Eager vs lazy initialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. AndroidX App Startup

AndroidX Startup cung cấp cách khai báo initializer phụ thuộc (dependency / 의존성) và centralize initialization đồ thị (graph / 그래프). Nó hữu ích khi nhiều thành phần (component / 컴포넌트) cần ordered initialization.

Concept:

```kotlin
class AnalyticsInitializer : Initializer<Analytics> {
    override fun create(context: Context): Analytics {
        return Analytics.create(context)
    }

    override fun dependencies(): List<Class<out Initializer<*>>> = emptyList()
}
```

Tuy nhiên khung phần mềm (framework / 프레임워크) không biến heavy công việc (work / 작업) thành free. Nếu initializer vẫn làm disk I/O trên main luồng thực thi (thread / 스레드), startup vẫn chậm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **7. Eager vs lazy initialization** tiếp nhận điểm tựa từ **6. AndroidX App Startup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và initialization đồ thị (graph / 그래프) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Eager vs lazy initialization

Một phụ thuộc (dependency / 의존성) nên eager chỉ nếu:

- mọi entry điểm (point / 지점) cần nó ngay;
- initialization rất rẻ;
- delay sẽ gây race/tính đúng đắn (correctness / 정확성) issue khó hơn.

Lazy tốt khi feature-specific hoặc expensive. Nhưng lazy không đồng nghĩa “first use muốn khối (block / 블록) bao lâu cũng được”. Nếu người dùng (user / 사용자) mở tính năng (feature / 기능), độ trễ (latency / 지연 시간) vẫn tồn tại—chỉ chuyển vị trí.

Có thể prewarm sau first frame hoặc khi thiết bị (device / 장치) idle phù hợp.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **8. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và initialization đồ thị (graph / 그래프) khác nhau** tiếp nhận điểm tựa từ **7. Eager vs lazy initialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Hilt/Dagger startup chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và initialization đồ thị (graph / 그래프) khác nhau

DI đồ thị (graph / 그래프) nói đối tượng (object / 객체) phụ thuộc đối tượng (object / 객체) nào. Initialization đồ thị (graph / 그래프) nói side tác động (effect / 효과) nào phải hoàn thành trước side tác động (effect / 효과) khác.

Một singleton `Database` có thể được inject lazy nhưng lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) vẫn là expensive initialization lúc first open.

Một analytics giao diện (interface / 인터페이스) có thể available sớm nhưng backend upload worker init sau.

Không dùng DI khung phần mềm (framework / 프레임워크) như implicit startup scheduler.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **9. Hilt/Dagger startup chi phí (cost / 비용)** tiếp nhận điểm tựa từ **8. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và initialization đồ thị (graph / 그래프) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. SplashScreen API** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Hilt/Dagger startup chi phí (cost / 비용)

Generated DI thường efficient nhưng đối tượng (object / 객체) đồ thị (graph / 그래프) lớn/eager singleton constructors có thể tạo chi phí (cost / 비용). Constructor nên gán phụ thuộc (dependency / 의존성), không làm I/O hoặc heavy computation.

Anti-pattern:

```kotlin
@Singleton
class UserRepository @Inject constructor(
    db: AppDatabase
) {
    init {
        runBlocking { /* load everything */ }
    }
}
```

Constructor side effects làm creation đường dẫn (path / 경로) khó kiểm soát và kiểm thử (test / 테스트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **10. SplashScreen API** tiếp nhận điểm tựa từ **9. Hilt/Dagger startup chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Startup tuyến (route / 경로): auth trạng thái (state / 상태) và deep link** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. SplashScreen API

Hiện đại (modern / 현대적) Android có SplashScreen API/hệ thống (system / 시스템) splash hành vi (behavior / 동작). Splash là visual chuyển tiếp (transition / 전이) trong startup, không phải license để khối (block / 블록) main luồng thực thi (thread / 스레드).

Nếu cần giữ splash tới điều kiện (condition / 조건), điều kiện (condition / 조건) phải ngắn và bounded. Long authentication/mạng (network / 네트워크) sync nên chuyển sang real loading UI.

Một splash đứng 5 giây vẫn là app chậm dù animation đẹp.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **11. Startup tuyến (route / 경로): auth trạng thái (state / 상태) và deep link** tiếp nhận điểm tựa từ **10. SplashScreen API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. cục bộ (local / 로컬) trạng thái (state / 상태) đọc bao nhiêu là đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Startup tuyến (route / 경로): auth trạng thái (state / 상태) và deep link

App thường phải quyết định tuyến (route / 경로) đầu:

```text
cold start
→ restore session locally
→ resolve incoming intent/deep link
→ decide auth gate
→ render route
```

Không cần gọi backend trước khi kết xuất (render / 렌더링) nếu cục bộ (local / 로컬) durable session siêu dữ liệu (metadata / 메타데이터) đủ quyết định provisional tuyến (route / 경로). mạng (network / 네트워크) kiểm tra hợp lệ (validation / 검증) có thể cập nhật (update / 업데이트) sau với correct chuyển tiếp trạng thái (state transition / 상태 전이).

Trường hợp (case / 사례) 02/04 đã cover auth/điều hướng (navigation / 내비게이션); startup đặt chúng trên đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **12. cục bộ (local / 로컬) trạng thái (state / 상태) đọc bao nhiêu là đủ** tiếp nhận điểm tựa từ **11. Startup tuyến (route / 경로): auth trạng thái (state / 상태) và deep link** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Main luồng thực thi (thread / 스레드) và disk I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. cục bộ (local / 로컬) trạng thái (state / 상태) đọc bao nhiêu là đủ

DataStore/Room read nhỏ có thể cần để quyết tuyến (route / 경로), nhưng loading toàn profile/feed cơ sở dữ liệu (database / 데이터베이스) trước frame là không cần.

Tách:

- **startup-critical trạng thái (state / 상태)**: theme, account existence, onboarding completed, pending tuyến (route / 경로);
- **screen dữ liệu (data / 데이터)**: tải (load / 로드) sau khi UI đơn vị sở hữu (owner / 오너) xuất hiện.

Minimize startup-critical dataset.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **13. Main luồng thực thi (thread / 스레드) và disk I/O** tiếp nhận điểm tựa từ **12. cục bộ (local / 로컬) trạng thái (state / 상태) đọc bao nhiêu là đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. nạp lớp (class loading / 클래스 로딩) và static initialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Main luồng thực thi (thread / 스레드) và disk I/O

Disk I/O độ trễ (latency / 지연 시간) có tail lớn tùy thiết bị (device / 장치)/lưu trữ (storage / 저장소) pressure. Nếu API cho synchronous disk read trong startup, hãy xem dấu vết (trace / 추적)/StrictMode.

Một read “chỉ 5 ms trên điểm ảnh (pixel / 픽셀) dev” có thể 100+ ms trên low-end thiết bị (device / 장치) dưới I/O contention.

Môi trường vận hành (production / 운영 환경) hiệu năng (performance / 성능) phải quan tâm percentile, không chỉ median nhà phát triển (developer / 개발자) phone.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **14. nạp lớp (class loading / 클래스 로딩) và static initialization** tiếp nhận điểm tựa từ **13. Main luồng thực thi (thread / 스레드) và disk I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Compose first composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. nạp lớp (class loading / 클래스 로딩) và static initialization

Large lớp (class / 클래스) đồ thị (graph / 그래프), static initializer và reflection có thể tăng startup.

Kotlin `object`, top-level thuộc tính (property / 속성) hoặc companion static initialization có thể tạo công việc (work / 작업) lúc lớp (class / 클래스) tải (load / 로드).

Không đặt heavy expression vào toàn cục (global / 전역) thuộc tính (property / 속성):

```kotlin
val expensiveConfig = parseHugeConfig(loadFile()) // bad as implicit class init
```

Prefer tường minh (explicit / 명시적)/lazy lifecycle-controlled creation.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **15. Compose first composition** tiếp nhận điểm tựa từ **14. nạp lớp (class loading / 클래스 로딩) và static initialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Baseline Profiles** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Compose first composition

Compose startup gồm Activity setup, composition, bố cục (layout / 레이아웃), draw và potential tài nguyên (resource / 자원)/font/ảnh (image / 이미지) công việc (work / 작업).

First screen nên tránh:

- huge danh sách (list / 목록) computation synchronous trong composable;
- decoding bitmap lớn trên main;
- creating unstable giant trạng thái (state / 상태) đồ thị (graph / 그래프);
- tác động (effect / 효과) launch gây immediate recomposition storm;
- reading disk directly trong composable.

UI nên kết xuất (render / 렌더링) from already modeled trạng thái (state / 상태); async tải (load / 로드) thuộc ViewModel/repository tầng (layer / 계층).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **16. Baseline Profiles** tiếp nhận điểm tựa từ **15. Compose first composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Macrobenchmark startup đo lường (measurement / 측정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Baseline Profiles

Baseline Profile cho thời gian chạy (runtime / 런타임) biết mã (code / 코드) paths quan trọng để cải thiện compilation/startup/thời gian chạy (runtime / 런타임) hiệu năng (performance / 성능). Đây không phải magic replacement cho slow thuật toán (algorithm / 알고리즘)/main-thread I/O.

Profile nên cover representative startup/trọng yếu (critical / 중요) journeys. Macrobenchmark đo benefit với profile enabled/disabled.

Nếu app startup 2 giây do mạng (network / 네트워크) blocking main luồng thực thi (thread / 스레드), Baseline Profile không sửa kiến trúc (architecture / 아키텍처) lỗi (error / 오류) đó.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **16. Baseline Profiles** nêu điều cần giải thích; **17. Macrobenchmark startup đo lường (measurement / 측정)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Macrobenchmark startup đo lường (measurement / 측정)

Macrobenchmark có thể đo cold/warm startup trên release-like bản dựng (build / 빌드).

Key principle:

```text
benchmark production-like artifact
+ representative device
+ repeated iteration
+ controlled compilation mode
```

Gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) timing không đại diện bản phát hành (release / 릴리스) vì instrumentation/JIT/minification khác.

Theo dõi percentile/phân phối (distribution / 분포), không chỉ một run.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **17. Macrobenchmark startup đo lường (measurement / 측정)** nêu điều cần giải thích; **18. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. StrictMode trong development** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)

Khi startup chậm, dấu vết (trace / 추적) cho bằng chứng (evidence / 증거) về main luồng thực thi (thread / 스레드) slices, binder calls, disk I/O, GC, nạp lớp (class loading / 클래스 로딩), rendering và scheduler.

Workflow:

```text
measure regression
→ capture trace
→ locate critical path
→ identify blocking work
→ move/remove/defer
→ remeasure
```

Không optimize bằng cảm giác hoặc số log timestamps rời rạc nếu Perfetto có thể cho timeline đầy đủ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **19. StrictMode trong development** tiếp nhận điểm tựa từ **18. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. SDK initialization quản trị (governance / 거버넌스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. StrictMode trong development

StrictMode giúp detect disk/mạng (network / 네트워크) thao tác (operation / 연산) trên main luồng thực thi (thread / 스레드) và một số tài nguyên (resource / 자원) misuse. Bật chính sách (policy / 정책) phù hợp trong gỡ lỗi (debug / 디버그)/dev giúp bắt startup anti-pattern sớm.

Không dùng StrictMode penalty làm môi trường vận hành (production / 운영 환경) crash cơ chế (mechanism / 메커니즘) tùy tiện. Mục tiêu là development tín hiệu (signal / 신호).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **20. SDK initialization quản trị (governance / 거버넌스)** tiếp nhận điểm tựa từ **19. StrictMode trong development** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Crash reporting nên init sớm nhưng nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. SDK initialization quản trị (governance / 거버넌스)

Mỗi third-party SDK thêm startup mã (code / 코드) cần đơn vị sở hữu (owner / 오너) và ngân sách (budget / 예산).

Inventory nên ghi:

| SDK | Need before first frame? | Auto provider? | Main-thread chi phí (cost / 비용) | Can lazy-init? | đơn vị sở hữu (owner / 오너) |
|---|---|---|---|---|---|
| crash reporting | often early | maybe | measure | partially | nền tảng (platform / 플랫폼) |
| analytics | usually no hard khối (block / 블록) | maybe | measure | yes | dữ liệu (data / 데이터) |
| ads | screen-specific | often | potentially high | yes | monetization |

Không để 10 SDK cùng tự auto-init vì vendor default.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **21. Crash reporting nên init sớm nhưng nhỏ** tiếp nhận điểm tựa từ **20. SDK initialization quản trị (governance / 거버넌스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Remote cấu hình (config / 설정) không được là hard startup phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Crash reporting nên init sớm nhưng nhỏ

Crash SDK cần available đủ sớm để capture startup crash, nhưng cấu hình (configuration / 구성) không nên perform heavy mạng (network / 네트워크)/remote fetch synchronously.

Upload có thể defer/background. Crash siêu dữ liệu (metadata / 메타데이터) trọng yếu (critical / 중요) có thể set sau khi cục bộ (local / 로컬) người dùng (user / 사용자)/session known.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **22. Remote cấu hình (config / 설정) không được là hard startup phụ thuộc (dependency / 의존성)** tiếp nhận điểm tựa từ **21. Crash reporting nên init sớm nhưng nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) trên startup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Remote cấu hình (config / 설정) không được là hard startup phụ thuộc (dependency / 의존성)

Nếu app cần mạng (network / 네트워크) Remote cấu hình (config / 설정) trước khi kết xuất (render / 렌더링), outage cấu hình (config / 설정) dịch vụ (service / 서비스) có thể làm app không mở.

Use cached defaults/cục bộ (local / 로컬) persisted cấu hình (config / 설정) và refresh async. trọng yếu (critical / 중요) kill-switch cần previous known trạng thái (state / 상태) và safe default.

Startup phải resilient khi mạng (network / 네트워크) offline.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **22. Remote cấu hình (config / 설정) không được là hard startup phụ thuộc (dependency / 의존성)** nêu điều cần giải thích; **23. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) trên startup** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Process-specific initialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) trên startup

Room DB first open có thể chạy di chuyển (migration / 마이그레이션). Large di chuyển (migration / 마이그레이션) ngay khi người dùng (user / 사용자) launch tạo long startup hoặc ANR nếu sai luồng thực thi (thread / 스레드).

Lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) nên:

- benchmark realistic DB kích thước (size / 크기);
- avoid unnecessary full-table rewrite;
- run via correct luồng thực thi (thread / 스레드) đường dẫn (path / 경로);
- show durable di chuyển (migration / 마이그레이션)/loading UX nếu truly long;
- backup/quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성) đã được trường hợp (case / 사례) 03 cover.

“di chuyển (migration / 마이그레이션) chỉ chạy một lần” không làm người dùng (user / 사용자) experience ít quan trọng.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **23. cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) trên startup** nêu điều cần giải thích; **24. Process-specific initialization** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Startup entry points không chỉ launcher icon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Process-specific initialization

Nếu app có multi-process thành phần (component / 컴포넌트), `Application.onCreate()` có thể chạy trong nhiều tiến trình (process / 프로세스).

Không giả định mã (code / 코드) startup chỉ chạy main app tiến trình (process / 프로세스). Heavy analytics/cơ sở dữ liệu (database / 데이터베이스) initialization có thể bị duplicate ở dịch vụ (service / 서비스)/provider tiến trình (process / 프로세스).

Nếu multi-process thật sự cần, detect tiến trình (process / 프로세스) name và initialize only required subsystem per tiến trình (process / 프로세스). Tránh multi-process trừ khi yêu cầu (requirement / 요구사항) rõ vì độ phức tạp (complexity / 복잡도) tăng mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **24. Process-specific initialization** xác định đầu vào; **25. Startup entry points không chỉ launcher icon** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **26. Lazy singleton race** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Startup entry points không chỉ launcher icon

Cold start có thể đến từ:

- launcher;
- notification tap;
- deep link/App Link;
- share intent;
- widget;
- shortcut;
- dịch vụ (service / 서비스)/receiver/provider.

Trường hợp (case / 사례) 14 đã cover hệ thống (system / 시스템) surfaces. Startup thiết kế (design / 설계) phải đảm bảo initialization thứ tự (order / 순서) đúng cho tất cả entry điểm (point / 지점), không chỉ MainActivity đường dẫn (path / 경로).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **26. Lazy singleton race** tiếp nhận điểm tựa từ **25. Startup entry points không chỉ launcher icon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Prewarming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Lazy singleton race

Lazy initialize dùng chung (shared / 공유) tài nguyên (resource / 자원) từ nhiều threads cần thread-safety. Kotlin `lazy` default synchronized ngữ nghĩa (semantics / 의미론) có thể đủ cho đối tượng (object / 객체) initialization đơn giản, nhưng async initialization cần máy trạng thái (state machine / 상태 머신).

Không dùng nullable toàn cục (global / 전역) + `if (x == null) x = create()` unsynchronized.

Async tài nguyên (resource / 자원) có thể mô hình (model / 모델):

```text
Uninitialized
→ Initializing(deferred)
→ Ready
→ Failed(retry policy)
```

Multiple callers await cùng initialization thay vì chạy duplicate.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **27. Prewarming** tiếp nhận điểm tựa từ **26. Lazy singleton race** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Startup bộ nhớ (memory / 메모리) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Prewarming

Sau first frame, app có thể prewarm tài nguyên (resource / 자원) có xác suất sắp dùng cao: cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결), decoder, bộ nhớ đệm (cache / 캐시) chỉ mục (index / 인덱스), tính năng (feature / 기능) mô-đun (module / 모듈).

Prewarm là speculation. Nếu làm quá nhiều sẽ tranh CPU/I/O với người dùng (user / 사용자) tương tác (interaction / 상호작용) và tăng battery.

Chỉ prewarm thứ có measured benefit và bounded chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **28. Startup bộ nhớ (memory / 메모리) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **27. Prewarming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Startup mạng (network / 네트워크) anti-pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Startup bộ nhớ (memory / 메모리) ngân sách (budget / 예산)

Eager initialization không chỉ tốn thời gian, còn tăng resident bộ nhớ (memory / 메모리). Low-end thiết bị (device / 장치) có thể bị bộ nhớ (memory / 메모리) pressure sớm.

Một SDK singleton có bộ nhớ đệm (cache / 캐시) 20 MB “để nhanh” có thể làm tiến trình (process / 프로세스) dễ kill background hơn.

Startup tối ưu hóa (optimization / 최적화) nên xem thời gian (time / 시간) + bộ nhớ (memory / 메모리) + battery sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **29. Startup mạng (network / 네트워크) anti-pattern** tiếp nhận điểm tựa từ **28. Startup bộ nhớ (memory / 메모리) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. First frame vs first useful content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Startup mạng (network / 네트워크) anti-pattern

Never require mạng (network / 네트워크) round trip để app tiến trình (process / 프로세스) trở thành usable nếu sản phẩm (product / 제품) có thể kết xuất (render / 렌더링) offline/cached trạng thái (state / 상태).

Mạng (network / 네트워크) có unbounded tail: DNS, TLS, captive portal, packet mất mát (loss / 손실), máy chủ (server / 서버) độ trễ (latency / 지연 시간).

Nếu bảo mật (security / 보안) requires fresh máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증) trước sensitive hành động (action / 동작), gate **sensitive hành động (action / 동작)**, không nhất thiết gate toàn app shell.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **30. First frame vs first useful content** tiếp nhận điểm tựa từ **29. Startup mạng (network / 네트워크) anti-pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Startup ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. First frame vs first useful content

Đẩy mọi công việc (work / 작업) sau first frame để chỉ số (metric / 지표) đẹp có thể tạo skeleton nhấp nháy và content arrive quá muộn.

Optimize user-perceived journey:

```text
fast stable shell
→ critical local content
→ async remote refresh
```

Không metric-game bằng blank frame.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **31. Startup ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **30. First frame vs first useful content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Startup regression quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Startup ngân sách (budget / 예산)

Nhóm (team / 팀) có thể đặt ngân sách (budget / 예산) theo representative thiết bị (device / 장치) tier, ví dụ TTID/TTFD percentile. Con số cụ thể tùy sản phẩm (product / 제품); quan trọng là có ngân sách (budget / 예산) và regression gate.

Bản dựng (build / 빌드)/CI benchmark nên detect trend chứ không thất bại (fail / 실패) vì noise một run. hiệu năng (performance / 성능) kiểm thử (test / 테스트) cần statistical tolerance.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, sau nội dung của **31. Startup ngân sách (budget / 예산)**, **32. Startup regression quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **33. trường hợp (case / 사례) study mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Startup regression quyền sở hữu (ownership / 소유권)

Nếu every tính năng (feature / 기능) có thể thêm initializer tự do, startup sẽ chậm dần theo thời gian.

Chính sách (policy / 정책) tốt:

- new eager initializer cần justification;
- đơn vị sở hữu (owner / 오너) + measured chi phí (cost / 비용);
- dấu vết (trace / 추적) before/after;
- prefer feature-local lazy init;
- rà soát (review / 검토) merged manifest providers;
- startup benchmark in bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **32. Startup regression quyền sở hữu (ownership / 소유권)** cho ta quy tắc; **33. trường hợp (case / 사례) study mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **34. cấp cao (senior / 시니어) startup checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. trường hợp (case / 사례) study mô hình tư duy (mental model / 사고 모델)

Giả sử app cold start cần theme, auth trạng thái (state / 상태), analytics và feed.

Bad luồng (flow / 흐름):

```text
Application
→ init every SDK
→ open/migrate DB
→ fetch remote config
→ validate token network
→ load feed network
→ Activity
```

Better luồng (flow / 흐름):

```text
process
→ minimal crash/config bootstrap
→ Activity + splash/system theme
→ read tiny local startup state
→ render authenticated shell or login
→ async feed from local source of truth
→ remote refresh
→ lazy/noncritical SDK init after first frame
```

Không phải mọi app giống nhau, nhưng đường găng (critical path / 임계 경로) thinking áp dụng rộng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, **33. trường hợp (case / 사례) study mô hình tư duy (mental model / 사고 모델)** cho ta quy tắc; **34. cấp cao (senior / 시니어) startup checklist** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **35. Official references** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. cấp cao (senior / 시니어) startup checklist

Trước bản phát hành (release / 릴리스), hỏi:

- cold/warm/hot startup measured chưa;
- main luồng thực thi (thread / 스레드) có disk/mạng (network / 네트워크)/blocking khóa (lock / 잠금) không;
- merged manifest có provider auto-init mới không;
- `Application` constructor/onCreate làm gì;
- DI singleton nào eager/heavy;
- DB di chuyển (migration / 마이그레이션) worst-case duration;
- bản phát hành (release / 릴리스) Baseline Profile valid không;
- notification/deep-link cold start kiểm thử (test / 테스트) chưa;
- low-end thiết bị (device / 장치) percentile thế nào;
- startup crash/ANR metrics segment theo phiên bản (version / 버전)/thiết bị (device / 장치) chưa.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 19 — App Startup, Initialization, Cold Start và Startup hiệu năng (performance / 성능)**, sau nội dung của **34. cấp cao (senior / 시니어) startup checklist**, **35. Official references** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 35. Official references
Phần này nối mạch Android vừa học với “35. Official references”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

- App startup thời gian (time / 시간): https://nhà phát triển (developer / 개발자).android.com/topic/hiệu năng (performance / 성능)/vitals/launch-time
- Baseline Profiles: https://nhà phát triển (developer / 개발자).android.com/topic/hiệu năng (performance / 성능)/baselineprofiles/overview
- Macrobenchmark: https://nhà phát triển (developer / 개발자).android.com/topic/hiệu năng (performance / 성능)/benchmarking/macrobenchmark-overview
- App Startup thư viện (library / 라이브러리): https://nhà phát triển (developer / 개발자).android.com/topic/libraries/app-startup
- Perfetto/hệ thống (system / 시스템) tracing: https://nhà phát triển (developer / 개발자).android.com/topic/hiệu năng (performance / 성능)/tracing

Performance guidance evolve cùng runtime/toolchain. Benchmark trên release-like artifact và representative devices luôn quan trọng hơn con số trong tutorial.

> **Bàn giao:** Sau **35. Official references**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

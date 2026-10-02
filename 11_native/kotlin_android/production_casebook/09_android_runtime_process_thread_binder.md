# Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)

> **Mạch đọc:** [README](./README.md) là owner của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**; đặt case sau Android architecture và trước startup/performance cases. Từ **1. Một Android app không phải là một tiến trình (process / 프로세스) sống vĩnh viễn** nối qua Linux process, main thread/Looper, Binder IPC, ART/memory và process death, rồi dùng các cơ chế này để giải thích ANR, state restoration và singleton lifetime.

Ở các chapter trước, ta nhìn Android từ phía ứng dụng (application / 애플리케이션) kiến trúc (architecture / 아키텍처): UI, ViewModel, repository, cơ sở dữ liệu (database / 데이터베이스), mạng (network / 네트워크) và bản phát hành (release / 릴리스). Nhưng đến một mức độ nhất định, nhiều bug không thể giải thích chỉ bằng kiến trúc tầng cao. Vì sao một callback chạy trên main luồng thực thi (thread / 스레드)? Vì sao một app có thể ANR dù không crash? Vì sao truyền một đối tượng (object / 객체) lớn qua `Bundle` đôi khi làm app chết ở nơi rất khó đoán? Vì sao tiến trình (process / 프로세스) có thể biến mất nhưng tác vụ (task / 작업)/back ngăn xếp (stack / 스택) vẫn được hệ thống phục hồi? Vì sao một `suspend` hàm (function / 함수) không đồng nghĩa với background luồng thực thi (thread / 스레드)? Vì sao một singleton không phải “sống suốt đời app”? Những câu hỏi này nằm ở tầng **Android thời gian chạy (runtime / 런타임)**.

Chapter này xây mô hình tư duy (mental model / 사고 모델) từ dưới lên: Linux tiến trình (process / 프로세스) → Android tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) → main luồng thực thi (thread / 스레드) → `Looper` / `MessageQueue` / `Handler` → Binder IPC → ART/thời gian chạy (runtime / 런타임)/bộ nhớ (memory / 메모리) → tiến trình (process / 프로세스) death. Mục tiêu không phải biến Android nhà phát triển (developer / 개발자) thành OS engineer, mà giúp bạn gỡ lỗi (debug / 디버그) đúng khi lớp trừu tượng (abstraction / 추상화) phía trên bị rò rỉ.

## 1. Một Android app không phải là một tiến trình (process / 프로세스) sống vĩnh viễn

Khi người dùng cài app, Android không tạo một tiến trình (process / 프로세스) thường trực cho app. tiến trình (process / 프로세스) chỉ được tạo khi hệ thống cần chạy một thành phần (component / 컴포넌트) của app, chẳng hạn khi người dùng (user / 사용자) mở Activity, một BroadcastReceiver được kích hoạt, một dịch vụ (service / 서비스) cần chạy hoặc ContentProvider được truy cập. Sau đó, Android có thể giữ tiến trình (process / 프로세스) trong bộ nhớ (memory / 메모리) để tái sử dụng, nhưng không có lời hứa rằng tiến trình (process / 프로세스) sẽ tồn tại cho tới khi người dùng (user / 사용자) “đóng app”.

Điều này dẫn tới một nguyên tắc rất quan trọng: **tiến trình (process / 프로세스) thời gian tồn tại (lifetime / 수명) không phải ứng dụng (application / 애플리케이션) thời gian tồn tại (lifetime / 수명) theo góc nhìn nghiệp vụ (business / 비즈니스)**. người dùng (user / 사용자) có thể nghĩ rằng họ “đang ở màn hình chi tiết sản phẩm”, nhưng tiến trình (process / 프로세스) chứa ViewModel, singleton và đối tượng (object / 객체) vùng nhớ động (heap / 힙) của bạn có thể đã bị kill khi app ở background. Khi người dùng (user / 사용자) quay lại, Android có thể tạo tiến trình (process / 프로세스) mới rồi reconstruct Activity/tác vụ (task / 작업) trạng thái (state / 상태) dựa trên thông tin hệ thống lưu được.

Vì vậy một singleton Kotlin như:

```kotlin
object SessionCache {
    var accessToken: String? = null
}
```

chỉ singleton **trong một tiến trình (process / 프로세스) cụ thể**. Nó không phải persistence. Nếu tiến trình (process / 프로세스) chết, đối tượng (object / 객체) chết. Nếu app dùng nhiều tiến trình (process / 프로세스), mỗi tiến trình (process / 프로세스) thậm chí có singleton riêng.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **1. Một Android app không phải là một tiến trình (process / 프로세스) sống vĩnh viễn** xác định đầu vào; **2. Linux tiến trình (process / 프로세스) và Android sandbox** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. Application không phải nơi đảm bảo dữ liệu sống lâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Linux tiến trình (process / 프로세스) và Android sandbox

Mỗi Android app thông thường chạy dưới một Linux UID riêng. UID này là nền tảng của ứng dụng (application / 애플리케이션) sandbox: tệp (file / 파일) private của app, tiến trình (process / 프로세스) permission và nhiều ranh giới bảo mật (security boundary / 보안 경계) được kernel thực thi dựa trên định danh (identity / 식별자) này. Android khung phần mềm (framework / 프레임워크) bổ sung thêm permission mô hình (model / 모델), SELinux chính sách (policy / 정책), Binder định danh (identity / 식별자) và package-level chính sách (policy / 정책) bên trên.

Một tiến trình (process / 프로세스) app thường chứa Android thời gian chạy (runtime / 런타임) (ART), vùng nhớ động (heap / 힙) managed cho Kotlin/Java đối tượng (object / 객체), bản địa (native / 네이티브) vùng nhớ động (heap / 힙) cho C/C++ hoặc bản địa (native / 네이티브) allocation, luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택), mapped libraries, graphics tài nguyên (resource / 자원) và các vùng bộ nhớ (memory / 메모리) khác. Khi nói “app dùng 300 MB RAM”, đừng tự động nghĩ toàn bộ là Kotlin đối tượng (object / 객체) trong vùng nhớ động (heap / 힙). Bitmap, graphics buffer, bản địa (native / 네이티브) codec, cơ sở dữ liệu (database / 데이터베이스) page bộ nhớ đệm (cache / 캐시) và memory-mapped tệp (file / 파일) có thể chiếm phần đáng kể.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, cơ chế trong **2. Linux tiến trình (process / 프로세스) và Android sandbox** cần được kiểm chứng bằng dấu vết cụ thể; **3. Application không phải nơi đảm bảo dữ liệu sống lâu** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **4. Main luồng thực thi (thread / 스레드) là vòng lặp sự kiện (event loop / 이벤트 루프), không phải “luồng thực thi (thread / 스레드) dành riêng cho UI mã (code / 코드)” theo nghĩa đơn giản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. `Application` không phải nơi đảm bảo dữ liệu sống lâu

`Application.onCreate()` chạy khi tiến trình (process / 프로세스) được tạo, trước phần lớn thành phần (component / 컴포넌트) app. Vì thế nó phù hợp để thiết lập phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), logging hạ tầng (infrastructure / 인프라) hoặc thư viện (library / 라이브러리) cần process-wide initialization. Nhưng `Application` đối tượng (object / 객체) chỉ tồn tại cùng tiến trình (process / 프로세스).

Một anti-pattern phổ biến là dùng `Application` như cơ sở dữ liệu (database / 데이터베이스) tạm:

```kotlin
class MyApp : Application() {
    var selectedOrder: Order? = null
}
```

Nếu tiến trình (process / 프로세스) chết rồi screen được restore, `selectedOrder` trở lại `null`. Nếu dữ liệu cần khôi phục, hãy lưu identifier nhỏ trong saved trạng thái (state / 상태) và reconstruct từ Room/backend, hoặc persist dữ liệu thực sự vào lưu trữ (storage / 저장소) phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **3. Application không phải nơi đảm bảo dữ liệu sống lâu** nêu điều cần giải thích; **4. Main luồng thực thi (thread / 스레드) là vòng lặp sự kiện (event loop / 이벤트 루프), không phải “luồng thực thi (thread / 스레드) dành riêng cho UI mã (code / 코드)” theo nghĩa đơn giản** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Looper, MessageQueue, Handler** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Main luồng thực thi (thread / 스레드) là vòng lặp sự kiện (event loop / 이벤트 루프), không phải “luồng thực thi (thread / 스레드) dành riêng cho UI mã (code / 코드)” theo nghĩa đơn giản

Khi Android tạo tiến trình (process / 프로세스) ứng dụng (application / 애플리케이션) thông thường, khung phần mềm (framework / 프레임워크) thiết lập một main luồng thực thi (thread / 스레드). luồng thực thi (thread / 스레드) này chạy vòng lặp sự kiện (event loop / 이벤트 루프) xử lý đầu vào (input / 입력), vòng đời (lifecycle / 생명주기) callback, message khung phần mềm (framework / 프레임워크), rendering coordination và phần lớn callback UI.

Mô hình tư duy (mental model / 사고 모델) quan trọng là:

```text
Message / Runnable / framework event
              ↓
         MessageQueue
              ↓
            Looper
              ↓
         main thread
              ↓
    xử lý callback từng lượt
```

Main luồng thực thi (thread / 스레드) không “chạy UI liên tục”. Nó nhận công việc từ hàng đợi (queue / 큐) rồi xử lý tuần tự. Nếu một callback chiếm luồng thực thi (thread / 스레드) quá lâu, các đầu vào (input / 입력)/kết xuất (render / 렌더링)/vòng đời (lifecycle / 생명주기) message phía sau không được xử lý đúng thời điểm. Đây là nền tảng của jank và ANR.

> **Chuyển mạch:** Main thread vận hành event loop; `Looper`/`MessageQueue`/`Handler` tổ chức dispatch, còn coroutine chạy trên scheduler chứ không thay thế event loop.

## 5. `Looper`, `MessageQueue`, `Handler`

`Looper` là lớp trừu tượng (abstraction / 추상화) chạy vòng lặp lấy message từ `MessageQueue` và dispatch chúng. Main luồng thực thi (thread / 스레드) có main `Looper`. `Handler` là API truyền thống để post `Runnable` hoặc message vào hàng đợi (queue / 큐) gắn với một Looper.

Ví dụ:

```kotlin
val mainHandler = Handler(Looper.getMainLooper())

mainHandler.post {
    // chạy trên main thread ở một lượt event loop tương lai
}
```

Mã (code / 코드) hiện đại thường không dùng `Handler` trực tiếp cho ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성) vì coroutine cung cấp lớp trừu tượng (abstraction / 추상화) tốt hơn, nhưng hiểu Handler/Looper vẫn quan trọng vì nhiều Android API, View hệ thống (system / 시스템) và thư viện (library / 라이브러리) cũ dựa trên cơ chế này.

Android 17 thay đổi hiện thực (implementation / 구현) của `MessageQueue` cho app mục tiêu (target / 대상) API 37+, theo hướng lock-free. ứng dụng (application / 애플리케이션) bình thường không nên phụ thuộc private trường dữ liệu (field / 필드) của `MessageQueue`; thay đổi này là ví dụ điển hình cho lý do không reflection vào hiện thực (implementation / 구현) detail của khung phần mềm (framework / 프레임워크).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **6. Coroutine không thay thế vòng lặp sự kiện (event loop / 이벤트 루프); nó chạy bên trên scheduler/luồng thực thi (thread / 스레드)** tiếp nhận điểm tựa từ **5. Looper, MessageQueue, Handler** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Main-safety** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Coroutine không thay thế vòng lặp sự kiện (event loop / 이벤트 루프); nó chạy bên trên scheduler/luồng thực thi (thread / 스레드)

Một `suspend` hàm (function / 함수) không tự động chạy background:

```kotlin
suspend fun loadUser() {
    val user = repository.getUser()
}
```

Nếu `repository.getUser()` thực hiện CPU-heavy công việc (work / 작업) trực tiếp và coroutine đang ở `Dispatchers.Main`, CPU công việc (work / 작업) vẫn chiếm main luồng thực thi (thread / 스레드). `suspend` chỉ có nghĩa hàm (function / 함수) có thể **suspend và resume** mà không giữ nguyên ngăn xếp lời gọi (call stack / 호출 스택) kiểu blocking truyền thống.

Khi dùng:

```kotlin
withContext(Dispatchers.IO) {
    blockingDatabaseCall()
}
```

coroutine được chuyển sang dispatcher khác cho khối (block / 블록) đó. Khi dùng API suspend-native như Room suspend DAO hoặc Retrofit coroutine adapter, thư viện (library / 라이브러리) thường đã quản lý luồng thực thi (thread / 스레드) phù hợp theo đặc tả hợp đồng (contract / 계약) của nó; đừng thêm `withContext(IO)` theo thói quen nếu không cần.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙) là hỏi: **thao tác (operation / 연산) này blocking hay non-blocking, CPU-bound hay IO-bound, và Đặc tả API (API contract / API 계약) nói gì về thực thi (execution / 실행) ngữ cảnh (context / 맥락)?** chứ không phải “mọi suspend đều background”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **7. Main-safety** tiếp nhận điểm tựa từ **6. Coroutine không thay thế vòng lặp sự kiện (event loop / 이벤트 루프); nó chạy bên trên scheduler/luồng thực thi (thread / 스레드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Frame ngân sách (budget / 예산) và jank** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Main-safety

Một hàm (function / 함수) được gọi từ main luồng thực thi (thread / 스레드) nên “main-safe”: nó không làm blocking IO hoặc CPU công việc (work / 작업) đủ lớn để gây lag. Một thiết kế (design / 설계) tốt thường để tầng (layer / 계층) sở hữu thao tác (operation / 연산) tự đảm bảo main-safety.

Ví dụ:

```kotlin
class ImageHasher(
    private val defaultDispatcher: CoroutineDispatcher
) {
    suspend fun hash(bytes: ByteArray): String =
        withContext(defaultDispatcher) {
            expensiveHash(bytes)
        }
}
```

Caller không cần biết hiện thực (implementation / 구현) dùng CPU nhiều. Điều này giảm việc dispatcher lô-gic (logic / 논리) bị rải khắp UI/ViewModel.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **8. Frame ngân sách (budget / 예산) và jank** tiếp nhận điểm tựa từ **7. Main-safety** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. ANR khác crash** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Frame ngân sách (budget / 예산) và jank

UI 60 Hz có khoảng 16.67 ms cho mỗi frame; màn hình refresh cao hơn có ngân sách (budget / 예산) nhỏ hơn. Không phải toàn bộ ngân sách (budget / 예산) thuộc ứng dụng (application / 애플리케이션) mã (code / 코드), vì rendering chuỗi xử lý (pipeline / 파이프라인) còn có measure/bố cục (layout / 레이아웃)/draw, GPU công việc (work / 작업) và hệ thống (system / 시스템) overhead.

Nếu main luồng thực thi (thread / 스레드) bị khối (block / 블록) 50 ms, người dùng (user / 사용자) có thể thấy dropped frames. Nếu bị khối (block / 블록) lâu hơn nhiều trong những ngữ cảnh (context / 맥락) nhất định, hệ thống có thể coi app không phản hồi và tạo ANR.

Hiệu năng (performance / 성능) công việc (work / 작업) vì vậy bắt đầu bằng đo dấu vết (trace / 추적)/frame/jank, không bằng nhìn mã (code / 코드) rồi đoán rằng một hàm (function / 함수) “có vẻ chậm”.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **9. ANR khác crash** tiếp nhận điểm tựa từ **8. Frame ngân sách (budget / 예산) và jank** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. StrictMode như development guardrail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. ANR khác crash

Crash xảy ra khi tiến trình (process / 프로세스) gặp exception/fatal tín hiệu (signal / 신호) không được xử lý và kết thúc. ANR xảy ra khi app vẫn tồn tại nhưng không đáp ứng đúng thời hạn mà khung phần mềm (framework / 프레임워크) yêu cầu cho một thao tác (operation / 연산) quan trọng, phổ biến nhất là main luồng thực thi (thread / 스레드) không xử lý sự kiện (event / 이벤트) đủ nhanh.

Nguồn ANR thường gồm blocking IO trên main, tranh chấp khóa (lock contention / 잠금 경합)/deadlock, synchronous Binder lời gọi (call / 호출) quá lâu, BroadcastReceiver làm việc quá nhiều, startup quá nặng hoặc luồng thực thi (thread / 스레드) pool starvation gián tiếp làm main chờ.

Một bug có thể không xuất hiện trong cục bộ (local / 로컬) testing vì mạng (network / 네트워크)/dev machine nhanh, nhưng xuất hiện môi trường vận hành (production / 운영 환경) trên thiết bị (device / 장치) chậm. Vì vậy StrictMode, tracing và representative hardware quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **10. StrictMode như development guardrail** tiếp nhận điểm tựa từ **9. ANR khác crash** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Tại sao Android cần IPC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `StrictMode` như development guardrail

`StrictMode` có thể phát hiện một số hành vi không mong muốn như disk/truy cập mạng (network access / 네트워크 접근) trên main luồng thực thi (thread / 스레드) trong development. Nó không thay profiling, nhưng rất hữu ích để biến “hiệu năng (performance / 성능) smell” thành tín hiệu sớm.

Ví dụ conceptual:

```kotlin
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder()
            .detectAll()
            .penaltyLog()
            .build()
    )
}
```

Không nên bật penalty phá app một cách mù quáng trong môi trường vận hành (production / 운영 환경). Mục tiêu là dùng StrictMode để phát hiện ranh giới (boundary / 경계) violation trong dev/kiểm thử (test / 테스트).

# Binder — xương sống IPC của Android

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **11. Tại sao Android cần IPC** tiếp nhận điểm tựa từ **10. StrictMode như development guardrail** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. IPC không miễn phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Tại sao Android cần IPC

Nhiều thứ ứng dụng (application / 애플리케이션) gọi thực tế sống ở tiến trình (process / 프로세스) khác: ActivityManager, PackageManager dịch vụ (service / 서비스), hệ thống (system / 시스템) dịch vụ (service / 서비스), media dịch vụ (service / 서비스) và các thành phần (component / 컴포넌트) hệ thống khác. Android dùng **Binder** làm cơ chế IPC chủ đạo để tiến trình (process / 프로세스) gọi qua ranh giới (boundary / 경계) an toàn hơn so với chia sẻ bộ nhớ (memory / 메모리) tùy ý.

Khi bạn gọi một phương thức (method / 메서드) trông như cục bộ (local / 로컬) Java/Kotlin lời gọi (call / 호출), đối tượng (object / 객체) phía sau có thể là Binder proxy gửi giao dịch (transaction / 트랜잭션) sang tiến trình (process / 프로세스) khác.

Mô hình tư duy (mental model / 사고 모델):

```text
App process
  proxy
    │ Binder transaction
    ▼
Kernel Binder driver
    │
    ▼
System/server process
  Binder stub
```

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **12. IPC không miễn phí** tiếp nhận điểm tựa từ **11. Tại sao Android cần IPC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Bundle, Intent và giao dịch (transaction / 트랜잭션) kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. IPC không miễn phí

Binder lời gọi (call / 호출) có serialization/marshalling, ngữ cảnh (context / 맥락) switching, scheduling và giới hạn giao dịch (transaction / 트랜잭션). Vì vậy tránh thiết kế chatty IPC ở đường xử lý nóng (hot path / 핫 패스).

Ví dụ, gọi hệ thống (system / 시스템) dịch vụ (service / 서비스) hàng nghìn lần trong vòng lặp (loop / 루프) có thể tốn hơn việc batch/caching hợp lý. Nhưng cũng không nên bộ nhớ đệm (cache / 캐시) dữ liệu hệ thống vô hạn nếu đặc tả hợp đồng (contract / 계약) yêu cầu freshness.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **13. Bundle, Intent và giao dịch (transaction / 트랜잭션) kích thước (size / 크기)** tiếp nhận điểm tựa từ **12. IPC không miễn phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Parcelable không phải persistence format** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. `Bundle`, `Intent` và giao dịch (transaction / 트랜잭션) kích thước (size / 크기)

`Bundle`, Intent extras và saved trạng thái (state / 상태) thường đi qua Binder hoặc hạ tầng (infrastructure / 인프라) có giới hạn kích thước. Truyền đối tượng (object / 객체) đồ thị (graph / 그래프) lớn là lỗi thiết kế.

Đừng làm:

```kotlin
intent.putExtra("whole_result_list", hugeParcelableList)
```

Nên truyền ID nhỏ:

```kotlin
intent.putExtra("order_id", orderId)
```

rồi reconstruct dữ liệu (data / 데이터) từ repository/nguồn chuẩn (source of truth / 정본) ở destination.

Điều này không chỉ tránh `TransactionTooLargeException`, mà còn làm trạng thái (state / 상태) restoration ổn định hơn.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **13. Bundle, Intent và giao dịch (transaction / 트랜잭션) kích thước (size / 크기)** cho ta quy tắc; **14. Parcelable không phải persistence format** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **15. Binder luồng thực thi (thread / 스레드) pool và callback threading** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Parcelable không phải persistence format

`Parcelable` tối ưu cho IPC/in-process Android ranh giới (boundary / 경계), không phải lược đồ (schema / 스키마) lưu trữ dài hạn. Không lưu raw Parcel vào cơ sở dữ liệu (database / 데이터베이스)/tệp (file / 파일) rồi kỳ vọng phiên bản (version / 버전) sau đọc ổn định.

Cho persistence, dùng lược đồ (schema / 스키마) rõ ràng: Room, Proto/DataStore, JSON/CBOR/protobuf tùy use trường hợp (case / 사례).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **14. Parcelable không phải persistence format** cho ta quy tắc; **15. Binder luồng thực thi (thread / 스레드) pool và callback threading** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. Binder định danh (identity / 식별자) và ranh giới bảo mật (security boundary / 보안 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Binder luồng thực thi (thread / 스레드) pool và callback threading

Không phải Binder callback nào cũng chạy main luồng thực thi (thread / 스레드). Một Binder dịch vụ (service / 서비스) có luồng thực thi (thread / 스레드) pool xử lý incoming giao dịch (transaction / 트랜잭션). Nếu bạn tự viết dịch vụ (service / 서비스)/AIDL hoặc tương tác low-level IPC, phải đọc đặc tả hợp đồng (contract / 계약) threading rõ ràng.

Nếu callback từ background/Binder luồng thực thi (thread / 스레드) cần mutate UI trạng thái (state / 상태), chuyển sang lifecycle-aware/main-safe đường dẫn (path / 경로) phù hợp. Ngược lại, đừng ép mọi callback sang main nếu processing nặng không cần UI.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **15. Binder luồng thực thi (thread / 스레드) pool và callback threading** đã nêu tiêu chí phân biệt, còn **16. Binder định danh (identity / 식별자) và ranh giới bảo mật (security boundary / 보안 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Kotlin không chạy trực tiếp như mã nguồn (source code / 소스 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Binder định danh (identity / 식별자) và ranh giới bảo mật (security boundary / 보안 경계)

Khi hệ thống (system / 시스템)/dịch vụ (service / 서비스) xử lý Binder lời gọi (call / 호출), caller định danh (identity / 식별자) có ý nghĩa bảo mật (security / 보안). Custom exported thành phần (component / 컴포넌트)/dịch vụ (service / 서비스) phải validate caller/permission nếu nhận dữ liệu nhạy cảm. Không nên nghĩ rằng “đây là app nội bộ nên Intent/Binder đầu vào (input / 입력) chắc chắn hợp lệ”.

Mọi bên ngoài (external / 외부) đầu vào (input / 입력) nên được xem là untrusted ranh giới (boundary / 경계).

# ART, bytecode và thời gian chạy (runtime / 런타임)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **16. Binder định danh (identity / 식별자) và ranh giới bảo mật (security boundary / 보안 경계)** đã nêu tiêu chí phân biệt, còn **17. Kotlin không chạy trực tiếp như mã nguồn (source code / 소스 코드)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **18. AOT, JIT và profile-guided tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Kotlin không chạy trực tiếp như mã nguồn (source code / 소스 코드)

Kotlin/JVM nguồn (source / 소스) được compile thành JVM bytecode/lớp (class / 클래스) biểu diễn (representation / 표현), Android bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) tiếp tục chuyển đổi thành DEX để ART thực thi. D8 xử lý dexing/desugaring; R8 có thể shrink, optimize và obfuscate.

Chuỗi xử lý (pipeline / 파이프라인) giản lược:

```text
Kotlin source
→ Kotlin compiler / K2 frontend + backend
→ JVM bytecode
→ D8 / R8
→ DEX
→ ART
```

Điều này giải thích vì sao Java interoperability, generic erasure, synthetic phương thức (method / 메서드), cầu nối (bridge / 브리지) phương thức (method / 메서드), boxing và reflection đều có thể ảnh hưởng Android app dù mã (code / 코드) viết bằng Kotlin.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **17. Kotlin không chạy trực tiếp như mã nguồn (source code / 소스 코드)** nêu điều cần giải thích; **18. AOT, JIT và profile-guided tối ưu hóa (optimization / 최적화)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. nạp lớp (class loading / 클래스 로딩) và startup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. AOT, JIT và profile-guided tối ưu hóa (optimization / 최적화)

ART có thể dùng nhiều cơ chế compile/thời gian chạy (runtime / 런타임) tối ưu hóa (optimization / 최적화) tùy Android phiên bản (version / 버전) và trạng thái app. nhà phát triển (developer / 개발자) không nên cố “điều khiển JIT” như JVM máy chủ (server / 서버) app. Thứ có thể kiểm soát tốt hơn ở app tầng (layer / 계층) là startup đường dẫn (path / 경로), mã (code / 코드) kích thước (size / 크기), nạp lớp (class loading / 클래스 로딩), Baseline Profile và đường xử lý nóng (hot path / 핫 패스) thiết kế (design / 설계).

Baseline Profile giúp thời gian chạy (runtime / 런타임) biết những đường đi mã (code path / 코드 경로) quan trọng nên được tối ưu sớm, giảm cold-start/jank cho đường dẫn (path / 경로) điển hình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **19. nạp lớp (class loading / 클래스 로딩) và startup** tiếp nhận điểm tựa từ **18. AOT, JIT và profile-guided tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Managed vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. nạp lớp (class loading / 클래스 로딩) và startup

Nếu app có quá nhiều initialization eager ở `Application.onCreate()`, cold startup tăng. Mỗi SDK analytics, DI đồ thị (graph / 그래프) lớn, reflection scan, cơ sở dữ liệu (database / 데이터베이스) open hoặc synchronous disk read đều có thể cộng dồn.

Cấp cao (senior / 시니어) approach là phân loại initialization:

| Nhóm | Cách nghĩ |
|---|---|
| bắt buộc trước first frame | giữ tối thiểu |
| cần sớm nhưng không trước first frame | defer |
| chỉ cần khi tính năng (feature / 기능) dùng | lazy/on-demand |
| background durable | cân nhắc WorkManager |

Không tối ưu startup bằng cách chuyển tất cả sang luồng thực thi (thread / 스레드) nền mà không xét phụ thuộc (dependency / 의존성); race điều kiện (condition / 조건) có thể thay hiệu năng (performance / 성능) bug bằng tính đúng đắn (correctness / 정확성) bug.

# Bộ nhớ (memory / 메모리)

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **20. Managed vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **19. nạp lớp (class loading / 클래스 로딩) và startup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Garbage Collection không phải leak detector** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Managed vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ (memory / 메모리)

Kotlin/Java đối tượng (object / 객체) sống trong managed vùng nhớ động (heap / 힙) do GC quản lý, nhưng app còn dùng bản địa (native / 네이티브) bộ nhớ (memory / 메모리), graphics buffer, bitmap, SQLite/bản địa (native / 네이티브) thư viện (library / 라이브러리) bộ nhớ (memory / 메모리) và mapped tệp (file / 파일).

Một profiler chỉ nhìn Java vùng nhớ động (heap / 힙) có thể không thấy toàn bộ vấn đề.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **21. Garbage Collection không phải leak detector** tiếp nhận điểm tựa từ **20. Managed vùng nhớ động (heap / 힙) không phải toàn bộ bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Context leak** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Garbage Collection không phải leak detector

GC thu đối tượng (object / 객체) không còn reachable. Nếu đối tượng (object / 객체) vẫn reachable vì tham chiếu (reference / 참조) chuỗi (chain / 사슬) không mong muốn, GC không thể giải phóng nó.

Ví dụ leak Android kinh điển:

```text
process singleton
→ listener
→ Activity
→ View tree
→ large bitmap/resources
```

Nếu singleton giữ listener của Activity sau destroy, toàn đồ thị (graph / 그래프) còn reachable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **22. Context leak** tiếp nhận điểm tựa từ **21. Garbage Collection không phải leak detector** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Listener và coroutine leak** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. `Context` leak

`Activity` ngữ cảnh (context / 맥락) giữ nhiều trạng thái (state / 상태) gắn với cửa sổ (window / 윈도우)/UI. Không giữ Activity trong singleton/static đối tượng (object / 객체) lâu hơn vòng đời (lifecycle / 생명주기).

Nếu phụ thuộc (dependency / 의존성) chỉ cần process-level ngữ cảnh (context / 맥락), inject `ApplicationContext`. Nhưng cũng không biến `ApplicationContext` thành giải pháp mặc định cho mọi thứ; một số API cần themed/activity ngữ cảnh (context / 맥락).

Câu hỏi đúng là **phụ thuộc (dependency / 의존성) cần thời gian tồn tại (lifetime / 수명)/ngữ cảnh (context / 맥락) năng lực (capability / 역량) nào?**

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **23. Listener và coroutine leak** tiếp nhận điểm tựa từ **22. Context leak** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Bitmap và ảnh (image / 이미지) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Listener và coroutine leak

Coroutine có structured tính đồng thời (concurrency / 동시성) tốt hơn luồng thực thi (thread / 스레드)/callback tự do, nhưng vẫn leak công việc (work / 작업) nếu phạm vi (scope / 범위) quyền sở hữu (ownership / 소유권) sai.

Ví dụ `GlobalScope.launch` trong ViewModel khiến công việc (work / 작업) không bị cancel cùng ViewModel. Tương tự, callback/listener đăng ký mà không unregister sẽ giữ đơn vị sở hữu (owner / 오너) sống.

Quyền sở hữu (ownership / 소유권) map nên rõ:

```text
Composable effect → Composition
ViewModel coroutine → viewModelScope
Lifecycle collection → lifecycleScope / repeatOnLifecycle
durable background work → WorkManager
process-level work → application-owned scope nếu thật sự cần
```

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **24. Bitmap và ảnh (image / 이미지) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **23. Listener và coroutine leak** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Low-memory và tiến trình (process / 프로세스) reclaim** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Bitmap và ảnh (image / 이미지) bộ nhớ (memory / 메모리)

Ảnh (image / 이미지) decoding có thể dùng bộ nhớ (memory / 메모리) lớn. Không tải (load / 로드) ảnh full-resolution chỉ để hiển thị thumbnail. Dùng ảnh (image / 이미지) loading thư viện (library / 라이브러리) có decode/downsample/bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) đúng. Với app widget/RemoteViews, Android 17 mục tiêu (target / 대상) 37+ còn áp giới hạn bộ nhớ (memory limit / 메모리 제한) rõ hơn cho combined Bitmap/Icon trong parcel, cho thấy nền tảng (platform / 플랫폼) ngày càng siết tài nguyên (resource / 자원) misuse.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **24. Bitmap và ảnh (image / 이미지) bộ nhớ (memory / 메모리)** xác định đầu vào; **25. Low-memory và tiến trình (process / 프로세스) reclaim** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **26. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Low-memory và tiến trình (process / 프로세스) reclaim

Android có thể reclaim background tiến trình (process / 프로세스) để giải phóng bộ nhớ (memory / 메모리). nhà phát triển (developer / 개발자) không được dựa vào callback kiểu “sẽ luôn được báo trước khi tiến trình (process / 프로세스) bị kill”. Hãy thiết kế như tiến trình (process / 프로세스) có thể mất mà không có cơ hội cleanup nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

Nếu dữ liệu quan trọng chỉ tồn tại trong RAM, đó là data-loss bug chờ xảy ra.

# Tiến trình (process / 프로세스) death và trạng thái (state / 상태) restoration

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **25. Low-memory và tiến trình (process / 프로세스) reclaim** xác định đầu vào; **26. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **27. trạng thái (state / 상태) classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death

Rotation/cửa sổ (window / 윈도우) resize có thể recreate Activity nhưng tiến trình (process / 프로세스) vẫn sống. ViewModel thường survive cấu hình (configuration / 구성) thay đổi (change / 변경).

Tiến trình (process / 프로세스) death thì ViewModel, singleton và vùng nhớ động (heap / 힙) biến mất. Android có thể restore điều hướng (navigation / 내비게이션)/tác vụ (task / 작업)/activity trạng thái (state / 상태) đủ để đưa người dùng (user / 사용자) về màn hình gần trước đó, nhưng ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) không được phục hồi tự động.

Bởi vậy kiểm thử (test / 테스트) rotation thôi chưa đủ; cần kiểm thử (test / 테스트) **Don't keep activities** chỉ giúp một phần và không hoàn toàn tương đương tiến trình (process / 프로세스) kill thật. Với luồng (flow / 흐름) quan trọng, cần kiểm thử (test / 테스트) restore từ saved trạng thái (state / 상태) + persistent nguồn chuẩn (source of truth / 정본).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **26. cấu hình (configuration / 구성) thay đổi (change / 변경) khác tiến trình (process / 프로세스) death** xác định đầu vào; **27. trạng thái (state / 상태) classification** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **28. “Chỉ dùng coroutine” không tự động thread-safe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. trạng thái (state / 상태) classification

Một cách phân loại thực dụng:

| trạng thái (state / 상태) | Ví dụ | đơn vị sở hữu (owner / 오너)/persistence |
|---|---|---|
| ephemeral UI | pressed trạng thái (state / 상태), animation progress | `remember` |
| restorable UI | tab/page nhỏ | `rememberSaveable` |
| screen nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) | loading/filter/kết quả (result / 결과) | ViewModel |
| restore key | truy vấn (query / 쿼리)/orderId/draftId | `SavedStateHandle` |
| durable cục bộ (local / 로컬) dữ liệu (data / 데이터) | thực thể (entity / 엔터티), pending sync | Room/DataStore |
| authoritative remote | account/thứ tự (order / 순서) máy chủ (server / 서버) trạng thái (state / 상태) | backend |

Không cố lưu mọi thứ vào `SavedStateHandle`; saved trạng thái (state / 상태) phải nhỏ và reconstructive.

# Luồng thực thi (thread / 스레드) an toàn (safety / 안전)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **28. “Chỉ dùng coroutine” không tự động thread-safe** tiếp nhận điểm tựa từ **27. trạng thái (state / 상태) classification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Confinement thường đơn giản hơn khóa (lock / 잠금)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. “Chỉ dùng coroutine” không tự động thread-safe

Nếu nhiều coroutine cùng mutate trạng thái dùng chung (shared state / 공유 상태) trên dispatcher đa luồng thực thi (thread / 스레드), race điều kiện (condition / 조건) vẫn tồn tại.

Ví dụ:

```kotlin
var counter = 0

coroutineScope {
    repeat(1000) {
        launch(Dispatchers.Default) {
            counter++
        }
    }
}
```

`counter++` không atomic. Giải pháp có thể là confinement, immutable trạng thái (state / 상태) reducer, `Mutex`, atomic thành phần nguyên thủy (primitive / 기본 요소) hoặc cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) tùy loại trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **29. Confinement thường đơn giản hơn khóa (lock / 잠금)** tiếp nhận điểm tựa từ **28. “Chỉ dùng coroutine” không tự động thread-safe** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Deadlock và khóa (lock / 잠금) inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Confinement thường đơn giản hơn khóa (lock / 잠금)

UI trạng thái (state / 상태) thường tốt khi mutation được serialize trong một đơn vị sở hữu (owner / 오너). Thay vì nhiều tầng (layer / 계층) cùng mutate `MutableStateFlow`, expose immutable trạng thái (state / 상태) và funnel sự kiện (event / 이벤트) qua một mutation đường dẫn (path / 경로).

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState
```

Không đưa `_uiState` ra ngoài.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **30. Deadlock và khóa (lock / 잠금) inversion** tiếp nhận điểm tựa từ **29. Confinement thường đơn giản hơn khóa (lock / 잠금)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Khi nào dùng công cụ (tool / 도구) nào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Deadlock và khóa (lock / 잠금) inversion

Nếu nhiều khóa (lock / 잠금) được acquire theo thứ tự khác nhau, deadlock có thể xảy ra. Trong Android, synchronous Binder lời gọi (call / 호출) trong khi giữ app khóa (lock / 잠금) còn có thể tạo phụ thuộc (dependency / 의존성) khó thấy giữa tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드).

Cấp cao (senior / 시니어) guideline: giữ trọng yếu (critical / 중요) section nhỏ, tránh blocking IO/Binder lời gọi (call / 호출) khi đang giữ khóa (lock / 잠금) nếu không thật sự cần, và ưu tiên kiến trúc (architecture / 아키텍처) giảm dùng chung (shared / 공유) mutable trạng thái (state / 상태).

# Debugging thời gian chạy (runtime / 런타임)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **31. Khi nào dùng công cụ (tool / 도구) nào** tiếp nhận điểm tựa từ **30. Deadlock và khóa (lock / 잠금) inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Ví dụ suy luận một ANR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Khi nào dùng công cụ (tool / 도구) nào

Logcat tốt cho chuỗi (sequence / 시퀀스)/sự kiện (event / 이벤트). Android Studio Profiler tốt cho CPU/bộ nhớ (memory / 메모리)/mạng (network / 네트워크) overview. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적) tốt cho luồng thực thi (thread / 스레드) scheduling, frame, Binder, khóa (lock / 잠금) và end-to-end timing. vùng nhớ động (heap / 힙) dump tốt cho retained đối tượng (object / 객체). Macrobenchmark đo startup/frame tương tác (interaction / 상호작용) ở gần môi trường vận hành (production / 운영 환경). StrictMode bắt một số chính sách (policy / 정책) violation dev-time.

Không chọn công cụ (tool / 도구) theo thói quen; chọn theo hypothesis.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **31. Khi nào dùng công cụ (tool / 도구) nào** cho ta quy tắc; **32. Ví dụ suy luận một ANR** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **33. Ví dụ suy luận bộ nhớ (memory / 메모리) leak** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Ví dụ suy luận một ANR

Giả sử ngăn xếp (stack / 스택) main luồng thực thi (thread / 스레드) cho thấy:

```text
Main thread
→ onResume
→ repository.refreshBlocking()
→ OkHttp execute()
```

Không cần tối ưu Compose trước. nguyên nhân gốc (root cause / 근본 원인) là synchronous mạng (network / 네트워크) trên vòng đời (lifecycle / 생명주기) callback/main luồng thực thi (thread / 스레드).

Nếu dấu vết (trace / 추적) lại cho thấy main luồng thực thi (thread / 스레드) đang chờ `CountDownLatch`, trong khi worker cần callback trên main để count down, đây có thể là deadlock/liveness bug chứ không phải mạng (network / 네트워크) chậm.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **32. Ví dụ suy luận một ANR** cho ta quy tắc; **33. Ví dụ suy luận bộ nhớ (memory / 메모리) leak** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **34. thời gian chạy (runtime / 런타임) kiến thức (knowledge / 지식) dùng để phá vỡ ảo tưởng lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Ví dụ suy luận bộ nhớ (memory / 메모리) leak

Nếu vùng nhớ động (heap / 힙) dump cho thấy destroyed Activity retained bởi `SomeManager.listener`, sửa manager/listener thời gian tồn tại (lifetime / 수명). Không “gọi hệ thống (system / 시스템).gc()” để chữa leak. GC không thể thu đối tượng (object / 객체) vẫn reachable.

# Cấp cao (senior / 시니어) Notes

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **33. Ví dụ suy luận bộ nhớ (memory / 메모리) leak** cho ta quy tắc; **34. thời gian chạy (runtime / 런타임) kiến thức (knowledge / 지식) dùng để phá vỡ ảo tưởng lớp trừu tượng (abstraction / 추상화)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **35. tiến trình (process / 프로세스) death là thiết kế (design / 설계) đầu vào (input / 입력), không phải trường hợp biên (edge case / 경계 사례) kỳ lạ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. thời gian chạy (runtime / 런타임) kiến thức (knowledge / 지식) dùng để phá vỡ ảo tưởng lớp trừu tượng (abstraction / 추상화)

Ở mã (code / 코드) bình thường, hãy làm việc ở lớp trừu tượng (abstraction / 추상화) cao: coroutine, luồng (flow / 흐름), Compose, Room, điều hướng (navigation / 내비게이션). Chỉ hạ xuống Handler/Binder/ART khi bằng chứng (evidence / 증거) chỉ tới đó. cấp cao (senior / 시니어) không phải người luôn viết low-level mã (code / 코드); cấp cao (senior / 시니어) là người biết lớp trừu tượng (abstraction / 추상화) nào đang giữ và khi nào nó đã rò rỉ.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **34. thời gian chạy (runtime / 런타임) kiến thức (knowledge / 지식) dùng để phá vỡ ảo tưởng lớp trừu tượng (abstraction / 추상화)** cho ta quy tắc; **35. tiến trình (process / 프로세스) death là thiết kế (design / 설계) đầu vào (input / 입력), không phải trường hợp biên (edge case / 경계 사례) kỳ lạ** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **36. luồng thực thi (thread / 스레드) là tài nguyên (resource / 자원), không phải đơn vị (unit / 단위) lô-gic nghiệp vụ (business logic / 비즈니스 로직)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. tiến trình (process / 프로세스) death là thiết kế (design / 설계) đầu vào (input / 입력), không phải trường hợp biên (edge case / 경계 사례) kỳ lạ

Nếu app mobile chạy đủ lâu ngoài môi trường vận hành (production / 운영 환경), tiến trình (process / 프로세스) death sẽ xảy ra. Vì vậy persistence/trạng thái (state / 상태) restoration nên là một phần kiến trúc (architecture / 아키텍처), không phải patch sau bug report.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, cơ chế trong **35. tiến trình (process / 프로세스) death là thiết kế (design / 설계) đầu vào (input / 입력), không phải trường hợp biên (edge case / 경계 사례) kỳ lạ** cần được kiểm chứng bằng dấu vết cụ thể; **36. luồng thực thi (thread / 스레드) là tài nguyên (resource / 자원), không phải đơn vị (unit / 단위) lô-gic nghiệp vụ (business logic / 비즈니스 로직)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **37. IPC ranh giới (boundary / 경계) là serialization + trust ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. luồng thực thi (thread / 스레드) là tài nguyên (resource / 자원), không phải đơn vị (unit / 단위) lô-gic nghiệp vụ (business logic / 비즈니스 로직)

Nghiệp vụ (business / 비즈니스) mã (code / 코드) nên nói “tải (load / 로드) profile”, “sync pending mutation”, “kết xuất (render / 렌더링) trạng thái (state / 상태)”, không nói “spawn luồng thực thi (thread / 스레드) 4”. luồng thực thi (thread / 스레드)/dispatcher là thực thi (execution / 실행) cơ chế (mechanism / 메커니즘). Tách hai thứ giúp mã (code / 코드) testable và portable hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **36. luồng thực thi (thread / 스레드) là tài nguyên (resource / 자원), không phải đơn vị (unit / 단위) lô-gic nghiệp vụ (business logic / 비즈니스 로직)** đã nêu tiêu chí phân biệt, còn **37. IPC ranh giới (boundary / 경계) là serialization + trust ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **38. bộ nhớ (memory / 메모리) tối ưu hóa (optimization / 최적화) phải dựa trên retained đồ thị (graph / 그래프) và allocation mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. IPC ranh giới (boundary / 경계) là serialization + trust ranh giới (boundary / 경계)

Qua Binder/Intent/URI, hãy nghĩ cùng lúc ba vấn đề: payload có nhỏ không, phiên bản (version / 버전)/serialization có đúng không, đầu vào (input / 입력) có đáng tin không.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 09 — Android thời gian chạy (runtime / 런타임): tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), Looper, Binder, ART và bộ nhớ (memory / 메모리)**, **37. IPC ranh giới (boundary / 경계) là serialization + trust ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **38. bộ nhớ (memory / 메모리) tối ưu hóa (optimization / 최적화) phải dựa trên retained đồ thị (graph / 그래프) và allocation mẫu (pattern / 패턴)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 38. bộ nhớ (memory / 메모리) tối ưu hóa (optimization / 최적화) phải dựa trên retained đồ thị (graph / 그래프) và allocation mẫu (pattern / 패턴)

Đừng thấy bộ nhớ (memory / 메모리) cao rồi xóa bộ nhớ đệm (cache / 캐시) ngẫu nhiên. Hãy phân biệt bộ nhớ đệm (cache / 캐시) hợp lệ, retained leak, bitmap/bản địa (native / 네이티브) allocation và working set cần thiết.

# Checklist kết thúc chapter

Sau chapter này, bạn nên tự giải thích được vì sao `suspend` không đồng nghĩa background; vì sao main luồng thực thi (thread / 스레드) thực chất là vòng lặp sự kiện (event loop / 이벤트 루프); vì sao `Handler` vẫn xuất hiện trong mã (code / 코드) Android; vì sao Intent/Bundle không nên mang đối tượng (object / 객체) đồ thị (graph / 그래프) lớn; Binder là gì và vì sao IPC không miễn phí; tiến trình (process / 프로세스) death khác cấu hình (configuration / 구성) thay đổi (change / 변경) thế nào; singleton/ứng dụng (application / 애플리케이션) không phải persistence; managed vùng nhớ động (heap / 힙) khác total tiến trình (process / 프로세스) bộ nhớ (memory / 메모리) thế nào; và khi gặp ANR/leak nên dùng dấu vết (trace / 추적)/vùng nhớ động (heap / 힙) bằng chứng (evidence / 증거) thay vì đoán.

> **Bàn giao:** Sau **38. bộ nhớ (memory / 메모리) tối ưu hóa (optimization / 최적화) phải dựa trên retained đồ thị (graph / 그래프) và allocation mẫu (pattern / 패턴)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

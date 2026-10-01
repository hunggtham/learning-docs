# Kotlin + Android — Coverage kiểm tra (audit / 감사)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Kotlin language foundations** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Coroutine và Flow** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

## 1. Kotlin language foundations
Phần này nối mạch Android vừa học với “1. Kotlin language foundations”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| cú pháp (syntax / 문법), `val`/`var`, kiểu (type / 타입) suy luận (inference / 추론) | Nền tảng đầy đủ | Beginner |
| null-safety, smart cast, cast | Nền tảng đầy đủ | Beginner |
| hàm (function / 함수)/default/named/vararg | Đầy đủ | Beginner |
| lớp (class / 클래스)/thuộc tính (property / 속성)/inheritance/giao diện (interface / 인터페이스) | Đầy đủ | Beginner |
| dữ liệu (data / 데이터)/enum/sealed | Đầy đủ theo mức (level / 수준) | Beginner + Intermediate |
| gói (package / 패키지)/import/top-level declaration | Deep dive | Deep Dive 01 |
| equality/phạm vi (range / 범위)/array/collection transformations | Đầy đủ | Beginner + Deep Dive 01 |
| lambda/HOF/phạm vi (scope / 범위) functions | Đầy đủ | Beginner + Intermediate |
| generics/variance/projection/erasure | Đầy đủ | Intermediate + Advanced + trường hợp (case / 사례) 08 |
| delegation/delegated thuộc tính (property / 속성) | Đầy đủ | Intermediate |
| inline/reified/contracts/reflection | Advanced | Advanced + trường hợp (case / 사례) 08 |
| giá trị (value / 값) lớp (class / 클래스)/boxing/JVM biểu diễn (representation / 표현) | Master | Master + trường hợp (case / 사례) 08 |
| suspend máy trạng thái (state machine / 상태 머신)/lambda capture | Under the hood | trường hợp (case / 사례) 08 |
| Java interop/ABI/trình biên dịch (compiler / 컴파일러) plugin | Master | Advanced + trường hợp (case / 사례) 08 + trường hợp (case / 사례) 20 + độ sâu (depth / 깊이) Lab 07 |

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **1. Kotlin language foundations** xác định đầu vào; **2. Coroutine và Flow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. Android runtime và component model** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Coroutine và Flow
Phần này nối mạch Android vừa học với “2. Coroutine và Flow”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| `suspend`, `launch`, `async`, `withContext` | Đầy đủ | Intermediate |
| structured tính đồng thời (concurrency / 동시성)/supervision | Đầy đủ + lập luận (reasoning / 추론) sâu | Intermediate + Deep Dive 02 + độ sâu (depth / 깊이) Lab 03 |
| cancellation/exception propagation | Đầy đủ + thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) | Intermediate + Advanced + độ sâu (depth / 깊이) Lab 03 |
| `CoroutineContext`/Job hierarchy | Deep dive | Deep Dive 02 + độ sâu (depth / 깊이) Lab 03 |
| luồng (flow / 흐름) cold/hot | Đầy đủ + thời gian tồn tại (lifetime / 수명) ngữ nghĩa (semantics / 의미론) | Intermediate + Deep Dive 02 + độ sâu (depth / 깊이) Lab 03 |
| StateFlow/SharedFlow | Đầy đủ | Intermediate + độ sâu (depth / 깊이) Lab 03 |
| `stateIn`/`shareIn`/SharingStarted | Đầy đủ | Deep Dive 02 + độ sâu (depth / 깊이) Lab 03 |
| `flowOn`/ngữ cảnh (context / 맥락) preservation | Đầy đủ | Deep Dive 02 + độ sâu (depth / 깊이) Lab 03 |
| `callbackFlow` | Đầy đủ | Deep Dive 02 + trường hợp (case / 사례) 06 + độ sâu (depth / 깊이) Lab 03 |
| buffer/conflate/collectLatest/backpressure | cấp cao (senior / 시니어) sâu | Deep Dive 03 + độ sâu (depth / 깊이) Lab 03 |
| Channel/Mutex/atomic/trạng thái dùng chung (shared state / 공유 상태) | cấp cao (senior / 시니어) sâu | Advanced + độ sâu (depth / 깊이) Lab 03 |
| dispatcher injection/kiểm thử (test / 테스트) scheduler | cấp cao (senior / 시니어) | Advanced + Deep Dive 02 + độ sâu (depth / 깊이) Lab 03 |
| main-safety/luồng thực thi (thread / 스레드) confinement | môi trường vận hành (production / 운영 환경) | trường hợp (case / 사례) 09 + độ sâu (depth / 깊이) Lab 03 |
| stale-result/concurrent-session race | môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) | độ sâu (depth / 깊이) Lab 03 |
| bản địa (native / 네이티브) callback/luồng thực thi (thread / 스레드) crossing | môi trường vận hành (production / 운영 환경)/bản địa (native / 네이티브) | trường hợp (case / 사례) 17 + độ sâu (depth / 깊이) Lab 07 |

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **2. Coroutine và Flow** xác định đầu vào; **3. Android runtime và component model** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Jetpack Compose UI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Android runtime và component model
Phần này nối mạch Android vừa học với “3. Android runtime và component model”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| Activity/dịch vụ (service / 서비스)/Receiver/Provider | Nền tảng → môi trường vận hành (production / 운영 환경) | Beginner + trường hợp (case / 사례) 14 |
| ngữ cảnh (context / 맥락)/ứng dụng (application / 애플리케이션)/Activity thời gian tồn tại (lifetime / 수명) | Đầy đủ | Deep Dive 01 + trường hợp (case / 사례) 09 |
| Intent/Bundle/Uri | Đầy đủ | Beginner + Deep Dive 01 + trường hợp (case / 사례) 14 |
| vòng đời (lifecycle / 생명주기)/cấu hình (configuration / 구성) thay đổi (change / 변경) | Đầy đủ | Beginner → Advanced + trường hợp (case / 사례) 04 |
| tiến trình (process / 프로세스) death/SavedStateHandle | Đầy đủ + reconstruction lập luận (reasoning / 추론) | Intermediate + Advanced + trường hợp (case / 사례) 04/09 + độ sâu (depth / 깊이) Lab 01/05 |
| Linux tiến trình (process / 프로세스)/app sandbox | nền tảng (platform / 플랫폼) | trường hợp (case / 사례) 09 |
| Looper/MessageQueue/Handler | nền tảng (platform / 플랫폼) | trường hợp (case / 사례) 09 |
| Binder/IPC/Parcelable giao dịch (transaction / 트랜잭션) | nền tảng (platform / 플랫폼) | trường hợp (case / 사례) 09 |
| ART/DEX/nạp lớp (class loading / 클래스 로딩)/thời gian chạy (runtime / 런타임) bộ nhớ (memory / 메모리) | nền tảng (platform / 플랫폼) | trường hợp (case / 사례) 08/09 |
| dịch vụ (service / 서비스)/Receiver/Provider cold entry | môi trường vận hành (production / 운영 환경) | trường hợp (case / 사례) 14 |
| notification/widget/shortcut/tile | môi trường vận hành (production / 운영 환경) | trường hợp (case / 사례) 14 |
| startup initialization đường găng (critical path / 임계 경로) | môi trường vận hành (production / 운영 환경) sâu | trường hợp (case / 사례) 19 + độ sâu (depth / 깊이) Lab 06 |

> **Chuyển mạch:** Android runtime/component model đặt constraint cho UI; coverage kiểm tra Compose trước, rồi đối chiếu XML/View để không bỏ sót legacy interoperability.

## 4. Jetpack Compose UI
Phần này nối mạch Android vừa học với “4. Jetpack Compose UI”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| composable/bố cục (layout / 레이아웃)/modifier | Đầy đủ | Beginner + Deep Dive 01 |
| trạng thái (state / 상태)/recomposition/hoisting | Đầy đủ + lập luận (reasoning / 추론) sâu | Beginner → Advanced + Deep Dive 02 + độ sâu (depth / 깊이) Lab 04 |
| remember/rememberSaveable | Đầy đủ | Beginner + Intermediate + độ sâu (depth / 깊이) Lab 04 |
| tác động (effect / 효과) APIs | Đầy đủ + thời gian tồn tại (lifetime / 수명) ngữ nghĩa (semantics / 의미론) | Intermediate + Deep Dive 02 + trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| lazy định danh (identity / 식별자)/key | Đầy đủ sâu | Deep Dive 02/03 + trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| Snapshot trạng thái (state / 상태)/CompositionLocal | cấp cao (senior / 시니어) sâu | Advanced + Deep Dive 03 + độ sâu (depth / 깊이) Lab 04 |
| composition/bố cục (layout / 레이아웃)/draw phases | Đầy đủ sâu | Deep Dive 03 + trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| ràng buộc (constraint / 제약조건)/custom bố cục (layout / 레이아웃)/draw | môi trường vận hành (production / 운영 환경) UI | trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| gestures/nested scroll/đầu vào (input / 입력) | môi trường vận hành (production / 운영 환경) UI | trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| focus/IME/hardware keyboard | môi trường vận hành (production / 운영 환경) UI | trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| animation trạng thái (state / 상태) mô hình (model / 모델) | môi trường vận hành (production / 운영 환경) UI | trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| ngữ nghĩa (semantics / 의미론)/khả năng tiếp cận (accessibility / 접근성) | Đầy đủ sâu | Master + Deep Dive 04 + trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04/05 |
| edge-to-edge/insets | Đầy đủ | trường hợp (case / 사례) 11 + độ sâu (depth / 깊이) Lab 04 |
| adaptive/foldable/cửa sổ (window / 윈도우) sizes | Đầy đủ | Master + trường hợp (case / 사례) 11 |
| first composition/startup chi phí (cost / 비용) | môi trường vận hành (production / 운영 환경) hiệu năng (performance / 성능) | trường hợp (case / 사례) 19 + độ sâu (depth / 깊이) Lab 06 |
| phase-specific vô hiệu hóa (invalidation / 무효화)/hiệu năng (performance / 성능) | cấp cao (senior / 시니어)/Master lập luận (reasoning / 추론) | độ sâu (depth / 깊이) Lab 04 |

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **5. XML/View và legacy interoperability** tiếp nhận điểm tựa từ **4. Jetpack Compose UI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Architecture và state management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. XML/View và legacy interoperability

XML bố cục (layout / 레이아웃), View Binding, Fragment/View vòng đời (lifecycle / 생명주기), RecyclerView, dữ liệu (data / 데이터) Binding awareness và Compose/View interoperability được giữ từ Beginner/Intermediate. trường hợp (case / 사례) 06 mở rộng incremental di chuyển (migration / 마이그레이션) Java/XML/Fragment/LiveData/Rx → Kotlin/coroutine/luồng (flow / 흐름)/Compose. trường hợp (case / 사례) 11 cover `AndroidView`/`ComposeView` như interoperability ranh giới (boundary / 경계). Legacy API được phân loại thành deprecated/historical/still-valid thay vì gắn nhãn “sai” một cách máy móc.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **6. Architecture và state management** tiếp nhận điểm tựa từ **5. XML/View và legacy interoperability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Persistence và lưu trữ (storage / 저장소)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Architecture và state management
Phần này nối mạch Android vừa học với “6. Architecture và state management”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| ViewModel/UiState/UDF | Đầy đủ | Intermediate + trường hợp (case / 사례) 01 |
| repository/dữ liệu (data / 데이터) nguồn (source / 소스) | Đầy đủ + ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계) | Intermediate + trường hợp (case / 사례) 01 + độ sâu (depth / 깊이) Lab 01 |
| nguồn chuẩn (source of truth / 정본) | Đầy đủ + quyền sở hữu (ownership / 소유권) lập luận (reasoning / 추론) | Intermediate + Deep Dive 02 + trường hợp (case / 사례) 01/03 + độ sâu (depth / 깊이) Lab 01/02 |
| lĩnh vực (domain / 도메인)/use-case tầng (layer / 계층) quyết định (decision / 결정) | Đầy đủ | Intermediate + trường hợp (case / 사례) 01 + độ sâu (depth / 깊이) Lab 01 |
| offline-first/sync/xung đột (conflict / 충돌) | môi trường vận hành (production / 운영 환경) sâu | Advanced/Master + trường hợp (case / 사례) 03 + độ sâu (depth / 깊이) Lab 02 |
| giao dịch (transaction / 트랜잭션) bất biến (invariant / 불변식)/outbox/idempotency | môi trường vận hành (production / 운영 환경) sâu | trường hợp (case / 사례) 03 + độ sâu (depth / 깊이) Lab 01/02 |
| stale snapshot/ambiguous kết quả (outcome / 결과) | Master lập luận (reasoning / 추론) | độ sâu (depth / 깊이) Lab 01/02 |
| multi-module kiến trúc (architecture / 아키텍처) | cấp cao (senior / 시니어)/Master | Advanced/Master + trường hợp (case / 사례) 06/07 |
| phụ thuộc (dependency / 의존성) direction/API surface | Master | Master + Deep Dive 04 + trường hợp (case / 사례) 07/20 + độ sâu (depth / 깊이) Lab 07 |
| ADR/quyền sở hữu (ownership / 소유권)/quản trị (governance / 거버넌스) | Master | Deep Dive 04 + trường hợp (case / 사례) 07 + độ sâu (depth / 깊이) Lab 01 |
| legacy strangler di chuyển (migration / 마이그레이션) | Đầy đủ | trường hợp (case / 사례) 06 |
| trạng thái (state / 상태) reconstruction after cold/hệ thống (system / 시스템) entry | môi trường vận hành (production / 운영 환경) | trường hợp (case / 사례) 04/14/19 + độ sâu (depth / 깊이) Lab 01/05 |

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **7. Persistence và lưu trữ (storage / 저장소)** tiếp nhận điểm tựa từ **6. Architecture và state management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Networking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Persistence và lưu trữ (storage / 저장소)

Room, DAO, quan hệ (relation / 관계), kiểu (type / 타입) converter, giao dịch (transaction / 트랜잭션), di chuyển (migration / 마이그레이션)/lược đồ (schema / 스키마) evolution, DataStore, tệp (file / 파일)/MediaStore/scoped lưu trữ (storage / 저장소), nguồn chuẩn (source of truth / 정본) và backup concern đã được cover từ Intermediate → cấp cao (senior / 시니어). trường hợp (case / 사례) 03 đi sâu durable mutation hàng đợi (queue / 큐), tombstone, xung đột (conflict / 충돌), pagination, di chuyển (migration / 마이그레이션) và quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성). trường hợp (case / 사례) 12 bổ sung SAF/Photo Picker/MediaStore/content URI. trường hợp (case / 사례) 13 bổ sung backup/restore/upgrade-path kiểm thử (test / 테스트). độ sâu (depth / 깊이) Lab 01–02 đào sâu giao dịch (transaction / 트랜잭션) bất biến (invariant / 불변식), cursor atomicity, outbox durability, tombstone ngữ nghĩa (semantics / 의미론) và thất bại (failure / 실패) after partial lần ghi nhận (commit / 커밋).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **8. Networking** tiếp nhận điểm tựa từ **7. Persistence và lưu trữ (storage / 저장소)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Authentication, authorization và session** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Networking

Retrofit/serialization nằm ở Intermediate; hết thời gian chờ (timeout / 타임아웃)/lỗi (error / 오류)/cancellation ở Deep Dive 02; thử lại (retry / 재시도)/idempotency/bộ nhớ đệm (cache / 캐시)/TLS/WebSocket/SSE ở Deep Dive 03; auth/session/đơn vị từ (token / 토큰) refresh ở trường hợp (case / 사례) 02; offline sync ở trường hợp (case / 사례) 03; slow/unreliable connectivity ở trường hợp (case / 사례) 12/13. độ sâu (depth / 깊이) Lab 02 đi sâu ambiguous kết quả (outcome / 결과), idempotency key, jitter, thử lại (retry / 재시도) classification, stale phản hồi (response / 응답)/phiên bản (version / 버전) guard và concurrent writer. lỗi (error / 오류) được tách vận chuyển (transport / 전송) → giao thức (protocol / 프로토콜) → lĩnh vực (domain / 도메인); UI không phụ thuộc vận chuyển (transport / 전송) detail.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **9. Authentication, authorization và session** tiếp nhận điểm tựa từ **8. Networking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. phụ thuộc (dependency / 의존성) Injection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Authentication, authorization và session

Trường hợp (case / 사례) 02 cover Credential Manager, account/session trạng thái (state / 상태), truy cập (access / 접근)/refresh đơn vị từ (token / 토큰), concurrent `401`, single-flight refresh, logout và secure lưu trữ (storage / 저장소). trường hợp (case / 사례) 10 nhấn mạnh OS permission không phải nghiệp vụ (business / 비즈니스) entitlement. độ sâu (depth / 깊이) Lab 02–03 bổ sung account isolation, session epoch, in-flight phản hồi (response / 응답) từ account cũ và single-flight tính đồng thời (concurrency / 동시성). bảo mật (security / 보안) mô hình (model / 모델) không xem máy khách (client / 클라이언트)/thiết bị (device / 장치) là trusted authority.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **10. phụ thuộc (dependency / 의존성) Injection** tiếp nhận điểm tựa từ **9. Authentication, authorization và session** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Background thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. phụ thuộc (dependency / 의존성) Injection

Constructor injection, Hilt/DI concept, phạm vi (scope / 범위)/thời gian tồn tại (lifetime / 수명) và large-scale DI đã được cover. DI không được coi là kiến trúc (architecture / 아키텍처); nó quản lý phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)/thời gian tồn tại (lifetime / 수명). trường hợp (case / 사례) 14/19 nhấn mạnh hệ thống (system / 시스템) entry điểm (point / 지점) và startup initialization không được phụ thuộc MainActivity chạy trước. trường hợp (case / 사례) 20/độ sâu (depth / 깊이) Lab 07 cover phụ thuộc (dependency / 의존성) exposure từ góc SDK author.

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **11. Background thực thi (execution / 실행)** tiếp nhận điểm tựa từ **10. phụ thuộc (dependency / 의존성) Injection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Background thực thi (execution / 실행)

WorkManager, foreground dịch vụ (service / 서비스)/công việc (work / 작업), notification, exact-alarm awareness, coroutine thời gian tồn tại (lifetime / 수명) và background restriction đã được cover. Deep Dive 03 có quyết định (decision / 결정) khung phần mềm (framework / 프레임워크); trường hợp (case / 사례) 10 nối foreground thực thi (execution / 실행) với permission/hệ thống (system / 시스템) chính sách (policy / 정책); trường hợp (case / 사례) 14 phân biệt dịch vụ (service / 서비스)/Receiver/WorkManager theo thời gian tồn tại (lifetime / 수명)/durability; trường hợp (case / 사례) 18 đặt chúng vào target-SDK di chuyển (migration / 마이그레이션). độ sâu (depth / 깊이) Lab 02 nhấn mạnh WorkManager là scheduler chứ không phải sync tính đúng đắn (correctness / 정확성) engine.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **12. Testing** tiếp nhận điểm tựa từ **11. Background thực thi (execution / 실행)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Testing
Phần này nối mạch Android vừa học với “12. Testing”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Tầng | Coverage |
|---|---|
| pure Kotlin JVM đơn vị (unit / 단위) kiểm thử (test / 테스트) | Beginner + Intermediate |
| fake/mock/kiểm thử (test / 테스트) double | Deep Dive 02 + độ sâu (depth / 깊이) Lab 05 |
| coroutine virtual-time/luồng (flow / 흐름) kiểm thử (test / 테스트) | Intermediate + Deep Dive 02 + độ sâu (depth / 깊이) Lab 03/05 |
| deterministic race thứ tự (ordering / 순서) | cấp cao (senior / 시니어)/Master | độ sâu (depth / 깊이) Lab 03/05 |
| property-based/bất biến (invariant / 불변식) testing | Master | độ sâu (depth / 깊이) Lab 02/05 |
| Robolectric | Deep Dive 03 |
| instrumented Android kiểm thử (test / 테스트) | Beginner + Deep Dive 03 |
| Compose UI/ngữ nghĩa (semantics / 의미론)/khả năng tiếp cận (accessibility / 접근성) | trường hợp (case / 사례) 11/13 + độ sâu (depth / 깊이) Lab 04/05 |
| Room/mạng (network / 네트워크) tích hợp (integration / 통합)/đặc tả hợp đồng (contract / 계약) | Advanced + trường hợp (case / 사례) 05 + độ sâu (depth / 깊이) Lab 05 |
| hardware/thiết bị (device / 장치) tích hợp (integration / 통합) | trường hợp (case / 사례) 12 + độ sâu (depth / 깊이) Lab 05 |
| di chuyển (migration / 마이그레이션)/upgrade/quay lui (rollback / 롤백) đường dẫn (path / 경로) | trường hợp (case / 사례) 03/13/18 + độ sâu (depth / 깊이) Lab 05 |
| process-death/cold-entry reconstruction | trường hợp (case / 사례) 04/14/19 + độ sâu (depth / 깊이) Lab 01/05 |
| Macrobenchmark/Baseline Profile | trường hợp (case / 사례) 05/19 + độ sâu (depth / 깊이) Lab 05/06 |
| OS/OEM/thiết bị (device / 장치) ma trận (matrix / 행렬) | trường hợp (case / 사례) 13/18 + độ sâu (depth / 깊이) Lab 05/06 |
| bản phát hành (release / 릴리스) bundle/split install | trường hợp (case / 사례) 16 + độ sâu (depth / 깊이) Lab 06 |
| bản địa (native / 네이티브) ABI/page kích thước (size / 크기)/symbol kiểm tra hợp lệ (validation / 검증) | trường hợp (case / 사례) 17 + độ sâu (depth / 깊이) Lab 07 |
| minified SDK bên tiêu thụ (consumer / 소비자)/API tính tương thích (compatibility / 호환성) | trường hợp (case / 사례) 20 + độ sâu (depth / 깊이) Lab 07 |

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **13. hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **12. Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. bảo mật (security / 보안) và privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. hiệu năng (performance / 성능)

Main-thread/ANR/leak, Compose recomposition, R8, startup, Baseline Profile, Macrobenchmark, Perfetto, bộ nhớ (memory / 메모리)/battery/mạng (network / 네트워크) và hiệu năng (performance / 성능) ngân sách (budget / 예산) đã được cover. trường hợp (case / 사례) 09 đi sâu vòng lặp sự kiện (event loop / 이벤트 루프)/Binder/ART/GC/luồng thực thi (thread / 스레드) contention; trường hợp (case / 사례) 11 cover hot UI paths; trường hợp (case / 사례) 13 cover low-memory/thermal/thiết bị (device / 장치) chất lượng (quality / 품질); trường hợp (case / 사례) 17 cover bản địa (native / 네이티브) bộ nhớ (memory / 메모리)/JNI overhead; trường hợp (case / 사례) 19 tập trung cold/warm/hot start và startup đường găng (critical path / 임계 경로). độ sâu (depth / 깊이) Lab 04 nhấn mạnh phase-specific vô hiệu hóa (invalidation / 무효화) và evidence-based Compose tối ưu hóa (optimization / 최적화); độ sâu (depth / 깊이) Lab 05–06 nối benchmark với SLO, release-like bản dựng (build / 빌드) và startup đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **14. bảo mật (security / 보안) và privacy** tiếp nhận điểm tựa từ **13. hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. bản dựng (build / 빌드), Gradle và AGP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. bảo mật (security / 보안) và privacy

Coverage gồm secure cấu hình (config / 설정), Credential Manager, WebView ranh giới (boundary / 경계), Android Keystore, TLS/mạng (network / 네트워크) bảo mật (security / 보안) cấu hình (config / 설정), backend authorization, integrity awareness, backup chính sách (policy / 정책), dữ liệu (data / 데이터) an toàn (safety / 안전)/privacy inventory, PendingIntent/exported components, supply-chain phụ thuộc (dependency / 의존성) rủi ro (risk / 위험) và bản địa (native / 네이티브) parser/memory-safety awareness. Obfuscation không được xem là secret lưu trữ (storage / 저장소); integrity chỉ là rủi ro (risk / 위험) tín hiệu (signal / 신호); bên ngoài (external / 외부) Intent/URI/Binder/bản địa (native / 네이티브) đầu vào (input / 입력) đều được coi là untrusted. độ sâu (depth / 깊이) Lab 07 bổ sung privacy/logging obligations của SDK consumer-facing.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **15. bản dựng (build / 빌드), Gradle và AGP** tiếp nhận điểm tựa từ **14. bảo mật (security / 보안) và privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. AAB, packaging và phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. bản dựng (build / 빌드), Gradle và AGP

Trường hợp (case / 사례) 15 nâng phần bản dựng (build / 빌드) từ awareness lên môi trường vận hành (production / 운영 환경) mô hình tư duy (mental model / 사고 모델): Gradle vs AGP vs Kotlin plugin; gốc (root / 루트)/settings/mô-đun (module / 모듈) mô hình (model / 모델); bản dựng (build / 빌드) kiểu (type / 타입)/sản phẩm (product / 제품) flavor/variant; source-set precedence; manifest/tài nguyên (resource / 자원) merging; phụ thuộc (dependency / 의존성) configurations; phiên bản (version / 버전) catalogs; convention plugins; cấu hình (configuration / 구성)/bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시); Java/Kotlin toolchain; Variant API; D8/R8; signing; reproducibility và CI variant chiến lược (strategy / 전략).

Độ sâu (depth / 깊이) Lab 06 đào sâu bản dựng (build / 빌드) theo phase, phụ thuộc (dependency / 의존성) visibility, generated-code forensic, release-only R8 thất bại (failure / 실패), variant-only issue, merged manifest/tài nguyên (resource / 자원) rà soát (review / 검토), phụ thuộc (dependency / 의존성) khóa (lock / 잠금) và sản phẩm tạo ra (artifact / 산출물) provenance. Các tệp (file / 파일) Beginner/Master/Deep Dive 04 vẫn giữ bản dựng (build / 빌드) fundamentals và quản trị (governance / 거버넌스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **16. AAB, packaging và phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **15. bản dựng (build / 빌드), Gradle và AGP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. bản địa (native / 네이티브)/NDK/JNI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. AAB, packaging và phân phối (distribution / 분포)

Trường hợp (case / 사례) 16 cover APK vs AAB, split APK, `bundletool`, động (dynamic / 동적) tính năng (feature / 기능)/Play tính năng (feature / 기능) Delivery, install-time/on-demand/conditional delivery, asset/kích thước (size / 크기) concern, ABI/ngôn ngữ (language / 언어) splits, Play App Signing, phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터), bản phát hành (release / 릴리스) tracks, staged rollout, mobile quay lui (rollback / 롤백) limitation, distribution-channel ranh giới (boundary / 경계) và sản phẩm tạo ra (artifact / 산출물) provenance.

Độ sâu (depth / 깊이) Lab 06 nhấn mạnh final installed sản phẩm tạo ra (artifact / 산출물) có thể khác upload bundle theo thiết bị (device / 장치) cấu hình (configuration / 구성), và bản phát hành (release / 릴리스) gate phải verify sản phẩm tạo ra (artifact / 산출물)/delivery đường dẫn (path / 경로) chứ không chỉ nguồn (source / 소스). AAB upload kích thước (size / 크기) không được nhầm với download/install kích thước (size / 크기) thực tế. động (dynamic / 동적) tính năng (feature / 기능) chỉ dùng khi delivery benefit bù được install-state độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **17. bản địa (native / 네이티브)/NDK/JNI** tiếp nhận điểm tựa từ **16. AAB, packaging và phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. bản địa (native / 네이티브)/NDK/JNI

Trường hợp (case / 사례) 17 cover `.so`, ABI, JNI static/động (dynamic / 동적) registration, cục bộ (local / 로컬)/toàn cục (global / 전역) references, `JNIEnv` luồng thực thi (thread / 스레드) affinity, callback, array/direct buffer, bản địa (native / 네이티브) bộ nhớ (memory / 메모리), RAII, CMake, prebuilt bản địa (native / 네이티브) libraries, bản địa (native / 네이티브) API levels, tệp (file / 파일) descriptor cầu nối (bridge / 브리지), symbolication, tombstone, sanitizers, JNI batching và bảo mật (security / 보안).

Độ sâu (depth / 깊이) Lab 07 đào sâu bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전) ở JNI ranh giới (boundary / 경계): luồng thực thi (thread / 스레드) quyền sở hữu (ownership / 소유권), pending Java exception, buffer/tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명), coarse-grained ranh giới (boundary / 경계), ABI testing, bản địa (native / 네이티브) symbol provenance và host-process blast radius. 16 KB page-size tính tương thích (compatibility / 호환성) được xem như bản phát hành (release / 릴리스) yêu cầu (requirement / 요구사항) đối với app/SDK có bản địa (native / 네이티브) thư viện (library / 라이브러리), bao gồm prebuilt vendor `.so`.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **18. Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링)** tiếp nhận điểm tựa từ **17. bản địa (native / 네이티브)/NDK/JNI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. App startup và initialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링)

Trường hợp (case / 사례) 18 cover bốn phiên bản (version / 버전) axes (`minSdk`, `compileSdk`, `targetSdk`, device OS), all-app vs target-gated hành vi (behavior / 동작) changes, tính tương thích (compatibility / 호환성) khung phần mềm (framework / 프레임워크), API guards/`@RequiresApi`, Jetpack compat lớp trừu tượng (abstraction / 추상화), desugaring, SDK Extensions, updatable hệ thống (system / 시스템) components, non-SDK restrictions, WebView versioning, target-API chính sách (policy / 정책) và OS/mục tiêu (target / 대상) di chuyển (migration / 마이그레이션) playbook.

Độ sâu (depth / 깊이) Lab 06 bổ sung forensic theo phase, compile di chuyển (migration / 마이그레이션) vs hành vi (behavior / 동작) di chuyển (migration / 마이그레이션), OEM/WebView dimension, phụ thuộc (dependency / 의존성)/toolchain isolation và exact-variant reproduction. nền tảng (platform / 플랫폼) upgrade được tách thành current-app-on-new-OS testing và targetSdk di chuyển (migration / 마이그레이션), thay vì tăng mục tiêu (target / 대상) rồi sửa lỗi đồng loạt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **19. App startup và initialization** tiếp nhận điểm tựa từ **18. Android tính tương thích (compatibility / 호환성) kỹ thuật (engineering / 엔지니어링)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Android thư viện (library / 라이브러리)/SDK authoring** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. App startup và initialization

Trường hợp (case / 사례) 19 cover cold/warm/hot start, TTID/TTFD, ứng dụng (application / 애플리케이션)/provider auto-init, AndroidX App Startup, lazy/eager initialization, DI constructor side effects, SplashScreen, startup routing, nạp lớp (class loading / 클래스 로딩)/static init, Compose first frame, Baseline Profile, Macrobenchmark, Perfetto, StrictMode, SDK initialization quản trị (governance / 거버넌스), DB di chuyển (migration / 마이그레이션)/startup, multi-process init và startup budgets.

Độ sâu (depth / 깊이) Lab 06 đi sâu startup như phụ thuộc (dependency / 의존성) đường găng (critical path / 임계 경로), phân loại eager/lazy/demand-driven công việc (work / 작업) và tách TTID khỏi TTFD. Startup được coi là đường găng (critical path / 임계 경로) có ngân sách (budget / 예산), không phải collection các `init()` lời gọi (call / 호출).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **20. Android thư viện (library / 라이브러리)/SDK authoring** tiếp nhận điểm tựa từ **19. App startup và initialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. môi trường vận hành (production / 운영 환경) quản trị (governance / 거버넌스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Android thư viện (library / 라이브러리)/SDK authoring

Trường hợp (case / 사례) 20 cover AAR vs pure JVM thư viện (library / 라이브러리), API công khai (public API / 공개 API) surface, nguồn (source / 소스)/nhị phân (binary / 이진) tính tương thích (compatibility / 호환성), Kotlin/Java interop, phụ thuộc (dependency / 의존성) exposure, tài nguyên (resource / 자원)/manifest đặc tả hợp đồng (contract / 계약), Compose thư viện (library / 라이브러리) API, threading/coroutine/luồng (flow / 흐름) đặc tả hợp đồng (contract / 계약), lỗi (error / 오류) mô hình (model / 모델), bên tiêu thụ (consumer / 소비자) ProGuard rules, minified bên tiêu thụ (consumer / 소비자) kiểm thử (test / 테스트), custom lint, SemVer behavioral tính tương thích (compatibility / 호환성), ABI kiểm tra hợp lệ (validation / 검증), công khai (public / 공개) inline/dữ liệu (data / 데이터)/enum evolution, publishing, mẫu (sample / 표본) apps, hỗ trợ (support / 지원) ma trận (matrix / 행렬), deprecation và privacy/bảo mật (security / 보안) obligations của SDK.

Độ sâu (depth / 깊이) Lab 07 đi sâu nguồn (source / 소스) vs nhị phân (binary / 이진) vs behavioral tính tương thích (compatibility / 호환성), Kotlin/Java ABI ergonomics, phụ thuộc (dependency / 의존성) leakage, auto-init startup debt, callback/luồng thực thi (thread / 스레드)/lỗi (error / 오류) đặc tả hợp đồng (contract / 계약), bên tiêu thụ (consumer / 소비자) R8, API dump, old-consumer tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) và sản phẩm tạo ra (artifact / 산출물) provenance.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **21. môi trường vận hành (production / 운영 환경) quản trị (governance / 거버넌스)** tiếp nhận điểm tựa từ **20. Android thư viện (library / 라이브러리)/SDK authoring** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Kotlin Multiplatform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. môi trường vận hành (production / 운영 환경) quản trị (governance / 거버넌스)

Master + Deep Dive 04 + trường hợp (case / 사례) 05/07/13/15/16 cover khả năng quan sát (observability / 관측 가능성) lược đồ (schema / 스키마), hiệu năng (performance / 성능) ngân sách (budget / 예산), phụ thuộc (dependency / 의존성) quản trị (governance / 거버넌스)/SBOM, ADR, mã (code / 코드) quyền sở hữu (ownership / 소유권), flaky-test chính sách (policy / 정책), feature-flag vòng đời (lifecycle / 생명주기), target-SDK cadence, sản phẩm tạo ra (artifact / 산출물) provenance, sự cố (incident / 인시던트) phản hồi (response / 응답) và quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성). độ sâu (depth / 깊이) Lab 05 bổ sung SLI/SLO, structured telemetry, staged rollout guardrail, flaky-test debt và postmortem vòng phản hồi (feedback loop / 피드백 루프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **22. Kotlin Multiplatform** tiếp nhận điểm tựa từ **21. môi trường vận hành (production / 운영 환경) quản trị (governance / 거버넌스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Offline-first và synchronization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Kotlin Multiplatform

KMP được giữ ở Master thay vì đưa vào Beginner. Coverage tập trung dùng chung (shared / 공유) lô-gic nghiệp vụ (business logic / 비즈니스 로직), API công khai (public API / 공개 API), `expect/actual`, nền tảng (platform / 플랫폼) ranh giới (boundary / 경계), threading/serialization và tiêu chí share đúng concern thay vì tối đa hóa phần trăm dùng chung (shared / 공유) mã (code / 코드).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **23. Offline-first và synchronization** tiếp nhận điểm tựa từ **22. Kotlin Multiplatform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Permission, năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Offline-first và synchronization

Trường hợp (case / 사례) 03 cover optimistic ghi (write / 쓰기), durable hàng đợi (queue / 큐), idempotency key, thử lại (retry / 재시도)/backoff, tombstone, giải quyết xung đột (conflict resolution / 충돌 해결), cursor, Paging/RemoteMediator và lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션). độ sâu (depth / 깊이) Lab 02 tăng độ sâu bằng consistency mô hình (model / 모델), outbox bất biến (invariant / 불변식), idempotency key vòng đời (lifecycle / 생명주기), thử lại (retry / 재시도)+jitter, mutation compaction, phiên bản (version / 버전)/xung đột (conflict / 충돌), pull/push thứ tự (ordering / 순서), checkpoint atomicity, poison mutation, sync debt và account isolation.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **24. Permission, năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **23. Offline-first và synchronization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. thiết bị (device / 장치)/media/hardware tích hợp (integration / 통합)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Permission, năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)

Trường hợp (case / 사례) 10 cover hardware năng lực (capability / 역량) vs permission, `<uses-feature>`, permission revocation, foreground/background location, Bluetooth/Nearby, local-network protection, notification, camera/mic, Photo Picker/SAF, foreground dịch vụ (service / 서비스), chính xác (exact / 정확한) alarm, exported thành phần (component / 컴포넌트), App Links và target-SDK concerns. độ sâu (depth / 깊이) Lab 05 bổ sung permission revoke như failure-injection scenario.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **25. thiết bị (device / 장치)/media/hardware tích hợp (integration / 통합)** tiếp nhận điểm tựa từ **24. Permission, năng lực (capability / 역량) và hệ thống (system / 시스템) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. khả năng tiếp cận (accessibility / 접근성), adaptive UI và advanced Compose** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. thiết bị (device / 장치)/media/hardware tích hợp (integration / 통합)

Trường hợp (case / 사례) 12 cover CameraX, Media3/player/media session/audio focus, microphone, files/media picker, hiện tại (current / 현재)/continuous location, geofence, BLE/GATT, NFC/sensor, connectivity và WebView. Những tích hợp (integration / 통합) này được mô hình (model / 모델) như bên ngoài (external / 외부) stateful các hệ thống (systems / 시스템들) có tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권), hết thời gian chờ (timeout / 타임아웃), vòng đời (lifecycle / 생명주기) và khôi phục (recovery / 복구). độ sâu (depth / 깊이) Lab 05 bổ sung hardware/thiết bị (device / 장치) kiểm thử tích hợp (integration test / 통합 테스트) theo rủi ro (risk / 위험).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **26. khả năng tiếp cận (accessibility / 접근성), adaptive UI và advanced Compose** tiếp nhận điểm tựa từ **25. thiết bị (device / 장치)/media/hardware tích hợp (integration / 통합)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. môi trường vận hành (production / 운영 환경) thiết bị (device / 장치) ma trận (matrix / 행렬) và app chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. khả năng tiếp cận (accessibility / 접근성), adaptive UI và advanced Compose

Trường hợp (case / 사례) 11 cover bố cục (layout / 레이아웃)/draw/đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인), custom bố cục (layout / 레이아웃)/draw, gesture/nested scroll, focus/IME, edge-to-edge, animation, ngữ nghĩa (semantics / 의미론)/khả năng tiếp cận (accessibility / 접근성), font/RTL, keyboard/mouse và adaptive/foldable chiến lược (strategy / 전략). độ sâu (depth / 깊이) Lab 04 tăng độ sâu ở định danh (identity / 식별자), Snapshot phụ thuộc (dependency / 의존성) tracking, tác động (effect / 효과) key, stability, phase-specific trạng thái (state / 상태) read, ngữ nghĩa (semantics / 의미론) cây (tree / 트리) và evidence-based tối ưu hóa (optimization / 최적화). khả năng tiếp cận (accessibility / 접근성) được coi là tính đúng đắn (correctness / 정확성)/công khai (public / 공개) ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약), không phải polish cuối.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **27. môi trường vận hành (production / 운영 환경) thiết bị (device / 장치) ma trận (matrix / 행렬) và app chất lượng (quality / 품질)** tiếp nhận điểm tựa từ **26. khả năng tiếp cận (accessibility / 접근성), adaptive UI và advanced Compose** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. hệ thống (system / 시스템) surfaces ngoài Activity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. môi trường vận hành (production / 운영 환경) thiết bị (device / 장치) ma trận (matrix / 행렬) và app chất lượng (quality / 품질)

Trường hợp (case / 사례) 13 cover risk-based OS/OEM/thiết bị (device / 장치) ma trận (matrix / 행렬), fresh install/upgrade đường dẫn (path / 경로), quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성), localization/plural/timezone/RTL, font scaling/TalkBack, battery/Doze, slow mạng (network / 네트워크)/thử lại (retry / 재시도) storm, low-memory/thermal, privacy inventory, telemetry, tính năng (feature / 기능) flags, backup/restore và sự cố (incident / 인시던트) readiness. độ sâu (depth / 깊이) Lab 05–06 nối thiết bị (device / 장치) ma trận (matrix / 행렬) với bản phát hành (release / 릴리스) SLO, thất bại (failure / 실패) injection và exact-artifact forensic.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **28. hệ thống (system / 시스템) surfaces ngoài Activity** tiếp nhận điểm tựa từ **27. môi trường vận hành (production / 운영 환경) thiết bị (device / 장치) ma trận (matrix / 행렬) và app chất lượng (quality / 품질)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. độ sâu (depth / 깊이) Labs — lập luận (reasoning / 추론) độ sâu (depth / 깊이) coverage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. hệ thống (system / 시스템) surfaces ngoài Activity

Trường hợp (case / 사례) 14 cover started/bound/foreground dịch vụ (service / 서비스), BroadcastReceiver + `goAsync`, ContentProvider/ContentResolver/URI grant, notification/channel/hành động (action / 동작), PendingIntent định danh (identity / 식별자)/mutability, App Widget, Shortcut, Quick Settings Tile, multi-process awareness, WorkManager coordination và exported-component bảo mật (security / 보안).

> **Chuyển mạch:** Trong **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **28. hệ thống (system / 시스템) surfaces ngoài Activity** cho ta quy tắc; **29. độ sâu (depth / 깊이) Labs — lập luận (reasoning / 추론) độ sâu (depth / 깊이) coverage** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **30. Các chủ đề cố ý không biến thành vendor manual** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. độ sâu (depth / 깊이) Labs — lập luận (reasoning / 추론) độ sâu (depth / 깊이) coverage

`depth_labs/` không mở thêm breadth mà làm sâu bảy trục đã có:

| độ sâu (depth / 깊이) Lab | Trọng tâm độ sâu |
|---|---|
| 01 kiến trúc (architecture / 아키텍처) | bất biến (invariant / 불변식), quyền sở hữu (ownership / 소유권), stale snapshot, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계), ambiguous kết quả (outcome / 결과), timeline rà soát (review / 검토) |
| 02 Offline Sync | consistency, durable outbox, idempotency, thứ tự (ordering / 순서), xung đột (conflict / 충돌), cursor atomicity, account isolation |
| 03 Coroutine/luồng (flow / 흐름) | Job cây (tree / 트리), cancellation, supervision, shared-state race, backpressure, stream thời gian tồn tại (lifetime / 수명), deterministic kiểm thử (test / 테스트) |
| 04 Compose | Snapshot định danh (identity / 식별자), tác động (effect / 효과) thời gian tồn tại (lifetime / 수명), phase vô hiệu hóa (invalidation / 무효화), stability, ngữ nghĩa (semantics / 의미론), measured hiệu năng (performance / 성능) |
| 05 độ tin cậy (reliability / 신뢰성) | invariant-based kiểm thử (test / 테스트), di chuyển (migration / 마이그레이션)/quay lui (rollback / 롤백), thất bại (failure / 실패) injection, SLI/SLO, telemetry, rollout/sự cố (incident / 인시던트) vòng lặp (loop / 루프) |
| 06 bản dựng (build / 빌드)/tính tương thích (compatibility / 호환성) | bản dựng (build / 빌드) phase forensic, R8/variant thất bại (failure / 실패), mục tiêu (target / 대상) di chuyển (migration / 마이그레이션), startup đường găng (critical path / 임계 경로), sản phẩm tạo ra (artifact / 산출물) provenance |
| 07 SDK/bản địa (native / 네이티브) | API công khai (public API / 공개 API)/ABI, phụ thuộc (dependency / 의존성) leakage, bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전), JNI thời gian tồn tại (lifetime / 수명)/threading, tính tương thích (compatibility / 호환성) evolution |

Độ sâu (depth / 깊이) Labs được dùng khi người học đã biết API và cần giải thích **tại sao hệ thống vẫn đúng khi thực thi (execution / 실행) thứ tự (order / 순서) không lý tưởng**.

> **Chuyển mạch:** Ở chặng này của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **29. độ sâu (depth / 깊이) Labs — lập luận (reasoning / 추론) độ sâu (depth / 깊이) coverage** cho ta quy tắc; **30. Các chủ đề cố ý không biến thành vendor manual** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **31. Tiêu chí cho vòng cập nhật (update / 업데이트) tiếp theo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Các chủ đề cố ý không biến thành vendor manual

Bộ ghi chú (note / 노트) không cố trở thành tham chiếu (reference / 참조) manual cho Firebase, từng DI khung phần mềm (framework / 프레임워크), từng HTTP máy khách (client / 클라이언트), Google Maps, Billing SDK, từng ML ngăn xếp (stack / 스택), cloud vendor hay mọi API Play Console. Những sản phẩm đó evolve nhanh. Tài liệu ưu tiên mô hình tư duy (mental model / 사고 모델), đặc tả hợp đồng (contract / 계약), thời gian tồn tại (lifetime / 수명), thất bại (failure / 실패), tính tương thích (compatibility / 호환성) và tích hợp (integration / 통합) ranh giới (boundary / 경계) để công cụ (tool / 도구) mới vẫn đặt được vào hệ thống đã hiểu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android — Coverage kiểm tra (audit / 감사)**, **31. Tiêu chí cho vòng cập nhật (update / 업데이트) tiếp theo** tiếp nhận điểm tựa từ **30. Các chủ đề cố ý không biến thành vendor manual** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 31. Tiêu chí cho vòng cập nhật (update / 업데이트) tiếp theo

Sau trường hợp (case / 사례) 20 + độ sâu (depth / 깊이) Labs, breadth của Kotlin + Android đã rất rộng và các ranh giới (boundary / 경계) chính đã có lập luận (reasoning / 추론) sâu. Chapter/lab mới chỉ nên được thêm khi ít nhất một điều đúng:

1. Android/Kotlin có hành vi (behavior / 동작) mới làm thay đổi mô hình tư duy (mental model / 사고 모델) hoặc di chuyển (migration / 마이그레이션) đường dẫn (path / 경로).
2. Một ranh giới (boundary / 경계) môi trường vận hành (production / 운영 환경) quan trọng vẫn chưa được giải thích hoặc bất biến (invariant / 불변식) chưa được chứng minh.
3. Một nhóm legacy mã (code / 코드) phổ biến chưa có di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략).
4. Một dạng thất bại (failure mode / 실패 모드) môi trường vận hành (production / 운영 환경) chưa có khôi phục (recovery / 복구)/kiểm thử (test / 테스트) mô hình (model / 모델).
5. Toolchain/nền tảng (platform / 플랫폼) chính sách (policy / 정책) mới làm ví dụ hiện tại sai.
6. Một lĩnh vực (domain / 도메인) Android chuyên biệt được quyết định học sâu riêng, ví dụ Wear/TV/Auto/XR, game/graphics hoặc ML on-device; khi đó nên tạo sub-library riêng thay vì nhồi vào cốt lõi (core / 핵심) đường dẫn (path / 경로).
7. Một chapter hiện có còn quá tóm tắt; trong trường hợp đó ưu tiên **đào sâu chapter/lab hiện hữu** thay vì tạo thêm title mới.

Không mở rộng chỉ để tăng số dòng. Mục tiêu của bộ ghi chú (note / 노트) là **đủ sâu nhưng có cấu trúc**, để người học biết khái niệm là gì, vì sao tồn tại, khi nào dùng, sự đánh đổi (trade-off / 트레이드오프) ra sao, bất biến (invariant / 불변식) nào phải giữ, nó thất bại như thế nào, sản phẩm tạo ra (artifact / 산출물) nào thực sự chạy trên thiết bị (device / 장치) và cách đặt nó vào một môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) có thể bản dựng (build / 빌드), kiểm thử (test / 테스트), bản phát hành (release / 릴리스), quan sát và evolve lâu dài.

> **Bàn giao:** Sau **31. Tiêu chí cho vòng cập nhật (update / 업데이트) tiếp theo**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

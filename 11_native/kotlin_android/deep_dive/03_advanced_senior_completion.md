# Kotlin + Android Advanced / cấp cao (senior / 시니어) — Completion Deep Dive

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Kotlin + Android Advanced / cấp cao (senior / 시니어) — Completion Deep Dive**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. Bắt đầu ở **Kotlin + Android Advanced / cấp cao (senior / 시니어) — Completion Deep Dive** để mở đối tượng chính của file và câu hỏi cần theo dõi, rồi dùng kết luận đó khi quay về lộ trình rộng hơn.

> tệp (file / 파일) này bổ sung cho [`../03_kotlin_advanced_senior.md`](../03_kotlin_advanced_senior.md). Trọng tâm là những dạng thất bại (failure mode / 실패 모드) và sự đánh đổi (trade-off / 트레이드오프) mà nhà phát triển (developer / 개발자) cấp cao (senior / 시니어) phải lập luận (reasoning / 추론) được: hệ kiểu (type system / 타입 시스템) sâu, cancellation an toàn (safety / 안전), luồng (flow / 흐름) backpressure, Compose Snapshot/định danh (identity / 식별자), background thực thi (execution / 실행), networking/TLS, lưu trữ (storage / 저장소)/backup, nhiều tầng testing và cổng chất lượng (quality gate / 품질 게이트).

# 1. Kotlin hệ kiểu (type system / 타입 시스템) sâu hơn

Ở cấp cao (senior / 시니어) mức (level / 수준), generic không còn chỉ là `List<T>`. Cần hiểu variance theo vị trí producer/bên tiêu thụ (consumer / 소비자), use-site projection, star projection và kiểu (type / 타입) erasure. `List<out T>` có thể đọc T an toàn nhưng không thể tùy ý ghi; bên tiêu thụ (consumer / 소비자) direction được diễn đạt bằng `in` khi phù hợp.

Trên JVM, generic phần lớn bị **kiểu (type / 타입) erasure**, vì vậy thời gian chạy (runtime / 런타임) thường không biết `List<String>` khác `List<Int>`. `reified` kiểu (type / 타입) parameter trong inline hàm (function / 함수) có thể giữ đủ kiểu (type / 타입) đơn vị từ (token / 토큰) cho một số thao tác (operation / 연산) như `is T` hoặc lấy `T::class`, nhưng nó không xóa mọi giới hạn erasure của nested generic.

Kotlin cũng có cú pháp (syntax / 문법) definitely non-null kiểu (type / 타입) `T & Any` trong một số generic/interoperability API để nói rằng T tại ranh giới (boundary / 경계) này chắc chắn non-null. Đây thường gặp hơn khi thiết kế API generic/Java interop hơn là app mã (code / 코드) hàng ngày.

# 2. Cancellation an toàn (safety / 안전) và cleanup

Cancellation là exception-based và cooperative. mã (code / 코드) cấp cao (senior / 시니어) phải đảm bảo tài nguyên (resource / 자원) cleanup vẫn chạy. `finally` được thực thi khi coroutine cancel; nếu cleanup cần gọi suspend hàm (function / 함수), đôi khi cần `withContext(NonCancellable)` rất hẹp.

```kotlin
try {
    repository.sync()
} finally {
    withContext(NonCancellable) {
        auditStore.flushPendingMetadata()
    }
}
```

Không dùng `NonCancellable` để “chống cancel” cả workflow vì sẽ phá structured tính đồng thời (concurrency / 동시성) và UX. Nếu thao tác (operation / 연산) có side tác động (effect / 효과) không thể bỏ dở, thiết kế idempotency/giao dịch (transaction / 트랜잭션) hoặc chuyển nó sang đơn vị sở hữu (owner / 오너) phù hợp như WorkManager thường đúng hơn cố giữ UI coroutine sống mãi.

Một lỗi tinh vi khác là catch `Exception` để map lỗi rồi vô tình nuốt `CancellationException`. Khi viết wrapper chung, hãy rethrow cancellation hoặc dùng API/operator giữ ngữ nghĩa (semantics / 의미론) cancellation đúng.

# 3. luồng (flow / 흐름) backpressure, buffering và conflation

Luồng (flow / 흐름) mặc định tạo backpressure: producer suspend nếu collector xử lý chậm. `buffer()` cho producer/bên tiêu thụ (consumer / 소비자) chạy tách nhịp; `conflate()` bỏ intermediate giá trị (value / 값) khi collector chỉ cần trạng thái mới nhất; `collectLatest` cancel phần xử lý emission trước khi giá trị (value / 값) mới tới.

Lựa chọn này phải theo ngữ nghĩa (semantics / 의미론). tìm kiếm (search / 검색) kết quả (result / 결과) UI có thể dùng latest-wins; sự kiện (event / 이벤트) thanh toán không được `conflate` mất giao dịch. Một operator hiệu năng (performance / 성능) tưởng đơn giản có thể đổi tính đúng đắn của hệ thống.

`SharedFlow` cần thiết kế `replay`, buffer và overflow chiến lược (strategy / 전략) cẩn thận. Dùng `SharedFlow` cho one-off UI sự kiện (event / 이벤트) phải cân nhắc collector vòng đời (lifecycle / 생명주기); nhiều trường hợp trạng thái (state / 상태) mô hình (model / 모델) tốt hơn sự kiện (event / 이벤트) channel vì trạng thái (state / 상태) có thể phục hồi sau recreation.

# 4. Compose Snapshot hệ thống (system / 시스템)

Compose Snapshot trạng thái (state / 상태) là một hệ thống quản lý trạng thái (state / 상태)/phiên bản (version / 버전) chứ không chỉ callback “set giá trị (value / 값) rồi redraw”. Khi composable đọc `State`, thời gian chạy (runtime / 런타임) ghi nhận phụ thuộc (dependency / 의존성); khi trạng thái (state / 상태) đổi, phạm vi (scope / 범위) liên quan có thể invalidate và recomposition. Điều này giải thích vì sao đọc trạng thái (state / 상태) ở phạm vi (scope / 범위) quá cao làm vùng recomposition lớn hơn cần thiết.

Snapshot cũng tạo một mô hình tư duy (mental model / 사고 모델) tương tự giao dịch (transaction / 트랜잭션)/versioned trạng thái (state / 상태). trạng thái (state / 상태) mutation phải tuân convention/thời gian chạy (runtime / 런타임) expectation; dùng chung (shared / 공유) mutable đối tượng (object / 객체) không observable có thể thay đổi mà Compose không biết.

# 5. `CompositionLocal`: ambient phụ thuộc (dependency / 의존성) có kiểm soát

`CompositionLocal` truyền phụ thuộc (dependency / 의존성)/giá trị (value / 값) theo composition cây (tree / 트리) mà không phải đưa parameter qua mọi tầng (layer / 계층). Nó phù hợp cho concern mang tính tree-local như theme, density, localization hoặc một năng lực (capability / 역량) UI-scoped.

```kotlin
val LocalAnalytics = staticCompositionLocalOf<Analytics> {
    error("Analytics not provided")
}
```

Dùng nó như dịch vụ (service / 서비스) locator toàn cục cho repository/nghiệp vụ (business / 비즈니스) phụ thuộc (dependency / 의존성) sẽ làm luồng dữ liệu (data flow / 데이터 흐름) khó theo dõi. Nếu phụ thuộc (dependency / 의존성) là lô-gic (logic / 논리)/lĩnh vực (domain / 도메인) phụ thuộc (dependency / 의존성) bình thường, constructor/ViewModel injection thường rõ hơn.

# 6. Recomposition, bố cục (layout / 레이아웃) và draw là các phase khác nhau

Không nên đồng nhất “recomposition” với “vẽ lại toàn màn hình”. Compose chuỗi xử lý (pipeline / 파이프라인) có composition, bố cục (layout / 레이아웃)/đo lường (measurement / 측정) và draw. Một thay đổi chỉ ảnh hưởng draw có thể không cần recomposition; một thay đổi bố cục (layout / 레이아웃) có thể không cần rebuild toàn subtree.

Tối ưu hóa (optimization / 최적화) cấp cao (senior / 시니어) bắt đầu bằng dấu vết (trace / 추적)/metrics chứ không thêm `remember` vô điều kiện. hàm (function / 함수) rẻ recomposition nhiều lần có thể hoàn toàn ổn; một allocation/bố cục (layout / 레이아웃) đắt ở đường xử lý nóng (hot path / 핫 패스) mới đáng tối ưu.

Stable/immutable mô hình (model / 모델) giúp thời gian chạy (runtime / 런타임) skip tốt hơn trong một số trường hợp, nhưng đừng annotation tùy tiện để “ép stable” khi đặc tả hợp đồng (contract / 계약) mutation không đúng. Sai stability đặc tả hợp đồng (contract / 계약) có thể biến bug trạng thái (state / 상태) thành thứ khó phát hiện hơn.

# 7. định danh (identity / 식별자) và `key`

Compose nhớ trạng thái (state / 상태) dựa trên định danh (identity / 식별자)/position trong composition. Khi một nhóm composable có thể đổi vị trí, `key` giúp thời gian chạy (runtime / 런타임) hiểu logical định danh (identity / 식별자).

```kotlin
for (item in items) {
    key(item.id) {
        ItemRow(item)
    }
}
```

Trong `LazyColumn`, dùng `items(..., key = { it.id })` thường là cách phù hợp hơn. Key phải stable và unique trong phạm vi danh sách (list / 목록).

# 8. Chọn background API theo ngữ nghĩa (semantics / 의미론)

Android có nhiều cơ chế background vì mỗi loại công việc có yêu cầu (requirement / 요구사항) khác nhau. **WorkManager** phù hợp deferred, durable công việc (work / 작업) có ràng buộc (constraint / 제약조건) và có thể chạy lại sau tiến trình (process / 프로세스) death. **Foreground dịch vụ (service / 서비스)** dùng cho tác vụ user-visible đang diễn ra và phải tuân notification/FGS kiểu (type / 타입)/restriction. **AlarmManager** dành cho alarm theo thời điểm; chính xác (exact / 정확한) alarm chỉ khi use trường hợp (case / 사례) thực sự cần và có chính sách (policy / 정책)/permission tương ứng.

Coroutine trong ViewModel chỉ phù hợp công việc gắn thời gian tồn tại (lifetime / 수명) ViewModel, không thay thế durable background scheduling.

Một quyết định tốt bắt đầu bằng câu hỏi: công việc có phải hoàn tất nếu app/tiến trình (process / 프로세스) chết không, có cần thời điểm chính xác không, người dùng (user / 사용자) có nhận biết đang chạy không, có ràng buộc (constraint / 제약조건) mạng/charging không, và OS có quyền trì hoãn không. Sau đó mới chọn API.

# 9. Foreground dịch vụ (service / 서비스) và notification restriction

Foreground dịch vụ (service / 서비스) không phải “dịch vụ (service / 서비스) chạy mãi”. Android ngày càng giới hạn việc start FGS từ background và yêu cầu khai báo dịch vụ (service / 서비스) kiểu (type / 타입)/permission phù hợp use trường hợp (case / 사례). Vì chính sách (policy / 정책) thay đổi theo API mức (level / 수준), môi trường vận hành (production / 운영 환경) mã (code / 코드) phải đọc hành vi (behavior / 동작) thay đổi (change / 변경) của mục tiêu (target / 대상) SDK hiện tại.

Notification channel trên Android 8+ có hành vi (behavior / 동작) do người dùng (user / 사용자) kiểm soát. App không nên giả định importance luôn như lúc tạo channel ban đầu. Android mới cũng có notification thời gian chạy (runtime / 런타임) permission; UX cần hoạt động hợp lý khi người dùng (user / 사용자) từ chối.

# 10. thử lại (retry / 재시도), idempotency và exponential backoff

Thử lại (retry / 재시도) chỉ an toàn khi thao tác (operation / 연산) idempotent hoặc backend có idempotency key. GET thường thử lại (retry / 재시도) dễ hơn POST tạo giao dịch. Nếu yêu cầu (request / 요청) “create thứ tự (order / 순서)” hết thời gian chờ (timeout / 타임아웃) sau khi máy chủ (server / 서버) đã lần ghi nhận (commit / 커밋) nhưng máy khách (client / 클라이언트) chưa nhận phản hồi (response / 응답), thử lại (retry / 재시도) mù có thể tạo thứ tự (order / 순서) thứ hai.

Exponential backoff giúp giảm tải khi backend/mạng có vấn đề; jitter tránh nhiều máy khách (client / 클라이언트) thử lại (retry / 재시도) cùng thời điểm. thử lại (retry / 재시도) chính sách (policy / 정책) phải phân loại lỗi: 400 kiểm tra hợp lệ (validation / 검증) thường không thử lại (retry / 재시도), 401 có thể trigger auth refresh, 429/503 có thể thử lại (retry / 재시도) theo chính sách (policy / 정책) và `Retry-After` nếu máy chủ (server / 서버) cung cấp.

# 11. HTTP bộ nhớ đệm (cache / 캐시) và app bộ nhớ đệm (cache / 캐시)

HTTP bộ nhớ đệm (cache / 캐시) có thể giảm độ trễ (latency / 지연 시간)/dữ liệu (data / 데이터) nhưng phải tôn trọng freshness/kiểm tra hợp lệ (validation / 검증) ngữ nghĩa (semantics / 의미론). ETag/If-None-Match cho phép revalidation. App-layer bộ nhớ đệm (cache / 캐시) như Room giải quyết source-of-truth/offline UX khác với HTTP bộ nhớ đệm (cache / 캐시) ở tầng vận chuyển (transport layer / 전송 계층).

Khi nói “bộ nhớ đệm (cache / 캐시)”, luôn trả lời bộ nhớ đệm (cache / 캐시) cái gì, key là gì, stale sau bao lâu, invalidate bằng gì, và khi bộ nhớ đệm (cache / 캐시)/mạng (network / 네트워크) khác nhau thì nguồn nào thắng.

# 12. TLS và certificate pinning

TLS mặc định của nền tảng (platform / 플랫폼)/OkHttp thường an toàn hơn tự viết trust manager. Không bao giờ “fix SSL lỗi (error / 오류)” bằng trust-all certificate verifier trong môi trường vận hành (production / 운영 환경).

Certificate pinning tăng một số lớp phòng thủ nhưng tạo operational rủi ro (risk / 위험) khi certificate rotation. Nếu dùng, phải có backup pin và quy trình rotation rõ ràng. Pinning không thay thế hostname xác minh (verification / 확인), authorization hay secure backend.

# 13. WebSocket, SSE và long-lived liên kết (connection / 연결)

WebSocket/SSE là liên kết (connection / 연결) lâu sống; cần vòng đời (lifecycle / 생명주기), reconnect, heartbeat, duplicate sự kiện (event / 이벤트) và thứ tự (ordering / 순서) chiến lược (strategy / 전략). Đừng gắn liên kết (connection / 연결) trực tiếp vào composable thời gian tồn tại (lifetime / 수명) nếu lĩnh vực (domain / 도메인) session sống rộng hơn màn hình.

Khi reconnect, máy chủ (server / 서버)/máy khách (client / 클라이언트) cần biết từ chuỗi (sequence / 시퀀스) nào tiếp tục hoặc chấp nhận duplicate rồi deduplicate bằng sự kiện (event / 이벤트) ID. Nếu không có giao thức (protocol / 프로토콜) chiến lược (strategy / 전략), “reconnect tự động” có thể gây mất hoặc lặp dữ liệu.

# 14. lưu trữ (storage / 저장소), backup và dữ liệu nhạy cảm

DataStore phù hợp setting/preferences nhỏ; Room phù hợp relational structured dữ liệu (data / 데이터); tệp (file / 파일) lưu trữ (storage / 저장소) phù hợp blob/document; MediaStore/lưu trữ (storage / 저장소) truy cập (access / 접근) khung phần mềm (framework / 프레임워크) dùng cho media/document theo scoped lưu trữ (storage / 저장소) mô hình (model / 모델).

Dữ liệu nhạy cảm cần threat mô hình (model / 모델). Android Keystore bảo vệ key material bằng hệ thống (system / 시스템)/hardware-backed năng lực (capability / 역량) khi có, nhưng ciphertext, siêu dữ liệu (metadata / 메타데이터) và backup chính sách (policy / 정책) vẫn phải thiết kế. Kiểm tra `android:allowBackup`, dữ liệu (data / 데이터) extraction rules và cloud/device-transfer hành vi (behavior / 동작) để tránh dữ liệu không nên rời thiết bị bị backup ngoài ý muốn.

# 15. JVM kiểm thử (test / 테스트), Robolectric và instrumented kiểm thử (test / 테스트)

Pure Kotlin/lĩnh vực (domain / 도메인) kiểm thử (test / 테스트) chạy JVM nhanh nhất. Robolectric mô phỏng nhiều Android API trên JVM và hữu ích ở middle tầng (layer / 계층) nhưng không thay thế thiết bị thật cho mọi hành vi (behavior / 동작). Instrumented kiểm thử (test / 테스트) kiểm tra tích hợp (integration / 통합) với Android thời gian chạy (runtime / 런타임)/thiết bị (device / 장치).

Không nên đưa toàn bộ kiểm thử (test / 테스트) xuống instrumented chỉ vì mã (code / 코드) chạm Android. Nếu lô-gic nghiệp vụ (business logic / 비즈니스 로직) có thể tách khỏi khung phần mềm (framework / 프레임워크) ranh giới (boundary / 경계), kiểm thử (test / 테스트) phần lô-gic (logic / 논리) ở JVM và chỉ giữ số lượng nhỏ kiểm thử tích hợp (integration test / 통합 테스트) quanh ranh giới (boundary / 경계) Android.

# 16. Compose UI testing

Compose UI kiểm thử (test / 테스트) tương tác với **ngữ nghĩa (semantics / 의미론) cây (tree / 트리)**, không phải điểm ảnh (pixel / 픽셀) cây (tree / 트리). Điều này khuyến khích UI có ngữ nghĩa (semantics / 의미론)/khả năng tiếp cận (accessibility / 접근성) tốt.

```kotlin
composeTestRule
    .onNodeWithText("Save")
    .performClick()
```

Kiểm thử (test / 테스트) nên assert hành vi (behavior / 동작) user-visible thay vì nội bộ (internal / 내부) composable lời gọi (call / 호출). Khi kiểm thử (test / 테스트) khó tìm nút (node / 노드), đôi khi vấn đề thật nằm ở ngữ nghĩa (semantics / 의미론)/khả năng tiếp cận (accessibility / 접근성) chứ không phải testing API.

# 17. hiệu năng (performance / 성능) kiểm thử (test / 테스트): Macrobenchmark và Baseline Profile

Macrobenchmark đo journey như startup/scroll/tương tác (interaction / 상호작용) ở app mức (level / 수준). Baseline Profile ghi lại đường đi mã (code path / 코드 경로) quan trọng để ART compile tối ưu sớm hơn. Hai thứ liên quan nhưng không đồng nghĩa: profile có thể cải thiện thời gian chạy (runtime / 런타임) đường dẫn (path / 경로), benchmark dùng để chứng minh improvement/regression.

Benchmark cần thiết bị/thermal trạng thái (state / 상태) đủ ổn định. Một lần chạy trên emulator mạnh không phải bằng chứng (evidence / 증거) môi trường vận hành (production / 운영 환경).

# 18. Android Lint và static phân tích (analysis / 분석)

Android Lint hiểu nhiều Android-specific issue như vòng đời (lifecycle / 생명주기), tài nguyên (resource / 자원), API mức (level / 수준), manifest và Compose. trình biên dịch (compiler / 컴파일러) warning, Lint, formatter/static-analysis công cụ (tool / 도구) như ktlint/Detekt nếu nhóm (team / 팀) chọn dùng có thể trở thành CI cổng chất lượng (quality gate / 품질 게이트).

Baseline chỉ nên là chiến lược di chuyển (migration / 마이그레이션): ghi nhận debt hiện có để chặn debt mới, rồi giảm dần baseline. Không để baseline trở thành “thùng rác warning vĩnh viễn”.

# 19. cấp cao (senior / 시니어) rà soát (review / 검토) khung phần mềm (framework / 프레임워크)

Khi rà soát (review / 검토) một tính năng (feature / 기능), đừng chỉ đọc happy đường dẫn (path / 경로). Hãy hỏi: coroutine thuộc phạm vi (scope / 범위) nào, cancellation có dọn tài nguyên (resource / 자원) không, luồng (flow / 흐름) có backpressure ngữ nghĩa (semantics / 의미론) đúng không, trạng thái (state / 상태) có nguồn chuẩn (source of truth / 정본) nào, tiến trình (process / 프로세스) death xảy ra thì sao, thử lại (retry / 재시도) có duplicate side tác động (effect / 효과) không, cục bộ (local / 로컬) lược đồ (schema / 스키마) upgrade ra sao, background công việc (work / 작업) có đúng API không, dữ liệu nhạy cảm có backup/log không, và chỉ số (metric / 지표) nào chứng minh hiệu năng (performance / 성능) ổn.

Senior-level rà soát mã (code review / 코드 리뷰) là kiểm tra **thời gian tồn tại (lifetime / 수명) + quyền sở hữu (ownership / 소유권) + thất bại (failure / 실패) + khôi phục (recovery / 복구) + khả năng quan sát (observability / 관측 가능성)**, không chỉ style hoặc mẫu (pattern / 패턴) name.

# 20. Checklist hoàn thiện Advanced / cấp cao (senior / 시니어)

Bạn nên lập luận (reasoning / 추론) được về cancellation/thất bại (failure / 실패), backpressure, Compose snapshot/phase/định danh (identity / 식별자), background thực thi (execution / 실행) ngữ nghĩa (semantics / 의미론), lưu trữ (storage / 저장소)/backup, mạng (network / 네트워크) thử lại (retry / 재시도)/TLS, long-lived liên kết (connection / 연결), test-layer sự đánh đổi (trade-off / 트레이드오프), benchmark và cổng chất lượng (quality gate / 품질 게이트). Seniority thể hiện ở khả năng dự đoán dạng thất bại (failure mode / 실패 모드) và blast radius trước khi chọn thư viện (library / 라이브러리) hoặc mẫu (pattern / 패턴).

> **Bàn giao:** Sau **Kotlin + Android Advanced / cấp cao (senior / 시니어) — Completion Deep Dive**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

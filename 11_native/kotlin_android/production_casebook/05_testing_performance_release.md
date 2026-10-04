# Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** [README](./README.md) là owner của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**; dùng README để đặt case ở cuối tuyến Android production. Từ **1. kiểm thử (test / 테스트) theo rủi ro (risk / 위험)** nối domain/contract tests với profiling, benchmark, reproducible build, signing, staged rollout, telemetry và rollback, rồi biến quality pipeline thành bằng chứng release.

Một Android app “chạy được trên máy dev” còn rất xa môi trường vận hành (production / 운영 환경). môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질) đòi hỏi ba vòng phản hồi liên tục: **tính đúng đắn (correctness / 정확성)** được bảo vệ bằng kiểm thử (test / 테스트) và static phân tích (analysis / 분석); **hiệu năng (performance / 성능)** được đo bằng profiler/benchmark thay vì cảm giác; **bản phát hành (release / 릴리스)** được kiểm soát bằng reproducible bản dựng (build / 빌드), signing, staged rollout, telemetry và quay lui (rollback / 롤백) plan.

Chương này không liệt kê công cụ (tool / 도구) đơn lẻ mà xây một chất lượng (quality / 품질) chuỗi xử lý (pipeline / 파이프라인) từ mã (code / 코드) tới Play bản phát hành (release / 릴리스).

## 1. kiểm thử (test / 테스트) theo rủi ro (risk / 위험), không theo tỷ lệ thần thánh

“70% đơn vị (unit / 단위), 20% tích hợp (integration / 통합), 10% UI” không phải luật. kiểm thử (test / 테스트) chiến lược (strategy / 전략) phải phản ánh thất bại (failure / 실패) chi phí (cost / 비용).

Pure nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) nên có đơn vị (unit / 단위) kiểm thử (test / 테스트) nhanh. ánh xạ (mapping / 매핑)/mạng (network / 네트워크) serialization cần đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트). Room di chuyển (migration / 마이그레이션) cần di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) thật. điều hướng (navigation / 내비게이션)/deep link cần tích hợp (integration / 통합)/UI kiểm thử (test / 테스트). Payment/auth cần nhiều tầng hơn một màn hình brochure.

Mục tiêu là mỗi trọng yếu (critical / 중요) hành vi (behavior / 동작) có kiểm thử (test / 테스트) ở tầng rẻ nhất đủ chứng minh hành vi (behavior / 동작) đó.

> **Nối mạch:** Risk-based testing chọn unit boundary theo failure impact; domain logic test trước, rồi fake stateful repository giúp integration behavior lặp lại ổn định hơn mock.

## 2. đơn vị (unit / 단위) kiểm thử (test / 테스트) lĩnh vực (domain / 도메인) lô-gic (logic / 논리)

Một use trường hợp (case / 사례) thuần Kotlin không cần emulator:

```kotlin
class CalculateCartTotalUseCase {
    operator fun invoke(items: List<CartItem>): Money =
        items.fold(Money.zero()) { total, item ->
            total + item.price * item.quantity
        }
}
```

Kiểm thử (test / 테스트) ranh giới (boundary / 경계) quan trọng hơn happy đường dẫn (path / 경로):

```kotlin
@Test
fun zero_quantity_does_not_change_total() {
    val result = CalculateCartTotalUseCase()(
        listOf(CartItem(price = Money.of(10), quantity = 0))
    )
    assertEquals(Money.zero(), result)
}
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **3. Fake thường hữu ích hơn mock cho stateful repository** nối từ **2. đơn vị (unit / 단위) kiểm thử (test / 테스트) lĩnh vực (domain / 도메인) lô-gic (logic / 논리)** sang **4. Coroutine kiểm thử (test / 테스트) và virtual thời gian (time / 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Fake thường hữu ích hơn mock cho stateful repository

Mock rất tốt để verify tương tác (interaction / 상호작용) nhỏ, nhưng với luồng (flow / 흐름)/repository stateful, fake có thể mô phỏng hành vi (behavior / 동작) tự nhiên hơn.

```kotlin
class FakeArticlesRepository : ArticlesRepository {
    private val data = MutableStateFlow<List<Article>>(emptyList())

    override fun observeArticles(): Flow<List<Article>> = data

    override suspend fun refresh() = Unit

    override suspend fun toggleBookmark(articleId: String) {
        data.update { items ->
            items.map { if (it.id == articleId) it.copy(bookmarked = !it.bookmarked) else it }
        }
    }
}
```

ViewModel kiểm thử (test / 테스트) có thể assert chuyển tiếp trạng thái (state transition / 상태 전이) thay vì verify “phương thức (method / 메서드) X được gọi đúng một lần” trong mọi trường hợp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **4. Coroutine kiểm thử (test / 테스트) và virtual thời gian (time / 시간)** nối từ **3. Fake thường hữu ích hơn mock cho stateful repository** sang **5. Main dispatcher trong kiểm thử (test / 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Coroutine kiểm thử (test / 테스트) và virtual thời gian (time / 시간)

Mã (code / 코드) dùng `delay`, thử lại (retry / 재시도)/backoff hoặc debounce không nên làm kiểm thử (test / 테스트) ngủ thật.

```kotlin
@Test
fun search_is_debounced() = runTest {
    viewModel.onQueryChanged("kot")
    advanceTimeBy(299)
    assertEquals(0, repository.searchCount)

    advanceTimeBy(1)
    runCurrent()
    assertEquals(1, repository.searchCount)
}
```

Inject dispatcher/scheduler-friendly phụ thuộc (dependency / 의존성) thay vì hard-code luồng thực thi (thread / 스레드) hành vi (behavior / 동작) khắp nơi.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **5. Main dispatcher trong kiểm thử (test / 테스트)** nối từ **4. Coroutine kiểm thử (test / 테스트) và virtual thời gian (time / 시간)** sang **6. luồng (flow / 흐름) kiểm thử (test / 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Main dispatcher trong kiểm thử (test / 테스트)

ViewModel dùng `viewModelScope` cần kiểm thử (test / 테스트) Main dispatcher. Có thể dùng kiểm thử (test / 테스트) quy tắc (rule / 규칙) thiết lập `Dispatchers.Main` thành `StandardTestDispatcher` và reset sau kiểm thử (test / 테스트).

Điểm quan trọng là tất cả coroutine trong kiểm thử (test / 테스트) chia sẻ cùng `TestCoroutineScheduler` nếu muốn deterministic virtual thời gian (time / 시간).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **5. Main dispatcher trong kiểm thử (test / 테스트)** đặt đầu vào cho **6. luồng (flow / 흐름) kiểm thử (test / 테스트)**, rồi **7. Room kiểm thử (test / 테스트)** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. luồng (flow / 흐름) kiểm thử (test / 테스트)

Với StateFlow, nhiều trường hợp (case / 사례) có thể assert `value`. Với luồng (flow / 흐름) chuỗi (sequence / 시퀀스), có thể collect bằng kiểm thử (test / 테스트) helper/thư viện (library / 라이브러리) phù hợp hoặc tự collect có kiểm soát.

Kiểm thử (test / 테스트) nên chú ý conflation: StateFlow đại diện trạng thái (state / 상태) mới nhất, không đảm bảo kiểm thử (test / 테스트) observer thấy mọi intermediate giá trị (value / 값) nếu producer chạy nhanh. Nếu cần assert chuỗi (sequence / 시퀀스) sự kiện (event / 이벤트), chọn thành phần nguyên thủy (primitive / 기본 요소) phù hợp.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **6. luồng (flow / 흐름) kiểm thử (test / 테스트)** đặt đầu vào cho **7. Room kiểm thử (test / 테스트)**, rồi **8. mạng (network / 네트워크) đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트)** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Room kiểm thử (test / 테스트)

DAO truy vấn (query / 쿼리) nên kiểm thử (test / 테스트) với cơ sở dữ liệu (database / 데이터베이스) thực in-memory hoặc kiểm thử (test / 테스트) DB, không mock SQL hành vi (behavior / 동작).

Kiểm thử (test / 테스트) giao dịch (transaction / 트랜잭션)/bất biến (invariant / 불변식) như:

- upsert preserve cục bộ (local / 로컬) bookmark;
- delete cascade đúng;
- unique ràng buộc (constraint / 제약조건) đúng;
- quan hệ (relation / 관계) truy vấn (query / 쿼리) không duplicate;
- giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백) khi một bước thất bại (fail / 실패).

Di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) phải dùng lược đồ (schema / 스키마) cũ và dữ liệu trường hợp biên (edge case / 경계 사례) như đã trình bày ở trường hợp (case / 사례) 03.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **8. mạng (network / 네트워크) đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트)** nối từ **7. Room kiểm thử (test / 테스트)** sang **9. Compose UI kiểm thử (test / 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. mạng (network / 네트워크) đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트)

Không cần gọi môi trường vận hành (production / 운영 환경) backend trong đơn vị (unit / 단위) kiểm thử (test / 테스트). Dùng fake HTTP máy chủ (server / 서버) để kiểm thử (test / 테스트):

- URL/đường dẫn (path / 경로)/truy vấn (query / 쿼리)/header;
- serialization/deserialization;
- 2xx/4xx/5xx ánh xạ (mapping / 매핑);
- hết thời gian chờ (timeout / 타임아웃)/cancellation;
- malformed phản hồi (response / 응답);
- unknown trường dữ liệu (field / 필드)/enum tính tương thích (compatibility / 호환성).

Đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) hữu ích hơn mock Retrofit giao diện (interface / 인터페이스) vì nó kiểm thử (test / 테스트) ranh giới (boundary / 경계) wire thực tế.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **9. Compose UI kiểm thử (test / 테스트)** nối từ **8. mạng (network / 네트워크) đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트)** sang **10. Screenshot kiểm thử (test / 테스트) và visual regression**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Compose UI kiểm thử (test / 테스트)

Pure content composable giúp kiểm thử (test / 테스트) dễ:

```kotlin
composeTestRule.setContent {
    ArticlesScreen(
        state = ArticlesUiState(items = sampleItems),
        onBookmark = { bookmarkedId = it },
        onOpenArticle = {}
    )
}

composeTestRule
    .onNodeWithText("Kotlin Coroutines")
    .assertIsDisplayed()
```

Dùng ngữ nghĩa (semantics / 의미론)/testTag khi văn bản (text / 텍스트)/content description không đủ ổn định, nhưng đừng làm UI chỉ để phục vụ kiểm thử (test / 테스트) nếu ngữ nghĩa (semantics / 의미론) user-facing có thể dùng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **10. Screenshot kiểm thử (test / 테스트) và visual regression** nối từ **9. Compose UI kiểm thử (test / 테스트)** sang **11. khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Screenshot kiểm thử (test / 테스트) và visual regression

Lô-gic (logic / 논리) kiểm thử (test / 테스트) không phát hiện padding sai, dark theme broken hoặc văn bản (text / 텍스트) overflow. Screenshot kiểm thử (test / 테스트) hữu ích cho thiết kế (design / 설계) hệ thống (system / 시스템)/thành phần (component / 컴포넌트) ổn định.

Cần kiểm soát font, density, locale, thiết bị (device / 장치) cấu hình (config / 설정) để giảm flaky điểm ảnh (pixel / 픽셀) diff. Với động (dynamic / 동적) content, kiểm thử (test / 테스트) thành phần (component / 컴포넌트)/trạng thái (state / 상태) cụ thể hơn full app screenshot.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **11. khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트)** nối từ **10. Screenshot kiểm thử (test / 테스트) và visual regression** sang **12. Instrumented kiểm thử (test / 테스트) chọn lọc**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트)

Cổng chất lượng (quality gate / 품질 게이트) nên kiểm tra content description, touch mục tiêu (target / 대상), contrast, font scaling và ngữ nghĩa (semantics / 의미론) cây (tree / 트리). Một screen “đẹp” ở font 1.0 có thể unusable ở font quy mô (scale / 규모) lớn.

Kiểm thử (test / 테스트) manual với TalkBack vẫn quan trọng vì automated quy tắc (rule / 규칙) không đánh giá được toàn bộ reading thứ tự (order / 순서) và tương tác (interaction / 상호작용) ngữ nghĩa (semantics / 의미론).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **12. Instrumented kiểm thử (test / 테스트) chọn lọc** nối từ **11. khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트)** sang **13. End-to-end kiểm thử (test / 테스트) ít nhưng giá trị cao**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Instrumented kiểm thử (test / 테스트) chọn lọc

Instrumented kiểm thử (test / 테스트) chậm hơn cục bộ (local / 로컬) JVM, nên dành cho hành vi (behavior / 동작) phụ thuộc Android khung phần mềm (framework / 프레임워크)/thiết bị (device / 장치): permission, Activity vòng đời (lifecycle / 생명주기), cơ sở dữ liệu (database / 데이터베이스) tích hợp (integration / 통합) đặc thù, deep link/tác vụ (task / 작업) hành vi (behavior / 동작), biometric/credential luồng (flow / 흐름) có kiểm thử (test / 테스트) harness phù hợp.

Không biến mọi đơn vị (unit / 단위) kiểm thử (test / 테스트) thành emulator kiểm thử (test / 테스트).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **13. End-to-end kiểm thử (test / 테스트) ít nhưng giá trị cao** nối từ **12. Instrumented kiểm thử (test / 테스트) chọn lọc** sang **14. Static phân tích (analysis / 분석) là kiểm thử (test / 테스트) chạy trước thời gian chạy (runtime / 런타임)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. End-to-end kiểm thử (test / 테스트) ít nhưng giá trị cao

Một số người dùng (user / 사용자) journey trọng yếu (critical / 중요) nên có E2E smoke kiểm thử (test / 테스트):

```text
cold start
→ restore session
→ open home
→ create item
→ item appears
→ restart app
→ item persists
```

E2E dễ flaky nếu phụ thuộc backend/mạng (network / 네트워크) thật. Có thể dùng controlled kiểm thử (test / 테스트) môi trường (environment / 환경), fake backend hoặc hermetic phụ thuộc (dependency / 의존성) tùy mục tiêu.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **14. Static phân tích (analysis / 분석) là kiểm thử (test / 테스트) chạy trước thời gian chạy (runtime / 런타임)** nối từ **13. End-to-end kiểm thử (test / 테스트) ít nhưng giá trị cao** sang **15. hiệu năng (performance / 성능): đo trước khi tối ưu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Static phân tích (analysis / 분석) là kiểm thử (test / 테스트) chạy trước thời gian chạy (runtime / 런타임)

Android Lint, Kotlin trình biên dịch (compiler / 컴파일러) warning, detekt/ktlint hoặc công cụ (tool / 도구) tương đương giúp bắt issue sớm. Nhưng quy tắc (rule / 규칙) phải có đơn vị sở hữu (owner / 오너) và chính sách (policy / 정책), không bật hàng trăm quy tắc (rule / 규칙) rồi suppress toàn bộ.

CI nên thất bại (fail / 실패) trên warning quan trọng như exported thành phần (component / 컴포넌트) không an toàn, tài nguyên (resource / 자원) issue, API misuse, Compose stability issue có quy tắc (rule / 규칙) tương ứng, hoặc kiến trúc (architecture / 아키텍처) phụ thuộc (dependency / 의존성) violation nếu dự án (project / 프로젝트) có custom quy tắc (rule / 규칙).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **15. hiệu năng (performance / 성능): đo trước khi tối ưu** nối từ **14. Static phân tích (analysis / 분석) là kiểm thử (test / 테스트) chạy trước thời gian chạy (runtime / 런타임)** sang **16. Startup ngân sách (budget / 예산)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. hiệu năng (performance / 성능): đo trước khi tối ưu

Bốn nhóm chỉ số (metric / 지표) thường quan trọng:

- startup: cold/warm/hot startup;
- frame rendering: jank/frame thời gian (time / 시간);
- bộ nhớ (memory / 메모리): allocation, vùng nhớ động (heap / 힙) growth, leak;
- tài nguyên (resource / 자원): CPU, battery, mạng (network / 네트워크), disk.

Không optimize một `map` nhỏ trong khi main luồng thực thi (thread / 스레드) đang parse 5 MB JSON.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **16. Startup ngân sách (budget / 예산)** nối từ **15. hiệu năng (performance / 성능): đo trước khi tối ưu** sang **17. Macrobenchmark**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Startup ngân sách (budget / 예산)

Ứng dụng (application / 애플리케이션) startup dễ bị chậm vì DI đồ thị (graph / 그래프) eager, SDK initialization, cơ sở dữ liệu (database / 데이터베이스) open, disk I/O hoặc mạng (network / 네트워크) setup trên main luồng thực thi (thread / 스레드).

Phân loại init:

```text
must before first frame
should before first interaction
can lazy after screen visible
can defer until feature first used
```

Không phải SDK nào cũng cần init trong `Application.onCreate()`.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **17. Macrobenchmark** nối từ **16. Startup ngân sách (budget / 예산)** sang **18. Baseline Profiles**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Macrobenchmark

Macrobenchmark đo hành vi (behavior / 동작) như startup/scroll ở app bản dựng (build / 빌드) gần môi trường vận hành (production / 운영 환경) hơn đơn vị (unit / 단위) benchmark.

Một benchmark tốt có scenario ổn định, warmup/iteration hợp lý và chỉ số (metric / 지표) cụ thể. So sánh regression theo baseline thay vì nhìn một con số một lần.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **18. Baseline Profiles** nối từ **17. Macrobenchmark** sang **19. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Baseline Profiles

Baseline Profile giúp thời gian chạy (runtime / 런타임) precompile hot đường đi mã (code path / 코드 경로), cải thiện startup và tương tác (interaction / 상호작용). Profile cần đại diện journey thực tế: launch, navigate screen chính, scroll/danh sách (list / 목록) tương tác (interaction / 상호작용).

Profile cũ không nên được coi là “set and forget”; khi app luồng (flow / 흐름) thay đổi, regenerate/rà soát (review / 검토).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **19. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)** nối từ **18. Baseline Profiles** sang **20. Compose hiệu năng (performance / 성능)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)

Khi UI jank, dấu vết (trace / 추적) giúp thấy main luồng thực thi (thread / 스레드) làm gì, binder, scheduling, I/O, GC và frame timeline. Đây là bước chuyển từ đoán “Compose chậm” sang biết chính xác (exact / 정확한) công việc (work / 작업) gây frame miss.

Một dấu vết (trace / 추적) investigation nên ghi:

```text
symptom → reproduction → trace marker → root cause → fix → benchmark before/after
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **20. Compose hiệu năng (performance / 성능)** nối từ **19. Perfetto/hệ thống (system / 시스템) dấu vết (trace / 추적)** sang **21. Leak investigation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Compose hiệu năng (performance / 성능)

Recomposition không mặc định xấu. Vấn đề là expensive công việc (work / 작업) trong composition, unstable parameter gây vô hiệu hóa (invalidation / 무효화) rộng, allocation nhiều trong đường xử lý nóng (hot path / 핫 패스) hoặc bố cục (layout / 레이아웃)/draw quá nặng.

Đưa calculation nặng ra khỏi composition hoặc dùng memoization phù hợp:

```kotlin
val filtered by remember(items, query) {
    derivedStateOf { items.filter { it.matches(query) } }
}
```

Nhưng không bọc mọi expression bằng `remember`. Memoization cũng có độ phức tạp (complexity / 복잡도)/bộ nhớ (memory / 메모리) chi phí (cost / 비용).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **21. Leak investigation** nối từ **20. Compose hiệu năng (performance / 성능)** sang **22. ANR**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Leak investigation

Leak thường đến từ đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) sai: singleton giữ Activity, listener không unregister, coroutine phạm vi (scope / 범위) dài hơn đơn vị sở hữu (owner / 오너), callback giữ Fragment/View, static bộ nhớ đệm (cache / 캐시) giữ large đối tượng (object / 객체).

Vùng nhớ vùng nhớ động (heap / 힙) dump/leak detector chỉ ra tham chiếu (reference / 참조) chuỗi (chain / 사슬). Fix gốc (root / 루트) quyền sở hữu (ownership / 소유권), không chỉ set random variable `null`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **22. ANR** nối từ **21. Leak investigation** sang **23. bản phát hành (release / 릴리스) bản dựng (build / 빌드) phải khác gỡ lỗi (debug / 디버그)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. ANR

ANR không chỉ do infinite vòng lặp (loop / 루프). Sync disk I/O, binder lời gọi (call / 호출) lâu, tranh chấp khóa (lock contention / 잠금 경합), heavy serialization hoặc main luồng thực thi (thread / 스레드) chờ worker đều có thể gây freeze.

Một mutex dùng sai trên main luồng thực thi (thread / 스레드) hoặc `runBlocking` trong callback khung phần mềm (framework / 프레임워크) cũng có thể tạo ANR/deadlock.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **23. bản phát hành (release / 릴리스) bản dựng (build / 빌드) phải khác gỡ lỗi (debug / 디버그)** nối từ **22. ANR** sang **24. R8 và keep quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. bản phát hành (release / 릴리스) bản dựng (build / 빌드) phải khác gỡ lỗi (debug / 디버그)

Gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) thường bật logging, inspection, mock menu và không minify. bản phát hành (release / 릴리스) cần:

- bản phát hành (release / 릴리스) signing;
- R8/minification/tài nguyên (resource / 자원) shrink nếu phù hợp;
- gỡ lỗi (debug / 디버그) endpoint/menu bị loại;
- secret/cấu hình (config / 설정) môi trường vận hành (production / 운영 환경) đúng;
- mạng (network / 네트워크) bảo mật (security / 보안) chính sách (policy / 정책) môi trường vận hành (production / 운영 환경);
- crash/analytics ánh xạ (mapping / 매핑) tệp (file / 파일) upload;
- `android:debuggable=false` theo hệ thống dựng (build system / 빌드 시스템);
- versionCode/versionName traceable.

Không kiểm thử (test / 테스트) hiệu năng (performance / 성능) trên gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) rồi kết luận bản phát hành (release / 릴리스) hiệu năng (performance / 성능).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **24. R8 và keep quy tắc (rule / 규칙)** nối từ **23. bản phát hành (release / 릴리스) bản dựng (build / 빌드) phải khác gỡ lỗi (debug / 디버그)** sang **25. Signing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. R8 và keep quy tắc (rule / 규칙)

Reflection/serialization/JNI có thể cần keep siêu dữ liệu (metadata / 메타데이터)/lớp (class / 클래스). Không thêm `-keep class ** { *; }` để “fix crash” vì nó vô hiệu hóa shrink lớn.

Tìm ranh giới (boundary / 경계) nào cần reflection và giữ tối thiểu. thư viện (library / 라이브러리) nên cung cấp bên tiêu thụ (consumer / 소비자) ProGuard quy tắc (rule / 규칙) nếu cần.

Bản phát hành (release / 릴리스) kiểm thử (test / 테스트) phải chạy minified bản dựng (build / 빌드) vì bug R8 chỉ xuất hiện ở đó.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **25. Signing** nối từ **24. R8 và keep quy tắc (rule / 규칙)** sang **26. Reproducible phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Signing

Signing key là định danh (identity / 식별자) cập nhật (update / 업데이트) của app. Mất key hoặc leak key là sự cố (incident / 인시던트) nghiêm trọng. Với Play App Signing, quản lý upload key và Play signing luồng (flow / 흐름) đúng.

Không lần ghi nhận (commit / 커밋) keystore/password vào repository. CI lấy secret từ secure secret store và giới hạn quyền.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **26. Reproducible phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** nối từ **25. Signing** sang **27. CI stages**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Reproducible phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)

Phiên bản (version / 버전) danh mục (catalog / 카탈로그)/BOM giúp centralize phiên bản (version / 버전). phụ thuộc (dependency / 의존성) locking hoặc xác minh (verification / 확인) giúp giảm bản dựng (build / 빌드) “hôm nay khác hôm qua”.

CI nên có command rõ ràng bản dựng (build / 빌드) từ clean checkout. Nếu chỉ máy một nhà phát triển (developer / 개발자) bản dựng (build / 빌드) được vì cục bộ (local / 로컬) Maven bộ nhớ đệm (cache / 캐시)/manual SDK tệp (file / 파일), chuỗi xử lý (pipeline / 파이프라인) chưa reproducible.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **27. CI stages** nối từ **26. Reproducible phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)** sang **28. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) và CI bộ nhớ đệm (cache / 캐시)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. CI stages

Một chuỗi xử lý (pipeline / 파이프라인) điển hình:

```text
checkout
→ verify formatting/static analysis
→ unit tests
→ build debug/release-like artifacts
→ integration/instrumented tests selected
→ lint
→ generate signed artifact in protected job
→ upload mapping/baseline metadata
→ publish internal track
```

Không nhất thiết mọi PR chạy full thiết bị (device / 장치) ma trận (matrix / 행렬); có thể tách fast PR gate và nightly/bản phát hành (release / 릴리스) suite.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **28. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) và CI bộ nhớ đệm (cache / 캐시)** nối từ **27. CI stages** sang **29. Staged rollout**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) và CI bộ nhớ đệm (cache / 캐시)

Bộ nhớ đệm (cache / 캐시) giúp nhanh nhưng bộ nhớ đệm (cache / 캐시) key sai có thể gây sản phẩm tạo ra (artifact / 산출물) stale. bộ nhớ đệm (cache / 캐시) Gradle theo tệp (file / 파일)/phiên bản (version / 버전) phù hợp, không bộ nhớ đệm (cache / 캐시) đầu ra (output / 출력) tùy tiện mà không hiểu vô hiệu hóa (invalidation / 무효화).

Đừng dùng bộ nhớ đệm (cache / 캐시) để che bản dựng (build / 빌드) phụ thuộc (dependency / 의존성) không khai báo. Clean bản dựng (build / 빌드) định kỳ hữu ích phát hiện hidden phụ thuộc (dependency / 의존성).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **29. Staged rollout** nối từ **28. bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) và CI bộ nhớ đệm (cache / 캐시)** sang **30. Kill switch và cờ tính năng (feature flag / 기능 플래그)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Staged rollout

Không bản phát hành (release / 릴리스) 100% người dùng (user / 사용자) ngay khi có thể rollout dần. Staged rollout cho phép quan sát crash/ANR/nghiệp vụ (business / 비즈니스) chỉ số (metric / 지표) ở cohort nhỏ.

Quy trình:

```text
internal/QA
→ small production percentage
→ observe technical + business metrics
→ expand gradually
→ halt/rollback if regression
```

Rollout percentage không cứu được nếu backend/lược đồ (schema / 스키마) thay đổi (change / 변경) không backward-compatible.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **30. Kill switch và cờ tính năng (feature flag / 기능 플래그)** nối từ **29. Staged rollout** sang **31. quay lui (rollback / 롤백)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Kill switch và cờ tính năng (feature flag / 기능 플래그)

Cờ tính năng (feature flag / 기능 플래그) cho phép disable một tính năng (feature / 기능) server-side khi issue. Nhưng flag phải có vòng đời (lifecycle / 생명주기): đơn vị sở hữu (owner / 오너), default, expiry/removal date.

Một app đầy flag vĩnh viễn tạo state-space khó kiểm thử (test / 테스트). Sau rollout ổn định, remove obsolete flag/đường đi mã (code path / 코드 경로).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **31. quay lui (rollback / 롤백)** nối từ **30. Kill switch và cờ tính năng (feature flag / 기능 플래그)** sang **32. Crash, ANR và symbolication**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. quay lui (rollback / 롤백)

Trước bản phát hành (release / 릴리스) hỏi: nếu app phiên bản (version / 버전) mới gây lỗi, quay lui (rollback / 롤백) bằng cách nào?

Nếu cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) irreversible hoặc backend API đã drop tính tương thích (compatibility / 호환성), quay lui (rollback / 롤백) nhị phân (binary / 이진) có thể không đủ. Vì vậy bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링) cần backward tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **32. Crash, ANR và symbolication** nối từ **31. quay lui (rollback / 롤백)** sang **33. khả năng quan sát (observability / 관측 가능성) cổng chất lượng (quality gate / 품질 게이트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Crash, ANR và symbolication

Minified bản phát hành (release / 릴리스) dấu vết ngăn xếp (stack trace / 스택 트레이스) cần ánh xạ (mapping / 매핑) tệp (file / 파일) để deobfuscate. bản địa (native / 네이티브) crash cần symbol tương ứng. sản phẩm tạo ra (artifact / 산출물)/ánh xạ (mapping / 매핑) phải gắn với versionCode/bản dựng (build / 빌드) ID và lưu đủ lâu để điều tra crash cũ.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **33. khả năng quan sát (observability / 관측 가능성) cổng chất lượng (quality gate / 품질 게이트)** nối từ **32. Crash, ANR và symbolication** sang **34. Privacy trong telemetry**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. khả năng quan sát (observability / 관측 가능성) cổng chất lượng (quality gate / 품질 게이트)

Trước rollout, dashboard cần biết ít nhất:

- crash-free users/sessions;
- ANR tỷ lệ (rate / 비율);
- startup/jank key chỉ số (metric / 지표);
- login/payment/sync success tỷ lệ (rate / 비율) nếu trọng yếu (critical / 중요);
- backend lỗi (error / 오류) increase;
- adoption theo phiên bản (version / 버전).

Một bản phát hành (release / 릴리스) “không có ticket” không có nghĩa healthy nếu telemetry không nhìn thấy thất bại (failure / 실패).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **34. Privacy trong telemetry** nối từ **33. khả năng quan sát (observability / 관측 가능성) cổng chất lượng (quality gate / 품질 게이트)** sang **35. bản phát hành (release / 릴리스) checklist theo bất biến (invariant / 불변식)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Privacy trong telemetry

Không log/đơn vị từ (token / 토큰)/người dùng (user / 사용자) content thừa. sự kiện (event / 이벤트) lược đồ (schema / 스키마) phải biết trường dữ liệu (field / 필드) nào PII. Sampling/redaction/retention cần chính sách (policy / 정책).

Gỡ lỗi (debug / 디버그) log có thể verbose hơn môi trường vận hành (production / 운영 환경) nhưng vẫn không nên in password/đơn vị từ (token / 토큰).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **35. bản phát hành (release / 릴리스) checklist theo bất biến (invariant / 불변식)** nối từ **34. Privacy trong telemetry** sang **36. cấp cao (senior / 시니어) notes**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. bản phát hành (release / 릴리스) checklist theo bất biến (invariant / 불변식)

Thay vì checklist “bấm 50 ô” không hiểu lý do, nhóm theo bất biến (invariant / 불변식):

**tính đúng đắn (correctness / 정확성)**: kiểm thử (test / 테스트)/lint pass, di chuyển (migration / 마이그레이션) tested, minified bản dựng (build / 빌드) smoke-tested.

**bảo mật (security / 보안)**: prod endpoint, signing, no gỡ lỗi (debug / 디버그) backdoor, phụ thuộc (dependency / 의존성) rủi ro (risk / 위험) reviewed.

**hiệu năng (performance / 성능)**: trọng yếu (critical / 중요) macrobenchmark không regression vượt ngân sách (budget / 예산).

**Operability**: telemetry, ánh xạ (mapping / 매핑)/symbol, cờ tính năng (feature flag / 기능 플래그)/quay lui (rollback / 롤백) plan sẵn.

**tính tương thích (compatibility / 호환성)**: backend/lược đồ (schema / 스키마)/mục tiêu (target / 대상) SDK hành vi (behavior / 동작) được kiểm tra.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 05 — Testing, hiệu năng (performance / 성능), CI/CD và bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링)**, **36. cấp cao (senior / 시니어) notes** nối từ **35. bản phát hành (release / 릴리스) checklist theo bất biến (invariant / 불변식)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 36. cấp cao (senior / 시니어) notes

Testing không phải mục tiêu coverage percentage; nó là confidence hệ thống (system / 시스템). hiệu năng (performance / 성능) không phải tối ưu microbenchmark; nó là ngân sách (budget / 예산) + dấu vết (trace / 추적) + regression detection. CI/CD không phải YAML dài; nó là khả năng tạo sản phẩm tạo ra (artifact / 산출물) lặp lại, kiểm chứng và phát hành có kiểm soát.

Một nhóm (team / 팀) trưởng thành có thể trả lời: “PR này thay bất biến (invariant / 불변식) nào?”, “kiểm thử (test / 테스트) nào bảo vệ nó?”, “chỉ số (metric / 지표) nào phát hiện regression?”, “bản phát hành (release / 릴리스) bao nhiêu phần trăm trước?”, “nếu thất bại (fail / 실패) thì quay lui (rollback / 롤백)/disable thế nào?”. Khi câu trả lời rõ, Android kỹ thuật (engineering / 엔지니어링) đã vượt xa mức chỉ biết API.

> **Bàn giao:** Sau **36. cấp cao (senior / 시니어) notes**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

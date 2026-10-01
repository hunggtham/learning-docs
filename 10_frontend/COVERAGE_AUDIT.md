# Frontend Coverage Kiểm tra (audit / 감사)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Frontend Coverage Kiểm tra (audit / 감사)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Cách đọc trạng thái** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **1. Kiểm tra (audit / 감사) theo mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình chung và giới hạn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Tệp (file / 파일) này kiểm tra `10_frontend/` theo mô hình tư duy (mental model / 사고 모델) cấp lĩnh vực (domain / 도메인), không chỉ theo
số lượng tệp (file / 파일). Mục tiêu là phát hiện nơi người học có thể biết cú pháp (syntax / 문법) nhưng
chưa hiểu ranh giới (boundary / 경계), quyền sở hữu (ownership / 소유권), thứ tự (ordering / 순서), thất bại (failure / 실패), bằng chứng (evidence / 증거) hoặc triển khai (deployment / 배포)
sản phẩm tạo ra (artifact / 산출물).

`CATALOG.md` vẫn dùng
[`javascript/javascript_beginner_rebuilt.md`](./javascript/javascript_beginner_rebuilt.md)
làm điểm vào (entrypoint / 진입점). [`README.md`](./README.md) là map cấp lĩnh vực (domain / 도메인) và giải thích vì
sao điểm vào (entrypoint / 진입점) là JavaScript nhánh học (track / 트랙) trong khi học tập (learning / 학습) mô hình (model / 모델) bắt đầu từ trình duyệt (browser / 브라우저)
yêu cầu (request / 요청) và Nền tảng Web (web platform / 웹 플랫폼).

## Cách đọc trạng thái

- **Covered** — có đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) và có đủ explanation để đi từ cơ chế (mechanism / 메커니즘) đến
  môi trường vận hành (production / 운영 환경) implication.
- **Deep** — đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) đã có, đồng thời có supplement/master/khung phần mềm (framework / 프레임워크)
  material hoặc trường hợp (case / 사례)/lab để lập luận (reasoning / 추론) ở ranh giới (boundary / 경계) khó.
- **Phân tán (distributed / 분산)** — coverage nằm ở nhiều nhánh học (track / 트랙); người học phải theo cross-link,
  nhưng không phải thiếu nội dung.
- **Partial** — đã có nội dung đáng kể nhưng map cấp lĩnh vực (domain / 도메인) hoặc một bất biến (invariant / 불변식) /
  bằng chứng (evidence / 증거) đường dẫn (path / 경로) còn mỏng; đây là candidate cho vòng cập nhật (update / 업데이트) sau.
- **Intentional ranh giới (boundary / 경계)** — không duplicate ở Frontend vì lĩnh vực (domain / 도메인) khác là đơn vị sở hữu (owner / 오너);
  Frontend chỉ giữ đặc tả hợp đồng (contract / 계약) cần để tích hợp.

> **Chuyển mạch:** Trong **Frontend Coverage Kiểm tra (audit / 감사)**, **1. Kiểm tra (audit / 감사) theo mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Cách đọc trạng thái** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **2. Kiểm tra (audit / 감사) theo nhánh học (track / 트랙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. Kiểm tra (audit / 감사) theo mô hình tư duy (mental model / 사고 모델)

| Stage | Đơn vị sở hữu (owner / 오너) chính | Coverage | Bằng chứng / tiêu chí kiểm chứng |
|---|---|---|---|
| URL / yêu cầu (request / 요청) | JavaScript + HTML Master; cross-link Khoa học máy tính (computer science / 컴퓨터 과학)/Backend | Deep | Có phân biệt URL, điều hướng (navigation / 내비게이션), yêu cầu tài nguyên (resource request / 리소스 요청), `fetch`, bộ nhớ đệm (cache / 캐시), CORS và Đặc tả API (API contract / API 계약) không? Lý thuyết (theory / 이론) được nối end-to-end bằng `90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md`. |
| Trình duyệt (browser / 브라우저) / mạng (network / 네트워크) | JavaScript Cấp cao (senior / 시니어)/Master; HTML Master; WebSquare 15/21 | Deep | Có nhìn trình duyệt (browser / 브라우저) là host môi trường (environment / 환경) thay vì chỉ ECMAScript không? Có dấu vết (trace / 추적) hết thời gian chờ (timeout / 타임아웃), cancellation, thử lại (retry / 재시도), bộ nhớ đệm (cache / 캐시), cross-origin và stale phản hồi (response / 응답) theo timeline không? |
| HTML parse | HTML Beginner + Master | Deep | Có phân biệt nguồn (source / 소스) markup, parser repair, DOM cây (tree / 트리), optional end tag, raw văn bản (text / 텍스트)/RCDATA và SSR parser-stable markup không? |
| DOM | HTML + JavaScript Beginner/Intermediate | Deep | Có phân biệt DOM nút (node / 노드), thành phần (component / 컴포넌트) đối tượng (object / 객체), attribute/live thuộc tính (property / 속성), logical định danh (identity / 식별자) và vật lý (physical / 물리적) DOM biểu diễn (representation / 표현) không? |
| CSS parse / CSSOM | CSS Beginner + Master | Deep | Có giải thích declaration → cascade → specified/computed/used/actual giá trị (value / 값) và formatting cây (tree / 트리) khác DOM cây (tree / 트리) không? |
| Style / cascade | CSS Beginner + Master; SCSS/Tailwind authoring | Deep | Có lập luận (reasoning / 추론) về specificity, layers, inheritance, phạm vi (scope / 범위) proximity, `!important`, đơn vị từ (token / 토큰) và nguồn (source / 소스) thứ tự (order / 순서) thay vì tăng selector bừa không? |
| Bố cục (layout / 레이아웃) | CSS Beginner + Master + Rendering Đo lường (measurement / 측정) Lab | Deep | Có hiểu luồng bố cục thông thường (normal flow / 일반 흐름), BFC/IFC, flex/grid, định cỡ nội tại (intrinsic sizing / 내재 크기 결정), fragmentation, bộ chứa (container / 컨테이너) truy vấn (query / 쿼리), vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용), forced synchronous bố cục (layout / 레이아웃) và read/ghi (write / 쓰기) thứ tự (ordering / 순서) không? |
| Paint | CSS Master; JavaScript Cấp cao (senior / 시니어); Rendering Đo lường (measurement / 측정) Lab | Deep | Có phân biệt style/bố cục (layout / 레이아웃)/paint/composite và chứng minh repaint bằng dấu vết (trace / 추적)/profile thay vì suy từ thuộc tính (property / 속성) folklore không? Có xem invalidated area, frequency và visual độ phức tạp (complexity / 복잡도) không? |
| Composite | CSS Master; JavaScript Cấp cao (senior / 시니어); Rendering Đo lường (measurement / 측정) Lab | Deep | Có hiểu compositing/tầng (layer / 계층) là tối ưu hóa (optimization / 최적화) có bộ nhớ (memory / 메모리)/tài nguyên (resource / 자원) chi phí (cost / 비용), không phải `transform`/GPU = miễn phí? Có baseline → dấu vết (trace / 추적) → thay đổi (change / 변경) → re-measure không? |
| Tương tác (interaction / 상호작용) | HTML + CSS + JavaScript Beginner/Intermediate; React/WebSquare | Deep | Có phân biệt ngữ nghĩa (semantic / 의미적) HTML, keyboard/focus/pointer/đầu vào (input / 입력), bubbling/capturing/delegation, form trạng thái (state / 상태) và khung phần mềm (framework / 프레임워크) sự kiện (event / 이벤트) lớp trừu tượng (abstraction / 추상화) không? |
| JavaScript / vòng lặp sự kiện (event loop / 이벤트 루프) | JavaScript Beginner → Intermediate → Cấp cao (senior / 시니어) → Master | Deep | Có dấu vết (trace / 추적) ngăn xếp (stack / 스택), tác vụ (task / 작업), microtask, kết xuất (render / 렌더링) opportunity, timer, `requestAnimationFrame`, worker, stream, cancellation và reentrancy theo timeline không? |
| Trạng thái (state / 상태) / dữ liệu (data / 데이터) | JavaScript Intermediate/Cấp cao (senior / 시니어); React; WebSquare | Deep | Có xác định nguồn chuẩn (source of truth / 정본), máy trạng thái (state machine / 상태 머신), derived trạng thái (state / 상태), DTO ranh giới (boundary / 경계), stale kết quả (result / 결과), optimistic cập nhật (update / 업데이트), định danh (identity / 식별자) và quyền sở hữu (ownership / 소유권) của async thao tác (operation / 연산) không? |
| Khả năng tiếp cận (accessibility / 접근성) | HTML Master; CSS; React; WebSquare 09 | Deep | Có xem cây khả năng tiếp cận (accessibility tree / 접근성 트리)/ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) là tính đúng đắn (correctness / 정확성), không phải polish? Có kiểm tra accessible name, focus, keyboard, live region, `aria-*`, form lỗi (error / 오류) và screen-reader hành vi (behavior / 동작) không? |
| Hiệu năng (performance / 성능) | JavaScript Cấp cao (senior / 시니어); CSS Master; React; WebSquare 24; `90_case_studies/` | Deep | Có đo mạng (network / 네트워크), main-thread, bố cục (layout / 레이아웃)/paint, bundle, bộ nhớ (memory / 메모리), large DOM, formatter/kết xuất (render / 렌더링) amplification, RUM/profile và môi trường vận hành (production / 운영 환경) ngân sách (budget / 예산) thay vì tối ưu theo cảm giác không? |
| Bảo mật (security / 보안) | HTML Master; JavaScript Cấp cao (senior / 시니어)/Master; React/WebSquare; Backend ranh giới (boundary / 경계) | Deep | Có dấu vết (trace / 추적) untrusted đầu vào (input / 입력) → parser/DOM/URL/HTML sink, XSS, CSP/Trusted Types, CSRF, đơn vị từ (token / 토큰), `postMessage`, cầu nối (bridge / 브리지), supply chuỗi (chain / 사슬) và máy chủ (server / 서버) authorization không? |
| Triển khai (deployment / 배포) | JavaScript Cấp cao (senior / 시니어)/Master; WebSquare 12/22; DevOps ranh giới (boundary / 경계); Yêu cầu (request / 요청)→Điểm ảnh (pixel / 픽셀) trường hợp (case / 사례) | Deep | Có phân biệt nguồn (source / 소스), hiện vật bản dựng (build artifact / 빌드 산출물), bundle/bản đồ mã nguồn (source map / 소스 맵), cấu hình (config / 설정), bộ nhớ đệm (cache / 캐시), triển khai (deployment / 배포) định danh (identity / 식별자), quay lui (rollback / 롤백) và trình duyệt (browser / 브라우저) đang chạy sản phẩm tạo ra (artifact / 산출물) nào không? Trường hợp (case / 사례) end-to-end buộc nối lần ghi nhận (commit / 커밋)/bản dựng (build / 빌드)/băm (hash / 해시)/cấu hình (config / 설정) với tài nguyên (resource / 자원) trình duyệt (browser / 브라우저) thực sự nhận. |

### Kết luận chuỗi xử lý (pipeline / 파이프라인)

Chuỗi xử lý (pipeline / 파이프라인) hiện có coverage mạnh từ yêu cầu (request / 요청) tới triển khai (deployment / 배포). Gap trước đây ở
paint/composite đã được đóng bằng một bằng chứng (evidence / 증거) đường dẫn (path / 경로) riêng: lý thuyết (theory / 이론) vẫn thuộc CSS
Master và JavaScript Cấp cao (senior / 시니어), còn
[`90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md`](./90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md)
buộc người học tạo baseline, bản ghi (record / 레코드) dấu vết (trace / 추적), phân loại scripting/style/bố cục (layout / 레이아웃)/
paint/composite, xác định vô hiệu hóa (invalidation / 무효화) rồi re-measure sau một thay đổi duy nhất.

Tương tự, [`Request → Pixel → Interaction Trace`](./90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md)
đã nối điều hướng (navigation / 내비게이션)/tài nguyên (resource / 자원) discovery, parser, DOM/CSSOM, vòng lặp sự kiện (event loop / 이벤트 루프), trạng thái (state / 상태),
khả năng tiếp cận (accessibility / 접근성), bảo mật (security / 보안) và nguồn (source / 소스)→bản dựng (build / 빌드)→bộ nhớ đệm (cache / 캐시)→deployed sản phẩm tạo ra (artifact / 산출물) thành một trường hợp (case / 사례)
duy nhất. Vì vậy hai P1 gap này không còn cần thêm lý thuyết (theory / 이론) tệp (file / 파일); vòng sau chỉ nên
mở rộng khi có năng lực (capability / 역량)/bằng chứng (evidence / 증거) mới.

> **Chuyển mạch:** Ở chặng này của **Frontend Coverage Kiểm tra (audit / 감사)**, **2. Kiểm tra (audit / 감사) theo nhánh học (track / 트랙)** gom các mảnh từ **1. Kiểm tra (audit / 감사) theo mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3. Cross-cutting bất biến (invariant / 불변식) kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Kiểm tra (audit / 감사) theo nhánh học (track / 트랙)

| Nhánh học (track / 트랙) | Trục học (learning spine / 학습 축) | Đã cover tốt | Ranh giới (boundary / 경계) cần giữ |
|---|---|---|---|
| HTML | Beginner → Master Hiện thực (implementation / 구현) | Ngữ nghĩa (semantics / 의미론), parser, forms, DOM quan hệ (relation / 관계), resources, a11y, bảo mật (security / 보안), legacy và SSR | Không biến HTML thành XML; không dùng ARIA thay bản địa (native / 네이티브) ngữ nghĩa (semantics / 의미론) khi bản địa (native / 네이티브) element đã đủ. |
| CSS | Beginner → Cấp cao (senior / 시니어) → Master Supplement | Cascade, selectors, box/formatting, sizing, responsive, animation, rendering và hiện đại (modern / 현대적) CSS | CSS authoring không đồng nghĩa rendering; SCSS/Tailwind không thay CSS mô hình tư duy (mental model / 사고 모델). |
| SCSS | Beginner → Cấp cao (senior / 시니어) → Master Supplement | Compile-time ngôn ngữ (language / 언어), mô-đun (module / 모듈)/cấu hình (configuration / 구성), mixin/hàm (function / 함수), selector algebra, colors và Dart Sass evolution | Đầu ra (output / 출력) chuẩn gốc (canonical / 정본) vẫn là CSS; thời gian chạy (runtime / 런타임) đơn vị từ (token / 토큰) nên tách khỏi compile-time cấu hình (config / 설정). |
| Tailwind | Beginner → Cấp cao (senior / 시니어) → Master Supplement | Utility-first, v4 bản dựng (build / 빌드) mô hình (model / 모델), tokens, variants, responsive, thành phần (component / 컴포넌트) ranh giới (boundary / 경계) và môi trường vận hành (production / 운영 환경) quản trị (governance / 거버넌스) | Utility lớp (class / 클래스) không loại bỏ cascade, khả năng tiếp cận (accessibility / 접근성), thiết kế (design / 설계) ngữ nghĩa (semantics / 의미론) hoặc hiệu năng (performance / 성능) rà soát (review / 검토). |
| JavaScript | Beginner → Intermediate → Cấp cao (senior / 시니어) → Master Supplement | Ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임), trình duyệt (browser / 브라우저) host, DOM/sự kiện (event / 이벤트), async, trạng thái (state / 상태), bộ nhớ (memory / 메모리), tính đồng thời (concurrency / 동시성), hiệu năng (performance / 성능), bảo mật (security / 보안), testing và kiến trúc (architecture / 아키텍처) | Đây là danh mục (catalog / 카탈로그) điểm vào (entrypoint / 진입점); không để React/WebSquare thay thế JavaScript ngữ nghĩa (semantics / 의미론). |
| TypeScript | Foundations → Hệ kiểu (type system / 타입 시스템) → Tooling/Modules → Cấp cao (senior / 시니어) Môi trường vận hành (production / 운영 환경) → Phiên bản (version / 버전)/Di chuyển (migration / 마이그레이션) | Static/thời gian chạy (runtime / 런타임) ranh giới (boundary / 경계), structural typing, generics, trình biên dịch (compiler / 컴파일러)/tooling, declarations, kiểm tra hợp lệ (validation / 검증) và di chuyển (migration / 마이그레이션) | Kiểu (type / 타입) annotation không phải thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) và không tạo authorization. |
| React | Beginner → Intermediate → Advanced/Cấp cao (senior / 시니어) → Master + Legacy Tham chiếu (reference / 참조) | Kết xuất (render / 렌더링)/reconciliation, định danh (identity / 식별자), trạng thái (state / 상태)/effects, tính đồng thời (concurrency / 동시성), SSR/hydration/RSC, trình biên dịch (compiler / 컴파일러), hiệu năng (performance / 성능), bảo mật (security / 보안) và di chuyển (migration / 마이그레이션) | React là bên tiêu thụ (consumer / 소비자) của Nền tảng Web (web platform / 웹 플랫폼); gỡ lỗi (debug / 디버그) DOM/CSS/sự kiện (event / 이벤트)/mạng (network / 네트워크) trước khi gán lỗi cho React. |
| WebSquare | 01 → 24 + glossary/coverage | Thời gian chạy (runtime / 런타임)/page/phạm vi (scope / 범위), DataCollection/Submission, Grid, reusable kiến trúc (architecture / 아키텍처), vòng đời (lifecycle / 생명주기), kiểm thử (test / 테스트), bản dựng (build / 빌드), auth, tích hợp (integration / 통합), khả năng quan sát (observability / 관측 가능성), workflow và profiling | Khung phần mềm (framework / 프레임워크) đặc tả hợp đồng (contract / 계약) có thể bản dựng (build / 빌드)/version-dependent; XML nguồn (source / 소스), thời gian chạy (runtime / 런타임) engine và W-Pack sản phẩm tạo ra (artifact / 산출물) phải tách. |
| XML | Beginner → Intermediate → Cấp cao (senior / 시니어) → Master Supplement | Cú pháp (syntax / 문법)/cây (tree / 트리), không gian tên (namespace / 네임스페이스), kiểm tra hợp lệ (validation / 검증), transformation, bảo mật (security / 보안) và tích hợp (integration / 통합) | XML là dữ liệu (data / 데이터)/cấu hình (config / 설정)/document ranh giới (boundary / 경계); không dùng XML parser các giả định (assumptions / 가정들) để giải thích HTML parser. |
| Trường hợp (case / 사례)/Lab | Yêu cầu (request / 요청)→Điểm ảnh (pixel / 픽셀) dấu vết (trace / 추적) → Rendering Đo lường (measurement / 측정) Lab | Cross-owner nhân quả (causal / 인과적) dấu vết (trace / 추적), bằng chứng vận hành (production evidence / 운영 증거), bố cục (layout / 레이아웃)/paint/composite profiling, sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자) | Không biến trường hợp (case / 사례) thành đơn vị sở hữu (owner / 오너) lý thuyết (theory / 이론) mới; framework-specific profiler chỉ bổ sung trình duyệt (browser / 브라우저)/nền tảng (platform / 플랫폼) bằng chứng (evidence / 증거). |

> **Chuyển mạch:** Track audit xác định từng nhánh đã có owner và evidence nào; cross-cutting invariants nối các nhánh qua accessibility, security, performance và state. Framework placement tiếp theo kiểm tra boundary khi chọn implementation.

## 3. Cross-cutting bất biến (invariant / 불변식) kiểm tra (audit / 감사)

Người học đạt coverage thực dụng khi có thể trả lời các câu hỏi sau mà không
đổi câu trả lời theo khung phần mềm (framework / 프레임워크):

### Định danh (identity / 식별자) và quyền sở hữu (ownership / 소유권)

- Tài nguyên (resource / 자원) nào được định danh bởi URL/bộ nhớ đệm (cache / 캐시) key/bản dựng (build / 빌드) ID; thực thể (entity / 엔터티) nào được định
  danh bởi nghiệp vụ (business / 비즈니스) key thay vì array chỉ mục (index / 인덱스) hoặc DOM position?
- Thành phần (component / 컴포넌트), DOM nút (node / 노드), screen instance, yêu cầu (request / 요청), session, workflow và sản phẩm tạo ra (artifact / 산출물)
  có thời gian tồn tại (lifetime / 수명) nào; ai tạo, ai sở hữu, ai dispose?
- Trạng thái (state / 상태) chuẩn gốc (canonical / 정본) nằm ở đâu; trạng thái (state / 상태) nào chỉ là derived view, bộ nhớ đệm (cache / 캐시), optimistic
  projection hoặc UI affordance?

### Thứ tự (ordering / 순서) và async

- Một sự kiện (event / 이벤트) đi qua capture → mục tiêu (target / 대상) → bubble hay khung phần mềm (framework / 프레임워크) dispatch nào?
- Promise continuation, timer, rendering opportunity, người dùng (user / 사용자) đầu vào (input / 입력) và mạng (network / 네트워크)
  phản hồi (response / 응답) có thể xen kẽ như thế nào?
- Khi phản hồi (response / 응답) cũ về sau intent mới, thao tác (operation / 연산) bị cancel, session đổi hoặc
  screen bị dispose, bất biến (invariant / 불변식) nào ngăn stale cập nhật (update / 업데이트)?

### Ngữ nghĩa (semantics / 의미론) và khả năng tiếp cận (accessibility / 접근성)

- Bản địa (native / 네이티브) HTML element đã biểu diễn đúng ngữ nghĩa (semantics / 의미론) chưa, hay mã (code / 코드) đang thêm ARIA
  để che markup sai?
- Focus, keyboard, accessible name, lỗi (error / 오류) announcement và reduced motion có
  được xem là công khai (public / 공개) hành vi (behavior / 동작) cần regression kiểm thử (test / 테스트) không?
- React/WebSquare lớp trừu tượng (abstraction / 추상화) có giữ được ngữ nghĩa (semantics / 의미론) khi kết xuất (render / 렌더링) conditionally,
  lazy, portal, popup, WFrame hoặc hydration không?

### Hiệu năng (performance / 성능) và bằng chứng (evidence / 증거)

- Độ trễ được chia thành DNS/connect/phản hồi (response / 응답)/parse/script/style/bố cục (layout / 레이아웃)/paint/
  tương tác (interaction / 상호작용) hay chỉ gọi chung là “frontend chậm”?
- Công việc (work / 작업) có bị khuếch đại theo rows × cells × listeners × renders không?
- Kết luận tối ưu dựa trên dấu vết (trace / 추적)/profile/chỉ số (metric / 지표) nào; có guard trong kiểm thử (test / 테스트) hoặc
  bản phát hành (release / 릴리스) gate không?
- Có phân biệt khung phần mềm (framework / 프레임워크) kết xuất (render / 렌더링)/reconciliation với trình duyệt (browser / 브라우저) rendering không?
- Có ghi scenario, môi trường (environment / 환경), bản dựng (build / 빌드) ID và run variance trước khi so before/after không?

### Bảo mật (security / 보안) và trust ranh giới (boundary / 경계)

- Dữ liệu đến từ URL, HTML, lưu trữ (storage / 저장소), postMessage, iframe, WebView cầu nối (bridge / 브리지),
  backend hay người dùng (user / 사용자) đầu vào (input / 입력) được coi là untrusted ở đâu?
- Kiểm tra hợp lệ (validation / 검증)/encoding/sanitization khác nhau thế nào; vì sao UI kiểm tra hợp lệ (validation / 검증)
  không thay máy chủ (server / 서버) authorization?
- CSP, cookie/đơn vị từ (token / 토큰), CSRF, CORS và phụ thuộc (dependency / 의존성)/bản dựng (build / 빌드) supply chuỗi (chain / 사슬) thuộc ranh giới (boundary / 경계)
  nào; bằng chứng (evidence / 증거) nào chứng minh chính sách (policy / 정책) đang active?

### Sản phẩm tạo ra (artifact / 산출물) và triển khai (deployment / 배포)

- Nguồn (source / 소스) markup/mã (code / 코드), generated CSS/JS, bundle, bản đồ mã nguồn (source map / 소스 맵), cấu hình (config / 설정), bộ nhớ đệm (cache / 캐시) và
  deployed tài nguyên (resource / 자원) liên hệ với nhau ra sao?
- Khi chỉ môi trường vận hành (production / 운영 환경) lỗi, có biết bản dựng (build / 빌드) ID, engine/trình duyệt (browser / 브라우저), cờ tính năng (feature flag / 기능 플래그),
  cấu hình (config / 설정) và bộ nhớ đệm (cache / 캐시) phiên bản (version / 버전) để tái tạo không?
- Quay lui (rollback / 롤백) có trả đúng sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정)/lược đồ (schema / 스키마) đặc tả hợp đồng (contract / 계약) hay chỉ quay lại Git
  branch?

> **Chuyển mạch:** Cross-cutting invariants cung cấp tiêu chí; framework placement audit áp dụng tiêu chí đó cho React, WebSquare và các framework khác mà không thay web-platform owner. Gaps tiếp theo được ưu tiên theo evidence còn thiếu.

## 4. Khung phần mềm (framework / 프레임워크) placement kiểm tra (audit / 감사)

Nhánh học khung phần mềm (framework track / 프레임워크 트랙) được xem là đạt khi mỗi chương trả lời được ba câu hỏi:

1. Trình duyệt (browser / 브라우저) thành phần nguyên thủy (primitive / 기본 요소) nào đang được dùng (DOM, CSS, event, history, fetch,
   storage, accessibility hoặc Web Worker)?
2. Khung phần mềm (framework / 프레임워크) thêm trạng thái (state / 상태)/vòng đời (lifecycle / 생명주기)/rendering lớp trừu tượng (abstraction / 추상화) nào, và lớp trừu tượng (abstraction / 추상화) đó
   sở hữu định danh (identity / 식별자), subscription, cleanup, lỗi (error / 오류) và scheduling ra sao?
3. Ứng dụng (application / 애플리케이션) phải kiểm chứng đặc tả hợp đồng (contract / 계약) nào bằng kiểm thử (test / 테스트), telemetry và sản phẩm tạo ra (artifact / 산출물)
   bằng chứng (evidence / 증거)?

React và WebSquare đều đã có chuẩn gốc (canonical / 정본) chỉ mục (index / 인덱스) riêng và đều cross-link về
JavaScript/XML/nền tảng (platform / 플랫폼). Không coi khung phần mềm (framework / 프레임워크) README là lĩnh vực (domain / 도메인) điểm vào (entrypoint / 진입점) là
điều kiện bắt buộc để tránh “framework-first drift”.

> **Chuyển mạch:** Placement audit làm lộ gap về ownership, test hoặc runtime evidence; backlog tiếp theo xếp chúng theo risk và dependency. Exit criteria chốt điều kiện để coverage chuyển thành bằng chứng hoàn chỉnh.

## 5. Gaps và ưu tiên vòng kiểm tra (audit / 감사) tiếp theo

Backlog hiện chuyển từ thiếu foundation sang **tích hợp (integration / 통합)/tính tương thích (compatibility / 호환성) và
regression bằng chứng (evidence / 증거)**. Không nên mở thêm khung phần mềm (framework / 프레임워크) chapter chỉ để tăng breadth.

| Priority | Cơ hội cải thiện | Trạng thái / hướng xử lý |
|---|---|---|
| P0 | Giữ một chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) map và một danh mục (catalog / 카탈로그) điểm vào (entrypoint / 진입점) duy nhất | Đã xử lý bằng `README.md`; giữ danh mục (catalog / 카탈로그) điểm vào (entrypoint / 진입점) là JavaScript Beginner. |
| P1 | Nối URL/điều hướng (navigation / 내비게이션)/yêu cầu tài nguyên (resource request / 리소스 요청) với DOM/CSS/kết xuất (render / 렌더링) dấu vết (trace / 추적) trong một trình duyệt (browser / 브라우저) trường hợp (case / 사례) | **Đã xử lý** bằng `90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md`. |
| P1 | Làm rõ paint/composite bằng chứng (evidence / 증거) và bố cục (layout / 레이아웃) vô hiệu hóa (invalidation / 무효화) bằng profile production-like | **Đã xử lý** bằng `90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md`; lý thuyết (theory / 이론) đơn vị sở hữu (owner / 오너) vẫn là CSS/JavaScript. |
| P1 | Chuẩn hóa nguồn (source / 소스) → bản dựng (build / 빌드) → bộ nhớ đệm (cache / 캐시) → deployed sản phẩm tạo ra (artifact / 산출물) vocabulary giữa React/WebSquare/vanilla | **Đã có chuẩn gốc (canonical / 정본) chuỗi (chain / 사슬)** trong Yêu cầu (request / 요청)→Điểm ảnh (pixel / 픽셀) trường hợp (case / 사례); có thể bổ sung glossary nhỏ chỉ khi track-specific vocabulary lệch nhau. |
| P2 | Tạo năng lực (capability / 역량) ma trận (matrix / 행렬) cho trình duyệt (browser / 브라우저), WebView, React và WebSquare | Chỉ thêm khi có di chuyển (migration / 마이그레이션)/tính tương thích (compatibility / 호환성) use trường hợp (case / 사례) thực; ma trận (matrix / 행렬) phải có phiên bản (version / 버전)/bằng chứng (evidence / 증거), không phải tính năng (feature / 기능) checklist chung. |
| P2 | Bổ sung end-to-end khả năng tiếp cận (accessibility / 접근성) regression example xuyên bản địa (native / 네이티브) HTML và khung phần mềm (framework / 프레임워크) | Đây là candidate độ sâu (depth / 깊이) tiếp theo nếu cần; đặt trường hợp (case / 사례) ở tầng (layer / 계층) tích hợp (integration / 통합) và cross-link đơn vị sở hữu (owner / 오너), không duplicate a11y lý thuyết (theory / 이론). |
| P2 | Tạo one-screen môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) drill | Candidate cao: sản phẩm tạo ra (artifact / 산출물) mismatch + stale yêu cầu (request / 요청) + hiệu năng (performance / 성능) + khả năng tiếp cận (accessibility / 접근성)/bảo mật (security / 보안) checks trong một sự cố (incident / 인시던트), nếu muốn luyện vận hành thay vì thêm lý thuyết (theory / 이론). |

> **Chuyển mạch:** Exit criteria gom owner, invariant, source, test và link checks thành điều kiện review. Coverage chỉ được coi là hoàn tất khi từng điều kiện có evidence truy nguyên.

## 6. Exit criteria cho Frontend lĩnh vực (domain / 도메인)

Coverage cấp lĩnh vực (domain / 도메인) được xem là đủ mạnh khi người học có thể:

1. vẽ yêu cầu (request / 요청) → parser → cây (tree / 트리) → style → bố cục (layout / 레이아웃) → paint → composite → sự kiện (event / 이벤트) →
   trạng thái (state / 상태) → triển khai (deployment / 배포) timeline cho một màn hình thật;
2. chỉ ra đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) của một concept và không giải thích trình duyệt (browser / 브라우저) hành vi (behavior / 동작)
   bằng khung phần mềm (framework / 프레임워크) folklore;
3. đặt tên định danh (identity / 식별자), đơn vị sở hữu (owner / 오너), thời gian tồn tại (lifetime / 수명), thứ tự (ordering / 순서) và bất biến (invariant / 불변식) của async trạng thái (state / 상태);
4. kiểm tra khả năng tiếp cận (accessibility / 접근성) như ngữ nghĩa (semantics / 의미론) và công khai (public / 공개) hành vi (behavior / 동작);
5. đo hiệu năng (performance / 성능) bằng bằng chứng (evidence / 증거), phân biệt máy khách (client / 클라이언트) công việc (work / 작업) với mạng (network / 네트워크)/máy chủ (server / 서버) công việc (work / 작업);
6. dấu vết (trace / 추적) untrusted dữ liệu (data / 데이터) qua HTML/DOM/URL/message/cầu nối (bridge / 브리지)/backend ranh giới (boundary / 경계);
7. nối nguồn (source / 소스) lần ghi nhận (commit / 커밋) với generated sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), bộ nhớ đệm (cache / 캐시), deployed tài nguyên (resource / 자원) và
   quay lui (rollback / 롤백) plan;
8. đọc mã (code / 코드) legacy, chọn di chuyển (migration / 마이그레이션) ranh giới (boundary / 경계) và giữ nguyên bất biến (invariant / 불변식) thay vì
   rewrite theo trend;
9. tạo hiệu năng (performance / 성능) report có scenario, baseline, dấu vết (trace / 추적) observation, hypothesis,
   one-change experiment, variance và regression check.

Hiện lĩnh vực (domain / 도메인) đã có đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) cho toàn bộ các exit criteria trên. Nội dung
mới chỉ nên được thêm khi tạo **new năng lực (capability / 역량), di chuyển (migration / 마이그레이션) bằng chứng (evidence / 증거), môi trường vận hành (production / 운영 환경)
sự cố (incident / 인시던트) drill hoặc regression sản phẩm tạo ra (artifact / 산출물)**, không nên mở rộng chỉ vì xuất hiện
một khung phần mềm (framework / 프레임워크) hay CSS API mới.

> **Bàn giao:** Sau **6. Exit criteria cho Frontend lĩnh vực (domain / 도메인)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.

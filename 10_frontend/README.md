# Thư viện kiến thức phát triển giao diện web (frontend development knowledge library / 프런트엔드 개발 지식 라이브러리)

> **Mạch đọc:** Đọc **Thư viện kiến thức phát triển giao diện web (frontend development knowledge library / 프런트엔드 개발 지식 라이브러리)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **mô hình tư duy (mental model / 사고 모델) cấp lĩnh vực (domain / 도메인)** sang **Cách đọc chuẩn gốc (canonical / 정본)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

`10_frontend/` là không gian tên (namespace / 네임스페이스) chuẩn gốc (canonical / 정본) cho Phát triển giao diện web (frontend development / 프런트엔드 개발). Đây không phải
là một danh sách khung phần mềm (framework / 프레임워크) rời rạc; nó là một lộ trình giải thích cách một yêu
cầu đi từ mạng (network / 네트워크) đến điểm ảnh (pixel / 픽셀), từ điểm ảnh (pixel / 픽셀) đến tương tác (interaction / 상호작용), rồi từ tương tác (interaction / 상호작용) đến
trạng thái (state / 상태), khả năng tiếp cận (accessibility / 접근성), hiệu năng (performance / 성능), bảo mật (security / 보안) và triển khai (deployment / 배포).

`CATALOG.md` dùng
[`javascript_beginner_rebuilt.md`](./javascript/javascript_beginner_rebuilt.md)
làm **điểm vào (entrypoint / 진입점) chuẩn gốc (canonical / 정본)** của Frontend. tệp (file / 파일) này là bản đồ cấp lĩnh vực (domain / 도메인): nó
giải thích thứ tự học và quan hệ giữa các nhánh học (track / 트랙), nhưng không thay thế trục học (learning spine / 학습 축) JavaScript hay các tệp chuẩn gốc (canonical file / 정본 파일) của từng nhánh học (track / 트랙).

## Mô hình tư duy (mental model / 사고 모델) cấp lĩnh vực (domain / 도메인)

Frontend nên được đọc như một hệ thống có nhiều ranh giới (boundary / 경계) nối tiếp và có thể
quay lại vô hiệu hóa (invalidation / 무효화) lẫn nhau:

```text
URL / request
→ browser / network
→ HTML parse
→ DOM
→ CSS parse
→ CSSOM
→ style / cascade
→ layout
→ paint
→ composite
→ interaction
→ JavaScript / event loop
→ state / data
→ accessibility
→ performance
→ security
→ deployment
```

Đây là một mô hình tư duy (mental model / 사고 모델), không phải một chuỗi xử lý (pipeline / 파이프라인)
chỉ chạy đúng một lần. điều hướng (navigation / 내비게이션) mới, phản hồi (response / 응답) mới, biểu định kiểu (stylesheet / 스타일시트) thay đổi,
font tải (load / 로드), resize, trạng thái (state / 상태) cập nhật (update / 업데이트), người dùng (user / 사용자) đầu vào (input / 입력) hoặc session chuyển tiếp (transition / 전이) đều có thể
làm một phần chuỗi xử lý (pipeline / 파이프라인) chạy lại. Vì vậy khi gỡ lỗi (debug / 디버그), câu hỏi hữu ích không chỉ là
“thành phần (component / 컴포넌트) nào lỗi?” mà là: yêu cầu (request / 요청) nào tạo ra tài nguyên (resource / 자원) này, cây (tree / 트리) nào đang được
kết xuất (render / 렌더링), trạng thái (state / 상태) nào là nguồn chuẩn (source of truth / 정본), công việc (work / 작업) được schedule ở đâu, và sản phẩm tạo ra (artifact / 산출물) nào
đang thật sự phục vụ trình duyệt (browser / 브라우저)?

Mối quan hệ giữa các lớp được giữ cố ý như sau:

```text
HTML / CSS / JavaScript
            ↓
      Web Platform
            ↓
   React / WebSquare / ...
```

HTML, CSS và JavaScript không phải “tầng cũ (legacy layer / 레거시 계층)” nằm dưới khung phần mềm (framework / 프레임워크). Chúng là
thành phần nguyên thủy (primitive / 기본 요소) và đặc tả hợp đồng (contract / 계약) của Nền tảng Web (web platform / 웹 플랫폼): parser, DOM, CSS cascade/bố cục (layout / 레이아웃),
sự kiện (event / 이벤트)/đầu vào (input / 입력), lưu trữ trình duyệt (browser storage / 브라우저 저장소), networking, cây khả năng tiếp cận (accessibility tree / 접근성 트리) và ranh giới bảo mật (security boundary / 보안 경계). React, WebSquare và các khung phần mềm (framework / 프레임워크) khác tổ chức các thành phần nguyên thủy (primitive / 기본 요소) đó thành
mô hình ứng dụng (application model / 애플리케이션 모델) riêng; chúng không xóa được ngữ nghĩa (semantics / 의미론) của trình duyệt (browser / 브라우저).


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델) cấp lĩnh vực (domain / 도메인)**, ta sang **Cách đọc chuẩn gốc (canonical / 정본)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách đọc chuẩn gốc (canonical / 정본)

Khi cần một điểm bắt đầu duy nhất, mở
[`JavaScript Beginner`](./javascript/javascript_beginner_rebuilt.md). tệp (file / 파일) này
được dùng làm danh mục (catalog / 카탈로그) điểm vào (entrypoint / 진입점) vì nó nối cú pháp (syntax / 문법) với mô hình thực thi (execution model / 실행 모델), DOM,
sự kiện (event / 이벤트), Promise, `fetch`, HTTP và ranh giới mô-đun (module boundary / 모듈 경계); từ đó người học có thể đi
sang các nhánh học (track / 트랙) nền tảng (platform / 플랫폼) mà không bắt đầu bằng một lớp trừu tượng (abstraction / 추상화) khung phần mềm (framework / 프레임워크).

Đường học đầy đủ nên đi theo các lớp sau:

1. **Nền tảng trình duyệt (browser / 브라우저):** đọc HTML và CSS để hiểu document, ngữ nghĩa (semantics / 의미론), DOM,
   cascade, bố cục (layout / 레이아웃) và rendering. XML được học như một cú pháp (syntax / 문법)/dữ liệu (data / 데이터)/cấu hình (config / 설정)
   ranh giới (boundary / 경계), không đồng nhất với HTML parser.
2. **Ngôn ngữ và thời gian chạy (runtime / 런타임):** đi từ JavaScript Beginner → Intermediate → cấp cao (senior / 시니어),
   sau đó dùng Master Supplement để ghép ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론), ranh giới trình duyệt (browser boundary / 브라우저 경계),
   bảo mật (security / 보안), hiệu năng (performance / 성능) và tính tương thích (compatibility / 호환성) thành một hệ thống.
3. **kiểu (type / 타입) và styling tooling:** học TypeScript sau khi đã phân biệt static
   kiểu (type / 타입) với hành vi thời gian chạy (runtime behavior / 런타임 동작); học SCSS/Tailwind sau CSS để hiểu chúng là
   authoring/bản dựng (build / 빌드) choices, không phải renderer mới.
4. **ứng dụng (application / 애플리케이션) frameworks:** chọn React hoặc WebSquare sau khi đã nắm
   nền tảng (platform / 플랫폼) thành phần nguyên thủy (primitive / 기본 요소). nhánh học khung phần mềm (framework track / 프레임워크 트랙) phải được đọc như cách hiện thực trạng thái (state / 상태),
   rendering, composition, tích hợp (integration / 통합) và vòng đời (lifecycle / 생명주기) trên cùng trình duyệt (browser / 브라우저).
5. **môi trường vận hành (production / 운영 환경):** dùng coverage kiểm tra (audit / 감사) để kiểm tra định danh (identity / 식별자), quyền sở hữu trạng thái (state ownership / 상태 소유권),
   async thứ tự (ordering / 순서), khả năng tiếp cận (accessibility / 접근성), bằng chứng hiệu năng (performance evidence / 성능 증거), ranh giới bảo mật (security boundary / 보안 경계),
   hiện vật bản dựng (build artifact / 빌드 산출물) và triển khai (deployment / 배포) provenance.

Không bắt buộc mọi người phải đọc mọi tệp (file / 파일) theo một đường thẳng. Tuy vậy,
không nên bỏ qua HTML/CSS/trình duyệt (browser / 브라우저) chỉ vì dự án dùng React hoặc WebSquare; làm
vậy sẽ biến lỗi parser, cascade, vòng lặp sự kiện (event loop / 이벤트 루프), hydration, focus, bộ nhớ đệm (cache / 캐시) hoặc
bảo mật (security / 보안) thành “phép màu của khung phần mềm (framework magic / 프레임워크 마법)”.


> **Chuyển mạch:** Từ **Cách đọc chuẩn gốc (canonical / 정본)**, ta sang **Bản đồ thư mục và đơn vị sở hữu (owner / 오너)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bản đồ thư mục và đơn vị sở hữu (owner / 오너)

| nhánh học (track / 트랙) | tệp chuẩn gốc (canonical file / 정본 파일) bắt đầu | Vai trò trong lĩnh vực (domain / 도메인) |
|---|---|---|
| [`html/`](./html/) | [`html_01_beginner_to_senior_detailed.md`](./html/html_01_beginner_to_senior_detailed.md) | Document cấu trúc (structure / 구조), ngữ nghĩa (semantics / 의미론), parser/cây (tree / 트리) construction, forms, gợi ý tài nguyên (resource hints / 리소스 힌트), khả năng tiếp cận (accessibility / 접근성), bảo mật (security / 보안) và legacy markup. |
| [`css/`](./css/) | [`CSS_Beginner_to_Senior_2026.md`](./css/CSS_Beginner_to_Senior_2026.md) | Cascade, selectors, box/mô hình định dạng (formatting model / 포매팅 모델), responsive bố cục (layout / 레이아웃), animation, rendering và môi trường vận hành (production / 운영 환경) CSS kiến trúc (architecture / 아키텍처). |
| [`scss/`](./scss/) | [`SCSS_Beginner_to_Senior_2026.md`](./scss/SCSS_Beginner_to_Senior_2026.md) | Sass như chương trình compile-time tạo CSS; mô-đun (module / 모듈)/cấu hình (configuration / 구성), mixin/hàm (function / 함수), tính tương thích (compatibility / 호환성) và Dart Sass evolution. |
| [`tailwind/`](./tailwind/) | [`TailwindCSS_Beginner_to_Senior_2026.md`](./tailwind/TailwindCSS_Beginner_to_Senior_2026.md) | Utility-first authoring, thiết kế (design / 설계) tokens, bản dựng (build / 빌드)/content detection, variants, responsive UI và kiến trúc vận hành (production architecture / 운영 아키텍처) trên nền CSS. |
| [`javascript/`](./javascript/) | [`javascript_beginner_rebuilt.md`](./javascript/javascript_beginner_rebuilt.md) | Ngôn ngữ, mô hình thực thi (execution model / 실행 모델), trình duyệt (browser / 브라우저) host, DOM/events, async/vòng lặp sự kiện (event loop / 이벤트 루프), trạng thái (state / 상태), hiệu năng (performance / 성능), bảo mật (security / 보안), testing và kiến trúc (architecture / 아키텍처). Đây là danh mục (catalog / 카탈로그) điểm vào (entrypoint / 진입점). |
| [`react/`](./react/) | [`00_index.md`](./react/00_index.md) | React mô hình ứng dụng (application model / 애플리케이션 모델) từ kết xuất (render / 렌더링)/reconciliation và định danh trạng thái (state identity / 상태 식별성) đến effects, tính đồng thời (concurrency / 동시성), SSR/hydration, RSC, trình biên dịch (compiler / 컴파일러), bảo mật (security / 보안) và môi trường vận hành (production / 운영 환경). |
| [`websquare/`](./websquare/) | [`README.md`](./websquare/README.md) | Enterprise UI/thời gian chạy (runtime / 런타임) nhánh học (track / 트랙): page/phạm vi (scope / 범위), DataCollection, Submission, GridView, vòng đời (lifecycle / 생명주기), reusable kiến trúc (architecture / 아키텍처), tích hợp (integration / 통합), khả năng quan sát (observability / 관측 가능성), bảo mật (security / 보안) và di chuyển (migration / 마이그레이션). |
| [`xml/`](./xml/) | [`xml_01_beginner_detailed.md`](./xml/xml_01_beginner_detailed.md) | XML cú pháp (syntax / 문법), cây (tree / 트리)/mô hình dữ liệu (data model / 데이터 모델), namespaces, kiểm tra hợp lệ (validation / 검증), transformation, bảo mật (security / 보안) và các ranh giới (boundary / 경계) nơi XML gặp HTML/WebSquare/backend. |

Các tệp (file / 파일) `Master`, `Supplement`, `Legacy` hoặc `GLOSSARY_AND_COVERAGE` mở
rộng một đơn vị sở hữu (owner / 오너) đã có. Chúng không tạo ra một lộ trình học (learning path / 학습 경로) cạnh tranh với
điểm vào (entrypoint / 진입점) của lĩnh vực (domain / 도메인). Ví dụ, `react/00_index.md` là chỉ mục (index / 인덱스) của React nhánh học (track / 트랙),
không phải điểm vào (entrypoint / 진입점) của toàn Frontend.


> **Chuyển mạch:** Từ **Bản đồ thư mục và đơn vị sở hữu (owner / 오너)**, ta sang **ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác

Frontend cần dùng mô hình tư duy (mental model / 사고 모델) từ các lĩnh vực (domain / 도메인) lân cận nhưng không duplicate
toàn bộ nội dung của chúng:

- [Computer Science](../computer_science/README.md) sở hữu nền tảng mạng (network / 네트워크),
  operating các hệ thống (systems / 시스템들), bảo mật (security / 보안), databases, algorithms và kỹ nghệ phần mềm (software engineering / 소프트웨어 공학).
- [Backend Development](../10_backend/README.md) sở hữu server-side yêu cầu (request / 요청),
  Đặc tả API (API contract / API 계약), định danh (identity / 식별자), persistence, giao dịch (transaction / 트랜잭션), messaging và backend
  khả năng quan sát (observability / 관측 가능성). Frontend chỉ giữ máy khách (client / 클라이언트) đặc tả hợp đồng (contract / 계약), loading/lỗi (error / 오류) trạng thái (state / 상태),
  cancellation, stale kết quả (result / 결과) và trust-boundary implications.
- [DevOps / Platform Engineering](../devops_platform_engineering/README.md)
  sở hữu CI/CD, sản phẩm tạo ra (artifact / 산출물) delivery, hạ tầng (infrastructure / 인프라) và operating nền tảng (platform / 플랫폼).
  Frontend giữ bản dựng (build / 빌드) đồ thị (graph / 그래프), bundle, bộ nhớ đệm (cache / 캐시), bản đồ mã nguồn (source map / 소스 맵) và triển khai (deployment / 배포) bằng chứng (evidence / 증거) ở
  mức cần thiết để hiểu sản phẩm tạo ra (artifact / 산출물) chạy trong trình duyệt (browser / 브라우저).
- [Native Mobile Development](../11_native/00_INDEX.md) là ranh giới (boundary / 경계) khi một
  WebView/hybrid app đưa trình duyệt (browser / 브라우저) content vào bản địa (native / 네이티브) vòng đời (lifecycle / 생명주기). WebSquare có
  nhánh học (track / 트랙) riêng cho cầu nối (bridge / 브리지) nhưng không biến bản địa (native / 네이티브) API thành trình duyệt (browser / 브라우저) API.


> **Chuyển mạch:** Từ **ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác**, ta sang **Nguyên tắc chống duplicate và framework-first** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Nguyên tắc chống duplicate và framework-first

Một concept nên có một đơn vị sở hữu (owner / 오너) chuẩn gốc (canonical / 정본). Nếu câu hỏi là “DOM sự kiện (event / 이벤트) được schedule
như thế nào?”, đơn vị sở hữu (owner / 오너) là JavaScript/nền tảng trình duyệt (browser platform / 브라우저 플랫폼); React hoặc WebSquare chỉ
giải thích khung phần mềm (framework / 프레임워크) thêm lớp trừu tượng (abstraction / 추상화) nào và đặc tả hợp đồng (contract / 계약) nào cần giữ. Nếu câu hỏi
là “máy chủ (server / 서버) xác thực quyền Save ra sao?”, đơn vị sở hữu (owner / 오너) là Backend/bảo mật (security / 보안); frontend
chỉ mô tả cách hiển thị năng lực (capability / 역량), xử lý `401/403`, stale session và không tin
UI kiểm tra hợp lệ (validation / 검증) như authorization.

Khi khung phần mềm (framework / 프레임워크) có hành vi (behavior / 동작) riêng, tài liệu phải tách ba lớp:

1. trình duyệt (browser / 브라우저)/nền tảng (platform / 플랫폼) ngữ nghĩa (semantics / 의미론);
2. ngữ nghĩa khung phần mềm (framework semantics / 프레임워크 의미론) và quyền sở hữu trạng thái (state ownership / 상태 소유권);
3. đặc tả ứng dụng (application contract / 애플리케이션 계약), sản phẩm tạo ra (artifact / 산출물) và bằng chứng vận hành (production evidence / 운영 증거).

Tách lớp như vậy giúp đọc mã (code / 코드) legacy, migrate khung phần mềm (framework / 프레임워크) và kiểm tra lỗi môi trường vận hành (production / 운영 환경)
mà không cần học lại toàn bộ lĩnh vực (domain / 도메인) từ đầu.


> **Chuyển mạch:** Từ **Nguyên tắc chống duplicate và framework-first**, ta sang **trường hợp (case / 사례) studies và bằng chứng (evidence / 증거) lab** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) studies và bằng chứng (evidence / 증거) lab

[`90_case_studies/README.md`](./90_case_studies/README.md) là lớp tích hợp (integration / 통합) cấp
lĩnh vực (domain / 도메인). Nó không tạo đơn vị sở hữu (owner / 오너) lý thuyết (theory / 이론) mới mà buộc người học nối các đơn vị sở hữu (owner / 오너) hiện có
thành nhân quả (causal / 인과적) dấu vết (trace / 추적) có thể đo và rà soát (review / 검토).

Bắt đầu với:

- [`Request → Pixel → Interaction Trace`](./90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md) để dấu vết (trace / 추적) một màn hình từ document yêu cầu (request / 요청), parser, DOM/CSSOM và rendering tới async trạng thái (state / 상태), ranh giới bảo mật (security boundary / 보안 경계) và deployed sản phẩm tạo ra (artifact / 산출물).
- [`Rendering Performance Measurement Lab`](./90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md) để đo scripting/style/bố cục (layout / 레이아웃)/paint/composite, bố cục (layout / 레이아웃) vô hiệu hóa (invalidation / 무효화) và khung phần mềm (framework / 프레임워크)/trình duyệt (browser / 브라우저) rendering bằng baseline → dấu vết (trace / 추적) → hypothesis → one thay đổi (change / 변경) → re-measure.

Hai trường hợp (case / 사례) này là bằng chứng (evidence / 증거) đường dẫn (path / 경로) cho các gap cấp lĩnh vực (domain / 도메인) mà lý thuyết (theory / 이론) riêng lẻ khó kiểm
tra: người đọc phải chứng minh trình duyệt (browser / 브라우저) đang làm công việc (work / 작업) gì thay vì suy nguyên nhân
từ tên CSS thuộc tính (property / 속성) hoặc khung phần mềm (framework / 프레임워크) lớp trừu tượng (abstraction / 추상화).


> **Chuyển mạch:** Từ **trường hợp (case / 사례) studies và bằng chứng (evidence / 증거) lab**, ta sang **Kiểm tra coverage** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) studies và bằng chứng (evidence / 증거) lab

[`90_case_studies/README.md`](./90_case_studies/README.md) là lớp tích hợp (integration / 통합) cấp
lĩnh vực (domain / 도메인). Nó không tạo đơn vị sở hữu (owner / 오너) lý thuyết (theory / 이론) mới mà buộc người học nối các đơn vị sở hữu (owner / 오너) hiện có
thành nhân quả (causal / 인과적) dấu vết (trace / 추적) có thể đo và rà soát (review / 검토).

Bắt đầu với:

- [`Request → Pixel → Interaction Trace`](./90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md) để dấu vết (trace / 추적) một màn hình từ document yêu cầu (request / 요청), parser, DOM/CSSOM và rendering tới async trạng thái (state / 상태), ranh giới bảo mật (security boundary / 보안 경계) và deployed sản phẩm tạo ra (artifact / 산출물).
- [`Rendering Performance Measurement Lab`](./90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md) để đo scripting/style/bố cục (layout / 레이아웃)/paint/composite, bố cục (layout / 레이아웃) vô hiệu hóa (invalidation / 무효화) và khung phần mềm (framework / 프레임워크)/trình duyệt (browser / 브라우저) rendering bằng baseline → dấu vết (trace / 추적) → hypothesis → one thay đổi (change / 변경) → re-measure.

Hai trường hợp (case / 사례) này là bằng chứng (evidence / 증거) đường dẫn (path / 경로) cho các gap cấp lĩnh vực (domain / 도메인) mà lý thuyết (theory / 이론) riêng lẻ khó kiểm
tra: người đọc phải chứng minh trình duyệt (browser / 브라우저) đang làm công việc (work / 작업) gì thay vì suy nguyên nhân
từ tên CSS thuộc tính (property / 속성) hoặc khung phần mềm (framework / 프레임워크) lớp trừu tượng (abstraction / 추상화).

## Kiểm tra coverage

[`COVERAGE_AUDIT.md`](./COVERAGE_AUDIT.md) là checklist cấp lĩnh vực (domain / 도메인). kiểm tra (audit / 감사) không
chỉ đếm số tệp (file / 파일); nó kiểm tra mỗi stage có đơn vị sở hữu (owner / 오너), ranh giới (boundary / 경계), bất biến (invariant / 불변식), dạng thất bại (failure mode / 실패 모드), kiểm thử (test / 테스트)/bằng chứng (evidence / 증거) và đường dẫn học rõ ràng hay chưa. Khi thêm tệp (file / 파일) mới, ưu
tiên bổ sung vào đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) hoặc kiểm tra (audit / 감사) trước khi mở một title khung phần mềm (framework / 프레임워크)
mới.

> **Bàn giao:** Sau **Kiểm tra coverage**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [COVERAGE AUDIT](./COVERAGE_AUDIT.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.

# WebSquare Glossary & Coverage kiểm tra (audit / 감사)

> **Mạch đọc:** Đặt **WebSquare Glossary & Coverage kiểm tra (audit / 감사)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Glossary cốt lõi** sang **2. Identifier/API cần nhận diện**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tệp (file / 파일) này có hai vai trò. Phần đầu là glossary để nhận diện thuật ngữ Việt–Anh–Hàn và tên API thường xuất hiện trong codebase. Phần sau là coverage kiểm tra (audit / 감사) để kiểm tra bạn đã hiểu thư viện (library / 라이브러리) theo mô hình tư duy (mental model / 사고 모델) hay chỉ mới nhớ cú pháp (syntax / 문법).

## 1. Glossary cốt lõi
Phần “1. Glossary cốt lõi” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


| Tiếng Việt | English term | 한국어 용어 | Ý nghĩa trong WebSquare |
|---|---|---|---|
| nền tảng giao diện web doanh nghiệp | enterprise web UI nền tảng (platform / 플랫폼) | 엔터프라이즈 웹 UI 플랫폼 | thời gian chạy (runtime / 런타임)/tooling/thành phần (component / 컴포넌트)/dữ liệu (data / 데이터) lớp trừu tượng (abstraction / 추상화) để xây màn hình nghiệp vụ. |
| bộ máy chạy | engine/thời gian chạy (runtime / 런타임) | 엔진/런타임 | WebSquare Engine tạo page, thành phần (component / 컴포넌트), phạm vi (scope / 범위), binding và communication hành vi (behavior / 동작) trong trình duyệt (browser / 브라우저). |
| trang | page | 화면/페이지 | Đơn vị màn hình WebSquare, thường author bằng XML và chứa script/dữ liệu (data / 데이터)/UI. |
| phạm vi hiệu lực | phạm vi (scope / 범위) | 유효 범위/스코프 | ranh giới (boundary / 경계) xác định thành phần (component / 컴포넌트)/hàm (function / 함수) nào thuộc một page instance. |
| biến phạm vi trang | phạm vi (scope / 범위) variable | 스코프 변수 | Biến đại diện hành vi (behavior / 동작) của page; thường là `scwin`. |
| thành phần giao diện | UI thành phần (component / 컴포넌트) | UI 컴포넌트 | đầu vào (input / 입력), Button, GridView, WFrame, TabControl... do engine quản lý. |
| thành phần (component / 컴포넌트) tự định nghĩa | người dùng (user / 사용자) Defined thành phần (component / 컴포넌트) (UDC) | 사용자 정의 컴포넌트 | thành phần (component / 컴포넌트) reusable của dự án (project / 프로젝트) có thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트) đặc tả hợp đồng (contract / 계약) riêng. |
| mô hình dữ liệu phía máy khách (client / 클라이언트) | máy khách (client / 클라이언트) mô hình dữ liệu (data model / 데이터 모델) | 클라이언트 데이터 모델 | DataCollection nằm trong trình duyệt (browser / 브라우저) bộ nhớ (memory / 메모리). |
| đối tượng một bản ghi | DataMap | 데이터맵 | Key/giá trị (value / 값) mô hình (model / 모델) cho form, điều kiện (condition / 조건) hoặc bản ghi (record / 레코드). |
| đối tượng nhiều dòng | DataList | 데이터리스트 | Table-like máy khách (client / 클라이언트) mô hình dữ liệu (data model / 데이터 모델) có row/column/status. |
| danh sách liên kết | LinkedDataList | 링크드 데이터리스트 | View filter/sort dựa trên DataList. |
| trạng thái dòng | row status | 행 상태 | siêu dữ liệu (metadata / 메타데이터) như R/U/C/D/V biểu diễn vòng đời (lifecycle / 생명주기) thay đổi của row. |
| liên kết dữ liệu | dữ liệu (data / 데이터) binding | 데이터 바인딩 | Nối thành phần (component / 컴포넌트) với DataCollection để đồng bộ giá trị (value / 값)/mô hình (model / 모델). |
| gửi nhận dữ liệu | submission | 서브미션/데이터 통신 | đối tượng (object / 객체) mô tả yêu cầu (request / 요청)/phản hồi (response / 응답) ánh xạ (mapping / 매핑) và máy chủ (server / 서버) communication. |
| dữ liệu gửi | tham chiếu (reference / 참조) | 요청 데이터 참조 | DataCollection/dữ liệu (data / 데이터) đường dẫn (path / 경로) được Submission serialize gửi máy chủ (server / 서버). |
| dữ liệu nhận | mục tiêu (target / 대상) | 응답 대상 | DataCollection/dữ liệu (data / 데이터) đường dẫn (path / 경로) nhận phản hồi (response / 응답). |
| khung trang | WFrame | WFrame | thành phần nguyên thủy (primitive / 기본 요소) để nhúng page, tạo phạm vi (scope / 범위) và hỗ trợ SPA composition. |
| tải trước | preload | 프리로드 | Tải/tạo một phần tài nguyên (resource / 자원)/đối tượng (object / 객체) trước khi UI thật sự kết xuất (render / 렌더링) hoặc activate. |
| kết xuất giao diện | rendering | 렌더링 | Tạo/cập nhật biểu diễn (representation / 표현) UI/DOM từ thành phần (component / 컴포넌트) trạng thái (state / 상태). |
| ứng dụng một trang | Single Page ứng dụng (application / 애플리케이션) (SPA) | 단일 페이지 애플리케이션 | Giữ engine shell và thay content page/frame mà không reload toàn ứng dụng. |
| cửa sổ bật lên | popup | 팝업 | Page/cửa sổ (window / 윈도우) tạm thời với đầu vào (input / 입력)/đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약) riêng. |
| vòng đời | vòng đời (lifecycle / 생명주기) | 생명주기 | Trình tự tải (load / 로드) script, tạo thành phần (component / 컴포넌트), kết xuất (render / 렌더링), sự kiện (event / 이벤트), unload/cleanup. |
| quốc tế hóa | internationalization (i18n) | 국제화 | Chuẩn bị UI cho nhiều ngôn ngữ/locale, không chỉ dịch văn bản (text / 텍스트). |
| khả năng truy cập | khả năng tiếp cận (accessibility / 접근성) | 접근성 | Khả năng thao tác/hiểu UI bằng keyboard, screen reader và nhiều nhu cầu sử dụng khác. |
| khả năng kiểm thử | testability | 테스트 용이성 | Mức độ kiến trúc (architecture / 아키텍처) cho phép quan sát và kiểm chứng hành vi (behavior / 동작) mà không phải boot toàn hệ thống cho mọi quy tắc (rule / 규칙). |
| kiểm thử hồi quy | regression testing | 회귀 테스트 | Chứng minh hành vi (behavior / 동작) đã đúng trước đây không bị phá bởi thay đổi mới. |
| dữ liệu kiểm thử có chủ đích | kiểm thử (test / 테스트) fixture | 테스트 픽스처 | Dataset/cấu hình (config / 설정) nhỏ, deterministic và có quyền sở hữu (ownership / 소유권) dùng để tái tạo scenario. |
| hiện vật bản dựng (build / 빌드) | hiện vật bản dựng (build artifact / 빌드 산출물) | 빌드 산출물 | đầu ra (output / 출력) thực thi/đóng gói được tạo từ nguồn (source / 소스), ví dụ W-Pack JavaScript. |
| nguồn gốc bản dựng (build / 빌드) | bản dựng (build / 빌드) provenance | 빌드 추적 정보 | Quan hệ giữa nguồn (source / 소스) lần ghi nhận (commit / 커밋), công cụ (tool / 도구)/cấu hình (config / 설정) bản dựng (build / 빌드), sản phẩm tạo ra (artifact / 산출물) và triển khai (deployment / 배포) định danh (identity / 식별자). |
| lệch cấu hình | cấu hình (configuration / 구성) drift | 설정 드리프트 | môi trường (environment / 환경) chạy cấu hình (config / 설정)/bản dựng (build / 빌드) khác chuẩn gốc (canonical / 정본) expectation dù ứng dụng (application / 애플리케이션) nguồn (source / 소스) giống nhau. |
| trạng thái nguồn chuẩn | nguồn chuẩn (source of truth / 정본) | 단일 진실 공급원 | Nơi chuẩn gốc (canonical / 정본) trạng thái (state / 상태) được giữ để tránh duplicate trạng thái (state / 상태). |
| bất biến | bất biến (invariant / 불변식) | 불변 조건 | Điều luôn phải đúng, ví dụ unique key hoặc authorization. |
| điều kiện tranh chấp | race điều kiện (condition / 조건) | 경쟁 상태 | Kết quả phụ thuộc thứ tự timing của nhiều async thao tác (operation / 연산). |
| tính lũy đẳng | idempotency | 멱등성 | thử lại (retry / 재시도) cùng yêu cầu (request / 요청) không tạo thêm side tác động (effect / 효과) ngoài ý muốn. |
| bằng chứng vận hành | bằng chứng vận hành (production evidence / 운영 증거) | 운영 증거 | mạng (network / 네트워크) dấu vết (trace / 추적), log, chỉ số (metric / 지표), ngăn xếp (stack / 스택), vùng nhớ động (heap / 힙), timing dùng để kiểm chứng giả thuyết. |
| nợ tương thích | tính tương thích (compatibility / 호환성) debt | 호환성 부채 | Workaround/API cũ còn tồn tại vì generation/trình duyệt (browser / 브라우저)/dự án (project / 프로젝트) legacy. |

## 2. Identifier/API cần nhận diện

`scwin` — page/phạm vi (scope / 범위) không gian tên (namespace / 네임스페이스) thường chứa sự kiện (event / 이벤트) handler và hàm (function / 함수) nghiệp vụ của màn hình.

`$p` — WebSquare utility có page/phạm vi (scope / 범위) ngữ cảnh (context / 맥락). Các API như `parent()`, `top()`, `main()`, `openPopup()`, `executeSubmission()` thường xuất hiện qua `$p` tùy phiên bản (version / 버전)/bản dựng (build / 빌드).

`$w` — utility style xuất hiện nhiều trong mã (code / 코드) WebSquare cũ/non-Scope. Không blind-replace bằng `$p`; phải hiểu thực thi (execution / 실행) ngữ cảnh (context / 맥락).

`DataMap` — mô hình (model / 모델) dạng key/giá trị (value / 값).

`DataList` — mô hình (model / 모델) dạng nhiều row, có API như `getRowCount()`, `getCellData()`, `getRowJSON()`, `getRowStatus()` ở SP5.

`LinkedDataList` — derived/filter/sort view của DataList.

`Submission` — communication đối tượng (object / 객체) nối DataCollection với HTTP/máy chủ (server / 서버).

`GridView` — view thành phần (component / 컴포넌트) cho bảng (table / 테이블) dữ liệu (data / 데이터), thường bind DataList.

`WFrame` — page composition + phạm vi (scope / 범위) thành phần nguyên thủy (primitive / 기본 요소).

`WindowContainer`, `TabControl` — bộ chứa (container / 컨테이너) có thể quản lý nhiều page/cửa sổ (window / 윈도우)/tab và phạm vi (scope / 범위) relationship.

`UDC` — thành phần (component / 컴포넌트) do dự án (project / 프로젝트) định nghĩa với công khai (public / 공개) thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트), phù hợp cho UI năng lực (capability / 역량) reusable có ranh giới (boundary / 경계) rõ.

`$p.getOptions()` — API thường dùng để đọc option/thuộc tính (property / 속성) đã truyền vào UDC; chính xác (exact / 정확한) hành vi (behavior / 동작) cần đối chiếu bản dựng (build / 빌드).

`$p.dynamicCreate()` — API dùng trong các bản dựng (build / 빌드) tương ứng để tạo thành phần (component / 컴포넌트)/UDC động; động (dynamic / 동적) quyền sở hữu (ownership / 소유권) và cleanup phải được thiết kế rõ.

`dataObject` — parameter đối tượng (object / 객체) dùng khi tạo WFrame/popup ở các API tương ứng; nên chứa JSON-serializable plain dữ liệu (data / 데이터).

`setSrc()` — thay nguồn (source / 소스) page của WFrame/page bộ chứa (container / 컨테이너) tương ứng; thao tác (operation / 연산) có vòng đời (lifecycle / 생명주기), không nên giả định child sẵn sàng ngay sau lời gọi (call / 호출).

`getParameter()` — đọc parameter được truyền vào page theo đặc tả hợp đồng (contract / 계약) tương ứng.

`alwaysDraw` — thuộc tính (property / 속성) quan trọng của TabControl/content để quyết định kết xuất (render / 렌더링) eagerly hay lazily trong các cấu hình (configuration / 구성) tương ứng.

`frameMode="wframePreload"` — chế độ (mode / 모드) cho phép tài nguyên (resource / 자원)/đối tượng (object / 객체) của tab có thể được chuẩn bị trước khi nội dung được kết xuất (render / 렌더링); vì vậy object-ready không đồng nghĩa render-ready.

`localeRef`, `useLocale`, ngôn ngữ (language / 언어) pack — cơ chế (mechanism / 메커니즘) đa ngôn ngữ của WebSquare cho thành phần (component / 컴포넌트)/bản dựng (build / 빌드) hỗ trợ.

`W-Pack` — cơ chế bản dựng (build / 빌드)/chuyển page nguồn (source / 소스) XML sang JavaScript sản phẩm tạo ra (artifact / 산출물) trong WebSquare5; SP5 có stand-alone W-Pack để dùng trong command-line/CI workflow.

`client.config.xml` — tài nguyên (resource / 자원) cấu hình phía máy khách (client / 클라이언트) trong SP5 Studio; chính xác (exact / 정확한) generated/thời gian chạy (runtime / 런타임) biểu diễn (representation / 표현) cần kiểm tra theo dự án (project / 프로젝트)/bản dựng (build / 빌드).

`server.config.xml` — tài nguyên (resource / 자원) cấu hình phía máy chủ (server / 서버)/engine trong SP5 Studio; quản lý nhóm setting engine/máy chủ (server / 서버) thay vì page lô-gic nghiệp vụ (business logic / 비즈니스 로직).

## 3. Những cặp khái niệm dễ nhầm

### Thành phần (component / 컴포넌트) đối tượng (object / 객체) vs DOM element

Thành phần (component / 컴포넌트) đối tượng (object / 객체) là công khai (public / 공개) khung phần mềm (framework / 프레임워크) lớp trừu tượng (abstraction / 추상화). DOM element là biểu diễn (representation / 표현) bên dưới. Không đồng nhất hai thứ.

### Logical ID vs DOM ID

Logical thành phần (component / 컴포넌트) ID là ID nhà phát triển (developer / 개발자) dùng trong phạm vi (scope / 범위). vật lý (physical / 물리적) DOM ID có thể được engine biến đổi, đặc biệt khi WFrame/phạm vi (scope / 범위) tạo nhiều instance.

### GridView vs DataList

GridView hiển thị và xử lý tương tác (interaction / 상호작용). DataList giữ dữ liệu và row status.

### UDC đặc tả hợp đồng (contract / 계약) vs UDC internals

Bên tiêu thụ (consumer / 소비자) nên phụ thuộc thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트) công khai (public / 공개). ID thành phần (component / 컴포넌트), DataMap hoặc popup nội bộ là hiện thực (implementation / 구현) detail.

### Template vs thời gian chạy (runtime / 런타임) lớp trừu tượng (abstraction / 추상화)

Template/snippet giúp sinh nguồn (source / 소스) nhất quán. UDC/dùng chung (common / 공통) mô-đun (module / 모듈)/WFrame mới tạo hành vi (behavior / 동작) reuse ở thời gian chạy (runtime / 런타임).

### Object-ready vs render-ready

DataCollection hoặc `scwin` có thể đã tồn tại trong preload stage trong khi UI thành phần (component / 컴포넌트) chưa kết xuất (render / 렌더링) đủ để thao tác.

### Render-ready vs data-ready

Page đã kết xuất (render / 렌더링) không có nghĩa Submission khởi tạo đã hoàn thành.

### Đầu vào (input / 입력) filtering vs kiểm tra hợp lệ (validation / 검증)

`allowChar`, `dataType` và tương tác (interaction / 상호작용) guard không chứng minh nghiệp vụ (business / 비즈니스) giá trị (value / 값) hợp lệ.

### UI kiểm tra hợp lệ (validation / 검증) vs máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증)

UI kiểm tra hợp lệ (validation / 검증) cải thiện UX. máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증) bảo vệ bất biến (invariant / 불변식) và trust ranh giới (boundary / 경계).

### hidden/readOnly vs authorization

Thuộc tính (property / 속성) UI không tạo ranh giới bảo mật (security boundary / 보안 경계). Authorization phải ở máy chủ (server / 서버).

### Localization vs internationalization

Dịch label là một phần của i18n. Date/number format, văn bản (text / 텍스트) expansion, bố cục (layout / 레이아웃), collation và locale hành vi (behavior / 동작) cũng thuộc i18n.

### Khả năng tiếp cận (accessibility / 접근성) vs hiệu năng (performance / 성능)

Khả năng tiếp cận (accessibility / 접근성) có thể làm tăng rendering footprint trong một số Grid cấu hình (configuration / 구성), nhưng giải pháp đúng thường là tối ưu dataset/kết xuất (render / 렌더링) chiến lược (strategy / 전략) chứ không tắt khả năng tiếp cận (accessibility / 접근성) mặc định.

### HTTP success vs nghiệp vụ (business / 비즈니스) success

HTTP 200 chỉ chứng minh vận chuyển (transport / 전송)/ứng dụng (application / 애플리케이션) endpoint trả phản hồi (response / 응답). nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) vẫn có thể thất bại (fail / 실패).

### row chỉ mục (index / 인덱스) vs nghiệp vụ (business / 비즈니스) định danh (identity / 식별자)

Chỉ mục (index / 인덱스) là vị trí có thể đổi khi sort/filter. nghiệp vụ (business / 비즈니스) key mới là định danh (identity / 식별자) ổn định.

### popup/frame đầu vào (input / 입력) vs dùng chung (shared / 공유) toàn cục (global / 전역) trạng thái (state / 상태)

Parameter/dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) dễ lập luận (reasoning / 추론) và reuse hơn toàn cục (global / 전역) mutable trạng thái (state / 상태).

### sync hàm (function / 함수) lời gọi (call / 호출) vs async nghiệp vụ (business / 비즈니스) thao tác (operation / 연산)

Gọi hàm (function / 함수) giữa phạm vi (scope / 범위) có thể synchronous, nhưng hàm (function / 함수) có thể bắt đầu mạng (network / 네트워크)/frame tải (load / 로드) asynchronous.

### Nguồn (source / 소스) XML vs thời gian chạy (runtime / 런타임) JavaScript sản phẩm tạo ra (artifact / 산출물)

XML là authoring nguồn (source / 소스); thời gian chạy (runtime / 런타임) có thể dùng JS sản phẩm tạo ra (artifact / 산출물) do W-Pack tạo.

### Nguồn (source / 소스) định danh (identity / 식별자) vs bản dựng (build / 빌드) định danh (identity / 식별자) vs triển khai (deployment / 배포) định danh (identity / 식별자)

Lần ghi nhận (commit / 커밋) đã merge chỉ chứng minh nguồn (source / 소스) trạng thái (state / 상태). bản dựng (build / 빌드) định danh (identity / 식별자) chứng minh sản phẩm tạo ra (artifact / 산출물) nào được tạo; triển khai (deployment / 배포) định danh (identity / 식별자) chứng minh sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) nào môi trường (environment / 환경) đang phục vụ.

### Kiểm thử (test / 테스트) delay vs vòng đời (lifecycle / 생명주기) synchronization

`setTimeout`/sleep chỉ chờ thời gian. kiểm thử (test / 테스트) đúng nên chờ observable điều kiện (condition / 조건) như yêu cầu (request / 요청) completion, DataList trạng thái (state / 상태) hoặc ready đặc tả hợp đồng (contract / 계약).

### mock tính đúng đắn (correctness / 정확성) vs môi trường vận hành (production / 운영 환경) tính đúng đắn (correctness / 정확성)

Mock giúp cô lập ranh giới (boundary / 경계) nhưng không chứng minh WebSquare tích hợp (integration / 통합) nếu mock đã bỏ qua phạm vi (scope / 범위), async hoặc vòng đời (lifecycle / 생명주기) ngữ nghĩa (semantics / 의미론) quan trọng.

## 4. Coverage kiểm tra (audit / 감사) — Foundation

Bạn đã đạt mức Foundation khi có thể giải thích bằng lời của mình, không nhìn ghi chú (note / 노트):

WebSquare giải quyết vấn đề gì mà trình duyệt (browser / 브라우저) + JavaScript thuần không tự chuẩn hóa cho enterprise screen?

Vì sao WebSquare không phải ngôn ngữ lập trình riêng?

Studio khác Engine thế nào?

Vì sao page XML có thể dẫn đến JavaScript thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물)?

Vì sao thành phần (component / 컴포넌트) không nên đồng nhất với DOM element?

`scwin` giải quyết collision gì?

`$p` cần page ngữ cảnh (context / 맥락) để làm gì?

DataMap và DataList khác nhau theo dữ liệu (data / 데이터) shape và use trường hợp (case / 사례) nào?

Submission tham chiếu (reference / 참조)/mục tiêu (target / 대상) biểu diễn gì?

Nếu chưa trả lời rõ được các câu này, quay lại chapter 01–03.

## 5. Coverage kiểm tra (audit / 감사) — Intermediate

Bạn đạt mức Intermediate khi có thể lập luận (reasoning / 추론) một màn hình truy vấn (query / 쿼리)/edit mà không dò API liên tục:

Khi người dùng (user / 사용자) sửa đầu vào (input / 입력) bind DataMap, trạng thái (state / 상태) nào thay đổi?

Khi Grid bind DataList, dữ liệu chuẩn gốc (canonical / 정본) phía máy khách (client / 클라이언트) nằm ở đâu?

Row `R/U/C/D/V` biểu diễn chuyển tiếp trạng thái (state transition / 상태 전이) gì?

Tại sao deleted row có thể vẫn tồn tại trong mô hình (model / 모델)?

Tại sao mã (code / 코드) ngay sau `executeSubmission()` không được giả định phản hồi (response / 응답) đã về?

Tại sao HTTP 200 chưa đủ để hiển thị “Save success”?

Tại sao máy chủ (server / 서버) paging làm `getRowCount()` không đại diện total dataset?

Tại sao giữ selected row chỉ mục (index / 인덱스) lâu dài có thể sai?

## 6. Coverage kiểm tra (audit / 감사) — phạm vi (scope / 범위) & kiến trúc (architecture / 아키텍처)

Bạn đạt mức này khi có thể mở một app shell nhiều tab và vẽ được topology:

Page nào là parent/child?

Mỗi WFrame có phạm vi (scope / 범위) nào?

Hai page có cùng thành phần (component / 컴포넌트) ID vì sao không collision?

`parent()`, `main()`, `top()` có khác nhau về intent nào?

Khi nào nên dùng `getWindow()` thay vì chuỗi (chain / 사슬) nhiều `parent()`?

`dataObject` nên chứa loại dữ liệu gì và vì sao không nên chứa hàm (function / 함수)/cửa sổ (window / 윈도우)/thành phần (component / 컴포넌트) instance?

Popup nên trả kết quả (result / 결과) đặc tả hợp đồng (contract / 계약) thế nào để giảm coupling?

Vì sao `setSrc()` tạo vòng đời (lifecycle / 생명주기) race nếu gọi child ngay sau đó?

## 7. Coverage kiểm tra (audit / 감사) — Reusable kiến trúc (architecture / 아키텍처)

Bạn đạt mức này khi có thể thiết kế một thành phần (component / 컴포넌트) dùng ở hàng chục màn hình mà không làm bên tiêu thụ (consumer / 소비자) phụ thuộc internals:

Khi nào dùng UDC thay vì WFrame page?

Khi nào pure dùng chung (common / 공통) hàm (function / 함수) tốt hơn helper đụng thành phần (component / 컴포넌트) trực tiếp?

Thuộc tính (property / 속성) nào là init cấu hình (configuration / 구성), thuộc tính (property / 속성) nào cần thời gian chạy (runtime / 런타임) setter?

Phương thức (method / 메서드) công khai (public / 공개) của UDC nên diễn đạt năng lực (capability / 역량) hay mirror nội bộ (internal / 내부) thành phần (component / 컴포넌트) API?

Tại sao sự kiện (event / 이벤트)/kết quả (result / 결과) đặc tả hợp đồng (contract / 계약) giảm coupling hơn child gọi thẳng `$p.parent()`?

Trạng thái (state / 상태) nào thuộc UDC, trạng thái (state / 상태) nào phải nằm ở page/DataCollection?

Template/snippet khác thời gian chạy (runtime / 런타임) reuse thế nào?

Động (dynamic / 동적) thành phần (component / 컴포넌트)/listener được cleanup ở ranh giới (boundary / 경계) nào?

Thay đổi công khai (public / 공개) UDC phương thức (method / 메서드)/sự kiện (event / 이벤트) có blast radius gì?

## 8. Coverage kiểm tra (audit / 감사) — Forms, i18n & khả năng tiếp cận (accessibility / 접근성)

Bạn đạt mức này khi có thể giải thích một form môi trường vận hành (production / 운영 환경) qua nhiều lớp:

Đầu vào (input / 입력) filtering khác ngữ nghĩa (semantic / 의미적) kiểm tra hợp lệ (validation / 검증) thế nào?

Chuẩn gốc (canonical / 정본) biểu diễn (representation / 표현) của date/money/ID nằm ở đâu?

Cross-field quy tắc (rule / 규칙) có đơn vị sở hữu (owner / 오너) duy nhất hay bị bản sao (copy / 복사) ở nhiều handler?

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) giúp UX nhưng vì sao máy chủ (server / 서버) vẫn phải validate?

`readOnly`, `disabled`, `hidden` khác nhau nhưng vì sao đều không phải authorization?

Locale key nên dùng ngữ nghĩa (semantic / 의미적) key hay raw Korean sentence?

Missing translation được phát hiện bằng bằng chứng (evidence / 증거) nào?

Bố cục (layout / 레이아웃) có chịu được văn bản (text / 텍스트) expansion giữa Korean/English/Vietnamese không?

Keyboard-only người dùng (user / 사용자) có đi hết form được không?

Grid khả năng tiếp cận (accessibility / 접근성) option ảnh hưởng DOM/bộ nhớ (memory / 메모리) thế nào và bạn tối ưu dataset ra sao?

Tệp (file / 파일) upload/Excel import cần server-side trust controls nào?

## 9. Coverage kiểm tra (audit / 감사) — Rendering & thời gian tồn tại (lifetime / 수명)

Bạn đạt mức này khi không còn dùng từ “loaded” một cách mơ hồ:

Source-ready, object-ready, render-ready và data-ready khác nhau thế nào?

Tại sao `setTimeout(500)` không phải vòng đời (lifecycle / 생명주기) synchronization?

`alwaysDraw=false` đổi startup chi phí (cost / 비용) thành first-use chi phí (cost / 비용) như thế nào?

`wframePreload` tạo trạng thái gì mà `scwin`/DataCollection dùng được nhưng UI manipulation chưa chắc dùng được?

Tại sao preload không tự động là hiệu năng (performance / 성능) win?

Một timer/cửa sổ (window / 윈도우) listener giữ page phạm vi (scope / 범위) sống sau close bằng cơ chế reachability nào?

Pending Submission trả về sau điều hướng (navigation / 내비게이션) có thể tạo stale cập nhật (update / 업데이트) ra sao?

Debounce khác latest-intent guard như thế nào?

Cold-cache và warm-cache kiểm thử (test / 테스트) cho kết quả khác nhau tại sao?

Bạn chứng minh bộ nhớ (memory / 메모리) leak bằng repeated vòng đời (lifecycle / 생명주기) + vùng nhớ động (heap / 힙) bằng chứng (evidence / 증거) thế nào?

## 10. Coverage kiểm tra (audit / 감사) — cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경)

Bạn đạt mức cấp cao (senior / 시니어) môi trường vận hành (production / 운영 환경) khi gặp sự cố (incident / 인시던트) và biết bằng chứng (evidence / 증거) cần lấy trước khi sửa:

Tìm kiếm (search / 검색) chậm: bạn đo mạng (network / 네트워크), ánh xạ (mapping / 매핑) hay rendering ở đâu?

Grid 50.000 row lag: làm sao phân biệt payload chi phí (cost / 비용) và renderer chi phí (cost / 비용)?

Screen càng mở lâu càng chậm: làm sao chứng minh timer/listener leak?

Save đôi lúc duplicate: bằng chứng (evidence / 증거) nào phân biệt double-click máy khách (client / 클라이언트) và thử lại (retry / 재시도) máy chủ (server / 서버)?

Phản hồi (response / 응답) 200 nhưng Grid rỗng: chuỗi xử lý (pipeline / 파이프라인) gỡ lỗi (debug / 디버그) theo thứ tự nào?

Popup đôi lúc không tìm thấy child đối tượng (object / 객체): vòng đời (lifecycle / 생명주기) hay phạm vi (scope / 범위) hypothesis nào cần kiểm thử (test / 테스트)?

Tại sao readOnly/hidden trường dữ liệu (field / 필드) không bảo vệ role/permission?

Tại sao mutation yêu cầu (request / 요청) không nên auto-retry mù quáng?

W-Pack/bộ nhớ đệm (cache / 캐시) có thể làm môi trường vận hành (production / 운영 환경) chạy mã (code / 코드) khác nguồn (source / 소스) bạn vừa sửa như thế nào?

API công khai (public API / 공개 API) discipline giúp engine upgrade an toàn hơn private DOM/engine hack như thế nào?

## 11. Coverage kiểm tra (audit / 감사) — Legacy & di chuyển (migration / 마이그레이션)

Bạn đạt mức migration-ready khi có thể phân loại mã (code / 코드) cũ:

Nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) nào phải giữ?

IFrame isolation cũ khác WFrame phạm vi (scope / 범위) thế nào?

`window.parent` nên migrate sang page đặc tả hợp đồng (contract / 계약) nào?

`$w` usage nào có thể chuyển `$p`, usage nào cần hiểu ngữ cảnh (context / 맥락) trước?

jQuery/DOM hack nào đã có thành phần (component / 컴포넌트) API thay thế?

Callback string/eval có thể thay bằng kết quả (result / 결과) đặc tả hợp đồng (contract / 계약) không?

Synchronous Submission di chuyển (migration / 마이그레이션) sang async làm điều khiển (control / 제어) luồng (flow / 흐름) thay đổi ở đâu?

Cấu hình (config / 설정)/workaround nào là historical debt và bằng chứng (evidence / 증거) nào cho phép remove?

Engine upgrade cần regression areas nào?

UDC/dùng chung (common / 공통) tầng (layer / 계층) cũ có công khai (public / 공개) đặc tả hợp đồng (contract / 계약) nào phải giữ khi refactor?

## 12. Coverage kiểm tra (audit / 감사) — Testing & Testability

Bạn đạt mức này khi có thể biến mô hình tư duy (mental model / 사고 모델) thành regression bằng chứng (evidence / 증거) thay vì chỉ manual-click:

Nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) nào nên được kiểm thử (test / 테스트) bằng pure hàm (function / 함수) và bất biến (invariant / 불변식) nào cần WebSquare Engine thật?

Tại sao mock Submission callback synchronous có thể che race bug môi trường vận hành (production / 운영 환경)?

DataList CRUD kiểm thử (test / 테스트) phải assert giá trị (value / 값), nghiệp vụ (business / 비즈니스) định danh (identity / 식별자) và row status như thế nào?

Tại sao E2E selector dựa vào vật lý (physical / 물리적) DOM ID/private engine cấu trúc (structure / 구조) dễ vỡ?

Bạn chờ async bằng observable điều kiện (condition / 조건) nào thay vì `sleep(1000)`?

Làm sao fault-inject phản hồi (response / 응답) A về sau phản hồi (response / 응답) B để kiểm tra latest intent?

Nested WFrame topology có thể lộ hidden `parent().parent()` phụ thuộc (dependency / 의존성) thế nào?

UDC đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) nên phụ thuộc công khai (public / 공개) thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트) hay nội bộ (internal / 내부) thành phần (component / 컴포넌트) ID?

Bộ nhớ (memory / 메모리) regression cần lặp vòng đời (lifecycle / 생명주기) bao nhiêu lần và bằng chứng (evidence / 증거) nào chứng minh retained đối tượng (object / 객체)/listener?

Bảo mật (security / 보안) negative kiểm thử (test / 테스트) nào chứng minh hidden/readOnly không phải authorization?

Một flaky kiểm thử (test / 테스트) cần được root-cause ở synchronization, fixture, selector hay cleanup như thế nào thay vì thử lại (retry / 재시도) đến xanh?

## 13. Coverage kiểm tra (audit / 감사) — bản dựng (build / 빌드), cấu hình (config / 설정) & triển khai (deployment / 배포)

Bạn đạt mức này khi có thể dấu vết (trace / 추적) một bản phát hành (release / 릴리스) từ Git đến trình duyệt (browser / 브라우저):

Nguồn (source / 소스) định danh (identity / 식별자), bản dựng (build / 빌드) định danh (identity / 식별자) và triển khai (deployment / 배포) định danh (identity / 식별자) khác nhau thế nào?

Vì sao lần ghi nhận (commit / 커밋) đã merge không chứng minh `_wpack_` sản phẩm tạo ra (artifact / 산출물) mới đang chạy?

Stand-alone W-Pack giúp CI/reproducible bản dựng (build / 빌드) ở ranh giới (boundary / 경계) nào?

`client.config.xml` và `server.config.xml` khác nhau về logical responsibility nào?

Ngữ cảnh (context / 맥락) gốc (root / 루트) sai có thể biểu hiện thành WFrame/Submission/tài nguyên (resource / 자원) bug ra sao?

Tại sao UAT và PROD khác engine bản dựng (build / 빌드) làm regression bằng chứng (evidence / 증거) yếu đi?

Bộ nhớ đệm (cache / 캐시) key/phiên bản (version / 버전) phải thay đổi khi sản phẩm tạo ra (artifact / 산출물) content đổi vì sao?

Tại sao sửa trực tiếp generated W-Pack JS tạo divergence với chuẩn gốc (canonical / 정본) nguồn (source / 소스)?

Build-once-promote giảm rủi ro “kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물) A, deploy sản phẩm tạo ra (artifact / 산출물) B” như thế nào?

Cấu hình (config / 설정) diff nào cần lấy khi nguồn (source / 소스) giống nhau nhưng chỉ PROD lỗi?

Quay lui (rollback / 롤백) cần xử lý sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), bộ nhớ đệm (cache / 캐시) và backend tính tương thích (compatibility / 호환성) ra sao?

## 14. Failure-mode ma trận (matrix / 행렬)
Phần “14. Failure-mode ma trận (matrix / 행렬)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


| Triệu chứng | Hypothesis ưu tiên | bằng chứng (evidence / 증거) đầu tiên |
|---|---|---|
| Click không làm gì | sự kiện (event / 이벤트)/disabled/phạm vi (scope / 범위) | breakpoint handler |
| yêu cầu (request / 요청) không chạy | kiểm tra hợp lệ (validation / 검증)/Submission/phạm vi (scope / 범위) | mạng (network / 네트워크) + handler log |
| yêu cầu (request / 요청) 200, mô hình (model / 모델) rỗng | mục tiêu (target / 대상)/lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) | phản hồi (response / 응답) body + DataList |
| mô hình (model / 모델) có dữ liệu (data / 데이터), Grid rỗng | binding/filter/kết xuất (render / 렌더링) | DataList trạng thái (state / 상태) + Grid binding |
| Save gửi giá trị cũ | binding/lần ghi nhận (commit / 커밋) timing/duplicate trạng thái (state / 상태) | yêu cầu (request / 요청) payload + mô hình (model / 모델) giá trị (value / 값) |
| Popup không gọi được parent | wrong phạm vi (scope / 범위)/topology | resolve parent phạm vi (scope / 범위) |
| Tab preload gọi phương thức (method / 메서드) nhưng lỗi UI | object-ready nhưng chưa render-ready | tab/frame chế độ (mode / 모드) + thành phần (component / 컴포넌트) existence |
| First open tab chậm | lazy first-use chi phí (cost / 비용) | mạng (network / 네트워크) + hiệu năng (performance / 성능) dấu vết (trace / 추적) |
| Mọi tab tải (load / 로드) chậm từ đầu | eager `alwaysDraw`/dữ liệu (data / 데이터) initialization | mạng (network / 네트워크) waterfall + tab cấu hình (config / 설정) |
| UDC chạy ở page A nhưng thất bại (fail / 실패) page B | hidden phụ thuộc (dependency / 의존성) vào parent/phạm vi (scope / 범위)/cấu hình (config / 설정) | option payload + parent topology |
| Form hợp lệ máy khách (client / 클라이언트) nhưng máy chủ (server / 서버) reject | nghiệp vụ (business / 비즈니스)/máy chủ (server / 서버) bất biến (invariant / 불변식) khác máy khách (client / 클라이언트) quy tắc (rule / 규칙) | payload + nghiệp vụ (business / 비즈니스) lỗi (error / 오류) mã (code / 코드) |
| Locale khác bị vỡ bố cục (layout / 레이아웃) | văn bản (text / 텍스트) expansion/fixed sizing | screenshot + computed bố cục (layout / 레이아웃) |
| dữ liệu (data / 데이터) đúng nhưng screen lag | rendering/script chi phí (cost / 비용) | hiệu năng (performance / 성능) dấu vết (trace / 추적) |
| Screen chậm dần | leak/timer/listener | repeat kiểm thử (test / 테스트) + vùng nhớ động (heap / 힙)/yêu cầu (request / 요청) count |
| Duplicate bản ghi (record / 레코드) | duplicate yêu cầu (request / 요청)/idempotency | mạng (network / 네트워크) + máy chủ (server / 서버) dấu vết (trace / 추적) |
| E2E kiểm thử (test / 테스트) lúc pass lúc thất bại (fail / 실패) | timing/dùng chung (shared / 공유) fixture/private selector | dấu vết (trace / 추적) + thử lại (retry / 재시도) comparison + kiểm thử (test / 테스트) isolation |
| Git có mã (code / 코드) mới nhưng UI vẫn cũ | stale W-Pack/triển khai (deployment / 배포)/bộ nhớ đệm (cache / 캐시) định danh (identity / 식별자) | mạng (network / 네트워크) sản phẩm tạo ra (artifact / 산출물) + bản dựng (build / 빌드) manifest |
| WFrame 404 chỉ ở PROD | ngữ cảnh (context / 맥락) gốc (root / 루트)/proxy/sản phẩm tạo ra (artifact / 산출물) đường dẫn (path / 경로) | resolved URL + cấu hình (config / 설정) diff |
| Chỉ môi trường vận hành (production / 운영 환경) lỗi | cấu hình (config / 설정)/bản dựng (build / 빌드)/bộ nhớ đệm (cache / 캐시) drift | engine/cấu hình (config / 설정)/sản phẩm tạo ra (artifact / 산출물) diff |

## 15. nội bộ (internal / 내부) kiến thức (knowledge / 지식) connections

JavaScript thực thi (execution / 실행), closure, vòng lặp sự kiện (event loop / 이벤트 루프) và Promise: [JavaScript Intermediate](../javascript/javascript_intermediate.md).

Trình duyệt (browser / 브라우저)/thời gian chạy (runtime / 런타임) hiệu năng (performance / 성능), bộ nhớ (memory / 메모리) và bảo mật (security / 보안): [JavaScript Senior](../javascript/javascript_senior.md) và [JavaScript Master](../javascript/javascript_master_supplement_detailed.md).

XML cây (tree / 트리), không gian tên (namespace / 네임스페이스), parsing và lược đồ (schema / 스키마) mindset: [XML track](../xml/xml_01_beginner_detailed.md).

Reusable WebSquare thành phần (component / 컴포넌트) kiến trúc (architecture / 아키텍처): [08 — Reusable Architecture, UDC & Common Modules](08_reusable_architecture_udc_common_modules.md).

Form/i18n/khả năng tiếp cận (accessibility / 접근성) boundaries: [09 — Forms, Validation, Internationalization & Accessibility](09_forms_validation_i18n_accessibility.md).

Rendering/lazy/thời gian tồn tại (lifetime / 수명): [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md).

Testing/testability/regression: [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).

Bản dựng (build / 빌드)/cấu hình (config / 설정)/triển khai (deployment / 배포): [12 — Build, Configuration, Deployment & Environment Reasoning](12_build_config_deployment.md).

Nếu backend là Java/Spring, giao dịch (transaction / 트랜잭션), authorization và API tính đúng đắn (correctness / 정확성) không thuộc WebSquare. Hãy cross-reference chuẩn gốc (canonical / 정본) backend docs trong `10_backend/` thay vì đưa máy chủ (server / 서버) ngữ nghĩa (semantics / 의미론) vào UI thư viện (library / 라이브러리).

## 16. Practical capstone

Thư viện (library / 라이브러리) được coi là thực sự “học xong” khi bạn có thể tự dựng và giải thích một luồng (flow / 흐름):

```text
Search form
→ dmSearch
→ sbmSearch
→ dlUser
→ GridView
→ edit rows
→ row status
→ validate changed rows
→ sbmSave
→ server result
→ refresh
→ popup detail trong WFrame/Scope
```

Sau đó nâng capstone thêm ba năng lực (capability / 역량):

```text
EmployeePicker UDC
→ public property/method/event
→ không biết internal ID của parent

Multilingual form
→ language pack
→ keyboard/focus flow
→ server validation error mapping

Lazy TabControl
→ tab content WFrame
→ first-use data load
→ stale-response guard
→ cleanup timer/listener khi close
```

Tiếp theo biến luồng (flow / 흐름) thành regression bằng chứng (evidence / 증거):

```text
pure validation test
→ DataList/row-status test
→ UDC contract test
→ nested WFrame integration
→ E2E critical path
→ race/fault injection
→ repeated lifecycle memory test
```

Cuối cùng đưa chính sản phẩm tạo ra (artifact / 산출물) đã kiểm thử (test / 테스트) qua bản phát hành (release / 릴리스) chuỗi xử lý (pipeline / 파이프라인):

```text
source commit
→ clean W-Pack build
→ artifact/build identity
→ UAT smoke/regression
→ promote cùng artifact
→ production smoke
→ verify browser artifact/config
→ observe/rollback nếu cần
```

Phải gỡ lỗi (debug / 디버그) được ít nhất tám fault injection:

Máy chủ (server / 서버) phản hồi (response / 응답) chậm 5 giây.

Người dùng (user / 사용자) double-click Save.

Popup được mở/đóng 30 lần và có timer cố ý không cleanup.

Tab preload gọi hàm (function / 함수) có thao tác Grid trước khi kết xuất (render / 렌더링).

Ngôn ngữ (language / 언어) pack thiếu một key và English văn bản (text / 텍스트) dài làm vỡ bố cục (layout / 레이아웃).

UDC bị dùng trong một parent topology khác và hidden phụ thuộc (dependency / 의존성) bị lộ.

Phản hồi (response / 응답) của tìm kiếm (search / 검색) cũ cố tình về sau tìm kiếm (search / 검색) mới.

Môi trường vận hành (production / 운영 환경) cố tình giữ W-Pack sản phẩm tạo ra (artifact / 산출물)/bộ nhớ đệm (cache / 캐시) cũ dù nguồn (source / 소스) lần ghi nhận (commit / 커밋) đã thay đổi.

Nếu bạn có thể chỉ ra dạng thất bại (failure mode / 실패 모드), bằng chứng (evidence / 증거), kiểm thử (test / 테스트) ranh giới (boundary / 경계) và fix ranh giới (boundary / 경계) cho các trường hợp (case / 사례) này, kiến thức đã chuyển từ “biết API” sang “lập luận (reasoning / 추론) được hệ thống và delivery chuỗi xử lý (pipeline / 파이프라인)”.

## 17. Coverage status của thư viện (library / 라이브러리)

Thư viện (library / 라이브러리) hiện bao phủ các trục chuẩn gốc (canonical / 정본) cần thiết cho WebSquare JavaScript enterprise development: nền tảng (platform / 플랫폼)/thời gian chạy (runtime / 런타임), page mô hình (model / 모델), thành phần (component / 컴포넌트) API, events, binding, DataCollection, DataMap/DataList/LinkedDataList, row status, Submission, async communication, WFrame, phạm vi (scope / 범위), `scwin`, `$p`, popup, SPA, GridView/CRUD, reusable UDC/dùng chung (common / 공통) kiến trúc (architecture / 아키텍처), đầu vào (input / 입력)/kiểm tra hợp lệ (validation / 검증), internationalization, khả năng tiếp cận (accessibility / 접근성), tệp (file / 파일)/Excel trust ranh giới (boundary / 경계), eager/lazy/preload rendering, tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), testing/testability, deterministic async regression, CI ranh giới (boundary / 경계), W-Pack/bản dựng (build / 빌드) provenance, máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (configuration / 구성), triển khai (deployment / 배포)/bộ nhớ đệm (cache / 캐시)/quay lui (rollback / 롤백), hiệu năng (performance / 성능), bộ nhớ (memory / 메모리), bảo mật (security / 보안), khả năng quan sát (observability / 관측 가능성), legacy patterns và di chuyển (migration / 마이그레이션) lập luận (reasoning / 추론).

Những thứ cố ý **không** biến thành chapter riêng gồm danh sách toàn bộ thuộc tính (property / 속성) của từng thành phần (component / 컴포넌트), exhaustive API tham chiếu (reference / 참조), mọi option GridView, mọi cấu hình (config / 설정) tag, mọi UDC thuộc tính (property / 속성) lược đồ (schema / 스키마), một testing khung phần mềm (framework / 프레임워크) tutorial và mọi bản dựng (build / 빌드) bản phát hành (release / 릴리스) ghi chú (note / 노트). Các nội dung đó thay đổi theo engine bản dựng (build / 빌드)/toolchain và đã có official tham chiếu (reference / 참조) hoặc tài liệu riêng của công cụ (tool / 도구). thư viện (library / 라이브러리) này ưu tiên mô hình tư duy (mental model / 사고 모델) giúp bạn đọc tham chiếu (reference / 참조) đúng và áp dụng an toàn.

Coverage cũng không coi “đã nhắc tên tính năng (feature / 기능)” là đủ. Một topic chỉ được xem là đã học khi người đọc giải thích được đơn vị sở hữu (owner / 오너) của trạng thái (state / 상태), vòng đời (lifecycle / 생명주기) prerequisite, trust ranh giới (boundary / 경계), observable đặc tả hợp đồng (contract / 계약), sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) provenance, dạng thất bại (failure mode / 실패 모드) và bằng chứng (evidence / 증거) cần lấy khi hành vi (behavior / 동작) sai.

> **Bàn giao:** Sau **17. Coverage status của thư viện (library / 라이브러리)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 platform runtime page model](./01_platform_runtime_page_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.

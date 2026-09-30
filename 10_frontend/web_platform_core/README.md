# Nền tảng Web (web platform / 웹 플랫폼) cốt lõi (core / 핵심)

> **Mạch đọc:** Đọc **Nền tảng Web (web platform / 웹 플랫폼) cốt lõi (core / 핵심)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) conceptual spine** sang **Cách đọc**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

`web_platform_core/` là đơn vị sở hữu (owner / 오너) chuẩn gốc (canonical / 정본) cho các concept đứng trước một
khung phần mềm (framework / 프레임워크) frontend cụ thể. Lớp này trả lời trình duyệt (browser / 브라우저) thực thi document, style,
script, đầu vào (input / 입력) và mạng (network / 네트워크) như thế nào; `html/`, `css/`, `javascript/`, React và
WebSquare sau đó hiện thực hoặc mở rộng các concept đó ở những ranh giới (boundary / 경계) riêng.

## Chuẩn gốc (canonical / 정본) conceptual spine
Phần “Chuẩn gốc (canonical / 정본) conceptual spine” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Web Platform
    ↓
HTML / CSS / JavaScript
    ↓
Browser runtime
    ↓
Rendering / events / networking
    ↓
Accessibility / security / performance
    ↓
Frameworks
├── React
└── WebSquare
```

Sơ đồ này là phụ thuộc (dependency / 의존성) map, không phải một chuỗi xử lý (pipeline / 파이프라인) chạy đúng một lần. HTML,
CSS và JavaScript là các thành phần nguyên thủy (primitive / 기본 요소)/ngôn ngữ (language / 언어) surface được trình duyệt (browser / 브라우저) host thực thi;
trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) nối chúng với document, vòng lặp sự kiện (event loop / 이벤트 루프), rendering và mạng (network / 네트워크).
khả năng tiếp cận (accessibility / 접근성),
bảo mật (security / 보안) và hiệu năng (performance / 성능) là tính đúng đắn (correctness / 정확성) các ràng buộc (constraints / 제약조건들) xuyên các bước. React và
WebSquare tổ chức những thành phần nguyên thủy (primitive / 기본 요소) này thành mô hình ứng dụng (application model / 애플리케이션 모델) riêng nhưng
không thay đổi ngữ nghĩa (semantics / 의미론) của HTML, DOM, CSS hoặc trình duyệt (browser / 브라우저) ranh giới bảo mật (security boundary / 보안 경계).


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) conceptual spine**, ta sang **Cách đọc** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách đọc

1. Đọc [browser runtime và lifecycle](./01_browser_runtime_and_lifecycle.md) để
   phân biệt ECMAScript ngôn ngữ (language / 언어) với host môi trường (environment / 환경), realm, document,
   vòng lặp sự kiện (event loop / 이벤트 루프) và rendering opportunity.
2. Đọc [rendering pipeline](./02_rendering_pipeline.md) để lần từ phản hồi (response / 응답) và
   markup đến DOM/CSSOM, cascade, bố cục (layout / 레이아웃), paint và composite.
3. Đọc [events, networking và state](./03_events_networking_and_state.md) để
   nối người dùng (user / 사용자) intent/mạng (network / 네트워크) phản hồi (response / 응답) với thứ tự (ordering / 순서), cancellation và quyền sở hữu trạng thái (state ownership / 상태 소유권).
4. Đọc [accessibility, security và performance](./04_accessibility_security_performance.md)
   như các bất biến (invariant / 불변식) phải giữ, không phải lớp đánh bóng sau cùng.
5. Đọc [framework boundary](./05_framework_boundary_react_websquare.md) trước
   khi đi vào [React](../react/00_index.md) hoặc [WebSquare](../websquare/README.md).

[`00_web_platform_model.md`](./00_web_platform_model.md) là bản đồ nhanh của
toàn bộ lớp cốt lõi (core / 핵심). Sau vòng đọc này, chọn nhánh học (track / 트랙) hiện thực (implementation / 구현) phù hợp:

- [HTML](../html/html_01_beginner_to_senior_detailed.md) sở hữu document,
  ngữ nghĩa (semantics / 의미론), parser và forms.
- [CSS](../css/CSS_Beginner_to_Senior_2026.md) sở hữu cascade, bố cục (layout / 레이아웃) và
  authoring/rendering detail.
- [JavaScript](../javascript/javascript_beginner_rebuilt.md) sở hữu ngôn ngữ (language / 언어),
  mô hình thực thi (execution model / 실행 모델), DOM/events, async và trình duyệt (browser / 브라우저) APIs.
- [React](../react/00_index.md) và [WebSquare](../websquare/README.md) sở hữu
  khung phần mềm (framework / 프레임워크) vòng đời (lifecycle / 생명주기), composition, trạng thái (state / 상태) và môi trường vận hành (production / 운영 환경) tích hợp (integration / 통합).


> **Chuyển mạch:** Từ **Cách đọc**, ta sang **ranh giới (boundary / 경계) và nguyên tắc quyền sở hữu (ownership / 소유권)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ranh giới (boundary / 경계) và nguyên tắc quyền sở hữu (ownership / 소유권)

Cốt lõi (core / 핵심) không sao chép toàn bộ giáo trình HTML/CSS/JavaScript hoặc khung phần mềm (framework / 프레임워크). Một
chapter ở đây chỉ giữ mô hình tư duy (mental model / 사고 모델) và bất biến (invariant / 불변식) cần dùng để nối các nhánh học (track / 트랙):

- trình duyệt (browser / 브라우저) ngữ nghĩa (semantics / 의미론) là đơn vị sở hữu (owner / 오너) của parser, DOM, CSSOM, sự kiện (event / 이벤트) dispatch, fetch,
  lưu trữ (storage / 저장소), cây khả năng tiếp cận (accessibility tree / 접근성 트리) và ranh giới bảo mật (security boundary / 보안 경계);
- khung phần mềm (framework / 프레임워크) là đơn vị sở hữu (owner / 오너) của reconciliation/vòng đời (lifecycle / 생명주기)/thành phần (component / 컴포넌트) trạng thái (state / 상태) hoặc page,
  phạm vi (scope / 범위), DataCollection và Submission;
- ứng dụng (application / 애플리케이션)/backend là đơn vị sở hữu (owner / 오너) của nghiệp vụ (business / 비즈니스) đặc tả hợp đồng (contract / 계약), authorization và dữ
  liệu máy chủ (server / 서버); UI kiểm tra hợp lệ (validation / 검증) không thay thế máy chủ (server / 서버) authorization;
- bản dựng (build / 빌드)/triển khai (deployment / 배포) là ranh giới (boundary / 경계) với DevOps: frontend giữ sản phẩm tạo ra (artifact / 산출물)/bộ nhớ đệm (cache / 캐시)/thời gian chạy (runtime / 런타임)
  bằng chứng (evidence / 증거) ở mức cần thiết để gỡ lỗi (debug / 디버그) trình duyệt (browser / 브라우저) đang chạy gì.

Khi một khái niệm đã có đơn vị sở hữu (owner / 오너) sâu hơn, cốt lõi (core / 핵심) link tới đơn vị sở hữu (owner / 오너) đó thay vì tạo bản
sao. Khi một khung phần mềm (framework / 프레임워크) có hành vi (behavior / 동작) riêng, luôn tách trình duyệt (browser / 브라우저) thành phần nguyên thủy (primitive / 기본 요소),
khung phần mềm (framework / 프레임워크) lớp trừu tượng (abstraction / 추상화) và đặc tả ứng dụng (application contract / 애플리케이션 계약) trước khi kết luận nguyên nhân.

> **Bàn giao:** Sau **ranh giới (boundary / 경계) và nguyên tắc quyền sở hữu (ownership / 소유권)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 web platform model](./00_web_platform_model.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.

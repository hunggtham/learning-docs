# Web Platform Core

`web_platform_core/` là owner canonical cho các concept đứng trước một
framework frontend cụ thể. Lớp này trả lời browser thực thi document, style,
script, input và network như thế nào; `html/`, `css/`, `javascript/`, React và
WebSquare sau đó hiện thực hoặc mở rộng các concept đó ở những boundary riêng.

## Canonical conceptual spine

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

Sơ đồ này là dependency map, không phải một pipeline chạy đúng một lần. HTML,
CSS và JavaScript là các primitive/language surface được browser host thực thi;
browser runtime nối chúng với document, event loop, rendering và network.
Accessibility,
security và performance là correctness constraints xuyên các bước. React và
WebSquare tổ chức những primitive này thành application model riêng nhưng
không thay đổi semantics của HTML, DOM, CSS hoặc browser security boundary.

## Cách đọc

1. Đọc [browser runtime và lifecycle](./01_browser_runtime_and_lifecycle.md) để
   phân biệt ECMAScript language với host environment, realm, document,
   event loop và rendering opportunity.
2. Đọc [rendering pipeline](./02_rendering_pipeline.md) để lần từ response và
   markup đến DOM/CSSOM, cascade, layout, paint và composite.
3. Đọc [events, networking và state](./03_events_networking_and_state.md) để
   nối user intent/network response với ordering, cancellation và state
   ownership.
4. Đọc [accessibility, security và performance](./04_accessibility_security_performance.md)
   như các invariant phải giữ, không phải lớp đánh bóng sau cùng.
5. Đọc [framework boundary](./05_framework_boundary_react_websquare.md) trước
   khi đi vào [React](../react/00_index.md) hoặc [WebSquare](../websquare/README.md).

[`00_web_platform_model.md`](./00_web_platform_model.md) là bản đồ nhanh của
toàn bộ lớp core. Sau vòng đọc này, chọn track implementation phù hợp:

- [HTML](../html/html_01_beginner_to_senior_detailed.md) sở hữu document,
  semantics, parser và forms.
- [CSS](../css/CSS_Beginner_to_Senior_2026.md) sở hữu cascade, layout và
  authoring/rendering detail.
- [JavaScript](../javascript/javascript_beginner_rebuilt.md) sở hữu language,
  execution model, DOM/events, async và browser APIs.
- [React](../react/00_index.md) và [WebSquare](../websquare/README.md) sở hữu
  framework lifecycle, composition, state và production integration.

## Boundary và nguyên tắc ownership

Core không sao chép toàn bộ giáo trình HTML/CSS/JavaScript hoặc framework. Một
chapter ở đây chỉ giữ mental model và invariant cần dùng để nối các track:

- browser semantics là owner của parser, DOM, CSSOM, event dispatch, fetch,
  storage, accessibility tree và security boundary;
- framework là owner của reconciliation/lifecycle/component state hoặc page,
  scope, DataCollection và Submission;
- application/backend là owner của business contract, authorization và dữ
  liệu server; UI validation không thay thế server authorization;
- build/deployment là boundary với DevOps: frontend giữ artifact/cache/runtime
  evidence ở mức cần thiết để debug browser đang chạy gì.

Khi một khái niệm đã có owner sâu hơn, core link tới owner đó thay vì tạo bản
sao. Khi một framework có behavior riêng, luôn tách browser primitive,
framework abstraction và application contract trước khi kết luận nguyên nhân.

# Accessibility, security và performance như correctness

Ba concern này không phải checklist cuối sprint. Chúng là constraint của cùng
một platform contract: người dùng phải có thể hiểu/tương tác, dữ liệu không
được vượt trust boundary sai, và work phải nằm trong budget có thể đo.

## Accessibility

Native semantics, accessible name, focus order, keyboard operation, error
announcement, live region và reduced-motion preference tạo nên public behavior.
ARIA chỉ bổ sung khi native element không đủ; nó không sửa một document model
sai. Conditional rendering, portal, popup, WFrame, lazy loading và hydration
đều phải giữ semantics và focus restoration.

## Security

Tách validation, encoding, sanitization và authorization. URL/HTML/storage/
`postMessage`/iframe/WebView bridge là untrusted input cho tới khi boundary
được xác định. XSS, CSRF, CORS, cookie/token, CSP/Trusted Types và dependency
supply chain có failure mode khác nhau; UI validation không thay server check.

## Performance

Đo theo causal chain: DNS/connect/response → parse/script → style/layout/paint
→ input latency → memory/bundle/cache. Trace phải ghi browser, build ID,
network condition và workload; budget nên có guard ở test hoặc release gate.

Các track implementation cung cấp chi tiết: [HTML accessibility/security](../html/html_02_master_implementation_detailed.md),
[JavaScript production](../javascript/javascript_master_supplement_detailed.md),
[WebSquare accessibility](../websquare/09_forms_validation_i18n_accessibility.md)
và [WebSquare profiling](../websquare/24_event_semantics_performance_profiling.md).
